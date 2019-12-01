#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:37:03 2019

@author: Lidia Sánchez Mérida
"""
import sys
sys.path.append("src")
import mascotas
import rest

app = rest.app.test_client()

def test_conectar_api():
    """Test 1: conexión correcta con la API Petfinder."""
    respuesta = app.get('/conectar_petfinder')
    assert respuesta.status_code == 200
    
def test_descargar_datos_mascotas():
    """Test 2: descarga correcta de datos de nuevas mascotas."""
    respuesta = app.get('/descargar_datos_mascotas')
    assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
    
def test_descargar_datos_mascotas_incorrecto():
    """Test 3: intento fallido de descargar nuevos datos de mascotas porque
    no se ha realizado una conexión previamente con la API Petfinder."""
    mascotas.Mascotas.api_petifinder = None
    respuesta = app.get('/descargar_datos_mascotas')
    assert respuesta.status_code == 400

def test_anadir_nueva_organizacion():
    """Test 4: añadir una nueva organización."""
    respuesta = app.put('/aniadir_organizacion/org2/Granada/Espania')
    assert (respuesta.status_code == 200 and respuesta.headers["Content-Type"] == "application/json")
    
def test_anadir_nueva_organizacion_incorrecto():
    """Test 5: intento fallido de añadir una nueva organización.
        Al no proporcionarle los argumentos necesarios no encuentra la ruta
        y por lo tanto devuelve un código 404 NOT FOUND."""
    respuesta = app.put('/aniadir_organizacion/org2//')
    assert (respuesta.status_code == 404)