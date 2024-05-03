from prototype.parser.PrototypeParser import PrototypeParser
from prototype.parser.PrototypeParserVisitor import PrototypeParserVisitor

from prototype import ast
from prototype.ast.base import MemoryContext


class ExprVisitorMixin(PrototypeParserVisitor):

    #
    # Tests (comparisons)
    #

    def visitRelationalExpression(self, ctx: PrototypeParser.RelationalExpressionContext):
        left = self.visit(ctx.singleExpression(0))
        right = self.visit(ctx.singleExpression(1))
        op = ctx.op.text

        return ast.expr.BinaryCompNode(left=left, right=right, op=op)

    def visitNotExpression(self, ctx: PrototypeParser.NotExpressionContext):
        test = self.visit(ctx.test())
        return ast.expr.UnaryCompNode(operand=test, op=ast.expr.CompareNode.Op.NOT)

    def visitLogicalAndExpression(self, ctx: PrototypeParser.LogicalAndExpressionContext):
        left = self.visit(ctx.test(0))
        right = self.visit(ctx.test(1))
        return ast.expr.BinaryCompNode(left=left, right=right, op=ast.expr.CompareNode.Op.AND)

    def visitLogicalOrExpression(self, ctx: PrototypeParser.LogicalOrExpressionContext):
        left = self.visit(ctx.test(0))
        right = self.visit(ctx.test(1))
        return ast.expr.BinaryCompNode(left=left, right=right, op=ast.expr.CompareNode.Op.OR)

    #
    # Arithmetic (@expr rule)
    #

    binaryExprTable = {
        PrototypeParser.Plus: ast.expr.AddOpNode,
        PrototypeParser.Minus: ast.expr.SubOpNode,
        PrototypeParser.Multiply: ast.expr.MultOpNode,
        PrototypeParser.Divide: ast.expr.DivOpNode,
        PrototypeParser.Modulus: ast.expr.ModOpNode,
        PrototypeParser.LeftShiftArithmetic: ast.expr.LShiftOpNode,
        PrototypeParser.RightShiftArithmetic: ast.expr.RShiftOpNode,
        PrototypeParser.BitAnd: ast.expr.BitAndOpNode,
        PrototypeParser.BitXOr: ast.expr.BitXorOpNode,
        PrototypeParser.BitOr: ast.expr.BitOrOpNode,
    }

    def visitGenericExpr(self, ctx):
        left = self.visit(ctx.singleExpression(0))
        right = self.visit(ctx.singleExpression(1))

        try:
            return ExprVisitorMixin.binaryExprTable[ctx.op.type](left, right)
        except KeyError:
            raise ValueError("Unexpected op type")

    def visitMultiplicativeExpression(self, ctx: PrototypeParser.MultiplicativeExpressionContext):
        return self.visitGenericExpr(ctx)

    def visitAdditiveExpression(self, ctx: PrototypeParser.AdditiveExpressionContext):
        return self.visitGenericExpr(ctx)

    def visitBitShiftExpression(self, ctx: PrototypeParser.BitShiftExpressionContext):
        return self.visitGenericExpr(ctx)

    def visitBitAndExpression(self, ctx: PrototypeParser.BitAndExpressionContext):
        return self.visitGenericExpr(ctx)

    def visitBitXOrExpression(self, ctx: PrototypeParser.BitXOrExpressionContext):
        return self.visitGenericExpr(ctx)

    def visitBitOrExpression(self, ctx: PrototypeParser.BitOrExpressionContext):
        return self.visitGenericExpr(ctx)

    #
    # Factor rule
    #

    def visitUnaryExpr(self, ctx: PrototypeParser.UnaryMinusExpressionContext):
        operand = ctx.factor().accept(self)
        return ast.expr.UnaryOpNode(op=ctx.op.text, operand=operand)

    def visitParenthesizedExpression(self, ctx: PrototypeParser.ParenthesizedExpressionContext):
        return self.visit(ctx.expressionSequence())

    def visitLiteral(self, ctx: PrototypeParser.LiteralContext):
        if ctx.NullLiteral() is not None:
            return ast.expr.NameConstantNode('null')
        
        if ctx.BooleanLiteral() is not None:
            return ast.expr.NameConstantNode(ctx.BooleanLiteral().getText())

        if ctx.StringLiteral() is not None:
            text = ctx.StringLiteral().getText()[1:-1]
            return ast.expr.StringNode(text)

        if ctx.RegularExpressionLiteral() is not None:
            raise NotImplementedError()

        # Visit other nodes
        return self.visitChildren(ctx)

    #
    # Assignment: AssignmentExpression, AssignmentOperatorExpression
    #

    def visitAssignmentExpression(self, ctx: PrototypeParser.AssignmentExpressionContext):
        name = self.visit(ctx.singleExpression(0))
        value = self.visit(ctx.singleExpression(1))

        return ast.stmt.AssignStmt(target=name, value=value)

    def visitAssignmentOperatorExpression(self, ctx: PrototypeParser.AssignmentOperatorExpressionContext):
        name = self.visit(ctx.singleExpression(0))
        value = self.visit(ctx.singleExpression(1))
        op = ctx.assignmentOperator().getText()

        return ast.stmt.AugAssignStmt(name=name, value=value, op=op)

    #
    # NameNode access: Identifier, ArgumentsExpression, SubName
    #

    def nameContextFor(self, ctx):
        parentContext = ctx.parentCtx.parentCtx
        if type(parentContext) is PrototypeParser.AssignmentExpressionContext or type(parentContext) is PrototypeParser.AssignmentOperatorExpressionContext:
            return MemoryContext.Store
        else:
            return MemoryContext.Load

    def visitIdentifier(self, ctx: PrototypeParser.IdentifierContext):
        context = self.nameContextFor(ctx)
        return ast.expr.NameNode(id=ctx.getText(), ctx=context)

    def visitArgumentsExpression(self, ctx: PrototypeParser.ArgumentsExpressionContext):
        funcName = self.visit(ctx.singleExpression())
        args = []

        for argStmt in ctx.arguments().argument():
            arg = self.visit(argStmt)
            if arg != None:
                args.append(arg)

        return ast.expr.CallExprNode(func=funcName, args=args)

    def visitMemberDotExpression(self, ctx: PrototypeParser.MemberDotExpressionContext):
        left = self.visit(ctx.singleExpression())
        attrName = ctx.identifierName().getText()
        return ast.stmt.PropertyNode(value=left, attr=attrName, ctx=MemoryContext.Load)

    def visitMemberIndexExpression(self, ctx: PrototypeParser.MemberIndexExpressionContext):
        leftNode = self.visit(ctx.singleExpression())
        if len(ctx.expressionSequence().singleExpression()) > 1:
            raise NotImplementedError()
        subscript = ast.stmt.IndexNode(self.visit(ctx.expressionSequence().singleExpression(0)))

        context = self.nameContextFor(ctx)

        return ast.stmt.SubscriptNode(value=leftNode, slice=subscript, ctx=context)

    #
    # IndexNode and slice operations
    #

    # def visitSubscriptIndex(self, ctx:PrototypeParser.SubscriptIndexContext):
    #     test = self.visit(ctx.test())
    #     return ast.stmt.IndexNode(value=test)

    # def visitSubscriptSlice(self, ctx:PrototypeParser.SubscriptSliceContext):
    #     lower = upper = None

    #     if ctx.lower != None:
    #         lower = self.visit(ctx.lower)

    #     if ctx.upper != None:
    #         upper = self.visit(ctx.upper)

    #     return ast.stmt.SliceNode(lower=lower, upper=upper, step=None)
    #
    # Collection definitions
    #

    # def visitDictorsetmaker(self, ctx:PrototypeParser.DictorsetmakerContext):
    #     if ctx.dictormaker() != None:
    #         return self.visit(ctx.dictormaker())

    #     if ctx.setmaker() != None:
    #         return self.visit(ctx.setmaker())

    # def visitDictMaker(self, ctx:PrototypeParser.DictMakerContext):
    #     if ctx.dictorsetmaker() != None:
    #         return self.visit(ctx.dictorsetmaker())

    #     return ast.expr.DictContainerNode({})

    # def visitSetmaker(self, ctx:PrototypeParser.SetmakerContext):
    #     result = set({})
    #     for test in ctx.test():
    #         result.add(self.visit(test))
    #     return ast.expr.SetContainerNode(result)

    # def visitDictormaker(self, ctx:PrototypeParser.DictormakerContext):
    #     if ctx.test(0) != None:
    #         left = self.visit(ctx.test(0))
    #         right = self.visit(ctx.test(1))
    #         return ast.expr.DictContainerNode({left : right})

    #     if ctx.dictormaker(0) != None:
    #         left = self.visit(ctx.dictormaker(0))
    #         right = self.visit(ctx.dictormaker(1))

    #         result = left.copy()
    #         result.update(right)

    #         if type(result) is not ast.expr.DictContainerNode:
    #             return ast.expr.DictContainerNode(result)
    #         else:
    #             return result

    def visitObjectLiteral(self, ctx:PrototypeParser.ObjectLiteralContext):
        result = ast.expr.DictContainerNode({})

        for propertyAssignment in ctx.propertyAssignment():
            right = self.visit(propertyAssignment)
            result = result.copy()
            result.update(right)

        return result

    def visitPropertyExpressionAssignment(self, ctx:PrototypeParser.PropertyExpressionAssignmentContext):
        left = self.visit(ctx.propertyName())
        right = self.visit(ctx.singleExpression())
        return ast.expr.DictContainerNode({left : right})

    def visitPropertyName(self, ctx:PrototypeParser.PropertyNameContext):
        if ctx.StringLiteral() is not None:
            text = ctx.StringLiteral().getText()[1:-1]
            return ast.expr.StringNode(text)
        
        if ctx.numericLiteral() is not None:
            return self.visit(ctx.numericLiteral())
        
        raise NotImplementedError()

    def visitArrayLiteral(self, ctx:PrototypeParser.ArrayLiteralContext):
        elements = []

        for arrayElement in ctx.elementList().arrayElement():
            elements.append(self.visit(arrayElement))

        return ast.expr.ListContainerNode(elements)

    # def visitTupleMaker(self, ctx:PrototypeParser.TupleMakerContext):
    #     if ctx.testlist_comp() == None:
    #         return ast.expr.TupleContainerNode(())

    #     return ast.expr.TupleContainerNode(tuple(self.visit(ctx.testlist_comp())))

    # def visitTestlist_comp(self, ctx:PrototypeParser.Testlist_compContext):
    #     if ctx.test() != None:
    #         return [self.visit(ctx.test())]

    #     if ctx.testlist_comp(1) == None:
    #         return self.visit(ctx.testlist_comp(0))

    #     left = self.visit(ctx.testlist_comp(0))
    #     right = self.visit(ctx.testlist_comp(1))
    #     result = []

    #     if type(left) is list:
    #         result += left
    #     else:
    #         result.append(left)

    #     if type(right) is list:
    #         result += right
    #     else:
    #         result.append(right)

    #     return result

    #
    # Strings and numbers
    #

    def visitNumericLiteral(self, ctx: PrototypeParser.NumericLiteralContext):

        if ctx.DecimalLiteral() != None:
            try:
                number = int(ctx.DecimalLiteral().getText())
                return ast.expr.NumberNode(number)
            except ValueError:
                number = float(ctx.DecimalLiteral().getText())
                return ast.expr.NumberNode(number)

        elif ctx.HexIntegerLiteral() != None:
            hex = int(ctx.HexIntegerLiteral().getText(), 16)
            return ast.expr.NumberNode(hex)

        elif ctx.BinaryIntegerLiteral() != None:
            bin = int(ctx.BinaryIntegerLiteral().getText(), 2)
            return ast.expr.NumberNode(bin)

        elif ctx.OctalIntegerLiteral() != None:
            oct = int(ctx.OctalIntegerLiteral().getText(), 8)
            return ast.expr.NumberNode(oct)

        elif ctx.OctalIntegerLiteral2() != None:
            oct = int(ctx.OctalIntegerLiteral2().getText(), 8)
            return ast.expr.NumberNode(oct)

        raise ValueError()