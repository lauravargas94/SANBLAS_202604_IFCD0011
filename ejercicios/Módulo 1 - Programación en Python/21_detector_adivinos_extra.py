# 1. Generar un número entero aleatorio entre 1 y 9
# 2. Pedir al usuario un número entre 1 y 9
# 3. Comprobar si ha acertado; si no acierta pedimos otro número
# EXTRA POINT
# 4. Establecer un número de intentos para determinar si el adivino es 
# un adivino o un fraude

import random

NUMERO_MINIMO = 1
NUMERO_MAXIMO = 9
NUMERO_MAXIMO_INTENTOS = 3

# PASO 1
NUMERO_SECRETO = random.randint(NUMERO_MINIMO, NUMERO_MAXIMO)
numero_candidato=-1
numero_intentos=0
while (numero_candidato!=NUMERO_SECRETO):
    numero_intentos+=1 # Incrementamos en 1 el contador de intentos
    if (numero_intentos>NUMERO_MAXIMO_INTENTOS):
        print('ERES UN FRAUDE')
        break
    # PASO 2
    numero_candidato = int(input(f'Introduce un número candidato[{NUMERO_MINIMO}-{NUMERO_MAXIMO}]:'))
    # PASO 3
    if (numero_candidato==NUMERO_SECRETO):
        print('HAS ACERTADO')
    else:
        print('HAS FALLADO')
else:
    # Sólo se ejecuta si la condición del while no se cumple
    # NO se ejecuta si se hace un break
    print('ERES UN ADIVINO')