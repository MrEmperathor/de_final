#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mega import Mega
import argparse


mega = Mega()
contra = 'Pelish242019'
file_cuentas_mega = '/var/local/backup_mega.txt'

class Cliente_mega:
    
    def __init__(self, correo, password, file):
        # user details
        self.email = correo
        self.password = password
        self.file = file
        # login
        self.m = mega.login(self.email, self.password)
    
    def mimega_login(self):
        
        self.details = self.m.get_user()
        print(self.details)
        
        
    def mimega_upload(self):
        # # upload file
        self.up_file = self.m.upload(self.file)
        
    
    def mimega_link(self, fil):
        #link
        if fil:
            return self.m.get_upload_link(fil)
        else:
            return self.m.get_upload_link(self.up_file)
        
        
    def mimega_import_link(self, link):
        return self.m.import_public_url(link)

    
    def mimega_quota(self):
        quota = self.m.get_quota()
        print(quota)
        
    
    def mimega_space(self):
        space = self.m.get_storage_space(mega=True)
        return space




lineas = list()
with open(file_cuentas_mega, 'r') as f:
    lineas = [linea.split() for linea in f]
    # lineas = f.read()

cuentas_llenas = list()
for i in lineas:
    
    c = Cliente_mega(i[0], contra, 'aaaa.txt')
    espacio_json = c.mimega_space()
    # print(espacio_json)
    if espacio_json["used"] >= 50000:
        # print('CUENTA LLENA')
        cuenta_llena = True
        cuentas_llenas.append(i[0])
    else:
        # print('CUENTA NUEVA')
        user = i[0]
        break

# ELIMINAR CUENTAS LLENAS
if 'cuenta_llena' in globals():
    f = open(file_cuentas_mega, "r")
    lineass = f.readlines()
    f.close()
    for i_linea in cuentas_llenas:
        lineass.remove(i_linea+'\n')
        
    f = open(file_cuentas_mega, "w")
    for linea in lineass:
        f.write(linea)
    f.close()

        

def link_m():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="Mostrar información de depuración", action="store_true")
    parser.add_argument("-i", "--id", help="Nombre de archivo a procesar")
    parser.add_argument("-l", "--link", help="link de mega")
    args = parser.parse_args()

    if args.link:
        id_db = args.id
        cliente = Cliente_mega(user, contra, 'aaaa.txt')
        fil = cliente.mimega_import_link(args.link)
        link = cliente.mimega_link(fil)
        return link
print(link_m())
    
    