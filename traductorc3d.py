import tab_simbolos as TABS
import gramatica as g
from expresiones import  *
from instrucciones import *
import temporal as T
import optimizacion as OP

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
    elif(isinstance(instruccion.exp, ExpresionBool)):
        if(instruccion.exp.boolean == True):
            tmp = 1
            c3d = ""
        else:
            tmp = 0
            c3d = ""
        cadena = c3d + "\t printf(\"%d\", (int)" + str(tmp) +"); \n"
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
    elif(isinstance(instruccion.exp, ExpresionIdentificador) and (tipos == TABS.TIPO_DATO.CHAR or tipos == "char")):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%c\", (int)" + str(tmp) + "); \n"
        fila += 1
    elif(isinstance(instruccion.exp, ExpresionIdentificador) and (tipos == TABS.TIPO_DATO.I64 or tipos == "i64")):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%d\", (int)" + str(tmp) +"); \n"
        fila += 1
    elif(isinstance(instruccion.exp, ExpresionIdentificador) and (tipos == TABS.TIPO_DATO.F64 or tipos == "f64")):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%f\", " + str(tmp) +"); \n"
        fila += 1
    elif(isinstance(instruccion.exp, ExpresionIdentificador) and (tipos == TABS.TIPO_DATO.BOOL or tipos == "bool")):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%f\"," + str(tmp) + "); \n"
        fila += 1

    elif(isinstance(instruccion.exp, ExpresionIdentificador) and (tipos == "Binaria")):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%f\"," + str(tmp) + "); \n"
        fila += 1

    #elif(isinstance(instruccion.exp, ExpresionIdentificador) and tipos != TABS.TIPO_DATO.STRING):
    #    tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
    #    cadena = c3d + "\t printf(\"%f\"," + str(tmp) + "); \n"
    #    fila += 1

    elif(isinstance(instruccion.exp, ExpresionIdentificador) and tipos == "Arreglo"):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d
        newT = t_global.varTemporal()
        newV = t_global.varTemporal()
        Ltrue = t_global.etiquetaT()
        Lsalto = t_global.etiquetaT()

        cadena += "\t " + newV + " = " + str(tmp) + "; \n"
        cadena += "\t printf(\"%c\", (int)91); \n"
        cadena += "\t " + newT + " = heap[(int)" + newV + "]; \n"
        cadena += "\t printf(\"%d\", (int)" + newT + "); \n"
        cadena += "\t " + Lsalto + ": \n"
        cadena += "\t " + newV + " = " + newV + " + 1; \n"
        cadena += "\t " + newT + " = heap[(int)" + newV + "]; \n"
        cadena += "\t if(" + newT + " == -1) goto " + Ltrue + "; \n"
        cadena += "\t printf(\"%c\", (int)44); \n"
        cadena += "\t printf(\"%d\", (int)" + newT + "); \n"
        cadena += "\t goto " + Lsalto + "; \n"
        cadena += "\t " + Ltrue + ": \n"
        cadena += "\t printf(\"%c\", (int)93); \n"
        fila += 11

    elif(isinstance(instruccion.exp, LlamadaFuncion)):
        tmp, c3d = instruccion_llamada_funcion(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%f\", " + str(tmp) + "); \n"
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

    print(".........")
    print(tipos)
    if(isinstance(instruccion.exp, ExpresionBinaria) and not isinstance(instruccion.exp.exp1, ExpresionDobleComilla) and not isinstance(instruccion.exp.exp2, ExpresionDobleComilla) and comprobar):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%f\", " + str(tmp) +"); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        fila += 2
    elif(isinstance(instruccion.exp, ExpresionBool)):
        if(instruccion.exp.boolean == True):
            tmp = 1
            c3d = ""
        else:
            tmp = 0
            c3d = ""
        cadena = c3d + "\t printf(\"%d\", (int)" + str(tmp) +"); \n"
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
    elif(isinstance(instruccion.exp, ExpresionIdentificador) and (tipos == TABS.TIPO_DATO.CHAR or tipos == "char")):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%c\", (int)" + str(tmp) + "); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        fila += 2

    #Falta una instancia de tipo list

    elif(isinstance(instruccion.exp, ExpresionIdentificador) and (tipos == TABS.TIPO_DATO.I64 or tipos == "i64")):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%d\", (int)" + str(tmp) +"); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        fila += 2

    elif(isinstance(instruccion.exp, ExpresionIdentificador) and (tipos == TABS.TIPO_DATO.F64 or tipos == "f64")):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%f\", " + str(tmp) +"); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        fila += 2

    elif(isinstance(instruccion.exp, ExpresionIdentificador) and (tipos == TABS.TIPO_DATO.BOOL or tipos == "bool")):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%f\"," + str(tmp) + "); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        fila += 2

    elif(isinstance(instruccion.exp, ExpresionIdentificador) and (tipos == "Binaria")):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%f\"," + str(tmp) + "); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        fila += 2

    #elif(isinstance(instruccion.exp, ExpresionIdentificador) and tipos != TABS.TIPO_DATO.STRING):
    #    print("Hoooola")
    #    tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
    #    cadena = c3d + "\t printf(\"%f\"," + str(tmp) + "); \n"
    #    cadena += "\t printf(\"%c\", (int)10); \n"
    #    fila += 2

    #Este de abajo es el correcto

    elif(isinstance(instruccion.exp, ExpresionIdentificador) and tipos == "Arreglo"):
        tmp, c3d = resolver_general(instruccion.exp, ts, ambito)
        cadena = c3d
        newT = t_global.varTemporal()
        newV = t_global.varTemporal()
        Ltrue = t_global.etiquetaT()
        Lsalto = t_global.etiquetaT()

        cadena += "\t " + newV + " = " + str(tmp) + "; \n"
        cadena += "\t printf(\"%c\", (int)91); \n"
        cadena += "\t " + newT + " = heap[(int)" + newV + "]; \n"
        cadena += "\t printf(\"%d\", (int)" + newT + "); \n"
        cadena += "\t " + Lsalto + ": \n"
        cadena += "\t " + newV + " = " + newV + " + 1; \n"
        cadena += "\t " + newT + " = heap[(int)" + newV + "]; \n"
        cadena += "\t if(" + newT + " == -1) goto " + Ltrue + "; \n"
        cadena += "\t printf(\"%c\", (int)44); \n"
        cadena += "\t printf(\"%d\", (int)" + newT + "); \n"
        cadena += "\t goto " + Lsalto + "; \n"
        cadena += "\t " + Ltrue + ": \n"
        cadena += "\t printf(\"%c\", (int)93); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"

        fila += 12

    elif(isinstance(instruccion.exp, LlamadaFuncion)):
        tmp, c3d = instruccion_llamada_funcion(instruccion.exp, ts, ambito)
        cadena = c3d + "\t printf(\"%f\", " + str(tmp) + "); \n"
        cadena += "\t printf(\"%c\", (int)10); \n"
        fila += 2

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
            fila += 2
        else:
            cadena += "\t if (0 == 1) goto " + Ltrue + "; \n"
            cadena += "\t goto " + Lfalse + ";\n"
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

            #Optimizacion
            comprobar = False
            for n in ListaAsignacion:
                if(n.op == "+"):
                    if(n.exp1 == str(tmp1) and n.exp2 == str(tmp2)):
                        comprobar = True
                        #Optimizacion
                        Original = newT + " = " + str(tmp1) + " + " + str(tmp2) + ";"
                        Opti = newT + " = " + n.id + ";"
                        R = OP.Optimizacion("Bloque", "Subexpresiones comunes <br/>Regla 1", Original, Opti, fila)
                        OP.agregarOp(R)

            if(not comprobar):
                A = OP.Asignacion(newT, "+", str(tmp1), str(tmp2))
                ListaAsignacion.append(A)

            #Optimizacion 
            for n in ListaAsignacion2:
                if(n.id == str(tmp1)):
                    try:
                        ListaAllAsignacion.remove(tmp1)
                    except:
                        print()
                    #Optimizacion 2
                    if(n.tipo == 1):
                        #Optimizacion 
                        Original = newT + " = " + str(tmp1) + " + " + str(tmp2) + ";"
                        Opti = newT + " = " + str(n.exp) + " + " + str(tmp2) + ";"
                        R = OP.Optimizacion("Bloque", "Propagacion de copias Regla 2", Original, Opti, fila)
                        OP.agregarOp(R)

                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = " + str(tmp1) + " + " + str(tmp2) + ";"
                        Opti2 = newT + " = " + str(n.exp) + " + " + str(tmp2) + ";"
                        R2 = OP.Optimizacion("Bloque", "Eliminacion de codigo muerto Regla 3", Original2, Opti2, fila)
                        OP.agregarOp(R2)
                    else:
                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = " + str(tmp2) + ";"
                        Opti2 = newT + " = " +str(n.exp) + " + " + str(tmp2) + ";"
                        R2 = OP.Optimizacion("Bloque", "Propagacion de constantes Regla 4", Original2, Opti2, fila)
                        OP.agregarOp(R2)
                elif(n.id == str(tmp2)):
                    #Optimizacion 2
                    if(n.tipo == 1):
                        #Optimizacion
                        Original = newT + " = " + str(tmp1) + " + " + str(tmp2) + ";"
                        Opti = newT + " = " + str(tmp1) + " + " + str(n.exp) + ";"
                        R = OP.Optimizacion("Bloque", "Propagacion de copias Regla 2", Original, Opti, fila)
                        OP.agregarOp(R)

                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = " + str(tmp1) + " + " + str(tmp2) + ";"
                        Opti2 = newT + " = " + str(tmp1) + " + " + str(n.exp) + ";"
                        R2 = OP.Optimizacion("Bloque", "Eliminacion de codigo muerto Regla 3", Original2, Opti2, fila)
                        OP.agregarOp(R2)
                    else:
                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = " + str(tmp1) + " + " + str(tmp2) + ";"
                        Opti2 = newT + " = " + str(tmp1) + " + " + str(n.exp) + ";"
                        R2 = OP.Optimizacion("Bloque", "Propagacion de constantes Regla 4", Original2, Opti2, fila)
                        OP.agregarOp(R2)
            fila += 1
            return newT, c3d
        if(exp.operador == OPERACIONES_ARITMETICAS.MENOS):
            newT = str(t_global.varTemporal())
            c3d = exp1 + exp2 + "\t " + newT + " = " + str(tmp1) + " - " + str(tmp2) + "; \n"

            #Optimizacion
            comprobar = False
            for n in ListaAsignacion:
                if (n.op == "-"):
                    if (n.exp1 == str(tmp1) and n.exp2 == str(tmp2)):
                        comprobar = True
                        #Optimizacion
                        Original = "\t "+ newT + " = " + str(tmp1)+ " - " + str(tmp2) + ";\n"
                        Opti = "\t  " + newT + " = " + n.id + ";\n"
                        R = OP.Optimizacion("Bloque", "Subexpresiones comunes Regla 1", Original, Opti, fila)
                        OP.agregarOp(R)

            if (not comprobar):
                A = OP.Asignacion(newT, "-", str(tmp1), str(tmp2))
                ListaAsignacion.append(A) 

            #Optimizacion
            for n in ListaAsignacion2:
                if (n.id == str(tmp1)):
                    #Optimizacion 2
                    if (n.tipo == 1):
                        #Optimizacion
                        Original = newT + " = " + str(tmp1)+ " - " + str(tmp2) + ";"
                        Opti = newT + " = " + str(n.exp) + " - " + str(tmp2) + ";"
                        R = OP.Optimizacion("Bloque", "Propagacion de copias Regla 2", Original, Opti, fila)
                        OP.agregarOp(R)
                        
                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = " + str(tmp1) + " - " + str(tmp2) + ";"
                        Opti2 = newT + " = " + str(n.exp) + " + " + str(tmp2) + ";"
                        R2 = OP.Optimizacion("Bloque", "Eliminacion de codigo muerto Regla 3", Original2, Opti2, fila)
                        OP.agregarOp(R2)
                    else:
                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = " + str(tmp1) + " - " + str(tmp2) + ";"
                        Opti2 = newT + " = " + str(n.exp) + " - " + str(tmp2) + ";"
                        R2 = OP.Optimizacion("Bloque", "Propagacion de constantes Regla 4", Original2, Opti2, fila)
                        OP.agregarOp(R2)
                elif (n.id == str(tmp2)):
                    #Optimizacion 2
                    if (n.tipo == 1):  
                        #Optimizacion 
                        Original = newT + " = " + str(tmp1) + " - " + str(tmp2) + ";"
                        Opti = newT + " = " + str(tmp1) + " - " + str(n.exp) + ";"
                        R = OP.Optimizacion("Bloque", "Propagacion de copias Regla 2", Original, Opti, fila)
                        OP.agregarOp(R)

                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = " + str(tmp1) + " - " + str(tmp2) + ";"
                        Opti2 = newT + " = " + str(tmp1) + " - " + str(n.exp) + ";"
                        R2 = OP.Optimizacion("Bloque", "Eliminacion de codigo muerto Regla 3", Original2, Opti2, fila)
                        OP.agregarOp(R2)
                    else:
                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = " + str(tmp1) + " - " + str(tmp2) + ";"
                        Opti2 = newT + " = " + str(tmp1) + " - " + str(n.exp) + ";"
                        R2 = OP.Optimizacion("Bloque", "Propagacion de copias Regla 4", Original2, Opti2, fila)
                        OP.agregarOp(R2)
            fila += 1
            return newT, c3d
        if(exp.operador == OPERACIONES_ARITMETICAS.MULTIPLICACION):
            newT = str(t_global.varTemporal())
            c3d = exp1 + exp2 + "\t " + newT + " = " + str(tmp1) + " * " + str(tmp2) + ";\n"
            fila += 1

            #Optimizacion
            comprobar = False
            for n in ListaAsignacion:
                if (n.op == "*"):
                    if (n.exp1 == str(tmp1) and n.exp2 == str(tmp2)):
                        comprobar = True
                        #Optimizacion
                        Original = "\t  " + newT + " = " + str(tmp1) + " * " + str(tmp2) + ";\n"
                        Opti = "\t  " + newT + " = " + n.id + ";\n"
                        R = OP.Optimizacion("Bloque", "Subexpresiones comunes Regla 1", Original, Opti, fila)
                        OP.agregarOp(R)

            if (not comprobar):
                A = OP.Asignacion(newT, "*", str(tmp1), str(tmp2))
                ListaAsignacion.append(A) 

            #Optimizacion
            for n in ListaAsignacion2:
                if (n.id == str(tmp1)):
                    #Optimizacion 2
                    if (n.tipo == 1):
                        #Optimizacion
                        Original = newT + " = " + str(tmp1) + " * " + str(tmp2) + ";"
                        Opti = newT + " = " + str(n.exp) + " * " + str(tmp2) + ";"
                        R = OP.Optimizacion("Bloque", "Propagacion de copias Regla 2", Original, Opti, fila)
                        OP.agregarOp(R)

                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = " + str(tmp1) + " * " + str(tmp2) + ";"
                        Opti2 = newT + " = " + str(n.exp) + " * " + str(tmp2) + ";"
                        R2 = OP.Optimizacion("Bloque", "Eliminacion de codigo muerto Regla 3", Original2, Opti2, fila)
                        OP.agregarOp(R2)
                    else:
                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = " + str(tmp1) + " * " + str(tmp2) + ";"
                        Opti2 = newT + " = " + str(n.exp) + " * " + str(tmp2) + ";"
                        R2 = OP.Optimizacion("Bloque", "Propagacion de constantes Regla 4", Original2, Opti2, fila)
                        OP.agregarOp(R2)
                elif (n.id == str(tmp2)):
                    #Optimizacion 2
                    if (n.tipo == 1):
                        #Optimizacion
                        Original = newT + " = "+ str(tmp1) + " * " + str(tmp2) + ";"
                        Opti = newT + " = " + str(tmp1) + " * " + str(n.exp) + ";"
                        R = OP.Optimizacion("Bloque", "Propagacion de copias Regla 2", Original, Opti, fila)
                        OP.agregarOp(R)

                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = " + str(tmp1) + " * " + str(tmp2) + ";"
                        Opti2 = newT + " = " + str(tmp1) + " * " + str(n.exp) + ";"
                        R2 = OP.Optimizacion("Bloque", "Eliminacion de codigo muerto Regla 3", Original2, Opti2, fila)
                        OP.agregarOp(R2)
                    else:
                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = " + str(tmp1) + " * " + str(tmp2) + ";"
                        Opti2 = newT + " = " + str(tmp1) + " * " + str(n.exp) + ";"
                        R2 = OP.Optimizacion("Bloque", "Propagacion de copias Regla 4", Original2, Opti2, fila)
                        OP.agregarOp(R2)
            return newT, c3d
        if(exp.operador == OPERACIONES_ARITMETICAS.DIVISION):
            newT = str(t_global.varTemporal())
            Ltrue = t_global.etiquetaT()
            Lsalto = t_global.etiquetaT()
            c3d = exp1 + exp2
            c3d += "\t if (" + str(tmp2) + " != 0) goto " + Ltrue + "; \n"
            c3d += "\t printf(\"%c\", 77); \n"
            c3d += "\t printf(\"%c\", 97); \n"
            c3d += "\t printf(\"%c\", 116); \n"
            c3d += "\t printf(\"%c\", 104); \n"
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

            #Optimizacion
            comprobar = False
            for n in ListaAsignacion:
                if (n.op == "/"):
                    if (n.exp1 == str(tmp1) and n.exp2 == str(tmp2)):
                        comprobar = True
                        #Optimizacion
                        Original = "\t  " + newT + " = "+ str(tmp1) + " / " + str(tmp2) + ";\n"
                        Opti = "\t  " + newT + " = " + n.id + ";\n"
                        R = OP.Optimizacion("Bloque", "Subexpresiones comunes Regla 1", Original, Opti, fila)
                        OP.agregarOp(R)

            if (not comprobar):
                A = OP.Asignacion(newT, "/", str(tmp1), str(tmp2))
                ListaAsignacion.append(A) 

            #Optimizacion
            for n in ListaAsignacion2:
                if (n.id == str(tmp1)):
                    #Optimizacion 2
                    if (n.tipo == 1):
                        #Optimizacion 1
                        Original = newT + " = " + str(tmp1) + " / " + str(tmp2) + ";"
                        Opti = newT + " = " + str(n.exp) + " / " + str(tmp2) + ";"
                        R = OP.Optimizacion("Bloque", "Propagacion de copias Regla 2", Original, Opti, fila)
                        OP.agregarOp(R)
                        
                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = " + str(tmp1) + " / " + str(tmp2) + ";"
                        Opti2 = newT + " = " + str(n.exp) + " / " + str(tmp2) + ";"
                        R2 = OP.Optimizacion("Bloque", "Eliminacion de codigo muerto Regla 3", Original2, Opti2, fila)
                        OP.agregarOp(R2)
                    else:
                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = " + str(tmp1) + " / " + str(tmp2) + ";"
                        Opti2 = newT + " = " + str(n.exp) + " / " + str(tmp2) + ";"
                        R2 = OP.Optimizacion("Bloque", "Propagacion de constantes Regla 4", Original2, Opti2, fila)
                        OP.agregarOp(R2)
                elif (n.id == str(tmp2)):
                    #Optimizacion 2
                    if (n.tipo == 1):
                        #Optimizacion 1
                        Original = newT + " = " + str(tmp1) + " / " + str(tmp2) + ";"
                        Opti = newT + " = " + str(tmp1) + " / " + str(n.exp) + ";"
                        R = OP.Optimizacion("Bloque", "Propagacion de copias Regla 2", Original, Opti, fila)
                        OP.agregarOp(R)

                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = "+ str(tmp1) + " / " + str(tmp2) + ";"
                        Opti2 = newT + " = " + str(tmp1) + " / " + str(n.exp) + ";"
                        R2 = OP.Optimizacion("Bloque", "Eliminacion de codigo muerto Regla 3", Original2, Opti2, fila)
                        OP.agregarOp(R2)
                    else:
                        Original2 = str(n.id) + " = " + str(n.exp) + ";<br/>" + newT + " = " + str(tmp1) + " / " + str(tmp2) + ";"
                        Opti2 = newT + " = " + str(tmp1)+ " / " + str(n.exp) + ";"
                        R2 = OP.Optimizacion("Bloque", "Propagacion de constantes Regla 4", Original2, Opti2, fila)
                        OP.agregarOp(R2)

            fila += 16
            return newT, c3d
        if(exp.operador == OPERACIONES_ARITMETICAS.MODULO):
            newT = str(t_global.varTemporal())
            c3d = exp1 + exp2 + "\t " + newT + " = " + str(tmp1) + " % " + str(tmp2) + "; \n"
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
            cadena += "\t " + valorT + " = stack[(int)" + newT + "]; \n"
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
    elif(isinstance(exp, LlamadaFuncion)):
        tmp, c3d = instruccion_llamada_funcion(exp, ts, ambito)
        return tmp, c3d
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
    LV = ""
    LF = ""
    c3d = ""
    if(isinstance(expIf.expLogica, ExpresionIdentificador)):
        valor = 0
        valorBool = {}
        tmp, c3d = resolver_general(expIf.expLogica, ts, "if_" + ambito)
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.temp == tmp):
                valor = tipo.valor
        if(valor == 1):
            valorBool = ExpresionBool(True)
        elif(valor == 0):
            valorBool = ExpresionBool(False)
        LV, LF, c3d = resolver_general(valorBool, ts, "if_" + ambito)
    else:        
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
    LV = ""
    LF = ""
    c3d = ""
    if(isinstance(expElseif.expLogica, ExpresionIdentificador)):
        valor = 0
        valorBool = {}
        tmp, c3d = resolver_general(expElseif.expLogica, ts, "if_" + ambito)
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.temp == tmp):
                valor = tipo.valor
        if(valor == 1):
            valorBool = ExpresionBool(True)
        elif(valor == 0):
            valorBool = ExpresionBool(False)
        LV, LF, c3d = resolver_general(valorBool, ts, "if_" + ambito)
    else:  
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
            LV2 = ""
            LF2 = ""
            c3d2 = ""
            if(isinstance(listaif.expLogica, ExpresionIdentificador)):
                valor = 0
                valorBool = {}
                tmp, c3d = resolver_general(listaif.expLogica, ts, "if_" + ambito)
                for var in t_global.tablaSimbolos:
                    tipo = t_global.obtenerSimbolo(var)
                    if(tipo.temp == tmp):
                        valor = tipo.valor
                if(valor == 1):
                    valorBool = ExpresionBool(True)
                elif(valor == 0):
                    valorBool = ExpresionBool(False)
                LV2, LF2, c3d2 = resolver_general(valorBool, ts, "if_" + ambito)
            else:  
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
        variable = T.tipoSimbolo(newT, asignacion.id, "", 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, True)
        t_global.agregarSimbolo(variable)
    else:
        comprobar = False
        valorT = ""
        valorR = ""
        pos = ""
        tmp = ""
        c3d = ""
        if(isinstance(asignacion.exp, ExpresionBool)):
            if(asignacion.exp.boolean == True):
                tmp = 1
                c3d = ""
            else:
                tmp = 0
                c3d = ""
        else:
            tmp, c3d = resolver_general(asignacion.exp, ts, ambito)
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.nombre == asignacion.id):
                valorT = tipo.temp
                valorR = tipo.rol
                pos = tipo.pos
                comprobar = True
                actualizarSimbolo = T.tipoSimbolo(valorT, tipo.nombre, tmp, 1, pos, valorR, ambito, tipo.tipo, True)
                t_global.actualizarSimbolo(var, actualizarSimbolo)
        if(comprobar):
            cadena += c3d
            if(valorR == "PAR"):
                newT = t_global.varTemporal()
                cadena += "\t " + newT + " = P + " + pos + "; \n"
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

                #Optimizacion
                A2 = OP.Asignacion2(valorT, str(tmp), 1)
                ListaAsignacion2.append(A2)

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
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, True)

                #Optimizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionBool)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.BOOL, True)
                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionNumero)):
                if(isinstance(tmp, float)):
                    cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                    variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.F64, True)
                    
                    #Optimizacion
                    ListaAllAsignacion.append(newT)
                    A2 = OP.Asignacion2(newT, str(tmp), 1)
                    ListaAsignacion2.append(A2)
                else:
                    cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                    variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.I64, True)
                    #Optimizacion
                    ListaAllAsignacion.append(newT)
                    A2 = OP.Asignacion2(newT, str(tmp), 1)
                    ListaAsignacion2.append(A2)

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionCaracter)):
                cadena += c3d + "\t " + newT + " = " + str(ord(tmp)) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.CHAR, True)

                #Optimizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionBinaria)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, "Binaria", True)
                                
                #Optimizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

                fila += 1
                t_global.agregarSimbolo(variable)
            else:
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, "", True)
                                
                #Optimizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

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
        variable = T.tipoSimbolo(newT, asignacion.id, "", 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, True)
        t_global.agregarSimbolo(variable)
    else:
        comprobar = False
        valorT = ""
        valorR = ""
        pos = ""
        tmp = ""
        c3d = ""
        if(isinstance(asignacion.exp, ExpresionBool)):
            if(asignacion.exp.boolean == True):
                tmp = 1
                c3d = ""
            else:
                tmp = 0
                c3d = ""
        else:
            tmp, c3d = resolver_general(asignacion.exp, ts, ambito)
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.nombre == asignacion.id):
                valorT = tipo.temp
                valorR = tipo.rol
                pos = tipo.pos
                comprobar = True
                actualizarSimbolo = T.tipoSimbolo(valorT, tipo.nombre, tmp, 1, pos, valorR, ambito, tipo.tipo, True)
                t_global.actualizarSimbolo(var, actualizarSimbolo)
        if(comprobar):
            cadena += c3d
            if(valorR == "PAR"):
                newT = t_global.varTemporal()
                cadena += "\t " + newT + " = P + " + pos + "; \n"
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

                #Optimizacion
                A2 = OP.Asignacion2(valorT, str(tmp), 1)
                ListaAsignacion2.append(A2)

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
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, True)

                #Optmizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionBool)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.BOOL, True)
                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionNumero)):
                if(isinstance(tmp, float)):
                    cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                    variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.F64, True)
                    
                    #Optmizacion
                    ListaAllAsignacion.append(newT)
                    A2 = OP.Asignacion2(newT, str(tmp), 1)
                    ListaAsignacion2.append(A2)
                else:
                    cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                    variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.I64, True)
                    
                    #Optmizacion
                    ListaAllAsignacion.append(newT)
                    A2 = OP.Asignacion2(newT, str(tmp), 1)
                    ListaAsignacion2.append(A2)

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionCaracter)):
                cadena += c3d + "\t " + newT + " = " + str(ord(tmp)) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.CHAR, True)

                #Optmizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionBinaria)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, "Binaria", True)
                                
                #Optmizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

                fila += 1
                t_global.agregarSimbolo(variable)
            else:
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, "", True)
                                
                #Optmizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

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
        variable = T.tipoSimbolo(newT, asignacion.id, "", 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, False)
        t_global.agregarSimbolo(variable)
    else:
        comprobar = False
        valorT = ""
        valorR = ""
        pos = ""
        tmp = ""
        c3d = ""
        if(isinstance(asignacion.exp, ExpresionBool)):
            if(asignacion.exp.boolean == True):
                tmp = 1
                c3d = ""
            else:
                tmp = 0
                c3d = ""
        else:
            tmp, c3d = resolver_general(asignacion.exp, ts, ambito)
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.nombre == asignacion.id):
                valorT = tipo.temp
                valorR = tipo.rol
                pos = tipo.pos
                comprobar = True
                actualizarSimbolo = T.tipoSimbolo(valorT, tipo.nombre, tmp, 1, pos, valorR, ambito, tipo.tipo, True)
                t_global.actualizarSimbolo(var, actualizarSimbolo)
        if(comprobar):
            cadena += c3d
            if(valorR == "PAR"):
                newT = t_global.varTemporal()
                cadena += "\t " + newT + " = P + " + pos + "; \n"
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

                #Optimizacion
                A2 = OP.Asignacion2(valorT, str(tmp), 1)
                ListaAsignacion2.append(A2)

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
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, False)

                #Optmizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionBool)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.BOOL, False)
                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionNumero)):
                if(isinstance(tmp, float)):
                    cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                    variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.F64, True)
                    
                    #Optmizacion
                    ListaAllAsignacion.append(newT)
                    A2 = OP.Asignacion2(newT, str(tmp), 1)
                    ListaAsignacion2.append(A2)
                else:
                    cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                    variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.I64, False)

                    #Optmizacion
                    ListaAllAsignacion.append(newT)
                    A2 = OP.Asignacion2(newT, str(tmp), 1)
                    ListaAsignacion2.append(A2)
                                
                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionCaracter)):
                cadena += c3d + "\t " + newT + " = " + str(ord(tmp)) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.CHAR, False)

                #Optmizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionBinaria)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, "Binaria", True)
                                
                #Optmizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

                fila += 1
                t_global.agregarSimbolo(variable)
            else:
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, "", False)
                                
                #Optmizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

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
        variable = T.tipoSimbolo(newT, asignacion.id, "", 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, False)
        t_global.agregarSimbolo(variable)
    else:
        comprobar = False
        valorT = ""
        valorR = ""
        pos = ""
        tmp = ""
        c3d = ""
        if(isinstance(asignacion.exp, ExpresionBool)):
            if(asignacion.exp.boolean == True):
                tmp = 1
                c3d = ""
            else:
                tmp = 0
                c3d = ""
        else:
            tmp, c3d = resolver_general(asignacion.exp, ts, ambito)
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.nombre == asignacion.id):
                valorT = tipo.temp
                valorR = tipo.rol
                pos = tipo.pos
                comprobar = True
                actualizarSimbolo = T.tipoSimbolo(valorT, tipo.nombre, tmp, 1, pos, valorR, ambito, tipo.tipo, True)
                t_global.actualizarSimbolo(var, actualizarSimbolo)
        if(comprobar):
            cadena += c3d
            if(valorR == "PAR"):
                newT = t_global.varTemporal()
                cadena += "\t " + newT + " = P + " + pos + "; \n"
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

                #Optimizacion
                A2 = OP.Asignacion2(valorT, str(tmp), 1)
                ListaAsignacion2.append(A2)

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
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, False)

                #Optmizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionBool)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.BOOL, False)
                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionNumero)):
                if(isinstance(tmp, float)):
                    cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                    variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.F64, True)
                    
                    #Optmizacion
                    ListaAllAsignacion.append(newT)
                    A2 = OP.Asignacion2(newT, str(tmp), 1)
                    ListaAsignacion2.append(A2)
                else:
                    cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                    variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.I64, False)

                    #Optmizacion
                    ListaAllAsignacion.append(newT)
                    A2 = OP.Asignacion2(newT, str(tmp), 1)
                    ListaAsignacion2.append(A2)
                                
                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionCaracter)):
                cadena += c3d + "\t " + newT + " = " + str(ord(tmp)) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, TABS.TIPO_DATO.CHAR, False)

                #Optmizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

                fila += 1
                t_global.agregarSimbolo(variable)
            elif(isinstance(asignacion.exp, ExpresionBinaria)):
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, "Binaria", True)
                                
                #Optmizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

                fila += 1
                t_global.agregarSimbolo(variable)
            else:
                cadena += c3d + "\t " + newT + " = " + str(tmp) + "; \n"
                variable = T.tipoSimbolo(newT, asignacion.id, tmp, 1, 1, "local", ambito, "", False)
                                
                #Optmizacion
                ListaAllAsignacion.append(newT)
                A2 = OP.Asignacion2(newT, str(tmp), 1)
                ListaAsignacion2.append(A2)

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
        variable = T.tipoSimbolo(newT, asignacion.id, "", 1, 1, "local", ambito, TABS.TIPO_DATO.STRING, False)
        t_global.agregarSimbolo(variable)
    else:
        comprobar = False
        valorT = ""
        valorR = ""
        valorM = False
        pos = ""
        tmp = ""
        c3d = ""
        if(isinstance(asignacion.exp, ExpresionBool)):
            if(asignacion.exp.boolean == True):
                tmp = 1
                c3d = ""
            else:
                tmp = 0
                c3d = ""
        else:
            tmp, c3d = resolver_general(asignacion.exp, ts, ambito)
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.nombre == asignacion.id):
                valorT = tipo.temp
                valorR = tipo.rol
                pos = tipo.pos
                valorM = tipo.mutable
                comprobar = True
                actualizarSimbolo = T.tipoSimbolo(valorT, tipo.nombre, tmp, 1, pos, valorR, ambito, tipo.tipo, True)
                t_global.actualizarSimbolo(var, actualizarSimbolo)
        if(comprobar):
            if(valorM == True):
                cadena += c3d
                if(valorR == "PAR"):
                    newT = t_global.varTemporal()
                    cadena += "\t " + newT + " = P + " + pos + "; \n"
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
    LV = ""
    LF = ""
    c3d = ""
    if(isinstance(instruccion.exp, ExpresionIdentificador)):
        valor = 0
        Ltrue = t_global.etiquetaT()
        Lfalse = t_global.etiquetaT()
        tmp, c3d = resolver_general(instruccion.exp, ts, "while_" + ambito)
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.temp == tmp):
                valor = tipo.valor
        if(valor == 1):
            c3d += "\t if (" + tmp + " == 1) goto " + Ltrue + ";\n"
            c3d += "\t goto " + Lfalse + ";\n"
            fila += 2
            LV = Ltrue
            LF = Lfalse
        elif(valor == 0):
            c3d += "\t if (" + tmp + " == 1) goto " + Ltrue + ";\n"
            c3d += "\t goto " + Lfalse + ";\n"
            fila += 2
            LV = Ltrue
            LF = Lfalse
    else:   
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

