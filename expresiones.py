from enum import Enum

class OPERACIONES_ARITMETICAS(Enum):
    MAS = 1
    MENOS = 2
    MULTIPLICACION = 3
    DIVISION = 4
    MODULO = 5

class OPERACION_LOGICA(Enum):
    MAYORQUE = 1
    MENORQUE = 2
    IGUALIGUAL = 3
    NOIGUAL = 4
    MAYORIGUAL = 5
    MENORIGUAL = 6

class OPERACION_RELACIONAL(Enum):
    AND = 1
    OR = 2
    NOT = 3

class FUNCIONES_NATIVAS(Enum):
    POW = 1
    POWF = 2
    ABS = 3
    SQRT = 4
    TO_STRING = 5
    CLONE = 6

class FUNCIONES_NATIVAS_VECTORES(Enum):
    NEW = 1
    LEN = 2
    PUSH = 3
    REMOVE = 4
    CONTAINS = 5
    INSERT = 6
    CAPACITY = 7
    WITH_CAPACITY = 8

class ExpresionCadena:
    ''

class ExpresionDobleComilla(ExpresionCadena):
    def __init__(self, val):
        self.val = val

class ExpresionCaracter(ExpresionCadena):
    def __init__(self, exp):
        self.exp = exp

class ExpresionNumerica:
    ''

class ExpresionBinaria(ExpresionNumerica):
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionNegativa(ExpresionNumerica):
    def __init__(self, exp):
        self.exp = exp

class ExpresionNumero(ExpresionNumerica):
    def __init__(self, val=0):
        self.val = val

class ExpresionIdentificador(ExpresionNumerica):
    def __init__(self, id = ""):
        self.id = id

class ExpresionArreglo(ExpresionNumerica):
    def __init__(self, id = "", pos = ""):
        self.id = id
        self.pos = pos

class ExpresionBool(ExpresionNumerica):
    def __init__(self, boolean):
        self.boolean = boolean

class ExpresionLogica():
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionRelacional():
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionFnLen():
    def __init__(self, exp, tipo):
        self.exp = exp
        self.tipo = tipo

class ExpresionParametro():
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo

class ExpresionAbs():
    def __init__(self, exp, tipo):
        self.exp = exp
        self.tipo = tipo

class ExpresionSqrt():
    def __init__(self, exp, tipo):
        self.exp = exp
        self.tipo = tipo

class ExpresionToString():
    def __init__(self, exp, tipo):
        self.exp = exp
        self.tipo = tipo