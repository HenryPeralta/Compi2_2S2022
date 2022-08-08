class Error():
    def __init__(self, descripcion, ambito, linea, columna, fecha):
        self.descripcion = descripcion
        self.ambito = ambito
        self.linea = linea
        self.columna = columna
        self.fecha = fecha

lista=[]

def agregarError(e):
    lista.append(e)

def GenerarTablaErrores():
    global lista
    file = open ("./reportes/taberrores.html", "w")
    file.write("<!DOCTYPE html>\n<html>\n")
    file.write("<head>\n")
    file.write("<meta charset = " + "'utf-8'" + " />\n")
    file.write("<title>Tabla de errores</title>\n")
    file.write("<meta name = " + "'viewport'" + " content = " + "'initial-scale=1.0; maximum-scale=1.0; width=device-width;'" + ">\n")
    file.write("<Style type = " + "'text/css'" + ">\n")
    file.write("@import url(https://fonts.googleapis.com/css?family=Roboto:400,500,700,300,100);;\n")
    file.write("body{\n")
    file.write("    background: rgba(204, 204, 204, 1);\n")
    file.write("    background: -moz-linear-gradient(top, rgba(204, 204, 204, 1) 0%, rgba(255, 255, 255, 1) 100%);\n")
    file.write("    background: -webkit-gradient(left top, left bottom, color-stop(0%, rgba(204, 204, 204, 1)), color - stop(100%, rgba(255, 255, 255, 1)));\n")
    file.write("    background: -webkit-linear-gradient(top, rgba(204, 204, 204, 1) 0%, rgba(255, 255, 255, 1) 100%);\n")
    file.write("    background: -o-linear-gradient(top, rgba(204, 204, 204, 1) 0%, rgba(255, 255, 255, 1) 100%);\n")
    file.write("    background: -ms-linear-gradient(top, rgba(204, 204, 204, 1) 0%, rgba(255, 255, 255, 1) 100%);\n")
    file.write("    background: linear-gradient(to bottom, rgba(204, 204, 204, 1) 0%, rgba(255, 255, 255, 1) 100%);\n")
    file.write("    filter: progid: DXImageTransform.Microsoft.gradient(startColorstr = '#cccccc', endColorstr = '#ffffff', GradientType = 0);\n")
    file.write("    font-family: " + "'Roboto'" + ", helvetica, arial, sans-serif;\n")
    file.write("    font-size: 16px;\n")
    file.write("    font-weight: 400;\n")
    file.write("    text-rendering: optimizeLegibility;\n")
    file.write("}\n")

    file.write("div.table-title{\n")
    file.write("    display: block;\n")
    file.write("    margin: auto;\n")
    file.write("    max-width: 600px;\n")
    file.write ("   padding: 5px;\n")
    file.write("    width: 100%;\n")
    file.write("}\n")

    file.write(".table-title h3{\n")
    file.write("    color: black;\n")
    file.write("    font-size: 30px;\n")
    file.write("    font-weight: 400;\n")
    file.write("    font-style:normal;\n")
    file.write("    text-shadow: 1px 1px black;\n")
    file.write("    text-transform:uppercase;\n")
    file.write("}\n")

    file.write(".table-fill{\n")
    file.write("    background: white;\n")
    file.write("    border-radius:3px;\n")
    file.write("    border-color: black;\n")
    file.write("    border-collapse: collapse;\n")
    file.write("    height: 320px;\n")
    file.write("    margin: auto;\n")
    file.write("    max-width: 600px;\n")
    file.write("    padding: 5px;\n")
    file.write("    width: 100%;\n")
    file.write("    box-shadow: 30px 30px 30px 30px rgba(1, 0.1, 0.1, 0.1);\n")
    file.write("    animation: float 5s infinite;\n")
    file.write("}\n")

    file.write("th{\n")
    file.write("    color:#D5DDE5;\n")
    file.write("    background:#1b1e24;\n")
    file.write("    border-bottom:4px solid #9ea7af;\n")
    file.write("    border-right: 1px solid #343a45;\n")
    file.write("    font-size:23px;\n")
    file.write("    font-weight: 100;\n")
    file.write("    padding: 24px;\n")
    file.write("    text-align:left;\n")
    file.write("    text-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);\n")
    file.write("    vertical-align:middle;\n")
    file.write("}\n")

    file.write("th:last-child {\n")
    file.write("    border-top-right-radius:3px;\n")
    file.write("    border-right:none;\n")
    file.write("}\n")

    file.write("tr{\n")
    file.write("    border-top: 1px solid #C1C3D1;\n")
    file.write("    border-bottom: 1px solid #C1C3D1;\n")
    file.write("    color:#666B85;\n")
    file.write("    font-size:16px;\n")
    file.write("    font-weight:normal;\n")
    file.write("    text-shadow: 0 1px 1px rgba(256, 256, 256, 0.1);\n")
    file.write("}\n")

    file.write("tr:first-child{\n")
    file.write("    border-top:none;\n")
    file.write("}\n")

    file.write("tr:last-child{\n")
    file.write("    border-bottom:none;\n")
    file.write("}\n")

    file.write("tr:last-child td:first-child{\n")
    file.write("    border-bottom-left-radius:3px;\n")
    file.write("}\n")

    file.write("tr:last-child td:last-child{\n")
    file.write("    border-bottom-right-radius:3px;\n")
    file.write("}\n")

    file.write("td{\n")
    file.write("    background:#FFFFFF;\n")
    file.write("    padding: 20px;\n")
    file.write("    text-align:left;\n")
    file.write("    vertical-align:middle;\n")
    file.write("    font-weight:300;\n")
    file.write("    font-size:18px;\n")
    file.write("    text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.1);\n")
    file.write("    border-right: 1px solid #C1C3D1;\n")
    file.write("}\n")

    file.write("td:last-child{\n")
    file.write("    border-right: 0px;\n")
    file.write("}\n")

    file.write("th.text-left {\n")
    file.write("    text-align: left;\n")
    file.write("}\n")

    file.write("th.text-center {\n")
    file.write("    text-align: center;\n")
    file.write("}\n")

    file.write("th.text-right {\n")
    file.write("    text-align: right;\n")
    file.write("}\n")

    file.write("td.text-left {\n")
    file.write("    text-align: left;\n")
    file.write("}\n")

    file.write("td.text-center {\n")
    file.write("    text-align: center;\n")
    file.write("}\n")

    file.write("td.text-right {\n")
    file.write("    text-align: right;\n")
    file.write("}\n")

    file.write("</Style>\n")
    file.write("</head>\n")

    file.write("<body>\n")

    file.write("</div>\n")
    file.write("<div class=" + "'table-title'" + ">\n")
    file.write("<h3>Tabla de Errores</h3>\n")
    file.write("</div>\n")
    file.write("<table class=" + "'table-fill'" + ">\n")
    file.write("<thead>\n")
    file.write("<tr>\n")
    file.write("<th class=" + "'text-left'" + ">No.</th>\n")
    file.write("<th class=" + "'text-left'" + ">Descripcion</th>\n")
    file.write("<th class=" + "'text-left'" + ">Ambito</th>\n")
    file.write("<th class=" + "'text-left'" + ">Fila</th>\n")
    file.write("<th class=" + "'text-left'" + ">Columna</th>\n")
    file.write("<th class=" + "'text-left'" + ">Fecha y Hora</th>\n")

    file.write("</tr>\n")

    file.write("</thead>\n")

    file.write("<tbody class=" + "'table-hover'" + ">")
    contador = 1
    for n in lista:
        file.write("<tr>")
        file.write("<td>"+str(contador)+"</td>")
        file.write("<td>"+str(n.descripcion)+"</td>")
        file.write("<td>"+str(n.ambito)+"</td>")
        file.write("<td>"+str(n.linea)+"</td>")
        file.write("<td>"+str(n.columna)+"</td>")
        file.write("<td>"+str(n.fecha)+"</td>")
        file.write("<tr>")
        contador += 1

    file.close()
    lista=[]