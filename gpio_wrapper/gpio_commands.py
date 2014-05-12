# coding=utf-8

from os import system
from errors import WrongMode, WrongWriteValue, WrongPinNumber


def write(pin, value):
    if value not in (0, 1):
        raise WrongWriteValue('Write value should be either 0 (low) or 1 (high).')
    if pin not in xrange(0, 26):
        raise WrongPinNumber('GPIO pin number expected to be between 0 and 25.')

    system('gpio -g write %d %d' % (pin, value))

    return True


def mode(pin, set_mode):
    if set_mode not in ('in', 'out'):
        raise WrongMode('Mode should be either "in" or "out".')
    if pin not in xrange(0, 26):
        raise WrongPinNumber('GPIO pin number expected to be between 0 and 25.')

    system('gpio -g mode %d %s' % (pin, set_mode))

    return True