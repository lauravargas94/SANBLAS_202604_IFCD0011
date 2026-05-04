# Crear un fichero de texto con palabras censurables
# Crear un fichero con el texto de un post

# Parte común
# Leer el fichero de palabras censurables
import re

with open('palabras_censurables.txt', mode='r', encoding='utf-8') as fichero:
    palabras_censuradas = [palabra.strip() for palabra in fichero]

with open('post.txt', mode='r', encoding='utf-8') as fichero:
    texto = fichero.read()
    texto = texto.replace('\n',' ')
    # Obtencion de los tokens
    pattern = r"[A-Za-záéíóúÁÉÍÓÚñÑ]+"
    palabras_del_post = re.findall(pattern=pattern, string=texto)

# Ejercicio 1. Construir un programa de censura de post
conjunto_palabras_censuradas = set(palabras_censuradas)
palabras_del_post = [palabra.lower() for palabra in palabras_del_post]
no_hay_palabras_censuradas = conjunto_palabras_censuradas.isdisjoint(palabras_del_post)
if no_hay_palabras_censuradas:
    print('CORRECTO')
else:
    print('CENSURA')

# Ejercicio 2. Construir un programa de censura de palabras
conjunto_palabras_censuradas = set(palabras_censuradas)
palabras_del_post = [palabra.lower() for palabra in palabras_del_post]
palabras_censuradas_encontradas = conjunto_palabras_censuradas.intersection(palabras_del_post)

texto_censurado = texto
for palabra_reemplazable in palabras_censuradas_encontradas:
    texto_censurado = re.sub(palabra_reemplazable, 
                             '*'*len(palabra_reemplazable), 
                             texto_censurado, 
                             flags=re.IGNORECASE)

print(texto_censurado)