"""Tools and utilities for generating simulations."""

import numpy as np

###################################################################################################
###################################################################################################



###################################################################################################
###################################################################################################

def average_of_sims(data):
    """ Takes a 3D array in the form of [slope][ratio method][trial] and averages [trials]
    
    -----------
    data : 3D array [slope][ratio method][trial]
    
    Output
    ------
    2D array [slope][ratio method]
       
    """

    res = []

    for i in range(len(data)):
        method = []
        for j in range(len(data[i])):
            method.append(np.mean(data[i][j]))
        res.append(method)

    return res

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
        func = gen_sample
    else:
        # [] should work instead
        func = gen_null_sample
    while(i*.25 < end_slope):

        bg = [0,i*.25]
        
        #100 trails for each treatment and control sim
        freq, power, _ = gen_group_power_spectra(100, [1,50], bg, func(), nlvs=np.random.uniform(.005,.02))
        fg = FOOOFGroup(peak_width_limits=[1,8], min_peak_amplitude=0.05, max_n_peaks=3)
        fg.fit(freq, power)
        res.append(get_group_ratios(fg,low_band_range,high_band_range))
        i+=1
    return res