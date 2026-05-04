from dataclasses import dataclass

@dataclass
class Factura:
    nombre_cliente: str
    cif: str
    lista_productos: list[str]
    lista_importes: list[int]
    
    def add_producto(self, nombre : str, importe : int) -> None:
        self.lista_productos.append(nombre)
        self.lista_importes.append(importe)

    def obtener_importe(self) -> int:
        importe = sum(self.lista_importes)
        return importe
    
factura_1 = Factura('Gerardo', 'A34328', ['Pan','Leche'], [200, 150])
factura_1.add_producto('Azúcar', 100)
importe = factura_1.obtener_importe()
print(importe)
print(factura_1)

        