class Object:
    PROTOTYPE = None

    @classmethod
    def initialize(cls):
        pass

    def __init__(self, prototype=None, properties=None):
        self.prototype = prototype or Object.PROTOTYPE
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
        return self.name

    def constructor(self):
        pass


class Array(Object):
    PROTOTYPE = None

    def __init__(self, array=None):
        self.prototype = Array.PROTOTYPE
        self.array = array or []

    def __str__(self):
        return str(self.array)


Object.PROTOTYPE = Prototype('Object', Function(Object))
Function.PROTOTYPE = Prototype('Function', Function(Function))
Function.PROTOTYPE.prototype = Object.PROTOTYPE
Array.PROTOTYPE = Prototype('Array', Function(Array))
Prototype.PROTOTYPE = Prototype('Prototype', Function(Prototype))

Object.PROTOTYPE.properties['print'] = Function('print', print)
