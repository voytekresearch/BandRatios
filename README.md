# BandRatios

Project repository for the `BandRatios` project, exploring frequency band ratio measures.

## Overview

Band ratios are a common measure in neuroscientific investigations, in which the the ratio of average power between two bands is examined as a feature of interest and potential biomarker in M/EEG, ECoG and LFP data analyses. Band ratios are a common measure in cognitive neuroscience, including in some clinical work. This repository contains a project examining the properties of band ratios, and what they reflect.

## Requirements

This repository requires Python >= 3.7 to run.

This requires standard scientific python packages:
- [numpy](https://github.com/numpy/numpy)
- [pandas](https://github.com/pandas-dev/pandas)
- [scipy](https://github.com/scipy/scipy)
- [matplotlib](https://github.com/matplotlib/matplotlib)
- [seaborn](https://github.com/mwaskom/seaborn)

You can get and manage these dependencies usingthe [Anaconda](https://www.anaconda.com/distribution/) distribution, which we recommend.

In addition, this project requires the following dependencies:

 - [MNE](https://github.com/mne-tools/mne-python) >= 0.18.2
 - [FOOOF](https://github.com/fooof-tools/fooof) >= 1.0.0
 - [lisc](https://github.com/lisc-tools/lisc) >= 1.0.0

You can install the extra required dependencies by running:

```
pip install mne
pip install fooof
pip install lisc
```

## Repository Layout

This project repository is set up in the following way:

- `notebooks/` is a collection of Jupyter notebooks that step through the project and create the figures
- `scripts/` contains stand alone scripts that run parts of the project
- `figures/` holds all figures produced from `notebooks/` and `scripts/`
- `bratios/` is a custom module containing the code for analyses and visualizations of this project
