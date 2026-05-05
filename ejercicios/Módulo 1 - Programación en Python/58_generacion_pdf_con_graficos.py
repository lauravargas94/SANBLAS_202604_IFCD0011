import csv

class Facturacion:
    def __init__(self, anyo, facturacion_t1, facturacion_t2, facturacion_t3, facturacion_t4) -> None:
        self.anyo = anyo
        self.facturacion_t1 = facturacion_t1
        self.facturacion_t2 = facturacion_t2
        self.facturacion_t3 = facturacion_t3
        self.facturacion_t4 = facturacion_t4

    def generar_informe_pdf(self):
        pass

    def generar_diagrama_barras(self):
        pass


if __name__=='__main__':
    # Abrimos el fichero csv
    with open('58_facturacion_simple.csv', mode='rt', encoding='utf-8', newline='') as fichero:
        # Creamos una instancia de DictReader con el fichero
        data = csv.DictReader(fichero)
        # Recorremos los 'registros' del DictReader
        for row in data:
            # Accedemos a los valores de las claves (son las cabeceras del fichero)
            print(row['año'],row['t1'],row['t2'],row['t3'],row['t4'])
