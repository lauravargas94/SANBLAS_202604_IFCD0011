import csv

# Lectura 'tradicional'
with open('peliculas.txt', mode='rt', encoding='utf-8') as fichero:
    for registro in fichero:
        registro = registro.strip()
        lista_campos = registro.split(',')
        print(lista_campos)

# Lectura con el módulo csv
with open('peliculas.txt', mode='rt', encoding='utf-8') as fichero:
    csvreader = csv.reader(fichero) # No hace falta split
    for lista_datos in csvreader:
        print(lista_datos)