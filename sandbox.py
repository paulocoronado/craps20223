from Dado import Dado

dado_1=Dado()
dado_2=Dado()


dado_1.girar()
dado_2.girar()

juego= dado_1.getValor()+dado_2.getValor()

print(juego)

