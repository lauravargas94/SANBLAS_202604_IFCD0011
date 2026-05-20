import pandas as pd

serie = pd.Series([8,20,12,-10,16], name='Diferencial')
descripcion = serie.describe()
print('Tipo:', type(descripcion))
print(descripcion)
print('Media:', descripcion['mean'])