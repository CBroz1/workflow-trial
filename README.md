# Workflow for trialization of sessions

This directory provides an example workflow to save the continuous behavior data, using
the following datajoint elements

+ [element-lab](https://github.com/datajoint/element-lab)
+ [element-animal](https://github.com/datajoint/element-animal)
+ [element-session](https://github.com/datajoint/element-session)
+ [element-trial](https://github.com/datajoint/element-trial)

This repository provides demonstrations for:
1. Setting up a workflow using different elements (see [pipeline.py](workflow_trial/pipeline.py))
2. Ingestion of data/metadata based on:
    + predefined file/folder structure and naming convention
    + predefined directory lookup methods (see [workflow_trial/paths.py](workflow_trial/paths.py))
3. Ingestion of trialized continuous behavior.

## Workflow architecture

The trialized behavior workflow presented here uses components from three upstream
DataJoint elements (element-lab, element-animal and element-session) and assembled
together to a functional workflow.

### element-lab

![element-lab](
https://github.com/datajoint/element-lab/raw/main/images/element_lab_diagram.svg)

### element-animal

`subject` contains basic information of subjects.
![element-animal](
https://github.com/datajoint/element-animal/blob/main/images/subject_diagram.svg)

### element-session

`session` is designed to handle metadata related to data collection, including
collection datetime, file paths, and notes. Most workflows will include element-session
as a starting point for further data entry.
![session](https://github.com/datajoint/element-session/blob/main/images/session_diagram.svg)

### element-trial

`trial` is designed to segment a continuous recording into trials, repeated windows,
typically conditions. Instantaneous or continuous events may occur within trials.

`event` is designed to handle paradigms that designate events (e.g., subject behavior)
within a session without trials.

### This workflow

This workflow serves as an example of the upstream part of a typical data workflow, for
examples using these elements with other data modalities refer to:

+ [workflow-array-ephys](https://github.com/datajoint/workflow-array-ephys)
+ [workflow-calcium-imaging](https://github.com/datajoint/workflow-calcium-imaging)

## Installation instructions

+ The installation instructions can be found at the 
[datajoint-elements repository](https://github.com/datajoint/datajoint-elements/blob/main/gh-pages/docs/install.md).

## Interacting with the DataJoint workflow

+ Please refer to the following workflow-specific
[Jupyter notebooks](/notebooks) for an in-depth explanation of how to run the
workflow ([01-Explore_Workflow.ipynb](notebooks/01-Explore_Workflow.ipynb)).
