# BandRatios
Project repo for exploring frequency band ratio measures. 

### Background
Given a power density spectrum, band ratios find the ratio of power between two bands in order to gain some deeper insight
about the source of the PSD. For example, ADHD is thought to be characterized by higher Theta/Beta power compared to non ADHD subjects. This repository aims to investigate how valid band ratios are at measuring physiological phenomena and to what extent.

##### 0-Introduction-to-Band-Ratios
This notebook introduces the background behind band ratios - where the data comes from, data significance, and our approach to this project.

###### 1-Ratio-Calculation-Methods
This notebook introduces three ways of calculating a band ratio - 1 cannonical method and 2 alternative measures.

Average Power Ratio: calc_band_ratio finds the average power within a band and divides by the number of samples which have power. The same is done for another band and a ratio is taken of the two.

Central Frequency Ratio: calc_cf_power_ratio finds the ratio of the maximum power within the two bands, which is found by the central frequency within the two bands.  Oscillation specific.

Density Ratio: calc_density_ratio sums all the power within a band and divides by the band width. This is similar to the cannonical approach with the distinction that the cannonical approach instead divides by number of samples.

##### 2-Simulation-Generation
This notebook generates synthetic PSDs to examine how slope and oscillatory parameters affect band ratios. 

Slope: FooofGroup objects are made with n_trials. Each fooofGroup object has a different slope ranging from 'inc' to 'end_slope' in increments of 'inc'. The 3 discussed ratio measures are taken and saved to the ./dat directory
[Slope][Ratio_Method][Trial]. The data is saved to /dat using numpy.save()

Center Frequency: Since ratios require 2 bands, one band is selected to be stationary while the other will generate fooofGroup objects of size n_trials to sweep across the non stationary band's bandwidth. Again 3 ratio measures will be taken for each variation in Center Frequency and saved to the ./dat directory.
[Center_Frequency][Ratio_Method][Trial]

Amplitude: One band is set stationary while the other is centered at its bandwith and examines the effects of amplitude change by generating FooofGroups object of size n_trials for each variation in amplitude from 0 to 'end_amp'. 3 ratio measures are taken and saved into the ./dat directory
[Amplitude][Ratio_Method][Trial]

Band Width: 

##### 3-Analysis
This notebook uses the data introduced last notebook to find the average of all trials which transforms the 3D array to a 2D array [Slope][Ratio Method]. Then pandas is used to easily access data such that plotting is easy.