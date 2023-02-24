from setuptools import setup
from setuptools import find_packages

setup( name = 'CGCN',
version = '1.0.0',
description='CGCN: A kind of cancer gene co-occurrence network.',
url='',
author='Dian MENG',
author_email='dianmeng2-c@my.cityu.edu.hk',
license='MIT',
packages=find_packages(),
install_requires=['pandas',
'numpy',
'networkx']
)
