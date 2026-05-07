import requests 

URL = 'https://servicios.ine.es/wstempus/js/es/DATOS_TABLA/79340?tip=AM'

response = requests.get(URL)

if response.status_code==200:
    datos = response.json()
    print(type(datos))
    print(datos)
    valor_buscado = datos[6]['Data'][0]['Valor']
    print(valor_buscado) # 682.3
    pass
else:
    print('Ha ocurrido un error: ', response.status_code)