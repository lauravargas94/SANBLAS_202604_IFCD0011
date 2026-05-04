# Los valores de la tupla son: Python? Inglés[0-3] B1? 
# Disponibilidad geográfica? sabe un poquito de Chino?
alberto = ('Alberto', True, 1, True, True, False)
joselin = ('Joselín', True, 2, True, False, False)
gerardo = ('Gerardo', True, 0, True, False, False)
sara = ('Sara', True, 3, True, True, True)
oswaldo = ('Oswaldo', True, 3, True, True, True)

candidatos = (alberto, joselin, gerardo, sara, oswaldo)

# Buscar TODOS los candidatos que:
# -saben Python
# -tienen disponibilidad geográfica
# -saben un poquito de chino
for candidato in candidatos:
    if candidato[5]==False:
        continue
    elif candidato[1]==False:
        continue
    elif candidato[4]==True:
        print(candidato[0])

# Buscar EL PRIMER candidato que:
# -sabe Python
# -tiene disponibilidad geográfica
# -sabe un poquito de chino
for candidato in candidatos:
    if candidato[5]==False:
        continue
    elif candidato[1]==False:
        continue
    elif candidato[4]==True:
        print(candidato[0])
        break