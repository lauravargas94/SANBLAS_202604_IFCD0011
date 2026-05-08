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
    sql = f'INSERT INTO peliculas (titulo, director, anyo, plot) \
        VALUES {pelicula.titulo, pelicula.director, pelicula.anyo, pelicula.plot}'
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    c.close()
    

if __name__=='__main__':
    print('Iniciando ejecución...')
    conn = obtener_conexion()
    crear_db(conn)
    # Creación de película
    batman = Pelicula('Batman', 'Christopher Nolan', 2010, 'Un rico se disfraza de murciélago')
    create(conn, pelicula=batman)

    conn.close()