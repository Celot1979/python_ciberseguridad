#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
from bs4 import BeautifulSoup
def peticion(direccion):
    url = direccion
    cabecera = {'User-Agent':'Safari'}
    peticion = requests.get(url = url, headers=cabecera)
    print(peticion.text)
def main():
    direccion = input('Dirección de wordpress   ==>  ')
    peticion(direccion)
    
   

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("saliendo")
        exit()