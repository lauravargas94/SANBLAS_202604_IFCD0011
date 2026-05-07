import requests 

URL = 'https://www.omdbapi.com'
API_KEY = '95c08eba'

titulo = input('Introduce el título de la película:')

parametros = {
    'apikey': API_KEY,
    't': titulo
}

response = requests.get(url=URL, params=parametros)

if response.status_code==200:
    datos = response.json()
    if (datos['Response']=='True'):
        print('Título:', datos['Title'])
        print('Director:', datos['Director'])
        print('Sinopsis:', datos['Plot'])
    else:
        print('No se ha encontrado ninguna película')

else:
    print('Ha ocurrido un error: ', response.status_code)