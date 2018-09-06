"""Tools and utilities for generating simulations."""

import numpy as np

from fooof import FOOOF, FOOOFGroup
from fooof.analysis import *
from fooof.synth import gen_group_power_spectra, param_sampler, gen_power_spectrum

from utils.ratios import *
###################################################################################################
###################################################################################################



###################################################################################################
###################################################################################################

def gen_sample():
    """
    generates a sample for generating a fooof PSD with a theta, alpha, and beta oscillation
    
    Output
    -------
    sample : array
            [Theta freq, Theta amp, Theta SD,
             Alpha freq, Alpha amp, Alpha SD,
             Beta freq,  Beta amp, Beta SD] 
    """
    
    sample = []
    
    sample.append(np.random.uniform(4, 7)) #Theta freq
    sample.append(np.random.uniform(.35,.75)) #Theta Amp
    sample.append(np.random.uniform(.25,1.05))#Theta SD
    
    sample.append(np.random.uniform(8, 12)) #Alpha freq
    sample.append(np.random.uniform(.25,.55)) #Alpha Amp
    sample.append(np.random.uniform(.25,1.05))#Alpha SD
    
    sample.append(np.random.uniform(18, 25)) #Beta freq
    sample.append(np.random.uniform(.4,.75)) #Beta Amp
    sample.append(np.random.uniform(.25,1.05))#Beta SD
    
    
    return sample

def set_vary_bands(low_band, high_band, stationary):
    """ Determines which of two bands is the band that will vary and will remain stationary
    
    ---------
    low_band : [float,float] : bandwidth to be assigned 'stationary' or 'vary'
    high_band : [float,float] : bandwidth to be assigned 'stationary' or 'vary'
    stationary : string : 'low' or 'high' to determine which bandwidth will remain stationary, other
                           will be assigned vary
    
    OUTPUT
    ----------
    tuple : (vary, stationary)
    
    """
    
    if(stationary == 'high'):
        vary = low_band
        stat = high_band
        
    # 'low' is not checked as it has a usage check before this function is called    
    else: 
        vary = high_band
        stat = low_band
    return (vary, stat)

def gen_trials(n_trials, bg = [0,1], gauss_params = []):
    """
    Simulates n_trials of fooof synthesized PSDs in the form of FooofGroup object.
    
    ----------
    
    n_trials : int : number of PSDs in FooofGroup object
    bg : [float, float] background params to generate PSD
    gauss_params [float, float] oscillations to add to aperiodic bg parameters
    
    OUTPUT
    ----------
    
    FooofGroup object of simulated PSDs
    """
    #100 trails for each treatment and control sim
    freqs, powers, _ = gen_group_power_spectra(n_trials, [1,50], bg, gauss_params, nlvs=np.random.uniform(.005,.02))
    fg = FOOOFGroup()
    fg.fit(freqs, powers)
    
    return fg

################~~~~ Slope ~~~~################

def gen_varying_slope(low_band, high_band, fname="./dat/slope_data", inc = .25, end_slope = 3,n_trials=100):
    """
    Generates 100 simulated PSDs with slopes ranging from .25 up to and including 'end_slope' without
    oscillations. For each set of 100 trials, 2 ratio measures are calculated. Output will be saved
    as a 3D array to './dat' in the form of [slope][ratio_measure][trial]
    
    -------
    end_slope : float: (optional) = 3 ; generates PSDs with slopes ranging from .25 to end_slope in .25 increments
    low_band_range: numerator used to calculate band ratio
    high_band_range: denominator used to calculate band ratio
    fname : string : (optional) = "slope_data" ; name of output file
    inc : float : (optional) = .25 ; increment size of generated slopes
    n_trials : int : (optional) = 100 ; number of trials simulated per each slope value
    
    Output
    ------
    3-D array [slope][ratio method][trial]
    """
    
    # Check for valid inc
    if( inc <= 0 or end_slope < inc or n_trials < 1):
        print(gen_varying_slope.__doc__)
        return
    
    res = []
    i = 1

    # iterates and makes simulations for each slope value
    while(i*inc < end_slope):
        
        bg = [0,i*inc]
        
        # creates 100 simulated fooof PSDs
        fg = gen_trials(int(n_trials),bg) 
        
        # calculates ratios
        res.append(get_group_ratios(fg,low_band,high_band))
        i+=1
    np.save(fname, res)

################~~~~ CENTER FREQUENCY ~~~~################
def gen_varying_cf(low_band, high_band, stationary, fname="./dat/cf_data", inc = .1, n_trials = 100):
    """
    This is a convenience function to simulate data about how varying CF influences band ratios.
    One band is set stationary, either 'low' or 'high' centered at its bandwidth while the other band 
    will vary CFs from the beginnning of its width until its end in increments of inc
    For each iteration 100 trials will be generated where
    both bands are set, 3 ratio measures will be calculated. The output will be a 3D array in the
    form of [CF][ratio_method][trial]. The output is saved to /dat
    ASSUMPTIONS:
    Slope = 1 ; Offset = 0 ; Amplitude = .5 ; BandWidth = 1 ; Stationary CF centered
    
    ---------------
    low_band : list : numerator when calculating band ratios, also potential stationary band
    high_band : list : denominator when calculating band ratios, also potential stationary band
    stationary : string : sets which band will remain constant 'low' or 'high'
    fname : string : output file name
    inc : float : (optional) = .1 resolution for simulating varying amplitudes
    n_trials : int : (optional) = 100 ; number of trials simulated per each cf value
    """
    res = []
    
    # Check if 'stationary' is set to a correct value
    if(stationary not in ['low','high'] or inc <= 0 or n_trials < 1):
        
        print(gen_varying_cf.__doc__)
        return
    
    # Set the stationary and varying band 
    vary, stat = set_vary_bands(low_band, high_band, stationary)
    
    i = 0
    while(vary[0]+ i*inc < vary[1] ):
        gauss_params = gen_sample_cf(vary, stat, i, inc)
        
        # creates 100 simulated fooof PSDs
        fg = gen_trials(n_trials, gauss_params = gauss_params)
        
        # calculates band ratios
        res.append(get_group_ratios(fg, low_band, high_band))
        i+=1
    np.save(fname, res)                          

