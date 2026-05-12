import time
import random
import sqlite3
from dataclasses import dataclass

NUMERO_REGISTROS_DEFAULT = 100
NOMBRE_DATABASE = 'db_empleados.sqlite3'
SALARIO_MINIMO_DEFAULT = 18_000
SALARIO_MAXIMO_DEFAULT = 50_000

@dataclass
class Empleado:
    nombre : str
    apellidos : str
    categoria_programacion : str
    ciudad : str
    salario : int
    id: int = None

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

def obtener_conexion():
    conn = sqlite3.connect(NOMBRE_DATABASE)
    return conn

def crear_db(conn):
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS empleados(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        categoria_programacion TEXT NOT NULL,
        ciudad TEXT NOT NULL,
        salario INTEGER NOT NULL
    );""")
    conn.commit()

def insert(conn: sqlite3.Connection, empleado: Empleado):
    sql = """INSERT INTO empleados (nombre, apellidos, categoria_programacion, ciudad, salario)
    VALUES (?, ?, ?, ?, ?)"""
    c = conn.cursor()
    c.execute(sql, (
        empleado.nombre,
        empleado.apellidos,
        empleado.categoria_programacion,
        empleado.ciudad,
        empleado.salario
    ))
    conn.commit()
    c.close()

numero_registros = input(f'Número de registros ({NUMERO_REGISTROS_DEFAULT}):')
nombre_database = input(f'Nombre de la base de datos ({NOMBRE_DATABASE}):')
salario_minimo = input(f'Salario mínimo ({SALARIO_MINIMO_DEFAULT}):')
salario_maximo = input(f'Salario máximo ({SALARIO_MAXIMO_DEFAULT}):')

numero_registros = NUMERO_REGISTROS_DEFAULT if len(numero_registros)==0 else int(numero_registros)
nombre_database = NOMBRE_DATABASE if len(nombre_database)==0 else nombre_database
salario_minimo = SALARIO_MINIMO_DEFAULT if len(salario_minimo)==0 else int(salario_minimo)
salario_maximo = SALARIO_MAXIMO_DEFAULT if len(salario_maximo)==0 else int(salario_maximo)

if __name__ == "__main__":
    inicio = time.perf_counter()

    conn = obtener_conexion()
    crear_db(conn)

    for i in range(numero_registros):
        empleado = Empleado(
            nombre=random.choice(nombres),
            apellidos=random.choice(apellidos),
            categoria_programacion=random.choice(categorias_programacion),
            ciudad=random.choice(ciudades),
            salario=random.randint(salario_minimo, salario_maximo)
        )        
        insert(conn, empleado)
    
    # Cerramos la conexión
    conn.close()

    fin = time.perf_counter()
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")