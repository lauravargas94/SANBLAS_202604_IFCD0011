# Asignación con tipos básicos copia los valores

x = 5
y = x # COPIANDO VALORES
print(x,y) # 5, 5
x = 7
print(x,y) # 7, 5

# Asignación con tipos 'complejos' como las listas
# copia las referencias en memoria

lista_x = [1, 2, 3]
lista_y = lista_x # COPIANDO REFERENCIAS
print("lista_x:", lista_x) # [1, 2, 3]
print("lista_y:", lista_y) # [1, 2, 3]
lista_x[0]=4
print("lista_x:", lista_x) # [4, 2, 3]
print("lista_y:", lista_y) # [4, 2, 3]

# Slicing hace una shallow copy (copia en el primer nivel)
# creando una nueva lista en el primer nivel

lista_x = [1, 2, 3]
lista_y = lista_x[:]
lista_x[0]=4
print("lista_x:", lista_x) # [4, 2, 3]
print("lista_y:", lista_y) # [1, 2, 3]

# Método copy hace una shallow copy (copia en el primer nivel)
# creando una nueva lista en el primer nivel
lista_x = [1, 2, 3]
lista_y = lista_x.copy()
lista_x[0]=4
print("lista_x:", lista_x) # [4, 2, 3]
print("lista_y:", lista_y) # [1, 2, 3]

# Método copy hace una shallow copy (copia en el primer nivel)
# creando una nueva lista en el primer nivel
# pero manteniendo las referencias del segundo nivel
lista_x = [1, 2, 3, ['a', 'b', 'c']]
lista_y = lista_x.copy()
lista_x[0]=4 # Cambia 1 por 4
lista_x[3][0]='Z' # Cambia 'a' por 'Z'
print("lista_x:", lista_x) # [4, 2, 3, ['Z', 'b', 'c']]
print("lista_y:", lista_y) # [1, 2, 3, ['Z', 'b', 'c']]

# Slicing hace una shallow copy (copia en el primer nivel)
# creando una nueva lista en el primer nivel
# pero manteniendo las referencias del segundo nivel
lista_x = [1, 2, 3, ['a', 'b', 'c']]
lista_y = lista_x[:]
lista_x[0]=4 # Cambia 1 por 4
lista_x[3][0]='Z' # Cambia 'a' por 'Z'
print("lista_x:", lista_x) # [4, 2, 3, ['Z', 'b', 'c']]
print("lista_y:", lista_y) # [1, 2, 3, ['Z', 'b', 'c']]

# Función deepcopy del módulo copy duplica todos los niveles
# creando una nueva estructura de datos independiente
# de la estructura original.
import copy

lista_x = [1, 2, 3, ['a', 'b', 'c']]
lista_y = copy.deepcopy(lista_x)
lista_x[0]=4 # Cambia 1 por 4
lista_x[3][0]='Z' # Cambia 'a' por 'Z'
print("lista_x:", lista_x) # [4, 2, 3, ['Z', 'b', 'c']]
print("lista_y:", lista_y) # [1, 2, 3, ['a', 'b', 'c']]