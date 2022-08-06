from flask import Flask, render_template, request
from analizador import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    entrada = ""
    salida = ""
    if(request.method == 'POST'):
        entrada = request.form.get('editor')
        salida = datos(entrada)
    return render_template('editor.html', entrada=entrada, salida=salida)

if(__name__ == '__main__'):
    app.run(port=5000, debug=True)
