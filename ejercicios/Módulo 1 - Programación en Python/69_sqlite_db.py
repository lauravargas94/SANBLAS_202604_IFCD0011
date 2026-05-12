import sqlite3

'''
CRUD:
C - CREATE
R - READ
U - UPDATE
D - DELETE
'''

'''
db_movies.sqlite3

Tabla: peliculas
Columnas: 
- id - INTEGER - PK (Primary Key) - AUTOINCREMENT
- titulo - TEXT
- director - TEXT
- anyo - INTEGER
- plot - TEXT
'''

class Pelicula:
    def __init__(self, titulo, director, anyo, plot, id=None) -> None:
        self.id=id
        self.titulo=titulo
        self.director=director
        self.anyo=anyo
        self.plot=plot


def obtener_conexion():
    conn=sqlite3.connect('db_movies.sqlite3')
    return conn

def crear_db(conn):
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS peliculas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        director TEXT NOT NULL,
        anyo INTEGER NOT NULL,
        plot TEXT NOT NULL
    );''')
    c.close()

def create(conn: sqlite3.Connection, pelicula : Pelicula):
    #sql = f'INSERT INTO peliculas (titulo, director, anyo, plot) \
    #    VALUES ("{pelicula.titulo}", "{pelicula.director}", {pelicula.anyo}, "{pelicula.plot}")'
    
    #sql = f'INSERT INTO peliculas (titulo, director, anyo, plot) \
    #    VALUES {pelicula.titulo, pelicula.director, pelicula.anyo, pelicula.plot}'
    
    sql = 'INSERT INTO peliculas (titulo, director, anyo, plot) VALUES (?, ?, ?, ?)'
        
    c = conn.cursor()
    c.execute(sql, (pelicula.titulo, pelicula.director, pelicula.anyo, pelicula.plot))
    conn.commit()
    c.close()

def read(conn: sqlite3.Connection, id: int):
    sql = f'SELECT * FROM peliculas WHERE id={id}'
    c = conn.cursor()
    cursor = c.execute(sql)
    registro = cursor.fetchone()
    cursor.close()
    c.close()
    return registro

def read_all(conn: sqlite3.Connection):
    sql = f'SELECT * FROM peliculas'
    c = conn.cursor()
    cursor = c.execute(sql)
    registros = cursor.fetchall()
    cursor.close()
    c.close()
    return registros

def update(conn: sqlite3.Connection, pelicula: Pelicula):
    sql = f'UPDATE peliculas SET id=?, titulo=?, director=?, anyo=?, plot=? WHERE id=?'
    valores = (pelicula.id, pelicula.titulo, pelicula.director, pelicula.anyo, pelicula.plot, pelicula.id)
    c = conn.cursor()
    c.execute(sql, valores)
    c.close

def delete(conn: sqlite3.Connection, id: int):
    sql = f'DELETE FROM peliculas WHERE id=?'
    valores = (id, )
    c = conn.cursor()
    c.execute(sql, valores)
    c.close

def delete_all(conn: sqlite3.Connection):
    sql = f'DELETE FROM peliculas'
    c = conn.cursor()
    c.execute(sql)
    c.close

if __name__=='__main__':
    print('Iniciando ejecución...')
    conn = obtener_conexion()
    crear_db(conn)
    print('1. Crear')
    print('2. Leer uno')
    print('3. Leer todos')
    print('4. Actualizar')
    print('5. Eliminar')
    print('6. Borrar todo - DANGER ZONE')
    print('0. Salir')
    opcion = int(input('Introduce opción:'))
    while opcion!=0:
        match (opcion):
            case 1:
                # Creación de película
                batman = Pelicula('Superman', 'Christopher Nolan', 2010, 'Un rico se disfraza de murciélago')
                create(conn, pelicula=batman)
            case 2:
                # Lectura de película
                id = int(input('Introduce id:'))
                pelicula_buscada = read(conn, id=id)
                print(type(pelicula_buscada))
                print(pelicula_buscada)
            case 3:
                # Lectura de todas las películas
                peliculas_buscadas = read_all(conn)
                print(type(peliculas_buscadas))
                print(peliculas_buscadas)
            case 4:
                # Modificación
                id = int(input('Introduce id:'))
                titulo = input('Introduce nuevo título:')
                tupla_pelicula = read(conn, id)
                pelicula = Pelicula(titulo=tupla_pelicula[1], director=tupla_pelicula[2],
                                    anyo=tupla_pelicula[3], plot=tupla_pelicula[4], id=tupla_pelicula[0])
                pelicula.titulo=titulo
                update(conn, pelicula)
            case 5:
                # Modificación
                id = int(input('Introduce id:'))
                delete(conn, id)
            case 6:
                delete_all(conn)
            case _:
                print('Opción no reconocida')
        opcion = int(input('Introduce opción:'))
    conn.close()