# Generar una lista con tuplas con las siguiente estructura
# (año (int), mes(int), facturacion (int), ciudad (homogeneizada))
# Algunas líneas tienen espacios en blanco al final

with open('facturacion.csv',encoding='utf-8') as facturacion:
    todo = [
        (
        fila.split(',')[0], 
        fila.split(',')[3].capitalize()
        ) 
        for fila in facturacion]

pass
