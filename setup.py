import os
from setuptools import setup, find_packages

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'python-template',
    version = '0.0.0',
    author = 'Davide Poletti',
    author_email = 'davide.pole@gmail.com',
    description = ('Template for python packages'),
    license = 'GPLv3',
    keywords = '',
    url = 'https://github.com/dpole/python-template',
    packages = find_packages(),
    long_description = read('README.rst'),
    install_requires = [
    ],
)
