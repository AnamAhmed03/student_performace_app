from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    Returns a list of requirements from a given file.
    Ignores "-e ." which is used for editable installs.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
name='student_performance_prediction',
version='0.0.1',
author='Anam',
author_email='anamkhan3aug@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)