"""Tools and utilities for calculating oscillation band ratios."""

from functools import partial

import numpy as np

from fooof.analysis import get_band_peak_fm
from fooof.utils import trim_spectrum
from fooof.sim import gen_freqs

from settings import BANDS, FREQ_RANGE, FREQ_RES

###################################################################################################
###################################################################################################

def calc_band_ratio(freqs, psd, low_band, high_band):
    """Calculate band ratio measure between two predefined frequency ranges.

    Parameters
    ----------
    freqs : 1d array
        Frequency values.
    psd : 1d array
        Power spectrum power values.
    low_band : list of [float, float]
        Band definition for the lower band.
    high_band : list of [float, float]
        Band definition for the upper band.

    Outputs
    -------
    ratio : float
        Oscillation band ratio.
    """

    # Extract frequencies within each specified band
    _, low_band = trim_spectrum(freqs, psd, low_band)
    _, high_band = trim_spectrum(freqs, psd, high_band)

    # Calculate average power within each band, and then the ratio between them
    ratio = np.mean(low_band) / np.mean(high_band)

    return ratio


# Create a partial function definitions for proto-typical band analyses
calc_theta_beta_ratio = partial(calc_band_ratio,
    low_band=BANDS['theta'], high_band=BANDS['beta'])
calc_theta_alpha_ratio = partial(calc_band_ratio,
    low_band=BANDS['theta'], high_band=BANDS['alpha'])
calc_alpha_beta_ratio = partial(calc_band_ratio,
    low_band=BANDS['alpha'], high_band=BANDS['beta'])

# Copy over docs for partial functions
calc_theta_beta_ratio.__doc__ = calc_band_ratio.__doc__
calc_theta_alpha_ratio.__doc__ = calc_band_ratio.__doc__
calc_alpha_beta_ratio.__doc__ = calc_band_ratio.__doc__


def calc_relative_ratio(rel_pow_low_band, rel_pow_high_band):
    """Calculate ratio of relative power between two bands.

    Parameters
    ----------
    rel_pow_low_band : float
        Relative power of lower band.
    rel_pow_high_band : float
        Relative power of higher band.

    Outputs
    -------
    ratio : float
    """

    return rel_pow_low_band / rel_pow_high_band


def calc_cf_power_ratio(fm, low_band, high_band):
    """Calculate band ratio from FOOOF derived peaks.

    Parameters
    ----------
    fm : fooof object used to find ratio
    low_band : list of [float, float]
        Band definition for the lower band.
    high_band : list of [float, float]
        Band definition for the upper band.

    Outputs
    -------
    fooof_ratio : float
        Oscillation power ratio.
    """

    low_peak = get_band_peak_fm(fm, low_band)
    high_peak = get_band_peak_fm(fm, high_band)

    fooof_ratio = low_peak[1] / high_peak[1]

    return fooof_ratio


def calc_density_ratio(freqs, psd, low_band, high_band):
    """Calculate band ratio by summing the power within bands,
    dividing each by respective bandwidths, then finding low/ high ratio.

    Parameters
    ----------
    freqs : 1d array
        List of frequencies.
    psd : 1d array
        Powers values.
    low_band : list of [float, float]
        Band definition for the lower band.
    high_band : list of [float, float]
        Band definition for the upper band.

    Outputs
    -------
    ratio : float
        Oscillation power ratio.
    """

    _, low_band_powers = trim_spectrum(freqs, psd, low_band)
    _, high_band_powers = trim_spectrum(freqs, psd, high_band)

    low_density = sum(low_band_powers) / len(low_band)
    high_density = sum(high_band_powers) / len(low_band)

    return low_density / high_density


def compare_ratio(fm1, fm2, low_band, high_band, mode):
    """Finds the difference in power ratio of fm2 - fm1.

    Parameters
    ----------
    fm1, fm2 : FOOOF
        fooof objects used to find ratio
    low_band : list of [float, float]
        Band definition for the lower band.
    high_band : list of [float, float]
        Band definition for the upper band.
    mode: string
        "d" - calculate density ratio
        "cf"- calculate ratio of power from FOOOF measures
        "a" - calculate average power within 2 band

    Outputs
    -------
    float
        Difference in ratios.
    """

    if mode == "d":

        r1 = calc_density_ratio(fm1.freqs, fm1.power_spectrum, low_band, high_band)
        r2 = calc_density_ratio(fm2.freqs, fm2.power_spectrum, low_band, high_band)

        return r2-r1

    elif mode == "cf":

        r1 = calc_cf_power_ratio(fm1, low_band, high_band)
        r2 = calc_cf_power_ratio(fm2, low_band, high_band)

        return r2-r1

    elif mode == "a":

        r1 = calc_band_ratio(fm1.freqs, fm1.power_spectrum, low_band, high_band)
        r2 = calc_band_ratio(fm2.freqs, fm2.power_spectrum, low_band, high_band)

        return r2-r1

    else:
        print(compare_ratio.__doc__)


