from setuptools import find_packages,setup
from typing import List

HYP_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
        """
        This fun return list of requirements
        """
        requirements = []
        with open(file_path) as file_obj:
                requirements = file_obj.readlines()
                requirements = [req.replace("\n","") for req in requirements]
                if HYP_E_DOT in requirements:
                        requirements.remove(HYP_E_DOT)

        return requirements                

setup(
        name= 'MLProject',
        version='0.1',
        author='Nandu',
        author_email='admanenandkumar8@gmail.com',
        packages= find_packages(),
        install_req = get_requirements('requirements.txt')
)