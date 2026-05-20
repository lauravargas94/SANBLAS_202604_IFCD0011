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

# Método tradicional
facturas_filtradas = []
for factura in facturas:
    if factura.monto>125:
        facturas_filtradas.append(factura)

# Programación funcional con la función filter
def comprobar_monto(factura):
    return factura.monto > 125

facturas_filtradas = filter(comprobar_monto, facturas)

# Programación funcional con la función filter y función lambda
facturas_filtradas = filter(lambda factura: factura.monto>125, facturas)