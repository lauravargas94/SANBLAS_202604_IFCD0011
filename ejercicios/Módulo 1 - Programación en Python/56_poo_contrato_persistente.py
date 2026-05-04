"""
Clase contrato de alquiler de vivienda.
- Atributos:
Nombre del casero.
Nombre del inquilino.
Fecha de inicio.
Renta mensual.
Dirección del inmueble.
Duración del contrato (en meses).

- Métodos:
- Obtener el importe total del alquiler.
- Modificar duración del contrato (incrementando o decrementado meses).
- Escribir los datos del contrato a un fichero de texto
- Escribir los datos del contrato a un fichero csv
- Escribir el contrato en un documento PDF
"""
import datetime
import csv

class Contrato:
    def __init__(self, nombre_casero: str, nombre_inquilino: str, 
                 fecha_inicio: datetime.date, renta_mensual: int,
                 direccion_inmueble: str, duracion_contrato: int):
        self.nombre_casero = nombre_casero
        self.nombre_inquilino = nombre_inquilino
        self.fecha_inicio = fecha_inicio
        self.renta_mensual = renta_mensual
        self.direccion_inmueble = direccion_inmueble
        self.duracion_contrato = duracion_contrato

    def obtener_importe_total(self) -> int:
        return self.duracion_contrato*self.renta_mensual

    def modificar_duracion(self, duracion: int) -> None:
        self.duracion_contrato+=duracion

    def escribir_fichero_texto(self, nombre_fichero: str):
        """
        Author: Michelle
        """
        with open(nombre_fichero, mode='w', encoding='utf-8') as fichero_txt:
            # fichero_txt.write(str(self.__dict__)) # Guarda un diccionario. Opción a la solución 'Manual'
            fichero_txt.write(self.nombre_casero)
            fichero_txt.write('#')
            fichero_txt.write(self.nombre_inquilino)
            fichero_txt.write('#')
            fichero_txt.write(str(self.fecha_inicio))
            fichero_txt.write('#')
            fichero_txt.write(str(self.renta_mensual))
            fichero_txt.write('#')
            fichero_txt.write(self.direccion_inmueble)
            fichero_txt.write('#')
            fichero_txt.write(str(self.duracion_contrato))

    def escribir_fichero_csv(self, nombre_fichero: str):
        with open(nombre_fichero, 'w', newline='', encoding='utf-8') as fichero:
            field_names = self.__dict__.keys()
            writer = csv.DictWriter(fichero, fieldnames=field_names)
            writer.writeheader()
            writer.writerow(self.__dict__)

contrato = Contrato(nombre_casero='Alberto',
                    nombre_inquilino='Joselín', 
                    fecha_inicio=datetime.date(2026, 5, 4), 
                    renta_mensual=600, 
                    direccion_inmueble='Paseo de la Castellana, 85, Ático 3', 
                    duracion_contrato=60)

importe_total_contrato = contrato.obtener_importe_total()
print('Importe total:', importe_total_contrato)

contrato.modificar_duracion(24)

pass

contrato.escribir_fichero_texto('contrato_01.txt')

contrato.escribir_fichero_csv('contrato_01.csv')
