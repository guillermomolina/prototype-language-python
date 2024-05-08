from prototype import runtime
from prototype.runtime.objects import Object

class MemoryContext:
    CURRENT = None

    @classmethod
    def getFunctionContext(cls):
        context = MemoryContext.CURRENT
        while context is not None:
            if context is MemoryContext:
                return context
            context = context.previousContext
        raise runtime.Errors.MemoryError("MemoryContext stack is not yet initialized")

    @classmethod
    def push(cls, context):
        context.previousContext = MemoryContext.CURRENT
        MemoryContext.CURRENT = context

    @classmethod
    def pop(cls, context=None):
        if context is not None:
            raise NotImplementedError()
        MemoryContext.CURRENT = MemoryContext.CURRENT.previousContext

    def __init__(self, slots):
        self.previousContext = None
        self.slots = slots

    def get(self, name):
        if name in self.slots:
            return self.slots[name]

        if self.previousContext is None and name in Object.GLOBALS:
            return Object.GLOBALS[name]

        raise runtime.Errors.NameError("name %s is not defined in context" % name)

    def set(self, name, value):
        self.slots[name] = value

class ClosureMemoryContext(MemoryContext):
    def __init__(self, outerContext, slots):
        super().__init__(slots)
        self.outerContext = outerContext

    def get(self, name):
        raise NotImplementedError()

    def set(self, name, value):
        raise NotImplementedError()
