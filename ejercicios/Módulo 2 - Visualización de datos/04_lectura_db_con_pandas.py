import sqlite3

import pandas as pd

conn = sqlite3.connect('db_empleados_optimizado.sqlite3')

# df = pd.read_sql_query('SELECT * FROM empleados', conn) # Todos los campos de todos los registros
# df = pd.read_sql_query('SELECT id, categoria_programacion, ciudad, salario FROM empleados', conn) # Obtenemos solo algunos campos
# df = pd.read_sql_query('SELECT categoria_programacion, salario FROM empleados WHERE ciudad="Madrid"', conn)

# Empleados de Madrid que cobren más de 30_000
# df = pd.read_sql_query('SELECT id as identificador, categoria_programacion, salario FROM empleados WHERE ciudad="Madrid" AND salario>30000', conn)

# Empleados de Madrid que sean Científico de Datos
# df = pd.read_sql_query('SELECT * FROM empleados WHERE ciudad="Madrid" AND categoria_programacion="Científico de Datos"', conn)

# Empleados de Madrid que sean desarrolladores (da igual de front o de back)
# df = pd.read_sql_query('SELECT * FROM empleados WHERE ciudad="Madrid" AND categoria_programacion LIKE "%Desarrollador%"', conn)

# Empleados de Madrid o de Barcelona que sean DevOps Engineer
# df = pd.read_sql_query('SELECT * FROM empleados WHERE (ciudad="Madrid" OR ciudad="Barcelona") AND categoria_programacion="DevOps Engineer"', conn)

# Empleados que sean DevOps Engineer y que cobren menos de 30_000
df = pd.read_sql_query('SELECT * FROM empleados WHERE categoria_programacion="DevOps Engineer" AND salario<30000', conn)

print(df.info())
print(df.head())
print(df.tail())

conn.close()