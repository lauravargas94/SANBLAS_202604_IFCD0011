ciudades = ['alicante','Zamora','almeria','zaragoza']

# De menor a mayor, por punto de código
ciudades_ordenadas = sorted(ciudades)
print(ciudades_ordenadas) # ['Zamora', 'alicante', 'almeria', 'zaragoza']

# De menor a mayor, alfabéticamente
ciudades_ordenadas = sorted(ciudades, key=str.lower)
print(ciudades_ordenadas) # ['alicante', 'almeria', 'Zamora', 'zaragoza']

# De mayor a menor, alfabéticamente
ciudades_ordenadas = sorted(ciudades, key=str.lower, reverse=True)
print(ciudades_ordenadas) # ['zaragoza', 'Zamora', 'almeria', 'alicante']

# Por longitud, de mayor a menor
ciudades_ordenadas = sorted(ciudades, key=len, reverse=True)
print(ciudades_ordenadas) # ['alicante', 'zaragoza', 'almeria', 'Zamora']

# Ídem. con el método sort (ordena la lista)