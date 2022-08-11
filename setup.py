from distutils.core import setup
from setuptools import find_packages
import os

setup_path = os.path.abspath(os.path.dirname(__file__))

setup(name='libfacedetection',
      version='1.0',

      python_requires='>=3',
      packages=find_packages(),
      )

