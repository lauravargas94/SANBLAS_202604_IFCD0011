import re

def sumar(sumando_1 : int, sumando_2 : int) -> int:
    """Proporciona la suma de dos números enteros.

    Argumentos:
    - sumando_1 : Primer sumando.
    - sumando_2 : Segundo sumando.

    Retorno:
    Suma de los dos argumentos.
    """
    resultado = sumando_1 + sumando_2 # Asigna la suma a resultado
    return resultado

def validar_dni(dni):
    """Valida la estructura del número de DNI"""
    if not isinstance(dni, str):
        return False
    
    dni = dni.upper()
    # fullmatch busca encajar la regexp con el dni
    # r --> Significa raw string --> No procesa la cadena
    # \d{8}[A-Z] --> Empieza por 8 dígitos y termina en un 
    # carácter alfabético
    if not re.fullmatch(r"\d{8}[A-Z]", dni):
        return False

    # Verificamos que la letra final es la correcta   
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    numero = int(dni[:8])
     # dni[-1] obtiene el último carácter del DNI
    return dni[-1] == letras[numero % 23]

sumar()