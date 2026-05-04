# Lectura línea a línea
with open('22_bucle_for.py',mode='rt',encoding='utf-8') as fichero:
    for linea in fichero:
        # Opción 1 - Elimino los saltos de línea
        linea = linea.replace('\n','')
        print(linea)
        # Opción 2 - Quitamos el salto de línea del print
        # print(linea, end='')

# Lectura carácter a carácter
with open('22_bucle_for.py',mode='rt',encoding='utf-8') as fichero:
    for caracter in fichero.read():
        print(caracter)        