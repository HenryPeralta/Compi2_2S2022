from datetime import datetime
import gramatica as g
import tab_simbolos as TABS
import tab_errores as TABE
from expresiones import *
from instrucciones import *
import math

mensaje = ""
existeBreak = False
existeContinue = False
existeReturn = False
valorReturn = ""

def instruccion_println(instruccion, ts, ambito):
    global mensaje
    mensaje += str(resolver_general(instruccion.exp, ts, ambito)) + '\n'

def instruccion_print(instruccion, ts, ambito):
    global mensaje
    mensaje += str(resolver_general(instruccion.exp, ts, ambito))

def instruccion_print_esp(instruccion, ts, ambito):
    global mensaje
    listaexp = []
    for n in instruccion.lista:
        listaexp.append(resolver_general(n, ts, ambito))
    if(isinstance(listaexp[0], str)):
        texto = listaexp[0]
        cantllaves = texto.count("{}")
        cantexp = len(listaexp) - 1
        if(cantllaves == cantexp):
            for i in range(cantexp):
                texto = texto.replace("{}", str(listaexp[i+1]), 1)
            mensaje += texto
        else:
            mensajeE = "Error semantico: la cantidad de llaves no coinciden con la cantidad de expresiones \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
            TABE.agregarError(e)
    else:
        mensajeE = "Error semantico: print incorrecto \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_println_esp(instruccion, ts, ambito):
    global mensaje
    listaexp = []
    for n in instruccion.lista:
        listaexp.append(resolver_general(n, ts, ambito))
    if(isinstance(listaexp[0], str)):
        texto = listaexp[0]
        cantllaves = texto.count("{}")
        cantexp = len(listaexp) - 1
        if(cantllaves == cantexp):
            for i in range(cantexp):
                texto = texto.replace("{}", str(listaexp[i+1]), 1)
            mensaje += texto + '\n'
        else:
            mensajeE = "Error semantico: la cantidad de llaves no coinciden con la cantidad de expresiones \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
            TABE.agregarError(e)
    else:
        mensajeE = "Error semantico: print incorrecto \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
        TABE.agregarError(e)

def resolver_general(exp, ts, ambito):
    global mensaje
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
        simbolo = TABS.Simbolo(exp.id, "", "", False, "",0,0)
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
            if((isinstance(exp1, int) and isinstance(exp2, float)) or (isinstance(exp1, float) and isinstance(exp2, int)) or (isinstance(exp1, int) and isinstance(exp2, str)) or (isinstance(exp1, str) and isinstance(exp2, int)) or (isinstance(exp1, int) and isinstance(exp2, bool)) or (isinstance(exp1, bool) and isinstance(exp2, int)) or (isinstance(exp1, float) and isinstance(exp2, str)) or (isinstance(exp1, str) and isinstance(exp2, float)) or (isinstance(exp1, float) and isinstance(exp2, bool)) or (isinstance(exp1, bool) and isinstance(exp2, float)) or (isinstance(exp1, str) and isinstance(exp2, bool)) or (isinstance(exp1, bool) and isinstance(exp2, str))):
                mensajeE = "Error semantico: no se puede sumar diferentes tipos \n"
                mensaje += mensajeE
                e = TABE.Error(mensajeE, ambito, "", "", datetime.now())
                TABE.agregarError(e)
            else:
                return exp1 + exp2
        if(exp.operador == OPERACIONES_ARITMETICAS.MENOS):
            if((type(exp1) == int or type(exp1) == float) and (type(exp2) == float or type(exp2) == int)):
                return exp1 - exp2
            else:
                mensajeE = "Error semantico: no se puede restar diferentes tipos \n"
                mensaje += mensajeE
                e = TABE.Error(mensajeE, ambito, "", "", datetime.now())
                TABE.agregarError(e)
        if(exp.operador == OPERACIONES_ARITMETICAS.MULTIPLICACION):
            if((type(exp1) == int or type(exp1) == float) and (type(exp2) == float or type(exp2) == int)):
                return exp1 * exp2
            else:
                mensajeE = "Error semantico: no se puede multiplicar diferentes tipos \n"
                mensaje += mensajeE
                e = TABE.Error(mensajeE, ambito, "", "", datetime.now())
                TABE.agregarError(e)
        if(exp.operador == OPERACIONES_ARITMETICAS.DIVISION):
            if((type(exp1) == int or type(exp1) == float) and (type(exp2) == float or type(exp2) == int)):
                if(exp2 == 0):
                    mensajeE = "Error semantico: no se puede dividir entre 0 \n"
                    mensaje += mensajeE
                    e = TABE.Error(mensajeE, ambito, "", "", datetime.now())
                    TABE.agregarError(e)
                else:
                    return exp1 / exp2
            else:
                mensajeE = "Error semantico: no se puede dividir diferentes tipos \n"
                mensaje += mensajeE
                e = TABE.Error(mensajeE, ambito, "", "", datetime.now())
                TABE.agregarError(e)
        if(exp.operador == OPERACIONES_ARITMETICAS.MODULO):
            if((type(exp1) == int or type(exp1) == float) and (type(exp2) == float or type(exp2) == int)):
                return exp1 % exp2
            else:
                mensajeE = "Error semantico: no se puede modular diferentes tipos \n"
                mensaje += mensajeE
                e = TABE.Error(mensajeE, ambito, "", "", datetime.now())
                TABE.agregarError(e)
    elif(isinstance(exp, ExpresionLogica)):
        return (resolver_logica(exp, ts, ambito))
    elif(isinstance(exp, ExpresionRelacional)):
        return (resolver_relacional(exp, ts, ambito))
    elif(isinstance(exp, ExpresionArreglo)):
        return (resolver_expresion_arreglo(exp, ts, ambito))
    elif(isinstance(exp, ExpresionFnLen)):
        return (resolver_len(exp, ts, ambito))
    elif(isinstance(exp, ExpresionAbs)):
        return (resolver_abs(exp, ts, ambito))
    elif(isinstance(exp, ExpresionSqrt)):
        return (resolver_sqrt(exp, ts, ambito))
    elif(isinstance(exp, ExpresionToString)):
        return (resolver_to_string(exp, ts, ambito))
    elif(isinstance(exp, LlamadaFuncion)):
        return instruccion_llamada_funcion(exp, ts, ambito)
    elif(isinstance(exp, Contains)):
        return instruccion_contains(exp, ts, ambito)

def resolver_len(expresion, ts, ambito):
    global mensaje
    exp = resolver_general(expresion.exp, ts, ambito)
    if(exp == None):
        print("no existe")
    else:
        if(isinstance(exp, int) or isinstance(exp, float) or isinstance(exp, bool)):
            mensajeE = "Error semantico: la funcion len() no acepta int, float y bool \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, "", "", datetime.now())
            TABE.agregarError(e)
        else:
            return len(exp)

