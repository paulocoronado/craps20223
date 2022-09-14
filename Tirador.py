from Dado import Dado
from Ficha import Ficha

class Tirador:

    def __init__(self):
        self.dado_1=Dado()
        self.dado_2=Dado()
        self.ficha=Ficha()
        self.ficha.setValor(5)

    def lanzar(self):
        self.dado_1.girar()
        self.dado_2.girar()
        return self.dado_1.getValor()+ self.dado_2.getValor()



