"""
Selenium con Python sirve principalmente para automatizar 
navegadores web, permitiendo simular acciones humanas como 
hacer clics, rellenar formularios, navegar entre páginas y 
extraer datos (web scraping). 
"""

from selenium import webdriver
import pandas as pd
from io import StringIO
import time

driver = webdriver.Chrome()

url = "https://www.coinbase.com/es-es/explore"
driver.get(url)

# Esperar a que cargue JavaScript
time.sleep(5)

html = driver.page_source

driver.quit()

data_frames = pd.read_html(StringIO(html))

print(f"Tablas encontradas: {len(data_frames)}")

for data_frame in data_frames:
    print(data_frame.info())