def resolver_abs(expresion, ts, ambito):
    global mensaje
    exp = resolver_general(expresion.exp, ts, ambito)
    if(exp == None):
        print("no existe")
    else:
        if(isinstance(exp, str) or isinstance(exp, bool)):
            mensajeE = "Error semantico: la funcion abs() solo es para valores numericos \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, "", "", datetime.now())
            TABE.agregarError(e)
        else:
            if(exp < 0):
                return (exp * -1)
            else:
                return exp

def resolver_sqrt(expresion, ts, ambito):
    global mensaje
    exp = resolver_general(expresion.exp, ts, ambito)
    if(exp == None):
        print("no existe")
    else:
        if(isinstance(exp, str) or isinstance(exp, bool)):
            mensajeE = "Error semantico: la funcion abs() solo es para valores numericos \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, "", "", datetime.now())
            TABE.agregarError(e)
        else:
            return math.sqrt(exp)

def resolver_to_string(expresion, ts, ambito):
    global mensaje
    exp = resolver_general(expresion.exp, ts, ambito)
    if(exp == None):
        print("no existe")
    else:
        if(isinstance(exp, int) or isinstance(exp, float) or isinstance(exp, bool)):
            mensajeE = "Error semantico: la funcion to_string() solo es para string \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, "", "", datetime.now())
            TABE.agregarError(e)
        else:
            return str(exp)

def resolver_expresion_arreglo(expresion, ts, ambito):
    global mensaje
    identificador = resolver_general(expresion.id, ts, ambito)
    print(identificador)
    if(identificador == None):
        mensajeE = "Error semantico: la variable no existe \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, "", "", datetime.now())
        TABE.agregarError(e)
    else:
        if(isinstance(identificador,list)):
            posicion = resolver_general(expresion.pos, ts, ambito)
            tamanio = len(identificador)
            pos = int(posicion)
            if(pos <= (tamanio - 1)):
                return identificador[posicion]
            else:
                mensajeE = "Error semantico: la posicion excede al tamanio del arreglo \n"
                mensaje += mensajeE
                e = TABE.Error(mensajeE, ambito, "", "", datetime.now())
                TABE.agregarError(e)
        else:
            mensajeE = "Error semantico: la variable no es de tipo arreglo \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, "", "", datetime.now())
            TABE.agregarError(e)

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
        exp2 = resolver_general(expRelacional.exp2, ts, ambito)
        return not exp2

def instruccion_asignacion_mutable(asignacion, ts, ambito):
    global mensaje
    valor = resolver_general(asignacion.exp, ts, ambito)
    if(isinstance(valor, bool)):
        simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.BOOL, valor, True, ambito, asignacion.linea, asignacion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
            #mensajeE = "Error semantico: la variable ya existe \n"
            #mensaje = mensajeE
            #e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
            #TABE.agregarError(e)
        else:
            ts.agregar(simbolo)
    elif(isinstance(valor, int)):
        simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.I64, valor, True, ambito, asignacion.linea, asignacion.columna)    
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
            #mensajeE = "Error semantico: la variable ya existe \n"
            #mensaje = mensajeE
            #e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
            #TABE.agregarError(e)
        else:
            ts.agregar(simbolo)
    elif(isinstance(valor,float)):
        simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.F64, valor, True, ambito, asignacion.linea, asignacion.columna)    
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
            #mensajeE = "Error semantico: la variable ya existe \n"
            #mensaje = mensajeE
            #e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
            #TABE.agregarError(e)
        else:
            ts.agregar(simbolo)
    elif(isinstance(valor, str)):
        if(len(valor) == 1):
            simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.CHAR, valor, True, ambito, asignacion.linea, asignacion.columna)    
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.STRING, valor, True, ambito, asignacion.linea, asignacion.columna)    
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
            simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.BOOL, valor, True, ambito, asignacion.linea, asignacion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el valor del tipo no coincide con el valor de la expresion \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
            TABE.agregarError(e)
    elif(isinstance(valor, int)):
        if(TABS.TIPO_DATO.I64 == asignacion.tipo):
            simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.I64, valor, True, ambito, asignacion.linea, asignacion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el valor del tipo no coincide con el valor de la expresion \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
            TABE.agregarError(e)
    elif(isinstance(valor, float)):
        if(TABS.TIPO_DATO.F64 == asignacion.tipo):
            simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.F64, valor, True, ambito, asignacion.linea, asignacion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el valor del tipo no coincide con el valor de la expresion \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
            TABE.agregarError(e)
    elif(isinstance(valor, str)):
        if(len(valor) == 1):
            if(TABS.TIPO_DATO.CHAR == asignacion.tipo):
                simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.CHAR, valor, True, ambito, asignacion.linea, asignacion.columna)
                comprobar = ts.comprobar(simbolo)
                if(comprobar):
                    ts.actualizar(simbolo)
                else:
                    ts.agregar(simbolo)
            else:
                mensajeE = "Error semantico: el valor del tipo no coincide con el valor de la expresion \n"
                mensaje += mensajeE
                e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
                TABE.agregarError(e)
        else:
            if(TABS.TIPO_DATO.STRING == asignacion.tipo):
                simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.STRING, valor, True, ambito, asignacion.linea, asignacion.columna)
                comprobar = ts.comprobar(simbolo)
                if(comprobar):
                    ts.actualizar(simbolo)
                else:
                    ts.agregar(simbolo)
            else:
                mensajeE = "Error semantico: el valor del tipo no coincide con el valor de la expresion \n"
                mensaje += mensajeE
                e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
                TABE.agregarError(e)

def instruccion_asignacion_no_mutable(asignacion, ts, ambito):
    valor = resolver_general(asignacion.exp, ts, ambito)
    if(isinstance(valor, bool)):
        simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.BOOL, valor, False, ambito, asignacion.linea, asignacion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(isinstance(valor, int)):
        simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.I64, valor, False, ambito, asignacion.linea, asignacion.columna)    
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(isinstance(valor,float)):
        simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.F64, valor, False, ambito, asignacion.linea, asignacion.columna)    
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(isinstance(valor, str)):
        if(len(valor) == 1):
            simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.CHAR, valor, False, ambito, asignacion.linea, asignacion.columna)    
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.STRING, valor, False, ambito, asignacion.linea, asignacion.columna)    
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)

