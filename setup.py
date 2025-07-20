''' setup.py file is an essential part of Python projects, especially for packaging and distribution. It defines the metadata about the project, such as its name, version, author, and dependencies. This file is crucial for installing the project in a virtual environment or on other systems. 
It also specifies the packages to be included, making it easier for users to install the project with all its requirements. The setup.py file is typically used with tools like pip and setuptools to manage Python packages effectively.
'''

from setuptools import setup, find_packages  #it consider which ever file contains __init__.py file as a package
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements from a file and returns them as a list.
    :param file_path: Path to the requirements file.
    :return: List of requirements.
    """
    try:
        with open(file_path, 'r') as file:
            requirements = file.readlines()
        return [req.strip() for req in requirements if req.strip() and not req.startswith('-e')]
    except FileNotFoundError:
        print(f"Warning: The file {file_path} was not found. Returning an empty list.")

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Harika',
    author_email='harikakundrapu216@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)