"""Tools to run analysis on BandRatios"""

import numpy as np

from ratios import *

##########################################

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

def compare_ratio(fm1, fm2, low_band_range, high_band_range, mode):
    """Finds the difference in power ratio of fm2 - fm1

    Parameters
    ----------
    fm1 : fooof object used to find ratio
    fm2 : fooof object used to find ratio
    low_band_range : list of [float, float]
        Band definition for the lower band.
    high_band_range : list of [float, float]
        Band definition for the upper band.
    mode: string
        "d" - calculate density ratio
        "cf"- calculate ratio of power from high and low central frequency
        "a" - calculate average power within 2 band

    Outputs
    -------
    difference in ratio : float
        Oscillation power ratio.
    """

    if(mode == "d"):
        r1 = calc_density_ratio(fm1.freqs, fm1.power_spectrum, low_band_range, high_band_range)
        r2 = calc_density_ratio(fm2.freqs, fm2.power_spectrum, low_band_range, high_band_range)
        return r2-r1
    elif(mode=="cf"):
        r1 = calc_cf_power_ratio(fm1, low_band_range, high_band_range)
        r2 = calc_cf_power_ratio(fm2, low_band_range, high_band_range)
        return r2-r1
    elif(mode == "a"):
        r1 = calc_band_ratio(fm1.freqs, fm1.power_spectrum, low_band_range, high_band_range)
        r2 = calc_band_ratio(fm2.freqs, fm2.power_spectrum, low_band_range, high_band_range)
        return r2-r1

    else:
        print(compare_ratio.__doc__)