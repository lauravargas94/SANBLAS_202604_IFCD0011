import sqlite3

'''
BASE DE DATOS: ENCUESTA_POBLACION
TABLA: DATOS_PERSONALES
CAMPOS:
- ID
- NOMBRE Y APELLIDOS
- GENERO
- AÑO DE NACIMIENTO
- ALTURA
- PESO
- NUMERO DE HIJOS
- GRADO DE FELICIDAD 
'''

class DatosPersonales:
    def __init__(self, nombre, genero, anyo, altura, peso, 
                 numero_hijos, felicidad, id=None) -> None:
        self.id=id
        self.nombre=nombre
        self.genero=genero
        self.anyo=anyo
        self.altura=altura
        self.peso=peso
        self.numero_hijos=numero_hijos
        self.felicidad=felicidad
    


def obtener_conexion():
    conn=sqlite3.connect('encuesta_poblacion.db')
    return conn

def crear_db(conn):
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS datos_personales(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        genero TEXT NOT NULL,
        anyo INTEGER NOT NULL,
        altura INTEGER NOT NULL,
        peso INTEGER NOT NULL,
        numero_hijos INTEGER NOT NULL,
        felicidad INTEGER NOT NULL
    );''')
    c.close()

'''
CRUD:
C - CREATE
R - READ
U - UPDATE
D - DELETE
'''
def create(conn: sqlite3.Connection, datos_personales : DatosPersonales):
    sql = 'INSERT INTO datos_personales (nombre, genero, anyo, altura, peso, numero_hijos, felicidad) \
          VALUES (?, ?, ?, ?, ?, ?, ?)'
    c = conn.cursor()
    c.execute(sql, (datos_personales.nombre, datos_personales.genero, 
                    datos_personales.anyo, datos_personales.altura,
                    datos_personales.peso, datos_personales.numero_hijos, datos_personales.felicidad))
    conn.commit()
    c.close()

def read(conn: sqlite3.Connection, id: int):
    sql = f'SELECT * FROM datos_personales WHERE id={id}'
    c = conn.cursor()
    cursor = c.execute(sql)
    registro = cursor.fetchone()
    cursor.close()
    c.close()
    return registro

def read_all(conn: sqlite3.Connection):
    sql = f'SELECT * FROM datos_personales'
    c = conn.cursor()
    cursor = c.execute(sql)
    registros = cursor.fetchall()
    cursor.close()
    c.close()
    return registros


if __name__=='__main__':
    print('Iniciando ejecución...')
    conn = obtener_conexion()
    crear_db(conn)
    # Creación de los datos personales
    christopher = DatosPersonales('Christopher ', 'Hombre', 1978, 185, 88, 2, 5)
    create(conn, christopher)
    # Lectura de uno
    persona_buscada = read(conn, id=1)
    print(type(persona_buscada))
    print(persona_buscada)
    # Lectura de todos
    peliculas_buscadas = read_all(conn)
    print(type(peliculas_buscadas))
    print(peliculas_buscadas)
    conn.close()