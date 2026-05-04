diccionario_registros = dict()
with open('peliculas.txt', mode='rt', encoding='utf-8') as fichero:
    for registro in fichero:
        registro = registro.strip() # Eliminamos espacios y \n
        lista_campos = registro.split(',') # Obtenemos una lista con los campos del registro
        print(lista_campos)
        diccionario_registros[(lista_campos[1][:-7]).upper()]=lista_campos

pelicula = input('DIME QUÉ PELÍCULA QUIERES:')
print(diccionario_registros[pelicula.upper()])