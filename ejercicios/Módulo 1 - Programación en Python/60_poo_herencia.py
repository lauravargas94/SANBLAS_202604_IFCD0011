class VehiculoMotor:
    def __init__(self, nombre, velocidad_maxima) -> None:
        self.nombre = nombre
        self.velocidad_maxima = velocidad_maxima

    def acelerar(self):
        print('Acelerando...')

    def reducir(self):
        print('Reduciendo...')

class Barco(VehiculoMotor):
    def __init__(self, nombre, velocidad_maxima, quilla, eslora, manga) -> None:
        super().__init__(nombre, velocidad_maxima)
        self.quilla = quilla
        self.eslora = eslora
        self.manga = manga

    def atracar(self):
        print('Atracar...')

class Motocicleta(VehiculoMotor):
    def __init__(self, nombre, velocidad_maxima, grado_inclinacion) -> None:
        super().__init__(nombre, velocidad_maxima)
        self.grado_inclinacion = grado_inclinacion

    def tumbar(self):
        print('Tumbándose en la curva...')

    def hacer_caballito(self):
        print('Haciendo caballito...')

    def filtrar(self):
        print('Filtrándose entre el resto de vehículos...')

mi_yate = Barco('Albacete', 100, 5, 50, 10)
mi_yate.acelerar()
mi_yate.atracar()
mi_yate.reducir()

la_moto_de_mario = Motocicleta('YAMAHA MT07', 214, 60)
la_moto_de_mario.acelerar()
la_moto_de_mario.reducir()
la_moto_de_mario.tumbar()
print(la_moto_de_mario.velocidad_maxima) # Este es un atributo de VehiculoMotor

print(isinstance(la_moto_de_mario, Motocicleta)) # True
print(isinstance(la_moto_de_mario, VehiculoMotor)) # True
print(isinstance(la_moto_de_mario, Barco)) # False
