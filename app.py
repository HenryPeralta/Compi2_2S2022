from flask import Flask, render_template, request
from analizador import *
from traductorc3d import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    entrada = ""
    salida = ""
    if(request.method == 'POST'):
        if(request.form['boton'] == 'Analizar'):
            entrada = request.form.get('editor')
            salida = datos(entrada)
        elif(request.form['boton'] == 'Traducir'):
            entrada = request.form.get('editor')
            salida = datosC3D(entrada)
    return render_template('editor.html', entrada=entrada, salida=salida)

if(__name__ == '__main__'):
    app.run(port=5000, debug=True)
