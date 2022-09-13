from asyncio.windows_events import NULL
import ply.yacc as yacc
import ply.lex as lex
from tab_simbolos import TIPO_DATO

reserved = {
    #tipo de dato
    'i64' : 'I64',
    'f64' : 'F64',
    'bool' : 'BOOL',
    'char' : 'CHAR',
    'String' : 'STRING',
    'str' : 'STR',
    'usize' : 'USIZE',
    'Vec' : 'VEC',

    #struct
    'struct' : 'STRUCT',

    #nativas
    'pow' : 'POW',
    'powf' : 'POWF',

    #Imprimir
    'print' : 'PRINT',
    'println' : 'PRINTLN',

    #variable
    'let' : 'LET',
    'mut' : 'MUT',

    #funciones
    'fn' : 'FN',
    'main' : 'MAIN',

    #funciones nativas
    'abs' : 'ABS',
    'sqrt' : 'SQRT',
    'to_string' : 'TO_STRING',
    'clone' : 'CLONE',

    #funciones nativas para vectores
    'new' : 'NEW',
    'len' : 'LEN',
    'push' : 'PUSH',
    'remove' : 'REMOVE',
    'contains' : 'CONTAINS',
    'insert' : 'INSERT',
    'capacity' : 'CAPACITY',
    'with_capacity' : 'WITH_CAPACITY',

    #sentencias
    'if' : 'IF',
    'else' : 'ELSE',

    #match
    'match' : 'MATCH',

    #loops
    'loop' : 'LOOP',
    'while' : 'WHILE',
    'for' : 'FOR',
    'in' : 'IN',

    #sentencias de transferencia
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',

    #modulos
    'mod' : 'MOD',
    'pub' : 'PUB',

    #booleanos
    'true' : 'TRUE',
    'false' : 'FALSE'
}

tokens=[
    'PUNTO',
    'COMA',
    'PUNTOYCOMA',
    'DOSPUNTOS',
    'PARENTIZQ',
    'PARENTDER',
    'CORCHIZQ',
    'CORCHDER',
    'LLAVEIZQ',
    'LLAVEDER',
    'EXCLAMACION',
    'AMPERSAND',

    #relacionales
    'MAYOR',
    'MENOR',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUALIGUAL',
    'NOIGUAL',

    #aritmeticas
    'MAS',
    'MENOS',
    'POR',
    'DIVISION',
    'IGUAL',
    'MODULO',

    #logicas
    'OR',
    'AND',
    'NOT',

    'ID',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'CARACTER'
] + list(reserved.values())

t_PUNTO = r'\.'
t_COMA = r','
t_PUNTOYCOMA = r';'
t_DOSPUNTOS = r':'
t_PARENTIZQ = r'\('
t_PARENTDER = r'\)'
t_CORCHIZQ = r'\['
t_CORCHDER = r'\]'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_EXCLAMACION = r'!'
t_AMPERSAND = r'&'

#relacionales
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_IGUALIGUAL = r'=='
t_NOIGUAL = r'!='

#aritmetica
t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_DIVISION = r'\/'
t_IGUAL = r'='
t_MODULO = r'\%'

#logicas
t_OR = r'\| \|'
t_AND = r'&&'
t_NOT = r'!'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("El valor no es decimal")
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("El valor no es entero")
        t.value = 0
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_CARACTER(t):
    r'\'(.|\")\''
    t.value = t.value[1:-1]
    return t

def t_COMENTARIO(t):
    r'\//.*\n'
    t.lexer.lineno +=1

#caracteres a ignorar
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    #t.lexer.lineno += t.value.count("\n")
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f'Error léxico: Caracter {t.value[0]} no reconocido')
    t.lexer.skip(1)

lexer = lex.lex()

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'EXCLAMACION'),
    ('left', 'IGUALIGUAL', 'NOIGUAL', 'MENOR', 'MAYOR', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVISION', 'MODULO'),
    ('right', 'UMENOS'),
)

from expresiones import *
from instrucciones import *

def p_init(t):
    '''
        init : instrucciones
    '''
    t[0] = t[1]

def p_instrucciones_lista(t):
    '''
        instrucciones : instrucciones instruccion
    '''
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t):
    'instrucciones : instruccion'
    t[0] = [t[1]]

def p_instruccion(t):
    '''
        instruccion : impresion
                    | declaracion
                    | asignacion
                    | sentencia_if
                    | ciclo_while
                    | ciclo_for
                    | declarar_arreglo
                    | asignacion_arreglo
                    | declarar_vector
                    | declarar_struct
                    | asignar_struct
                    | nativa_push
                    | nativa_insert
                    | nativa_remove
                    | sen_transferencia
                    | main
                    | funcion
                    | llamada_funcion
                    | struct
                    | return
    '''
    t[0] = t[1]

def p_logica(t):
    '''
        expresion : expresion MAYOR expresion
                  | expresion MENOR expresion
                  | expresion MAYORIGUAL expresion
                  | expresion MENORIGUAL expresion
                  | expresion IGUALIGUAL expresion
                  | expresion NOIGUAL expresion
    '''
    if(t[2] == '>'):
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYORQUE)
    elif(t[2] == '<'):
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENORQUE)
    elif(t[2] == '=='):
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUALIGUAL)
    elif(t[2] == '!='):
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.NOIGUAL)
    elif(t[2] == '>='):
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYORIGUAL)
    elif(t[2] == '<='):
        t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENORIGUAL)

def p_relacionales(t):
    '''
        expresion : expresion OR expresion
                  | expresion AND expresion
    '''
    if(t[2] == '&&'):
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.AND)
    elif(t[2] == '||'):
        t[0] = ExpresionRelacional(t[1], t[3], OPERACION_RELACIONAL.OR)

def p_relacionales_not(t):
    '''
        expresion : EXCLAMACION expresion
    '''
    t[0] = ExpresionRelacional("", t[2], OPERACION_RELACIONAL.NOT)

