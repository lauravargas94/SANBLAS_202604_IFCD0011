import sqlite3

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

'''
CRUD:
C - CREATE
R - READ
U - UPDATE
D - DELETE
'''
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


if __name__=='__main__':
    print('Iniciando ejecución...')
    conn = obtener_conexion()
    crear_db(conn)
    # Creación de película
    batman = Pelicula('Superman', 'Christopher Nolan', 2010, 'Un rico se disfraza de murciélago')
    create(conn, pelicula=batman)
    # Lectura de película
    pelicula_buscada = read(conn, id=1)
    print(type(pelicula_buscada))
    print(pelicula_buscada)
    # Lectura de todas las películas
    peliculas_buscadas = read_all(conn)
    print(type(peliculas_buscadas))
    print(peliculas_buscadas)
    conn.close()