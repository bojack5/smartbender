from stepper.stepper import Nema42
from cilindros.cilindro import Doble

tr = Doble(0,1)
a = Nema42(12,7)

tr.entrar()
a.parar()

