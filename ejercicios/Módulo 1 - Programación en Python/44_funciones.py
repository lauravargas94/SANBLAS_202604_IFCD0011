def escribir_hola():
    print('Hola')

def escribir_adios():
    print('Adios')

def escribir(texto : str):
    print(texto)

def cambia_de_sitio(fila : int, columna : int):
    pass

def calcula_importe_a_pagar_renta(salario_bruto, hijos):
    # Proceso de cálculo
    a_pagar = 3_000
    return a_pagar

def eliminar_almohadillas(texto : str):
    resultado = texto.replace('#', '')
    return resultado

def eliminar_caracter(texto : str, caracter : str) -> str:
    resultado = texto.replace(caracter, '')
    return resultado