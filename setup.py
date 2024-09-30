from setuptools import setup, find_packages
from pathlib import Path

# Đọc nội dung từ README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='HUST_PPS',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy>=2.1.1',
        'sympy>=1.11.1'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',  # Xác định loại nội dung là Markdown
)