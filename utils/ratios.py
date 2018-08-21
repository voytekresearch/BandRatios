"""Tools and utilities for calculating oscillation band ratios."""

from functools import partial
from fooof.analysis import get_band_peak
import numpy as np

from fooof.utils import trim_spectrum

###################################################################################################
###################################################################################################

# Define canonical bands
THETA_BAND = [4, 8]
ALPHA_BAND = [8, 12]
BETA_BAND = [15, 30]

###################################################################################################
###################################################################################################

def calc_band_ratio(freqs, psd, low_band_range, high_band_range):
    """Calculate band ratio measure between two predefined band ranges from a power spectrum.

    Parameters
    ----------
    freqs : 1d array
        Frequency values.
    psd : 1d array
        Power spectrum power values.
    low_band_range : list of [float, float]
        Band definition for the lower band.
    high_band_range : list of [float, float]
        Band definition for the upper band.

    Outputs
    -------
    ratio : float
        Oscillation band ratio.
    """

    # Extract frequencies within each specified band
    _, low_band = trim_spectrum(freqs, psd, low_band_range)
    _, high_band = trim_spectrum(freqs, psd, high_band_range)

    # Calculate average power within each band, and then the ratio between them
    ratio = np.mean(low_band) / np.mean(high_band)

    return ratio

# Create a partial function definitions for proto-typical band analyses
calc_theta_beta_ratio = partial(calc_band_ratio, low_band_range=THETA_BAND, high_band_range=BETA_BAND)
calc_theta_alpha_ratio = partial(calc_band_ratio, low_band_range=THETA_BAND, high_band_range=ALPHA_BAND)
calc_alpha_beta_ratio = partial(calc_band_ratio, low_band_range=ALPHA_BAND, high_band_range=BETA_BAND)

# Copy over docs for partial functions
calc_theta_beta_ratio.__doc__ = calc_band_ratio.__doc__
calc_theta_alpha_ratio.__doc__ = calc_band_ratio.__doc__
calc_alpha_beta_ratio.__doc__ = calc_band_ratio.__doc__


def calc_cf_power_ratio(fm, low_band_range, high_band_range):
    """Calculate band ratio by finding the power of high and low central frequency

    Parameters
    ----------
    fm : fooof object used to find ratio
    low_band_range : list of [float, float]
        Band definition for the lower band.
    high_band_range : list of [float, float]
        Band definition for the upper band.

    Outputs
    -------
    ratio : float
        Oscillation power ratio. - low/high (?)
    """

    peaks = fm.get_results()

    low_peak = get_band_peak(peaks[1], low_band_range, ret_one=True)
    high_peak = get_band_peak(peaks[1], high_band_range, ret_one=True)

    return low_peak[1]/high_peak[1]


def calc_density_ratio(freqs, psd, low_band_range,high_band_range):
    """Calculate band ratio by summing the power within bands, dividing each by respective bandwidths, then finding low/ high ratio
    ----------
    freqs : [n floats]
        list of frequencies.
    psd : [n floats]
        associated powers to frequencies.
    low_band_range : list of [float, float]
        Band definition for the lower band.
    high_band_range : list of [float, float]
        Band definition for the upper band.

    Outputs
    -------
    ratio : float
        Oscillation power ratio.
    """
    _, low_band_powers = trim_spectrum(freqs, psd, low_band_range)
    _, high_band_powers = trim_spectrum(freqs, psd, high_band_range)

    low_density = sum(low_band_powers) / len(low_band_range)
    high_density = sum(high_band_powers) / len(low_band_range)

    return low_density/high_density


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


def calc_group_band_ratio(fg,low_band_range, high_band_range):
    """Calculate average power in band ratio

    ----------
    fg : fooof group object used to find ratio
    low_band_range : list of [float, float]
        Band definition for the lower band.
    high_band_range : list of [float, float]
        Band definition for the upper band.

    Outputs
    -------
    ratios : list of floats
        Oscillation power ratios.
    """

    size = len(fg.get_results())
    res = []
    for i in range(size):
        res.append(calc_band_ratio(fg.freqs,fg.power_spectra[i], low_band_range, high_band_range))

    return res


def calc_group_cf_power_ratio(fg, low_band_range, high_band_range):
    """Calculate band ratio by finding the power of high and low central frequency

    Parameters
    ----------
    fg : fooof group object used to find ratio
    low_band_range : list of [float, float]
        Band definition for the lower band.
    high_band_range : list of [float, float]
        Band definition for the upper band.

    Outputs
    -------
    ratios : floats
        Oscillation power ratio.
    """

    size = len(fg.get_results())
    res = []
    for i in range(size):
        res.append(calc_cf_power_ratio(fg.get_fooof(i), low_band_range, high_band_range))

    return res


def calc_group_density_ratio(fg, low_band_range, high_band_range):
    """Calculate band ratio by summing power power in bands and dividing by bandwidth

    ----------
    fg : fooofGroup object used to find ratio
    low_band_range : list of [float, float]
        Band definition for the lower band.
    high_band_range : list of [float, float]
        Band definition for the upper band.

    Outputs
    -------
    ratios : floats
        Oscillation power ratio.
    """

    size = len(fg.get_results())
    res = []
    for i in range(size):
        res.append(calc_density_ratio(fg.freqs,fg.power_spectra[i], low_band_range, high_band_range))

    return res


def get_group_ratios(fg, low_band_range, high_band_range):
<<<<<<< HEAD
    """ Calculates group band ratios cannonically, central frequency ratio, and density 
    
     ----------
    fg : fooofGroup object used to find ratios
    low_band_range : list of [float, float]
        Band definition for the lower band.
    high_band_range : list of [float, float]
        Band definition for the upper band.

    Outputs
    -------
    ratios : floats
        Oscillation power ratio.
    
    """
=======
    """   """

>>>>>>> a9a3b8e91f0b2704a59c5b55f449e20a89cb91a5
    res = []
    res.append( calc_group_band_ratio(fg, low_band_range, high_band_range))
    res.append( calc_group_cf_power_ratio(fg, low_band_range, high_band_range))
    res.append( calc_group_density_ratio(fg, low_band_range, high_band_range))

    return res


def average_of_sims(data):
    """   """

    res = []

    for i in range(len(data)):
        method = []
        for j in range(len(data[i])):
            method.append(np.mean(data[i][j]))
        res.append(method)

    return res
<<<<<<< HEAD
    
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

def gen_null_sample():
    """
    generates a sample for generating a fooof PSD with no oscillations
    
    Output
    ------
    sample : array
            [.0000001,.0000001,.0000001]
    """
    
    return [.0000001,.0000001,.0000001]

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
=======
>>>>>>> a9a3b8e91f0b2704a59c5b55f449e20a89cb91a5
