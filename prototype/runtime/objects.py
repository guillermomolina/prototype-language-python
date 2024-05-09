from prototype import runtime


class Object:
    PROTOTYPE = None
    GLOBALS = None

    @classmethod
    def initialize(cls):
        pass

    @classmethod
    def fromNative(cls, value):
        if value is None:
            return Null.INSTANCE
        if value is True:
            return Boolean.TRUE
        if value is False:
            return Boolean.FALSE
        if isinstance(value, int) or isinstance(value, float):
            return Number.PROTOTYPE
        if isinstance(value, str):
            return String.PROTOTYPE
        if isinstance(value, list):
            return Array.PROTOTYPE
        if isinstance(value, dict):
            return Object.PROTOTYPE
        if isinstance(value, Object):
            return value
        raise ValueError("unkonw object type")

    def __init__(self, prototype=None, properties=None):
        self.prototype = prototype or Object.PROTOTYPE
        self.properties = properties or {}

    def __repr__(self):
        return str(self)

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
            values.append(f"'{key}': {str(value)}")
        return '{' + ', '.join(values) + '}'


class Function(Object):
    PROTOTYPE = None

    def __init__(self, function, parameters=[], source_code=None, prototype=None, properties=None):
        super().__init__(prototype or Function.PROTOTYPE, properties)
        self.function = function
        self.parameters = parameters
        self.source_code = source_code

    def __str__(self):
        string = 'function ('
        string += ', '.join(self.parameters)
        string += ') { '
        string += self.source_code or '/* native code */'
        string += ' }'
        return string


class ArrowFunction(Function):
    def __str__(self):
        string = '('
        string += ', '.join(self.parameters)
        string += ') { '
        string += self.source_code or '/* native code */'
        string += ' }'
        return string


class Prototype(Function):
    PROTOTYPE = None

    def __init__(self, name, constructor=None, parameters=[], source_code=None, prototype=None, properties=None):
        super().__init__(constructor or self.constructor, parameters, source_code,
                         prototype or Prototype.PROTOTYPE, properties)
        self.name = name

    def __str__(self):
        string = 'function ' + self.name + '('
        string += ', '.join(self.parameters)
        string += ') { '
        string += self.source_code or '/* native code */'
        string += ' }'
        return string

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


Object.PROTOTYPE = Prototype('Object')
Function.PROTOTYPE = Prototype('Function')
Function.PROTOTYPE.prototype = Object.PROTOTYPE
Array.PROTOTYPE = Prototype('Array')
Prototype.PROTOTYPE = Prototype('Prototype')
String.PROTOTYPE = Prototype('String')
Number.PROTOTYPE = Prototype('Number')
Boolean.PROTOTYPE = Prototype('Boolean')
Boolean.FALSE = Boolean(False)
Boolean.TRUE = Boolean(True)
Null.PROTOTYPE = Prototype('Null')
Null.INSTANCE = Null()


Object.PROTOTYPE.properties['print'] = Function(print)

Object.GLOBALS = Object()
Object.GLOBALS.properties['Object'] = Object.PROTOTYPE
Object.GLOBALS.properties['Array'] = Array.PROTOTYPE
Object.GLOBALS.properties['Function'] = Function.PROTOTYPE
Object.GLOBALS.properties['Prototype'] = Function.PROTOTYPE
Object.GLOBALS.properties['String'] = Prototype.PROTOTYPE
Object.GLOBALS.properties['Number'] = Number.PROTOTYPE
Object.GLOBALS.properties['Boolean'] = Boolean.PROTOTYPE
Object.GLOBALS.properties['True'] = Boolean.TRUE
Object.GLOBALS.properties['False'] = Boolean.FALSE
Object.GLOBALS.properties['Null'] = Null.PROTOTYPE
