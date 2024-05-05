from enum import Enum
import operator

from prototype.ast.base import ExpressionNode, MemoryContext, ControlFlowMark
from prototype import runtime
from prototype.runtime.objects import Array, Boolean, Function, Null, Object



"""
# Anonymous function definition.
#   @args - list of arguments (just names)
#   @body - list of statements, which form functions body
#
# Every function has name which is written to the outer scope.
# For the top-level function definitions, the outer scope is the global scope.
# For nested functions its the scope of the outer function.
#
# Our way to implement name scoping is to set current scope during the evaluation of ANY *STATEMENT*
# Actually, we'll need to set the new (and then back the old one) when evaluating only functions,
# as there are no scoping rules for other statements; thus, @NameNode expression will need to check
# only single global variable - current scope, and function calls will switch scopes.
#
# This solution is far from perfect. However, it just works as there is no need for modules.
# Implementing modules will require providing each @NameNode node an ability to get a proper scope.
"""
class AnonymousFunctionDef(ExpressionNode):
    def __init__(self, args:list, body:list, source_code:str):
        super().__init__()
        self.args = args
        self.body = body
        self.source_code = source_code

    def getScope(self) -> runtime.memory.Scope:
        return runtime.memory.CurrentScope

    def eval(self) -> None:

        declarationScope = self.getScope()

        def container(*args):
            scope = runtime.memory.Scope(outerScope=declarationScope)
            previousScope = runtime.memory.CurrentScope
            runtime.memory.CurrentScope = scope

            if len(args) != len(self.args):
                message = "function() takes %d positional arguments but %d were given" % \
                          (len(self.args), len(args))
                raise runtime.Errors.TypeError(message)

            for pair in zip (self.args, args):
                scope.set(name=pair[0], value=pair[1])

            returnValue = None

            for stmt in self.body:
                res = stmt.eval()
                if isinstance(res, ControlFlowMark):
                    if res.type == ControlFlowMark.Type.Return:
                        if res.toEval != None:
                            returnValue = res.toEval.eval()
                        break

            runtime.memory.CurrentScope = previousScope
            return returnValue
        
        return Function(container, self.args, self.source_code)


"""
# Binary arithmetic, bitwise and logic operations
"""
class BinOpNode(ExpressionNode):
    def __init__(self, left:ExpressionNode, right:ExpressionNode):
        super().__init__()
        self.left = left
        self.right = right

class AddOpNode(BinOpNode):
    def eval(self):
        return self.left.eval() + self.right.eval()

class SubOpNode(BinOpNode):
    def eval(self):
        return self.left.eval() - self.right.eval()

class MultOpNode(BinOpNode):
    def eval(self):
        return self.left.eval() * self.right.eval()

class DivOpNode(BinOpNode):
    def eval(self):
        left  = self.left.eval()
        right = self.right.eval()

        if right == 0:
            raise runtime.Errors.ZeroDivisionError()

        return left / right

class ModOpNode(BinOpNode):
    def eval(self):
        left  = self.left.eval()
        right = self.right.eval()

        if right == 0:
            raise runtime.Errors.ZeroDivisionError()

        return left % right

class LShiftOpNode(BinOpNode):
    def eval(self):
        return self.left.eval() << self.right.eval()

class RShiftOpNode(BinOpNode):
    def eval(self):
        return self.left.eval() >> self.right.eval()

class BitAndOpNode(BinOpNode):
    def eval(self):
        return self.left.eval() & self.right.eval()

class BitXorOpNode(BinOpNode):
    def eval(self):
        return self.left.eval() ^ self.right.eval()

class BitOrOpNode(BinOpNode):
    def eval(self):
        return self.left.eval() | self.right.eval()


"""
# Unary arithmetic operations
"""
class UnaryOpNode(ExpressionNode):
    def __init__(self, op, operand:ExpressionNode):
        super().__init__()
        self.op = op
        self.operand = operand

    def eval(self):
        if self.op == '+':
            return self.operand.eval()
        elif self.op == '-':
            return -(self.operand.eval())
        else:
            raise ValueError('Unsupported unary operation!')


"""
# Base class for comparisons.
"""
class CompareNode(ExpressionNode):

    class Op(Enum):
        AND = 1
        OR  = 2
        NOT = 3
        IN  = 4
        IS  = 5
        NOT_IN = 6
        IS_NOT = 7

    opTable = {
        '<'  : operator.lt,
        '>'  : operator.gt,
        '==' : operator.eq,
        '>=' : operator.ge,
        '<=' : operator.le,
        '!=' : operator.ne,
        Op.AND : operator.__and__,
        Op.OR  : operator.__or__,
        Op.NOT : operator.__not__,
        Op.IS  : operator.is_,
        Op.IS_NOT : operator.is_not,
    }

    def __init__(self, op):
        super().__init__()
        self.op = op

class BinaryCompNode(CompareNode):
    def __init__(self, left, right, op):
        super().__init__(op=op)
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()

        if self.op == CompareNode.Op.IN:
            return left in right
        elif self.op == CompareNode.Op.NOT_IN:
            return left not in right

        return CompareNode.opTable[self.op](left, right)

