"""setup module"""

from setuptools import setup, find_packages

with open('README.md', encoding="utf-8") as f:
    readme = f.read()

with open('LICENSE', encoding="utf-8") as f:
    _license = f.read()

with open('requirements.txt', encoding="utf-8") as f:
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
    license=_license,
    packages=find_packages()
)
