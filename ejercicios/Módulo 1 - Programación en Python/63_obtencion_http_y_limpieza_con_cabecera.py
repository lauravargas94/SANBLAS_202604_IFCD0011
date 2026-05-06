import csv

import requests

URL = 'https://fpaniaguapython.github.io/datos/datos_con_cabecera.csv'

def get_data_from_url(URL) -> str:
    """Obtiene el texto proporcionado por una URL"""
    response = requests.get(URL)
    if response.status_code==200:
        contenido = response.text
        return contenido
    else:
        raise Exception('Ha ocurrido un error con STATUS CODE:', response.status_code)

def guardar_csv(nombre_fichero, datos):
    with open(nombre_fichero, mode='w', encoding='utf-8') as fichero:
        fichero.write(datos)

if __name__=='__main__':
    # Obtención de los datos
    datos = get_data_from_url(URL)
    # Almacenamiento en un fichero csv
    guardar_csv('datos_sin_cabecera.csv', datos)
    # Lectura del fichero
    lista = []
    with open('datos_sin_cabecera.csv', mode='rt', encoding='utf-8', newline='') as fichero:
        datos = csv.DictReader(fichero, delimiter=',')
        for dato in datos:
            diccionario = dict()
            for k,v in dato.items():
                diccionario[k]=int(v)
            lista.append(diccionario)
    print(lista)

