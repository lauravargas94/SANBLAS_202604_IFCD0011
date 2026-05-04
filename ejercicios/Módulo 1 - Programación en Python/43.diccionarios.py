from statistics import mean

estaciones = ('Primavera', 'Verano', 'Otoño', 'Invierno', 'Veranillo', 'Pre-otoño', 'Post-primavera')

facturacion = {'Primavera':2_000, 'Invierno':4_000}

# Añadir el elemento con la clave Verano (si existe la reemplaza)
facturacion['Verano']=8_000

# Añadir valores por defecto
for estacion in estaciones:
    #facturacion[estacion]=1000 # Cambia todas las claves
    #facturacion.setdefault(estacion, 1000) # Asignando valor a las claves inexistentes
    #facturacion.setdefault(estacion, sum(facturacion.values())//len(facturacion)) # A mano
    # Ojo, la media se hace sobre lo que hay AHORA
    facturacion.setdefault(estacion, int(mean(facturacion.values()))) # Utilizando statistics

facturacion_verano = facturacion['Verano'] # Si no existe 'Verano' --> KeyError
facturacion_primahermana = facturacion.get('Primahermana', 5_000) # Si no existe --> 5_000
facturacion_invierno = facturacion.get('Invierno', 18_000) # Como existe, devuelve 4_000