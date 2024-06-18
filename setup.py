# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='call_viz',
    version='0.1.0',
    install_requires=required,
    description='Recursive function calls visualization using Graphviz',
    long_description=readme,
    author='Théo Bori',
    author_email='nagi@tilde.team',
    url='https://github.com/theobori/recursion-digraph',
    license=license,
    packages=find_packages()
)
