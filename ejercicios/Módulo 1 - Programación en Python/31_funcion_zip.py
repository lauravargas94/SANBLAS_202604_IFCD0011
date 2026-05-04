personas = ['Mario', 'Carlos', 'Nayra', 'Michelle', 'Hani', 'Pablo','Pablo David']
edades = [54, 35, 45, 26, 36, 20]
# mezcla = zip(personas, edades, strict=True) # Si hay discrepancias, chilla
mezcla = zip(personas, edades)
alumnos = list(mezcla)
print(alumnos)