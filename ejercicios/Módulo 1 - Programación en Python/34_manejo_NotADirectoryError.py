import os

nombre_directorio = input('Introduce el nombre de la carpeta:')

try:
    contenido = os.listdir(nombre_directorio)
    print(contenido)
except NotADirectoryError as nade:
    print(nade)
except FileNotFoundError as fnfe:
    print(fnfe)
