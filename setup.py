from setuptools import setup


setup (
    name='chesslib',
    version='0.1.0',
    description='A library for playing classic chess.',
    author='Daniel Halvarsson',
    url='https://github.com/DanielH4/chesslib',
    install_requires=['pytest>=7.1.1, <8.0.0',
                      'jsonschema>=4.9.1, <5.0.0'],
    packages=['chesslib']
)
