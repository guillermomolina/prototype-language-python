from prototype import runtime


class Object:
    PROTOTYPE = None

    @classmethod
    def initialize(cls):
        pass

    def __init__(self, prototype=None, properties=None):
        self.prototype = prototype or Object.PROTOTYPE
        self.properties = properties or {}

    def __repr__(self):
        return self.properties.__repr__()

    def __iter__(self):
        return iter(self.properties)

    def __getitem__(self, item):
        try:
            return self.properties.__getitem__(item)
        except KeyError:
            if self.prototype is not None:
                return self.prototype[item]

            raise runtime.Errors.NameError("property %s is not defined" % item)

    def __setitem__(self, key, value):
        return self.properties.__setitem__(key, value)

    def __len__(self):
        return self.properties.__len__()

    def __str__(self):
        values = []
        for key, value in self.properties.items():
            if isinstance(value, Function):
                values.append(f'{key}{str(value)}')
            else:
                values.append(f"'{key}': {str(value)}")
        return '{' + ', '.join(values) + '}'


class Function(Object):
    PROTOTYPE = None

    def __init__(self, function, arguments=None, source_code=None, prototype=None, properties=None):
        super().__init__(prototype or Function.PROTOTYPE, properties)
        self.function = function
        self.arguments = arguments or []
        self.source_code = source_code

    def __str__(self):
        string = '('
        string += ', '.join(self.arguments)
        string += ') => {'
        string += self.source_code or ' /* native code */ '
        string += '}'
        return string


class Prototype(Function):
    PROTOTYPE = None

    def __init__(self, name, constructor=None, arguments=None, source_code=None, prototype=None, properties=None):
        super().__init__(constructor or self.constructor, arguments, source_code,
                         prototype or Prototype.PROTOTYPE, properties)
        self.name = name

    def __str__(self):
        return self.name + super().__str__()

    def constructor(self):
        pass


class Array(Object):
    PROTOTYPE = None

    def __init__(self, array=None):
        super().__init__(Array.PROTOTYPE)
        self.array = array or []

    def __str__(self):
        return str(self.array)


class String(Object):
    PROTOTYPE = None

    def __init__(self, string=None):
        super().__init__(String.PROTOTYPE)
        self.string = string or ""

    def __str__(self):
        return str(self.string)


class Number(Object):
    PROTOTYPE = None

    def __init__(self, number=None):
        super().__init__(Number.PROTOTYPE)
        self.number = number or 0

    def __str__(self):
        return str(self.number)


class Boolean(Object):
    PROTOTYPE = None
    FALSE = None
    TRUE = None

    def __init__(self, value=None):
        super().__init__(Boolean.PROTOTYPE)
        self.value = value or False

    def __str__(self):
        return 'true' if self.value else 'false'


class Null(Object):
    PROTOTYPE = None
    INSTANCE = None

    def __init__(self):
        super().__init__(Null.PROTOTYPE)

    def __str__(self):
        return 'null'  

class Scope(Object):
    PROTOTYPE = None
    GLOBAL = None

    def __init__(self, outerScope):
        super().__init__(Scope.PROTOTYPE)
        self.outerScope = outerScope


    def __getitem__(self, item):
        try:
            return self.properties.__getitem__(item)
        except KeyError:
            if self.outerScope is not None:
                return self.outerScope[item]

            raise runtime.Errors.NameError("name %s is not defined in scope" % item)

Object.PROTOTYPE = Prototype('Object', Function(Object))
Function.PROTOTYPE = Prototype('Function', Function(Function))
Function.PROTOTYPE.prototype = Object.PROTOTYPE
Array.PROTOTYPE = Prototype('Array', Function(Array))
Prototype.PROTOTYPE = Prototype('Prototype', Function(Prototype))
String.PROTOTYPE = Prototype('String', Function(String))
Number.PROTOTYPE = Prototype('Number', Function(Number))
Boolean.PROTOTYPE = Prototype('Boolean', Function(Boolean))
Boolean.FALSE = Boolean(False)
Boolean.TRUE = Boolean(True)
Null.PROTOTYPE = Prototype('Null', Function(Null))
Null.INSTANCE= Null()


Scope.PROTOTYPE = Prototype('Scope', Function(Scope))
Scope.GLOBAL= Scope(None)
Scope.GLOBAL.properties['Object'] = Object.PROTOTYPE
Scope.GLOBAL.properties['Array'] = Array.PROTOTYPE
Scope.GLOBAL.properties['Function'] = Function.PROTOTYPE
Scope.GLOBAL.properties['Prototype'] = Function.PROTOTYPE
Scope.GLOBAL.properties['String'] = Prototype.PROTOTYPE
Scope.GLOBAL.properties['Number'] = Number.PROTOTYPE
Scope.GLOBAL.properties['Boolean'] = Boolean.PROTOTYPE
Scope.GLOBAL.properties['Null'] = Null.PROTOTYPE

Object.PROTOTYPE.properties['print'] = Function(print)