def instruccion_ciclo_for(instruccion, ts, ambito):
    global t_global, existe_break, existe_continue, fila
    cadena = ""
    if(instruccion.exp2 != ""):
        tmp1, c3d1 = resolver_general(instruccion.exp1, ts, "for_" + ambito)
        asignar = AsignacionMutable(instruccion.id, ExpresionNumero(tmp1), instruccion.linea, instruccion.columna)
        cadena = c3d1
        cadena += instruccion_asignacion_mut(asignar, ts, "for_" + ambito)

        Ltrue = t_global.etiquetaT()
        Lfalse = t_global.etiquetaT()
        Lsalto = t_global.etiquetaT()

        tmp2, c3d2 = resolver_general(instruccion.exp2, ts, "for_" + ambito)
        cadena += c3d2
        valorT = ""
        for var in t_global.tablaSimbolos:
            tipo = t_global.obtenerSimbolo(var)
            if(tipo.nombre == instruccion.id and tipo.ambito == "for_" + ambito):
                valorT = tipo.temp
        cadena += "\t " + Lsalto + ": \n"
        fila += 1
        cadena += "\t if(" + str(valorT) + " < " + str(tmp2) + ") goto " + Ltrue + "; \n \t goto " + Lfalse + "; \n"

        #Falta Optimizacion de 1597 a 1600

        fila += 2

        cadena += "\t " + Ltrue + ": \n"
        cadena += procesar_instrucciones(instruccion.instrucciones, ts, "for_" + ambito)
        cadena += "\t " + str(valorT) + " = " + str(valorT) + " + 1; \n"
        cadena += "\t goto " + Lsalto + "; \n"
        cadena += "\t " + Lfalse + ": \n"
        fila += 4
    return cadena 
    #elif(type(instruccion.exp1) == list):
    #    for i in instruccion.exp1:
    #        tmp1, c3d1 = resolver_general(i, ts, "for_" + ambito)
    #        asignar = AsignacionMutable(instruccion.id, ExpresionNumero(tmp1), instruccion.linea, instruccion.columna)
    #        cadena += c3d1
    #        cadena += instruccion_asignacion_mut(asignar, ts, "for_" + ambito)
    #        cadena += procesar_instrucciones(instruccion.instrucciones, ts, "for_" + ambito)
    #    return cadena
    #else:
    #    tmp, c3d = resolver_general(instruccion.exp1, ts, "for_" + ambito)

