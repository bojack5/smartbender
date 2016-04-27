from conf import pines
import stepper.stepper as st

pins = pines['nema23-2']

Nema23 = st.Nema23(pins['enable'] , pins['direccion'] , pins['pulso'])

Nema23.avance(0,1000,1000)
