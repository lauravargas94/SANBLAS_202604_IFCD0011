#Función que reemplaza un carácter por otro
def sustituir_caracter(texto : str, caracter : str, caracter_reemplazo : str) -> str:
    resultado = texto.replace(caracter, caracter_reemplazo)
    return resultado

resultado = sustituir_caracter('Me gusta la montaña', 'a', '@')
print(resultado)

#Función que reemplaza un texto por otro
def reemplezar_texto(texto_completo : str, parte_texto_original : str, parte_texto_nuevo : str):
    texto_completo = texto_completo.replace(parte_texto_original, parte_texto_nuevo)
    return texto_completo

texto_original = 'Me gusta la montaña'
resultado = reemplezar_texto(texto_original, 'montaña', 'playa')
print(resultado)

#Función que convierte un texto a mayúsculas
def convertir_mayusculas(texto: str):
    texto_en_mayusculas = texto.upper()
    return texto_en_mayusculas

resultado = convertir_mayusculas('Me gusta la montaña')
print(resultado)

#Función que convierte las 10 primeras posiciones de un texto a mayúsculas
def convertir_10_en_mayusculas(texto: str,) -> str:
    resultado = texto[:10].upper() + texto[10:] 
    return resultado

resultado = convertir_10_en_mayusculas('Me gusta la montaña')
print(resultado)

# Versión más versátil
def convertir_parcialmente_en_mayusculas(texto: str, numero_caracteres : int) -> str:
    resultado = texto[:numero_caracteres].upper() + texto[numero_caracteres:] 
    return resultado

resultado = convertir_parcialmente_en_mayusculas('Me gusta la montaña',4)
print(resultado)

#Función que suma 2 números
def sumar_dos_numeros(numero_1 : int, numero_2 : int) -> int: 
    return numero_1 + numero_2

resultado = sumar_dos_numeros(10,8)
print(resultado)

#Función que multiplica 2 números
def multiplicar_dos_numeros(numero_1:int, numero_2:int) ->int:
    return numero_1*numero_2

resultado = multiplicar_dos_numeros(10,3)
print(resultado)

#Función que invierte una cadena
def invertir_cadena(texto : str) -> str:
    return texto[::-1]
    
resultado = invertir_cadena('Me gusta la montaña')
print(resultado)

#Función que lee un fichero y devuelve el contenido en un str convertido a mayúsculas
def convertir_fichero_a_mayusculas(nombre_fichero):
    with open(nombre_fichero, mode='r', encoding='utf-8') as fichero:
        texto = fichero.read()
        resultado = texto.upper()
    return resultado

texto = convertir_fichero_a_mayusculas('45_ejercicio_funciones.py')
print(texto)

# Función que lee un fichero y devuelve una lista de str sin saltos de línea
def quitar_saltos_de_linea(nombre_fichero):
    with open(nombre_fichero, mode='r', encoding='utf-8') as fichero:
        lineas = fichero.readlines()
        lineas = [linea.strip() for linea in lineas]
    return lineas

resultado = quitar_saltos_de_linea('45_ejercicio_funciones.py')
print(resultado)

#Función que lee un fichero de números enteros y devuelve la suma
def sumar_numeros_fichero(nombre_archivo):
  total = 0

  with open(nombre_archivo) as fichero: # Abrimos archivo
    numeros = fichero.readlines()
  
  for numero in numeros:
      total+=int(numero)

  return total

resultado = sumar_numeros_fichero('datos_ejercicio_45.txt')
print(resultado)

#Función que lee un fichero de números enteros y devuelve el máximo
# **********************
# SOLUCIÓN 1
# **********************
# NO tiene en cuenta que no haya numneros en el fichero y pueda haber texto.
# NO contempla que vengan varios numeros en la misma linea.
def get_valor_maximo_from_fichero(nombre_fichero: str) -> int:
    with open(nombre_fichero, mode="rt", encoding="utf-8") as fichero:
         # Las dos siguientes (hay que elegir una) descartan líneas
         # en blanco. Las dos líneas son equivalentes
         # numeros = [int(linea.strip()) for linea in fichero if linea.strip()]
         # numeros = [int(linea.strip()) for linea in fichero if linea.strip()!='']
         numeros = [int(linea.strip()) for linea in fichero]
    return max(numeros)

print(get_valor_maximo_from_fichero("datos_ejercicio_45.txt"))

# **********************
# SOLUCIÓN 2
# **********************

# SI tiene en cuenta que no haya numneros en el fichero y pueda haber texto.
# SI contempla que vengan varios numeros en la misma linea.
import re

def get_maximo_from_fichero_optimizado(nombre_fichero: str) -> int:
    with open(nombre_fichero, mode="rt", encoding="utf-8") as fichero:
        # La re busca secuencias de dígitos numéricos
        numeros = [
            int(numero)
            for numero in re.findall(r"-?\d+", fichero.read())  # Busca todos los números dentro del texto que leemos.
        ]
    return max(numeros) if numeros else 0

print(get_maximo_from_fichero_optimizado("datos_ejercicio_45_con_caracteres.txt"))

#Función que lee un fichero de números enteros y devuelve el mínimo
def encontrar_minimo(nombre_fichero: str) -> int:
    with open(nombre_fichero, mode="r", encoding="utf-8") as fichero:
        numeros = [int(linea.strip()) for linea in fichero]
    return min(numeros)

print(encontrar_minimo('datos_ejercicio_45.txt'))

#Función que lee un fichero de números enteros y devuelve la media
def obtener_media_fichero(nombre_fichero : str):
    with open(nombre_fichero, mode='rt', encoding='utf-8') as fichero:
        numeros=[int(linea.strip()) for linea in fichero if linea.strip()]
        return sum(numeros) / len(numeros)
    
print(obtener_media_fichero('datos_ejercicio_45.txt'))

#Función que recibe una ciudad e indica si está en una lista de ciudades previa
ciudades = [
    "Madrid",
    "Barcelona",
    "París",
    "Londres",
    "Roma",
    "Berlín",
    "Lisboa",
    "Ámsterdam",
    "Nueva York",
    "Tokio"
]

def comprobar_ciudad(ciudad: str, lista_ciudades: list[str]) -> bool:
    resultado = ciudad in lista_ciudades
    return resultado

print(comprobar_ciudad('Madrid', ciudades))
print(comprobar_ciudad('Bogotá', ciudades))

#Función que indica si un número es par
def es_par(numero: int) -> bool:
    return numero % 2 == 0

print(es_par(4))
print(es_par(5))

#Función que calcula la media de una tupla
def calcular_media_tupla(tupla: tuple) -> int:
    suma = sum(tupla)
    resultado = suma // len(tupla)
    return resultado

tupla_ejemplo = (54, 64, 68, 8, 76)
print(calcular_media_tupla(tupla_ejemplo))

#Función que calcula la mediana de una tupla


#Función que calcula la moda de una tupla