def instruccion_funcion(funcion, ts, ambito):
    global t_global, cadenafuncion, Lista_return, fila
    funciones = T.tipoSimbolo("", funcion.id, "", len(funcion.listaparametro) + 1, 0, "funcion", ambito, "funcion", True)
    t_global.agregarSimbolo(funciones)
    pos = 1
    for n in funcion.listaparametro:
        newT = t_global.varTemporal()
        parametro = T.tipoSimbolo(newT, n.id, "", 1, str(pos), "PAR", ambito, n.tipo, True)
        t_global.agregarSimbolo(parametro)
        pos += 1
    cadena = procesar_instrucciones(funcion.instrucciones, ts, ambito)
    cadenafuncion += "\n void " + funcion.id + "(){ \n"
    cadenafuncion += cadena
    fila += 1
    for n in Lista_return:
        cadenafuncion += "\t " + n + ": \n"
        fila += 1
    Lista_return = []
    cadenafuncion += "\t return; \n"
    cadenafuncion += "} \n"
    fila += 2
    return ""

def instruccion_funcion_tipo(funcion, ts, ambito):
    global t_global, cadenafuncion, Lista_return, fila
    funciones = T.tipoSimbolo("", funcion.id, "", len(funcion.listaparametro) + 1, 0, "funcion", ambito, "funcion", True)
    t_global.agregarSimbolo(funciones)
    pos = 1
    for n in funcion.listaparametro:
        newT = t_global.varTemporal()
        parametro = T.tipoSimbolo(newT, n.id, "", 1, str(pos), "PAR", ambito, n.tipo, True)
        t_global.agregarSimbolo(parametro)
        pos += 1
    cadena = procesar_instrucciones(funcion.instrucciones, ts, ambito)
    cadenafuncion += "\n void " + funcion.id + "(){ \n"
    cadenafuncion += cadena
    fila += 1
    for n in Lista_return:
        cadenafuncion += "\t " + n + ": \n"
        fila += 1
    Lista_return = []
    cadenafuncion += "\t return; \n"
    cadenafuncion += "} \n"
    fila += 2
    return ""

