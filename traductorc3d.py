from re import TEMPLATE
import tab_simbolos as TABS
import gramatica as g
from expresiones import  *
from instrucciones import *
import temporal as T

t_global = T.Temporales()
mensaje = ""
cadenafuncion = ""
LFunciones = []
existe_break = False
existe_continue = False
Lista_Break = ""
Lista_Continue = ""
posH = 0
fila = 0
fila += 16

ListaAllAsignacion = []
ListaAsignacion = []
ListaAsignacion2 = []

Lista_return = []

def instruccion_print(instruccion, ts, ambito):
    global t_global, LFunciones, cadenafuncion, fila
    cadena = ""
    comprobar = True
    print(instruccion.exp)
    if(isinstance(instruccion.exp, ExpresionBinaria)):
        if(isinstance(instruccion.exp.exp1, ExpresionBinaria)):
            if(isinstance(instruccion.exp.exp1.exp2, ExpresionDobleComilla) or isinstance(instruccion.exp.exp1.exp1, ExpresionDobleComilla)):
                comprobar = False

    tipos = ""
    if(isinstance(instruccion.exp, ExpresionIdentificador)):
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.nombre == instruccion.exp.id):
                tipos = tipo.tipo

    if(isinstance(instruccion.exp, ExpresionBinaria) and not isinstance(instruccion.exp.exp1, ExpresionDobleComilla) and not isinstance(instruccion.exp.exp2, ExpresionDobleComilla) and comprobar):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%f\", " + str(tmp) +"); \n"
        fila += 1
    elif(isinstance(instruccion.exp, ExpresionNumero)):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%d\", (int)" + str(tmp) +"); \n"
        fila += 1
    elif(isinstance(instruccion.exp, ExpresionNegativa)):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%d\", (int)" + str(tmp) +"); \n"
        fila += 1
    elif(isinstance(instruccion.exp, ExpresionCaracter)):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%c\", " + str(ord(tmp)) +"); \n"
        fila += 1
    elif(isinstance(instruccion.exp, ExpresionLogica)):
        newT = t_global.etiquetaT()
        LV, LF, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena += c3d
        cadena += "\t "+ LV + ": \n"
        cadena += "\t printf(\"%c\", (int)116); \n"
        cadena += "\t printf(\"%c\", (int)114); \n"
        cadena += "\t printf(\"%c\", (int)117); \n"
        cadena += "\t printf(\"%c\", (int)101); \n"
        cadena += "\t goto " + newT + "; \n"

        cadena += "\t "+ LF + ": \n"
        cadena += "\t printf(\"%c\", (int)102); \n"
        cadena += "\t printf(\"%c\", (int)97); \n"
        cadena += "\t printf(\"%c\", (int)108); \n"
        cadena += "\t printf(\"%c\", (int)115); \n"
        cadena += "\t printf(\"%c\", (int)101); \n"
        cadena += "\t " + newT + ": \n"
        fila += 13
    elif(isinstance(instruccion.exp, ExpresionRelacional)):
        newT = t_global.etiquetaT()
        LV, LF, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena += c3d
        if(type(LV) != list):
            cadena += "\t " + LV + ":\n"
            fila += 1
        else:
            for n in LV:
                cadena += "\t " + n + ":\n"
                fila += 1

        cadena += "\t printf(\"%c\", (int)116); \n"
        cadena += "\t printf(\"%c\", (int)114); \n"
        cadena += "\t printf(\"%c\", (int)117); \n"
        cadena += "\t printf(\"%c\", (int)101); \n"
        cadena += "\t goto " + newT + "; \n"
        fila += 5

        if(type(LF) != list):
            cadena += "\t " + LF + ":\n"
            fila += 1
        else:
            for n in LF:
                cadena += "\t " + n + ":\n"
                fila += 1
        
        cadena += "\t printf(\"%c\", (int)102); \n"
        cadena += "\t printf(\"%c\", (int)97); \n"
        cadena += "\t printf(\"%c\", (int)108); \n"
        cadena += "\t printf(\"%c\", (int)115); \n"
        cadena += "\t printf(\"%c\", (int)101); \n"
        cadena += "\t " + newT + ": \n"
        fila += 6
    elif(isinstance(instruccion.exp, ExpresionIdentificador) and tipos == TABS.TIPO_DATO.CHAR):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%c\", (int)" + str(tmp) + "); \n"
        fila += 1
    elif(isinstance(instruccion.exp, ExpresionIdentificador) and tipos != TABS.TIPO_DATO.STRING):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%f\"," + str(tmp) + "); \n"
        fila += 1
    else:
        if "printString" not in LFunciones:
            funcionPrint = ""
            Lfloat = t_global.etiquetaT()
            Lint = t_global.etiquetaT()
            newT3 = t_global.varTemporal()
            newT4 = t_global.varTemporal()
            newT5 = t_global.varTemporal()

            Ltrue = t_global.etiquetaT()
            Lsalto = t_global.etiquetaT()

            funcionPrint += "void concatenarCadena(){\n"
            funcionPrint += "\t " + newT3 + " = P + 1; \n"
            funcionPrint += "\t " + newT4 + " = stack[(int)" + newT3 + "]; \n"
            funcionPrint += "\t " + Lsalto + ": \n"
            funcionPrint += "\t " + newT5 + " = heap[(int)" + newT4 + "]; \n"
            funcionPrint += "\t if (" + newT5 + " == -3) goto " + Lfloat + "; \n"
            funcionPrint += "\t if (" + newT5 + " == -2) goto " + Lint + "; \n"
            funcionPrint += "\t if (" + newT5 + " == -1) goto " + Ltrue + "; \n"
            funcionPrint += "\t printf(\"%c\", (int)" + newT5+ "); \n"
            funcionPrint += "\t " + newT4 + " = " + newT4 + " + 1; \n"
            funcionPrint += "\t goto " + Lsalto + "; \n"

            funcionPrint += "\t " + Lfloat + ": \n"
            funcionPrint += "\t " + newT4 + " = " + newT4 + " + 1; \n"
            funcionPrint += "\t " + newT5 + " = heap[(int)" + newT4 + "]; \n"
            funcionPrint += "\t printf(\"%f\", "+ newT5 + "); \n"
            funcionPrint += "\t " + newT4 + " = " + newT4 + " + 1; \n"
            funcionPrint += "\t goto " + Lsalto +"; \n"

            funcionPrint += "\t " + Lint + ": \n"
            funcionPrint += "\t " + newT4 + " = " + newT4 + " + 1; \n"
            funcionPrint += "\t " + newT5 + " = heap[(int)" + newT4 + "]; \n"
            funcionPrint += "\t printf(\"%d\", (int)" + newT5 + "); \n"
            funcionPrint += "\t " + newT4 + " = " + newT4 + " + 1; \n"
            funcionPrint += "\t goto " + Lsalto + "; \n"

            funcionPrint += "\t " + Ltrue + ":\n"
            funcionPrint += "\t return; \n"
            funcionPrint += "} \n"
            fila += 26
            cadenafuncion += funcionPrint
            LFunciones.append("printString")

        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        newT = t_global.varTemporal()
        newT2 = t_global.varTemporal()
        newT6 = t_global.varTemporal()

        cadena += c3d +"\t " + newT + " = P + 0; \n"
        cadena += "\t " + newT2 + " = " + newT + " + 1; \n"
        cadena += "\t stack[(int)" + newT2 + "]= " + tmp + "; \n"
        cadena += "\t P = P + 0; \n"
        cadena += "\t concatenarCadena(); \n"
        cadena += "\t " + newT6 + " = stack[(int)P]; \n"
        cadena += "\t P = P - 0; \n"
        fila += 7
    return cadena

