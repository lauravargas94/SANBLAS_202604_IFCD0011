def sumar(numero_1:int , numero_2:int) -> int:
    resultado = numero_1+numero_2
    return resultado

def restar(numero_1:float, numero_2:float) -> float:
    resultado = numero_1-numero_2
    return resultado

# Calcular el área de un cuadrado
def calcular_area_cuadrado(longitud_lado : float) -> float:
    area = longitud_lado ** 2
    return area

# Calcular la hipotenusa de un triángulo rectángulo
def calcular_hipotenusa(base: float, altura: float) -> float:
    hipotenusa_cuadrado  = (base ** 2) + (altura ** 2)
    hipotenusa = hipotenusa_cuadrado ** 0.5
    return hipotenusa

# Calcular el IMC
def calcular_imc(peso:float, altura:float) -> float:
    """Calculo del Índice de masa corporal.

    Parámetros:
    - peso : Peso de la persona expresado en kilos.
    - altura : Altura de la persona expresada en metros.

    Retorno:
    - El IMC.
    """
    if (not isinstance(peso, float)):
        raise TypeError('El peso debe ser un float')
    if (not isinstance(altura, float)):
        raise TypeError('La altura debe ser un float')
    if (altura<=0):
        raise ValueError('La altura debe ser positiva')
    imc = peso/altura**2
    return imc

# Convierta una distancia en centímetros a pulgadas
def convertir_centimetros_a_pulgadas(centimetros : float) -> float:
    raise NotImplementedError('No está implementado')

print('Area de un cuadrado de 10 de lado:',calcular_area_cuadrado(10)) # 100
print('Hipotenusa de 10.1 (base), 3.8 (altura):', calcular_hipotenusa(10.1, 3.8)) # 10.79
print('IMC de 90kg y 1.70m:', calcular_imc(90.0, 1.7))