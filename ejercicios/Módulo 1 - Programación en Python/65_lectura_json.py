import json

datos_json = '''{
    "Título": "Lo que el viento se llevó",
    "Año": 1932,
    "Director": "El nombre del director",
    "Casting": [
        "Clark Gable",
        "Vivian Leigh",
        "Otro más"
    ],
    "Netflix": false,
    "Recaudacion": null
}'''

# Desde fichero
with open('pelicula.json', mode='rt', encoding='utf-8') as fichero:
    datos = json.load(fichero) # Carga desde fichero
    print(type(datos))
    print(datos)
    print(datos['Director'])

# Desde str
datos = json.loads(datos_json) # Carga desde str
print(type(datos))
print(datos)
print(datos['Director'])