from prototype.ast.base import StatementNode, ExpressionNode, MemoryContextAccessType, ControlFlowMark
from prototype.ast.expr import AddOpNode, SubOpNode, MultOpNode, DivOpNode, ModOpNode, LShiftOpNode, RShiftOpNode, BinOpNode, UnaryOpNode, CompareNode
from prototype.ast.expr import BitAndOpNode, BitOrOpNode, BitXorOpNode, NameNode, CallExprNode

from prototype import runtime
from prototype.runtime.memory import MemoryContext
from prototype.runtime.objects import Array, Boolean, Null, Number, Object, String


"""
# An if statement.
#    @test holds a single node, such as a CompareNode node.
#    @body and orelse each hold a list of nodes.
#
# @elif clauses don’t have a special representation in the Node, but rather
# appear as extra If nodes within the orelse section of the previous one.
#
# Optional clauses such as @else are stored as an empty list if they’re not present.
"""
class IfStmt(StatementNode):
    def __init__(self, test, body:list, orelse:list):
        super().__init__()
        self.test = test
        self.body = body
        self.orelse = orelse

    def eval(self):
        test = self.test.eval()
        result = []

        for stmt in self.body if (test) else self.orelse:
            evalResult = stmt.eval()

            if isinstance(evalResult, ControlFlowMark):
                if evalResult.type != ControlFlowMark.Type.Pass:
                    return evalResult

            if type(evalResult) is list:
                result += evalResult
            else:
                result.append(evalResult)

        return result


"""
# An while statement.
#    @test holds a single node, such as a @CompareNode node.
#    @body and @orelse each hold a list of nodes.
#
# @orelse is not used as it is not present in grammar.
"""
class WhileStmt(StatementNode):
    def __init__(self, test, body:list, orelse:list):
        super().__init__()
        self.test = test
        self.body = body

    def eval(self):
        result = []

        while self.test.eval():
            shouldBreak = False
            for stmt in self.body:
                evalResult = stmt.eval()

                if isinstance(evalResult, ControlFlowMark):
                    if evalResult.type == ControlFlowMark.Type.Break:
                        shouldBreak = True
                        break
                    elif evalResult.type == ControlFlowMark.Type.Continue:
                        break
                    elif evalResult.type == ControlFlowMark.Type.Pass:
                        pass
                    elif evalResult.type == ControlFlowMark.Type.Return:
                        return evalResult

                if type(evalResult) is list:
                    result += evalResult
                else:
                    result.append(evalResult)
            if shouldBreak:
                break

        return result

"""
# A for loop.
#   @target holds the variable(s) the loop assigns to, as a single NameNode, Tuple or List node.
#   @iter holds the item to be looped over, again as a single node.
#   @body and orelse contain lists of nodes to execute.
#
# @orelse is not used as it is not present in grammar.
"""
class ForInStmt(StatementNode):
    def __init__(self, target, iter, body, orelse=None):
        super().__init__()
        self.target = target
        self.iter = iter
        self.body = body

        if not isinstance(target, NameNode):
            raise runtime.Errors.SyntaxError("can't assign to literal")

        if orelse is not None:
            raise NotImplementedError("You should implement orelse in grammar first!")

    def eval(self):
        result = []

        # Check if target name exists. If no - create it.
        #MemoryContext.CURRENT.get(self)

        for x in self.iter.eval():
            # Set target to the current value
            MemoryContext.CURRENT.set(self.target.id, x)

            shouldBreak = False
            for stmt in self.body:
                evalResult = stmt.eval()

                if isinstance(evalResult, ControlFlowMark):
                    if evalResult.type == ControlFlowMark.Type.Break:
                        shouldBreak = True
                        break
                    elif evalResult.type == ControlFlowMark.Type.Continue:
                        break
                    elif evalResult.type == ControlFlowMark.Type.Pass:
                        pass
                    elif evalResult.type == ControlFlowMark.Type.Return:
                        return evalResult

                if type(evalResult) is list:
                    result += evalResult
                else:
                    result.append(evalResult)
            if shouldBreak:
                break

        return result


"""
# Control flow statements.
# Each statement returns corresponding @ControlFlowMark as a result of evaluation.
# Compound statements are checking whether evaluation result is a such mark, and react accordingly.
"""
class ControlFlowStmtNode(StatementNode):
    pass


class ReturnStmtNode(ControlFlowStmtNode):
    def __init__(self, expr):
        super().__init__()
        self.expr = expr

    def eval(self):
        return ControlFlowMark(ControlFlowMark.Type.Return, self.expr)


class PassStmtNode(ControlFlowStmtNode):
    def eval(self):
        return ControlFlowMark(ControlFlowMark.Type.Pass)


class ContinueStmtNode(ControlFlowStmtNode):
    def eval(self):
        return ControlFlowMark(ControlFlowMark.Type.Continue)


class BreakStmtNode(ControlFlowStmtNode):
    def eval(self):
        return ControlFlowMark(ControlFlowMark.Type.Break)



