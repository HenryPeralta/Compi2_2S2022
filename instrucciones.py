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
    def __init__(self, expLogica, linea, columna, instrucciones = []):
        self.expLogica = expLogica
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

class IfElseIf(Instruccion):
    def __init__(self, expLogica, linea, columna, instrucciones = [], listaElseif = []):
        self.expLogica = expLogica
        self.linea = linea
        self.columna = columna
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

class AsignacionArregloMutable(Instruccion):
    def __init__(self, id, listaexp, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.linea = linea
        self.columna = columna

class AsignacionArregloMutableTipo(Instruccion):
    def __init__(self, id, listaexp, tipo, tamanio, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.tipo = tipo
        self.tamanio = tamanio
        self.linea = linea
        self.columna = columna

class CicloWhile(Instruccion):
    def __init__(self, exp, linea, columna, instrucciones = []):
        self.exp = exp
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

class CicloFor(Instruccion):
    def __init__(self, id, exp1, exp2, instrucciones, linea, columna):
        self.id = id
        self.exp1 = exp1
        self.exp2 = exp2
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna