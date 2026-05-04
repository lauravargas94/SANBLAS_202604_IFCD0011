# 1. Crear una lista vacía
lista_vacia = []

# 2. Crear una lista con las estaciones del año (no poner el verano ni el invierno)
estaciones = ['Primavera', 'Otoño']

# 3. Crear una lista vacía con la función list
lista_vacia = list()

# 4. Crear una lista con las estaciones del año en MAYÚSCULAS
# utilizando la lista del punto 2
estaciones_mayusculas = [estacion.upper() for estacion in estaciones]

# 5. Añadir el invierno con el método append.
estaciones.append('Invierno')

# 6. Añadir el verano con el método insert.
estaciones.insert(1, 'Verano')

# 7. Añadir la estación 'Atocha'
estaciones.append('Atocha')

# 8. Averiguar si existe 'Atocha' en la lista
tiene_atocha = 'Atocha' in estaciones
print(tiene_atocha)

# 9. Borrar la estación 'Atocha' con la sentencia del
del estaciones[-1] # Borrado por índice
# estaciones.remove('Atocha') # Borrado por contenido

# 10. Obtener una lista ordenada de las estaciones
estaciones_ordenadas = sorted(estaciones)

# 11. Ordenar la lista.
estaciones.sort()
pass

#12. Extend --> Concatena listas
lista_1 = ['Hola', 'Buenos días']
lista_2 = ['Buenas tardes', 'Buenas noches']
tupla_1 = tuple(lista_1)
tupla_2 = tuple(lista_2)
print(lista_1+lista_2) # ['Hola', 'Buenos días', 'Buenas tardes', 'Buenas noches']
print(tupla_1+tupla_2) # ('Hola', 'Buenos días', 'Buenas tardes', 'Buenas noches')
# print(lista_1+tupla_2) # Error. El operador + solo funciona con elementos del mismo tipo (simplificando)
lista_1.extend(lista_2)
print(lista_1) # ['Hola', 'Buenos días', 'Buenas tardes', 'Buenas noches']
lista_1.extend(tupla_2)
print(lista_1) # ['Hola', 'Buenos días', 'Buenas tardes', 'Buenas noches', 'Buenas tardes', 'Buenas noches']
lista_1.extend(['Hasta luego, Lucas'])
print(lista_1) # ['Hola', 'Buenos días', 'Buenas tardes', 'Buenas noches', 'Buenas tardes', 'Buenas noches', 'Hasta luego, Lucas']

# 13. Index
posicion = lista_1.index('Buenos días')
print(posicion) # 1

# 14. count
print(lista_1.count('Hola')) # 1
print(lista_1.count('Jelou')) # 0

# 15. reverse y pop
tareas = ['Tarea 1', 'Tarea 2', 'Tarea 3', 'Tarea 4']
tareas.reverse() # Invierte el orden
print(tareas) # ['Tarea 4', 'Tarea 3', 'Tarea 2', 'Tarea 1']
ultima_tarea = tareas.pop() 
print(ultima_tarea) # Tarea 1
print(tareas) # ['Tarea 4', 'Tarea 3', 'Tarea 2']