def instruccion_funcion_main(funcion, ts, ambito):
    global t_global, cadenafuncion, Lista_return, fila
    cadena = ""
    funciones = T.tipoSimbolo("", funcion.id, "", "", 0, "funcion", ambito, "funcion", True)
    t_global.agregarSimbolo(funciones)
    cadena = procesar_instrucciones(funcion.instrucciones, ts, ambito)
    return cadena

def instruccion_llamada_funcion(funcion, ts, ambito):
    global t_global, fila
    cadena = ""
    tam = 0
    newT = t_global.varTemporal()
    cadena += "\t " + newT + " = P + 0; \n"
    fila += 1
    for n in funcion.listaparametro:
        tmp, c3d = resolver_general(n, ts, ambito)
        cadena += "\t " + newT + " = " + newT + " + 1; \n"
        cadena += c3d + "\t stack[(int)" + str(newT) + "] = " + str(tmp) + "; \n"
        fila += 2
    cadena += "\t P = P + 0; \n"
    cadena += "\t " + funcion.id + "(); \n"
    fila += 1
    newV = t_global.varTemporal()
    cadena += "\t " + newV + " = stack[(int)P]; \n"
    cadena += "\t P = P - 0; \n"
    fila += 2
    return newV, cadena

def instruccion_asignacion_arreglo_mutable(instruccion, ts, ambito):
    global posH, t_global, fila
    cadena = ""
    listaValor = []
    listac3d = []
    for n in instruccion.listaexp:
        tmp, c3d = resolver_general(n, ts, ambito)
        listac3d.append(c3d)
        listaValor.append(tmp)
    newT = t_global.varTemporal()
    simbolo = T.tipoSimbolo(newT, instruccion.id, listaValor, len(listaValor), posH, "local", ambito, "Arreglo", True)
    cadena += "\t " + newT + " = H; \n"
    fila += 1
    x = 0
    for n in listaValor:
        cadena += listac3d[x]
        cadena += "\t heap[(int)H] = " + str(n) + "; \n"
        cadena += "\t H = H + 1; \n"
        posH += 1
        x += 1
        fila += 2
    cadena += "\t heap[(int)H] = -1; \n"
    cadena += "\t H = H + 1; \n"
    posH += 1
    fila += 2
    t_global.agregarSimbolo(simbolo)
    return cadena

