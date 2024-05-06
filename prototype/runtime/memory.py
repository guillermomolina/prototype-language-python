from prototype import runtime
from prototype.runtime.objects import Scope


class Context:
    current = None

    @classmethod
    def push(cls, previousContext, currentobject):
        context = cls(previousContext, currentobject)
        olderContext = cls.current
        cls.current = context
        return olderContext

    @classmethod
    def pop(cls, previousContext):
        olderContext = cls.current
        cls.current = previousContext
        return olderContext

    def __init__(self, previousContext, currentobject):
        self.previousContext = previousContext
        self.currentobject = currentobject

    def get(self, name):
        try:
            # Search in the current context first
            return self.currentobject[name]
        except KeyError:
            if self.previousContext is not None:
                return self.previousContext.get(name)

            raise runtime.Errors.NameError("name %s is not defined" % name)

    def set(self, name, value):
        self.currentobject[name] = value


Context.current = Context(None, Scope.GLOBAL)
