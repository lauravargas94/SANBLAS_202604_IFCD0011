# PASO DE PARÁMETROS POR VALOR
def modificar(argumento):
    argumento+=1

original = 10
modificar(original)
print(original) # 10

# PASO DE PARÁMETROS POR REFERENCIA
def cambiar(argumento : list):
    argumento.append('sufijo')

original = [1,2,3]
cambiar(original)
print(original) # [1, 2, 3, 'sufijo']