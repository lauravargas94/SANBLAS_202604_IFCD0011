class Factura:
    def __init__(self, numero, cliente, monto):
        self.numero = numero
        self.cliente = cliente
        self.monto = monto

    def __str__(self):
        return f"Factura {self.numero} - Cliente: {self.cliente}, Monto: {self.monto}"
    
    def __repr__(self) -> str:
        return f"Factura {self.numero} - Cliente: {self.cliente}, Monto: {self.monto}"
    
facturas = [
    Factura(1, "Cliente A", 100),
    Factura(2, "Cliente B", 200),
    Factura(3, "Cliente A", 150)]

def duplicar(factura):
    factura.monto=factura.monto*2
    return factura

facturas_duplicadas = map(duplicar, facturas)
for factura in facturas_duplicadas:
    print(factura)