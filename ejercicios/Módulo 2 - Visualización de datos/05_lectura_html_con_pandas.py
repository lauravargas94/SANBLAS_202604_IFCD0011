import requests
from io import StringIO

import pandas as pd

URL = 'https://es.wikipedia.org/wiki/Liga_Nacional_de_F%C3%BAtbol_Profesional'
headers = {
    "User-Agent": "Mozilla/5.0"
}
html = requests.get(URL, headers=headers).text
html_io = StringIO(html)
data_frames = pd.read_html(html_io)

print('Número de tablas:',len(data_frames))
for data_frame in data_frames:
    print(data_frame.info())