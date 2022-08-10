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
    'vec' : 'VEC',

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

    'push' : 'PUSH',
    'insert' : 'INSERT',
    'remove' : 'REMOVE',
    'contains' : 'CONTAINS',
    'len' : 'LEN',

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
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f'Error léxico: Caracter {t.value[0]} no reconocido')
    t.lexer.skip(1)

lexer = lex.lex()

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
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
        expresion : NOT expresion
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

def p_impresion(t):
    '''
        impresion : PRINT EXCLAMACION PARENTIZQ expresion PARENTDER PUNTOYCOMA
                  | PRINTLN EXCLAMACION PARENTIZQ expresion PARENTDER PUNTOYCOMA
    '''
    if(t[1] == "print"):
        t[0] = Print(t[4])
    elif(t[1] == "println"):
        t[0] = Println(t[4])

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
    '''
    t[0] = t[1]

def p_sentencia_if(t):
    '''
       sentencia_if : IF expresion LLAVEIZQ instrucciones LLAVEDER
    '''
    t[0] = IF(t[2], t[4])

def p_sentencia_if_elseif(t):
    '''
        sentencia_if : IF expresion LLAVEIZQ instrucciones LLAVEDER elseif  
    '''
    t[0] = IfElseIf(t[2], t[4], t[6])

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
        t[0] = IF(t[3], t[5])
    else:
        t[0] = ELSE(t[3])

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