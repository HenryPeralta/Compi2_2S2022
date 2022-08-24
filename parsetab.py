
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightNOTleftIGUALIGUALNOIGUALMENORMAYORMAYORIGUALMENORIGUALleftMASMENOSleftPORDIVISIONMODULOrightUMENOSABS AMPERSAND AND BOOL BREAK CADENA CAPACITY CARACTER CHAR CLONE COMA CONTAINS CONTINUE CORCHDER CORCHIZQ DECIMAL DIVISION DOSPUNTOS ELSE ENTERO EXCLAMACION F64 FALSE FN FOR I64 ID IF IGUAL IGUALIGUAL IN INSERT LEN LET LLAVEDER LLAVEIZQ LOOP MAIN MAS MATCH MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MOD MODULO MUT NEW NOIGUAL NOT OR PARENTDER PARENTIZQ POR POW POWF PRINT PRINTLN PUB PUNTO PUNTOYCOMA PUSH REMOVE RETURN SQRT STR STRING STRUCT TO_STRING TRUE USIZE VEC WHILE WITH_CAPACITY\n        init : instrucciones\n    \n        instrucciones : instrucciones instruccion\n    instrucciones : instruccion\n        instruccion : impresion\n                    | declaracion\n                    | asignacion\n                    | sentencia_if\n                    | ciclo_while\n                    | ciclo_for\n                    | declarar_arreglo\n                    | asignacion_arreglo\n                    | declarar_vector\n                    | sen_transferencia\n                    | funcion\n                    | llamada_funcion\n                    | return\n    \n        expresion : expresion MAYOR expresion\n                  | expresion MENOR expresion\n                  | expresion MAYORIGUAL expresion\n                  | expresion MENORIGUAL expresion\n                  | expresion IGUALIGUAL expresion\n                  | expresion NOIGUAL expresion\n    \n        expresion : expresion OR expresion\n                  | expresion AND expresion\n    \n        expresion : NOT expresion\n    \n        expresion : expresion MAS expresion\n                  | expresion MENOS expresion\n                  | expresion POR expresion\n                  | expresion DIVISION expresion\n                  | expresion MODULO expresion\n    expresion : MENOS expresion %prec UMENOS\n        expresion : PARENTIZQ expresion PARENTDER\n    \n        expresion : expresion PUNTO LEN PARENTIZQ PARENTDER\n    \n        impresion : PRINT EXCLAMACION PARENTIZQ expresion PARENTDER PUNTOYCOMA\n                  | PRINTLN EXCLAMACION PARENTIZQ expresion PARENTDER PUNTOYCOMA\n    \n        declaracion : LET MUT ID IGUAL expresion PUNTOYCOMA\n    \n        declaracion : LET MUT ID DOSPUNTOS tipo IGUAL expresion PUNTOYCOMA \n    \n        declaracion : LET ID IGUAL expresion PUNTOYCOMA\n    \n        declaracion : LET ID DOSPUNTOS tipo IGUAL expresion PUNTOYCOMA\n    \n        asignacion : ID IGUAL expresion PUNTOYCOMA\n    \n        tipo : I64\n             | F64\n             | BOOL\n             | CHAR\n             | STRING\n             | STR\n             | USIZE\n             | VEC\n             | ID\n    \n        return : RETURN expresion PUNTOYCOMA \n    \n        funcion : FN ID PARENTIZQ lista_parametros PARENTDER LLAVEIZQ instrucciones LLAVEDER\n                | FN ID PARENTIZQ PARENTDER LLAVEIZQ instrucciones LLAVEDER\n    \n        lista_parametros : lista_parametros COMA parametro\n    \n        lista_parametros : parametro\n    \n        parametro : ID DOSPUNTOS tipo\n    \n        llamada_funcion : ID PARENTIZQ PARENTDER PUNTOYCOMA\n                        | ID PARENTIZQ llamada_parametros PARENTDER PUNTOYCOMA\n    \n       sentencia_if : IF expresion LLAVEIZQ instrucciones LLAVEDER\n    \n        sentencia_if : IF expresion LLAVEIZQ instrucciones LLAVEDER elseif  \n    \n        elseif : elseif lista_elseif\n    \n        elseif : lista_elseif\n    \n        lista_elseif : ELSE IF expresion LLAVEIZQ instrucciones LLAVEDER\n                     | ELSE LLAVEIZQ instrucciones LLAVEDER\n    \n        ciclo_while : WHILE expresion LLAVEIZQ instrucciones LLAVEDER\n    \n        ciclo_for : FOR ID IN expresion PUNTO PUNTO expresion LLAVEIZQ instrucciones LLAVEDER\n    \n        sen_transferencia : BREAK PUNTOYCOMA\n                          | CONTINUE PUNTOYCOMA\n    \n        declarar_vector : LET MUT ID IGUAL VEC EXCLAMACION CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA\n    \n        declarar_vector : LET MUT ID DOSPUNTOS VEC MENOR tipo MAYOR IGUAL VEC EXCLAMACION CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA\n    \n        declarar_vector : LET ID IGUAL VEC EXCLAMACION CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA\n    \n        declarar_vector : LET ID DOSPUNTOS VEC MENOR tipo MAYOR IGUAL VEC EXCLAMACION CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA\n    \n        declarar_arreglo : LET MUT ID IGUAL CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA\n    \n        declarar_arreglo : LET MUT ID DOSPUNTOS CORCHIZQ tipo PUNTOYCOMA expresion CORCHDER IGUAL CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA\n    \n        declarar_arreglo : LET ID IGUAL CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA\n    \n        declarar_arreglo : LET ID DOSPUNTOS CORCHIZQ tipo PUNTOYCOMA expresion CORCHDER IGUAL CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA\n    \n        llamada_parametros : llamada_parametros COMA valor_parametro\n    \n        llamada_parametros : valor_parametro\n    \n        valor_parametro : expresion\n    \n        asignacion_arreglo : ID CORCHIZQ expresion CORCHDER IGUAL expresion PUNTOYCOMA\n    \n        expresion : ENTERO\n                  | DECIMAL\n    \n        expresion : ID\n    \n        expresion : TRUE\n                  | FALSE\n    \n        expresion : CADENA\n    \n        expresion : CARACTER\n    '
    
