import gramatica as g
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
    #elif(isinstance(exp, ExpresionIdentificador)):
    elif(isinstance(exp, ExpresionNegativa)):
        exp = resolver_general(exp.exp, ts, ambito)
        return exp*-1
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

def procesar_instrucciones(instrucciones, ts, ambito):
    global mensaje
    for instruccion in instrucciones:
        if(isinstance(instruccion, Println)):
            instruccion_println(instruccion, ts, ambito)
        elif(isinstance(instruccion,Print)):
            instruccion_print(instruccion, ts, ambito)
        else:
            print('Error semantico: Instrucción no válida')

def datos(inputs):
    instrucciones = g.parse(inputs)
    print(instrucciones)
    procesar_instrucciones(instrucciones, "HOLA", "Global")
    return mensaje