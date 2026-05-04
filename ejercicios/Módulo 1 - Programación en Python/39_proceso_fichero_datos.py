# Generar una lista con tuplas con las siguiente estructura
# (año (int), mes(int), facturacion (int), ciudad (homogeneizada))
# Algunas líneas tienen espacios en blanco al final

# TODOS LOS DATOS
with open('facturacion.csv',encoding='utf-8') as facturacion:
    todo = [
        (
        int(fila.split(',')[0]), 
        int(fila.split(',')[1]),
        int(fila.split(',')[2].replace('*','')),
        fila.split(',')[3].capitalize().strip()
        ) 
        for fila in facturacion]
pass

# SOLO TOLEDO
with open('facturacion.csv',encoding='utf-8') as facturacion:
    solo_toledo = [
        (
        int(fila.split(',')[0]), 
        int(fila.split(',')[1]),
        int(fila.split(',')[2].replace('*','')),
        fila.split(',')[3].capitalize().strip()
        ) 
        for fila in facturacion 
        if fila.split(',')[3].capitalize().strip()=='Toledo']
pass

# FACTURACION > 5000
with open('facturacion.csv',encoding='utf-8') as facturacion:
    solo_mayor_5000 = [
        (
        int(fila.split(',')[0]), 
        int(fila.split(',')[1]),
        int(fila.split(',')[2].replace('*','')),
        fila.split(',')[3].capitalize().strip()
        ) 
        for fila in facturacion 
        if int(fila.split(',')[2].replace('*','')) > 5000]
    
pass