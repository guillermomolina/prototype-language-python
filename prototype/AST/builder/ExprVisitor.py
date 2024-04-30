from prototype.parser.PrototypeParser import PrototypeParser
from prototype.parser.PrototypeParserVisitor import PrototypeParserVisitor

from prototype import AST
from prototype.AST.ast import MemoryContext

class ExprVisitorMixin(PrototypeParserVisitor):

    #
    # Tests (comparisons)
    #

    def visitComparison(self, ctx:PrototypeParser.RelationalExpressionContext):
        left  = self.visit(ctx.test(0))
        right = self.visit(ctx.test(1))
        op = ctx.comp_op().getText()

        firstSymbolType = ctx.comp_op().children[0].symbol.type

        if firstSymbolType == PrototypeParser.IN:
            op = AST.expr.Compare.Op.IN
        elif firstSymbolType == PrototypeParser.IS:
            op = AST.expr.Compare.Op.IS

        if len(ctx.comp_op().children) == 2:
            secondSymbolType = ctx.comp_op().children[1].symbol.type

            if firstSymbolType == PrototypeParser.NOT and secondSymbolType == PrototypeParser.IN:
                op = AST.expr.Compare.Op.NOT_IN
            elif firstSymbolType == PrototypeParser.IS and secondSymbolType == PrototypeParser.NOT:
                op = AST.expr.Compare.Op.IS_NOT
            else:
                raise ValueError("Unexpected binary comparison operation")

        return AST.expr.BinaryComp(left=left, right=right, op=op)

    def visitNotTest(self, ctx:PrototypeParser.NotExpressionContext):
        test = self.visit(ctx.test())
        return AST.expr.UnaryComp(operand=test, op=AST.expr.Compare.Op.NOT)

    def visitAndTest(self, ctx:PrototypeParser.LogicalAndExpressionContext):
        left  = self.visit(ctx.test(0))
        right = self.visit(ctx.test(1))
        return AST.expr.BinaryComp(left=left, right=right, op=AST.expr.Compare.Op.AND)

    def visitOrTest(self, ctx:PrototypeParser.LogicalOrExpressionContext):
        left  = self.visit(ctx.test(0))
        right = self.visit(ctx.test(1))
        return AST.expr.BinaryComp(left=left, right=right, op=AST.expr.Compare.Op.OR)

    #
    # Arithmetic (@expr rule)
    #

    binaryExprTable = {
        PrototypeParser.Plus                 : AST.expr.AddOp,
        PrototypeParser.Minus                : AST.expr.SubOp,
        PrototypeParser.Multiply             : AST.expr.MultOp,
        PrototypeParser.Divide               : AST.expr.DivOp,
        PrototypeParser.Modulus              : AST.expr.ModOp,
        PrototypeParser.LeftShiftArithmetic  : AST.expr.LshiftOp,
        PrototypeParser.RightShiftArithmetic : AST.expr.RshiftOp,
        PrototypeParser.BitAnd               : AST.expr.BitAndOp,
        PrototypeParser.BitXOr               : AST.expr.BitXorOp,
        PrototypeParser.BitOr                : AST.expr.BitOrOp,
    }

    def visitGenericExpr(self, ctx):
        left  = self.visit(ctx.singleExpression(0))
        right = self.visit(ctx.singleExpression(1))

        try:
            return ExprVisitorMixin.binaryExprTable[ctx.op.type](left, right)
        except KeyError:
            raise ValueError("Unexpected op type")

    def visitMulDivMod(self, ctx:PrototypeParser.MultiplicativeExpressionContext):
        return self.visitGenericExpr(ctx)

    def visitAdditiveExpression(self, ctx:PrototypeParser.AdditiveExpressionContext):
        return self.visitGenericExpr(ctx)

    def visitShifts(self, ctx:PrototypeParser.BitShiftExpressionContext):
        return self.visitGenericExpr(ctx)

    def visitBitAnd(self, ctx:PrototypeParser.BitAndExpressionContext):
        return self.visitGenericExpr(ctx)

    def visitBitXor(self, ctx:PrototypeParser.BitXOrExpressionContext):
        return self.visitGenericExpr(ctx)

    def visitBitOr(self, ctx:PrototypeParser.BitOrExpressionContext):
        return self.visitGenericExpr(ctx)

    #
    # Factor rule
    #

    def visitUnaryExpr(self, ctx:PrototypeParser.UnaryMinusExpressionContext):
        operand = ctx.factor().accept(self)
        return AST.expr.UnaryOp(op=ctx.op.text, operand=operand)


    def visitParenExpr(self, ctx:PrototypeParser.ParenthesizedExpressionContext):
        return self.visit(ctx.test())


    def visitAtom(self, ctx:PrototypeParser.LiteralExpressionContext):
        if ctx.NONE() != None:
            return AST.expr.NameConstant('None')
        elif ctx.TRUE() != None:
            return AST.expr.NameConstant('True')
        elif ctx.FALSE() != None:
            return AST.expr.NameConstant('False')

        # Visit other nodes
        return self.visitChildren(ctx)


    #
    # Name access: PlainName, FuncInvoke, SubName
    #

    def nameContextFor(self, ctx):
        if type(ctx.parentCtx) is PrototypeParser.ExprStmtAssignContext or type(ctx.parentCtx) is PrototypeParser.ExprStmtAugmentedContext:
            return MemoryContext.Store
        else:
            return MemoryContext.Load


    def visitPlainName(self, ctx:PrototypeParser.IdentifierExpressionContext):
        context = self.nameContextFor(ctx)
        return AST.expr.Name(id=ctx.NAME().getText(), ctx=context)


    def visitFuncInvoke(self, ctx:PrototypeParser.ArgumentsExpressionContext):
        funcName = self.visit(ctx.nameaccess())
        args = []

        if ctx.arglist() != None:
            for argStmt in ctx.arglist().test():
                arg = self.visit(argStmt)
                if arg != None:
                    args.append(arg)

        return AST.expr.CallExpr(func=funcName, args=args)


    def visitDottedName(self, ctx:PrototypeParser.MemberDotExpressionContext):
        left = self.visit(ctx.nameaccess())
        attrName = ctx.NAME().getText()
        return AST.stmt.Attribute(value=left, attr=attrName, ctx=MemoryContext.Load)


    def visitSubName(self, ctx:PrototypeParser.MemberIndexExpressionContext):
        leftNode = self.visit(ctx.nameaccess())
        subscript = self.visit(ctx.subscript())

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

    # def visitListMaker(self, ctx:PrototypeParser.ListMakerContext):
    #     if ctx.testlist_comp() == None:
    #         return AST.expr.ListContainer([])

    #     return AST.expr.ListContainer(self.visit(ctx.testlist_comp()))

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

    def visitNumericLiteral(self, ctx:PrototypeParser.NumericLiteralContext):

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

    def visitString(self, ctx:PrototypeParser.TemplateStringLiteralContext):
        node = ctx.STRING_LITERAL()
        if node != None:
            text = node.getText()[1:-1]
            return AST.expr.Str(text)

        raise ValueError()
