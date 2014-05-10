# coding=utf-8

from os import system
from errors import WrongMode, WrongWriteValue


def write(pin, value):
    if value not in (0,1):
        raise WrongWriteValue('Write value should be either 0 (low) or 1 (high).')

    system('gpio -g write %d %d' % (pin, value))

    return True

def mode(pin, mode):
    if mode not in ('in', 'out'):
        raise WrongMode('Mode should be either "in" or "out".')

    system('gpio -g mode %d %d' % (pin, mode))

    return True