import random

# Lista de 20 nombres (masculinos y femeninos)
nombres = [
    "Carlos", "María", "Juan", "Lucía", "Pedro",
    "Ana", "Luis", "Elena", "Jorge", "Carmen",
    "Diego", "Sofía", "Miguel", "Paula", "Andrés",
    "Laura", "Fernando", "Isabel", "Raúl", "Clara"
]

# Lista de 20 apellidos
apellidos = [
    "García", "Fernández", "López", "Martínez", "Sánchez",
    "Pérez", "Gómez", "Martín", "Jiménez", "Ruiz",
    "Hernández", "Díaz", "Moreno", "Muñoz", "Álvarez",
    "Romero", "Alonso", "Gutiérrez", "Navarro", "Torres"
]

# Lista de 10 ciudades
ciudades = [
    "Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao",
    "Málaga", "Zaragoza", "Granada", "Toledo", "Salamanca"
]

# Lista de 5 categorías profesionales del sector programación
categorias_programacion = [
    "Desarrollador Backend",
    "Desarrollador Frontend",
    "Ingeniero de Software",
    "Científico de Datos",
    "DevOps Engineer"
]

NUMERO_REGISTROS_DEFAULT = 100
NOMBRE_FICHERO_DEFAULT = 'generated_data.csv'
SALARIO_MINIMO_DEFAULT = 18_000
SALARIO_MAXIMO_DEFAULT = 50_000
numero_registros = input(f'Número de registros ({NUMERO_REGISTROS_DEFAULT}):')
nombre_fichero = input(f'Nombre de fichero ({NOMBRE_FICHERO_DEFAULT}):')
salario_minimo = input(f'Salario mínimo ({SALARIO_MINIMO_DEFAULT}):')
salario_maximo = input(f'Salario mínimo ({SALARIO_MAXIMO_DEFAULT}):')

numero_registros = NUMERO_REGISTROS_DEFAULT if len(numero_registros)==0 else int(numero_registros)
nombre_fichero = NOMBRE_FICHERO_DEFAULT if len(nombre_fichero)==0 else nombre_fichero
salario_minimo = SALARIO_MINIMO_DEFAULT if len(salario_minimo)==0 else int(salario_minimo)
salario_maximo = SALARIO_MAXIMO_DEFAULT if len(salario_maximo)==0 else int(salario_maximo)

with open(nombre_fichero, mode='wt', encoding='utf-8') as fichero:
    for i in range(numero_registros):
        registro=f'{i+1},{random.choice(nombres)},{random.choice(apellidos)},{random.choice(categorias_programacion)},{random.choice(ciudades)},{random.randint(salario_minimo,salario_maximo)}'
        fichero.write(registro)
        fichero.write('\n')