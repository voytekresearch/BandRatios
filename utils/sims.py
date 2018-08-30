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

def gen_sample_slope():
    
    return [6, .5, 1, 25, .5, 1]

def set_vary_bands(low_band, high_band, stationary):
    if(stationary == 'high'):
        vary = low_band
        stat = high_band
        
    else: 
        vary = high_band
        stat = low_band
    return (vary, stat)

def sim_slope_data(end_slope, low_band_range, high_band_range, osc=True):
    """
    Generates 100 simulated PSDs with slopes ranging from .25 to end_slope with or without oscillation
    
    -------
    end_slope : generates PSDs with slopes ranging from .25 to end_slope in .25 increments
    low_band_range: numerator used to calculate band ratio
    high_band_range: denominator used to calculate band ratio
    osc : if false PSD contains only 1/f, else, theta, alpha, and beta oscillations added
    
    Output
    ------
    3-D array [slope][ratio method][trial]
    """
    res = []
    i = 1
    if(osc==True):
        gauss_params = gen_sample_slope()
    else:
        # [] should work instead
        gauss_params = []
    while(i*.25 < end_slope):

        bg = [0,i*.25]
        
        #100 trails for each treatment and control sim
        freq, power, _ = gen_group_power_spectra(100, [1,50], bg, gauss_params, nlvs=np.random.uniform(.005,.02))
        fg = FOOOFGroup(peak_width_limits=[1,8], min_peak_amplitude=0.05, max_n_peaks=3)
        fg.fit(freq, power)
        res.append(get_group_ratios(fg,low_band_range,high_band_range))
        i+=1
    return res

################~~~~ CENTER FREQUENCY ~~~~################
def gen_varying_cf(low_band, high_band, stationary, fname=""):
    """
    This is a convenience function to simulate data about how varying CF influences band ratios.
    One band is set stationary, either 'low' or 'high' centered at its bandwidth while the other band 
    will vary CFs from the beginnning of its width until its end in increments of .1.
    For each iteration 100 trials will be generated where
    both bands are set, 3 ratio measures will be calculated. The output will be a 3D array in the
    form of [CF][ratio_method][trial]. The output is saved to /dat
    ASSUMPTIONS:
    Slope = 1 ; Offset = 0 ; Amplitude = .5 ; BandWidth = 1
    
    ---------------
    low_band : list : numerator when calculating band ratios, also potential stationary band
    high_band : list : denominator when calculating band ratios, also potential stationary band
    stationary : string : sets which band will remain constant 'low' or 'high'
    fname : string : output file name
    """
    res = []
    
    # Check if 'stationary' is set to a correct value
    if(stationary not in ['low','high']):
        
        print(gen_varying_CF.__doc__)
        return
    
    # Set the stationary and varying band 
    vary, stat = set_vary_bands(low_band, high_band, stationary)
    
    # iterations is .1 increments
    iters = (vary[1]-vary[0])*10
                              
    for i in range(iters):
        fg = gen_cf_iter(vary,stat, i, low_band, high_band)
        res.append(get_group_ratios(fg, low_band, high_band))
        i+=1
    np.save('./dat/'+ fname, res)
    

def gen_cf_iter(vary, stat, i, low_band, high_band):
    """
    Simulates 100 fooof PSDs of an instances of varying Central Frequencies
    """
    gauss_params = gen_sample_cf(vary, stat, i)
    freqs, powers, _ = gen_group_power_spectra(100, [1, 50], [0,1], gauss_params, nlvs=np.random.uniform(.005,.02))
    fg = FOOOFGroup(peak_width_limits=[1,8], min_peak_amplitude=0.05, max_n_peaks=3)
    fg.fit(freqs, powers)
    return fg
                              

# One function can be used regardless if low_band or high_band is stationary
def gen_sample_cf(vary, stat, i):
    """
    Generates oscillations of varying center frequencies based on current iteration
    [vary CF, vary amplitude, BW, centered stationary CF, stationary amp, BW]
    
    vary : [float, float]
    stat : [float, float]
    i : ith iteration
    
    """
    return [vary[0]+i*.1, .5, 1, np.mean(stat), .5, 1]

################~~~~ Amplitude ~~~~################

