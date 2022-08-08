from datetime import datetime
import gramatica as g
import tab_simbolos as TABS
import tab_errores as TABE
from expresiones import *
from instrucciones import *

mensaje = ""

def instruccion_println(instruccion, ts, ambito):
    global mensaje
    mensaje += str(resolver_general(instruccion.exp, ts, ambito)) + '\n'

def instruccion_print(instruccion, ts, ambito):
    global mensaje
    mensaje += str(resolver_general(instruccion.exp, ts, ambito))

def resolver_general(exp, ts, ambito):
    if(isinstance(exp, ExpresionDobleComilla)):
        return exp.val
    elif(isinstance(exp, ExpresionBool)):
        return exp.boolean
    elif(isinstance(exp, ExpresionCaracter)):
        return exp.exp
    elif(isinstance(exp, ExpresionNegativa)):
        exp = resolver_general(exp.exp, ts, ambito)
        return exp*-1
    elif(isinstance(exp, ExpresionIdentificador)):
        simbolo = TABS .Simbolo(exp.id, "", "", "",0,0)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            return ts.obtener(exp.id).valor
        else:
            print(ts.obtener(exp.id))
    elif(isinstance(exp, ExpresionNumero)):
        return exp.val
    elif(isinstance(exp, ExpresionBinaria)):
        exp1 = resolver_general(exp.exp1, ts, ambito)
        exp2 = resolver_general(exp.exp2, ts, ambito)
        if(exp.operador == OPERACIONES_ARITMETICAS.MAS):
            return exp1 + exp2
        if(exp.operador == OPERACIONES_ARITMETICAS.MENOS):
            return exp1 - exp2
        if(exp.operador == OPERACIONES_ARITMETICAS.MULTIPLICACION):
            if((type(exp1) == int or type(exp1) == float) and (type(exp2) == float or type(exp2) == int)):
                return exp1 * exp2
            else:
                return str(exp1) + str(exp2)
        if(exp.operador == OPERACIONES_ARITMETICAS.DIVISION):
            return exp1 / exp2
        if(exp.operador == OPERACIONES_ARITMETICAS.MODULO):
            return exp1 % exp2
    elif(isinstance(exp, ExpresionLogica)):
        return (resolver_logica(exp, ts, ambito))
    elif(isinstance(exp, ExpresionRelacional)):
        return (resolver_relacional(exp, ts, ambito))

def resolver_logica(expLogica, ts, ambito):
    exp1 = resolver_general(expLogica.exp1, ts, ambito)
    exp2 = resolver_general(expLogica.exp2, ts, ambito)
    if(expLogica.operador == OPERACION_LOGICA.MAYORQUE):
        return exp1 > exp2
    elif(expLogica.operador == OPERACION_LOGICA.MENORQUE):
        return exp1 < exp2
    elif(expLogica.operador == OPERACION_LOGICA.IGUALIGUAL):
        return exp1 == exp2
    elif(expLogica.operador == OPERACION_LOGICA.NOIGUAL):
        return exp1 != exp2
    elif(expLogica.operador == OPERACION_LOGICA.MAYORIGUAL):
        return exp1 >= exp2
    elif(expLogica.operador == OPERACION_LOGICA.MENORIGUAL):
        return exp1 <= exp2

def resolver_relacional(expRelacional, ts, ambito):
    if(expRelacional.operador != OPERACION_RELACIONAL.NOT):
        exp1 = resolver_general(expRelacional.exp1, ts, ambito)
        exp2 = resolver_general(expRelacional.exp2, ts, ambito)
    if(expRelacional.operador == OPERACION_RELACIONAL.AND):
        return (exp1 and exp2)
    elif(expRelacional.operador == OPERACION_RELACIONAL.OR):
        return (exp1 or exp2)
    elif(expRelacional.operador == OPERACION_RELACIONAL.NOT):
        return not exp2

def instruccion_asignacion_mutable(asignacion, ts, ambito):
    valor = resolver_general(asignacion.exp, ts, ambito)
    if(isinstance(valor, bool)):
        simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.BOOL, valor, ambito, asignacion.linea, asignacion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(isinstance(valor, int)):
        simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.I64, valor, ambito, asignacion.linea, asignacion.columna)    
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(isinstance(valor,float)):
        simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.F64, valor, ambito, asignacion.linea, asignacion.columna)    
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(isinstance(valor, str)):
        if(len(valor) == 1):
            simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.CHAR, valor, ambito, asignacion.linea, asignacion.columna)    
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.STRING, valor, ambito, asignacion.linea, asignacion.columna)    
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)

def instruccion_asignacion_mutable_tipo(asignacion, ts, ambito):
    global mensaje
    valor = resolver_general(asignacion.exp, ts, ambito)
    if(isinstance(valor, bool)):
        if(TABS.TIPO_DATO.BOOL == asignacion.tipo):
            simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.BOOL, valor, ambito, asignacion.linea, asignacion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el valor del tipo no coincide con el valor de la expresion \n"
            mensaje = mensajeE
            e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
            TABE.agregarError(e)
    elif(isinstance(valor, int)):
        if(TABS.TIPO_DATO.I64 == asignacion.tipo):
            simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.I64, valor, ambito, asignacion.linea, asignacion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el valor del tipo no coincide con el valor de la expresion \n"
            mensaje = mensajeE
            e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
            TABE.agregarError(e)
    elif(isinstance(valor, float)):
        if(TABS.TIPO_DATO.F64 == asignacion.tipo):
            simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.F64, valor, ambito, asignacion.linea, asignacion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el valor del tipo no coincide con el valor de la expresion \n"
            mensaje = mensajeE
            e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
            TABE.agregarError(e)
    elif(isinstance(valor, str)):
        if(len(valor) == 1):
            if(TABS.TIPO_DATO.CHAR == asignacion.tipo):
                simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.CHAR, valor, ambito, asignacion.linea, asignacion.columna)
                comprobar = ts.comprobar(simbolo)
                if(comprobar):
                    ts.actualizar(simbolo)
                else:
                    ts.agregar(simbolo)
            else:
                mensajeE = "Error semantico: el valor del tipo no coincide con el valor de la expresion \n"
                mensaje = mensajeE
                e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
                TABE.agregarError(e)
        else:
            if(TABS.TIPO_DATO.STRING == asignacion.tipo):
                simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.STRING, valor, ambito, asignacion.linea, asignacion.columna)
                comprobar = ts.comprobar(simbolo)
                if(comprobar):
                    ts.actualizar(simbolo)
                else:
                    ts.agregar(simbolo)
            else:
                mensajeE = "Error semantico: el valor del tipo no coincide con el valor de la expresion \n"
                mensaje = mensajeE
                e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
                TABE.agregarError(e)

def procesar_instrucciones(instrucciones, ts, ambito):
    global mensaje
    for instruccion in instrucciones:
        if(isinstance(instruccion, Println)):
            instruccion_println(instruccion, ts, ambito)
        elif(isinstance(instruccion,Print)):
            instruccion_print(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionMutable)):
            instruccion_asignacion_mutable(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionMutableTipo)):
            instruccion_asignacion_mutable_tipo(instruccion, ts, ambito)
        else:
            print('Error semantico: Instrucción no válida')

def datos(inputs):
    instrucciones = g.parse(inputs)
    tabs_global = TABS.TablaSimbolos()
    print(instrucciones)
    procesar_instrucciones(instrucciones, tabs_global, "Global")
    TABE.GenerarTablaErrores()
    tabs_global.GenerarTablaSimbolos()
    tabs_global.reiniciar()
    return mensaje