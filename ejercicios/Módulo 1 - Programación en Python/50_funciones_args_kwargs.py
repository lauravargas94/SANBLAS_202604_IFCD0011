def sumar(*args):
    print(type(args)) # <class 'tuple'>
    print(args) # (1, 4)

sumar(1,4)
#sumar('hola','python')# Error

def ordenar(**kwargs):
    print(type(kwargs)) # <class 'dict'>
    print(kwargs) # {'palabra_2': 'otracosa', 'palabra_1': 'loquesea'}

ordenar(palabra_2='otracosa', palabra_1='loquesea')

def combinar(*args, offset=5, **kwargs):
    print('args:', args)
    print('offset:', offset)
    print('kwargs:', kwargs)

combinar() # OK
combinar(10) # OK
combinar(nombre='Sara') # OK
combinar(offset=6,nombre='Python') # OK
combinar(8, offset=10, nombre='Python') # OK
combinar(8, True, 'Pepe', offset=25, nombre='Python', anyo=1996, compilado=False) # OK
