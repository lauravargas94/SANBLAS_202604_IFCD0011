alumnos = ['Esther', 'Aleksandra', 'Sara', 'Gerardo', 'Joselín', 'Alberto']
# Lista
for alumno in alumnos:
    print(alumno, end='*')
print()

# Tupla
alumnos = tuple(alumnos)    
for alumno in alumnos:
    print(alumno, end='+')
print()

# Conjunto
alumnos = set(alumnos)
for alumno in alumnos:
    print(alumno, end=':')
print()

#Diccionario
alumnos = {'Esther':('Inglés', 32, 'Madrid'),'Mario':('Alemán', 25, 'Berlín'), 'Joselín':('Mandarín', 63, 'Bogotá')}

for alumno in alumnos:
    print(alumno, end=':::') # Muestra las claves
print()

for alumno in alumnos.keys():
    print(alumno, end=';;;') # Muestra las claves
print()

for alumno in alumnos.values():
    print(alumno, end='===') # Muestra los valores
print()

for clave, valor in alumnos.items():
    print('Clave:',clave,'Valor:',valor) # Muestra claves y valores
print()

# A partir de un rango

for indice in range(10):
    print(indice, end='*') # 0*1*2*3*4*5*6*7*8*9*
print()

for numero in range(0,101,2):
    print(numero, end='-') # 0-2-4-6-8-10...100
print()