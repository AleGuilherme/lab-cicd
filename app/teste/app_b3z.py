#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route('/') # rota inicial
def startup_inicio():
    return 'Rota Inicio!\n'

@app.route('/startup') # rota nome startup
def startup_name():
    return 'B3Z - COMBATE A DENGUE!\n'

@app.route('/startup/equipe') # rota equipe B3Z
def startup_equipe():
    return 'ALEXANDRE GUILHERME\nADRIANO CESAR MARTINS\nVITOR CHALUPPE RADI\n'

@app.route('/startup/<rota_dinamica>') # rota dinamica
def startup_din(rota_dinamica):
    return 'Rota dinamica B3Z %s!\n' % rota_dinamica

if __name__ == '__main__':
    app.run(host='0.0.0.0') # open for everyone
