import csv

import matplotlib.pyplot as plt

if __name__=='__main__':
    with open('matriculaciones.csv', mode='rt', encoding='utf-8', newline='') as fichero:
        dictionary_data = csv.DictReader(fichero, delimiter=';')
        field_names = dictionary_data.fieldnames # Obtengo los nombres de las columnas
        for row in dictionary_data:
            nombres_columnas = list(row.keys())
            valores_columnas = list(row.values())
            valores_numericos_columnas = [int(valor.replace('.','')) for valor in valores_columnas[1:]]

            plt.bar(nombres_columnas[1:], valores_numericos_columnas)
            plt.title(f'Matriculaciones de {valores_columnas[0]}')
            plt.xlabel('Mes')
            plt.ylabel('Unidades')
            plt.show()
            break


            #for k, v in row.items():
            #    print(f'{k}:{v}***', end='')
            #break
            