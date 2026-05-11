import pandas as pd

df = pd.read_csv('http://fpaniaguapython.github.io/datos/encuesta_poblacion.csv')
#Columnas originales
# ['Marca temporal', 'Nombre y apellidos', 'Género', 'Fecha de nacimiento', Altura', 'Peso', 'Número de hijos', 'Grado de felicidad']


# Renombrado manual
# df.columns = ['timestamp', 'nombre', 'genero', 'fecha', 'altura', 'peso', 'hijos', 'felicidad']

# Renombrado 'automático'
# Renombrar las columnas eliminando tildes, convirtiendo a minúsculas y sustituyendo espacios en blanco por _
# Ejemplo: 'Número de hijos' --> 'numero_de_hijos'

# Con comprensión de listas
#df.columns = [nombre_columna.lower().replace(' ','_') for nombre_columna in df.columns]
#print(df.columns)

# Directamente desde pandas
df.columns = df.columns.str.lower().str.replace(' ','_')
print(df.columns)

# Eliminación de tildes
df.columns = (df.columns
                .str.normalize('NFD')
                .str.encode('ascii',errors='ignore')
                .str.decode('utf-8'))
print(df.columns)