from abc import abstractmethod
from prototype import runtime
from prototype.runtime.objects import Object

class MemoryContext:
    CURRENT = None

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

    def getFunctionContext(self):
        context = self
        while context is not None:
            if isinstance(context, FunctionMemoryContext):
                return context
            context = context.previousContext
        raise runtime.Errors.MemoryError("MemoryContext stack is not yet initialized")

    def get(self, name):
        if name in self.slots:
            return self.slots[name]
        raise runtime.Errors.NameError("name %s is not defined in context" % name)

    def set(self, name, value):
        self.slots[name] = value

    @abstractmethod
    def getReceiver(self):
        raise NotImplementedError("Needs to implement in subclass")

class FunctionMemoryContext(MemoryContext):
    def __init__(self, receiver, slots):
        super().__init__(slots)
        self.receiver = receiver

    def get(self, name):
        receiver = Object.fromNative(self.receiver)
        if name in receiver:
            return receiver[name]
        return super().get(name)

    def set(self, name, value):
        receiver = Object.fromNative(self.receiver)
        if name in receiver:
            receiver[name] = value
        super().set(name, value)

    def getReceiver(self):
        return self.receiver

class ClosureMemoryContext(MemoryContext):
    def __init__(self, outerContext, slots):
        super().__init__(slots)
        self.outerContext = outerContext

    def get(self, name):
        try: 
            return super().get(name)
        except runtime.Errors.NameError:
            return self.outerContext.get(name)

    def set(self, name, value):
        raise NotImplementedError()

    def getReceiver(self):
        context = self.getFunctionContext()
        return context.receiver
