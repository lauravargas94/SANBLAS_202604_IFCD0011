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

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

MESES = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio',
         'Agosto','Septiembre','Octubre','Noviembre','Diciembre')

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
            field_names = self.__dict__.keys() # Obtenemos los nombres de los atributos
            writer = csv.DictWriter(fichero, fieldnames=field_names)
            writer.writeheader() # Escribe el encabezado
            writer.writerow(self.__dict__) # Escribe los valores del diccionario

    def escribir_fichero_pdf(self):
        nombre_fichero = f"contrato_{self.nombre_casero.replace(' ','_')}_{self.nombre_inquilino.replace(' ','_')}.pdf"
        
        doc = SimpleDocTemplate(nombre_fichero)
        estilos = getSampleStyleSheet()
        
        contenido = []

        titulo = Paragraph(
            "MODELO ORIENTATIVO DE CONTRATO DE ARRENDAMIENTO DE VIVIENDA",
            estilos['Title']
        )
        contenido.append(titulo)

        fecha = f"En Madrid, a {self.fecha_inicio.day} de {MESES[self.fecha_inicio.month-1]} de {self.fecha_inicio.year}"
        contenido.append(Paragraph(fecha, estilos['Normal']))

        contenido.append(Paragraph("REUNIDOS", estilos['Heading2']))

        contenido.append(Spacer(1, 20))

        primer_parrafo = f"""
        De una parte, y como arrendador, persona física, D/Dña. {self.nombre_casero},
        mayor de edad, domiciliado/a en ………, y con NIF nº …….... Y con datos de contacto
        a efectos de notificaciones: correo electrónico: ……….........., y número de teléfono: ……
        """

        contenido.append(Paragraph(primer_parrafo, estilos['Normal']))

        contenido.append(Spacer(1, 20))


        segundo_parrafo = f"""
        De otra parte, y como arrendatario, D/Dña. {self.nombre_inquilino}, mayor de edad, con NIF…...., con
        domicilio a efectos de notificaciones en la vivienda objeto de arrendamiento. Y con datos de
        contacto a efectos de notificaciones: correo electrónico: ………........., y número de teléfono:…..

        """
        contenido.append(Paragraph(segundo_parrafo, estilos['Normal']))
        doc.build(contenido)

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

contrato.escribir_fichero_pdf()