def instruccion_println(instruccion, ts, ambito):
    global t_global, LFunciones, cadenafuncion, fila
    cadena = ""
    comprobar = True
    print(instruccion.exp)
    if(isinstance(instruccion.exp, ExpresionBinaria)):
        if(isinstance(instruccion.exp.exp1, ExpresionBinaria)):
            if(isinstance(instruccion.exp.exp1.exp2, ExpresionDobleComilla) or isinstance(instruccion.exp.exp1.exp1, ExpresionDobleComilla)):
                comprobar = False

    tipos = ""
    if(isinstance(instruccion.exp, ExpresionIdentificador)):
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.nombre == instruccion.exp.id):
                tipos = tipo.tipo

    if(isinstance(instruccion.exp, ExpresionBinaria) and not isinstance(instruccion.exp.exp1, ExpresionDobleComilla) and not isinstance(instruccion.exp.exp2, ExpresionDobleComilla) and comprobar):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%f\", " + str(tmp) +"); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        fila += 2
    elif(isinstance(instruccion.exp, ExpresionNumero)):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%d\", (int)" + str(tmp) +"); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        fila += 2
    elif(isinstance(instruccion.exp, ExpresionNegativa)):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%d\", (int)" + str(tmp) +"); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        fila += 2
    elif(isinstance(instruccion.exp, ExpresionCaracter)):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%c\", " + str(ord(tmp)) +"); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        fila += 2
    elif(isinstance(instruccion.exp, ExpresionLogica)):
        newT = t_global.etiquetaT()
        LV, LF, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena += c3d
        cadena += "\t "+ LV + ": \n"
        cadena += "\t printf(\"%c\", (int)116); \n"
        cadena += "\t printf(\"%c\", (int)114); \n"
        cadena += "\t printf(\"%c\", (int)117); \n"
        cadena += "\t printf(\"%c\", (int)101); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        cadena += "\t goto " + newT + "; \n"

        cadena += "\t "+ LF + ": \n"
        cadena += "\t printf(\"%c\", (int)102); \n"
        cadena += "\t printf(\"%c\", (int)97); \n"
        cadena += "\t printf(\"%c\", (int)108); \n"
        cadena += "\t printf(\"%c\", (int)115); \n"
        cadena += "\t printf(\"%c\", (int)101); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        cadena += "\t " + newT + ": \n"
        fila += 15
    elif(isinstance(instruccion.exp, ExpresionRelacional)):
        newT = t_global.etiquetaT()
        LV, LF, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena += c3d
        if(type(LV) != list):
            cadena += "\t " + LV + ":\n"
            fila += 1
        else:
            for n in LV:
                cadena += "\t " + n + ":\n"
                fila += 1

        cadena += "\t printf(\"%c\", (int)116); \n"
        cadena += "\t printf(\"%c\", (int)114); \n"
        cadena += "\t printf(\"%c\", (int)117); \n"
        cadena += "\t printf(\"%c\", (int)101); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        cadena += "\t goto " + newT + "; \n"
        fila += 6

        if(type(LF) != list):
            cadena += "\t " + LF + ":\n"
            fila += 1
        else:
            for n in LF:
                cadena += "\t " + n + ":\n"
                fila += 1
        
        cadena += "\t printf(\"%c\", (int)102); \n"
        cadena += "\t printf(\"%c\", (int)97); \n"
        cadena += "\t printf(\"%c\", (int)108); \n"
        cadena += "\t printf(\"%c\", (int)115); \n"
        cadena += "\t printf(\"%c\", (int)101); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        cadena += "\t " + newT + ": \n"
        fila += 7
    elif(isinstance(instruccion.exp, ExpresionIdentificador) and tipos == TABS.TIPO_DATO.CHAR):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%c\", (int)" + str(tmp) + "); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        fila += 2

    #Falta una instancia de tipo list

    elif(isinstance(instruccion.exp, ExpresionIdentificador) and tipos != TABS.TIPO_DATO.STRING):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%f\"," + str(tmp) + "); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        fila += 2

    #Falta una instancia de tipo list

    else:
        if "printString" not in LFunciones:
            funcionPrint = ""
            Lfloat = t_global.etiquetaT()
            Lint = t_global.etiquetaT()
            newT3 = t_global.varTemporal()
            newT4 = t_global.varTemporal()
            newT5 = t_global.varTemporal()

            Ltrue = t_global.etiquetaT()
            Lsalto = t_global.etiquetaT()

            funcionPrint += "void concatenarCadena(){\n"
            funcionPrint += "\t " + newT3 + " = P + 1; \n"
            funcionPrint += "\t " + newT4 + " = stack[(int)" + newT3 + "]; \n"
            funcionPrint += "\t " + Lsalto + ": \n"
            funcionPrint += "\t " + newT5 + " = heap[(int)" + newT4 + "]; \n"
            funcionPrint += "\t if (" + newT5 + " == -3) goto " + Lfloat + "; \n"
            funcionPrint += "\t if (" + newT5 + " == -2) goto " + Lint + "; \n"
            funcionPrint += "\t if (" + newT5 + " == -1) goto " + Ltrue + "; \n"
            funcionPrint += "\t printf(\"%c\", (int)" + newT5+ "); \n"
            funcionPrint += "\t " + newT4 + " = " + newT4 + " + 1; \n"
            funcionPrint += "\t goto " + Lsalto + "; \n"

            funcionPrint += "\t " + Lfloat + ": \n"
            funcionPrint += "\t " + newT4 + " = " + newT4 + " + 1; \n"
            funcionPrint += "\t " + newT5 + " = heap[(int)" + newT4 + "]; \n"
            funcionPrint += "\t printf(\"%f\", "+ newT5 + "); \n"
            funcionPrint += "\t " + newT4 + " = " + newT4 + " + 1; \n"
            funcionPrint += "\t goto " + Lsalto +"; \n"

            funcionPrint += "\t " + Lint + ": \n"
            funcionPrint += "\t " + newT4 + " = " + newT4 + " + 1; \n"
            funcionPrint += "\t " + newT5 + " = heap[(int)" + newT4 + "]; \n"
            funcionPrint += "\t printf(\"%d\", (int)" + newT5 + "); \n"
            funcionPrint += "\t " + newT4 + " = " + newT4 + " + 1; \n"
            funcionPrint += "\t goto " + Lsalto + "; \n"

            funcionPrint += "\t " + Ltrue + ":\n"
            funcionPrint += "\t return; \n"
            funcionPrint += "} \n"
            fila += 26
            cadenafuncion += funcionPrint
            LFunciones.append("printString")

        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        newT = t_global.varTemporal()
        newT2 = t_global.varTemporal()
        newT6 = t_global.varTemporal()

        cadena += c3d +"\t " + newT + " = P + 0; \n"
        cadena += "\t " + newT2 + " = " + newT + " + 1; \n"
        cadena += "\t stack[(int)" + newT2 + "]= " + tmp + "; \n"
        cadena += "\t P = P + 0; \n"
        cadena += "\t concatenarCadena(); \n"
        cadena += "\t " + newT6 + " = stack[(int)P]; \n"
        cadena += "\t P = P - 0; \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        fila += 8
    return cadena

