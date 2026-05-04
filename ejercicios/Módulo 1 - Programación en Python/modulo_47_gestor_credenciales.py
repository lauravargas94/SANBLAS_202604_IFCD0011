import hashlib
import hmac

def _obtener_nombre_fichero(email : str) -> str:
    """
    Genera el nombre del fichero.

    :param email: dirección de correo electrónico
    :return: el nombre del fichero
    """
    EXTENSION = '.credentials'
    nombre_fichero = email + EXTENSION
    return nombre_fichero


def _obtener_hash_sha256(texto:str) -> bytes:
    """
    Proporciona un hash utilizando el algoritmo SHA256.
    
    :param texto: texto a convertir
    :return: el hash del texto 
    """
    implementacion = hashlib.sha256()
    implementacion.update(texto.encode('utf-8'))
    hash = implementacion.digest()
    return hash


def guardar_credenciales(email:str, password_en_claro:str):
    """
    Guarda el hash de la contraseña en un fichero.
    
    :param email: email de la credencial
    :param password_en_claro: contraseña de la credencial
    """
    nombre_fichero = _obtener_nombre_fichero(email)
    hash = _obtener_hash_sha256(password_en_claro)
    with open(nombre_fichero, mode='wb') as fichero:
        fichero.write(hash)


def validar_credenciales(email:str, password_en_claro:str) -> bool:
    """ 
    Comprueba si las credenciales son correctas.

    Params:
    - email: la dirección de correo de las credenciales
    - password_en_claro: la contraseña en claro

    Return:
    True si las credenciales son correctas o False en caso contrario.
    """
    nombre_fichero = _obtener_nombre_fichero(email)
    with open(nombre_fichero, mode='rb') as fichero:
        hash_almacenado = fichero.read()
    hash_introducido = _obtener_hash_sha256(password_en_claro)
    if hmac.compare_digest(hash_almacenado, hash_introducido):
        return True
    else:
        return False