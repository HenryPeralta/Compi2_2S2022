import ply.yacc as yacc
import ply.lex as lex

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