def resolver_general(exp, ts, ambito):
    print(exp)
    global t_global, fila, ListaAsignacion, ListaAsignacion2, ListaAllAsignacion
    if(isinstance(exp, ExpresionNegativa)):
        tmp, c3d = resolver_general(exp.exp, ts, ambito)
        newT = t_global.varTemporal()
        c3d += "\t " + newT + " = " + str(tmp) + " * -1; \n"
        fila += 1
        return newT, c3d

    elif(isinstance(exp, ExpresionNumero)):
        return exp.val, ""

    elif(isinstance(exp, ExpresionCaracter)):
        return exp.exp, ""

    elif(isinstance(exp, ExpresionBool)):
        cadena = ""
        Ltrue = t_global.etiquetaT()
        Lfalse = t_global.etiquetaT()
        if(exp.boolean):
            cadena += "\t if (1 == 1) goto " + Ltrue + ";\n"
            cadena += "\t goto " + Lfalse + ";\n"

            #Falta Optimizacion de la fila 375 a 378

            fila += 2
        else:
            cadena += "\t if (0 == 1) goto " + Ltrue + "; \n"
            cadena += "\t goto " + Lfalse + ";\n"

            #Falta Optimizacion de la fila 386 a 389

            fila += 2
        return Ltrue, Lfalse, cadena

    elif(isinstance(exp, ExpresionBinaria)):
        tmp1, exp1 = resolver_general(exp.exp1, ts, ambito)
        tmp2, exp2 = resolver_general(exp.exp2, ts, ambito)
        if(isinstance(exp.exp1, ExpresionDobleComilla) or isinstance(exp.exp2, ExpresionDobleComilla)):
            if(exp.operador == OPERACIONES_ARITMETICAS.MULTIPLICACION):
                c3d = ""
                c3d += exp1 + exp2
                newT = t_global.varTemporal()
                c3d += "\t " + newT + " = H; \n"
                fila += 1
                if(isinstance(exp.exp1, ExpresionIdentificador)):
                    TypeV = ""
                    for var in t_global.tablaSimbolos:
                        tipo = t_global.obtenerSimbolo(var)
                        if(tipo.temp == tmp1):
                            TypeV = tipo.tipo
                    if(TypeV == TABS.TIPO_DATO.I64):
                        c3d += "\t heap[(int)H] = -2; \n"
                        c3d += "\t H = H+1; \n"
                        c3d += "\t heap[(int)H] = " + str(tmp1) + ";\n"
                        c3d += "\t H+1; \n"
                        fila += 4
                    elif(TypeV == TABS.TIPO_DATO.F64):
                        c3d += "\t heap[(int)H] = -3; \n"
                        c3d += "\t H = H+1; \n"
                        c3d += "\t heap[(int)H] = " + str(tmp1) + ";\n"
                        c3d += "\t H+1; \n"
                        fila += 4
                    elif(TypeV == TABS.TIPO_DATO.STRING):
                        newT2 = t_global.varTemporal()
                        Ltrue1 = t_global.etiquetaT()
                        Lsalto1 = t_global.etiquetaT()
                        c3d += "\t " + Lsalto1 + ": \n"
                        c3d += "\t " + newT2 + " = heap[(int)" + tmp1 + "]; \n"
                        c3d += "\t if (" + newT2 + " == -1) goto " + Ltrue1 + "; \n"
                        c3d += "\t heap[(int)H] = " + str(newT2) + "; \n"
                        c3d += "\t H = H+1; \n"
                        c3d += "\t " + tmp1 + " = " + tmp1 + "+1; \n"
                        c3d += "\t goto " + Lsalto1 + "; \n"
                        c3d += "\t " + Ltrue1 + ": \n"
                        fila += 8
                else:
                    newT2 = t_global.varTemporal()
                    Ltrue1 = t_global.etiquetaT()
                    Lsalto1 = t_global.etiquetaT()
                    c3d += "\t " + Lsalto1 + ":\n"
                    c3d += "\t " + newT2 +" = heap[(int)" + tmp1 + "]; \n"
                    c3d += "\t if (" + newT2 + " == -1) goto " + Ltrue1 + "; \n"
                    c3d += "\t heap[(int)H] = " + str(newT2) + "; \n"
                    c3d += "\t H = H+1; \n"
                    c3d += "\t " + tmp1 + " = " + tmp1 + "+1; \n"
                    c3d += "\t goto " + Lsalto1 + "; \n"
                    c3d += "\t " + Ltrue1 + ": \n"
                    fila += 8

                if(isinstance(exp.exp2, ExpresionIdentificador)):
                    TypeV = ""
                    for var in t_global.tablaSimbolos:
                        tipo = t_global.obtenerSimbolo(var)
                        if(tipo.temp == tmp2):
                            TypeV = tipo.tipo
                    if(TypeV == TABS.TIPO_DATO.I64):
                        c3d += "\t heap[(int)H] = -2; \n"
                        c3d += "\t H = H+1; \n"
                        c3d += "\t heap[(int)H] = " + str(tmp2) + ";\n"
                        c3d += "\t H+1; \n"
                        fila += 4
                    elif(TypeV == TABS.TIPO_DATO.F64):
                        c3d += "\t heap[(int)H] = -3; \n"
                        c3d += "\t H = H+1; \n"
                        c3d += "\t heap[(int)H] = " + str(tmp2) + ";\n"
                        c3d += "\t H+1; \n"
                        fila += 4
                    elif(TypeV == TABS.TIPO_DATO.STRING):
                        newT3 = t_global.varTemporal()
                        Ltrue2 = t_global.etiquetaT()
                        Lsalto2 = t_global.etiquetaT()
                        c3d += "\t " + Lsalto2 + ": \n"
                        c3d += "\t " + newT3 + " = heap[(int)" + tmp2 + "]; \n"
                        c3d += "\t if (" + newT3 + " == -1) goto " + Ltrue2 + "; \n"
                        c3d += "\t heap[(int)H] = " + str(newT3) + "; \n"
                        c3d += "\t H = H+1; \n"
                        c3d += "\t " + tmp2 + " = " + tmp2 + "+1; \n"
                        c3d += "\t goto " + Lsalto2 + "; \n"
                        c3d += "\t " + Ltrue2 + ": \n"
                        fila += 8
                else:
                    newT3 = t_global.varTemporal()
                    Ltrue2 = t_global.etiquetaT()
                    Lsalto2 = t_global.etiquetaT()
                    c3d += "\t " + Lsalto2 + ":\n"
                    c3d += "\t " + newT3 +" = heap[(int)" + tmp2 + "]; \n"
                    c3d += "\t if (" + newT3 + " == -1) goto " + Ltrue2 + "; \n"
                    c3d += "\t heap[(int)H] = " + str(newT3) + "; \n"
                    c3d += "\t H = H+1; \n"
                    c3d += "\t " + tmp2 + " = " + tmp2 + "+1; \n"
                    c3d += "\t goto " + Lsalto2 + "; \n"
                    c3d += "\t " + Ltrue2 + ": \n"
                    fila += 8

                c3d += "\t heap[(int)H] = -1; \n"
                c3d += "\t H = H+1; \n"
                fila += 2

                return newT, c3d
        if(exp.operador == OPERACIONES_ARITMETICAS.MAS):
            newT = str(t_global.varTemporal())
            c3d = exp1 + exp2 + "\t " + newT + " = " + str(tmp1) + " + " + str(tmp2) + "; \n"

            #Falta Optimizacion de 504 a 569

            fila += 1
            return newT, c3d
        if(exp.operador == OPERACIONES_ARITMETICAS.MENOS):
            newT = str(t_global.varTemporal())
            c3d = exp1 + exp2 + "\t " + newT + " = " + str(tmp1) + " - " + str(tmp2) + "; \n"

            #Falta Optimizacion de 579 a 638

            fila += 1
            return newT, c3d
        if(exp.operador == OPERACIONES_ARITMETICAS.MULTIPLICACION):
            newT = str(t_global.varTemporal())
            c3d = exp1 + exp2 + "\t " + newT + " = " + str(tmp1) + " * " + str(tmp2) + ";\n"
            fila += 1

            #Falta Optimizacion de 647 a 736

            return newT, c3d
        if(exp.operador == OPERACIONES_ARITMETICAS.DIVISION):
            newT = str(t_global.varTemporal())
            Ltrue = t_global.etiquetaT()
            Lsalto = t_global.etiquetaT()
            c3d = exp1 + exp2
            c3d += "\t if (" + str(tmp2) + " != 0) goto " + Ltrue + "; \n"
            c3d += "\t printf(\"%c\", 69); \n"
            c3d += "\t printf(\"%c\", 114); \n"
            c3d += "\t printf(\"%c\", 114); \n"
            c3d += "\t printf(\"%c\", 111); \n"
            c3d += "\t printf(\"%c\", 114); \n"
            c3d += "\t printf(\"%c\", 10); \n"
            c3d += "\t " + newT + " = 0; \n"
            c3d += "\t goto " + Lsalto + "; \n"
            c3d += "\t " + Ltrue + ": \n"
            c3d += "\t " + newT + " = " + str(tmp1) + " / " + str(tmp2) + "; \n"
            c3d += "\t " + Lsalto + ": \n"

            #Falta Optimizacion de 762 a 828

            fila += 16
            return newT, c3d
        if(exp.operador == OPERACIONES_ARITMETICAS.MODULO):
            newT = str(t_global.varTemporal())
            c3d = exp1 + exp2 + "\t " + newT + " = " + str(tmp1) + " % " + str(tmp2) + "; \n"

            #Falta Optimizacion de 504 a 569

            fila += 1
            return newT, c3d
    elif(isinstance(exp, ExpresionIdentificador)):
        valorT = ""
        valorR = ""
        pos = ""
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.nombre == exp.id):
                valorT = tipo.temp
                valorR = tipo.rol
                pos = tipo.pos
        if(valorR == "PAR"):
            cadena = ""
            newT = t_global.varTemporal()
            cadena += "\t " + newT + " = P + " + pos + "; \n"
            cadena += "\t " + valorT + " stack[(int)" + newT + "]; \n"
            fila += 2
            try:
                ListaAllAsignacion.remove(valorT)
            except:
                print()
            return valorT, cadena
        else:
            try:
                ListaAllAsignacion.remove(valorT)
            except:
                print()
            return valorT, ""
    elif(isinstance(exp, ExpresionRelacional)):
        Ltrue, Lfalse, c3d = resolver_relacional(exp, ts, ambito)
        return Ltrue, Lfalse, c3d
    elif(isinstance(exp, ExpresionLogica)):
        Ltrue, Lfalse, c3d = resolver_logica(exp, ts, ambito)
        return Ltrue, Lfalse, c3d
    elif(isinstance(exp, ExpresionDobleComilla)):
        cadena = ""
        newT = t_global.varTemporal()
        cadena += "\t " + newT + " = H; \n"
        fila += 1
        for n in exp.val:
            cadena += "\t heap[(int)H] = " + str(ord(n)) + "; \n"
            cadena += "\t H = H + 1; \n"
            fila += 2
        cadena += "\t heap[(int)H] = -1; \n"
        cadena += "\t H = H + 1; \n"
        fila += 2
        return newT, cadena

