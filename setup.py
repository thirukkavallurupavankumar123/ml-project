from setuptools import setup, find_packages
from typing import List



def get_requirements(file_path:str) -> list:
    """
    This function reads the requirements file and returns a list of packages.

    """
    requirements= []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements =[req.replace("\n","") for req in requirements ]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements 






setup(
    name='ml_project',
    version='0.0.1',
    author='pavankumar',
    author_email='thirukkavallurupavankumar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)