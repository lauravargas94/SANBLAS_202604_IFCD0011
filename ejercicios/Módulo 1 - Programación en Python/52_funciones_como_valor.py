import time

def arrancar():
    print('Arrancando motor...')
    time.sleep(1)

def parar():
    print('Parando motor...')
    time.sleep(1)
    

def acelerar():
    print('Acelerando...')
    time.sleep(1)
    

def frenar():
    print('Frenando...')
    time.sleep(1)

def ejecutar(funcion):
    funcion()

lista = [arrancar, acelerar, acelerar, acelerar, frenar, parar]
while len(lista)>0:
    ejecutar(lista.pop(0))