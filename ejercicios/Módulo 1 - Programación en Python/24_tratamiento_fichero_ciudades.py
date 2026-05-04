# ETAPA 1
# Leer el fichero ciudades.txt con un bucle for y mostrar los datos por pantalla.
input('PULSA ENTER PARA EJECUTAR LA ETAPA 1')

fichero = open('ciudades.txt', mode='rt', encoding='utf-8')
for registro in fichero:
    print(registro.replace('\n',''))
fichero.close() #¡OBLIGATORIO SI NO SE UTILIZA WITH!

# ETAPA 2
# Leer el fichero ciudades.txt con un bucle for y mostrar los datos por pantalla.
# Mostrar los datos sin separador
input('PULSA ENTER PARA EJECUTAR LA ETAPA 2')

with open('ciudades.txt', mode='rt', encoding='utf-8') as fichero:
    for registro in fichero:
        registro = registro.strip() # Elíminamos espacios y saltos de línea
        campos = registro.split('#') # Obtenemos los campos del registro
        print(f'CP:{campos[0]}. CIUDAD:{campos[1]}. RENTA:{campos[3]}')

# ETAPA 3
# Leer el fichero ciudades.txt con un bucle for y guardamos los datos
# una lista de tuplas
input('PULSA ENTER PARA EJECUTAR LA ETAPA 3')

lista_registros = []
with open('ciudades.txt', mode='rt', encoding='utf-8') as fichero:
    for registro in fichero:
        registro = registro.replace('\n','') # Eliminamos los saltos de línea
        registro = registro.strip() # Elíminamos los espacios en blanco de los extremos
        campos = registro.split('#') # Obtenemos una lista con los campos del registro
        campos = tuple(campos) # Obtenemos una tupla con los campos del registro
        lista_registros.append(campos)

# ETAPA 4
# Leer el fichero ciudades.txt con un bucle for y guardamos los datos
# en un diccionario en el que la clave es el nombre de la ciudad
input('PULSA ENTER PARA EJECUTAR LA ETAPA 4')

diccionario_registros = dict()
with open('ciudades.txt', mode='rt', encoding='utf-8') as fichero:
    for registro in fichero:
        registro = registro.replace('\n','') # Eliminamos los saltos de línea
        registro = registro.strip() # Elíminamos los espacios en blanco de los extremos
        campos = registro.split('#') # Obtenemos una lista con los campos del registro
        campos = tuple(campos) # Obtenemos una tupla con los campos del registro
        diccionario_registros[campos[1]]=campos

# ETAPA 5
# Programamos un sistema que nos pida el nombre de la ciudad y nos
# muestre sus datos

input('PULSA ENTER PARA EJECUTAR LA ETAPA 5')

diccionario_registros = dict()
with open('ciudades.txt', mode='rt', encoding='utf-8') as fichero:
    for registro in fichero:
        registro = registro.strip() # Elíminamos espacios y saltos de línea
        campos = registro.split('#') # Obtenemos una lista con los campos del registro
        campos = tuple(campos) # Obtenemos una tupla con los campos del registro
        diccionario_registros[campos[1]]=campos

ciudad = input('DIME QUÉ CIUDAD QUIERES:')
print(diccionario_registros[ciudad])