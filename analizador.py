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
        simbolo = TABS .Simbolo(exp.id, "", "", False, "",0,0)
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
    valor = resolver_general(expif.expLogica, ts, "If_"+ambito)
    if(valor):
        procesar_instrucciones(expif.instrucciones, ts, "If_"+ambito)

def instruccion_elseif(expelseif, ts, ambito):
    valor = resolver_general(expelseif.expLogica, ts, "If_"+ambito)
    if(valor):
        procesar_instrucciones(expelseif.instrucciones, ts, "If_"+ambito)
    else:
        for listaif in expelseif.listaElseif:
            if(isinstance(listaif, IF)):
                valor2 = resolver_general(listaif.expLogica, ts, "If_"+ambito)
                if(valor2):
                    procesar_instrucciones(listaif.instrucciones, ts, "if_"+ambito)
                    break
            elif(isinstance(listaif, ELSE)):
                procesar_instrucciones(listaif.instrucciones, ts, "if_"+ambito)
                break

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
        elif(isinstance(instruccion, AsignacionNoMutable)):
            instruccion_asignacion_no_mutable(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionNoMutableTipo)):
            instruccion_asignacion_no_mutable_tipo(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionNuevoValor)):
            instruccion_asignacion_nuevo_valor(instruccion, ts, ambito)
        elif(isinstance(instruccion, IF)):
            instruccion_if(instruccion, ts, ambito)
        elif(isinstance(instruccion, IfElseIf)):
            instruccion_elseif(instruccion, ts, ambito)
        elif(isinstance(instruccion, ELSE)):
            instruccion_elseif(instruccion.instrucciones, ts, "If_"+ambito)
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