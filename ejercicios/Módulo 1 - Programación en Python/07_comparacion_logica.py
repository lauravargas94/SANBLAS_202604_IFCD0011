"""
Solicitar al usuario los siguientes datos:
- Nombre
- DNI
- email
- Edad

Comprobar:
- El nombre tiene una longitud > 5
- La longitud del DNI es 9 y el último carácter es una letra
(dni[-1:], ), método isalpha() 
- El email contiene una @  
'@' in email
- Es mayor de edad
"""
# Constantes
LONGITUD_MINIMA_NOMBRE = 6
LONGITUD_DNI = 9
MAYORIA_EDAD = 18

# Solicitamos los datos
nombre = input('Introduce tu nombre:')
dni = input('Introduce tu DNI:')
email = input('Introduce tu email:')
edad = int(input('Introduce tu edad:'))

nombre=nombre.strip()
dni=dni.strip()
email=email.strip()

# Verificar el tamaño del nombre
if (len(nombre) < LONGITUD_MINIMA_NOMBRE):
    print('ERROR: el nombre no tiene la longitud suficiente')
else:
    print('EL NOMBRE ES CORRECTO')

# Verificar el DNI (longitud y composición)
if (len(dni) != LONGITUD_DNI):
    #print('ERROR: la longitud del DNI debe ser ' + str(LONGITUD_DNI))
    #print('ERROR: la longitud del DNI debe ser', LONGITUD_DNI)
    print(f'ERROR: la longitud del DNI debe ser {LONGITUD_DNI}')
else:
    print('LA LONGITUD DEL DNI ES CORRECTA')

letra_dni = dni[-1:]
if (not letra_dni.isalpha()):
    print('Error: el DNI debe terminar en una letra')
else:
    print('EL DNI TERMINA EN LETRA')

# Verificar el EMAIL
if '@' not in email:
    print('Error: el EMAIL debe llevar una @')
else:
    print('EL EMAIL ESTÁ OK')

# VERIFICACIÓN MAYORÍA DE EDAD
if (edad<MAYORIA_EDAD):
    print('Error: debe ser mayor de edad')
else:
    print('ES MAYOR DE EDAD')