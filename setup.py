from setuptools import setup, find_packages

setup(
    name='HUST_PPS',
    version='0.1.0',
    packages=find_packages(),
    install_requires = [
        'numpy>=2.1.1',
        'sympy>=1.11.1'
    ],
)