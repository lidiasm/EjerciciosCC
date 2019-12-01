#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:19:12 2019

@author: Lidia Sánchez Mérida.
"""

from flask import Flask, Response
import mascotas
import json
import os

app = Flask(__name__)
m = mascotas.Mascotas()

@app.route("/")
def index():
    return Response("Microservicio para recopilar datos de mascotas.", status=200)

@app.route("/conectar_petfinder", methods=['GET'])
def conectar_petfinder():
    """Servicio REST para conectar con la API Petfinder. Para ello deberán
    haberse definido, previamente, dos variables de entorno con la api key y
    la api secret.
    Si las credenciales no son válidas devolverá el código 404 BAD REQUEST."""
    api_key = os.environ.get("API_KEY")
    api_secret = os.environ.get("API_SECRET")
    resultado = m.conectar_APIPetfinder(api_key, api_secret)
    if (resultado == "Credenciales no válidas."): return Response(resultado, status=400)
    else: return Response(resultado, status=200)
    
@app.route("/descargar_datos_mascotas", methods=['GET'])
def descargar_datos_mascotas():
    """Servicio REST que descarga datos de hasta 20 mascotas. Para ello,
    previamente, se deberá haber realizado la conexión con la API.
    Si no se ha realizado dicha conexion devolverá el código de error 400 BAD REQUEST.
    """
    resultado = m.descargar_datos_mascotas()
    if (type(resultado) == str): return Response(resultado, status=400)
    elif (type(resultado) == dict): return Response(json.dumps(resultado),
          status=200, mimetype="application/json")

@app.route("/aniadir_organizacion/<string:nombre>/<string:ciudad>/<string:pais>", methods=['PUT'])
def aniadir_organizacion(nombre, ciudad, pais):
    """Servicio REST para añadir una nueva organización. Para ello se deberá
    proporcionar el nombre, la ciudad y el país."""
    nueva_organizacion = {'nombre':nombre, 'ciudad':ciudad, 'pais':pais}
    resultado = m.aniadir_organizacion(nueva_organizacion)
    if (type(resultado) == str): return Response(resultado, status=400)
    elif (type(resultado) == dict): return Response(json.dumps(resultado),
          status=200, mimetype="application/json")
    
if __name__ == "__main__":
    app.run(debug=True)