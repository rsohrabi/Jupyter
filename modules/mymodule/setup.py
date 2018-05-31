import os
from setuptools import setup
# after making the 'dist' package, you can install using pip.
# pip install mymodule_1.0.tar.gz

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()
	
setup(
	name='mymodule',
	version='1.0',
	description='first python module',
	author='Rocky Sohrabi',
	author_email='rockysohrabi@hotmail.com',
	url='tobedone@xx.com',
	py_modules=['mymodule'],
)