def p_expresion_binaria(t):
    '''
        expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVISION expresion
                  | expresion MODULO expresion
    '''
    if(t[2] == '+'):
        t[0] = ExpresionBinaria(t[1], t[3], OPERACIONES_ARITMETICAS.MAS)
    elif(t[2] == '-'):
        t[0] = ExpresionBinaria(t[1], t[3], OPERACIONES_ARITMETICAS.MENOS)
    elif(t[2] == '*'):
        t[0] = ExpresionBinaria(t[1], t[3], OPERACIONES_ARITMETICAS.MULTIPLICACION)
    elif(t[2] == '/'):
        t[0] = ExpresionBinaria(t[1], t[3], OPERACIONES_ARITMETICAS.DIVISION)
    elif(t[2] == '%'):
        t[0] = ExpresionBinaria(t[1], t[3], OPERACIONES_ARITMETICAS.MODULO)

def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = ExpresionNegativa(t[2])

def p_expresion_parentesis(t):
    '''
        expresion : PARENTIZQ expresion PARENTDER
    '''
    t[0] = t[2]

def p_fn_nativas_vectores(t):
    '''
        expresion : expresion PUNTO LEN PARENTIZQ PARENTDER
                  | expresion PUNTO CONTAINS PARENTIZQ AMPERSAND expresion PARENTDER
                  | expresion PUNTO ABS PARENTIZQ PARENTDER
                  | expresion PUNTO SQRT PARENTIZQ PARENTDER
                  | expresion PUNTO TO_STRING PARENTIZQ PARENTDER
                  | expresion CORCHIZQ expresion CORCHDER
                  | expresion PUNTO REMOVE PARENTIZQ expresion PARENTDER 
    '''
    if(t[3] == "len"):
        t[0] = ExpresionFnLen(t[1], FUNCIONES_NATIVAS_VECTORES.LEN)
    elif(t[3] == "abs"):
        t[0] = ExpresionAbs(t[1], FUNCIONES_NATIVAS.ABS)
    elif(t[3] == "sqrt"):
        t[0] = ExpresionSqrt(t[1], FUNCIONES_NATIVAS.SQRT)
    elif(t[3] == "to_string"):
        t[0] = ExpresionToString(t[1], FUNCIONES_NATIVAS.TO_STRING)
    elif(t[2] == "["):
        t[0] = ExpresionArreglo(t[1], t[3])
    elif(t[3] == "remove"):
        t[0] = RegresoRemove(t[1], t[5])
    else:
        t[0] = Contains(t[1], t[6])

def p_impresion(t):
    '''
        impresion : PRINT EXCLAMACION PARENTIZQ expresion PARENTDER PUNTOYCOMA
                  | PRINTLN EXCLAMACION PARENTIZQ expresion PARENTDER PUNTOYCOMA
    '''
    if(t[1] == "print"):
        t[0] = Print(t[4])
    elif(t[1] == "println"):
        t[0] = Println(t[4])

def p_impresion_especial(t):
    '''
        impresion : PRINT EXCLAMACION PARENTIZQ listaimpresion PARENTDER PUNTOYCOMA
                  | PRINTLN EXCLAMACION PARENTIZQ listaimpresion PARENTDER PUNTOYCOMA
    '''
    if(t[1] == "print"):
        t[0] = PrintEsp(t.slice[1].lineno, 1, t[4])
    elif(t[1] == "println"):
        t[0] = PrintlnEsp(t.slice[1].lineno, 1, t[4])

def p_lista_impresion(t):
    '''
        listaimpresion : listaimpresion COMA implimir
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_a_impresion(t):
    '''
        listaimpresion : implimir
    '''
    t[0] = [t[1]]

def p_implimir_exp(t):
    '''
        implimir : expresion 
    '''
    t[0] = t[1]

def p_declaracion_mutable(t):
    '''
        declaracion : LET MUT ID IGUAL expresion PUNTOYCOMA
    '''
    t[0] = AsignacionMutable(t[3], t[5], t.slice[1].lineno, 1)

def p_declaracion_mutable_tipo(t):
    '''
        declaracion : LET MUT ID DOSPUNTOS tipo IGUAL expresion PUNTOYCOMA 
    '''
    if(t[5] == "i64"):
        t[0] = AsignacionMutableTipo(t[3], t[7], TIPO_DATO.I64, t.slice[1].lineno, 1)
    elif(t[5] == "f64"):
        t[0] = AsignacionMutableTipo(t[3], t[7], TIPO_DATO.F64, t.slice[1].lineno, 1)
    elif(t[5] == "bool"):
        t[0] = AsignacionMutableTipo(t[3], t[7], TIPO_DATO.BOOL, t.slice[1].lineno, 1)
    elif(t[5] == "char"):
        t[0] = AsignacionMutableTipo(t[3], t[7], TIPO_DATO.CHAR, t.slice[1].lineno, 1)
    elif(t[5] == "String"):
        t[0] = AsignacionMutableTipo(t[3], t[7], TIPO_DATO.STRING, t.slice[1].lineno, 1)
    elif(t[5] == "str"):
        t[0] = AsignacionMutableTipo(t[3], t[7], TIPO_DATO.STR, t.slice[1].lineno, 1)
    elif(t[5] == "usize"):
        t[0] = AsignacionMutableTipo(t[3], t[7], TIPO_DATO.USIZE, t.slice[1].lineno, 1)

def p_declaracion_no_mutable(t):
    '''
        declaracion : LET ID IGUAL expresion PUNTOYCOMA
    '''
    t[0] = AsignacionNoMutable(t[2], t[4], t.slice[1].lineno, 1)

def p_declaracion_no_mutable_tipo(t):
    '''
        declaracion : LET ID DOSPUNTOS tipo IGUAL expresion PUNTOYCOMA
    '''
    if(t[4] == "i64"):
        t[0] = AsignacionNoMutableTipo(t[2], t[6], TIPO_DATO.I64, t.slice[1].lineno, 1)
    elif(t[4] == "f64"):
        t[0] = AsignacionNoMutableTipo(t[2], t[6], TIPO_DATO.F64, t.slice[1].lineno, 1)
    elif(t[4] == "bool"):
        t[0] = AsignacionNoMutableTipo(t[2], t[6], TIPO_DATO.BOOL, t.slice[1].lineno, 1)
    elif(t[4] == "char"):
        t[0] = AsignacionNoMutableTipo(t[2], t[6], TIPO_DATO.CHAR, t.slice[1].lineno, 1)
    elif(t[4] == "String"):
        t[0] = AsignacionNoMutableTipo(t[2], t[6], TIPO_DATO.STRING, t.slice[1].lineno, 1)
    elif(t[4] == "str"):
        t[0] = AsignacionNoMutableTipo(t[2], t[6], TIPO_DATO.STR, t.slice[1].lineno, 1)
    elif(t[4] == "usize"):
        t[0] = AsignacionNoMutableTipo(t[2], t[6], TIPO_DATO.USIZE, t.slice[1].lineno, 1)

def p_asignacion_nuevo_valor(t):
    '''
        asignacion : ID IGUAL expresion PUNTOYCOMA
    '''
    t[0] = AsignacionNuevoValor(t[1], t[3], t.slice[1].lineno, 1)

def p_tipo(t):
    '''
        tipo : I64
             | F64
             | BOOL
             | CHAR
             | STRING
             | STR
             | USIZE
             | VEC
             | ID
    '''
    t[0] = t[1]

def p_return(t):
    '''
        return : RETURN expresion PUNTOYCOMA 
    '''
    t[0] = InstruccionReturn(t[2])

def p_main(t):
    '''
        main : FN MAIN PARENTIZQ PARENTDER LLAVEIZQ instrucciones LLAVEDER
    '''
    t[0] = FuncionMain(t[2], t[6], t.slice[1].lineno, 1)

def p_funcion_sin_return(t):
    '''
        funcion : FN ID PARENTIZQ lista_parametros PARENTDER LLAVEIZQ instrucciones LLAVEDER
                | FN ID PARENTIZQ PARENTDER LLAVEIZQ instrucciones LLAVEDER
    '''
    if(t[4] == ")"):
        t[0] = Funcion(t[2], [], t[6], t.slice[1].lineno, 1)
    else:
        t[0] = Funcion(t[2], t[4], t[7], t.slice[1].lineno, 1)

def p_lista_parametros(t):
    '''
        lista_parametros : lista_parametros COMA parametro
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros(t):
    '''
        lista_parametros : parametro
    '''
    t[0] = [t[1]]

