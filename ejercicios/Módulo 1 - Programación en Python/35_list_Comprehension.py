lista_numeros = [2, -2, 10, 8, 4]
lista_palabras = ['Pizza', 'Brócoli', 'Lechuga', 'tomate', 'pera']

nueva_lista = [numero*4 for numero in lista_numeros]
print(nueva_lista) # [8, -8, 40, 32, 16]

nueva_lista = [palabra.upper() for palabra in lista_palabras]
print(nueva_lista) # ['PIZZA', 'BRÓCOLI', 'LECHUGA', 'TOMATE', 'PERA']

nueva_lista = [len(palabra) for palabra in lista_palabras]
print(nueva_lista) # [5, 7, 7, 6, 4]

nueva_lista = [0 for palabra in lista_palabras]
print(nueva_lista) # [0, 0, 0, 0, 0]

nueva_lista = [len(palabra)>5 for palabra in lista_palabras]
print(nueva_lista) #[False, True, True, True, False]

# Nueva lista con la lista de palabras traducida al inglés
def traducir(palabra):
    return (palabra+'traducida')

nueva_lista = [traducir(palabra) for palabra in lista_palabras]
print(nueva_lista) # ['Pizzatraducida', 'Brócolitraducida', 'Lechugatraducida', 'tomatetraducida', 'peratraducida']

# Crear una nueva lista a partir de lista_numeros 
# incrementando cada número en 100 unidades
nueva_lista = [(numero+100) for numero in lista_numeros]
print(nueva_lista)

# Limpiar espacios
lista_palabras = ['   Pizza   ', '  Brócoli   ', '   Lechuga  ', '  tomate  ', 'pera  ']
nueva_lista = [palabra.strip() for palabra in lista_palabras]
print(nueva_lista)

# Limpiar espacios y quitar # y unificar las mayúsculas
lista_palabras = ['   Pizza  # ', '  Bró#coli   ', '   Lec#huga  ', '  to#mate  ', 'pe#ra  ']
nueva_lista = [palabra.replace('#','').strip().capitalize() for palabra in lista_palabras]
print(nueva_lista)

# Obtener una lista con los nombres de los alumnos
# Obtener una tupla con las edades de los alumnos
alumnos = (('Mario', 54), ('Carlos', 35), ('Nayra', 45), ('Michelle', 26), ('Hani', 36), ('Pablo', 20))

nueva_lista = [alumno[0] for alumno in alumnos]
print(nueva_lista) # ['Mario', 'Carlos', 'Nayra', 'Michelle', 'Hani', 'Pablo']

nueva_lista = [alumno[0] for alumno in alumnos if alumno[1]>40]
print(nueva_lista) # ['Mario', 'Nayra']