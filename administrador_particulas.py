from particula import Particula

class Administrador:
    def __init__(self):
        self.__particulas = []

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)




# Prueba    
p01 = Particula(id=1001, origenx=350, origeny=220, destinox=390, destinoy=500, velocidad=150, red=255, green=255, blue=255)
p02 = Particula(id=1002, origenx=100, origeny=200, destinox=300, destinoy=400, velocidad=210, red=50, green=50, blue=50)
administrador = Administrador()
administrador.agregar_inicio(p01)
administrador.agregar_final(p02)
administrador.mostrar()