def p_parametro_tipo(t):
    '''
        parametro : ID DOSPUNTOS tipo
                  | ID DOSPUNTOS AMPERSAND MUT CORCHIZQ tipo CORCHDER
                  | ID DOSPUNTOS AMPERSAND MUT CORCHIZQ tipo PUNTOYCOMA expresion CORCHDER
                  | ID DOSPUNTOS AMPERSAND MUT CORCHIZQ CORCHIZQ tipo PUNTOYCOMA expresion CORCHDER PUNTOYCOMA expresion CORCHDER
                  | ID DOSPUNTOS AMPERSAND MUT CORCHIZQ CORCHIZQ CORCHIZQ tipo PUNTOYCOMA expresion CORCHDER PUNTOYCOMA expresion CORCHDER PUNTOYCOMA expresion CORCHDER
                  | ID DOSPUNTOS AMPERSAND MUT VEC MENOR tipo MAYOR
    '''
    if(t[3] == "&"):
        if(t[5] == "["):
            if(t[6] == "["):
                if(t[7] == "["):
                    t[0] = ExpresionParametro(t[1], t[8])
                else:
                    t[0] = ExpresionParametro(t[1], t[7])
            else:
                t[0] = ExpresionParametro(t[1], t[6])
        else:
            t[0] = ExpresionParametro(t[1], t[7])
    else:    
        t[0] = ExpresionParametro(t[1], t[3])

def p_llamada_funcion(t):
    '''
        llamada_funcion : ID PARENTIZQ PARENTDER PUNTOYCOMA
                        | ID PARENTIZQ llamada_parametros_fun PARENTDER PUNTOYCOMA
    '''
    if(t[3] == ")"):
        t[0] = LlamadaFuncion(t[1], [], t.slice[1].lineno, 1)
    else:
        t[0] = LlamadaFuncion(t[1], t[3], t.slice[1].lineno, 1)

