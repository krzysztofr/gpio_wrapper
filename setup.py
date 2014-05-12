#!/usr/bin/env python

from distutils.core import setup

execfile('gpio_wrapper/version.py')

setup(
    name='gpio_wrapper',
    version=__version__,
    description='Simple wrapper for gpio.',
    long_description=open('README.rst').read(),
    author='Krzysztof Rakowski',
    author_email='krzysztof@rakowski.pro',
    url='http://github.com/krzysztofr/gpio_wrapper',
    license='MIT',
    packages=[
        'gpio_wrapper'
    ],
    scripts=['bin/gpio-init'],
    #classifiers = [
    #    'TODO: Add trove classifiers (http://pypi.python.org/pypi?%3Aaction=list_classifiers)'
    #]
)
