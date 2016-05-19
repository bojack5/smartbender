#!/usr/bin/env python
import sys

from random import choice
vel_max = 40

def prbs():
    while True:
        return choice([-vel_max, 0 , vel_max])


def prbs_live():
    while True:
        yield choice([0,1])