def p_lista_llamada_parametros_fun(t):
    '''
        llamada_parametros_fun : llamada_parametros_fun COMA valor_parametro_fun
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_llamada_parametros_fun(t):
    '''
        llamada_parametros_fun : valor_parametro_fun
    '''
    t[0] = [t[1]]

def p_valor_parametro_fun(t):
    '''
        valor_parametro_fun : expresion
                            | AMPERSAND MUT expresion
    '''
    if(t[1] == "&"):
        t[0] = t[3]
    else:
        t[0] = t[1]

def p_llamada_funcion2(t):
    '''
        expresion : ID PARENTIZQ PARENTDER 
                  | ID PARENTIZQ llamada_parametros_fun PARENTDER
    '''
    if(t[3] == ")"):
        t[0] = LlamadaFuncion(t[1], [], t.slice[1].lineno, 1)
    else:
        t[0] = LlamadaFuncion(t[1], t[3], t.slice[1].lineno, 1)

def p_funcion_con_return(t):
    '''
        funcion : FN ID PARENTIZQ lista_parametros PARENTDER MENOS MAYOR tipo LLAVEIZQ instrucciones LLAVEDER
                | FN ID PARENTIZQ PARENTDER MENOS MAYOR tipo LLAVEIZQ instrucciones LLAVEDER
    '''
    if(t[4] == ")"):
        if(t[7] == "i64"):
            t[0] = FuncionTipo(t[2], [], TIPO_DATO.I64, t[9], t.slice[1].lineno, 1)
        elif(t[7] == "f64"):
            t[0] = FuncionTipo(t[2], [], TIPO_DATO.F64, t[9], t.slice[1].lineno, 1)
        elif(t[7] == "bool"):
            t[0] = FuncionTipo(t[2], [], TIPO_DATO.BOOL, t[9], t.slice[1].lineno, 1)
        elif(t[7] == "char"):
            t[0] = FuncionTipo(t[2], [], TIPO_DATO.CHAR, t[9], t.slice[1].lineno, 1)
        elif(t[7] == "String"):
            t[0] = FuncionTipo(t[2], [], TIPO_DATO.STRING, t[9], t.slice[1].lineno, 1)
        elif(t[7] == "str"):
            t[0] = FuncionTipo(t[2], [], TIPO_DATO.STR, t[9], t.slice[1].lineno, 1)
        elif(t[7] == "usize"):
            t[0] = FuncionTipo(t[2], [], TIPO_DATO.USIZE, t[9], t.slice[1].lineno, 1)
    else:
        if(t[8] == "i64"):
            t[0] = FuncionTipo(t[2], t[4], TIPO_DATO.I64, t[10], t.slice[1].lineno, 1)
        elif(t[8] == "f64"):
            t[0] = FuncionTipo(t[2], t[4], TIPO_DATO.F64, t[10], t.slice[1].lineno, 1)
        elif(t[8] == "bool"):
            t[0] = FuncionTipo(t[2], t[4], TIPO_DATO.BOOL, t[10], t.slice[1].lineno, 1)
        elif(t[8] == "char"):
            t[0] = FuncionTipo(t[2], t[4], TIPO_DATO.CHAR, t[10], t.slice[1].lineno, 1)
        elif(t[8] == "String"):
            t[0] = FuncionTipo(t[2], t[4], TIPO_DATO.STRING, t[10], t.slice[1].lineno, 1)
        elif(t[8] == "str"):
            t[0] = FuncionTipo(t[2], t[4], TIPO_DATO.STR, t[10], t.slice[1].lineno, 1)
        elif(t[8] == "usize"):
            t[0] = FuncionTipo(t[2], t[4], TIPO_DATO.USIZE, t[10], t.slice[1].lineno, 1)

def p_sentencia_if(t):
    '''
       sentencia_if : IF expresion LLAVEIZQ instrucciones LLAVEDER
    '''
    t[0] = IF(t[2], t.slice[1].lineno, 1, t[4])

def p_sentencia_if_elseif(t):
    '''
        sentencia_if : IF expresion LLAVEIZQ instrucciones LLAVEDER elseif  
    '''
    t[0] = IfElseIf(t[2], t.slice[1].lineno, 1, t[4], t[6])

def p_lista_else_if(t):
    '''
        elseif : elseif lista_elseif
    '''
    t[1].append(t[2])
    t[0] = t[1]

def p_lista_esle_if2(t):
    '''
        elseif : lista_elseif
    '''
    t[0] = [t[1]]

def p_else_elseif(t):
    '''
        lista_elseif : ELSE IF expresion LLAVEIZQ instrucciones LLAVEDER
                     | ELSE LLAVEIZQ instrucciones LLAVEDER
    '''
    if(t[2] == "if"):
        t[0] = IF(t[3], t.slice[1].lineno, 1, t[5])
    else:
        t[0] = ELSE(t[3])

def p_ciclo_while(t):
    '''
        ciclo_while : WHILE expresion LLAVEIZQ instrucciones LLAVEDER
    '''
    t[0] = CicloWhile(t[2], t.slice[1].lineno, 1, t[4])

def p_ciclo_for(t):
    '''
        ciclo_for : FOR ID IN expresion PUNTO PUNTO expresion LLAVEIZQ instrucciones LLAVEDER
                  | FOR ID IN CORCHIZQ llamada_parametros CORCHDER LLAVEIZQ instrucciones LLAVEDER
                  | FOR ID IN expresion LLAVEIZQ instrucciones LLAVEDER
    '''
    if(t[4] == "["):
        t[0] = CicloFor(t[2], t[5], "", t[8], t.slice[1].lineno, 1)
    else:
        if(t[5] == "."):
            t[0] = CicloFor(t[2], t[4], t[7], t[9], t.slice[1].lineno, 1)
        else:
            t[0] = CicloFor(t[2], t[4], "", t[6], t.slice[1].lineno, 1)

def p_sen_transferencia(t):
    '''
        sen_transferencia : BREAK PUNTOYCOMA
                          | CONTINUE PUNTOYCOMA
    '''
    if(t[1] == "break"):
        t[0] = ExisteBreak()
    elif(t[1] == "continue"):
        t[0] = ExisteContinue()

def p_declaracion_vector_mutable(t):
    '''
        declarar_vector : LET MUT ID IGUAL VEC EXCLAMACION CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA
    '''
    t[0] = AsignacionVectorMutable(t[3], t[8], t.slice[1].lineno, 1)

def p_declaracion_vector_mutable_tipo(t):
    '''
        declarar_vector : LET MUT ID DOSPUNTOS VEC MENOR tipo MAYOR IGUAL VEC EXCLAMACION CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA
    '''
    if(t[7] == "i64"):
        t[0] = AsignacionVectorMutableTipo(t[3], t[13], TIPO_DATO.I64, t.slice[1].lineno, 1)
    elif(t[7] == "f64"):
        t[0] = AsignacionVectorMutableTipo(t[3], t[13], TIPO_DATO.F64, t.slice[1].lineno, 1)
    elif(t[7] == "bool"):
        t[0] = AsignacionVectorMutableTipo(t[3], t[13], TIPO_DATO.BOOL, t.slice[1].lineno, 1)
    elif(t[7] == "char"):
        t[0] = AsignacionVectorMutableTipo(t[3], t[13], TIPO_DATO.CHAR, t.slice[1].lineno, 1)
    elif(t[7] == "String"):
        t[0] = AsignacionVectorMutableTipo(t[3], t[13], TIPO_DATO.STRING, t.slice[1].lineno, 1)
    elif(t[7] == "str"):
        t[0] = AsignacionVectorMutableTipo(t[3], t[13], TIPO_DATO.STR, t.slice[1].lineno, 1)
    elif(t[7] == "usize"):
        t[0] = AsignacionVectorMutableTipo(t[3], t[13], TIPO_DATO.USIZE, t.slice[1].lineno, 1)
    else:
        t[0] = AsignacionVectorMutableTipo(t[3], t[13], TIPO_DATO.ID, t.slice[1].lineno, 1)

def p_declaracion_vector_no_mutable(t):
    '''
        declarar_vector : LET ID IGUAL VEC EXCLAMACION CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA
    '''
    t[0] = AsignacionVectorNoMutable(t[2], t[7], t.slice[1].lineno, 1)

def p_declaracion_vector_no_mutable_tipo(t):
    '''
        declarar_vector : LET ID DOSPUNTOS VEC MENOR tipo MAYOR IGUAL VEC EXCLAMACION CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA
    '''
    if(t[6] == "i64"):
        t[0] = AsignacionVectorNoMutableTipo(t[2], t[12], TIPO_DATO.I64, t.slice[1].lineno, 1)
    elif(t[6] == "f64"):
        t[0] = AsignacionVectorNoMutableTipo(t[2], t[12], TIPO_DATO.F64, t.slice[1].lineno, 1)
    elif(t[6] == "bool"):
        t[0] = AsignacionVectorNoMutableTipo(t[2], t[12], TIPO_DATO.BOOL, t.slice[1].lineno, 1)
    elif(t[6] == "char"):
        t[0] = AsignacionVectorNoMutableTipo(t[2], t[12], TIPO_DATO.CHAR, t.slice[1].lineno, 1)
    elif(t[6] == "String"):
        t[0] = AsignacionVectorNoMutableTipo(t[2], t[12], TIPO_DATO.STRING, t.slice[1].lineno, 1)
    elif(t[6] == "str"):
        t[0] = AsignacionVectorNoMutableTipo(t[2], t[12], TIPO_DATO.STR, t.slice[1].lineno, 1)
    elif(t[6] == "usize"):
        t[0] = AsignacionVectorNoMutableTipo(t[2], t[12], TIPO_DATO.USIZE, t.slice[1].lineno, 1)
    else:
        t[0] = AsignacionVectorNoMutableTipo(t[2], t[12], TIPO_DATO.ID, t.slice[1].lineno, 1)

def p_declaracion_vector_vacio_mutable(t):
    '''
        declarar_vector : LET MUT ID DOSPUNTOS VEC MENOR tipo MAYOR IGUAL VEC DOSPUNTOS DOSPUNTOS NEW PARENTIZQ PARENTDER PUNTOYCOMA
    '''
    if(t[7] == "i64"):
        t[0] = AsignacionVectorVacioMutable(t[3], TIPO_DATO.I64, t.slice[1].lineno, 1)
    elif(t[7] == "f64"):
        t[0] = AsignacionVectorVacioMutable(t[3], TIPO_DATO.F64, t.slice[1].lineno, 1)
    elif(t[7] == "bool"):
        t[0] = AsignacionVectorVacioMutable(t[3], TIPO_DATO.BOOL, t.slice[1].lineno, 1)
    elif(t[7] == "char"):
        t[0] = AsignacionVectorVacioMutable(t[3], TIPO_DATO.CHAR, t.slice[1].lineno, 1)
    elif(t[7] == "String"):
        t[0] = AsignacionVectorVacioMutable(t[3], TIPO_DATO.STRING, t.slice[1].lineno, 1)
    elif(t[7] == "str"):
        t[0] = AsignacionVectorVacioMutable(t[3], TIPO_DATO.STR, t.slice[1].lineno, 1)
    elif(t[7] == "usize"):
        t[0] = AsignacionVectorVacioMutable(t[3], TIPO_DATO.USIZE, t.slice[1].lineno, 1)

def p_declaracion_vector_vacio_no_mutable(t):
    '''
        declarar_vector : LET ID DOSPUNTOS VEC MENOR tipo MAYOR IGUAL VEC DOSPUNTOS DOSPUNTOS NEW PARENTIZQ PARENTDER PUNTOYCOMA
    '''
    if(t[6] == "i64"):
        t[0] = AsignacionVectorVacioNoMutable(t[2], TIPO_DATO.I64, t.slice[1].lineno, 1)
    elif(t[6] == "f64"):
        t[0] = AsignacionVectorVacioNoMutable(t[2], TIPO_DATO.F64, t.slice[1].lineno, 1)
    elif(t[6] == "bool"):
        t[0] = AsignacionVectorVacioNoMutable(t[2], TIPO_DATO.BOOL, t.slice[1].lineno, 1)
    elif(t[6] == "char"):
        t[0] = AsignacionVectorVacioNoMutable(t[2], TIPO_DATO.CHAR, t.slice[1].lineno, 1)
    elif(t[6] == "String"):
        t[0] = AsignacionVectorVacioNoMutable(t[2], TIPO_DATO.STRING, t.slice[1].lineno, 1)
    elif(t[6] == "str"):
        t[0] = AsignacionVectorVacioNoMutable(t[2], TIPO_DATO.STR, t.slice[1].lineno, 1)
    elif(t[6] == "usize"):
        t[0] = AsignacionVectorVacioNoMutable(t[2], TIPO_DATO.USIZE, t.slice[1].lineno, 1)

def p_struct(t):
    '''
        struct : STRUCT ID LLAVEIZQ lista_structs LLAVEDER
    '''
    t[0] = InstruccionStruct(t[2], t[4], t.slice[1].lineno, 1)

def p_lista_structs(t):
    '''
        lista_structs : lista_structs COMA lista_struct
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_struct(t):
    '''
        lista_structs : lista_struct
    '''
    t[0] = [t[1]]

