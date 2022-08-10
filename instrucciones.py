class Instruccion:
    '''
    '''

class Print(Instruccion):
    def __init__(self, exp):
        self.exp = exp

class Println(Instruccion):
    def __init__(self, exp):
        self.exp = exp

class IF(Instruccion):
    def __init__(self, expLogica, instrucciones = []):
        self.expLogica = expLogica
        self.instrucciones = instrucciones

class IfElseIf(Instruccion):
    def __init__(self, expLogica, instrucciones = [], listaElseif = []):
        self.expLogica = expLogica
        self.instrucciones = instrucciones
        self.listaElseif = listaElseif

class ELSE(Instruccion):
    def __init__(self, instrucciones = []):
        self.instrucciones = instrucciones

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

class AsignacionNoMutable(Instruccion):
    def __init__(self, id, exp, linea, columna):
        self.id = id
        self.exp = exp
        self.linea = linea
        self.columna = columna

class AsignacionNoMutableTipo(Instruccion):
    def __init__(self, id, exp, tipo, linea, columna):
        self.id = id
        self.exp = exp
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

class AsignacionNuevoValor(Instruccion):
    def __init__(self, id, exp, linea, columna):
        self.id = id
        self.exp = exp
        self.linea = linea
        self.columna = columna