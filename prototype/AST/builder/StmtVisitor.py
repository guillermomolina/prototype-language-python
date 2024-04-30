from prototype.parser.PrototypeParser import PrototypeParser
from prototype.parser.PrototypeParserVisitor import PrototypeParserVisitor

from prototype import AST
from prototype import runtime


class StmtVisitorMixin(PrototypeParserVisitor):

    #
    # Base statements
    #
    def visitBlock(self, ctx:PrototypeParser.BlockContext):
        statements = []

        if ctx.statementList() is not None:
            for stmt in ctx.statementList().statement():
                statement = self.visit(stmt)
                if statement != None:
                    statements.append(statement)

        return statements

    def visitSourceElements(self, ctx:PrototypeParser.SourceElementsContext):
        statements = []

        for sourceElement in ctx.sourceElement():
            statement =  self.visit(sourceElement.statement())
            if statement != None:
                if type(statement) is list:
                    statements += statement
                else:
                    statements.append(statement)

        return statements

    # def visitStatement(self, ctx:PrototypeParser.StatementContext):
    #     statements = []

    #     for smallStmt in ctx.small_stmt():
    #         statement = self.visit(smallStmt)
    #         if statement != None:
    #             statements.append(statement)

    #     return statements

    # #
    # # Base statements
    # #
    # def visitSimple_stmt(self, ctx:PrototypeParser.Simple_stmtContext):
    #     statements = []

    #     for smallStmt in ctx.small_stmt():
    #         statement = self.visit(smallStmt)
    #         if statement != None:
    #             statements.append(statement)

    #     return statements

    # #
    # # Compound statements
    # #
    # def visitSuite(self, ctx:PrototypeParser.SuiteContext):
    #     if ctx.simple_stmt() != None:
    #         return self.visit(ctx.simple_stmt())

    #     statements = []

    #     for stmt in ctx.stmt():
    #         if stmt.simple_stmt() != None:
    #             statements += self.visit(stmt.simple_stmt())
    #         else:
    #             statements.append(self.visit(stmt))

    #     return statements

    def visitIfStatement(self, ctx:PrototypeParser.IfStatementContext):
        test = self.visit(ctx.expressionSequence())
        suite = self.visit(ctx.statement(0))
        orelse = []

        if ctx.Else() is not None:
            orelse = self.visit(ctx.statement(1))

        return AST.stmt.IfStmt(test=test, body=suite, orelse=orelse)

    def visitWhileStatement(self, ctx:PrototypeParser.WhileStatementContext):
        test = self.visit(ctx.expressionSequence())
        suite = self.visit(ctx.statement())

        return AST.stmt.WhileStmt(test=test, body=suite, orelse=[])

    def visitForInStatement(self, ctx:PrototypeParser.ForInStatementContext):
        if ctx.singleExpression() is not None:
            expr = self.visit(ctx.singleExpression())
        else:
            raise NotImplementedError()
        test = self.visit(ctx.expressionSequence())
        suite = self.visit(ctx.statement())

        return AST.stmt.ForInStmt(target=expr, iter=test, body=suite)

    def visitForStatement(self, ctx:PrototypeParser.ForStatementContext):
        raise NotImplementedError()
        # if ctx.expressionSequence() is not None:
        #     expr = self.visit(ctx.expressionSequence())
        # elif ctx.variableDeclarationList() is not None:
        #     expr = self.visit(ctx.variableDeclarationList())
        # else:
        #     raise SyntaxError()
        # test = self.visit(ctx.expressionSequence())
        # suite = self.visit(ctx.statement())

        # return AST.stmt.ForStmt(target=expr, iter=test, body=suite)

    def visitFunctionDeclaration(self, ctx:PrototypeParser.FunctionDeclarationContext):
        name = ctx.identifier().getText()
        body = self.visit(ctx.functionBody())

        param_ctx = ctx.formalParameterList()
        params = []

        if param_ctx != None:
            for param_arg in param_ctx.formalParameterArg():
                if param_arg.singleExpression() is not None:
                    raise NotImplementedError()
                if param_arg.assignable().identifier() is None:
                    raise NotImplementedError()
                else:
                    params.append(param_arg.assignable().identifier().getText())
            if param_ctx.lastFormalParameterArg() is not None:
                raise NotImplementedError()

        return AST.stmt.FunctionDef(name=name, args=params, body=body)
    
    def visitFunctionBody(self, ctx:PrototypeParser.FunctionBodyContext):
        statements = []

        if ctx.sourceElements() != None:
            statements = self.visit(ctx.sourceElements())

        return statements

    #
    # Small statements
    #
    def visitExpressionStatement(self, ctx: PrototypeParser.ExpressionStatementContext):
        return self.visit(ctx.expressionSequence())

    #
    # Control flow statements
    #
    def visitReturnStatement(self, ctx: PrototypeParser.ReturnStatementContext):
        expressionSequence = None

        validParents = (PrototypeParser.FunctionBodyContext, )

        if not self.validContextParents(ctx, validParents):
            raise runtime.Errors.SyntaxError("'return' outside function")

        if ctx.expressionSequence() != None:
            expressionSequence = self.visit(ctx.expressionSequence())

        return AST.stmt.ReturnStmt(expr=expressionSequence)

    # def visitPass_stmt(self, ctx:PrototypeParser.Pass_stmtContext):
    #     return AST.stmt.PassStmt()

    # def visitBreak_stmt(self, ctx:PrototypeParser.Break_stmtContext):
    #     validParents = PrototypeParser.For_stmtContext, PrototypeParser.While_stmtContext

    #     if not self.validContextParents(ctx, validParents):
    #         raise runtime.Errors.SyntaxError("'break' outside loop")

    #     return AST.stmt.BreakStmt()

    # def visitContinue_stmt(self, ctx:PrototypeParser.Continue_stmtContext):
    #     validParents = PrototypeParser.For_stmtContext, PrototypeParser.While_stmtContext

    #     if not self.validContextParents(ctx, validParents):
    #         raise runtime.Errors.SyntaxError("'continue' outside loop")

    #     return AST.stmt.ContinueStmt()

    #
    # Check whether context has one of the specified proper parents
    #
    def validContextParents(self, context, properParents: tuple):
        context = context.parentCtx

        while context != None:
            context = context.parentCtx
            if isinstance(context, properParents):
                return True

        return False