def p_valores_struct(t):
    '''
        lista_struct : ID DOSPUNTOS tipo
    '''
    t[0] = t[1]

def p_fnativa_push(t):
    '''
        nativa_push : ID PUNTO PUSH PARENTIZQ expresion PARENTDER PUNTOYCOMA
    '''
    t[0] = Push(t[1], t[5], t.slice[1].lineno, 1)

def p_fnativa_insert(t):
    '''
        nativa_insert : ID PUNTO INSERT PARENTIZQ expresion COMA expresion PARENTDER PUNTOYCOMA
    '''
    t[0] = Insert(t[1], t[5], t[7], t.slice[1].lineno, 1)

def p_fnativa_remove(t):
    '''
        nativa_remove : ID PUNTO REMOVE PARENTIZQ expresion PARENTDER PUNTOYCOMA
    '''
    t[0] = Remove(t[1], t[5], t.slice[1].lineno, 1)

def p_declaracion_arreglo_mutable(t):
    '''
        declarar_arreglo : LET MUT ID IGUAL CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA
    '''
    t[0] = AsignacionArregloMutable(t[3], t[6], t.slice[1].lineno, 1)

def p_declaracion_arreglo_mutable_tipo(t):
    '''
        declarar_arreglo : LET MUT ID DOSPUNTOS CORCHIZQ tipo PUNTOYCOMA expresion CORCHDER IGUAL CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA
    '''
    if(t[6] == "i64"):
        t[0] = AsignacionArregloMutableTipo(t[3], t[12], TIPO_DATO.I64, t[8], t.slice[1].lineno, 1)
    elif(t[6] == "f64"):
        t[0] = AsignacionArregloMutableTipo(t[3], t[12], TIPO_DATO.F64, t[8], t.slice[1].lineno, 1)
    elif(t[6] == "bool"):
        t[0] = AsignacionArregloMutableTipo(t[3], t[12], TIPO_DATO.BOOL, t[8], t.slice[1].lineno, 1)
    elif(t[6] == "char"):
        t[0] = AsignacionArregloMutableTipo(t[3], t[12], TIPO_DATO.CHAR, t[8], t.slice[1].lineno, 1)
    elif(t[6] == "String"):
        t[0] = AsignacionArregloMutableTipo(t[3], t[12], TIPO_DATO.STRING, t[8], t.slice[1].lineno, 1)
    elif(t[6] == "str"):
        t[0] = AsignacionArregloMutableTipo(t[3], t[12], TIPO_DATO.STR, t[8], t.slice[1].lineno, 1)
    elif(t[6] == "usize"):
        t[0] = AsignacionArregloMutableTipo(t[3], t[12], TIPO_DATO.USIZE, t[8], t.slice[1].lineno, 1)
    else:
        t[0] = AsignacionArregloMutableTipo(t[3], t[12], TIPO_DATO.ID, t[8], t.slice[1].lineno, 1)

