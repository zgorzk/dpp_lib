from setuptools import setup, find_packages

setup(
    name='biblioteka',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='An example python package',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='https://github.com/zgorzk/dpp_lib.git',
    author='Dominik Kinastowski',
    author_email='242081@student.pwr.edu.pl'
)