class UnaryCompNode(CompareNode):
    def __init__(self, operand, op):
        super().__init__(op=op)
        self.operand = operand

    def eval(self):
        operand = self.operand.eval()
        return CompareNode.opTable[self.op](operand)


"""
# Represents None, False and True literals.
"""
class NameConstantNode(ExpressionNode):
    nameTable = { 
        'null' : Null.INSTANCE, 
        'true': Boolean.TRUE, 
        'false': Boolean.FALSE
    }

    def __init__(self, name):
        super().__init__()
        self.name = name

    def eval(self):
        try:
            return NameConstantNode.nameTable[self.name]
        except KeyError:
            raise ValueError("Wrong name constant")

"""
# A variable name.
#     @id holds the name as a string
#     @ctx is one of the following types: @Load / @Store / @Del
"""
class NameNode(ExpressionNode):

    def __init__(self, id, ctx:MemoryContext):
        super().__init__()
        self.id = id
        self.ctx = ctx

    def eval(self):
        if self.ctx == MemoryContext.Load:
            return self.getScope().get(name=self.id)
        elif self.ctx == MemoryContext.Store:
            return self.id
        else:
            raise NotImplementedError()

    def getScope(self):
        # Problem: we're very loosely coupled.
        return runtime.memory.CurrentScope

"""
# A variable name.
#     @id holds the name as a string
#     @ctx is one of the following types: @Load / @Store / @Del
"""
class ThisExprNode(ExpressionNode):

    def __init__(self):
        super().__init__()

    def eval(self):
        raise NotImplementedError()
        if self.ctx == MemoryContext.Load:
            return self.getScope().get(name=self.id)
        elif self.ctx == MemoryContext.Store:
            return self.id
        else:
            raise NotImplementedError()

    def getScope(self):
        # Problem: we're very loosely coupled.
        return runtime.memory.CurrentScope

"""
# Function call
#     @param func is the function, which will often be a NameNode object.
#     @args holds a list of the arguments passed by position.
"""
class CallExprNode(ExpressionNode):
    def __init__(self, rcvr, func, args):
        super().__init__()
        self.rcvr = rcvr
        self.func = func   # name
        self.args = args

    def eval(self):
        rcvr = self.rcvr.eval()
        func = self.func.eval()
        evalArgs = [ arg.eval() for arg in self.args ]
        return func(rcvr, *evalArgs)


"""
# Base class for collections.
#   @value holds a collection, such as a list or a dict.
#
# This class delegates common collection methods  to the contained value.
"""
class CollectionContainerNode(ExpressionNode):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __repr__(self):
        return self.value.__repr__()

    def __iter__(self):
        return iter(self.value)

    def __getitem__(self, item):
        return self.value.__getitem__(item)

    def __setitem__(self, key, value):
        return self.value.__setitem__(key, value)

    def __len__(self):
        return self.value.__len__()


class ArrayContainerNode(CollectionContainerNode):
    def __init__(self, value:list):
        super().__init__(value)

    def eval(self):

        return Array([value.eval() for value in self.value])

    def __add__(self, other):
        if type(other) is not ArrayContainerNode:
            msg = 'can only concatenate list to list'
            raise runtime.Errors.TypeError(msg)
        return ArrayContainerNode(self.value + other.value)

    def __mul__(self, other):
        return ArrayContainerNode(self.value.__mul__(other))

    def append(self, what):
        return self.value.append(what)


class TupleContainerNode(CollectionContainerNode):
    def __init__(self, value):
        super().__init__(value)

    def eval(self):
        return TupleContainerNode(tuple(value.eval() for value in self.value))

    def __add__(self, other):
        if type(other) is not TupleContainerNode:
            msg = 'can only concatenate tuple to tuple'
            raise runtime.Errors.TypeError(msg)
        return TupleContainerNode(self.value + other.value)

    def __mul__(self, other):
        return TupleContainerNode(self.value.__mul__(other))

class ObjectContainerNode(CollectionContainerNode):
    def __init__(self, value:dict):
        super().__init__(value)

    def copy(self):
        return ObjectContainerNode(self.value.copy())

    def update(self, right):
        self.value.update(right.value)
        # return ObjectContainerNode(self.value.update(right.value))

    def eval(self):
        result = Object()

        for key in self.value.keys():
            newKey = key.eval()
            newVal = self.value[key].eval()
            result.properties[newKey] = newVal

        return result


class SetContainerNode(CollectionContainerNode):
    def __init__(self, value:set):
        super().__init__(value)

    def eval(self):
        result = set({})
        for item in self.value:
            result.add(item.eval())
        return SetContainerNode(result)

    def update(self, right):
        SetContainerNode(self.value.update(right))

"""
# Number literal
"""
class NumberNode(ExpressionNode):

    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        return self.value

"""
# String literal
"""
class StringNode(ExpressionNode):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        return self.value