def resolver_relacional(expRel, ts, ambito):
    global fila
    if(expRel.operador != OPERACION_RELACIONAL.NOT):
        Ltrue1, Lfalse1, exp1 = resolver_general(expRel.exp1, ts, ambito)
    Ltrue2, Lfalse2, exp2 = resolver_general(expRel.exp2, ts, ambito)
    if(expRel.operador == OPERACION_RELACIONAL.AND):
        if(type(Ltrue1) == list):
            c3d = str(exp1) + "\t " + Ltrue1.pop() + ": \n" + str(exp2)
            fila += 1
        else:
            c3d = str(exp1) + "\t " + str(Ltrue1) + ": \n" + str(exp2)
            fila += 1
        ListaF = []
        ListaV = []
        if(type(Ltrue1) == list):
            for n in Ltrue1:
                ListaV.append(n)
        if(type(Ltrue2) == list):
            for n in Ltrue2:
                ListaV.append(n)
        else:
            ListaV.append(Ltrue2)
        if(type(Lfalse1) == list):
            for n in Lfalse1:
                ListaF.append(n)
        else:
            ListaF.append(Lfalse1)
        if(type(Lfalse2) == list):
            for n in Lfalse2:
                ListaF.append(n)
        else:
            ListaF.append(Lfalse2)
        return ListaV, ListaF, c3d
    elif(expRel.operador == OPERACION_RELACIONAL.OR):
        if(type(Lfalse1) == list):
            c3d = str(exp1) + "\t " + Lfalse1.pop() + ": \n" + str(exp2)
            fila += 1
        else:
            c3d = str(exp1) + "\t " + Lfalse1 + ": \n" + str(exp2)
            fila += 1
        ListaF = []
        ListaV = []
        if(type(Ltrue2) == list):
            for n in Ltrue2:
                ListaV.append(n)
        else:
            ListaV.append(Ltrue2)
        if(type(Ltrue1) == list):
            for n in Ltrue1:
                ListaV.append(n)
        else:
            ListaV.append(Ltrue1)
        if(type(Lfalse1) == list):
            for n in Lfalse1:
                ListaF.append(n)
        if(type(Lfalse2) == list):
            for n in Lfalse2:
                ListaF.append(n)
        else:
            ListaF.append(Lfalse2)
        return ListaV, ListaF, c3d
    elif(expRel.operador == OPERACION_RELACIONAL.NOT):
        if(type(Lfalse2) == list):
            c3d = str(exp2) + "\t " + Lfalse2.pop() + ": \n"
            fila += 1
        else:
            c3d = str(exp2) + "\t " + Lfalse2 + ": \n"
            fila += 1
        ListaF = []
        ListaV = []
        if(type(Ltrue2) == list):
            for n in Ltrue2:
                ListaF.append(n)
        else:
            ListaF.append(Ltrue2)
        if(type(Lfalse2) == list):
            for n in Lfalse2:
                ListaV.append(n)
        return ListaV, ListaF, c3d

