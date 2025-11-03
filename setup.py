from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requrements = f.read().splitlines()

setup(
    name="MLOps-Project",
    version="0.1.0",
    author="AasimDev",
    packages=find_packages(),
    install_requires=requrements,
)