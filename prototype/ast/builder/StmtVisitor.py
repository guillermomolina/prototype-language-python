from prototype.ast.builder.ExprVisitor import getParameters
from prototype.ast.builder.Scope import Scope
from prototype.parser.PrototypeParser import PrototypeParser
from prototype.parser.PrototypeParserVisitor import PrototypeParserVisitor

from prototype import ast
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
                if statement is not None:
                    statements.append(statement)

        return statements

    def visitSourceElements(self, ctx:PrototypeParser.SourceElementsContext):
        statements = []

        for sourceElement in ctx.sourceElement():
            statement =  self.visit(sourceElement.statement())
            if statement is not None:
                if type(statement) is list:
                    statements += statement
                else:
                    statements.append(statement)

        return statements

    # def visitStatement(self, ctx:PrototypeParser.StatementContext):
    #     statements = []

    #     for smallStmt in ctx.small_stmt():
    #         statement = self.visit(smallStmt)
    #         if statement is not None:
    #             statements.append(statement)

    #     return statements

    # #
    # # Base statements
    # #
    # def visitSimple_stmt(self, ctx:PrototypeParser.Simple_stmtContext):
    #     statements = []

    #     for smallStmt in ctx.small_stmt():
    #         statement = self.visit(smallStmt)
    #         if statement is not None:
    #             statements.append(statement)

    #     return statements

    # #
    # # Compound statements
    # #
    # def visitSuite(self, ctx:PrototypeParser.SuiteContext):
    #     if ctx.simple_stmt() is not None:
    #         return self.visit(ctx.simple_stmt())

    #     statements = []

    #     for stmt in ctx.stmt():
    #         if stmt.simple_stmt() is not None:
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

        return ast.stmt.IfStmt(test=test, body=suite, orelse=orelse)

    def visitWhileStatement(self, ctx:PrototypeParser.WhileStatementContext):
        test = self.visit(ctx.expressionSequence())
        suite = self.visit(ctx.statement())

        return ast.stmt.WhileStmt(test=test, body=suite, orelse=[])

    def visitForInStatement(self, ctx:PrototypeParser.ForInStatementContext):
        if ctx.singleExpression() is not None:
            expr = self.visit(ctx.singleExpression())
        else:
            raise NotImplementedError()
        test = self.visit(ctx.expressionSequence())
        suite = self.visit(ctx.statement())

        return ast.stmt.ForInStmt(target=expr, iter=test, body=suite)

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

        # return ast.stmt.ForStmt(target=expr, iter=test, body=suite)

    def visitFunctionDeclaration(self, ctx:PrototypeParser.FunctionDeclarationContext):
        name = ctx.identifier().getText()
        params = getParameters(ctx.formalParameterList())
        Scope.enterFunction(params)
        body = self.visit(ctx.functionBody())
        Scope.leave()
        return ast.stmt.FunctionDef(name=name, args=params, body=body)

    def visitFunctionBody(self, ctx:PrototypeParser.FunctionBodyContext):
        statements = []

        if ctx.sourceElements() is not None:
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

        if ctx.expressionSequence() is not None:
            expressionSequence = self.visit(ctx.expressionSequence())

        return ast.stmt.ReturnStmtNode(expr=expressionSequence)

    # def visitPass_stmt(self, ctx:PrototypeParser.Pass_stmtContext):
    #     return ast.stmt.PassStmtNode()

    # def visitBreak_stmt(self, ctx:PrototypeParser.Break_stmtContext):
    #     validParents = PrototypeParser.For_stmtContext, PrototypeParser.While_stmtContext

    #     if not self.validContextParents(ctx, validParents):
    #         raise runtime.Errors.SyntaxError("'break' outside loop")

    #     return ast.stmt.BreakStmtNode()

    # def visitContinue_stmt(self, ctx:PrototypeParser.Continue_stmtContext):
    #     validParents = PrototypeParser.For_stmtContext, PrototypeParser.While_stmtContext

    #     if not self.validContextParents(ctx, validParents):
    #         raise runtime.Errors.SyntaxError("'continue' outside loop")

    #     return ast.stmt.ContinueStmtNode()

    #
    # Check whether context has one of the specified proper parents
    #
    def validContextParents(self, context, properParents: tuple):
        context = context.parentCtx

        while context is not None:
            context = context.parentCtx
            if isinstance(context, properParents):
                return True

        return False
