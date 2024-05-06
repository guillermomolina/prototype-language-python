import copy
from prototype.ast.base import StatementNode, ExpressionNode, MemoryContext, ControlFlowMark
from prototype.ast.expr import AddOpNode, SubOpNode, MultOpNode, DivOpNode, ModOpNode, LShiftOpNode, RShiftOpNode, BinOpNode, UnaryOpNode, CompareNode
from prototype.ast.expr import BitAndOpNode, BitOrOpNode, BitXorOpNode, NameNode, CallExprNode

from prototype import ast
from prototype import runtime
from prototype.runtime.memory import Context
from prototype.runtime.objects import Array, Boolean, Null, Number, Object, String

"""
# Function definition.
#   @name - text name of the function
#   @args - list of arguments (just names)
#   @body - list of statements, which form functions body
#
# Every function has name which is written to the outer context.
# For the top-level function definitions, the outer context is the global context.
# For nested functions its the context of the outer function.
#
# Our way to implement name scoping is to set current context during the evaluation of ANY *STATEMENT*
# Actually, we'll need to set the new (and then back the old one) when evaluating only functions,
# as there are no scoping rules for other statements; thus, @NameNode expression will need to check
# only single global variable - current context, and function calls will switch contexts.
#
# This solution is far from perfect. However, it just works as there is no need for modules.
# Implementing modules will require providing each @NameNode node an ability to get a proper context.
"""
class FunctionDef(StatementNode):
    def __init__(self, name:str, args:list, body:list):
        super().__init__()
        self.name = name
        self.args = args
        self.body = body

    def getContext(self) -> runtime.memory.Context:
        return Context.current

    def eval(self) -> None:
        raise NotImplementedError()

        declarationContext = self.getContext()

        def container(*args):
            context = runtime.memory.Context(outerContext=declarationContext)
            previousContext = Context.current
            Context.current = context

            if len(args) != len(self.args):
                message = "%s() takes %d positional arguments but %d were given" % \
                          (self.name, len(self.args), len(args))
                raise runtime.Errors.TypeError(message)

            for pair in zip (self.args, args):
                context.set(name=pair[0], value=pair[1])

            returnValue = None

            for stmt in self.body:
                res = stmt.eval()
                if isinstance(res, ControlFlowMark):
                    if res.type == ControlFlowMark.Type.Return:
                        if res.toEval is not None:
                            returnValue = res.toEval.eval()
                        break

            Context.current = previousContext
            return returnValue

        # Finally, write the function container to the memory.
        # Call to the container will trigger eval of function body
        declarationContext.set(self.name, container)
        return None


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
        #Context.current.get(self)

        for x in self.iter.eval():
            # Set target to the current value
            Context.current.set(self.target.id, x)

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
# An assignment.
#   @targets is a list of nodes,
#   @value is a single node.
#
# Multiple nodes in targets represents assigning the same value to each.
# Unpacking is represented by putting a Tuple or List within targets.
#
# Notice, that grammar I've implemented doesn't allow to assign to operators/keywords/literals;
# Because of this we don't perform check for the type of a target value here.
"""
class AssignStmt(StatementNode):
    def __init__(self, target, value:ExpressionNode):
        super().__init__()
        self.target = target
        self.value = value

    def eval(self) -> None:
        if isinstance(self.target, ast.expr.CallExprNode):
            raise runtime.Errors.SyntaxError("can't assign to function call")

        lValue = self.target.eval()
        rValue = self.value.eval()

        if isinstance(lValue, SubscriptNode.AssignWrapper):
            lValue.collection[lValue.index] = rValue
        elif isinstance(lValue, PropertyNode.AssignWrapper):
            lValue.object[lValue.property] = rValue
        else:
            Context.current.set(name=lValue, value=rValue)

        return rValue


class AugAssignStmt(AssignStmt):
    opTable = {
        '+=' : AddOpNode,
        '-=' : SubOpNode,
        '*=' : MultOpNode,
        '/=' : DivOpNode,
        '%=' : ModOpNode,
        '&=' : BitAndOpNode,
        '|=' : BitOrOpNode,
        '^=' : BitXorOpNode,
        '<<=' : LShiftOpNode,
        '>>=' : RShiftOpNode,
    }

    def __init__(self, name, value, op):
        nameNodeLoad = copy.copy(name)
        nameNodeStore = copy.copy(name)

        nameNodeLoad.ctx = MemoryContext.Load
        nameNodeStore.ctx = MemoryContext.Store

        binOp = AugAssignStmt.opTable[op](left=nameNodeLoad, right=value)
        super().__init__(target=nameNodeStore, value=binOp)



"""
# PropertyNode access (e.g., name.attribute)
#   @value is a node, typically a NameNode.
#   @attr is a bare string giving the name of the attribute
#   @ctx is Load, Store or Del according to how the attribute is acted on.
"""
class PropertyNode(StatementNode):

    class AssignWrapper():
        def __init__(self, object, property):
            self.object = object
            self.property = property

    def __init__(self, value, attr, ctx):
        super().__init__()
        self.value = value
        self.attr = attr
        self.ctx = ctx

    def eval(self):
        value = self.value.eval()

        if value is None:
            value = Null.INSTANCE
        elif value is True:
            value = Boolean.TRUE
        elif value is False:
            value = Boolean.FALSE
        elif isinstance(value, int) or isinstance(value, float):
            value = Number.PROTOTYPE
        elif isinstance(value, str):
            value = String.PROTOTYPE
        elif isinstance(value, list):
            value = Array.PROTOTYPE
        elif isinstance(value, dict):
            value = Object.PROTOTYPE
        if self.ctx == MemoryContext.Load:
            return value[self.attr]
        elif self.ctx == MemoryContext.Store:
            return PropertyNode.AssignWrapper(value, self.attr)
        else:
            raise NotImplementedError()

"""
A subscript, such as l[1].
    @value is the object, often a NameNode.
    @slice is one of @IndexNode or @SliceNode.
    @ctx is Load, Store or Del according to what it does with the subscript.
