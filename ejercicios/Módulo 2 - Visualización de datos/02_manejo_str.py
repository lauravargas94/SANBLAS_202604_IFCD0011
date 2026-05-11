import pandas as pd

df = pd.read_csv('http://fpaniaguapython.github.io/datos/encuesta_poblacion.csv')

df['GÉNERO']=df['Género'].str.upper()
print(df)