def resolver_logica(expLog, ts, ambito):
    global fila
    if isinstance(expLog.exp1, ExpresionLogica):
        LV1, LF1, c3d1 = resolver_general(expLog.exp1, ts, ambito)
        LV2, LF2, c3d2 = resolver_general(expLog.exp2, ts, ambito)
        Ltrue = t_global.etiquetaT()
        Lfalse = t_global.etiquetaT()
        tmp1 = t_global.varTemporal()
        tmp2 = t_global.varTemporal()
        Lsalto1 = t_global.etiquetaT()
        Lsalto2 = t_global.etiquetaT()
        c3d = ""
        c3d = c3d1 + "\t " + LV1 + ": \n"
        c3d = "\t " + tmp1 + " = 1; \n"
        c3d = "\t goto " + Lsalto1 + "; \n"
        c3d = "\t " + LF1 + ": \n"
        c3d = "\t " + tmp1 + " = 0; \n"
        c3d = "\t " + Lsalto1 + ": \n"

        c3d += c3d2 + "\t " + LV2 + ": \n"
        c3d += "\t " + tmp2 + " = 1; \n"
        c3d += "\t goto " + Lsalto2 + "; \n"
        c3d += "\t " + LF2 + ": \n"
        c3d += "\t " + tmp2 + "; \n"
        c3d += "\t " + Lsalto2 + ": \n"
        exp1 = ""
        exp2 = ""
        fila += 12
    else:
        tmp1, exp1 = resolver_general(expLog.exp1, ts, ambito)
        tmp2, exp2 = resolver_general(expLog.exp2, ts, ambito)
    if(expLog.operador == OPERACION_LOGICA.MAYORQUE):
        Ltrue = t_global.etiquetaT()
        Lfalse = t_global.etiquetaT()
        c3d = exp1 + exp2 + "\t if (" + str(tmp1) + " > " + str(tmp2) + ") goto " + str(Ltrue) + "; \n\t goto " + str(Lfalse) + "; \n"

        #Falta Optimizacion 1081 a 1085

        fila += 2
        return Ltrue, Lfalse, c3d
    elif(expLog.operador == OPERACION_LOGICA.MENORQUE):
        Ltrue = t_global.etiquetaT()
        Lfalse = t_global.etiquetaT()
        c3d = exp1 + exp2 + "\t if (" + str(tmp1) + " < " + str(tmp2) + ") goto " + str(Ltrue) + "; \n\t goto " + str(Lfalse) + "; \n"

        #Falta Optimizacion 1094 a 1098

        fila += 2
        return Ltrue, Lfalse, c3d
    elif(expLog.operador == OPERACION_LOGICA.IGUALIGUAL):
        Ltrue = t_global.etiquetaT()
        Lfalse = t_global.etiquetaT()
        c3d = exp1 + exp2 + "\t if (" + str(tmp1) + " == " + str(tmp2) + ") goto " + str(Ltrue) + "; \n\t goto " + str(Lfalse) + "; \n"

        #Falta Optimizacion 1108 a 1111

        fila += 2
        return Ltrue, Lfalse, c3d
    elif(expLog.operador == OPERACION_LOGICA.NOIGUAL):
        Ltrue = t_global.etiquetaT()
        Lfalse = t_global.etiquetaT()
        c3d = exp1 + exp2 + "\t if (" + str(tmp1) + " != " + str(tmp2) + ") goto " + str(Ltrue) + "; \n\t goto " + str(Lfalse) + "; \n"

        #Falta Optimizacion 1121 a 1124

        fila += 2
        return Ltrue, Lfalse, c3d
    elif(expLog.operador == OPERACION_LOGICA.MAYORIGUAL):
        Ltrue = t_global.etiquetaT()
        Lfalse = t_global.etiquetaT()
        c3d = exp1 + exp2 + "\t if (" + str(tmp1) + " >= " + str(tmp2) + ") goto " + str(Ltrue) + "; \n\t goto " + str(Lfalse) + "; \n"

        #Falta Optimizacion 1134 a 1137

        fila += 2
        return Ltrue, Lfalse, c3d
    elif(expLog.operador == OPERACION_LOGICA.MENORIGUAL):
        Ltrue = t_global.etiquetaT()
        Lfalse = t_global.etiquetaT()
        c3d = exp1 + exp2 + "\t if (" + str(tmp1) + " <= " + str(tmp2) + ") goto " + str(Ltrue) + "; \n\t goto " + str(Lfalse) + "; \n"

        #Falta Optimizacion 1147 a 1150

        fila += 2
        return Ltrue, Lfalse, c3d

def instruccion_if(expIf, ts, ambito):
    global t_global, fila
    cadena = ""
    LS = []
    print(expIf.expLogica)
    LV, LF, c3d = resolver_general(expIf.expLogica, ts, "if_" + ambito)
    newL1 = t_global.etiquetaT()
    LS.append(newL1)
    cadena += c3d
    if(type(LV) != list):
        cadena += "\t " + LV + ": \n"
        fila += 1
    else:
        for n in LV:
            cadena += "\t " + n + ": \n"
            fila += 1
    
    cadena += procesar_instrucciones(expIf.instrucciones, ts, "if_" + ambito)
    cadena += "\t goto " + newL1 + "; \n"
    fila += 1
    if(type(LF) == list):
        for n in LF:
            cadena += "\t " + n + ": \n"
            fila += 1
    else:
        cadena += "\t " + LF + ": \n"
        fila += 1

    for n in LS:
        cadena += "\t " + n + ": \n"
        fila += 1
    return cadena

def instruccion_elseif(expElseif, ts, ambito):
    global t_global, fila
    cadena = ""
    LS = []
    LV, LF, c3d = resolver_general(expElseif.expLogica, ts, "if_" + ambito)
    newL1 = t_global.etiquetaT()
    LS.append(newL1)
    cadena += c3d
    if(type(LV) != list):
        cadena += "\t " + LV + ": \n"
        fila += 1
    else:
        for n in LV:
            cadena += "\t " + n + ": \n"
            fila += 1
    
    cadena += procesar_instrucciones(expElseif.instrucciones, ts, "if_" + ambito)
    cadena += "\t goto " + newL1 + "; \n"
    fila += 1
    if(type(LF) == list):
        for n in LF:
            cadena += "\t " + n + ": \n"
            fila += 1
    else:
        cadena += "\t " + LF + ": \n"
        fila += 1
    for listaif in expElseif.listaElseif:
        if(isinstance(listaif, IF)):
            LV2, LF2, c3d2 = resolver_general(listaif.expLogica, ts, "if_" + ambito)
            newL2 = t_global.etiquetaT()
            LS.append(newL2)
            cadena += c3d2
            if(type(LV2) != list):
                cadena += "\t " + LV2 + ": \n"
                fila += 1
            else:
                for n in LV2:
                    cadena += "\t " + n + "\n"
                    fila += 1
            cadena += procesar_instrucciones(listaif.instrucciones, ts, "if_" + ambito)
            cadena += "\t goto " + newL2 + ";\n"
            fila += 1
            if(type(LF2) == list):
                for n in LF2:
                    cadena += "\t " + n + ": \n"
                    fila += 1
            else:
                cadena += "\t " + LF2 + ": \n"
                fila += 1
        elif(isinstance(listaif, ELSE)):
            cadena += procesar_instrucciones(listaif.instrucciones, ts, "if_" + ambito)
    for n in LS:
        cadena += "\t " + n + ": \n"
        fila += 1
    return cadena