def instruccion_asignacion_no_mutable_tipo(asignacion, ts, ambito):
    global mensaje
    valor = resolver_general(asignacion.exp, ts, ambito)
    if(isinstance(valor, bool)):
        if(TABS.TIPO_DATO.BOOL == asignacion.tipo):
            simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.BOOL, valor, False, ambito, asignacion.linea, asignacion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el valor del tipo no coincide con el valor de la expresion \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
            TABE.agregarError(e)
    elif(isinstance(valor, int)):
        if(TABS.TIPO_DATO.I64 == asignacion.tipo):
            simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.I64, valor, False, ambito, asignacion.linea, asignacion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el valor del tipo no coincide con el valor de la expresion \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
            TABE.agregarError(e)
    elif(isinstance(valor, float)):
        if(TABS.TIPO_DATO.F64 == asignacion.tipo):
            simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.F64, valor, False, ambito, asignacion.linea, asignacion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el valor del tipo no coincide con el valor de la expresion \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
            TABE.agregarError(e)
    elif(isinstance(valor, str)):
        if(len(valor) == 1):
            if(TABS.TIPO_DATO.CHAR == asignacion.tipo):
                simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.CHAR, valor, False, ambito, asignacion.linea, asignacion.columna)
                comprobar = ts.comprobar(simbolo)
                if(comprobar):
                    ts.actualizar(simbolo)
                else:
                    ts.agregar(simbolo)
            else:
                mensajeE = "Error semantico: el valor del tipo no coincide con el valor de la expresion \n"
                mensaje += mensajeE
                e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
                TABE.agregarError(e)
        else:
            if(TABS.TIPO_DATO.STRING == asignacion.tipo):
                simbolo = TABS.Simbolo(asignacion.id, TABS.TIPO_DATO.STRING, valor, False, ambito, asignacion.linea, asignacion.columna)
                comprobar = ts.comprobar(simbolo)
                if(comprobar):
                    ts.actualizar(simbolo)
                else:
                    ts.agregar(simbolo)
            else:
                mensajeE = "Error semantico: el valor del tipo no coincide con el valor de la expresion \n"
                mensaje += mensajeE
                e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
                TABE.agregarError(e)

def instruccion_asignacion_nuevo_valor(asignacion, ts, ambito):
    global mensaje
    existeVar = ts.existeVariable(asignacion.id)
    if(existeVar):
        variable = ts.obtener(asignacion.id)
        if(variable.mutable == True):
            valor = resolver_general(asignacion.exp, ts, ambito)
            if(type(valor) == type(variable.valor)):
                if(type(valor) == str):
                    if(len(valor) == 1 and len(variable.valor) == 1): 
                        ts.actualizarValor(variable, valor)
                    elif(len(valor) != 1 and len(variable.valor) == 1):
                        mensajeE = "Error semantico: los valores no son del mismo tipo \n"
                        mensaje += mensajeE
                        e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
                        TABE.agregarError(e)
                        #print("El valor no es del mismo tipo")
                    elif(len(valor) == 1 and len(variable.valor) != 1):
                        mensajeE = "Error semantico: los valores no son del mismo tipo \n"
                        mensaje += mensajeE
                        e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
                        TABE.agregarError(e)                        
                        #print("El valor no es del mismo tipo")
                    elif(len(valor) != 1 and len(variable.valor) != 1):
                        ts.actualizarValor(variable, valor)
                else:
                    ts.actualizarValor(variable, valor)
            else:
                mensajeE = "Error semantico: los valores no son del mismo tipo \n"
                mensaje += mensajeE
                e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
                TABE.agregarError(e)
                #print("El valor no es del mismo tipo")
        else:
            mensajeE = "Error semantico: la variable no es mutable \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
            TABE.agregarError(e)
            #print("No es mutable")
    else:
        mensajeE = "Error semantico: la variable no existe \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, asignacion.linea, asignacion.columna, datetime.now())
        TABE.agregarError(e)
        #print("La variable no existe")

def instruccion_if(expif, ts, ambito):
    global mensaje
    valor = resolver_general(expif.expLogica, ts, "If_"+ambito)
    if(isinstance(valor, bool)):
        if(valor):
            procesar_instrucciones(expif.instrucciones, ts, "If_"+ambito)
    else:
        mensajeE = "Error semantico: condicion invalida, tiene que devolver un bool \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, expif.linea, expif.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_elseif(expelseif, ts, ambito):
    global mensaje
    valor = resolver_general(expelseif.expLogica, ts, "If_"+ambito)
    if(isinstance(valor, bool)):
        if(valor):
            procesar_instrucciones(expelseif.instrucciones, ts, "If_"+ambito)
        else:
            bandera_else = False;
            for listaif in expelseif.listaElseif:
                if(isinstance(listaif, IF)):
                    valor2 = resolver_general(listaif.expLogica, ts, "If_"+ambito)
                    if(isinstance(valor2, bool)):
                        if(valor2):
                            procesar_instrucciones(listaif.instrucciones, ts, "if_"+ambito)
                            break
                    else:
                        bandera_else = True
                        mensajeE = "Error semantico: condicion invalida, tiene que devolver un bool \n"
                        mensaje += mensajeE
                        e = TABE.Error(mensajeE, ambito, expelseif.linea, expelseif.columna, datetime.now())
                        TABE.agregarError(e)
                elif(isinstance(listaif, ELSE)):
                    if(bandera_else == False):
                        procesar_instrucciones(listaif.instrucciones, ts, "if_"+ambito)
                        break
    else:
        mensajeE = "Error semantico: condicion invalida, tiene que devolver un bool \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, expelseif.linea, expelseif.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_while(instruccion, ts, ambito):
    global existeBreak
    global existeContinue
    global existeReturn
    global mensaje
    expresion = resolver_general(instruccion.exp, ts, "while_"+ambito)
    if(isinstance(expresion, bool)):
        while(expresion):
            procesar_instrucciones(instruccion.instrucciones, ts, "while_"+ambito)
            expresion = resolver_general(instruccion.exp, ts, "while_"+ambito)
            if(existeBreak):
                existeBreak = False
                break
            if(existeContinue):
                existeContinue = False
                continue
            if(existeReturn):
                return valorReturn
    else:
        mensajeE = "Error semantico: condicion invalida, tiene que devolver un bool \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_for(instruccion, ts, ambito):
    global existeBreak
    global existeContinue
    listaArreglo = []
    if(instruccion.exp2 != ""):
        expresion1 = resolver_general(instruccion.exp1, ts, "for_"+ambito)
        asignar = AsignacionMutable(instruccion.id, ExpresionNumero(expresion1), instruccion.linea, instruccion.columna)
        instruccion_asignacion_mutable(asignar, ts, "for_"+ambito)
        expresion2 = resolver_general(instruccion.exp2, ts, "for_"+ambito)
        while(expresion1 < expresion2):
            procesar_instrucciones(instruccion.instrucciones, ts, "for_"+ambito)
            expresion1 = expresion1 + 1
            simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.I64, expresion1, True, "for_"+ambito, instruccion.linea, instruccion.columna)
            ts.actualizar(simbolo)
            if(existeBreak):
                existeBreak = False
                break
            if(existeContinue):
                existeContinue = False
                continue
    else:
        for n in instruccion.exp1:
            listaArreglo.append(resolver_general(n, ts, ambito))
        asignar = AsignacionArregloMutable(instruccion.id, instruccion.exp1, instruccion.linea, instruccion.columna)
        instruccion_asignacion_arreglo_mutable(asignar, ts, "for_"+ambito)
        inicio = 0
        tamlista = len(listaArreglo)
        while(inicio < tamlista):
            simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaArreglo[inicio], True, "for_"+ambito, instruccion.linea, instruccion.columna)
            ts.actualizar(simbolo)
            inicio = inicio + 1
            procesar_instrucciones(instruccion.instrucciones, ts, "for_"+ambito)
            if(existeBreak):
                existeBreak = False
                break
            if(existeContinue):
                existeContinue = False
                continue      

