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


class InteractiveNode(Node):
    def __init__(self, body:list):
        super().__init__()
        self.body = body

    def eval(self):
        if type(self.body) is not list:
            return self.body.eval()
        else:
            return [stmt.eval() for stmt in self.body]


class EvalExpressionNode(Node):
    def __init__(self, body):
        super().__init__()
        self.body = body

    def eval(self):
        return self.body.eval()


""" Base node types """

class ExpressionNode(Node):
    def __init__(self):
        super().__init__()


class StatementNode(Node):
    def __init__(self):
        super().__init__()


""" Memory context for names, attributes, indexes, etc. """
class MemoryContext(Enum):
    Load = 1
    Store = 2
    Del = 3