def instruccion_asignacion_arreglo_mutable_tipo(instruccion, ts, ambito):
    global posH, t_global, fila
    cadena = ""
    listaValor = []
    listac3d = []
    for n in instruccion.listaexp:
        tmp, c3d = resolver_general(n, ts, ambito)
        listac3d.append(c3d)
        listaValor.append(tmp)
    newT = t_global.varTemporal()
    simbolo = T.tipoSimbolo(newT, instruccion.id, listaValor, len(listaValor), posH, "local", ambito, "Arreglo", True)
    cadena += "\t " + newT + " = H; \n"
    fila += 1
    x = 0
    for n in listaValor:
        cadena += listac3d[x]
        cadena += "\t heap[(int)H] = " + str(n) + "; \n"
        cadena += "\t H = H + 1; \n"
        posH += 1
        x += 1
        fila += 2
    cadena += "\t heap[(int)H] = -1; \n"
    cadena += "\t H = H + 1; \n"
    posH += 1
    fila += 2
    t_global.agregarSimbolo(simbolo)
    return cadena

def instruccion_asignacion_arreglo_no_mutable(instruccion, ts, ambito):
    global posH, t_global, fila
    cadena = ""
    listaValor = []
    listac3d = []
    for n in instruccion.listaexp:
        tmp, c3d = resolver_general(n, ts, ambito)
        listac3d.append(c3d)
        listaValor.append(tmp)
    newT = t_global.varTemporal()
    simbolo = T.tipoSimbolo(newT, instruccion.id, listaValor, len(listaValor), posH, "local", ambito, "Arreglo", False)
    cadena += "\t " + newT + " = H; \n"
    fila += 1
    x = 0
    for n in listaValor:
        cadena += listac3d[x]
        cadena += "\t heap[(int)H] = " + str(n) + "; \n"
        cadena += "\t H = H + 1; \n"
        posH += 1
        x += 1
        fila += 2
    cadena += "\t heap[(int)H] = -1; \n"
    cadena += "\t H = H + 1; \n"
    posH += 1
    fila += 2
    t_global.agregarSimbolo(simbolo)
    return cadena