def p_declaracion_arreglo_no_mutable(t):
    '''
        declarar_arreglo : LET ID IGUAL CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA
    '''
    t[0] = AsignacionArregloNoMutable(t[2], t[5], t.slice[1].lineno, 1)

def p_declaracion_arreglo_no_mutable_tipo(t):
    '''
        declarar_arreglo : LET ID DOSPUNTOS CORCHIZQ tipo PUNTOYCOMA expresion CORCHDER IGUAL CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA
    '''
    if(t[5] == "i64"):
        t[0] = AsignacionArregloNoMutableTipo(t[2], t[11], TIPO_DATO.I64, t[7], t.slice[1].lineno, 1)
    elif(t[5] == "f64"):
        t[0] = AsignacionArregloNoMutableTipo(t[2], t[11], TIPO_DATO.F64, t[7], t.slice[1].lineno, 1)
    elif(t[5] == "bool"):
        t[0] = AsignacionArregloNoMutableTipo(t[2], t[11], TIPO_DATO.BOOL, t[7], t.slice[1].lineno, 1)
    elif(t[5] == "char"):
        t[0] = AsignacionArregloNoMutableTipo(t[2], t[11], TIPO_DATO.CHAR, t[7], t.slice[1].lineno, 1)
    elif(t[5] == "String"):
        t[0] = AsignacionArregloNoMutableTipo(t[2], t[11], TIPO_DATO.STRING, t[7], t.slice[1].lineno, 1)
    elif(t[5] == "str"):
        t[0] = AsignacionArregloNoMutableTipo(t[2], t[11], TIPO_DATO.STR, t[7], t.slice[1].lineno, 1)
    elif(t[5] == "usize"):
        t[0] = AsignacionArregloNoMutableTipo(t[2], t[11], TIPO_DATO.USIZE, t[7], t.slice[1].lineno, 1)
    else:
        t[0] = AsignacionArregloNoMutableTipo(t[2], t[11], TIPO_DATO.ID, t[7], t.slice[1].lineno, 1)

