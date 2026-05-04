"""
edad = 25
permiso_de_conducir = True
idiomas = ['Inglés', 'Chino', 'Polaco', 'Alemán']
lenguajes = ['Python', 'Java']
movilidad_geografica = False

Edad entre 20 y 30 años.
Debe tener permiso de conducir y movilidad geográfica.
Debe saber programar en Python
Debe tener conocimientos de Chino, pero no de Polaco.
"""
edad = 25
permiso_de_conducir = True
idiomas = ['Inglés', 'Chino', 'Polaco', 'Alemán']
lenguajes = ['Python', 'Java']
movilidad_geografica = False

EDAD_MINIMA = 20
EDAD_MAXIMA = 30
LENGUAJE_PROGRAMACION = 'Python'
IDIOMA_EXIGIDO = 'Chino'
IDIOMA_CANCELADO = 'Polaco'
if (edad>=EDAD_MINIMA and edad<=EDAD_MAXIMA) and (permiso_de_conducir==True) and (movilidad_geografica==True) and (LENGUAJE_PROGRAMACION in lenguajes) and (IDIOMA_EXIGIDO in idiomas) and (IDIOMA_CANCELADO not in idiomas):
    print('CONTRATADO')
else:
    print('YA TE LLAMAREMOS...')

edad_valida = (edad>=EDAD_MINIMA and edad<=EDAD_MAXIMA)
conoce_lenguaje = (LENGUAJE_PROGRAMACION in lenguajes)
cumple_idiomas = (IDIOMA_EXIGIDO in idiomas) and (IDIOMA_CANCELADO not in idiomas)

if edad_valida and permiso_de_conducir and movilidad_geografica and conoce_lenguaje and cumple_idiomas:
    print('CONTRATADO')
else:
    print('YA TE LLAMAREMOS...')