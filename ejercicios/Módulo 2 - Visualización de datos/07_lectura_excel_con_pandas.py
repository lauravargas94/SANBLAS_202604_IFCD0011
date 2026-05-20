import pandas as pd

#datos = pd.read_excel('Patrimonio_arquitectonico.xlsx') # Lee la primera hoja del archivo Excel y lo convierte en un DataFrame de pandas
#print(datos.info())

#datos = pd.read_excel('Patrimonio_arquitectonico.xlsx', sheet_name='Hoja2') # Lee la hoja llamada "Hoja2" del archivo Excel y lo convierte en un DataFrame de pandas
#print(datos.info())

#datos = pd.read_excel('Patrimonio_arquitectonico.xlsx', sheet_name=['Hoja1', 'Hoja2']) # Lee las hojas "Hoja1" y "Hoja2" del archivo Excel y lo convierte en un diccionario de DataFrames de pandas
#print(datos['Hoja1'].info())
#print(datos['Hoja2'].info())

#datos = pd.read_excel('Patrimonio_arquitectonico.xlsx', sheet_name=None) # Lee todas las hojas del archivo Excel y lo convierte en un diccionario de DataFrames de pandas
#print(datos.keys()) # Imprime las claves del diccionario, que corresponden a los nombres de las hojas del archivo Excel

datos = pd.read_excel('Patrimonio_arquitectonico.xlsx', sheet_name=1) # Lee la hoja "Hoja2" del archivo Excel y solo las columnas A, B y C, y lo convierte en un DataFrame de pandas
print(datos.info())
print(datos.head())