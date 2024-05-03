#
# Some useful stuff here:
# http://greentreesnakes.readthedocs.org/en/latest/index.html
# https://docs.python.org/3/reference/expressions.html#calls
# https://docs.python.org/3/reference/executionmodel.html#naming
#
from enum import Enum


class Node:
    def eval(self):
        raise NotImplementedError()


""" Input types """

class Module(Node):
    def __init__(self, body:list):
        super().__init__()
        self.body = body

    def eval(self):
        if type(self.body) is not list:
            self.body.eval()
        for stmt in self.body:
            stmt.eval()


class Interactive(Node):
    def __init__(self, body:list):
        super().__init__()
        self.body = body

    def eval(self):
        if type(self.body) is not list:
            return self.body.eval()
        else:
            return [stmt.eval() for stmt in self.body]


class EvalExpression(Node):
    def __init__(self, body):
        super().__init__()
        self.body = body

    def eval(self):
        return self.body.eval()


""" Base node types """

class Expression(Node):
    def __init__(self):
        super().__init__()


class Statement(Node):
    def __init__(self):
        super().__init__()


""" Memory context for names, attributes, indexes, etc. """
class MemoryContext(Enum):
    Load = 1
    Store = 2
    Del = 3
