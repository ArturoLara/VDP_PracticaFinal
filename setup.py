# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='Practica 3 BDD',
    version='1.0.0',
    description='Practica para contar el numero de palabras que aparecen en un texto en una web con Django y probandolo con Lettuce',
    long_description=readme,
    author='Alfonso Cuesta y Arturo Lara'
)