def calc_group_band_ratio(fg, low_band, high_band, func=calc_band_ratio):
    """Calculate band ratios across a group.

    Parameters
    ----------
    fg : fooof group object used to find ratio
    low_band : list of [float, float]
        Band definition for the lower band.
    high_band : list of [float, float]
        Band definition for the upper band.

    Outputs
    -------
    ratios : list of floats
        Oscillation power ratios.
    """

    res = []
    for i in range(len(fg)):
        res.append(func(fg.freqs, np.power(10, fg.power_spectra[i]),
                        low_band, high_band))

    return res


def calc_group_cf_power_ratio(fg, low_band, high_band):
    """Calculate band ratios from FOOOF across a group.

    Parameters
    ----------
    fg : fooof group object used to find ratio
    low_band : list of [float, float]
        Band definition for the lower band.
    high_band : list of [float, float]
        Band definition for the upper band.

    Outputs
    -------
    ratios : floats
        Oscillation power ratio.
    """

    res = []
    for ind in range(len(fg)):
        res.append(calc_cf_power_ratio(fg.get_fooof(ind), low_band, high_band))

    return res


def get_group_ratios(fg, low_band, high_band):
    """Calculates group band ratios canonically, fooof derived ratio, and density.

    Parameters
    ----------
    fg : fooofGroup object used to find ratios
    low_band : list of float, float
        Band definition for the lower band.
    high_band : list of float, float
        Band definition for the upper band.

    Outputs
    -------
    ratios : floats
        Oscillation power ratio.
    """

    res = []
    res.append(calc_group_band_ratio(fg, low_band, high_band))
    res.append(calc_group_cf_power_ratio(fg, low_band, high_band))
    res.append(calc_group_ratio(fg, low_band, high_band, calc_density_ratio))

    return res


def calc_relative_power(freqs, ps, freq_range):
    """Calculates relative power within a frequency band.

    Parameters
    ----------
    freqs : list of floats
        Frequency vector.
    ps : list of floats
        Powers of frequencies.
    freq_range : list of [float]
        Range to calculate relative power from.

    Outputs
    -------
    rel_power : float
        Relative power of given frequency range.
    """

    total_power = sum(ps) #This will be denominator

    # Extract frequencies within specified band
    _, band_ps = trim_spectrum(freqs, ps, freq_range)

    rel_power = np.mean(band_ps) / total_power

    return rel_power


def calc_group_relative_power(freqs, ps, freq_range):
    """Calculates relative power within a frequency band.

    Parameters
    ----------
    freqs : list of list of floats
        List of frequency vectors.
    ps : list of list of floats
        List of powers of frequencies.
    freq_range : list of float
        Range to calculate relative power from.

    Outputs
    -------
    relative power : list of float
        List of relative power of given frequency range.
    """

    res = []

    for powers in ps:
        res.append(calc_relative_power(freqs, powers, freq_range))

    return res


def calc_group_rel_ratios(rel_pow_low, rel_pow_high):
    """ Calculates relative ratio of power within two bands.

    Parameters
    ----------
    rel_pow_low : float or list of floats
        Low band power or list of low band powers
    rel_pow_high : float or list of floats
        High band power or list of high band powers

    Outputs
    -------
    res : list of float
        List of relative power ratio of given frequency range.
    """

    res = []

    if len(rel_pow_low) != len(rel_pow_high):
        raise ValueError("Size of lists do not match.")

    for low, high in zip(rel_pow_low, rel_pow_high):
        res.append(low / high)

    return res


def calc_interacting_param_ratios(data, low_band=BANDS["theta"], high_band=BANDS["beta"]):
    """Calculates matrix of absolute ratios from interacting data.

    Parameters
    ----------
    data : custom object ndarray [apc value][frequency vector][psds][syn_params]

    Outputs
    -------
    res : 2D matrix of ratios where each dimension is a varied parameter

    ------------------------
    |           |          |
    |   r_11    |  r_12    |
    |           |          |
    |-----------------------
    |           |          |
    |   r_21    |  r_22    |
    |           |          |
    ------------------------
    """

    fs = gen_freqs(FREQ_RANGE, FREQ_RES)
    ratios = np.zeros(shape=(len(data), len(data[0])))

    for rot_ind, rot_val in enumerate(data):

        for del_ind, del_val in enumerate(data[0]):
            psd = data[rot_ind, del_ind, :]
            ratios[rot_ind, del_ind] = calc_band_ratio(fs, psd, low_band, high_band)

    return ratios