def p_lista_llamada_parametros(t):
    '''
        llamada_parametros : llamada_parametros COMA valor_parametro
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_llamada_parametros(t):
    '''
        llamada_parametros : valor_parametro
    '''
    t[0] = [t[1]]

def p_valor_parametro(t):
    '''
        valor_parametro : expresion
    '''
    t[0] = t[1]

def p_asignacion_arreglo_1x1_mutable(t):
    '''
        asignacion_arreglo : ID CORCHIZQ expresion CORCHDER IGUAL expresion PUNTOYCOMA
    '''
    t[0] = AsignacionNuevoArreglo(t[1], t[3], t[6], t.slice[1].lineno, 1)

def p_asignacion_arreglo_2x2_mutable(t):
    '''
        asignacion_arreglo : ID CORCHIZQ expresion CORCHDER CORCHIZQ expresion CORCHDER IGUAL expresion PUNTOYCOMA
    '''
    t[0] = AsignacionNuevoArregloDimensional(t[1], t[3], t[6], t[9], t.slice[1].lineno, 1)

def p_declaracion_arreglo_mutable_2x2(t):
    '''
        declarar_arreglo : LET MUT ID IGUAL CORCHIZQ lista_arrgeglo_mas_dim CORCHDER PUNTOYCOMA
    '''
    t[0] = AsignacionArregloMutableDimensional(t[3], t[6], t.slice[1].lineno, 1)

def p_declaracion_arreglo_mutable_tipo_2x2(t):
    '''
        declarar_arreglo : LET MUT ID DOSPUNTOS CORCHIZQ CORCHIZQ tipo PUNTOYCOMA expresion CORCHDER PUNTOYCOMA expresion CORCHDER IGUAL CORCHIZQ lista_arrgeglo_mas_dim CORCHDER PUNTOYCOMA
    '''
    if(t[7] == "i64"):
        t[0] = AsignacionArregloMutableTipoDimensional(t[3], t[16], TIPO_DATO.I64, t[12], t[9], t.slice[1].lineno, 1)
    elif(t[7] == "f64"):
        t[0] = AsignacionArregloMutableTipoDimensional(t[3], t[16], TIPO_DATO.F64, t[12], t[9], t.slice[1].lineno, 1)
    elif(t[7] == "bool"):
        t[0] = AsignacionArregloMutableTipoDimensional(t[3], t[16], TIPO_DATO.BOOL, t[12], t[9], t.slice[1].lineno, 1)
    elif(t[7] == "char"):
        t[0] = AsignacionArregloMutableTipoDimensional(t[3], t[16], TIPO_DATO.CHAR, t[12], t[9], t.slice[1].lineno, 1)
    elif(t[7] == "String"):
        t[0] = AsignacionArregloMutableTipoDimensional(t[3], t[16], TIPO_DATO.STRING, t[12], t[9], t.slice[1].lineno, 1)
    elif(t[7] == "str"):
        t[0] = AsignacionArregloMutableTipoDimensional(t[3], t[16], TIPO_DATO.STR, t[12], t[9], t.slice[1].lineno, 1)
    elif(t[7] == "usize"):
        t[0] = AsignacionArregloMutableTipoDimensional(t[3], t[16], TIPO_DATO.USIZE, t[12], t[9], t.slice[1].lineno, 1)
    else:
        t[0] = AsignacionArregloMutableTipoDimensional(t[3], t[16], TIPO_DATO.ID, t[12], t[9], t.slice[1].lineno, 1)

def p_declaracion_arreglo_no_mutable_2x2(t):
    '''
        declarar_arreglo : LET ID IGUAL CORCHIZQ lista_arrgeglo_mas_dim CORCHDER PUNTOYCOMA
    '''
    t[0] = AsignacionArregloNoMutableDimensional(t[2], t[5], t.slice[1].lineno, 1)

def p_declaracion_arreglo_no_mutable_tipo_2x2(t):
    '''
        declarar_arreglo : LET ID DOSPUNTOS CORCHIZQ CORCHIZQ tipo PUNTOYCOMA expresion CORCHDER PUNTOYCOMA expresion CORCHDER IGUAL CORCHIZQ lista_arrgeglo_mas_dim CORCHDER PUNTOYCOMA
    '''
    if(t[6] == "i64"):
        t[0] = AsignacionArregloNoMutableTipoDimensional(t[2], t[15], TIPO_DATO.I64, t[11], t[8], t.slice[1].lineno, 1)
    elif(t[6] == "f64"):
        t[0] = AsignacionArregloNoMutableTipoDimensional(t[2], t[15], TIPO_DATO.F64, t[11], t[8], t.slice[1].lineno, 1)
    elif(t[6] == "bool"):
        t[0] = AsignacionArregloNoMutableTipoDimensional(t[2], t[15], TIPO_DATO.BOOL, t[11], t[8], t.slice[1].lineno, 1)
    elif(t[6] == "char"):
        t[0] = AsignacionArregloNoMutableTipoDimensional(t[2], t[15], TIPO_DATO.CHAR, t[11], t[8], t.slice[1].lineno, 1)
    elif(t[6] == "String"):
        t[0] = AsignacionArregloNoMutableTipoDimensional(t[2], t[15], TIPO_DATO.STRING, t[11], t[8], t.slice[1].lineno, 1)
    elif(t[6] == "str"):
        t[0] = AsignacionArregloNoMutableTipoDimensional(t[2], t[15], TIPO_DATO.STR, t[11], t[8], t.slice[1].lineno, 1)
    elif(t[6] == "usize"):
        t[0] = AsignacionArregloNoMutableTipoDimensional(t[2], t[15], TIPO_DATO.USIZE, t[11], t[8], t.slice[1].lineno, 1)
    else:
        t[0] = AsignacionArregloNoMutableTipoDimensional(t[2], t[15], TIPO_DATO.ID, t[11], t[8], t.slice[1].lineno, 1)

def p_lista_arrgeglo_mas_dim(t):
    '''
        lista_arrgeglo_mas_dim : lista_arrgeglo_mas_dim COMA valor_arrgeglo_mas_dim
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_arreglo_mas_dim(t):
    '''
        lista_arrgeglo_mas_dim : valor_arrgeglo_mas_dim
    '''
    t[0] = [t[1]]

def p_valor_arrgeglo_mas_dim(t):
    '''
        valor_arrgeglo_mas_dim : CORCHIZQ llamada_parametros CORCHDER
    '''
    t[0] = t[2]

def p_asignacion_arreglo_3x3_mutable(t):
    '''
        asignacion_arreglo : ID CORCHIZQ expresion CORCHDER CORCHIZQ expresion CORCHDER CORCHIZQ expresion CORCHDER IGUAL expresion PUNTOYCOMA
    '''
    t[0] = AsignacionNuevoArregloDimensional3x3(t[1], t[3], t[6], t[9], t[12], t.slice[1].lineno, 1)

def p_declaracion_arreglo_mutable_3x3(t):
    '''
        declarar_arreglo : LET MUT ID IGUAL CORCHIZQ lista_arrgeglo_dimensional_tres CORCHDER PUNTOYCOMA
    '''
    t[0] = AsignacionArregloMutableDimensional3x3(t[3], t[6], t.slice[1].lineno, 1)

def p_declaracion_arreglo_mutable_tipo_3x3(t):
    '''
        declarar_arreglo : LET MUT ID DOSPUNTOS CORCHIZQ CORCHIZQ CORCHIZQ tipo PUNTOYCOMA expresion CORCHDER PUNTOYCOMA expresion CORCHDER PUNTOYCOMA expresion CORCHDER IGUAL CORCHIZQ lista_arrgeglo_dimensional_tres CORCHDER PUNTOYCOMA
    '''
    if(t[8] == "i64"):
        t[0] = AsignacionArregloMutableTipoDimensional3x3(t[3], t[20], TIPO_DATO.I64, t[16], t[13], t[10], t.slice[1].lineno, 1)
    elif(t[8] == "f64"):
        t[0] = AsignacionArregloMutableTipoDimensional3x3(t[3], t[20], TIPO_DATO.F64, t[16], t[13], t[10], t.slice[1].lineno, 1)
    elif(t[8] == "bool"):
        t[0] = AsignacionArregloMutableTipoDimensional3x3(t[3], t[20], TIPO_DATO.BOOL, t[16], t[13], t[10], t.slice[1].lineno, 1)
    elif(t[8] == "char"):
        t[0] = AsignacionArregloMutableTipoDimensional3x3(t[3], t[20], TIPO_DATO.CHAR, t[16], t[13], t[10], t.slice[1].lineno, 1)
    elif(t[8] == "String"):
        t[0] = AsignacionArregloMutableTipoDimensional3x3(t[3], t[20], TIPO_DATO.STRING, t[16], t[13], t[10], t.slice[1].lineno, 1)
    elif(t[8] == "str"):
        t[0] = AsignacionArregloMutableTipoDimensional3x3(t[3], t[20], TIPO_DATO.STR, t[16], t[13], t[10], t.slice[1].lineno, 1)
    elif(t[8] == "usize"):
        t[0] = AsignacionArregloMutableTipoDimensional3x3(t[3], t[20], TIPO_DATO.USIZE, t[16], t[13], t[10], t.slice[1].lineno, 1)
    else:
        t[0] = AsignacionArregloMutableTipoDimensional3x3(t[3], t[20], TIPO_DATO.ID, t[16], t[13], t[10], t.slice[1].lineno, 1)

