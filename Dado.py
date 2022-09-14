import random

class Dado:
    #Método constructor
    def __init__(self):
        self.valor=0

    def girar(self):        
        self.valor=random.randint(1,6)

    def getValor(self):
        return self.valor