def instruccion_asignacion_arreglo_mutable(instruccion, ts, ambito):
    global mensaje
    listaValor = []
    bandera_i64 = False
    bandera_f64 = False
    bandera_bool = False
    bandera_char = False
    bandera_string = False
    for n in instruccion.listaexp:
        listaValor.append(resolver_general(n, ts, ambito))
    print(listaValor)
    for valor in listaValor:
        if(isinstance(valor, bool)):
            bandera_bool = True
        elif(isinstance(valor, int)):
            bandera_i64 = True
        elif(isinstance(valor, float)):
            bandera_f64 = True
        elif(isinstance(valor, str)):
            if(len(valor) == 1):
                bandera_char = True
            else:
                bandera_string = True
    if(bandera_i64 == True and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, True, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == True and bandera_bool == False and bandera_char == False and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, True, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == True and bandera_char == False and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, True, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == True and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, True, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == True):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, True, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    else:
        mensajeE = "Error semantico: los valores del arreglo no son del mismo tipo \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_asignacion_arreglo_mutable_tipo(instruccion, ts, ambito):
    global mensaje
    listaValor = []
    bandera_i64 = False
    bandera_f64 = False
    bandera_bool = False
    bandera_char = False
    bandera_string = False
    for n in instruccion.listaexp:
        listaValor.append(resolver_general(n, ts, ambito))
    tamanio = resolver_general(instruccion.tamanio, ts, ambito)
    if(isinstance(tamanio, int)):
        if(tamanio == len(listaValor)):
            for valor in listaValor:
                if(isinstance(valor, bool)):
                    bandera_bool = True
                elif(isinstance(valor, int)):
                    bandera_i64 = True
                elif(isinstance(valor, float)):
                    bandera_f64 = True
                elif(isinstance(valor, str)):
                    if(len(valor) == 1):
                        bandera_char = True
                    else:
                        bandera_string = True
            if(bandera_i64 == True and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == False):
                if(TABS.TIPO_DATO.I64 == instruccion.tipo):
                    simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, True, ambito, instruccion.linea, instruccion.columna)
                    comprobar = ts.comprobar(simbolo)
                    if(comprobar):
                        ts.actualizar(simbolo)
                    else:
                        ts.agregar(simbolo)
                else:
                    mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
                    mensaje += mensajeE
                    e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
                    TABE.agregarError(e)
            elif(bandera_i64 == False and bandera_f64 == True and bandera_bool == False and bandera_char == False and bandera_string == False):
                if(TABS.TIPO_DATO.F64 == instruccion.tipo):
                    simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, True, ambito, instruccion.linea, instruccion.columna)
                    comprobar = ts.comprobar(simbolo)
                    if(comprobar):
                        ts.actualizar(simbolo)
                    else:
                        ts.agregar(simbolo)
                else:
                    mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
                    mensaje += mensajeE
                    e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
                    TABE.agregarError(e)
            elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == True and bandera_char == False and bandera_string == False):
                if(TABS.TIPO_DATO.BOOL == instruccion.tipo):
                    simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, True, ambito, instruccion.linea, instruccion.columna)
                    comprobar = ts.comprobar(simbolo)
                    if(comprobar):
                        ts.actualizar(simbolo)
                    else:
                        ts.agregar(simbolo)
                else:
                    mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
                    mensaje += mensajeE
                    e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
                    TABE.agregarError(e)
            elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == True and bandera_string == False):
                if(TABS.TIPO_DATO.CHAR == instruccion.tipo):
                    simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, True, ambito, instruccion.linea, instruccion.columna)
                    comprobar = ts.comprobar(simbolo)
                    if(comprobar):
                        ts.actualizar(simbolo)
                    else:
                        ts.agregar(simbolo)
                else:
                    mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
                    mensaje += mensajeE
                    e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
                    TABE.agregarError(e)
            elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == True):
                if(TABS.TIPO_DATO.STRING == instruccion.tipo):
                    simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, True, ambito, instruccion.linea, instruccion.columna)
                    comprobar = ts.comprobar(simbolo)
                    if(comprobar):
                        ts.actualizar(simbolo)
                    else:
                        ts.agregar(simbolo)
                else:
                    mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
                    mensaje += mensajeE
                    e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
                    TABE.agregarError(e)
            else:
                mensajeE = "Error semantico: los valores del arreglo no son del mismo tipo \n"
                mensaje += mensajeE
                e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
                TABE.agregarError(e)
        else:
            mensajeE = "Error semantico: el tamanio del arreglo no coincide \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
            TABE.agregarError(e)
    else:
        mensajeE = "Error semantico: el valor del tamaño debe ser un entero \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_asignacion_arreglo_no_mutable(instruccion, ts, ambito):
    global mensaje
    listaValor = []
    bandera_i64 = False
    bandera_f64 = False
    bandera_bool = False
    bandera_char = False
    bandera_string = False
    for n in instruccion.listaexp:
        listaValor.append(resolver_general(n, ts, ambito))
    for valor in listaValor:
        if(isinstance(valor, bool)):
            bandera_bool = True
        elif(isinstance(valor, int)):
            bandera_i64 = True
        elif(isinstance(valor, float)):
            bandera_f64 = True
        elif(isinstance(valor, str)):
            if(len(valor) == 1):
                bandera_char = True
            else:
                bandera_string = True
    if(bandera_i64 == True and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, False, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == True and bandera_bool == False and bandera_char == False and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, False, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == True and bandera_char == False and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, False, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == True and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, False, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == True):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, False, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    else:
        mensajeE = "Error semantico: los valores del arreglo no son del mismo tipo \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_asignacion_arreglo_no_mutable_tipo(instruccion, ts, ambito):
    global mensaje
    listaValor = []
    bandera_i64 = False
    bandera_f64 = False
    bandera_bool = False
    bandera_char = False
    bandera_string = False
    for n in instruccion.listaexp:
        listaValor.append(resolver_general(n, ts, ambito))
    tamanio = resolver_general(instruccion.tamanio, ts, ambito)
    if(isinstance(tamanio, int)):
        if(tamanio == len(listaValor)):
            for valor in listaValor:
                if(isinstance(valor, bool)):
                    bandera_bool = True
                elif(isinstance(valor, int)):
                    bandera_i64 = True
                elif(isinstance(valor, float)):
                    bandera_f64 = True
                elif(isinstance(valor, str)):
                    if(len(valor) == 1):
                        bandera_char = True
                    else:
                        bandera_string = True
            if(bandera_i64 == True and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == False):
                if(TABS.TIPO_DATO.I64 == instruccion.tipo):
                    simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, False, ambito, instruccion.linea, instruccion.columna)
                    comprobar = ts.comprobar(simbolo)
                    if(comprobar):
                        ts.actualizar(simbolo)
                    else:
                        ts.agregar(simbolo)
                else:
                    mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
                    mensaje += mensajeE
                    e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
                    TABE.agregarError(e)
            elif(bandera_i64 == False and bandera_f64 == True and bandera_bool == False and bandera_char == False and bandera_string == False):
                if(TABS.TIPO_DATO.F64 == instruccion.tipo):
                    simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, False, ambito, instruccion.linea, instruccion.columna)
                    comprobar = ts.comprobar(simbolo)
                    if(comprobar):
                        ts.actualizar(simbolo)
                    else:
                        ts.agregar(simbolo)
                else:
                    mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
                    mensaje += mensajeE
                    e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
                    TABE.agregarError(e)
            elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == True and bandera_char == False and bandera_string == False):
                if(TABS.TIPO_DATO.BOOL == instruccion.tipo):
                    simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, False, ambito, instruccion.linea, instruccion.columna)
                    comprobar = ts.comprobar(simbolo)
                    if(comprobar):
                        ts.actualizar(simbolo)
                    else:
                        ts.agregar(simbolo)
                else:
                    mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
                    mensaje += mensajeE
                    e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
                    TABE.agregarError(e)
            elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == True and bandera_string == False):
                if(TABS.TIPO_DATO.CHAR == instruccion.tipo):
                    simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, False, ambito, instruccion.linea, instruccion.columna)
                    comprobar = ts.comprobar(simbolo)
                    if(comprobar):
                        ts.actualizar(simbolo)
                    else:
                        ts.agregar(simbolo)
                else:
                    mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
                    mensaje += mensajeE
                    e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
                    TABE.agregarError(e)
            elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == True):
                if(TABS.TIPO_DATO.STRING == instruccion.tipo):
                    simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.ARREGLO, listaValor, False, ambito, instruccion.linea, instruccion.columna)
                    comprobar = ts.comprobar(simbolo)
                    if(comprobar):
                        ts.actualizar(simbolo)
                    else:
                        ts.agregar(simbolo)
                else:
                    mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
                    mensaje += mensajeE
                    e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
                    TABE.agregarError(e)
            else:
                mensajeE = "Error semantico: los valores del arreglo no son del mismo tipo \n"
                mensaje += mensajeE
                e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
                TABE.agregarError(e)
        else:
            mensajeE = "Error semantico: el tamanio del arreglo no coincide \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
            TABE.agregarError(e)
    else:
        mensajeE = "Error semantico: el valor del tamaño debe ser un entero \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_asignacion_nuevo_arreglo(instruccion, ts, ambito):
    global mensaje
    existeVar = ts.existeVariable(instruccion.id)
    if(existeVar):
        variable = ts.obtener(instruccion.id)
        variableN = variable
        posiciona = resolver_general(instruccion.posicion, ts, ambito)
        if(isinstance(posiciona, int)):
            if(variable.mutable == True):
                tamanio = len(variableN.valor)
                valornuevo = resolver_general(instruccion.valor, ts, ambito)
                if(posiciona >= tamanio):
                    mensajeE = "Error semantico: el rango es mayor que el tamanio del arreglo \n"
                    mensaje += mensajeE
                    e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
                    TABE.agregarError(e)
                else:
                    for valorarreglo in range(tamanio):
                        if(posiciona == valorarreglo):
                            variableN.valor[valorarreglo] = valornuevo
                    ts.actualizarValor(variable, variableN.valor)
            else:
                mensajeE = "Error semantico: el arreglo no es mutable \n"
                mensaje += mensajeE
                e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
                TABE.agregarError(e)
        else:
            mensajeE = "Error semantico: la posicion del arreglo no es un entero \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
            TABE.agregarError(e)
    else:
        mensajeE = "Error semantico: la variable no ha sido declarada \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_asignacion_vector_mutable(instruccion, ts, ambito):
    global mensaje
    listaValor = []
    bandera_i64 = False
    bandera_f64 = False
    bandera_bool = False
    bandera_char = False
    bandera_string = False
    for n in instruccion.listaexp:
        listaValor.append(resolver_general(n, ts, ambito))
    for valor in listaValor:
        if(isinstance(valor, bool)):
            bandera_bool = True
        elif(isinstance(valor, int)):
            bandera_i64 = True
        elif(isinstance(valor, float)):
            bandera_f64 = True
        elif(isinstance(valor, str)):
            if(len(valor) == 1):
                bandera_char = True
            else:
                bandera_string = True
    if(bandera_i64 == True and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, True, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == True and bandera_bool == False and bandera_char == False and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, True, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == True and bandera_char == False and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, True, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == True and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, True, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == True):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, True, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    else:
        mensajeE = "Error semantico: los valores del vector no son del mismo tipo \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_asignacion_vector_mutable_tipo(instruccion, ts, ambito):
    global mensaje
    listaValor = []
    bandera_i64 = False
    bandera_f64 = False
    bandera_bool = False
    bandera_char = False
    bandera_string = False
    for n in instruccion.listaexp:
        listaValor.append(resolver_general(n, ts, ambito))
    for valor in listaValor:
        if(isinstance(valor, bool)):
            bandera_bool = True
        elif(isinstance(valor, int)):
            bandera_i64 = True
        elif(isinstance(valor, float)):
            bandera_f64 = True
        elif(isinstance(valor, str)):
            if(len(valor) == 1):
                bandera_char = True
            else:
                bandera_string = True
    if(bandera_i64 == True and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == False):
        if(TABS.TIPO_DATO.I64 == instruccion.tipo):
            simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, True, ambito, instruccion.linea, instruccion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
            TABE.agregarError(e)
    elif(bandera_i64 == False and bandera_f64 == True and bandera_bool == False and bandera_char == False and bandera_string == False):
        if(TABS.TIPO_DATO.F64 == instruccion.tipo):
            simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, True, ambito, instruccion.linea, instruccion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
            TABE.agregarError(e)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == True and bandera_char == False and bandera_string == False):
        if(TABS.TIPO_DATO.BOOL == instruccion.tipo):
            simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, True, ambito, instruccion.linea, instruccion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
            TABE.agregarError(e)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == True and bandera_string == False):
        if(TABS.TIPO_DATO.CHAR == instruccion.tipo):
            simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, True, ambito, instruccion.linea, instruccion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
            TABE.agregarError(e)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == True):
        if(TABS.TIPO_DATO.STRING == instruccion.tipo):
            simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, True, ambito, instruccion.linea, instruccion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
            TABE.agregarError(e)
    else:
        mensajeE = "Error semantico: los valores del arreglo no son del mismo tipo \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_asignacion_vector_no_mutable(instruccion, ts, ambito):
    global mensaje
    listaValor = []
    bandera_i64 = False
    bandera_f64 = False
    bandera_bool = False
    bandera_char = False
    bandera_string = False
    for n in instruccion.listaexp:
        listaValor.append(resolver_general(n, ts, ambito))
    for valor in listaValor:
        if(isinstance(valor, bool)):
            bandera_bool = True
        elif(isinstance(valor, int)):
            bandera_i64 = True
        elif(isinstance(valor, float)):
            bandera_f64 = True
        elif(isinstance(valor, str)):
            if(len(valor) == 1):
                bandera_char = True
            else:
                bandera_string = True
    if(bandera_i64 == True and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, False, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == True and bandera_bool == False and bandera_char == False and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, False, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == True and bandera_char == False and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, False, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == True and bandera_string == False):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, False, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == True):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, False, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    else:
        mensajeE = "Error semantico: los valores del vector no son del mismo tipo \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_asignacion_vector_no_mutable_tipo(instruccion, ts, ambito):
    global mensaje
    listaValor = []
    bandera_i64 = False
    bandera_f64 = False
    bandera_bool = False
    bandera_char = False
    bandera_string = False
    for n in instruccion.listaexp:
        listaValor.append(resolver_general(n, ts, ambito))
    for valor in listaValor:
        if(isinstance(valor, bool)):
            bandera_bool = True
        elif(isinstance(valor, int)):
            bandera_i64 = True
        elif(isinstance(valor, float)):
            bandera_f64 = True
        elif(isinstance(valor, str)):
            if(len(valor) == 1):
                bandera_char = True
            else:
                bandera_string = True
    if(bandera_i64 == True and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == False):
        if(TABS.TIPO_DATO.I64 == instruccion.tipo):
            simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, False, ambito, instruccion.linea, instruccion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
            TABE.agregarError(e)
    elif(bandera_i64 == False and bandera_f64 == True and bandera_bool == False and bandera_char == False and bandera_string == False):
        if(TABS.TIPO_DATO.F64 == instruccion.tipo):
            simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, False, ambito, instruccion.linea, instruccion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
            TABE.agregarError(e)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == True and bandera_char == False and bandera_string == False):
        if(TABS.TIPO_DATO.BOOL == instruccion.tipo):
            simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, False, ambito, instruccion.linea, instruccion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
            TABE.agregarError(e)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == True and bandera_string == False):
        if(TABS.TIPO_DATO.CHAR == instruccion.tipo):
            simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, False, ambito, instruccion.linea, instruccion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
            TABE.agregarError(e)
    elif(bandera_i64 == False and bandera_f64 == False and bandera_bool == False and bandera_char == False and bandera_string == True):
        if(TABS.TIPO_DATO.STRING == instruccion.tipo):
            simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, False, ambito, instruccion.linea, instruccion.columna)
            comprobar = ts.comprobar(simbolo)
            if(comprobar):
                ts.actualizar(simbolo)
            else:
                ts.agregar(simbolo)
        else:
            mensajeE = "Error semantico: el tipo no coincide con los valores del arreglo \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
            TABE.agregarError(e)
    else:
        mensajeE = "Error semantico: los valores del arreglo no son del mismo tipo \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_asignacion_vector_vacio_mutable(instruccion, ts, ambito):
    global mensaje
    listaValor = []
    print("Estoy en el metodo")
    if(TABS.TIPO_DATO.I64 == instruccion.tipo):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, True, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(TABS.TIPO_DATO.F64 == instruccion.tipo):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, True, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(TABS.TIPO_DATO.BOOL == instruccion.tipo):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, True, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(TABS.TIPO_DATO.CHAR == instruccion.tipo):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, True, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(TABS.TIPO_DATO.STRING == instruccion.tipo):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, True, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    else:
        mensajeE = "Error semantico: el tipo no es correcto \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_asignacion_vector_vacio_no_mutable(instruccion, ts, ambito):
    global mensaje
    listaValor = []
    print("Estoy en el metodo")
    if(TABS.TIPO_DATO.I64 == instruccion.tipo):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, False, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(TABS.TIPO_DATO.F64 == instruccion.tipo):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, False, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(TABS.TIPO_DATO.BOOL == instruccion.tipo):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, False, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(TABS.TIPO_DATO.CHAR == instruccion.tipo):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, False, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    elif(TABS.TIPO_DATO.STRING == instruccion.tipo):
        simbolo = TABS.Simbolo(instruccion.id, TABS.TIPO_DATO.VEC, listaValor, False, ambito, instruccion.linea, instruccion.columna)
        comprobar = ts.comprobar(simbolo)
        if(comprobar):
            ts.actualizar(simbolo)
        else:
            ts.agregar(simbolo)
    else:
        mensajeE = "Error semantico: el tipo no es correcto \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, instruccion.linea, instruccion.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_funcion(funcion, ts, ambito):
    fuction = TABS.Funcion(funcion.id, funcion.listaparametro, "", funcion.instrucciones, ambito, funcion.linea, funcion.columna)
    comprobar = ts.comprobar_funcion(fuction)
    if(comprobar):
        ts.actualizar_funcion(fuction)
        print("Se actualizo la funcion")
    else:
        ts.agregar_funcion(fuction)
        print("Se agrego la funcion")

