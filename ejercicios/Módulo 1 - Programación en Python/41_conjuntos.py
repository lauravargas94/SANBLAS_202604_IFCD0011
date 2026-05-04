xbox_disco_1={'COD', 'Forza Motosport 3', 'Batman'}
juegos_potenciales = ['Lego Star Wars', 'Fifa 2008', 'Formula 1 2004']

# Determinar si son disjuntos
son_disjuntos = xbox_disco_1.isdisjoint(juegos_potenciales)
print(son_disjuntos) # True --> No tienen elementos comunes

# Juegos comunes
print(xbox_disco_1.intersection(juegos_potenciales))

# Crear un fichero de texto con palabras censurables
# Crear un fichero con el texto de un post

# Construir un pograma de censura