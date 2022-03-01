#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

pkg_name = 'workflow_trial'
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
with open(path.join(here, pkg_name, 'version.py')) as f:
    exec(f.read())

setup(
    name='workflow-trial',
    version=__version__,
    description="DataJoint Elements for Trialized Experiments",
    long_description=long_description,
    author='DataJoint',
    author_email='info@datajoint.com',
    license='MIT',
    url='https://github.com/datajoint/workflow-trial',
    keywords='neuroscience trial datajoint',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=requirements,
)
