nombre_completo = input('Nombre de fichero:')

posicion = nombre_completo.index('.')

nombre = nombre_completo[0:posicion]
extension = nombre_completo[posicion+1:]

print('Nombre:',nombre)
print('Extensión:',extension)

