#!/usr/bin/env python
import sys

from random import choice
vel_max = 40

def prbs():
    while True:
        return choice(xrange(0,51))


def prbs_live():
    while True:
        yield choice([0,1])