def instruccion_funcion_main(funcion, ts, ambito):
    fuction = TABS.Funcion(funcion.id, [], "", funcion.instrucciones, ambito, funcion.linea, funcion.columna)
    comprobar = ts.comprobar_funcion(fuction)
    if(comprobar):
        ts.actualizar_funcion(fuction)
        procesar_instrucciones(funcion.instrucciones, ts, ambito)
    else:
        ts.agregar_funcion(fuction)
        procesar_instrucciones(funcion.instrucciones, ts, ambito)

def instruccion_llamada_funcion(funcion, ts, ambito):
    global existeReturn
    global mensaje
    aux = TABS.Funcion(funcion.id, "","", "", "", 0, 0)
    comprobar = ts.comprobar_funcion(aux)
    if(comprobar):
        llamada = ts.obtener_funcion(funcion.id)
        if(len(llamada.listaparametros) == len(funcion.listaparametro)):
            ListaSimbolo = []
            simbolo = {}
            nuevoTS = TABS.TablaSimbolos(simbolo)
            if(len(funcion.listaparametro) != 0):
                x = 0
                for n in llamada.listaparametros:
                    valor = resolver_general(funcion.listaparametro[x], ts, "funcion_"+ambito)
                    simbolo = TABS.Simbolo(n.id, TABS.TIPO_DATO.ARREGLO, valor, True, "funcion_"+ambito, funcion.linea, funcion.columna)
                    ListaSimbolo.append(simbolo)
                    x+=1
                nuevoTS.simbolos = ts.simbolos.copy()
                for n in ListaSimbolo:
                    nuevoTS.agregar(n)
                procesar_instrucciones(llamada.instruccion, nuevoTS, "funcion_"+ambito)
                for i in nuevoTS.simbolos:
                    ts.agregar_simbolos_funciones(nuevoTS.simbolos[i])
                if(existeReturn):
                    if(llamada.tipo == ""):
                        existeReturn = False
                        return valorReturn
                    else:
                        if(isinstance(valorReturn, bool)):
                            if(TABS.TIPO_DATO.BOOL == llamada.tipo):
                                existeReturn = False
                                return valorReturn
                            else:
                                mensajeE = "Error semantico: valor de retorno no valido \n"
                                mensaje += mensajeE
                                e = TABE.Error(mensajeE, ambito, funcion.linea, funcion.columna, datetime.now())
                                TABE.agregarError(e)
                        elif(isinstance(valorReturn, int)):
                            if(TABS.TIPO_DATO.I64 == llamada.tipo):
                                existeReturn = False
                                return valorReturn
                            else:
                                mensajeE = "Error semantico: valor de retorno no valido \n"
                                mensaje += mensajeE
                                e = TABE.Error(mensajeE, ambito, funcion.linea, funcion.columna, datetime.now())
                                TABE.agregarError(e)
                        elif(isinstance(valorReturn, float)):
                            if(TABS.TIPO_DATO.F64 == llamada.tipo):
                                existeReturn = False
                                return valorReturn
                            else:
                                mensajeE = "Error semantico: valor de retorno no valido \n"
                                mensaje += mensajeE
                                e = TABE.Error(mensajeE, ambito, funcion.linea, funcion.columna, datetime.now())
                                TABE.agregarError(e)
                        elif(isinstance(valorReturn, str)):
                            if(len(valorReturn) == 1):
                                if(TABS.TIPO_DATO.CHAR == llamada.tipo):
                                    existeReturn = False
                                    return valorReturn
                                else:
                                    mensajeE = "Error semantico: valor de retorno no valido \n"
                                    mensaje += mensajeE
                                    e = TABE.Error(mensajeE, ambito, funcion.linea, funcion.columna, datetime.now())
                                    TABE.agregarError(e)
                            else:
                                if(TABS.TIPO_DATO.STRING == llamada.tipo):
                                    existeReturn = False
                                    return valorReturn
                                else:
                                    mensajeE = "Error semantico: valor de retorno no valido \n"
                                    mensaje += mensajeE
                                    e = TABE.Error(mensajeE, ambito, funcion.linea, funcion.columna, datetime.now())
                                    TABE.agregarError(e)
            else:
                x = 0
                for n in llamada.listaparametros:
                    asignar = AsignacionMutable(n.id, funcion.listaparametro[x], funcion.linea, funcion.columna)
                    instruccion_asignacion_mutable(asignar, ts, "funcion_"+ambito)
                    x+=1
                nuevoTS.simbolos = ts.simbolos.copy()
                procesar_instrucciones(llamada.instruccion, nuevoTS, "funcion_"+ambito)
                for i in nuevoTS.simbolos:
                    ts.agregar_simbolos_funciones(nuevoTS.simbolos[i])
                if(existeReturn):
                    if(llamada.tipo == ""):
                        existeReturn = False
                        return valorReturn
                    else:
                        if(isinstance(valorReturn, bool)):
                            if(TABS.TIPO_DATO.BOOL == llamada.tipo):
                                existeReturn = False
                                return valorReturn
                            else:
                                mensajeE = "Error semantico: valor de retorno no valido \n"
                                mensaje += mensajeE
                                e = TABE.Error(mensajeE, ambito, funcion.linea, funcion.columna, datetime.now())
                                TABE.agregarError(e)
                        elif(isinstance(valorReturn, int)):
                            if(TABS.TIPO_DATO.I64 == llamada.tipo):
                                existeReturn = False
                                return valorReturn
                            else:
                                mensajeE = "Error semantico: valor de retorno no valido \n"
                                mensaje += mensajeE
                                e = TABE.Error(mensajeE, ambito, funcion.linea, funcion.columna, datetime.now())
                                TABE.agregarError(e)
                        elif(isinstance(valorReturn, float)):
                            if(TABS.TIPO_DATO.F64 == llamada.tipo):
                                existeReturn = False
                                return valorReturn
                            else:
                                mensajeE = "Error semantico: valor de retorno no valido \n"
                                mensaje += mensajeE
                                e = TABE.Error(mensajeE, ambito, funcion.linea, funcion.columna, datetime.now())
                                TABE.agregarError(e)
                        elif(isinstance(valorReturn, str)):
                            if(len(valorReturn) == 1):
                                if(TABS.TIPO_DATO.CHAR == llamada.tipo):
                                    existeReturn = False
                                    return valorReturn
                                else:
                                    mensajeE = "Error semantico: valor de retorno no valido \n"
                                    mensaje += mensajeE
                                    e = TABE.Error(mensajeE, ambito, funcion.linea, funcion.columna, datetime.now())
                                    TABE.agregarError(e)
                            else:
                                if(TABS.TIPO_DATO.STRING == llamada.tipo):
                                    existeReturn = False
                                    return valorReturn
                                else:
                                    mensajeE = "Error semantico: valor de retorno no valido \n"
                                    mensaje += mensajeE
                                    e = TABE.Error(mensajeE, ambito, funcion.linea, funcion.columna, datetime.now())
                                    TABE.agregarError(e)
        else:
            mensajeE = "Error semantico: la cantidad no coincide con los parametros del arreglo \n"
            mensaje += mensajeE
            e = TABE.Error(mensajeE, ambito, funcion.linea, funcion.columna, datetime.now())
            TABE.agregarError(e)
    else:
        print("Aqui va la parte de los structs")

