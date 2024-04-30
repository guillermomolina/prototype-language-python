from prototype.AST.builder.ExprVisitor import ExprVisitorMixin
from prototype.AST.builder.StmtVisitor import StmtVisitorMixin

from prototype.parser.PrototypeParser import PrototypeParser
from prototype.parser.PrototypeParserVisitor import PrototypeParserVisitor

from prototype.AST import ast

class CustomVisitor(StmtVisitorMixin, ExprVisitorMixin, PrototypeParserVisitor):
    def visitChildren(self, node):
        result = self.defaultResult()
        n = node.getChildCount()
        for i in range(n):
            if not self.shouldVisitNextChild(node, result):
                return result

            c = node.getChild(i)
            childResult = c.accept(self)
            result = self.aggregateResult(result, childResult)

        if not isinstance(result, ast.AST):
            raise NotImplementedError()
        return result

    #
    # Visit parse tree produced from a file
    #
    def visitProgram(self, ctx:PrototypeParser.ProgramContext):
        statements = []

        if ctx.sourceElements() != None:
            for sourceElement in ctx.sourceElements().sourceElement():
                statement =  self.visit(sourceElement.statement())
                if statement != None:
                    if type(statement) is list:
                        statements += statement
                    else:
                        statements.append(statement)

        return ast.Module(body=statements)

    # #
    # # Visit parse tree produced from a file
    # #
    # def visitFile_input(self, ctx:PrototypeParser.File_inputContext):
    #     statements = []

    #     for stmt in ctx.stmt():
    #         statement =  self.visit(stmt)
    #         if statement != None:
    #             if type(statement) is list:
    #                 statements += statement
    #             else:
    #                 statements.append(statement)

    #     return ast.Module(body=statements)


    # #
    # # Single input is used both in interpreter mode and with strings passes as a parameter
    # #
    # def visitSingle_input(self, ctx:PrototypeParser.Single_inputContext):
    #     if ctx.compound_stmt() != None:
    #         return ast.Interactive(self.visit(ctx.compound_stmt()))

    #     elif ctx.simple_stmt() != None:
    #         return ast.Interactive(self.visit(ctx.simple_stmt()))

    #     return None

    # #
    # # Visit single expression (call to the eval() function)
    # #
    # def visitEval_input(self, ctx:PrototypeParser.Eval_inputContext):
    #     return ast.EvalExpression(self.visit(ctx.test()))


