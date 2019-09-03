# BandRatios

Project repository for exploring frequency band ratio measures.

## Overview

Band ratios are a common measure in neuroscientific investigations, in which the the ratio of average power between two bands is examined as a feature of interest and potential biomarker in M/EEG, ECoG and LFP data analyses. Band ratios are a common measure in cognitive neuroscience, including in some clinical work. This repository contains a project examining the properties of band ratios, and what they reflect.

## Requirements

This repository requires Python >= 3.7 to run and uses the following dependencies:

 - [numpy](https://github.com/numpy/numpy) >= 1.16.2
 - [scipy](https://github.com/scipy/scipy) >= 1.2.1
 - [MNE](https://github.com/mne-tools/mne-python) >= 0.18.2
 - [FOOOF](https://github.com/fooof-tools/fooof) >= 1.0.0rc1

Optionally, if you want to re-run the literature search, you will need:

 - [lisc](https://github.com/lisc-tools/lisc) >= 1.0.0

Installing the [Anaconda](https://www.anaconda.com/distribution/) distribution and then running `pip install mne` and `pip install fooof` will get you set up to re-run the code for this project.

## Repository Layout

This project repository is set up in the following way:

- `notebooks/` is a collection of jupyter notebooks that step through the project, and create all the figures in the paper.
- `scripts/` is a set of stand alone scripts that runs parts of the project
- `figures/` holds all figures produced from `notebooks/` and `scripts/`
- `bratios` is a custom module with code to analyze and plot data for this project
