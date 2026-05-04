with open('empleados.csv', mode='rt', encoding='utf-8') as fichero_empleados:
    # Leer todo el contenido en una única lectura
    # todo_el_contenido = fichero_empleados.read()
    
    # Leer una única línea
    # linea = fichero_empleados.readline()

    # Leer todas las líneas y las mete en una lista
    # lineas = fichero_empleados.readlines()

    # Leer todas las líneas de uno en uno
    # for empleado in fichero_empleados:
    #    print(empleado)

    # Obtener una lista de listas con los campos del fichero
    # eliminando los \n
    fichero_empleados.seek(0) # Posicionamos la cabeza de lectura al principio 

    empleados = [linea.strip().split(',') for linea in fichero_empleados]

    # Obtener una lista de listas con los empleados de Zaragoza
    fichero_empleados.seek(0) # Posicionamos la cabeza de lectura al principio 
    
    empleados = [linea.strip().split(',') for linea in fichero_empleados if linea.split(',')[-2]=='Zaragoza']

    # Obtener una lista de listas con los empleados 'Ingeniero de Software'
    fichero_empleados.seek(0) # Posicionamos la cabeza de lectura al principio 
    
    empleados_ingenieros_software = [linea.strip().split(',') for linea in fichero_empleados if linea.split(',')[3]=='Ingeniero de Software']
    
    # Obtener una lista de listas con los empleados 'Ingeniero de Software' y de Zaragoza
    fichero_empleados.seek(0) # Posicionamos la cabeza de lectura al principio 

    empleados_ingenieros_software_de_zaragoza = [linea.strip().split(',') 
                                     for linea in fichero_empleados 
                                     if linea.split(',')[3]=='Ingeniero de Software' and linea.split(',')[-2]=='Zaragoza']

    # Obtener una lista de listas con los empleados que cobran más de 40000€
    fichero_empleados.seek(0) # Posicionamos la cabeza de lectura al principio 

    empleados_salarios_altos = [linea.strip().split(',') 
                                for linea in fichero_empleados 
                                if int(linea.split(',')[5])>40000]
    
    # Obtener una lista de listas con los empleados que cobran más de 40000€
    # siendo los valores identificador y salario numéricos
    # y concatenando nombre y apellido
    fichero_empleados.seek(0) # Posicionamos la cabeza de lectura al principio 

    empleados_filtrados = [
        [int(linea.strip().split(',')[0]),
        f'{linea.strip().split(',')[1]} {linea.strip().split(',')[2]}',
        linea.strip().split(',')[3],
        linea.strip().split(',')[4],
        int(linea.strip().split(',')[5])]
        for linea in fichero_empleados]

    pass   