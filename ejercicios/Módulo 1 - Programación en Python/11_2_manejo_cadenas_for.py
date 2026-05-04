import unicodedata

FILE_NAME = 'C:/Users/Profesormanana/Documents/el_quijote.txt'
# Opción 'tradicional'
# fichero = open(FILE_NAME, mode='rt', encoding='utf-8')
# texto = fichero.read()
# fichero.close()

# Opción 'with'
with open(FILE_NAME, mode='rt', encoding='utf-8') as fichero:
    texto = fichero.read()

texto = unicodedata.normalize('NFC', texto)

print(f'Longitud:{len(texto)}')#48851

# Replace
caracteres_a_eliminar = ':,.();¿?¡!&%#@'
texto_limpio = texto
for caracter in caracteres_a_eliminar:
    texto_limpio = texto_limpio.replace(caracter, ' ')

# Convertir a mayúsculas
texto_limpio = texto_limpio.upper()

# Obtención de las palabras
tokens = texto_limpio.split() # Devuelve una lista
print(f'Número de palabras:{len(tokens)}')

# Obtención de las palabras distintas
set_tokens = set(tokens)
print(f'Número de palabras distintas:{len(set_tokens)}')#2216

#
# Preguntar al usuario (input) por una palabra e indicar 
# si existe en el texto o no (operador in)
# 

palabra = input('Introduce una palabra:')
palabra=palabra.strip().upper()

if palabra in set_tokens:
    print('La palabra existe')
else:
    print('La palabra no existe')


# Escribir el fichero limpio
CLEAR_FILE_NAME = 'C:/Users/Profesormanana/Documents/texto_limpio.txt'
with open(CLEAR_FILE_NAME, mode='w', encoding='utf-8') as fichero:
    fichero.write(texto_limpio)


#print(texto)