from functools import reduce

class Factura:
    def __init__(self, numero, cliente, monto):
        self.numero = numero
        self.cliente = cliente
        self.monto = monto

facturas = [
    Factura(1, "Cliente A", 100),
    Factura(2, "Cliente B", 200),
    Factura(3, "Cliente A", 150)]

# Opción con función 'normal'
def acumular_monto(acumulado, factura):
    acumulado=acumulado+factura.monto
    return acumulado
total = reduce(acumular_monto, facturas, 0)

# Opción con función lambda
total = reduce(lambda acumulado, factura:acumulado + factura.monto, facturas, 0)


print(total)