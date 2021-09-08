# BandRatios

`BandRatios` project repository: exploring frequency band ratio measures in electrophysiological data.

[![Paper](https://img.shields.io/badge/DOI-10.1523/ENEURO.0192--20.2020-informational.svg)](https://doi.org/10.1523/ENEURO.0192-20.2020 )

## Overview

Band ratios are a common measure in neuroscience, and are commonly used across cognitive and clinical investigations. In band ratio measures, the ratio of power between two frequency bands are examined as a feature of interest and potential biomarker in M/EEG, ECoG, and LFP data analyses. 

In this project, we explore the properties of band ratio measures, and how they relate to other spectral features. Specifically, we examine if band ratio measures are specific to periodic power, and to what degree they reflect other periodic and aperiodic spectral features.

This project was completed in the [VoytekLab](https://voyteklab.com/) at UC San Diego, by 
[Thomas Donoghue](https://github.com/TomDonoghue), 
[Julio Dominguez](https://github.com/ArcadeShrimp), and 
[Bradley Voytek](https://github.com/voytek).

## Project Guide

You can step through all the analyses and results in this project by stepping through the `notebooks`.

If you want to re-run the project, there are some parts that are done by stand-alone scripts, which are available in the `scripts` folder. These scripts are also described in the notebooks.

## Reference

This project is described in the following paper:

    Donoghue T, Dominguez J & Voytek B (2020). Electrophysiological Frequency Band Ratio Measures 
    Conflate Periodic and Aperiodic Neural Activity. eNeuro, 7(6) DOI: 10.1523/ENEURO.0192-20.2020

Direct Link: https://doi.org/10.1523/ENEURO.0192-20.2020 

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

- `bratios/` is a custom module containing code used for analyses and visualizations
- `data/` includes data for the project, include simulated data, processed EEG data, and output files
- `figures/` contains figures for the project, which are created in `notebooks/` and `scripts/`
- `notebooks/` is a collection of Jupyter notebooks that step through the project and create the figures
- `scripts/` contains stand alone scripts that run parts of the project

## Data

This project uses simulated data, literature data, and electroencephalography (EEG) data.

The simulations are all done using the [FOOOF](https://github.com/fooof-tools/fooof) tool and associated simulation framework. Code for generating these simulations is included in this repositry, and all simulated data reported upon is available in the `data/` folder.

The literature data was collected with [LISC](https://github.com/lisc-tools/lisc), a tool for collecting and analyzing literature data. Code to re-run the literature data collection is available in the `notebooks/`. All collected literature data used in this project is available in the `data/` folder.

The EEG data is open-access data from the 'Multimodal Resource for Studying Information Processing in the Developing Brain' or [MIPDB](http://fcon_1000.projects.nitrc.org/indi/cmi_eeg/) dataset. This dataset was collected and released by the [ChildMind Institute](https://childmind.org/). Raw data can be downloaded through their data portal. The processed power spectra, upon which we operate, and the calculated output measures for this project are collected and available in the `data/` folder.
