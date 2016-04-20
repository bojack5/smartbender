from conf import pines
import stepper.stepper as st

pins = pines['nema42']

Nema42 = st.Nema42(pins['direccion'] , pins['pulso'])

Nema42.avance(0,2300,1000)