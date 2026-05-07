import json

datos = {'Madrid':7_000_000, 'Capital':'Madrid', 'Activo':False, 'AI':None}
with open('madrid.json', mode='wt', encoding='utf-8') as fichero:
    # json.dump(datos, fichero) # Guarda el json en un fichero
    json.dump(obj=datos, fp=fichero) # Guarda el json en un fichero

texto = json.dumps(datos) # Obtenemos un str con el json
print(texto)

