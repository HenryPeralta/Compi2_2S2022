class Instruccion:
    '''
    '''

class Print(Instruccion):
    def __init__(self, exp):
        self.exp = exp

class Println(Instruccion):
    def __init__(self, exp):
        self.exp = exp

class PrintEsp(Instruccion):
    def __init__(self, linea, columna, lista=[]):
        self.linea = linea
        self.columna = columna
        self.lista = lista

class PrintlnEsp(Instruccion):
    def __init__(self, linea, columna, lista=[]):
        self.linea = linea
        self.columna = columna
        self.lista = lista

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

class AsignacionArregloNoMutable(Instruccion):
    def __init__(self, id, listaexp, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.linea = linea
        self.columna = columna

class AsignacionArregloNoMutableTipo(Instruccion):
    def __init__(self, id, listaexp, tipo, tamanio, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.tipo = tipo
        self.tamanio = tamanio
        self.linea = linea
        self.columna = columna

class AsignacionNuevoArreglo(Instruccion):
    def __init__(self, id, posicion, valor, linea, columna):
        self.id = id
        self.posicion = posicion
        self.valor = valor
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

class ExisteBreak(Instruccion):
    ""

class ExisteContinue(Instruccion):
    ""

class InstruccionReturn(Instruccion):
    def __init__(self, exp):
        self.exp = exp

class Funcion(Instruccion):
    def __init__(self, id, listaparametro, instrucciones, linea, columna):
        self.id = id
        self.listaparametro = listaparametro
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

class FuncionTipo(Instruccion):
    def __init__(self, id, listaparametro, tipo, instrucciones, linea, columna):
        self.id = id
        self.listaparametro = listaparametro
        self.tipo = tipo
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

class FuncionMain(Instruccion):
    def __init__(self, id, instrucciones, linea, columna):
        self.id = id
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

class LlamadaFuncion(Instruccion):
    def __init__(self, id, listaparametro, linea, columna):
        self.id = id
        self.listaparametro = listaparametro
        self.linea = linea
        self.columna = columna

class AsignacionVectorMutable(Instruccion):
    def __init__(self, id, listaexp, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.linea = linea
        self.columna = columna

class AsignacionVectorMutableTipo(Instruccion):
    def __init__(self, id, listaexp, tipo, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

class AsignacionVectorNoMutable(Instruccion):
    def __init__(self, id, listaexp, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.linea = linea
        self.columna = columna

class AsignacionVectorNoMutableTipo(Instruccion):
    def __init__(self, id, listaexp, tipo, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

class AsignacionVectorVacioMutable(Instruccion):
    def __init__(self, id, tipo, linea, columna):
        self.id = id
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

class AsignacionVectorVacioNoMutable(Instruccion):
    def __init__(self, id, tipo, linea, columna):
        self.id = id
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

class Push(Instruccion):
    def __init__(self, id, exp, linea, columna):
        self.id = id
        self.exp = exp
        self.linea = linea
        self.columna = columna

class Insert(Instruccion):
    def __init__(self, id, pos, exp, linea, columna):
        self.id = id
        self.pos = pos
        self.exp = exp
        self.linea = linea
        self.columna = columna

class Remove(Instruccion):
    def __init__(self, id, pos, linea, columna):
        self.id = id
        self.pos = pos
        self.linea = linea
        self.columna = columna

class RegresoRemove(Instruccion):
    def __init__(self, id, pos):
        self.id = id
        self.pos = pos

class Contains(Instruccion):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp

class InstruccionStruct(Instruccion):
    def __init__(self, id, lista, linea, columna):
        self.id = id
        self.lista = lista
        self.linea = linea
        self.columna = columna

class AsignacionArregloMutableDimensional(Instruccion):
    def __init__(self, id, listaexp, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.linea = linea
        self.columna = columna

class AsignacionArregloMutableTipoDimensional(Instruccion):
    def __init__(self, id, listaexp, tipo, tamanio1, tamanio2, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.tipo = tipo
        self.tamanio1 = tamanio1
        self.tamanio2 = tamanio2
        self.linea = linea
        self.columna = columna

class AsignacionArregloNoMutableDimensional(Instruccion):
    def __init__(self, id, listaexp, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.linea = linea
        self.columna = columna

class AsignacionArregloNoMutableTipoDimensional(Instruccion):
    def __init__(self, id, listaexp, tipo, tamanio1, tamanio2, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.tipo = tipo
        self.tamanio1 = tamanio1
        self.tamanio2 = tamanio2
        self.linea = linea
        self.columna = columna

class AsignacionNuevoArregloDimensional(Instruccion):
    def __init__(self, id, posicion1, posicion2, valor, linea, columna):
        self.id = id
        self.posicion1 = posicion1
        self.posicion2 = posicion2
        self.valor = valor
        self.linea = linea
        self.columna = columna

class AsignacionArregloMutableDimensional3x3(Instruccion):
    def __init__(self, id, listaexp, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.linea = linea
        self.columna = columna

class AsignacionArregloMutableTipoDimensional3x3(Instruccion):
    def __init__(self, id, listaexp, tipo, tamanio1, tamanio2, tamanio3, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.tipo = tipo
        self.tamanio1 = tamanio1
        self.tamanio2 = tamanio2
        self.tamanio3 = tamanio3
        self.linea = linea
        self.columna = columna

class AsignacionArregloNoMutableDimensional3x3(Instruccion):
    def __init__(self, id, listaexp, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.linea = linea
        self.columna = columna

class AsignacionArregloNoMutableTipoDimensional3x3(Instruccion):
    def __init__(self, id, listaexp, tipo, tamanio1, tamanio2, tamanio3, linea, columna):
        self.id = id
        self.listaexp = listaexp
        self.tipo = tipo
        self.tamanio1 = tamanio1
        self.tamanio2 = tamanio2
        self.tamanio3 = tamanio3
        self.linea = linea
        self.columna = columna

class AsignacionNuevoArregloDimensional3x3(Instruccion):
    def __init__(self, id, posicion1, posicion2, posicion3, valor, linea, columna):
        self.id = id
        self.posicion1 = posicion1
        self.posicion2 = posicion2
        self.posicion3 = posicion3
        self.valor = valor
        self.linea = linea
        self.columna = columna

class AsignacionStruct(Instruccion):
    def __init__(self, id, ids, lista, linea, columna):
        self.id = id
        self.ids = ids
        self.lista = lista
        self.linea = linea
        self.columna = columna

class AsignacionValorStruct(Instruccion):
    def __init__(self, id1, id2, exp, linea, columna):
        self.id1 = id1
        self.id2 = id2
        self.exp = exp
        self.linea = linea
        self.columna = columna