def instruccion_asignacion_arreglo_no_mutable_tipo(instruccion, ts, ambito):
    global posH, t_global, fila
    cadena = ""
    listaValor = []
    listac3d = []
    for n in instruccion.listaexp:
        tmp, c3d = resolver_general(n, ts, ambito)
        listac3d.append(c3d)
        listaValor.append(tmp)
    newT = t_global.varTemporal()
    simbolo = T.tipoSimbolo(newT, instruccion.id, listaValor, len(listaValor), posH, "local", ambito, "Arreglo", False)
    cadena += "\t " + newT + " = H; \n"
    fila += 1
    x = 0
    for n in listaValor:
        cadena += listac3d[x]
        cadena += "\t heap[(int)H] = " + str(n) + "; \n"
        cadena += "\t H = H + 1; \n"
        posH += 1
        x += 1
        fila += 2
    cadena += "\t heap[(int)H] = -1; \n"
    cadena += "\t H = H + 1; \n"
    posH += 1
    fila += 2
    t_global.agregarSimbolo(simbolo)
    return cadena

def instruccion_asignacion_vector_mutable(instruccion, ts, ambito):
    global posH, t_global, fila
    cadena = ""
    listaValor = []
    listac3d = []
    for n in instruccion.listaexp:
        tmp, c3d = resolver_general(n, ts, ambito)
        listac3d.append(c3d)
        listaValor.append(tmp)
    newT = t_global.varTemporal()
    simbolo = T.tipoSimbolo(newT, instruccion.id, listaValor, len(listaValor), posH, "local", ambito, "Arreglo", True)
    cadena += "\t " + newT + " = H; \n"
    fila += 1
    x = 0
    for n in listaValor:
        cadena += listac3d[x]
        cadena += "\t heap[(int)H] = " + str(n) + "; \n"
        cadena += "\t H = H + 1; \n"
        posH += 1
        x += 1
        fila += 2
    cadena += "\t heap[(int)H] = -1; \n"
    cadena += "\t H = H + 1; \n"
    posH += 1
    fila += 2
    t_global.agregarSimbolo(simbolo)
    return cadena

