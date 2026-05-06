import pandas

# URL = 'https://fpaniaguapython.github.io/datos/datos_sin_cabecera.csv'
URL = 'https://fpaniaguapython.github.io/datos/datos_con_cabecera.csv'

# datos = pandas.read_csv(URL, header=None)
datos = pandas.read_csv(URL)
print(type(datos))
print(datos.head(10))
print(datos.info())
print(datos['T1'].mean())