"""
class SubscriptNode(StatementNode):

    class AssignWrapper:
        def __init__(self, collection, index):
            self.collection = collection
            self.index = index

    def __init__(self, value, slice, ctx):
        super().__init__()
        self.value = value
        self.slice = slice
        self.ctx = ctx

    def eval(self):
        lValue = self.value.eval()

        try:
            if isinstance(self.slice, IndexNode):
                index = self.slice.eval()

                if self.ctx == MemoryContext.Load:
                    return lValue[index]
                elif self.ctx == MemoryContext.Store:
                    return SubscriptNode.AssignWrapper(lValue, index)
                else:
                    raise NotImplementedError

            elif isinstance(self.slice, SliceNode):
                lower, upper = self.slice.eval()

                if self.ctx == MemoryContext.Load:
                    return lValue[lower:upper]
                else:
                    raise NotImplementedError("Writing to slices & deleting elements is not supported")

            else:
                raise ValueError("Unexpected slice type")
        except IndexError as e:
            raise runtime.Errors.IndexError(e)
        except KeyError as e:
            raise runtime.Errors.KeyError(e)
        except TypeError as e:
            raise runtime.Errors.TypeError(e)

"""
Simple subscripting with a single value: l[1]
"""
class IndexNode(StatementNode):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        return self.value.eval()

"""
Regular slicing: l[1:2]
"""
class SliceNode(StatementNode):
    def __init__(self, lower, upper, step):
        super().__init__()
        self.lower = lower
        self.upper = upper
        self.step = step

        if self.step is not None:
            raise NotImplementedError()

    def eval(self):
        lower = upper = None
        if self.lower is not None:
            lower = self.lower.eval()
        if self.upper is not None:
            upper = self.upper.eval()
        return lower, upper


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



