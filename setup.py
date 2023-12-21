from setuptools import find_packages
from setuptools import setup

setup(
    name='cGenFF Scraper',
    version='1.1.3',
    description='Clean and send your pdb to cGenFF from your terminal and prepare your ligand for MD',
    author=' Pipitò',
    author_email='pipitol@uni.coventry.ac.uk',
    python_requires=">=3.6.6",
    packages=find_packages(),
    install_requires=[
    'mechanize',
    'setuptools'
    ],
)

