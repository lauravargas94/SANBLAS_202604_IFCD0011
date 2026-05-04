import unicodedata

with open('fichero.txt', mode='r', encoding='utf-8') as fichero:
    texto = fichero.read()

texto_normalizado = unicodedata.normalize('NFC', texto)

tokens = texto.split()
tokens_normalizados = texto_normalizado.split()

print('Amadís está en el texto "normal":', 'Amadís' in tokens)
print('Amadís está en el texto "normalizado":', 'Amadís' in tokens_normalizados)