def p_declaracion_arreglo_no_mutable_3x3(t):
    '''
        declarar_arreglo : LET ID IGUAL CORCHIZQ lista_arrgeglo_dimensional_tres CORCHDER PUNTOYCOMA
    '''
    t[0] = AsignacionArregloNoMutableDimensional3x3(t[2], t[5], t.slice[1].lineno, 1)

def p_declaracion_arreglo_no_mutable_tipo_3x3(t):
    '''
        declarar_arreglo : LET ID DOSPUNTOS CORCHIZQ CORCHIZQ CORCHIZQ tipo PUNTOYCOMA expresion CORCHDER PUNTOYCOMA expresion CORCHDER PUNTOYCOMA expresion CORCHDER IGUAL CORCHIZQ lista_arrgeglo_dimensional_tres CORCHDER PUNTOYCOMA
    '''
    if(t[7] == "i64"):
        t[0] = AsignacionArregloNoMutableTipoDimensional3x3(t[2], t[19], TIPO_DATO.I64, t[15], t[12], t[9], t.slice[1].lineno, 1)
    elif(t[7] == "f64"):
        t[0] = AsignacionArregloNoMutableTipoDimensional3x3(t[2], t[19], TIPO_DATO.F64, t[15], t[12], t[9], t.slice[1].lineno, 1)
    elif(t[7] == "bool"):
        t[0] = AsignacionArregloNoMutableTipoDimensional3x3(t[2], t[19], TIPO_DATO.BOOL, t[15], t[12], t[9], t.slice[1].lineno, 1)
    elif(t[7] == "char"):
        t[0] = AsignacionArregloNoMutableTipoDimensional3x3(t[2], t[19], TIPO_DATO.CHAR, t[15], t[12], t[9], t.slice[1].lineno, 1)
    elif(t[7] == "String"):
        t[0] = AsignacionArregloNoMutableTipoDimensional3x3(t[2], t[19], TIPO_DATO.STRING, t[15], t[12], t[9], t.slice[1].lineno, 1)
    elif(t[7] == "str"):
        t[0] = AsignacionArregloNoMutableTipoDimensional3x3(t[2], t[19], TIPO_DATO.STR, t[15], t[12], t[9], t.slice[1].lineno, 1)
    elif(t[7] == "usize"):
        t[0] = AsignacionArregloNoMutableTipoDimensional3x3(t[2], t[19], TIPO_DATO.USIZE, t[15], t[12], t[9], t.slice[1].lineno, 1)
    else:
        t[0] = AsignacionArregloNoMutableTipoDimensional3x3(t[2], t[19], TIPO_DATO.ID, t[15], t[12], t[9], t.slice[1].lineno, 1)

def p_lista_arreglo_dimensional_3x3(t):
    '''
        lista_arrgeglo_dimensional_tres : lista_arrgeglo_dimensional_tres COMA valor_arrgeglo_dimensional_tres
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_arreglo_dimensional_3x3(t):
    '''
        lista_arrgeglo_dimensional_tres : valor_arrgeglo_dimensional_tres
    '''
    t[0] = [t[1]]

def p_valor_dimensional_3x3(t):
    '''
        valor_arrgeglo_dimensional_tres : CORCHIZQ lista_arrgeglo_mas_dim CORCHDER
    '''
    t[0] = t[2]

def p_declarar_struct_mutable(t):
    '''
        declarar_struct : LET MUT ID IGUAL ID LLAVEIZQ dec_lista_structs LLAVEDER PUNTOYCOMA 
    '''
    t[0] = AsignacionStruct(t[3], t[5], t[7], t.slice[1].lineno, 1)

def p_dec_lista_structs(t):
    '''
        dec_lista_structs : dec_lista_structs COMA dec_valores_struct
    '''
    t[1].append(t[3])
    t[0] = t[1]

def p_dec_lista_struct(t):
    '''
        dec_lista_structs : dec_valores_struct
    '''
    t[0] = [t[1]]

def p_dec_valores_struct(t):
    '''
        dec_valores_struct : ID DOSPUNTOS expresion
    '''
    t[0] = t[3]

def p_asignacion_valor_struct(t):
    '''
        asignar_struct : ID PUNTO ID IGUAL expresion PUNTOYCOMA 
    '''
    t[0] = AsignacionValorStruct(t[1], t[3], t[5], t.slice[1].lineno, 1)

def p_expresion_acceso_struct(t):
    '''
        expresion : expresion PUNTO expresion
    '''
    #t[1] = ExpresionIdentificador(t[1])
    #t[3] = ExpresionIdentificador(t[3])
    t[0] = ExpresionAccesoStruct([t[1], t[3]])

def p_expresion_numero(t):
    '''
        expresion : ENTERO
                  | DECIMAL
    '''
    t[0] = ExpresionNumero(t[1])

def p_expresion_id(t):
    '''
        expresion : ID
    '''
    t[0] = ExpresionIdentificador(t[1])

def p_expresion_bool(t):
    '''
        expresion : TRUE
                  | FALSE
    '''
    if(t[1] == 'true'):
        t[0] = ExpresionBool(True)
    else: t[0] = ExpresionBool(False)

def p_expresion_cadena(t):
    '''
        expresion : CADENA
    '''
    t[0] = ExpresionDobleComilla(t[1])

def p_expresion_caracter(t):
    '''
        expresion : CARACTER
    '''
    t[0] = ExpresionCaracter(t[1])

def p_error(t):
    print(t)
    print(f'Error sintáctico: {t.value} no esperado')

parser = yacc.yacc()

def parse(input):
    return parser.parse(input)