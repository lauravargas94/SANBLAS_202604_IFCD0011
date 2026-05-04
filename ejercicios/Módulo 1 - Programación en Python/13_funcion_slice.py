cadena_1 = 'En un lugar de La Mancha'
cadena_2 = 'de cuyo nombre no quiero acordarme'

trozo_1 = cadena_1[3:8]
trozo_2 = cadena_2[3:8]

fragmento = slice(3,8)

trozo_3 = cadena_1[fragmento]
trozo_4 = cadena_2[fragmento]

print(trozo_1)
print(trozo_2)
print(trozo_3)
print(trozo_4)