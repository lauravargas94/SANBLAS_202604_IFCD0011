print('LA CALCULADORA MUNDIAL')

try:
    numero = int(input('Número entero positivo:'))
    resultado = 100 / numero
    print(resultado)
except:
    print('Ha pasado algo muy malo pero no sé qué es')

try:
    numero = int(input('Número entero positivo:'))
    resultado = 100 / numero
    print(resultado)
except ValueError as ve:
    print('Error. Debe introducir un número entero')   
except ZeroDivisionError as zde:
    print('Error: El número entero debe ser distinto de 0') 
except BaseException as e:
    print('Error: Ha ocurrido un error desconocido')