import csv

import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image

class Facturacion:
    def __init__(self, anyo, facturacion_t1 : float, facturacion_t2 : float, facturacion_t3 : float, facturacion_t4 : float) -> None:
        self.anyo = anyo
        self.facturacion_t1 = facturacion_t1
        self.facturacion_t2 = facturacion_t2
        self.facturacion_t3 = facturacion_t3
        self.facturacion_t4 = facturacion_t4

    def generar_informe_pdf(self):
        nombre_fichero = f'informe_facturacion_{self.anyo}.pdf'
        
        # Creación del documento
        doc = SimpleDocTemplate(nombre_fichero)
        contenido = [] # List con el contenido
        
        # Texto
        trimestre_1 = Paragraph(f'Facturación T1: {self.facturacion_t1}')
        contenido.append(trimestre_1)

        contenido.append(Spacer(1, 20)) # Espacio en blanco

        trimestre_2 = Paragraph(f'Facturación T2: {self.facturacion_t2}')
        contenido.append(trimestre_2)

        contenido.append(Spacer(1, 20)) # Espacio en blanco

        trimestre_3 = Paragraph(f'Facturación T3: {self.facturacion_t3}')
        contenido.append(trimestre_3)

        contenido.append(Spacer(1, 20)) # Espacio en blanco

        trimestre_4 = Paragraph(f'Facturación T4: {self.facturacion_t4}')
        contenido.append(trimestre_4)
        
        # Diagrama
        self.generar_diagrama_barras()
        img = Image("./figura.png")
        img.drawWidth = 200
        img.drawHeight = 150
        contenido.append(img)

        # Construimos el documento
        doc.build(contenido)

    def generar_diagrama_barras(self):
        plt.bar(['T1','T2','T3','T4'], [self.facturacion_t1, self.facturacion_t2, self.facturacion_t3, self.facturacion_t4])
        plt.title(f'Facturación {self.anyo}')
        plt.xlabel('Trimestre')
        plt.ylabel('Facturación (€)')
        plt.savefig('figura.png')
        plt.clf() # Borra la figura para no dibujar encima en la siguiente iteracción

if __name__=='__main__':
    # Abrimos el fichero csv
    with open('58_facturacion.csv', mode='rt', encoding='utf-8', newline='') as fichero:
        # Creamos una instancia de DictReader con el fichero
        data = csv.DictReader(fichero)
        # Recorremos los 'registros' del DictReader
        for row in data:
            # Accedemos a los valores de las claves (son las cabeceras del fichero)
            print(row['año'],row['t1'],row['t2'],row['t3'],row['t4'])
            facturacion = Facturacion(row['año'],float(row['t1']),float(row['t2']),float(row['t3']),float(row['t4']))
            #facturacion.generar_diagrama_barras()
            facturacion.generar_informe_pdf()
