from setuptools import setup, find_packages

setup(
    name="rock_paper_scissors",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["gymnasium", "numpy", "pettingzoo", "pygame"],
)