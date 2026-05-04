opcion = int(input('Introduce una opción 1-3:'))

if opcion==1:
    print('Ha pulsado 1')
elif opcion==2:
    print('Ha pulsado 2')
elif opcion==3:
    print('Ha pulsado 3')
else:
    print('Opción incorrecta')

match opcion:
    case 1:
        print('Ha pulsado 1')
    case 2:
        print('Ha pulsado 2')
    case 3:
        print('Ha pulsado 3')
    case _:
        print('Opción incorrecta')