def instruccion_asignacion_mut(asignacion, ts, ambito):
    global t_global, fila, ListaAsignacion, ListaAsignacion2
    cadena = ""
    if(isinstance(asignacion.exp, ExpresionRelacional)):
        newT = t_global.varTemporal()
        LV, LF, c3d = resolver_general(asignacion.exp, ts, ambito)
        cadena += c3d
        if(type(LV) != list):
            cadena += "\t " + LV + ": \n"
            fila += 1
        else:
            for n in LV:
                cadena += "\t " + n + ": \n"
                fila += 1
        cadena += "\t " + newT + " = H; \n"
        cadena += "\t heap[(int)H] = 116; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 114; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 117; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 101; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = -1; \n"
        cadena += "\t H = H + 1; \n"
        fila += 11
        if(type(LF) != list):
            cadena += "\t " + LF + ": \n"
            fila += 1
        else:
            for n in LF:
                cadena += "\t " + n + ": \n"
                fila += 1
        cadena += "\t " + newT + " = H; \n"
        cadena += "\t heap[(int)H] = 102; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 97; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 108; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 115; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 101; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = -1; \n"
        cadena += "\t H = H + 1; \n"
        fila += 13
        variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, True)
        t_global.agregarSimbolo(variable)
    else:
        comprobar = False
        valorT = ""
        valorR = ""
        pos = ""
        tmp, c3d = resolver_general(asignacion.exp, ts, ambito)
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.nombre == asignacion.id):
                valorT = tipo.temp
                valorR = tipo.rol
                pos = tipo.pos
                comprobar = True
        if(comprobar):
            cadena += c3d
            if(valorR == "PAR"):
                newT = t_global.varTemporal()
                cadena += "\t " + newT + " = P +" + pos + "; \n"
                cadena += "\t stack[(int)" + newT + "] = " + str(tmp) + "; \n"
                fila += 2
            else:
                newT = t_global.varTemporal()
                listaAux = []
                for n in ListaAsignacion:
                    if(n.id != valorT):
                        listaAux.append(n)
                ListaAsignacion = listaAux

                listaAux = []
                for n in ListaAsignacion2:
                    if(n.id != valorT):
                        listaAux.append(n)
                ListaAsignacion2 = listaAux

                #Falta Optimizacion de 1244 a 1245

                if(isinstance(tmp, str)):
                    if(len(tmp) == 1):
                        cadena += "\t " + valorT + " = " + str(ord(tmp)) + "; \n"
                        fila += 1
                    else:
                        cadena += "\t " + valorT + " = " + str(tmp) + "; \n"
                        fila += 1
                else:
                    cadena += "\t " + valorT + " = " + str(tmp) + "; \n"
                    fila += 1
        else:
            newT = t_global.varTemporal()
            print("-----" + newT + "------")
            if(isinstance(asignacion.exp, ExpresionDobleComilla)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, True)

                #Falta Optimizacion de 1257 a 1259

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionNumero)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.I64, True)
                                
                #Falta Optimizacion de 1268 a 1270

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionCaracter)):
                cadena += c3d + "\t " + newT + " = " + str(ord(tmp)) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.CHAR, True)

                #Falta Optimizacion de 1257 a 1259

                fila += 1
                t_global.agregarSimbolo(variable)
            else:
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, "", True)
                                
                #Falta Optimizacion de 1279 a 1281

                fila += 1
                t_global.agregarSimbolo(variable)
    return cadena

def instruccion_asignacion_mut_tipo(asignacion, ts, ambito):
    global t_global, fila, ListaAsignacion, ListaAsignacion2
    cadena = ""
    if(isinstance(asignacion.exp, ExpresionRelacional)):
        newT = t_global.varTemporal()
        LV, LF, c3d = resolver_general(asignacion.exp, ts, ambito)
        cadena += c3d
        if(type(LV) != list):
            cadena += "\t " + LV + ": \n"
            fila += 1
        else:
            for n in LV:
                cadena += "\t " + n + ": \n"
                fila += 1
        cadena += "\t " + newT + " = H; \n"
        cadena += "\t heap[(int)H] = 116; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 114; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 117; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 101; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = -1; \n"
        cadena += "\t H = H + 1; \n"
        fila += 11
        if(type(LF) != list):
            cadena += "\t " + LF + ": \n"
            fila += 1
        else:
            for n in LF:
                cadena += "\t " + n + ": \n"
                fila += 1
        cadena += "\t " + newT + " = H; \n"
        cadena += "\t heap[(int)H] = 102; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 97; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 108; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 115; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 101; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = -1; \n"
        cadena += "\t H = H + 1; \n"
        fila += 13
        variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, True)
        t_global.agregarSimbolo(variable)
    else:
        comprobar = False
        valorT = ""
        valorR = ""
        pos = ""
        tmp, c3d = resolver_general(asignacion.exp, ts, ambito)
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.nombre == asignacion.id):
                valorT = tipo.temp
                valorR = tipo.rol
                pos = tipo.pos
                comprobar = True
        if(comprobar):
            cadena += c3d
            if(valorR == "PAR"):
                newT = t_global.varTemporal()
                cadena += "\t " + newT + " = P +" + pos + "; \n"
                cadena += "\t stack[(int)" + newT + "] = " + str(tmp) + "; \n"
                fila += 2
            else:
                newT = t_global.varTemporal()
                listaAux = []
                for n in ListaAsignacion:
                    if(n.id != valorT):
                        listaAux.append(n)
                ListaAsignacion = listaAux

                listaAux = []
                for n in ListaAsignacion2:
                    if(n.id != valorT):
                        listaAux.append(n)
                ListaAsignacion2 = listaAux

                #Falta Optimizacion de 1244 a 1245

                if(isinstance(tmp, str)):
                    if(len(tmp) == 1):
                        cadena += "\t " + valorT + " = " + str(ord(tmp)) + "; \n"
                        fila += 1
                    else:
                        cadena += "\t " + valorT + " = " + str(tmp) + "; \n"
                        fila += 1
                else:
                    cadena += "\t " + valorT + " = " + str(tmp) + "; \n"
                    fila += 1
        else:
            newT = t_global.varTemporal()
            print("-----" + newT + "------")
            if(isinstance(asignacion.exp, ExpresionDobleComilla)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, True)

                #Falta Optimizacion de 1257 a 1259

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionNumero)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.I64, True)
                                
                #Falta Optimizacion de 1268 a 1270

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionCaracter)):
                cadena += c3d + "\t " + newT + " = " + str(ord(tmp)) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.CHAR, True)

                #Falta Optimizacion de 1257 a 1259

                fila += 1
                t_global.agregarSimbolo(variable)
            else:
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, "", True)
                                
                #Falta Optimizacion de 1279 a 1281

                fila += 1
                t_global.agregarSimbolo(variable)
    return cadena

