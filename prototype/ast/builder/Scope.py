from prototype.runtime.objects import Object


class Scope:
    CURRENT = None

    @classmethod
    def enter(cls):   
        Scope.CURRENT = cls(Scope.CURRENT)
    
    @classmethod
    def leave(cls):
        Scope.CURRENT = Scope.CURRENT.outerScope

    def __init__(self, outerScope):
        self.outerScope = outerScope
        self.variables = []
   
    def addVariable(self, id, forceLocal=False):
        if id in self.variables:
            return
        if hasattr(Object.GLOBALS, id):
            return
        self.variables.append(id)

class LoopScope(Scope):
    pass

class FunctionScope(Scope):

    @classmethod
    def enter(cls, parameters=[]):   
        Scope.CURRENT = cls(Scope.CURRENT, parameters)

    def __init__(self, outerScope=None, parameters=[]):
        super().__init__(outerScope)
        self.parameters = parameters

class ArrowFunctionScope(FunctionScope):

    pass

