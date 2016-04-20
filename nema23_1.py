#!/usr/bin/env python
from conf import pines
import stepper.stepper as st

pins = pines['nema23-1']

Nema23 = st.Nema23(pins['enable'] , pins['direccion'] , pins['pulso'])

Nema23.avance(0,1000,1000)


