#For building/creating libraries

from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    ## this will give the list of installments present in requirements.txt

    requirements_list:List[str] =[]
    return requirements_list


setup(
    name='sensor',
    author='SanyuktaP',
    version='0.0.1',
    authon_mail='spartan71972@gmail.com',
    packages=find_packages(),
    install_requires=[]
)