def instruccion_asignacion_vector_mutable_tipo(instruccion, ts, ambito):
    global posH, t_global, fila
    cadena = ""
    listaValor = []
    listac3d = []
    for n in instruccion.listaexp:
        tmp, c3d = resolver_general(n, ts, ambito)
        listac3d.append(c3d)
        listaValor.append(tmp)
    newT = t_global.varTemporal()
    simbolo = T.tipoSimbolo(newT, instruccion.id, listaValor, len(listaValor), posH, "local", ambito, "Arreglo", True)
    cadena += "\t " + newT + " = H; \n"
    fila += 1
    x = 0
    for n in listaValor:
        cadena += listac3d[x]
        cadena += "\t heap[(int)H] = " + str(n) + "; \n"
        cadena += "\t H = H + 1; \n"
        posH += 1
        x += 1
        fila += 2
    cadena += "\t heap[(int)H] = -1; \n"
    cadena += "\t H = H + 1; \n"
    posH += 1
    fila += 2
    t_global.agregarSimbolo(simbolo)
    return cadena

def instruccion_asignacion_vector_no_mutable(instruccion, ts, ambito):
    global posH, t_global, fila
    cadena = ""
    listaValor = []
    listac3d = []
    for n in instruccion.listaexp:
        tmp, c3d = resolver_general(n, ts, ambito)
        listac3d.append(c3d)
        listaValor.append(tmp)
    newT = t_global.varTemporal()
    simbolo = T.tipoSimbolo(newT, instruccion.id, listaValor, len(listaValor), posH, "local", ambito, "Arreglo", False)
    cadena += "\t " + newT + " = H; \n"
    fila += 1
    x = 0
    for n in listaValor:
        cadena += listac3d[x]
        cadena += "\t heap[(int)H] = " + str(n) + "; \n"
        cadena += "\t H = H + 1; \n"
        posH += 1
        x += 1
        fila += 2
    cadena += "\t heap[(int)H] = -1; \n"
    cadena += "\t H = H + 1; \n"
    posH += 1
    fila += 2
    t_global.agregarSimbolo(simbolo)
    return cadena

