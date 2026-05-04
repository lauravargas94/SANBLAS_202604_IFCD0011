def sumar(numero_1 : int, numero_2 : int, numero_3=0) -> int:
    return numero_1 + numero_2 + numero_3

sumar(5, 8)
sumar(5, 8, 10)

def saludar(nombre='Ramón', idioma='Inglés'):
    print(f'Hola en {idioma}, {nombre}')

saludar('Nayra', 'Chino')
saludar('Nayra')
saludar()
saludar(idioma='Alemán', nombre='Pedro')

def multiplicar(*numeros):
    print(type(numeros)) # Tupla
    print(numeros) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    resultado = 1
    for numero in numeros:
        resultado*=numero
    return resultado

resultado = multiplicar(1,2,3,4,5,6,7,8,9,10)
print(resultado)

def super_suma(*numeros : tuple[int], offset=10):
    resultado = sum(numeros) + offset
    return resultado

resultado = super_suma(2,2,2) # 16
print(resultado)
resultado = super_suma(2,2,2,offset=5) # 11
print(resultado)
# resultado = super_suma(offset=6, 2,2,2) # Error

def ultra_suma(offset=10, *numeros : tuple[int]):
    print('offset:',offset)
    resultado = sum(numeros) + offset
    return resultado

resultado = ultra_suma(1,2,3) # Asigna el 1 al offset
print(resultado) # 6
resultado = ultra_suma()
print(resultado) # Es el único caso en el que el offset toma el valor por defecto