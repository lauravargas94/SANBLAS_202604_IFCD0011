class Automovil:
    def __init__(self, matricula, marca, modelo, combustible='Gasolina') -> None:
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.alta = True # Atributo creado en el constructor
        self.velocidad = 0
        self.arrancado = False

    def arrancar(self):
        self.arrancado = True
        print(f'Soy {self.matricula} y estoy arrancando...')

    def acelerar(self):
        if self.arrancado==True:
            self.velocidad += 10

    def __str__(self) -> str:
        #return f'Matricula:{self.matricula}. Velocidad:{self.velocidad}'
        return str(self.__dict__)

    def __repr__(self) -> str:
        return self.__str__()

entero = int(17.8)
lista = list((1,2,3,4,5))
mi_coche = Automovil('7324-FMN', 'SEAT', 'TOLEDO')
mi_coche.arrancar()
for i in range(12):
    mi_coche.acelerar()

print(mi_coche) # Utiliza __str__
print([mi_coche]) # Utiliza __repr__