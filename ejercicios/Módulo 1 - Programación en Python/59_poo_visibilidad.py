class ContratoLaboral:
    def __init__(self, nombre_empleado, categoria, salario) -> None:
        self.nombre_empleado = nombre_empleado
        self.categoria = categoria
        self.__salario = salario # Atributo privado

    def get_salario(self):
        if (self.__salario>200_000):
            raise ValueError('No se pueden consultar salarios saltos')
        return self.__salario
    
    def set_salario(self, nuevo_salario):
        if (nuevo_salario>(self.__salario*1.1)):
            raise Exception('No se puede incrementar más del 10%')
        self.__salario = nuevo_salario


contrato_1 = ContratoLaboral('Donald Trump', 'Presidente', 100_000)

print('Nombre de empleado:', contrato_1.nombre_empleado)
print('Categoría:', contrato_1.categoria)
#print('Salario:', contrato_1.__salario) # Error
print('Salario:', contrato_1._ContratoLaboral__salario) # Funciona, pero no se debe usar
#contrato_1.__salario = 200_000 # Error
#print('Salario modificado:', contrato_1.__salario) # Error

print(contrato_1.__dict__)