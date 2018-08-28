# BandRatios
Project repo for exploring frequency band ratio measures. 

### Background
Given a power density spectrum, band ratios find the ratio of power between two bands in order to gain some deeper insight about the source of the PSD. For example, ADHD is thought to be characterized by higher Theta/Beta power compared to non ADHD subjects. This repository aims to investigate how valid band ratios are at measuring physiological phenomena and to what extent.

##### 0-PSDRatioExplorations
This notebook examines how the ratio two PSDs can differ with and without synthetic calculation. The cannonical method for calculating band ratio is used, namely finding the average power within a band and dividing it by the average power in another band.

###### 1-Ratio-Calculation-Methods
This notebook introduces two more ways of calculating band ratios. Functions can be found in /utils/ratios

Central Frequency Ratio: calc_cf_power_ratio finds the ratio of the maximum power within the two bands, which is found by the central frequency within the two bands.  Oscillation specific

Density Ratio: calc_density_ratio sums all the power within a band and divides by the band width. This is similar to the cannonical approach with the distinction that the cannonical approach instead divides by number of samples.

##### 2-Slope-Simulations
This notebook generates synthetic PSDs to examine how slope affects band ratios. Sets of 100 trials of PSDs with synthetic Theta, Alpha, and Beta oscillations are generated. Each set of 100 trials has a varying slope from .25 to 5 all of which have the band ratios calculated using the 3 methods introduced so far. All the data generated comes in the form of a 3D array
[Slope][Ratio Method][Trial]. The data is saved to /dat using numpy.save()

##### 3-Analysis
This notebook uses the data introduced last notebook to find the average of all trials which transforms the 3D array to a 2D array [Slope][Ratio Method]. Then pandas is used to easily access data such that plotting is easy.