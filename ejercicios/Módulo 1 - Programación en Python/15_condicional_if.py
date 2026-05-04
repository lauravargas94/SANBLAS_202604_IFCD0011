EDAD_JUBILACION = 67
MAYORIA_EDAD = 18
edad = 15

# Averiguar si es mayor de edad
if edad >= MAYORIA_EDAD:
    print('Es mayor de edad')
else:
    print('Es menor de edad')

# Averiguar si está en edad de jubilación o es mayor de edad
if edad >= EDAD_JUBILACION:
    print('Está en edad de jubilación')
elif edad >= MAYORIA_EDAD:
    print('Es mayor de edad')
else:
    print('Es menor de edad')

# Averiguar si es mayor de edad y si está en edad de jubilación
if (edad >= MAYORIA_EDAD):
    print('Es mayor de edad')
    if (edad >= EDAD_JUBILACION):
        print('Está en edad de jubilación')
else:
    print('Es menor de edad')

# Un if con evaluaciones diversas
if (edad >= MAYORIA_EDAD) and (edad >= EDAD_JUBILACION):
    print('Es mayor de edad y está en edad de jubilación')
else:
    print('Es menor de edad y no está en edad de jubilación')
