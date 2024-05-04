

#
# Looks like we have to pass scope instance to every @NameNode node;
# Alternatively, we can make every node being able to retreive scope by its own.
# How? Probably, enclosing statement should provide such API, so we'll pass enclosing statements
# as arguments for expressions, and @ExpressionNode will have a method "retrieve scope"
#
from prototype import runtime
from prototype.runtime.objects import Boolean, Null, Number, Object, Array, Function, Prototype


class Scope:

    GLOBAL = None

    builtInFunctions = {
        'print': print,
        'input': input,
        'exit': exit,
        'len': len,
        'str': str,
        'int': int,
        'hex': hex,
        'oct': oct,
        'bin': bin,
        'float': float,
        'type': type,
        'range': range,
        'chr': chr,
        'ascii': ascii,
        'abs': abs,
        'max': max,
        'min': min,
        'sum': sum,
        'open': open,
        'reversed': reversed
    }

    def __init__(self, outerScope):
        self.outerScope = outerScope
        self.content = {}
        if self.outerScope == None:
            self.init_globals()

    def init_globals(self):
        self.content.update(Scope.builtInFunctions)
        self.content['Object'] = Object.INSTANCE
        self.content['Array'] = Array.INSTANCE
        self.content['Function'] = Function.INSTANCE
        self.content['Prototype'] = Function.INSTANCE
        self.content['String'] = Prototype.INSTANCE
        self.content['Number'] = Number.INSTANCE
        self.content['Boolean'] = Boolean.INSTANCE
        self.content['Null'] = Null.INSTANCE

    def get(self, name):
        try:
            # Search in the current scope first
            return self.content[name]
        except KeyError:
            if self.outerScope != None:
                return self.outerScope.get(name)

            raise runtime.Errors.NameError("name %s is not defined" % name)

    def set(self, name, value):
        self.content[name] = value


Scope.GLOBAL = Scope(None)
CurrentScope = Scope.GLOBAL
