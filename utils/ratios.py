"""Tools and utilities for calculating oscillation band ratios."""

from functools import partial

import numpy as np

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
