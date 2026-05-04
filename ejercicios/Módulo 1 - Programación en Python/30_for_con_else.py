import random
aleatorio = random.randint(0,200)
print('Aleatorio:', aleatorio)
for i in range(0,100):
    print(i,end='*')
    if (i==aleatorio):
        break
else:# Sólo se ejecuta si no se sale con break
    print()
    print('El aleatorio NO está entre 0 y 99')