def instruccion_asignacion_no_mut(asignacion, ts, ambito):
    global t_global, fila, ListaAsignacion, ListaAsignacion2
    cadena = ""
    if(isinstance(asignacion.exp, ExpresionRelacional)):
        newT = t_global.varTemporal()
        LV, LF, c3d = resolver_general(asignacion.exp, ts, ambito)
        cadena += c3d
        if(type(LV) != list):
            cadena += "\t " + LV + ": \n"
            fila += 1
        else:
            for n in LV:
                cadena += "\t " + n + ": \n"
                fila += 1
        cadena += "\t " + newT + " = H; \n"
        cadena += "\t heap[(int)H] = 116; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 114; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 117; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 101; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = -1; \n"
        cadena += "\t H = H + 1; \n"
        fila += 11
        if(type(LF) != list):
            cadena += "\t " + LF + ": \n"
            fila += 1
        else:
            for n in LF:
                cadena += "\t " + n + ": \n"
                fila += 1
        cadena += "\t " + newT + " = H; \n"
        cadena += "\t heap[(int)H] = 102; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 97; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 108; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 115; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 101; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = -1; \n"
        cadena += "\t H = H + 1; \n"
        fila += 13
        variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, False)
        t_global.agregarSimbolo(variable)
    else:
        comprobar = False
        valorT = ""
        valorR = ""
        pos = ""
        tmp, c3d = resolver_general(asignacion.exp, ts, ambito)
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.nombre == asignacion.id):
                valorT = tipo.temp
                valorR = tipo.rol
                pos = tipo.pos
                comprobar = True
        if(comprobar):
            cadena += c3d
            if(valorR == "PAR"):
                newT = t_global.varTemporal()
                cadena += "\t " + newT + " = P +" + pos + "; \n"
                cadena += "\t stack[(int)" + newT + "] = " + str(tmp) + "; \n"
                fila += 2
            else:
                newT = t_global.varTemporal()
                listaAux = []
                for n in ListaAsignacion:
                    if(n.id != valorT):
                        listaAux.append(n)
                ListaAsignacion = listaAux

                listaAux = []
                for n in ListaAsignacion2:
                    if(n.id != valorT):
                        listaAux.append(n)
                ListaAsignacion2 = listaAux

                #Falta Optimizacion de 1244 a 1245

                if(isinstance(tmp, str)):
                    if(len(tmp) == 1):
                        cadena += "\t " + valorT + " = " + str(ord(tmp)) + "; \n"
                        fila += 1
                    else:
                        cadena += "\t " + valorT + " = " + str(tmp) + "; \n"
                        fila += 1
                else:
                    cadena += "\t " + valorT + " = " + str(tmp) + "; \n"
                    fila += 1
        else:
            newT = t_global.varTemporal()
            print("-----" + newT + "------")
            if(isinstance(asignacion.exp, ExpresionDobleComilla)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, False)

                #Falta Optimizacion de 1257 a 1259

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionNumero)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.I64, False)
                                
                #Falta Optimizacion de 1268 a 1270

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionCaracter)):
                cadena += c3d + "\t " + newT + " = " + str(ord(tmp)) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.CHAR, False)

                #Falta Optimizacion de 1257 a 1259

                fila += 1
                t_global.agregarSimbolo(variable)
            else:
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, "", False)
                                
                #Falta Optimizacion de 1279 a 1281

                fila += 1
                t_global.agregarSimbolo(variable)
    return cadena

def instruccion_asignacion_no_mut_tipo(asignacion, ts, ambito):
    global t_global, fila, ListaAsignacion, ListaAsignacion2
    cadena = ""
    if(isinstance(asignacion.exp, ExpresionRelacional)):
        newT = t_global.varTemporal()
        LV, LF, c3d = resolver_general(asignacion.exp, ts, ambito)
        cadena += c3d
        if(type(LV) != list):
            cadena += "\t " + LV + ": \n"
            fila += 1
        else:
            for n in LV:
                cadena += "\t " + n + ": \n"
                fila += 1
        cadena += "\t " + newT + " = H; \n"
        cadena += "\t heap[(int)H] = 116; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 114; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 117; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 101; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = -1; \n"
        cadena += "\t H = H + 1; \n"
        fila += 11
        if(type(LF) != list):
            cadena += "\t " + LF + ": \n"
            fila += 1
        else:
            for n in LF:
                cadena += "\t " + n + ": \n"
                fila += 1
        cadena += "\t " + newT + " = H; \n"
        cadena += "\t heap[(int)H] = 102; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 97; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 108; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 115; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 101; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = -1; \n"
        cadena += "\t H = H + 1; \n"
        fila += 13
        variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, False)
        t_global.agregarSimbolo(variable)
    else:
        comprobar = False
        valorT = ""
        valorR = ""
        pos = ""
        tmp, c3d = resolver_general(asignacion.exp, ts, ambito)
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.nombre == asignacion.id):
                valorT = tipo.temp
                valorR = tipo.rol
                pos = tipo.pos
                comprobar = True
        if(comprobar):
            cadena += c3d
            if(valorR == "PAR"):
                newT = t_global.varTemporal()
                cadena += "\t " + newT + " = P +" + pos + "; \n"
                cadena += "\t stack[(int)" + newT + "] = " + str(tmp) + "; \n"
                fila += 2
            else:
                newT = t_global.varTemporal()
                listaAux = []
                for n in ListaAsignacion:
                    if(n.id != valorT):
                        listaAux.append(n)
                ListaAsignacion = listaAux

                listaAux = []
                for n in ListaAsignacion2:
                    if(n.id != valorT):
                        listaAux.append(n)
                ListaAsignacion2 = listaAux

                #Falta Optimizacion de 1244 a 1245

                if(isinstance(tmp, str)):
                    if(len(tmp) == 1):
                        cadena += "\t " + valorT + " = " + str(ord(tmp)) + "; \n"
                        fila += 1
                    else:
                        cadena += "\t " + valorT + " = " + str(tmp) + "; \n"
                        fila += 1
                else:
                    cadena += "\t " + valorT + " = " + str(tmp) + "; \n"
                    fila += 1
        else:
            newT = t_global.varTemporal()
            print("-----" + newT + "------")
            if(isinstance(asignacion.exp, ExpresionDobleComilla)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, False)

                #Falta Optimizacion de 1257 a 1259

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionNumero)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.I64, False)
                                
                #Falta Optimizacion de 1268 a 1270

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionCaracter)):
                cadena += c3d + "\t " + newT + " = " + str(ord(tmp)) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.CHAR, False)

                #Falta Optimizacion de 1257 a 1259

                fila += 1
                t_global.agregarSimbolo(variable)
            else:
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, "", False)
                                
                #Falta Optimizacion de 1279 a 1281

                fila += 1
                t_global.agregarSimbolo(variable)
    return cadena

