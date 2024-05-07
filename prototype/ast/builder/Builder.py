from prototype.ast.builder.ExprVisitor import ExprVisitorMixin
from prototype.ast.builder.Scope import Scope
from prototype.ast.builder.StmtVisitor import StmtVisitorMixin

from prototype.parser.PrototypeParser import PrototypeParser
from prototype.parser.PrototypeParserVisitor import PrototypeParserVisitor

from prototype.ast import base

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

        if not isinstance(result, (base.Node, list)):
            raise NotImplementedError()
        return result

    #
    # Visit parse tree produced from a file
    #
    def visitProgram(self, ctx:PrototypeParser.ProgramContext):
        Scope.enterArrowFunction()
        
        statements = []

        if ctx.sourceElements() is not None:
            statements = self.visit(ctx.sourceElements())

        Scope.leave()
        return base.Module(body=statements)

    # #
    # # Visit parse tree produced from a file
    # #
    # def visitFile_input(self, ctx:PrototypeParser.File_inputContext):
    #     statements = []

    #     for stmt in ctx.stmt():
    #         statement =  self.visit(stmt)
    #         if statement is not None:
    #             if type(statement) is list:
    #                 statements += statement
    #             else:
    #                 statements.append(statement)

    #     return base.Module(body=statements)


    # #
    # # Single input is used both in interpreter mode and with strings passes as a parameter
    # #
    # def visitSingle_input(self, ctx:PrototypeParser.Single_inputContext):
    #     if ctx.compound_stmt() is not None:
    #         return base.InteractiveNode(self.visit(ctx.compound_stmt()))

    #     elif ctx.simple_stmt() is not None:
    #         return base.InteractiveNode(self.visit(ctx.simple_stmt()))

    #     return None

    # #
    # # Visit single expression (call to the eval() function)
    # #
    # def visitEval_input(self, ctx:PrototypeParser.Eval_inputContext):
    #     return base.EvalExpressionNode(self.visit(ctx.test()))


