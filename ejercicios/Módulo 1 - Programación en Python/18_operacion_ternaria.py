IDIOMA_REQUERIDO = 'Inglés'
idiomas = ['Inglés', 'Polaco', 'Alemán']
sabe_ingles = None

# Método tradicional
if IDIOMA_REQUERIDO in idiomas:
    sabe_ingles = True
else:
    sabe_ingles = False

# Utilizando ternaria
sabe_ingles = True if IDIOMA_REQUERIDO in idiomas else False

# Utilizando el sentido común
sabe_ingles = IDIOMA_REQUERIDO in idiomas

# Dado un número y utilizando una expresión ternaria, 
# asigna el valor 'PAR' o 'IMPAR' a una variable 

numero = int(input('Introduce un número:'))
tipo = 'PAR' if numero%2==0 else 'IMPAR'
print(tipo)

