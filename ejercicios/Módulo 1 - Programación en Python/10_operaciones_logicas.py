# or vs |
def is_active(id_sensor : int) -> bool:
    activado = True
    print(f'Sensor:{id_sensor}. Estado:{activado}')
    return activado

if is_active(0) or is_active(1):
    # Evalua la primera condición y no la segunda
    print('(or)Alarma')
else:
    print('(or)OK')

if is_active(0) | is_active(1):
    print('(|)Alarma')
else:
    print('(|)OK')

# and vs & 
def is_open(id_ventana : int) -> bool:
    abierta = False
    print(f'Ventana:{id_ventana}. Estado:{abierta}')
    return abierta

if is_open(0) and is_open(1):
    print('(and)Estan todas abiertas')
else:
    print('(and)Hay alguna ventana cerrada')

if is_open(0) & is_open(1):
    print('(&)Estan todas abiertas')
else:
    print('(&)Hay alguna ventana cerrada')

# XOR

if is_active(0) ^ is_active(1):
    print('Está activo alguno de los sensores')
else:
    print('O no hay sensores activos o lo están todos')
