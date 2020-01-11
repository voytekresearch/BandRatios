# BandRatios

Project repository for the `BandRatios` project, exploring frequency band ratio measures in electrophysiological data.

## Overview

Band ratios are a common measure in neuroscientific investigations, in which the the ratio of average power between two frequency bands are examined as a feature of interest and potential biomarker in M/EEG, ECoG and LFP data analyses. These ratio measures are commonly applied in investigations within cognitive and clinical neuroscience. In this project, we explore the properties of band ratio measures, and how they relate to other spectral features.

## Project Guide

You can follow along with this project by stepping through the whole thing, as outlined in the `notebooks`.

If you want to re-run the whole project, keep in mind that some parts are done by stand-alone scripts, available in the `scripts` folder. These scripts are also described in the notebooks.

## Reference

Coming soon!

## Requirements

This project was written in Python 3 and requires Python >= 3.7 to run.

If you want to re-run this project, you will need some external dependencies.

Dependencies include 3rd party scientific Python packages:
- [numpy](https://github.com/numpy/numpy)
- [pandas](https://github.com/pandas-dev/pandas)
- [scipy](https://github.com/scipy/scipy)
- [matplotlib](https://github.com/matplotlib/matplotlib)
- [seaborn](https://github.com/mwaskom/seaborn)

You can get and manage these dependencies using the [Anaconda](https://www.anaconda.com/distribution/) distribution, which we recommend.

In addition, this project requires the following dependencies:

 - [mne](https://github.com/mne-tools/mne-python) >= 0.18.2
 - [fooof](https://github.com/fooof-tools/fooof) >= 1.0.0
 - [lisc](https://github.com/lisc-tools/lisc) >= 0.1.0

You can install the extra required dependencies by running:

```
pip install mne, fooof, lisc
```

## Repository Layout

This project repository is set up in the following way:

- `bratios/` is a custom module containing the code for analyses and visualizations of this project
- `data/` is a collection of the project data, include simulation data, EEG data, and outputs
- `figures/` holds all figures produced from `notebooks/` and `scripts/`
- `notebooks/` is a collection of Jupyter notebooks that step through the project and create the figures
- `scripts/` contains stand alone scripts that run parts of the project

## Data

This project uses simulated data, literature data, and electroencephalography (EEG) data from an open-access repository.

The simulations are all done using the [FOOOF](https://github.com/fooof-tools/fooof) tool and associated simulation framework. All simulated data reported upon in this project is available in the `data/` folder.

The literature data was collected with [LISC](https://github.com/lisc-tools/lisc), a tool for collecting and analyzing literature data. All collected literature data used in this project is available in the `data/` folder, and code to re-run the literature data collection is available in the `notebooks/`.

The EEG data is taken from the 'Multimodal Resource for Studying Information Processing in the Developing Brain' or [MIPDB](http://fcon_1000.projects.nitrc.org/indi/cmi_eeg/) dataset. This dataset was collected and released by the [ChildMind Institute](https://childmind.org/). Raw data can be downloaded through their data portal. The processed power spectra, upon which we operate, and the calculated output measures for this project are collected and available in the `data/` folder.
