class Instruccion:
    '''
    '''

class Print(Instruccion):
    def __init__(self, exp):
        self.exp = exp

class Println(Instruccion):
    def __init__(self, exp):
        self.exp = exp

class AsignacionMutable(Instruccion):
    def __init__(self, id, exp, linea, columna):
        self.id = id
        self.exp = exp
        self.linea = linea
        self.columna = columna

class AsignacionMutableTipo(Instruccion):
    def __init__(self, id, exp, tipo, linea, columna):
        self.id = id
        self.exp = exp
        self.tipo = tipo
        self.linea = linea
        self.columna = columna