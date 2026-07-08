from setuptools import setup, find_packages

from typing import List


HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirments
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","")for req in requirements]


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name="ML-Project",
    version="0.0.1",
    author="Jaswanth Madamanchi",
    author_email="jaswanth.m.ai@gmail.com",
    Packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)