# 2 tuplas con el mismo contenido
tupla_1=(3, 4, 'Hola', True)
tupla_2=(3, 4, 'Hola', True)
print(tupla_1==tupla_2) # True
#print(tupla_1 is tupla_2) # ¿True?

# 2 tuplas con distinto contenido, pero el primer elemento es común
tupla_1 = (3, 4, 'Hola', True)
tupla_2 = (3, 5, 'adios', False)
print(tupla_1==tupla_2) # False

# 2 tuplas con el primer elemento distinto y el resto igual
tupla_1 = (3, 4, 'Hola', True)
tupla_2 = (4, 4, 'Hola', True)
print(tupla_1==tupla_2) # False

# 2 tuplas con el primer elemento distinto y el resto igual
tupla_1 = (3, [1,2,3])
tupla_2 = (4, 4, 'Hola', True)
print(tupla_1==tupla_2) # False

# 1 tupla y 1 lista con el primer elemento igual y el resto distinto
tupla_1 = (3, [1,2,3])
lista_1 = [3, 4, 'Hola', True]
print(tupla_1==lista_1) # False

# 1 tupla y 1 lista con el mismo contenido
tupla_1=(3, 4, 'Hola', True)
lista_1=[3, 4, 'Hola', True]
print(tupla_1==lista_1) # False

tuple_3 = (9, 10,'Aprobado', True)
tuple_4 = (9, 10,'Sobresaliente', True)
print(tuple_3==tuple_4) # True

# Comparación múltiple
tupla_1=(3, 4, 'Hola', True)
tupla_2=(3, 4, 'Hola', True)
tupla_3=(3, 4, 'Hola', True)
print(tupla_1==tupla_2==tupla_3)
print(tupla_1 is tupla_2 is tupla_3)
