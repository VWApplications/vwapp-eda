# flake8: noqa
from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# Muda para o diretório desse arquivo
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='vwapp-eda',
    version='0.2.1',
    url='https://github.com/VictorDeon/vwapp-eda',
    license='MIT License',
    author='Victor Deon',
    author_email='vwapplication@gmail.com',
    keywords='python python3 EDA',
    description=u'Pacote de estruturas de dados e algorítmos em python',
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
      'Development Status :: 4 - Beta',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[]
)
