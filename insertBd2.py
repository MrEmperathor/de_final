#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
import argparse
import shlex, subprocess
import pdb


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Mostrar información de depuración", action="store_true")
# parser.add_argument("-f", "--file", help="Nombre de archivo a procesar")
parser.add_argument("-i", "--id", help="Nombre del ID de la base de datos")
parser.add_argument("-d", "--tmdb", help="Nombre de id tmdb")
parser.add_argument("-t", "--tabla", help="Nombre de la tabla")
parser.add_argument("-b", "--base", help="Nombre de la base")
args = parser.parse_args()

# Aquí procesamos lo que se tiene que hacer con cada argumento
if args.verbose:
    print("depuración activada!!!")
    
if args.id:
    
    myId = args.id
    idDrive = args.tmdb
    tabla = args.tabla
    if args.base == "3":
        baseDatos = "breaky"
        print("esta es mi base",baseDatos)

        conexion1=mysql.connector.connect(host="localhost", user="root", passwd="9999zzzz", database=baseDatos)
    else:
        conexion1=mysql.connector.connect(host="localhost", user="root", passwd="9999zzzz", database="uploaddll")

    print("El nombre de archivo a procesar es myId: ", myId)
    print("El nombre de archivo a procesar es tmdb: ", idDrive)
    

    cursor1=conexion1.cursor()
    # cursor1.execute("delete from articulos where codigo=1")

    cursor1.execute("update pelis set "+tabla+"='"+idDrive+"' where id="+myId)
    conexion1.commit()
    # cursor1.execute("select id, nombre, calidad, idioma, TMDB, links, Backup, Embed, estado720, LVIP, LFREE, 7VIP, 7FREE from pelis")
    cursor1.execute("select id, Backup from pelis")
    # for fila in cursor1:
    #     print(fila)
    conexion1.close()
    