import sqlite3

import pandas as pd

conn = sqlite3.connect('db_empleados_optimizado.sqlite3')

# df = pd.read_sql_query('SELECT * FROM empleados', conn) # Todos los campos de todos los registros
# df = pd.read_sql_query('SELECT id, categoria_programacion, ciudad, salario FROM empleados', conn) # Obtenemos solo algunos campos
# df = pd.read_sql_query('SELECT categoria_programacion, salario FROM empleados WHERE ciudad="Madrid"', conn)
# Empleados de Madrid que cobren más de 30_000
# Empleados de Madrid que sean Científico de Datos
# Empleados de Madrid y de Barcelona que sean DevOps Engineer
# Empleados que sean DevOps Engineer y que cobren menos de 30_000
print(df.info())
print(df.head())
print(df.tail())

conn.close()