class Scope:
    CURRENT = None

    def __init__(self, outerScope=None, arguments=[], inLoop = False):
        self.outerScope = outerScope
        self.inLoop = inLoop
        self.arguments = arguments
        self.variables = []
        self.sharedVariables = []

    @classmethod
    def enterFunction(cls, arguments=[]):   
        cls.CURRENT = Scope(cls.CURRENT, ['this'] + arguments)

    @classmethod
    def enterArrowFunction(cls, arguments=[]):
        cls.CURRENT = Scope(cls.CURRENT, arguments)

    @classmethod
    def enterLoop(cls):
        cls.CURRENT = Scope(cls.CURRENT, inLoop=True)
    
    @classmethod
    def leave(cls):
        cls.CURRENT = cls.CURRENT.outerScope
