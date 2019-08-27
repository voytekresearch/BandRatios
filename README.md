# BandRatios
Project repo for exploring frequency band ratio measures. 

### Background
Given a power density spectrum, band ratios find the ratio of average power between two bands in order to gain some deeper insight
about the source of the PSD. For example, ADHD is thought to be characterized by higher Theta/Beta power compared to non ADHD subjects. This repository aims to investigate how valid band ratios are at measuring physiological phenomena and to what extent.

##### 0-Introduction-to-Band-Ratios
This notebook introduces the domain band ratios are used in and walksthrough how to calculate a band ratio.

###### 1-Ratio-Calculation-Methods
This notebook simulates power spectra to demonstrate how changing spectral features could yield the same ratio measure. This is done both when power spectra include and do not include oscillations.

##### 2-Simulation-Generation
This notebook walksthrough how spectra were simulated. There are two types of simulations involved in this project - single parameter variations and interacting parameter variations. This notebook shows how both simulations are run and shows resulting power spectra of the parameter manipulation.

##### 3-Simulation-Analysis
Here we calculate the Theta/Beta ratios for the data we previously generated. We then plot the results using a line graph for single parameter simulations, and a heatmap for interacting parameter simulations.

##### 3a-Rotation-Explore
In this notebook we explore the effects on band ratios when we rotate a power spectra by an amount about a given frequency. We find that these two variables makes rotation frequency unimpactful.

##### 4-EEG-Dataset-Analysis
This notebook examines data from the ChildMind Institute to find the relationship between spectral features and various band ratios at different regions of cortex.

##### 4a-Topos
We create topographies for each spectral feature from the theta, alpha, and beta bands, as well as various ratio measures.
