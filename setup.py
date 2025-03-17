'''
A setup.py file is essential for packaging and distributing
Python projects. It serves as a build script for the setuptools 
package, which helps define the project structure and dependencies.
When you create a setup.py file, you can easily install the project
using pip install . and share it with others through platforms
 like PyPI (Python Package Index).
'''

from setuptools import find_packages,setup
from typing import List

requirement_lst:List[str]=[]

def get_requirements()->List[str]:
    """
    This function will return list of requirements

    """
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not Found")

    return requirement_lst

print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Karanbir Bhagat",
    author_email="karanbiriitkgp@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

