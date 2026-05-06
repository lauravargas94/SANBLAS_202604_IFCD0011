import csv

import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def generar_informe(nombres_columnas : list[str], nombre_fila : str, valores_numericos_columnas):
    nombre_fichero = f'matriculaciones_{nombre_fila}.pdf'
        
    # Creación del documento
    doc = SimpleDocTemplate(nombre_fichero)

    estilos = getSampleStyleSheet()

    contenido = [] # List con el contenido
    
    parrafo = Paragraph(f'{nombres_columnas[0].strip().capitalize()}:{nombre_fila}', estilos['Heading1'])
    contenido.append(parrafo)
    for registro in zip(nombres_columnas[1:], valores_numericos_columnas):
        parrafo = Paragraph(f'{registro[0].strip().capitalize()}:{registro[1]}', estilos['Normal'])
        contenido.append(parrafo)

    # Diagrama
    generar_diagrama(nombres_columnas, nombre_fila, valores_numericos_columnas)
    img = Image("./matriculaciones.png")
    img.drawWidth = 400
    img.drawHeight = 350
    contenido.append(img)

    # Construimos el documento
    doc.build(contenido)
   

def generar_diagrama(nombres_columnas, nombre_fila, valores_numericos_columnas):
    plt.bar(nombres_columnas[1:], valores_numericos_columnas)
    plt.title(f'Matriculaciones de {nombre_fila}')
    plt.xlabel('Mes')
    plt.ylabel('Unidades')
    plt.xticks(rotation=90) # Rota los textos del eje x en 90º
    plt.tight_layout() # Ajusta los márgenes
    plt.savefig('matriculaciones.png')
    plt.clf()

if __name__=='__main__':
    with open('matriculaciones.csv', mode='rt', encoding='utf-8-sig', newline='') as fichero:
        dictionary_data = csv.DictReader(fichero, delimiter=';')
        field_names = dictionary_data.fieldnames # Obtengo los nombres de las columnas
        for row in dictionary_data:
            nombres_columnas = list(row.keys())
            valores_columnas = list(row.values())
            valores_numericos_columnas = [int(valor.replace('.','')) for valor in valores_columnas[1:]]
            generar_informe(nombres_columnas, valores_columnas[0], valores_numericos_columnas)            
            break