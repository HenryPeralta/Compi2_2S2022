class Temporales:
    def __init__(self, tablaSimbolos = {}, temp = 0, etiqueta = 0, parametro = 0, funcion = 1, retorno = 0):
        self.tablaSimbolos = tablaSimbolos.copy()
        self.temp = temp
        self.parametro = parametro
        self.etiqueta = etiqueta
        self.funcion = funcion
        self.retorno = retorno

    def limpiar(self):
        self.temp = 0
        self.parametro = 0
        self.etiqueta = 0

    def varTemporal(self):
        variable = "t" + str(self.temp)
        self.temp += 1
        return str(variable)

    def varParametro(self):
        variable = "p" + str(self.parametro)
        self.parametro += 1
        return str(variable)

    def varRetorno(self):
        variable = "r"+ str(self.retorno)
        self.retorno += 1
        return str(variable)

    def varFuncion(self):
        variable = "F" + str(self.funcion)
        self.funcion += 1
        return str(variable)

    def etiquetaT(self):
        variable = "L" + str(self.etiqueta)
        self.etiqueta += 1
        return variable

    def obtenerT(self):
        return self.temp

    def agregarSimbolo(self, simbolo):
        self.tablaSimbolos[str(simbolo.nombre)] = simbolo

    def obtenerSimbolo(self, simbolo):
        if not simbolo in self.tablaSimbolos:
            pass
            return None
        else:
            return self.tablaSimbolos[simbolo]

    def actualizarSimbolo(self, simbolo, nuevoSi):
        if not simbolo in self.tablaSimbolos:
            print("Si se actualizo")
            pass
        else:
            self.tablaSimbolos[simbolo] = nuevoSi

class tipoSimbolo():
    def __init__(self, temp, nombre, tam, pos, rol, ambito, tipo, mutable):
        self.temp = temp
        self.nombre = nombre
        self.tam = tam
        self.pos = pos
        self.rol = rol
        self.ambito = ambito
        self.tipo = tipo
        self.mutable = mutable