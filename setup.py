#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path
import sys

here = path.abspath(path.dirname(__file__))

long_description = """"
# Workflow for trialized experiments

Build a workflow for trialized data using DataJoint Elements
+ [elements-session](https://github.com/datajoint/element-session)
+ [elements-behavior](https://github.com/datajoint/element-behavior)
+ [elements-trial](https://github.com/datajoint/element-trial)
"""

with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

setup(
    name='workflow-trial',
    version='0.0.1',
    description="DataJoint Elements for Trialized Experiments",
    long_description=long_description,
    author='DataJoint',
    author_email='info@vathes.com',
    license='MIT',
    url='https://github.com/datajoint/workflow-behavior',
    keywords='neuroscience behavior deeplabcut datajoint',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=requirements,
)