def instruccion_funcion_tipo(funcion, ts, ambito):
    print(funcion.tipo)
    fuction = TABS.Funcion(funcion.id, funcion.listaparametro, funcion.tipo, funcion.instrucciones, ambito, funcion.linea, funcion.columna)
    print(fuction)
    comprobar = ts.comprobar_funcion(fuction)
    if(comprobar):
        ts.actualizar_funcion(fuction)
        print("Se actualizo la funcion")
    else:
        ts.agregar_funcion(fuction)
        print("Se agrego la funcion")

def instruccion_push(exp, ts, ambito):
    global mensaje
    simbolo = TABS.Simbolo(exp.id, "", "", "", "", 0, 0)
    comprobar = ts.comprobar(simbolo)
    if(comprobar):
        expresion = resolver_general(exp.exp, ts, ambito)
        lista = ts.obtener(exp.id).valor
        lista.append(expresion)
    else:
        mensajeE = "Error semantico: la variable es incorrecta \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, exp.linea, exp.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_insert(exp, ts, ambito):
    global mensaje
    simbolo = TABS.Simbolo(exp.id, "", "", "", "", 0, 0)
    comprobar = ts.comprobar(simbolo)
    if(comprobar):
        expresion = resolver_general(exp.exp, ts, ambito)
        posicion = resolver_general(exp.pos, ts, ambito)
        lista = ts.obtener(exp.id).valor
        lista.insert(posicion, expresion)
    else:
        mensajeE = "Error semantico: la variable es incorrecta \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, exp.linea, exp.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_remove(exp, ts, ambito):
    global mensaje
    simbolo = TABS.Simbolo(exp.id, "", "", "", "", 0, 0)
    comprobar = ts.comprobar(simbolo)
    if(comprobar):
        posicion = resolver_general(exp.pos, ts, ambito)
        lista = ts.obtener(exp.id).valor
        del lista[posicion]
    else:
        mensajeE = "Error semantico: la variable es incorrecta \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, exp.linea, exp.columna, datetime.now())
        TABE.agregarError(e)

