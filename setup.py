from setuptools import setup , find_packages 
import os
from datetime import datetime
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(filepath:str)->List[str]:
    requirements = []
    try:
        with open(filepath) as file_obj:
            obj = file_obj.readlines()
            obj = [req.replace("\n" , "") for req in requirements]
            
            if HYPEN_E_DOT in requirements:
                obj.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print("FileNotFoundError")
    
    return requirements
    
    

setup(
    name="NetworkSequrity",
    author= "Jatin Agrawal",
    author_email="agrawaljatin405@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)