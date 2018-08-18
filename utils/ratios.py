"""Tools and utilities for calculating oscillation band ratios."""

from functools import partial

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


def calc_fooof_band_ratio(fm, low_band_range, high_band_range):
    """Calculate band ratio by finding the power of high and low peak frequency from FOOOF.

    Parameters
    ----------
    fm : fooof object
        fooof'ed power spectrum
    low_band_range : list of [float, float]
        Band definition for the lower band.
    high_band_range : list of [float, float]
        Band definition for the upper band.

    Outputs
    -------
    ratio : float
        Oscillation power ratio. - low/high (?)
    """

    # Gather peak info for psd
    peaks = fm.get_all_data('peak_params')

    # Extract band specific peaks
    #  Note: outputs are 1d vector, as [CF, Amp, BW]
    low_peak = get_band_peak(peaks, low_band_range, True)
    high_peak = get_band_peak(peaks, high_band_range, True)

    ratio = low_peak[1] / high_peak[1]

    # Note: if either peak are not present in FOOOF results, then result will be nan

    return ratio

    # # adds the power ratio of each peak contained in low_band and high band respectively to a list
    # for i in range(len(treatment_peaks)):
    #     if((low_band[0] <= treatment_peaks[i][0] <=low_band[1]) and low_found == False):
    #         low_found = True
    #         #curr_id = treatment_peaks[i][3]
    #         low_power = treatment_peaks[i][1]
    #         continue

    #     elif((low_found == True) and high_band[0]<=treatment_peaks[i][0]<=high_band[1]):
    #         high_power = treatment_peaks[i][1]
    #         treatmentRatioList.append(low_power/high_power)
    #         low_found = False

    # for i in range(len(control_peaks)):
    #     if((low_band[0] <= control_peaks[i][0] <=low_band[1]) and low_found == False):
    #         low_found = True
    #         #curr_id = treatment_peaks[i][3]
    #         low_power = control_peaks[i][1]
    #         continue

    #     elif((low_found == True) and high_band[0]<=control_peaks[i][0]<=high_band[1]):
    #         high_power = control_peaks[i][1]
    #         controlRatioList.append(low_power/high_power)
    #         low_found = False

    #res = abs(np.mean(treatmentRatioList)-np.mean(controlRatioList))

    #return res

# def diff_average_power_set_band(treatment,control,low_band,high_band):
#     """Calculate band ratio by finding average power within specified bands
#     ----------
#     treatment : fooof object/ fooof.group object
#         fooof'ed power spectrum
#     control : fooof object/ fooof.group object
#         fooof'ed power spectrum
#     low_band_range : list of [float, float]
#         Band definition for the lower band.
#     high_band_range : list of [float, float]
#         Band definition for the upper band.

#     Outputs
#     -------
#     ratio : float
#         Oscillation power ratio.
#     """

#     treatment_ratio = calc_band_ratio(treatment.freqs,treatment.power_spectra,low_band,high_band)
#     control_ratio = calc_band_ratio(control.freqs, control.power_spectra,low_band,high_band)

#     res = abs(treatment_ratio-control_ratio)

#     #print("Diff ratio of average power set bands: ", res)

#     return res


#def diff_sum_div_band(treatment, control,low_band,high_band):
def calc_power_density_ratio(treatment, control, low_band, high_band):
    """Calculate band ratio by summing the power within bands, dividing each by respective bandwidths, then finding low/ high ratio

    NOTE: fix this up to do 'power density'
        - Unpack from FOOOF: inputs as freq vector & powers vector
        - Take 1 PSD
        - Make sure consistent API

    ----------
    treatment : fooof object/ fooof.group object
        fooof'ed power spectrum
    control : fooof object/ fooof.group object
        fooof'ed power spectrum
    low_band_range : list of [float, float]
        Band definition for the lower band.
    high_band_range : list of [float, float]
        Band definition for the upper band.

    Outputs
    -------
    ratio : float
        Oscillation power ratio.
    """

    # Extract frequencies within each specified band
    _, low_band_powers = trim_spectrum(treatment.freqs, treatment.power_spectra, low_band)
    _, high_band_powers = trim_spectrum(control.freqs, control.power_spectra,high_band)

    # Divides each sum of each power spectrum by bandwidth.
    #  Note: low_band[1] - low_band[0]
    low_sum = sum(low_band_powers) / len(low_band)
    high_sum = sum(high_band_powers) / len(high_band)

    # Average divided sums and find ratio
    res = np.mean(low_sum) / np.mean(high_sum)

    #print("Diff sum(power in band)/bandwidth: ",res)

    return res

#By this point fooof should have fit both treatment and control
def ratios(treatment,control,low_band=[4,8],high_band=[15,30]):
    """Runs 3 distinct ratio calculations. See 'diff_CF_Power_only' 'diff_average_power_set_band' 'diff_sum_div_band'

    Suggest:
        - Yes: on a convenience to run all ratio measures, given a PSD, and print out
        - Still split out calculation of ratios from comparison of ratios

    ----------
    treatment : fooof object/ fooof.group object
        fooof'ed power spectrum
    control : fooof object/ fooof.group object
        fooof'ed power spectrum
    low_band_range (optional): list of [float, float]
        Band definition for the lower band.
    high_band_range (optional): list of [float, float]
        Band definition for the upper band.

    Outputs
    -------
    ratio : float
        Oscillation power ratio.
    """
    res =[]
    # Execute first method:
    # difference in power of central frequency
    # of high and low frequency peak only
    res.append(diff_CF_Power_only(treatment,control,low_band,high_band))
    print("\t")

    # Execute second method:
    # difference in average power in set bands ratio
    res.append(diff_average_power_set_band(treatment,control,low_band,high_band))
    print("\t")

    # Execute third method:
    # difference in sum(powers in set band)/bandwidth ratio
    res.append(diff_sum_div_band(treatment,control,low_band,high_band))
    print("--------------------------------------------------")

    return res
