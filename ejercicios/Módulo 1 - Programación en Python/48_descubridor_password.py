# Encuentra la password a partir de un hash SHA256
# comparando con un fichero de contraseñas más habituales
#
# Author: CHA

import hashlib

def cargar_contrasenyas(nombre_fichero: str) -> set[str]:
    """Obtiene un conjunto de hash de contraseñas almacenadas en un fichero
    Params:
    - nombre_fichero : Nombre del fichero (de texto) que almacena las contraseñas en distintas líneas.

    Return:
    - Conjunto de cadenas con los hash de las contraseñas
    """
    with open(nombre_fichero, "r", encoding="utf-8") as f:
        return {linea.strip() for linea in f if linea.strip()}


def obtener_hash_hexadecimal(texto: str) -> str:
    """Proporciona la versión hexadecimal de un hash que se encontraba en formato str

    Params:
    - texto : hash del password en formato str

    Return:
    Hash del password en hexadecimal
    """
    return hashlib.sha256(texto.encode()).hexdigest()


def obtener_hash_binario(texto: str) -> bytes:
    """
    Genera el hash SHA-256 de una contraseña en texto plano.

    Args:
        texto (str): Contraseña sin cifrar.

    Returns:
        Hash de la contraseña en formato bytes.
    """
    password_bytes = texto.encode("utf-8")
    return hashlib.sha256(password_bytes).digest()    

# busqueda por hexadecimal
def buscar_password_por_hash_hexadecimal(hash_objetivo: str, contrasenyas: set[str]) -> str | None:
    """
    Busca un hash dentro de un conjunto de contraseñas en claro.

    Params:
    - hash_objetivo : hash a buscar.
    - contrasenyas : conjunto de contraseñas en claro.
    
    Return:
        La contraseña en claro o None si no lo encuentra.
    """
    for password in contrasenyas:
        if obtener_hash_hexadecimal(password) == hash_objetivo:
            return password
    return None

def buscar_password_por_hash_binario(hash_objetivo: bytes , contrasenyas: set[str]) -> str | None:
    """
    Busca un hash dentro de un conjunto de contraseñas en claro.

    Params:
    - hash_objetivo : hash binario a buscar.
    - contrasenyas : conjunto de contraseñas en claro.
    
    Return:
        La contraseña en claro o None si no lo encuentra.
    """
    for password in contrasenyas:
        if obtener_hash_binario(password) == hash_objetivo:
            return password
    return None

# *************
# ---- USO ----
# *************

# para usar el fichero en colab hay que cargarlo antes.
conjunto_contrasenyas = cargar_contrasenyas("100k-most-used-passwords-NCSC.txt")

# b'e\xe8K\xe352\xfbxLH\x12\x96u\xf9\xef\xf3\xa6\x82\xb2qh\xc0\xeatK,\xf5\x8e\xe0#7\xc5'
hash_usuario_hex = input("Introduce el hash SHA-256: ").strip()
#hash_usuario_hex ="65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5"

resultado = buscar_password_por_hash_hexadecimal(hash_usuario_hex, conjunto_contrasenyas)

if resultado:
    print(f"Coincidencia encontrada: {resultado}")
else:
    print("No se encontró ninguna contraseña en la lista")

print(obtener_hash_hexadecimal('qwerty'))
# 65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5


print('********************************************')

hash_usuario_bin = bytes.fromhex(hash_usuario_hex)

resultado = buscar_password_por_hash_binario(hash_usuario_bin, conjunto_contrasenyas)



if resultado:
    print(f"Coincidencia encontrada: {resultado}")
else:
    print("No se encontró ninguna contraseña en la lista")



print(obtener_hash_binario('qwerty'))
# b'e\xe8K\xe352\xfbxLH\x12\x96u\xf9\xef\xf3\xa6\x82\xb2qh\xc0\xeatK,\xf5\x8e\xe0#7\xc5'

print('********************************************')


# para comparar con bytes mirar este codigo.
#import hmac
#hmac.compare_digest(hash_almacenado, hash_introducido)