def gen_varying_amp(low_band, high_band, stationary, fname=""):
    """
    This is a convenience function to simulate data about how varying Amplitude influences band ratios.
    One band is set stationary, either 'low' or 'high' while the other band will vary in amplitude from .1 to 1.5.
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
    fname : string : output file name
    """
    res = []
    
    # Check if 'stationary' is set to a correct value
    if(stationary not in ['low','high']):
        
        print(gen_varying_amp.__doc__)
        return
    
    # Set the stationary and varying band 
    vary, stat = set_vary_bands(low_band, high_band, stationary)
    
    #iterates amplitudes .1 -> 1.5
    for i in range(14):
        fg = gen_amp_iter(vary,stat,i,low_band, high_band)
        res.append(get_group_ratios(fg, low_band, high_band))
        i+=1
    np.save('./dat/'+ fname, res)
        
def gen_amp_iter(vary,stat,i,low_band, high_band):
    """
    Simulates 100 fooof PSDs for an instance of varying amplitude
    
    -----------
    vary : [float, float] : band which will vary in amplitude
    stat : [float, float  : band which will remain stationaty
    i : int : ith iteration
    low_band : [float, float] : lower band of interest
    high_band : [float, float] : higher band of interest
    
    
    OUTPUT
    --------
    FOOOFGroup object of 100 trials of oscillations of a given amplitude
    """
    gauss_params = gen_sample_amp(vary, stat, i)
    freqs, powers, _ = gen_group_power_spectra(100, [1, 50], [0,1], gauss_params, nlvs=np.random.uniform(.005,.02))
    fg = FOOOFGroup(peak_width_limits=[1,8], min_peak_amplitude=0.05, max_n_peaks=3)
    fg.fit(freqs, powers)
    return fg


def gen_sample_amp(vary,stat, i):
    """
    Generates oscillations of varying amplitude based on current iteration
    [centered vary CF, varied amplitude, BW, centered stationary CF, stationary amp, BW]
    
    vary : [float, float]
    stat : [float, float]
    i : ith iteration
    """
    return [np.mean(vary),.1*(i+1),1,np.mean(stat),.5,1]

################~~~~ Band Width ~~~~################

def gen_varying_bw(low_band, high_band, stationary, fname=""):
    """
    This is a convenience function to simulate data about how varying bandwidth influences band ratios
    One band is set stationary, either 'low' or 'high' while the other band will vary in band width from
    .2 to 1.2. Both bands will be centered at the middle of their respective frequency band. Amplitude 
    is set to .5. For each iteration 100 trials will be generated where both bands are set, 3 ratio
    measures will be calculated. The output will be a 3D list in the form of [BW][ratio_method][trial]
    the output will be saved to /dat
    """
    res = []
    
    # Check if 'stationary' is set to a correct value
    if(stationary not in ['low','high']):
        
        print(gen_varying_band_width.__doc__)
        return
    
    # Set the stationary and varying band 
    vary, stat = set_vary_bands(low_band, high_band, stationary)
    i = 2
    #iterates amplitudes .2 -> 1.2
    for i in range(12):
        fg = gen_bw_iter(vary,stat,i,low_band, high_band)
        res.append(get_group_ratios(fg, low_band, high_band))
        i+=1
    np.save('./dat/'+ fname, res)
    
def gen_bw_iter(vary,stat,i,low_band, high_band):
    """
    Simulates 100 fooof PSDs for and instance of varying band width
    
    -----------
    vary : [float, float] : band which will vary in band width
    stat : [float, float  : band which will remain stationaty
    i : int : ith iteration
    low_band : [float, float] : lower band of interest
    high_band : [float, float] : higher band of interest
    
    
    OUTPUT
    --------
    FOOOFGroup object of 100 trials of oscillations of a given band width
    """
    gauss_params = gen_sample_bw(vary, stat, i)
    freqs, powers, _ = gen_group_power_spectra(100, [1, 50], [0,1], gauss_params, nlvs=np.random.uniform(.005,.02))
    fg = FOOOFGroup(peak_width_limits=[1,8], min_peak_amplitude=0.05, max_n_peaks=3)
    fg.fit(freqs, powers)
    return fg

def gen_sample_bw(vary, stat, i):
    """
    Generates oscillations of varying band widths based on current iteration
    [centered vary CF, vary amplitude, BW, centered stationary CF, stationary amp, BW]
    
    vary : [float, float]
    stat : [float, float]
    i : ith iteration
    
    """
    return [np.mean(vary), .5, .1*i, np.mean(stat), .5, 1]