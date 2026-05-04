# Leer un fichero
# Limpiar caracteres no alfabéticos y una lista de tokens
# Convertir los tokens a mayúsculas
# Convertir la lista de tokens en un conjunto
# Obtener el número de elementos del conjunto
import re

def leer_fichero(nombre_fichero: str) -> str:
    with open(nombre_fichero, mode='rt', encoding='utf-8') as fichero:
        texto = fichero.read()
    return texto

def obtener_tokens_spanish(texto: str) -> list[str]:
    pattern = r'[a-zA-ZáéíóúÁÉÍÓÚñÑ]+'
    tokens = re.findall(pattern, texto)
    return tokens

def convertir_tokens_a_mayusculas(tokens : list[str]) -> list[str]:
    tokens_mayusculas = [token.upper() for token in tokens]
    return tokens_mayusculas

def convertir_tokens_a_conjunto(tokens: list[str]) -> set[str]:
    conjunto = set(tokens)
    return conjunto

def obtener_numero_elementos(conjunto_tokens: set[str]) -> int:
    numero_elementos = len(conjunto_tokens)
    return numero_elementos

texto = leer_fichero('46_ejercicio_funciones.py')
tokens = obtener_tokens_spanish(texto)
tokens_mayusculas = convertir_tokens_a_mayusculas(tokens)
set_tokens = convertir_tokens_a_conjunto(tokens_mayusculas)
numero_elementos = obtener_numero_elementos(set_tokens)

print(numero_elementos)