def instruccion_asignacion_vector_no_mutable_tipo(instruccion, ts, ambito):
    global posH, t_global, fila
    cadena = ""
    listaValor = []
    listac3d = []
    for n in instruccion.listaexp:
        tmp, c3d = resolver_general(n, ts, ambito)
        listac3d.append(c3d)
        listaValor.append(tmp)
    newT = t_global.varTemporal()
    simbolo = T.tipoSimbolo(newT, instruccion.id, listaValor, len(listaValor), posH, "local", ambito, "Arreglo", False)
    cadena += "\t " + newT + " = H; \n"
    fila += 1
    x = 0
    for n in listaValor:
        cadena += listac3d[x]
        cadena += "\t heap[(int)H] = " + str(n) + "; \n"
        cadena += "\t H = H + 1; \n"
        posH += 1
        x += 1
        fila += 2
    cadena += "\t heap[(int)H] = -1; \n"
    cadena += "\t H = H + 1; \n"
    posH += 1
    fila += 2
    t_global.agregarSimbolo(simbolo)
    return cadena

def procesar_instrucciones(instrucciones, ts, ambito):
    print(instrucciones)
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
        elif(isinstance(instruccion, CicloFor)):
            cadena += instruccion_ciclo_for(instruccion, ts, ambito)
        elif(isinstance(instruccion, Funcion)):
            cadena += instruccion_funcion(instruccion, ts, ambito)
        elif(isinstance(instruccion, FuncionTipo)):
            cadena += instruccion_funcion_tipo(instruccion, ts, ambito)
        elif(isinstance(instruccion, FuncionMain)):
            cadena += instruccion_funcion_main(instruccion, ts, ambito)
        elif(isinstance(instruccion, LlamadaFuncion)):
            tmp, c3d = instruccion_llamada_funcion(instruccion, ts, ambito)
            cadena += c3d
        elif(isinstance(instruccion, AsignacionArregloMutable)):
            cadena += instruccion_asignacion_arreglo_mutable(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionArregloMutableTipo)):
            cadena += instruccion_asignacion_arreglo_mutable_tipo(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionArregloNoMutable)):
            cadena += instruccion_asignacion_arreglo_no_mutable(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionArregloNoMutableTipo)):
            cadena += instruccion_asignacion_arreglo_no_mutable_tipo(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionVectorMutable)):
            cadena += instruccion_asignacion_vector_mutable(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionVectorMutableTipo)):
            cadena += instruccion_asignacion_vector_mutable_tipo(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionVectorNoMutable)):
            cadena += instruccion_asignacion_vector_no_mutable(instruccion, ts, ambito)
        elif(isinstance(instruccion, AsignacionVectorNoMutableTipo)):
            cadena += instruccion_asignacion_vector_no_mutable_tipo(instruccion, ts, ambito)

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

    for n in ListaAllAsignacion:
        Original2 = str(n)
        Opti2 = ""
        R2 = OP.Optimizacion("Bloque", "Eliminacion de codigo muerto Regla 3", Original2, Opti2, fila)
        OP.agregarOp(R2)

    ListaAllAsignacion = []
    ListaAsignacion = []
    ListaAsignacion2 = []
    fila = 0

    t_global.generarTablaTemporales()
    OP.ReporteOptimizacion()
    t_global.limpiar()
    return mensaje