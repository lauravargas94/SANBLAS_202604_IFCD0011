nombre_fichero = input('Introduce un nombre de fichero:')

try:
    with open(nombre_fichero, mode='rt', encoding='utf-8') as fichero:
        contenido = fichero.read()
        print(contenido)
except FileNotFoundError as fnfe:
    print('Ha ocurrido un error. El fichero no existe.')
    #print(fnfe)