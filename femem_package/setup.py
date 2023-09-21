from os.path import join, dirname
from setuptools import setup

VERSION = (1, 0, 0)

__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = open(join(dirname(__file__), 'requirements.txt'))
install_requires = f.readlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="femem",
    version=__versionstr__,
    author="Batuhan Şanlı",
    author_email="batuhansanli@gmail.com",
    description="A Python Library for Finite Element Analysis of Truss Systems with Energy Minimization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/batuhan0sanli/femem",
    packages=setuptools.find_packages(),
    # packages=["femem", "femem.options", "femem.structure", "femem.structure.controls"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license="MIT License",
    install_requires=install_requires,
)