def instruccion_contains(exp, ts, ambito):
    global mensaje
    valores = resolver_general(exp.id, ts, ambito)
    if(valores == None):
        mensajeE = "Error semantico: la variable no contine ningun valor o no existe \n"
        mensaje += mensajeE
        e = TABE.Error(mensajeE, ambito, 1, 1, datetime.now())
        TABE.agregarError(e)
    else:
        expresion = resolver_general(exp.exp, ts, ambito)
        if(expresion in valores):
            return True
        else:
            return False  

def procesar_instrucciones(instrucciones, ts, ambito):
    global mensaje
    global existeBreak
    existeBreak = False
    global existeContinue
    existeContinue = False
    global existeReturn
    existeReturn = False
    global valorReturn
    valorReturn = ""
    for instruccion in instrucciones:
        if(isinstance(instruccion, Println)):
            instruccion_println(instruccion, ts, ambito)
        elif(isinstance(instruccion,Print)):
            instruccion_print(instruccion, ts, ambito)
        elif(isinstance(instruccion,PrintlnEsp)):
            instruccion_println_esp(instruccion, ts, ambito)
        elif(isinstance(instruccion,PrintEsp)):
            instruccion_print_esp(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionMutable)):
            instruccion_asignacion_mutable(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionMutableTipo)):
            instruccion_asignacion_mutable_tipo(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionNoMutable)):
            instruccion_asignacion_no_mutable(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionNoMutableTipo)):
            instruccion_asignacion_no_mutable_tipo(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionNuevoValor)):
            instruccion_asignacion_nuevo_valor(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionArregloMutable)):
            instruccion_asignacion_arreglo_mutable(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionArregloMutableTipo)):
            instruccion_asignacion_arreglo_mutable_tipo(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionArregloNoMutable)):
            instruccion_asignacion_arreglo_no_mutable(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionArregloNoMutableTipo)):
            instruccion_asignacion_arreglo_no_mutable_tipo(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionNuevoArreglo)):
            instruccion_asignacion_nuevo_arreglo(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionVectorMutable)):
            instruccion_asignacion_vector_mutable(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionVectorMutableTipo)):
            instruccion_asignacion_vector_mutable_tipo(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionVectorNoMutable)):
            instruccion_asignacion_vector_no_mutable(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionVectorNoMutableTipo)):
            instruccion_asignacion_vector_no_mutable_tipo(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionVectorVacioMutable)):
            instruccion_asignacion_vector_vacio_mutable(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionVectorVacioNoMutable)):
            instruccion_asignacion_vector_vacio_no_mutable(instruccion, ts, ambito)
        elif(isinstance(instruccion, Funcion)):
            instruccion_funcion(instruccion, ts, ambito)
        elif(isinstance(instruccion, FuncionMain)):
            instruccion_funcion_main(instruccion, ts, ambito)
        elif(isinstance(instruccion, FuncionTipo)):
            instruccion_funcion_tipo(instruccion, ts, ambito)
        elif(isinstance(instruccion, LlamadaFuncion)):
            instruccion_llamada_funcion(instruccion, ts, ambito)
        elif(isinstance(instruccion, IF)):
            instruccion_if(instruccion, ts, ambito)
        elif(isinstance(instruccion, IfElseIf)):
            instruccion_elseif(instruccion, ts, ambito)
        elif(isinstance(instruccion, ELSE)):
            instruccion_elseif(instruccion.instrucciones, ts, "If_"+ambito)
        elif(isinstance(instruccion, CicloWhile)):
            instruccion_while(instruccion, ts, ambito)
        elif(isinstance(instruccion, CicloFor)):
            instruccion_for(instruccion, ts, ambito)
        elif(isinstance(instruccion, Push)):
            instruccion_push(instruccion, ts, ambito)
        elif(isinstance(instruccion, Insert)):
            instruccion_insert(instruccion, ts, ambito)
        elif(isinstance(instruccion, Remove)):
            instruccion_remove(instruccion, ts, ambito)
        elif(isinstance(instruccion, ExisteBreak)):
            existeBreak = True
        elif(isinstance(instruccion, ExisteContinue)):
            existeContinue = True
        elif(isinstance(instruccion, InstruccionReturn)):
            valorReturn = resolver_general(instruccion.exp, ts, ambito)
            existeReturn = True
        if(existeBreak):
            break
        if(existeContinue):
            break
        if(existeReturn):
            break
        #else:
        #    print('Error semantico: Instrucción no válida')

def datos(inputs):
    global mensaje
    mensaje = ""
    instrucciones = g.parse(inputs)
    tabs_global = TABS.TablaSimbolos()
    print(instrucciones)
    procesar_instrucciones(instrucciones, tabs_global, "Global")
    TABE.GenerarTablaErrores()
    tabs_global.GenerarTablaSimbolos()
    tabs_global.reiniciar()
    return mensaje