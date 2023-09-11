from setuptools import find_packages, setup
from typing import List

"""
Use pip install -r requirements.txt to install the requirements.
OBS: you need to activate the env created with python 3.11.5 (lasted cheked version).
and be in the folder where the requirements.txt is located in your cmd.
"""


def get_requirements(file_path: str) -> List[str]:
    """
    function returns the requirements list from a file.
    """
    try:
        with open(file_path, "r") as file_obj:
            requirements = [line.strip() for line in file_obj.readlines()]
        return requirements
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")


setup(
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
