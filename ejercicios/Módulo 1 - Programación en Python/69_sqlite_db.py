import sqlite3

'''
db_movies.sqlite3

Tabla: peliculas
Columnas: 
- id - INTEGER - PK (Primary Key)
- titulo - TEXT
- director - TEXT
- anyo - INTEGER
- plot - TEXT
'''

def crear_db():
    conn=sqlite3.connect('db_movies.sqlite3')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS peliculas(
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        director TEXT NOT NULL,
        anyo INTEGER NOT NULL,
        plot TEXT NOT NULL
    );''')

crear_db()