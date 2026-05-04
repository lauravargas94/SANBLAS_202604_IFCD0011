"""
Crear una clase factura
Tiene como atributos: nombre cliente, cif, lista de productos, 
lista importes
Métodos:
- Añadir producto: add_producto(nombre, importe)
- Obtener importe de la factura
- Programar los métodos __str__ y __repr__
"""
class Factura:
    def __init__(self, nombre_cliente : str, cif : str, lista_productos : list[str],
                  lista_importes: list[int]) -> None:
        self.nombre_cliente = nombre_cliente
        self.cif = cif
        self.lista_productos = lista_productos
        self.lista_importes = lista_importes

    def add_producto(self, nombre : str, importe : int) -> None:
        self.lista_productos.append(nombre)
        self.lista_importes.append(importe)

    def obtener_importe(self) -> int:
        importe = sum(self.lista_importes)
        return importe
    
    def __str__(self) -> str:
        return str(self.__dict__)
    
    def __repr__(self) -> str:
        return self.__str__()
    
factura_1 = Factura('Gerardo', 'A34328', ['Pan','Leche'], [200, 150])
factura_1.add_producto('Azúcar', 100)
importe = factura_1.obtener_importe()
print(importe)
print(factura_1)

        