def instruccion_asignacion_nuevo_valor(asignacion, ts, ambito):
    global t_global, fila, ListaAsignacion, ListaAsignacion2
    cadena = ""
    if(isinstance(asignacion.exp, ExpresionRelacional)):
        newT = t_global.varTemporal()
        LV, LF, c3d = resolver_general(asignacion.exp, ts, ambito)
        cadena += c3d
        if(type(LV) != list):
            cadena += "\t " + LV + ": \n"
            fila += 1
        else:
            for n in LV:
                cadena += "\t " + n + ": \n"
                fila += 1
        cadena += "\t " + newT + " = H; \n"
        cadena += "\t heap[(int)H] = 116; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 114; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 117; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 101; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = -1; \n"
        cadena += "\t H = H + 1; \n"
        fila += 11
        if(type(LF) != list):
            cadena += "\t " + LF + ": \n"
            fila += 1
        else:
            for n in LF:
                cadena += "\t " + n + ": \n"
                fila += 1
        cadena += "\t " + newT + " = H; \n"
        cadena += "\t heap[(int)H] = 102; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 97; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 108; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 115; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = 101; \n"
        cadena += "\t H = H + 1; \n"
        cadena += "\t heap[(int)H] = -1; \n"
        cadena += "\t H = H + 1; \n"
        fila += 13
        variable = T.tipoSimbolo(newT, asignacion.id, 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, False)
        t_global.agregarSimbolo(variable)
    else:
        comprobar = False
        valorT = ""
        valorR = ""
        valorM = False
        pos = ""
        tmp, c3d = resolver_general(asignacion.exp, ts, ambito)
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.nombre == asignacion.id):
                valorT = tipo.temp
                valorR = tipo.rol
                pos = tipo.pos
                valorM = tipo.mutable
                comprobar = True
        if(comprobar):
            if(valorM == True):
                cadena += c3d
                if(valorR == "PAR"):
                    newT = t_global.varTemporal()
                    cadena += "\t " + newT + " = P +" + pos + "; \n"
                    cadena += "\t stack[(int)" + newT + "] = " + str(tmp) + "; \n"
                    fila += 2
                else:
                    newT = t_global.varTemporal()
                    listaAux = []
                    for n in ListaAsignacion:
                        if(n.id != valorT):
                            listaAux.append(n)
                    ListaAsignacion = listaAux

                    listaAux = []
                    for n in ListaAsignacion2:
                        if(n.id != valorT):
                            listaAux.append(n)
                    ListaAsignacion2 = listaAux

                    #Falta Optimizacion de 1244 a 1245

                    if(isinstance(tmp, str)):
                        if(len(tmp) == 1):
                            cadena += "\t " + valorT + " = " + str(ord(tmp)) + "; \n"
                            fila += 1
                        else:
                            cadena += "\t " + valorT + " = " + str(tmp) + "; \n"
                            fila += 1
                    else:
                        cadena += "\t " + valorT + " = " + str(tmp) + "; \n"
                        fila += 1
            else:
                print("La variable no es mutable")
    return cadena

def instruccion_ciclo_while(instruccion, ts, ambito):
    global t_global, existe_continue, existe_break, Lista_Break, Lista_Continue, fila
    cadena = ""
    LV, LF, c3d = resolver_general(instruccion.exp, ts, "while_" + ambito)
    cadena += c3d
    if(type(LV) != list):
        cadena += "\t " + LV + ": \n"
        fila += 1
    else:
        for n in LV:
            cadena += "\t " + n + ": \n"
            fila += 1
    cadena += procesar_instrucciones(instruccion.instrucciones, ts, "while_" + ambito)
    newL = t_global.etiquetaT()
    cadena = "\t " + newL + ": \n" + cadena
    fila += 1
    if(existe_continue):
        cadena += "\t " + Lista_Continue + ": \n"
        fila += 1
        existe_continue = False
    cadena += "\t goto " + newL + "; \n"
    fila += 1
    if(type(LF) == list):
        for n in LF:
            cadena += "\t " + n + ": \n"
            fila += 1
    else:
        cadena += "\t " + LF + ": \n"
        fila += 1
    if(existe_break):
        cadena += "\t " + Lista_Break + ": \n"
        fila += 1
        existe_break = False
    return cadena

def procesar_instrucciones(instrucciones, ts, ambito):
    global existe_break, existe_continue, Lista_Break, Lista_Continue, t_global, fila
    cadena = ""
    for instruccion in instrucciones:
        if(isinstance(instruccion, Print)):
            cadena += instruccion_print(instruccion, ts, ambito)
        elif(isinstance(instruccion, Println)):
            cadena += instruccion_println(instruccion, ts, ambito)
        elif(isinstance(instruccion, IF)):
            cadena += instruccion_if(instruccion, ts, ambito)
        elif(isinstance(instruccion, IfElseIf)):
            cadena += instruccion_elseif(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionMutable)):
            cadena += instruccion_asignacion_mut(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionMutableTipo)):
            cadena += instruccion_asignacion_mut_tipo(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionNoMutable)):
            cadena += instruccion_asignacion_no_mut(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionNoMutableTipo)):
            cadena += instruccion_asignacion_no_mut_tipo(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionNuevoValor)):
            cadena += instruccion_asignacion_nuevo_valor(instruccion, ts, ambito)
        elif(isinstance(instruccion, CicloWhile)):
            cadena += instruccion_ciclo_while(instruccion, ts, ambito)

        elif(isinstance(instruccion, InstruccionReturn)):
            tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
            cadena += c3d + "\t stack[(int) P] = " + str(tmp) + "; \n"
            Lsalto = t_global.etiquetaT()
            cadena += "\t goto " + Lsalto + "; \n"
            Lista_return.append(Lsalto)
            fila += 2
        elif(isinstance(instruccion, ExisteBreak)):
            tmp = t_global.etiquetaT()
            Lista_Break = tmp
            existe_break = True
            cadena += "\t goto " + str(tmp) + "; \n"
            fila += 1
        elif(isinstance(instruccion, ExisteContinue)):
            tmp = t_global.etiquetaT()
            Lista_Continue = tmp
            existe_continue = True
            cadena += "\t goto " + str(tmp) + "; \n"
            fila += 1
    return cadena

def datosC3D(inputs):
    global mensaje, t_global, ListaAllAsignacion, ListaAsignacion, ListaAsignacion2, fila, LFunciones, cadenafuncion
    LFunciones = []
    cadenafuncion = ""
    ts_global = TABS.TablaSimbolos()
    instrucciones = g.parse(inputs)
    mensaje = ""
    mensajeaux = procesar_instrucciones(instrucciones, ts_global, "Global")
    Ntmp = t_global.obtenerT()

    aux = 0
    cad = "float "
    com = False
    while(aux < Ntmp):
        com = True
        cad += "t"+str(aux)
        aux += 1
        if(aux < Ntmp):
            cad += ","
    cad += ";\n"

    mensaje += "#include <stdio.h> \n"
    mensaje += "float stack[10000]; \n"
    mensaje += "float heap[10000]; \n"
    mensaje += "float P; \n"
    mensaje += "float H; \n"

    if(com):
        mensaje += cad

    mensaje += "\n" + cadenafuncion + "\n"
    mensaje += "int main(){ \n"
    mensaje += mensajeaux
    mensaje += "\t return 0; \n"
    mensaje += "}"

    t_global.limpiar()
    return mensaje