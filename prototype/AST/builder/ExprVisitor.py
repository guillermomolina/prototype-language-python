from prototype.parser.PrototypeParser import PrototypeParser
from prototype.parser.PrototypeParserVisitor import PrototypeParserVisitor

from prototype import AST
from prototype.AST.ast import MemoryContext


class ExprVisitorMixin(PrototypeParserVisitor):

    #
    # Tests (comparisons)
    #

    def visitRelationalExpression(self, ctx: PrototypeParser.RelationalExpressionContext):
        left = self.visit(ctx.singleExpression(0))
        right = self.visit(ctx.singleExpression(1))
        op = ctx.op.text

        return AST.expr.BinaryComp(left=left, right=right, op=op)

    def visitNotExpression(self, ctx: PrototypeParser.NotExpressionContext):
        test = self.visit(ctx.test())
        return AST.expr.UnaryComp(operand=test, op=AST.expr.Compare.Op.NOT)

    def visitLogicalAndExpression(self, ctx: PrototypeParser.LogicalAndExpressionContext):
        left = self.visit(ctx.test(0))
        right = self.visit(ctx.test(1))
        return AST.expr.BinaryComp(left=left, right=right, op=AST.expr.Compare.Op.AND)

    def visitLogicalOrExpression(self, ctx: PrototypeParser.LogicalOrExpressionContext):
        left = self.visit(ctx.test(0))
        right = self.visit(ctx.test(1))
        return AST.expr.BinaryComp(left=left, right=right, op=AST.expr.Compare.Op.OR)

    #
    # Arithmetic (@expr rule)
    #

    binaryExprTable = {
        PrototypeParser.Plus: AST.expr.AddOp,
        PrototypeParser.Minus: AST.expr.SubOp,
        PrototypeParser.Multiply: AST.expr.MultOp,
        PrototypeParser.Divide: AST.expr.DivOp,
        PrototypeParser.Modulus: AST.expr.ModOp,
        PrototypeParser.LeftShiftArithmetic: AST.expr.LshiftOp,
        PrototypeParser.RightShiftArithmetic: AST.expr.RshiftOp,
        PrototypeParser.BitAnd: AST.expr.BitAndOp,
        PrototypeParser.BitXOr: AST.expr.BitXorOp,
        PrototypeParser.BitOr: AST.expr.BitOrOp,
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
        return AST.expr.UnaryOp(op=ctx.op.text, operand=operand)

    def visitParenthesizedExpression(self, ctx: PrototypeParser.ParenthesizedExpressionContext):
        return self.visit(ctx.expressionSequence())

    def visitLiteral(self, ctx: PrototypeParser.LiteralContext):
        if ctx.NullLiteral() is not None:
            return AST.expr.NameConstant('null')
        
        if ctx.BooleanLiteral() is not None:
            return AST.expr.NameConstant(ctx.BooleanLiteral().getText())

        if ctx.StringLiteral() is not None:
            text = ctx.StringLiteral().getText()[1:-1]
            return AST.expr.Str(text)

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

        return AST.stmt.AssignStmt(target=name, value=value)

    def visitAssignmentOperatorExpression(self, ctx: PrototypeParser.AssignmentOperatorExpressionContext):
        name = self.visit(ctx.singleExpression(0))
        value = self.visit(ctx.singleExpression(1))
        op = ctx.assignmentOperator().getText()

        return AST.stmt.AugAssignStmt(name=name, value=value, op=op)

    #
    # Name access: Identifier, ArgumentsExpression, SubName
    #

    def nameContextFor(self, ctx):
        parentContext = ctx.parentCtx.parentCtx
        if type(parentContext) is PrototypeParser.AssignmentExpressionContext or type(parentContext) is PrototypeParser.AssignmentOperatorExpressionContext:
            return MemoryContext.Store
        else:
            return MemoryContext.Load

    def visitIdentifier(self, ctx: PrototypeParser.IdentifierContext):
        context = self.nameContextFor(ctx)
        return AST.expr.Name(id=ctx.getText(), ctx=context)

    def visitArgumentsExpression(self, ctx: PrototypeParser.ArgumentsExpressionContext):
        funcName = self.visit(ctx.singleExpression())
        args = []

        for argStmt in ctx.arguments().argument():
            arg = self.visit(argStmt)
            if arg != None:
                args.append(arg)

        return AST.expr.CallExpr(func=funcName, args=args)

    def visitMemberDotExpression(self, ctx: PrototypeParser.MemberDotExpressionContext):
        left = self.visit(ctx.singleExpression())
        attrName = ctx.identifierName().getText()
        return AST.stmt.Attribute(value=left, attr=attrName, ctx=MemoryContext.Load)

    def visitMemberIndexExpression(self, ctx: PrototypeParser.MemberIndexExpressionContext):
        leftNode = self.visit(ctx.singleExpression())
        if len(ctx.expressionSequence().singleExpression()) > 1:
            raise NotImplementedError()
        subscript = AST.stmt.Index(self.visit(ctx.expressionSequence().singleExpression(0)))

        context = self.nameContextFor(ctx)

        return AST.stmt.Subscript(value=leftNode, slice=subscript, ctx=context)

    #
    # Index and slice operations
    #

    # def visitSubscriptIndex(self, ctx:PrototypeParser.SubscriptIndexContext):
    #     test = self.visit(ctx.test())
    #     return AST.stmt.Index(value=test)

    # def visitSubscriptSlice(self, ctx:PrototypeParser.SubscriptSliceContext):
    #     lower = upper = None

    #     if ctx.lower != None:
    #         lower = self.visit(ctx.lower)

    #     if ctx.upper != None:
    #         upper = self.visit(ctx.upper)

    #     return AST.stmt.Slice(lower=lower, upper=upper, step=None)
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

    #     return AST.expr.DictContainer({})

    # def visitSetmaker(self, ctx:PrototypeParser.SetmakerContext):
    #     result = set({})
    #     for test in ctx.test():
    #         result.add(self.visit(test))
    #     return AST.expr.SetContainer(result)

    # def visitDictormaker(self, ctx:PrototypeParser.DictormakerContext):
    #     if ctx.test(0) != None:
    #         left = self.visit(ctx.test(0))
    #         right = self.visit(ctx.test(1))
    #         return AST.expr.DictContainer({left : right})

    #     if ctx.dictormaker(0) != None:
    #         left = self.visit(ctx.dictormaker(0))
    #         right = self.visit(ctx.dictormaker(1))

    #         result = left.copy()
    #         result.update(right)

    #         if type(result) is not AST.expr.DictContainer:
    #             return AST.expr.DictContainer(result)
    #         else:
    #             return result

    def visitObjectLiteral(self, ctx:PrototypeParser.ObjectLiteralContext):
        result = AST.expr.DictContainer({})

        for propertyAssignment in ctx.propertyAssignment():
            right = self.visit(propertyAssignment)
            result = result.copy()
            result.update(right)

        return result

    def visitPropertyExpressionAssignment(self, ctx:PrototypeParser.PropertyExpressionAssignmentContext):
        left = self.visit(ctx.propertyName())
        right = self.visit(ctx.singleExpression())
        return AST.expr.DictContainer({left : right})

    def visitPropertyName(self, ctx:PrototypeParser.PropertyNameContext):
        if ctx.StringLiteral() is not None:
            text = ctx.StringLiteral().getText()[1:-1]
            return AST.expr.Str(text)
        
        if ctx.numericLiteral() is not None:
            return self.visit(ctx.numericLiteral())
        
        raise NotImplementedError()

    def visitArrayLiteral(self, ctx:PrototypeParser.ArrayLiteralContext):
        elements = []

        for arrayElement in ctx.elementList().arrayElement():
            elements.append(self.visit(arrayElement))

        return AST.expr.ListContainer(elements)

    # def visitTupleMaker(self, ctx:PrototypeParser.TupleMakerContext):
    #     if ctx.testlist_comp() == None:
    #         return AST.expr.TupleContainer(())

    #     return AST.expr.TupleContainer(tuple(self.visit(ctx.testlist_comp())))

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
                return AST.expr.Num(number)
            except ValueError:
                number = float(ctx.DecimalLiteral().getText())
                return AST.expr.Num(number)

        elif ctx.HexIntegerLiteral() != None:
            hex = int(ctx.HexIntegerLiteral().getText(), 16)
            return AST.expr.Num(hex)

        elif ctx.BinaryIntegerLiteral() != None:
            bin = int(ctx.BinaryIntegerLiteral().getText(), 2)
            return AST.expr.Num(bin)

        elif ctx.OctalIntegerLiteral() != None:
            oct = int(ctx.OctalIntegerLiteral().getText(), 8)
            return AST.expr.Num(oct)

        elif ctx.OctalIntegerLiteral2() != None:
            oct = int(ctx.OctalIntegerLiteral2().getText(), 8)
            return AST.expr.Num(oct)

        raise ValueError()
