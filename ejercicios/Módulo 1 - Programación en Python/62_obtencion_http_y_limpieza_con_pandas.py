import pandas

URL_SIN_CABECERA = 'https://fpaniaguapython.github.io/datos/datos_sin_cabecera.csv'
URL_CON_CABECERA = 'https://fpaniaguapython.github.io/datos/datos_con_cabecera.csv'
# FICHERO = 'matriculaciones.csv'

# datos = pandas.read_csv(URL_SIN_CABECERA, header=None)
datos = pandas.read_csv(URL_CON_CABECERA)
# datos = pandas.read_csv(FICHERO, sep=';')

#print(datos.info()) # Información del DF
#print(datos.shape)  # Dimensiones del DF
print(datos.head()) # 5 primeros registros
#print(datos.tail()) # 5 últimos registros