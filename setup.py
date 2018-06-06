# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='Practica Final',
    version='1.0.0',
    description='Practica final en la que se usará django como framework web, lettuce para tests bdd y test unitarios '
                '(mockeando en alguno de ellos).',
    long_description=readme,
    author='Alfonso Cuesta y Arturo Lara'
)