from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='HUST_PPS',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy>=2.1.1',
        'sympy>=1.11.1'
    ],
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
)