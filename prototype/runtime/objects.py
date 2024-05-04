class Object:
    INSTANCE = None

    @classmethod
    def initialize(cls):
        pass

    def __init__(self, prototype=None, properties=None):
        self.prototype = prototype or Object.INSTANCE
        self.properties = properties or {}

    def __str__(self):
        values = []
        for key, value in self.properties.items():
            if isinstance(value, Function):
                values.append(f'{key}{str(value)}')
            else:
                values.append(f"'{key}': {str(value)}")
        return '{' + ', '.join(values) + '}'


class Function(Object):
    INSTANCE = None

    def __init__(self, function, arguments=None, source_code=None, prototype=None, properties=None):
        super().__init__(prototype or Function.INSTANCE, properties)
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
    INSTANCE = None

    def __init__(self, name, constructor=None, arguments=None, source_code=None, prototype=None, properties=None):
        super().__init__(constructor or self.constructor, arguments, source_code,
                         prototype or Prototype.INSTANCE, properties)
        self.name = name

    def __str__(self):
        return self.name

    def constructor(self):
        pass


class Array(Object):
    INSTANCE = None

    def __init__(self, array=None):
        self.prototype = Array.INSTANCE
        self.array = array or []

    def __str__(self):
        return str(self.array)


class String(Object):
    INSTANCE = None

    def __init__(self, string=None):
        self.prototype = String.INSTANCE
        self.string = string or ""

    def __str__(self):
        return str(self.string)


class Number(Object):
    INSTANCE = None

    def __init__(self, number=None):
        self.prototype = Number.INSTANCE
        self.number = number or 0

    def __str__(self):
        return str(self.number)


class Boolean(Object):
    INSTANCE = None

    def __init__(self, value=None):
        self.prototype = Boolean.INSTANCE
        self.value = value or False

    def __str__(self):
        return 'true' if self.value else 'false'


class Null(Object):
    INSTANCE = None

    def __init__(self, null=None):
        self.prototype = Null.INSTANCE

    def __str__(self):
        return 'null'  

Object.INSTANCE = Prototype('Object', Function(Object))
Function.INSTANCE = Prototype('Function', Function(Function))
Function.INSTANCE.prototype = Object.INSTANCE
Array.INSTANCE = Prototype('Array', Function(Array))
Prototype.INSTANCE = Prototype('Prototype', Function(Prototype))
String.INSTANCE = Prototype('String', Function(String))
Number.INSTANCE = Prototype('Number', Function(Number))
Boolean.INSTANCE = Prototype('Boolean', Function(Boolean))
Null.INSTANCE = Prototype('Null', Function(Null))

Object.INSTANCE.properties['print'] = Function('print', print)