_lr_action_items = {'PRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,28,49,50,64,82,85,104,106,109,125,139,147,149,151,156,157,158,159,171,172,177,179,185,187,190,191,193,195,196,197,199,206,207,208,212,215,216,217,218,223,224,229,236,238,240,241,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-66,-67,17,17,-50,-40,-56,17,17,-38,-57,-58,-64,17,-34,-35,-36,-59,-61,17,17,-74,-39,-79,-60,17,17,-52,-72,-37,17,17,-51,-70,17,-63,17,-68,17,-65,-62,-75,-73,-71,-69,]),'PRINTLN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,28,49,50,64,82,85,104,106,109,125,139,147,149,151,156,157,158,159,171,172,177,179,185,187,190,191,193,195,196,197,199,206,207,208,212,215,216,217,218,223,224,229,236,238,240,241,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-66,-67,18,18,-50,-40,-56,18,18,-38,-57,-58,-64,18,-34,-35,-36,-59,-61,18,18,-74,-39,-79,-60,18,18,-52,-72,-37,18,18,-51,-70,18,-63,18,-68,18,-65,-62,-75,-73,-71,-69,]),'LET':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,28,49,50,64,82,85,104,106,109,125,139,147,149,151,156,157,158,159,171,172,177,179,185,187,190,191,193,195,196,197,199,206,207,208,212,215,216,217,218,223,224,229,236,238,240,241,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-66,-67,19,19,-50,-40,-56,19,19,-38,-57,-58,-64,19,-34,-35,-36,-59,-61,19,19,-74,-39,-79,-60,19,19,-52,-72,-37,19,19,-51,-70,19,-63,19,-68,19,-65,-62,-75,-73,-71,-69,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,19,21,22,23,26,27,28,31,33,34,35,37,38,39,49,50,53,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,82,83,84,85,88,89,91,95,104,106,108,109,125,134,137,139,142,145,146,147,149,151,153,155,156,157,158,159,162,164,166,168,171,172,175,177,179,181,183,185,187,190,191,192,193,195,196,197,199,206,207,208,212,215,216,217,218,221,223,224,225,228,229,231,236,238,240,241,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,32,42,42,48,51,42,-2,55,42,42,42,42,42,42,-66,-67,42,42,42,93,20,42,42,42,42,42,42,42,42,42,42,42,42,42,20,42,127,-50,42,93,42,93,-40,-56,42,20,20,42,93,-38,42,93,42,-57,-58,-64,93,127,20,-34,-35,-36,42,93,42,42,-59,-61,42,20,20,42,42,-74,-39,-79,-60,42,20,20,-52,-72,-37,20,20,-51,-70,20,-63,20,-68,42,20,-65,42,42,-62,42,-75,-73,-71,-69,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,28,49,50,64,82,85,104,106,109,125,139,147,149,151,156,157,158,159,171,172,173,177,179,185,187,190,191,193,195,196,197,199,206,207,208,212,215,216,217,218,223,224,229,236,238,240,241,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-66,-67,21,21,-50,-40,-56,21,21,-38,-57,-58,-64,21,-34,-35,-36,-59,-61,192,21,21,-74,-39,-79,-60,21,21,-52,-72,-37,21,21,-51,-70,21,-63,21,-68,21,-65,-62,-75,-73,-71,-69,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,28,49,50,64,82,85,104,106,109,125,139,147,149,151,156,157,158,159,171,172,177,179,185,187,190,191,193,195,196,197,199,206,207,208,212,215,216,217,218,223,224,229,236,238,240,241,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-66,-67,22,22,-50,-40,-56,22,22,-38,-57,-58,-64,22,-34,-35,-36,-59,-61,22,22,-74,-39,-79,-60,22,22,-52,-72,-37,22,22,-51,-70,22,-63,22,-68,22,-65,-62,-75,-73,-71,-69,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,28,49,50,64,82,85,104,106,109,125,139,147,149,151,156,157,158,159,171,172,177,179,185,187,190,191,193,195,196,197,199,206,207,208,212,215,216,217,218,223,224,229,236,238,240,241,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-66,-67,23,23,-50,-40,-56,23,23,-38,-57,-58,-64,23,-34,-35,-36,-59,-61,23,23,-74,-39,-79,-60,23,23,-52,-72,-37,23,23,-51,-70,23,-63,23,-68,23,-65,-62,-75,-73,-71,-69,]),'BREAK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,28,49,50,64,82,85,104,106,109,125,139,147,149,151,156,157,158,159,171,172,177,179,185,187,190,191,193,195,196,197,199,206,207,208,212,215,216,217,218,223,224,229,236,238,240,241,],[24,24,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-66,-67,24,24,-50,-40,-56,24,24,-38,-57,-58,-64,24,-34,-35,-36,-59,-61,24,24,-74,-39,-79,-60,24,24,-52,-72,-37,24,24,-51,-70,24,-63,24,-68,24,-65,-62,-75,-73,-71,-69,]),'CONTINUE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,28,49,50,64,82,85,104,106,109,125,139,147,149,151,156,157,158,159,171,172,177,179,185,187,190,191,193,195,196,197,199,206,207,208,212,215,216,217,218,223,224,229,236,238,240,241,],[25,25,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-66,-67,25,25,-50,-40,-56,25,25,-38,-57,-58,-64,25,-34,-35,-36,-59,-61,25,25,-74,-39,-79,-60,25,25,-52,-72,-37,25,25,-51,-70,25,-63,25,-68,25,-65,-62,-75,-73,-71,-69,]),'FN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,28,49,50,64,82,85,104,106,109,125,139,147,149,151,156,157,158,159,171,172,177,179,185,187,190,191,193,195,196,197,199,206,207,208,212,215,216,217,218,223,224,229,236,238,240,241,],[26,26,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-66,-67,26,26,-50,-40,-56,26,26,-38,-57,-58,-64,26,-34,-35,-36,-59,-61,26,26,-74,-39,-79,-60,26,26,-52,-72,-37,26,26,-51,-70,26,-63,26,-68,26,-65,-62,-75,-73,-71,-69,]),'RETURN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,28,49,50,64,82,85,104,106,109,125,139,147,149,151,156,157,158,159,171,172,177,179,185,187,190,191,193,195,196,197,199,206,207,208,212,215,216,217,218,223,224,229,236,238,240,241,],[27,27,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-66,-67,27,27,-50,-40,-56,27,27,-38,-57,-58,-64,27,-34,-35,-36,-59,-61,27,27,-74,-39,-79,-60,27,27,-52,-72,-37,27,27,-51,-70,27,-63,27,-68,27,-65,-62,-75,-73,-71,-69,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,28,49,50,85,104,106,139,147,149,151,157,158,159,171,172,185,187,190,191,196,197,199,208,212,216,218,224,229,236,238,240,241,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-66,-67,-50,-40,-56,-38,-57,-58,-64,-34,-35,-36,-59,-61,-74,-39,-79,-60,-52,-72,-37,-51,-70,-63,-68,-65,-62,-75,-73,-71,-69,]),'LLAVEDER':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,28,49,50,85,104,106,109,125,139,147,149,151,157,158,159,171,172,179,185,187,190,191,195,196,197,199,206,208,212,216,217,218,223,224,229,236,238,240,241,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-2,-66,-67,-50,-40,-56,149,151,-38,-57,-58,-64,-34,-35,-36,-59,-61,196,-74,-39,-79,-60,208,-52,-72,-37,216,-51,-70,-63,224,-68,229,-65,-62,-75,-73,-71,-69,]),'EXCLAMACION':([17,18,92,135,214,220,],[29,30,141,161,222,226,]),'MUT':([19,],[31,]),'IGUAL':([20,32,55,93,94,96,97,98,99,100,101,102,103,105,136,138,189,201,203,210,],[33,56,88,-49,142,-48,-41,-42,-43,-44,-45,-46,-47,146,162,-48,204,211,213,219,]),'CORCHIZQ':([20,56,57,88,89,141,161,213,219,222,226,],[34,91,95,134,137,166,181,221,225,228,231,]),'PARENTIZQ':([20,21,22,27,29,30,33,34,35,37,38,39,51,53,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,83,88,91,108,123,134,142,146,162,166,168,175,181,183,192,221,225,228,231,],[35,39,39,39,53,54,39,39,39,39,39,39,84,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,150,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'NOT':([21,22,27,33,34,35,37,38,39,53,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,83,88,91,108,134,142,146,162,166,168,175,181,183,192,221,225,228,231,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'MENOS':([21,22,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,52,53,54,56,58,59,63,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80,81,83,86,87,88,90,91,108,110,111,112,113,114,115,116,117,118,119,120,121,122,124,126,133,134,142,146,162,166,167,168,170,174,175,181,182,183,188,192,194,200,205,221,225,228,231,],[38,38,38,38,38,38,74,38,38,38,-80,-81,-82,-83,-84,-85,-86,74,74,38,38,38,74,74,74,38,38,38,38,38,38,38,38,38,38,38,38,38,74,-31,74,38,74,74,38,74,38,38,74,74,74,74,74,74,74,74,-26,-27,-28,-29,-30,-32,74,74,38,38,38,38,38,74,38,74,-33,38,38,74,38,74,38,74,74,74,38,38,38,38,]),'ENTERO':([21,22,27,33,34,35,37,38,39,53,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,83,88,91,108,134,142,146,162,166,168,175,181,183,192,221,225,228,231,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'DECIMAL':([21,22,27,33,34,35,37,38,39,53,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,83,88,91,108,134,142,146,162,166,168,175,181,183,192,221,225,228,231,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'TRUE':([21,22,27,33,34,35,37,38,39,53,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,83,88,91,108,134,142,146,162,166,168,175,181,183,192,221,225,228,231,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'FALSE':([21,22,27,33,34,35,37,38,39,53,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,83,88,91,108,134,142,146,162,166,168,175,181,183,192,221,225,228,231,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'CADENA':([21,22,27,33,34,35,37,38,39,53,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,83,88,91,108,134,142,146,162,166,168,175,181,183,192,221,225,228,231,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'CARACTER':([21,22,27,33,34,35,37,38,39,53,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,83,88,91,108,134,142,146,162,166,168,175,181,183,192,221,225,228,231,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'PUNTOYCOMA':([24,25,40,41,42,43,44,45,46,52,58,60,79,80,90,93,97,98,99,100,101,102,103,107,110,111,112,113,114,115,116,117,118,119,120,121,122,124,131,132,133,143,144,163,165,167,170,174,180,182,202,209,232,234,237,239,],[49,50,-80,-81,-82,-83,-84,-85,-86,85,104,106,-25,-31,139,-49,-41,-42,-43,-44,-45,-46,-47,147,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-32,157,158,159,168,-48,183,185,187,190,-33,197,199,212,218,236,238,240,241,]),'DOSPUNTOS':([32,55,127,],[57,89,153,]),'PARENTDER':([35,40,41,42,43,44,45,46,61,62,63,79,80,81,84,86,87,93,97,98,99,100,101,102,103,110,111,112,113,114,115,116,117,118,119,120,121,122,124,128,130,144,148,150,174,176,178,],[60,-80,-81,-82,-83,-84,-85,-86,107,-77,-78,-25,-31,124,129,131,132,-49,-41,-42,-43,-44,-45,-46,-47,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-32,154,-54,-48,-76,174,-33,-55,-53,]),'LLAVEIZQ':([36,40,41,42,43,44,45,46,47,79,80,110,111,112,113,114,115,116,117,118,119,120,121,122,124,129,154,173,174,194,205,],[64,-80,-81,-82,-83,-84,-85,-86,82,-25,-31,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-32,156,177,193,-33,207,215,]),'MAYOR':([36,40,41,42,43,44,45,46,47,52,58,59,63,79,80,81,86,87,90,93,97,98,99,100,101,102,103,110,111,112,113,114,115,116,117,118,119,120,121,122,124,126,133,144,167,169,170,174,182,184,188,194,200,205,],[65,-80,-81,-82,-83,-84,-85,-86,65,65,65,65,65,65,-31,65,65,65,65,-49,-41,-42,-43,-44,-45,-46,-47,-17,-18,-19,-20,-21,-22,65,65,-26,-27,-28,-29,-30,-32,65,65,-48,65,189,65,-33,65,201,65,65,65,65,]),'MENOR':([36,40,41,42,43,44,45,46,47,52,58,59,63,79,80,81,86,87,90,96,110,111,112,113,114,115,116,117,118,119,120,121,122,124,126,133,138,167,170,174,182,188,194,200,205,],[66,-80,-81,-82,-83,-84,-85,-86,66,66,66,66,66,66,-31,66,66,66,66,145,-17,-18,-19,-20,-21,-22,66,66,-26,-27,-28,-29,-30,-32,66,66,164,66,66,-33,66,66,66,66,66,]),'MAYORIGUAL':([36,40,41,42,43,44,45,46,47,52,58,59,63,79,80,81,86,87,90,110,111,112,113,114,115,116,117,118,119,120,121,122,124,126,133,167,170,174,182,188,194,200,205,],[67,-80,-81,-82,-83,-84,-85,-86,67,67,67,67,67,67,-31,67,67,67,67,-17,-18,-19,-20,-21,-22,67,67,-26,-27,-28,-29,-30,-32,67,67,67,67,-33,67,67,67,67,67,]),'MENORIGUAL':([36,40,41,42,43,44,45,46,47,52,58,59,63,79,80,81,86,87,90,110,111,112,113,114,115,116,117,118,119,120,121,122,124,126,133,167,170,174,182,188,194,200,205,],[68,-80,-81,-82,-83,-84,-85,-86,68,68,68,68,68,68,-31,68,68,68,68,-17,-18,-19,-20,-21,-22,68,68,-26,-27,-28,-29,-30,-32,68,68,68,68,-33,68,68,68,68,68,]),'IGUALIGUAL':([36,40,41,42,43,44,45,46,47,52,58,59,63,79,80,81,86,87,90,110,111,112,113,114,115,116,117,118,119,120,121,122,124,126,133,167,170,174,182,188,194,200,205,],[69,-80,-81,-82,-83,-84,-85,-86,69,69,69,69,69,69,-31,69,69,69,69,-17,-18,-19,-20,-21,-22,69,69,-26,-27,-28,-29,-30,-32,69,69,69,69,-33,69,69,69,69,69,]),'NOIGUAL':([36,40,41,42,43,44,45,46,47,52,58,59,63,79,80,81,86,87,90,110,111,112,113,114,115,116,117,118,119,120,121,122,124,126,133,167,170,174,182,188,194,200,205,],[70,-80,-81,-82,-83,-84,-85,-86,70,70,70,70,70,70,-31,70,70,70,70,-17,-18,-19,-20,-21,-22,70,70,-26,-27,-28,-29,-30,-32,70,70,70,70,-33,70,70,70,70,70,]),'OR':([36,40,41,42,43,44,45,46,47,52,58,59,63,79,80,81,86,87,90,110,111,112,113,114,115,116,117,118,119,120,121,122,124,126,133,167,170,174,182,188,194,200,205,],[71,-80,-81,-82,-83,-84,-85,-86,71,71,71,71,71,-25,-31,71,71,71,71,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-32,71,71,71,71,-33,71,71,71,71,71,]),'AND':([36,40,41,42,43,44,45,46,47,52,58,59,63,79,80,81,86,87,90,110,111,112,113,114,115,116,117,118,119,120,121,122,124,126,133,167,170,174,182,188,194,200,205,],[72,-80,-81,-82,-83,-84,-85,-86,72,72,72,72,72,-25,-31,72,72,72,72,-17,-18,-19,-20,-21,-22,72,-24,-26,-27,-28,-29,-30,-32,72,72,72,72,-33,72,72,72,72,72,]),'MAS':([36,40,41,42,43,44,45,46,47,52,58,59,63,79,80,81,86,87,90,110,111,112,113,114,115,116,117,118,119,120,121,122,124,126,133,167,170,174,182,188,194,200,205,],[73,-80,-81,-82,-83,-84,-85,-86,73,73,73,73,73,73,-31,73,73,73,73,73,73,73,73,73,73,73,73,-26,-27,-28,-29,-30,-32,73,73,73,73,-33,73,73,73,73,73,]),'POR':([36,40,41,42,43,44,45,46,47,52,58,59,63,79,80,81,86,87,90,110,111,112,113,114,115,116,117,118,119,120,121,122,124,126,133,167,170,174,182,188,194,200,205,],[75,-80,-81,-82,-83,-84,-85,-86,75,75,75,75,75,75,-31,75,75,75,75,75,75,75,75,75,75,75,75,75,75,-28,-29,-30,-32,75,75,75,75,-33,75,75,75,75,75,]),'DIVISION':([36,40,41,42,43,44,45,46,47,52,58,59,63,79,80,81,86,87,90,110,111,112,113,114,115,116,117,118,119,120,121,122,124,126,133,167,170,174,182,188,194,200,205,],[76,-80,-81,-82,-83,-84,-85,-86,76,76,76,76,76,76,-31,76,76,76,76,76,76,76,76,76,76,76,76,76,76,-28,-29,-30,-32,76,76,76,76,-33,76,76,76,76,76,]),'MODULO':([36,40,41,42,43,44,45,46,47,52,58,59,63,79,80,81,86,87,90,110,111,112,113,114,115,116,117,118,119,120,121,122,124,126,133,167,170,174,182,188,194,200,205,],[77,-80,-81,-82,-83,-84,-85,-86,77,77,77,77,77,77,-31,77,77,77,77,77,77,77,77,77,77,77,77,77,77,-28,-29,-30,-32,77,77,77,77,-33,77,77,77,77,77,]),'PUNTO':([36,40,41,42,43,44,45,46,47,52,58,59,63,79,80,81,86,87,90,110,111,112,113,114,115,116,117,118,119,120,121,122,124,126,133,152,167,170,174,182,188,194,200,205,],[78,-80,-81,-82,-83,-84,-85,-86,78,78,78,78,78,-25,-31,78,78,78,78,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-32,152,78,175,78,78,-33,78,78,78,78,78,]),'CORCHDER':([40,41,42,43,44,45,46,59,62,63,79,80,110,111,112,113,114,115,116,117,118,119,120,121,122,124,140,148,160,174,186,188,198,200,227,230,233,235,],[-80,-81,-82,-83,-84,-85,-86,105,-77,-78,-25,-31,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-32,165,-76,180,-33,202,203,209,210,232,234,237,239,]),'COMA':([40,41,42,43,44,45,46,61,62,63,79,80,93,97,98,99,100,101,102,103,110,111,112,113,114,115,116,117,118,119,120,121,122,124,128,130,140,144,148,160,174,176,178,186,198,227,230,233,235,],[-80,-81,-82,-83,-84,-85,-86,108,-77,-78,-25,-31,-49,-41,-42,-43,-44,-45,-46,-47,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-32,155,-54,108,-48,-76,108,-33,-55,-53,108,108,108,108,108,108,]),'IN':([48,],[83,]),'VEC':([56,57,88,89,95,137,145,153,164,204,211,],[92,96,135,138,144,144,144,144,144,214,220,]),'I64':([57,89,95,137,145,153,164,],[97,97,97,97,97,97,97,]),'F64':([57,89,95,137,145,153,164,],[98,98,98,98,98,98,98,]),'BOOL':([57,89,95,137,145,153,164,],[99,99,99,99,99,99,99,]),'CHAR':([57,89,95,137,145,153,164,],[100,100,100,100,100,100,100,]),'STRING':([57,89,95,137,145,153,164,],[101,101,101,101,101,101,101,]),'STR':([57,89,95,137,145,153,164,],[102,102,102,102,102,102,102,]),'USIZE':([57,89,95,137,145,153,164,],[103,103,103,103,103,103,103,]),'LEN':([78,152,],[123,123,]),'ELSE':([149,171,172,191,216,229,],[173,173,-61,-60,-63,-62,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,64,82,156,177,193,207,215,],[2,109,125,179,195,206,217,223,]),'instruccion':([0,2,64,82,109,125,156,177,179,193,195,206,207,215,217,223,],[3,28,3,3,28,28,3,3,28,3,28,28,3,3,28,28,]),'impresion':([0,2,64,82,109,125,156,177,179,193,195,206,207,215,217,223,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'declaracion':([0,2,64,82,109,125,156,177,179,193,195,206,207,215,217,223,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'asignacion':([0,2,64,82,109,125,156,177,179,193,195,206,207,215,217,223,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'sentencia_if':([0,2,64,82,109,125,156,177,179,193,195,206,207,215,217,223,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'ciclo_while':([0,2,64,82,109,125,156,177,179,193,195,206,207,215,217,223,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'ciclo_for':([0,2,64,82,109,125,156,177,179,193,195,206,207,215,217,223,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'declarar_arreglo':([0,2,64,82,109,125,156,177,179,193,195,206,207,215,217,223,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'asignacion_arreglo':([0,2,64,82,109,125,156,177,179,193,195,206,207,215,217,223,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'declarar_vector':([0,2,64,82,109,125,156,177,179,193,195,206,207,215,217,223,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'sen_transferencia':([0,2,64,82,109,125,156,177,179,193,195,206,207,215,217,223,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'funcion':([0,2,64,82,109,125,156,177,179,193,195,206,207,215,217,223,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'llamada_funcion':([0,2,64,82,109,125,156,177,179,193,195,206,207,215,217,223,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'return':([0,2,64,82,109,125,156,177,179,193,195,206,207,215,217,223,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'expresion':([21,22,27,33,34,35,37,38,39,53,54,56,65,66,67,68,69,70,71,72,73,74,75,76,77,83,88,91,108,134,142,146,162,166,168,175,181,183,192,221,225,228,231,],[36,47,52,58,59,63,79,80,81,86,87,90,110,111,112,113,114,115,116,117,118,119,120,121,122,126,133,63,63,63,167,170,182,63,188,194,63,200,205,63,63,63,63,]),'llamada_parametros':([35,91,134,166,181,221,225,228,231,],[61,140,160,186,198,227,230,233,235,]),'valor_parametro':([35,91,108,134,166,181,221,225,228,231,],[62,62,148,62,62,62,62,62,62,62,]),'tipo':([57,89,95,137,145,153,164,],[94,136,143,163,169,176,184,]),'lista_parametros':([84,],[128,]),'parametro':([84,155,],[130,178,]),'elseif':([149,],[171,]),'lista_elseif':([149,171,],[172,191,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','gramatica.py',221),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','gramatica.py',227),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',233),
  ('instruccion -> impresion','instruccion',1,'p_instruccion','gramatica.py',238),
  ('instruccion -> declaracion','instruccion',1,'p_instruccion','gramatica.py',239),
  ('instruccion -> asignacion','instruccion',1,'p_instruccion','gramatica.py',240),
  ('instruccion -> sentencia_if','instruccion',1,'p_instruccion','gramatica.py',241),
  ('instruccion -> ciclo_while','instruccion',1,'p_instruccion','gramatica.py',242),
  ('instruccion -> ciclo_for','instruccion',1,'p_instruccion','gramatica.py',243),
  ('instruccion -> declarar_arreglo','instruccion',1,'p_instruccion','gramatica.py',244),
  ('instruccion -> asignacion_arreglo','instruccion',1,'p_instruccion','gramatica.py',245),
  ('instruccion -> declarar_vector','instruccion',1,'p_instruccion','gramatica.py',246),
  ('instruccion -> sen_transferencia','instruccion',1,'p_instruccion','gramatica.py',247),
  ('instruccion -> funcion','instruccion',1,'p_instruccion','gramatica.py',248),
  ('instruccion -> llamada_funcion','instruccion',1,'p_instruccion','gramatica.py',249),
  ('instruccion -> return','instruccion',1,'p_instruccion','gramatica.py',250),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_logica','gramatica.py',256),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_logica','gramatica.py',257),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_logica','gramatica.py',258),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_logica','gramatica.py',259),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_logica','gramatica.py',260),
  ('expresion -> expresion NOIGUAL expresion','expresion',3,'p_logica','gramatica.py',261),
  ('expresion -> expresion OR expresion','expresion',3,'p_relacionales','gramatica.py',278),
  ('expresion -> expresion AND expresion','expresion',3,'p_relacionales','gramatica.py',279),
  ('expresion -> NOT expresion','expresion',2,'p_relacionales_not','gramatica.py',288),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','gramatica.py',294),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','gramatica.py',295),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','gramatica.py',296),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_expresion_binaria','gramatica.py',297),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_binaria','gramatica.py',298),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','gramatica.py',312),
  ('expresion -> PARENTIZQ expresion PARENTDER','expresion',3,'p_expresion_parentesis','gramatica.py',317),
  ('expresion -> expresion PUNTO LEN PARENTIZQ PARENTDER','expresion',5,'p_fn_nativas_vectores','gramatica.py',323),
  ('impresion -> PRINT EXCLAMACION PARENTIZQ expresion PARENTDER PUNTOYCOMA','impresion',6,'p_impresion','gramatica.py',329),
  ('impresion -> PRINTLN EXCLAMACION PARENTIZQ expresion PARENTDER PUNTOYCOMA','impresion',6,'p_impresion','gramatica.py',330),
  ('declaracion -> LET MUT ID IGUAL expresion PUNTOYCOMA','declaracion',6,'p_declaracion_mutable','gramatica.py',339),
  ('declaracion -> LET MUT ID DOSPUNTOS tipo IGUAL expresion PUNTOYCOMA','declaracion',8,'p_declaracion_mutable_tipo','gramatica.py',345),
  ('declaracion -> LET ID IGUAL expresion PUNTOYCOMA','declaracion',5,'p_declaracion_no_mutable','gramatica.py',364),
  ('declaracion -> LET ID DOSPUNTOS tipo IGUAL expresion PUNTOYCOMA','declaracion',7,'p_declaracion_no_mutable_tipo','gramatica.py',370),
  ('asignacion -> ID IGUAL expresion PUNTOYCOMA','asignacion',4,'p_asignacion_nuevo_valor','gramatica.py',389),
  ('tipo -> I64','tipo',1,'p_tipo','gramatica.py',395),
  ('tipo -> F64','tipo',1,'p_tipo','gramatica.py',396),
  ('tipo -> BOOL','tipo',1,'p_tipo','gramatica.py',397),
  ('tipo -> CHAR','tipo',1,'p_tipo','gramatica.py',398),
  ('tipo -> STRING','tipo',1,'p_tipo','gramatica.py',399),
  ('tipo -> STR','tipo',1,'p_tipo','gramatica.py',400),
  ('tipo -> USIZE','tipo',1,'p_tipo','gramatica.py',401),
  ('tipo -> VEC','tipo',1,'p_tipo','gramatica.py',402),
  ('tipo -> ID','tipo',1,'p_tipo','gramatica.py',403),
  ('return -> RETURN expresion PUNTOYCOMA','return',3,'p_return','gramatica.py',409),
  ('funcion -> FN ID PARENTIZQ lista_parametros PARENTDER LLAVEIZQ instrucciones LLAVEDER','funcion',8,'p_funcion_sin_return','gramatica.py',415),
  ('funcion -> FN ID PARENTIZQ PARENTDER LLAVEIZQ instrucciones LLAVEDER','funcion',7,'p_funcion_sin_return','gramatica.py',416),
  ('lista_parametros -> lista_parametros COMA parametro','lista_parametros',3,'p_lista_parametros','gramatica.py',425),
  ('lista_parametros -> parametro','lista_parametros',1,'p_parametros','gramatica.py',432),
  ('parametro -> ID DOSPUNTOS tipo','parametro',3,'p_parametro_tipo','gramatica.py',438),
  ('llamada_funcion -> ID PARENTIZQ PARENTDER PUNTOYCOMA','llamada_funcion',4,'p_llamada_funcion','gramatica.py',444),
  ('llamada_funcion -> ID PARENTIZQ llamada_parametros PARENTDER PUNTOYCOMA','llamada_funcion',5,'p_llamada_funcion','gramatica.py',445),
  ('sentencia_if -> IF expresion LLAVEIZQ instrucciones LLAVEDER','sentencia_if',5,'p_sentencia_if','gramatica.py',473),
  ('sentencia_if -> IF expresion LLAVEIZQ instrucciones LLAVEDER elseif','sentencia_if',6,'p_sentencia_if_elseif','gramatica.py',479),
  ('elseif -> elseif lista_elseif','elseif',2,'p_lista_else_if','gramatica.py',485),
  ('elseif -> lista_elseif','elseif',1,'p_lista_esle_if2','gramatica.py',492),
  ('lista_elseif -> ELSE IF expresion LLAVEIZQ instrucciones LLAVEDER','lista_elseif',6,'p_else_elseif','gramatica.py',498),
  ('lista_elseif -> ELSE LLAVEIZQ instrucciones LLAVEDER','lista_elseif',4,'p_else_elseif','gramatica.py',499),
  ('ciclo_while -> WHILE expresion LLAVEIZQ instrucciones LLAVEDER','ciclo_while',5,'p_ciclo_while','gramatica.py',508),
  ('ciclo_for -> FOR ID IN expresion PUNTO PUNTO expresion LLAVEIZQ instrucciones LLAVEDER','ciclo_for',10,'p_ciclo_for','gramatica.py',514),
  ('sen_transferencia -> BREAK PUNTOYCOMA','sen_transferencia',2,'p_sen_transferencia','gramatica.py',520),
  ('sen_transferencia -> CONTINUE PUNTOYCOMA','sen_transferencia',2,'p_sen_transferencia','gramatica.py',521),
  ('declarar_vector -> LET MUT ID IGUAL VEC EXCLAMACION CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA','declarar_vector',10,'p_declaracion_vector_mutable','gramatica.py',530),
  ('declarar_vector -> LET MUT ID DOSPUNTOS VEC MENOR tipo MAYOR IGUAL VEC EXCLAMACION CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA','declarar_vector',15,'p_declaracion_vector_mutable_tipo','gramatica.py',536),
  ('declarar_vector -> LET ID IGUAL VEC EXCLAMACION CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA','declarar_vector',9,'p_declaracion_vector_no_mutable','gramatica.py',557),
  ('declarar_vector -> LET ID DOSPUNTOS VEC MENOR tipo MAYOR IGUAL VEC EXCLAMACION CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA','declarar_vector',14,'p_declaracion_vector_no_mutable_tipo','gramatica.py',563),
  ('declarar_arreglo -> LET MUT ID IGUAL CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA','declarar_arreglo',8,'p_declaracion_arreglo_mutable','gramatica.py',584),
  ('declarar_arreglo -> LET MUT ID DOSPUNTOS CORCHIZQ tipo PUNTOYCOMA expresion CORCHDER IGUAL CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA','declarar_arreglo',14,'p_declaracion_arreglo_mutable_tipo','gramatica.py',590),
  ('declarar_arreglo -> LET ID IGUAL CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA','declarar_arreglo',7,'p_declaracion_arreglo_no_mutable','gramatica.py',611),
  ('declarar_arreglo -> LET ID DOSPUNTOS CORCHIZQ tipo PUNTOYCOMA expresion CORCHDER IGUAL CORCHIZQ llamada_parametros CORCHDER PUNTOYCOMA','declarar_arreglo',13,'p_declaracion_arreglo_no_mutable_tipo','gramatica.py',617),
  ('llamada_parametros -> llamada_parametros COMA valor_parametro','llamada_parametros',3,'p_lista_llamada_parametros','gramatica.py',638),
  ('llamada_parametros -> valor_parametro','llamada_parametros',1,'p_llamada_parametros','gramatica.py',645),
  ('valor_parametro -> expresion','valor_parametro',1,'p_valor_parametro','gramatica.py',651),
  ('asignacion_arreglo -> ID CORCHIZQ expresion CORCHDER IGUAL expresion PUNTOYCOMA','asignacion_arreglo',7,'p_asignacion_arreglo_1x1','gramatica.py',657),
  ('expresion -> ENTERO','expresion',1,'p_expresion_numero','gramatica.py',663),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_numero','gramatica.py',664),
  ('expresion -> ID','expresion',1,'p_expresion_id','gramatica.py',670),
  ('expresion -> TRUE','expresion',1,'p_expresion_bool','gramatica.py',676),
  ('expresion -> FALSE','expresion',1,'p_expresion_bool','gramatica.py',677),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','gramatica.py',685),
  ('expresion -> CARACTER','expresion',1,'p_expresion_caracter','gramatica.py',691),
]
