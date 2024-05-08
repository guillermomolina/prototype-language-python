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

    def getFunctionScope(self):
        scope = self
        while scope is not None:
            if isinstance(scope, FunctionScope):
                return scope
            scope = scope.outerScope
        raise NameError("Scope is wrong")

    def hasVariable(self, id):
        if id in self.variables:
            return True
        return hasattr(Object.GLOBALS, id)

    def addVariable(self, id, forceLocal=False):
        if not self.hasVariable(id) or forceLocal:
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
   
    def hasVariable(self, id):
        if id in self.parameters:
            return True
        return super().hasVariable(id)

class ArrowFunctionScope(FunctionScope):   
    def hasVariable(self, id):
        if super().hasVariable(id):
            return True
        if self.outerScope is None:
            raise NameError("Scope is wrong")
        return self.outerScope.hasVariable(id)