def gen_sample_cf(vary, stat, i, inc):
    """
    Generates oscillations of varying center frequencies based on current iteration
    [vary CF, vary amplitude, BW, centered stationary CF, stationary amp, BW]
    
    vary : [float, float]
    stat : [float, float]
    i : int :ith iteration
    inc : float : resolution to generate varying CF
    """
    return [vary[0]+i*inc, .5, 1, np.mean(stat), .5, 1]    
################~~~~ Amplitude ~~~~################

def gen_varying_amp(low_band, high_band, stationary, fname="./dat/amp_data", end_amp = 1.5, inc = .1, n_trials = 100):
    """
    This is a convenience function to simulate data about how varying Amplitude influences band ratios.
    One band is set stationary, either 'low' or 'high' while the other band will vary in amplitude from .1 to end_amp.
    The CF for both bands will be the middle of their band
    For each iteration 100 trials will be generated where
    both bands are set, 3 ratio measures will be calculated. The output will be a 3D array in the
    form of [Amp][ratio_method][trial]. The output is saved to /dat
    ASSUMPTIONS:
    Slope = 1 ; Offset = 0 ; CF = center of band ; BandWidth = 1
    
    ---------------
    low_band : list : numerator when calculating band ratios, also potential stationary band
    high_band : list : denominator when calculating band ratios, also potential stationary band
    stationary : string : sets which band will remain constant 'low' or 'high'
    fname : string : (optional) = "amp_data" output file name
    end_amp : float : (optional) = 1.5 highest simulated amplitude
    inc : float : (optional) = .1 resolution for simulating varying amplitudes
    n_trials : int : (optional) = 100 ; number of trials simulated per each amplitude value
    """
    res = []
    
    # Check if 
    #  -'stationary' is set to a correct value
    #  - inc is positive
    #  - end_amp is greater than inc
    if(stationary not in ['low','high'] or inc <= 0 or end_amp < inc or n_trials < 1):
        
        print(gen_varying_amp.__doc__)
        return
    
    # Set the stationary and varying band 
    vary, stat = set_vary_bands(low_band, high_band, stationary)

    i = 0
    while( i * inc < end_amp):
        
        gauss_params = gen_sample_amp(vary,stat, i,inc)
        
        # creates 100 simulated fooof PSDs
        fg = gen_trials(n_trials, gauss_params = gauss_params)
        
        # calculates ratios for all 100 trials
        res.append(get_group_ratios(fg, low_band, high_band))
        i+=1
    np.save(fname, res)
    
def gen_sample_amp(vary,stat, i,inc):
    """
    Generates oscillations of varying amplitude based on current iteration
    [centered vary CF, varied amplitude, BW, centered stationary CF, stationary amp, BW]
    
    vary : [float, float]
    stat : [float, float]
    i : ith iteration
    """
    return [np.mean(vary), inc * i, 1, np.mean(stat), .5, 1]

################~~~~ Band Width ~~~~################

def gen_varying_bw(low_band, high_band, stationary, fname="./dat/band_width_data", inc = .1, end_width = 2,n_trials = 100):
    """
    This is a convenience function to simulate data about how varying bandwidth influences band ratios
    One band is set stationary, either 'low' or 'high' while the other band will vary in band width from
    .2 to 1.2. Both bands will be centered at the middle of their respective frequency band. Amplitude 
    is set to .5. For each iteration 100 trials will be generated where both bands are set, 3 ratio
    measures will be calculated. The output will be a 3D list in the form of [BW][ratio_method][trial]
    the output will be saved to /dat
    
    ---------------
    low_band : list : numerator when calculating band ratios, also potential stationary band
    high_band : list : denominator when calculating band ratios, also potential stationary band
    stationary : string : sets which band will remain constant 'low' or 'high'
    fname : string : (optional) = "amp_data" output file name
    end_width : float : (optional) = 1.5 highest simulated band width
    inc : float : (optional) = .1 resolution for simulating varying band widths
    n_trials : int : (optional) = 100 ; number of trials simulated per each band width value
    """
    res = []
    
    # Check if 
    #  -'stationary' is set to a correct value
    #  - inc is positive
    #  - end_width is greater than inc
    if(stationary not in ['low','high'] or inc <= 0 or end_width < inc or n_trials < 1):
        
        print(gen_varying_bw.__doc__)
        return
    
    # Set the stationary and varying band 
    vary, stat = set_vary_bands(low_band, high_band, stationary)
    
    #iterates Bandwidths
    i = 1
    while (i*inc < end_width):
        
        gauss_params = gen_sample_bw(vary, stat, i,inc)
        
        # creates 100 simulated fooof PSDs
        fg = gen_trials(n_trials, gauss_params = gauss_params)
        
        #calculates ratios for all 100 trials
        res.append(get_group_ratios(fg, low_band, high_band))
        i+=1
    np.save(fname, res)

def gen_sample_bw(vary, stat, i, inc):
    """
    Generates oscillations of varying band widths based on current iteration
    [centered vary CF, vary amplitude, BW, centered stationary CF, stationary amp, BW]
    
    vary : [float, float]
    stat : [float, float]
    i : ith iteration
    
    """
    return [np.mean(vary), .5, .1 * inc, np.mean(stat), .5, 1]