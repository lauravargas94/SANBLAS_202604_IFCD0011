import pandas as pd

df = pd.read_csv('http://fpaniaguapython.github.io/datos/encuesta_poblacion.csv')

print(df.index)
df.index=['Indice'+str(indice) for indice in df.index]
print(df)