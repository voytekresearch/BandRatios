"""Tools to analyze band ratio data."""

import numpy as np
from numpy.linalg import LinAlgError
import pandas as pd
from scipy.stats import pearsonr, spearmanr

from fooof import FOOOF
from fooof.analysis import get_band_peak_fm

from settings import *
from ratios import *
from paths import DATA_PATHS as dp

###################################################################################################
###################################################################################################

def nan_corr_pearson(vec1, vec2):
    """Pearson correlation of two vectors with NaN values.

    Parameters
    ----------
    vec1 : 1d array floats
        List of numbers to correlate with vec2.
    vec2 : 1d array floats
        List of numbers to correlate with vec1.

    Outputs
    -------
    Correlation : float
        r-value correlation.
    """

    vec1 = np.asarray(vec1)
    vec2 = np.asarray(vec2)

    nan_mask_1 = np.isnan(vec1)
    nan_mask_2 = np.isnan(vec2)

    mask = np.logical_and(~nan_mask_1, ~nan_mask_2)

    return pearsonr(vec1[mask], vec2[mask])

def nan_corr_spearman(vec1, vec2):
    """Spearman correlation of two vectors with NaN values.

    Parameters
    ----------
    vec1 : 1d array floats
        List of numbers to correlate with vec2
    vec2 : 1d array floats
        List of numbers to correlate with vec1

    Outputs
    -------
    Correlation : float
        r-value correlation.
    """

    vec1 = np.asarray(vec1)
    vec2 = np.asarray(vec2)

    nan_mask_1 = np.isnan(vec1)
    nan_mask_2 = np.isnan(vec2)

    mask = np.logical_and(~nan_mask_1, ~nan_mask_2)
    return spearmanr(vec1[mask], vec2[mask])


def get_wave_params(band_label):
    """Obtain labels of slow and fast wave spectral parameters.

    Parameters
    ----------
    band_label: character
        Character corresponding to frequency band.

    Return
    ------
    list of strings containing spectral labels.
        ex) [Theta_CF, Theta_PW, Theta_BW]
    """

    curr_band = BAND_LABELS[band_label]

    return [curr_band + "_" + feat for feat in FEATURE_LABELS]


def print_aperiodic_correlation(ratio_type, corr, ps=None, show=True):
    """Prints out the correlation between ratio and aperiodic parameters.

    Parameters
    ----------
    ratio_type : string
        Which specific ratio measure to report (ex. "TBR").
    corr : list of float
        Correlation r-values for aperiodic params.
    ps : list of float
        P-values for the correlations.
    show : boolean
        Whether to display the print out.

    Outputs
    -------
    Prints formatted sentences of correlations between ratio and aperiodic parameters.
    """

    if show:
        for ind, param in enumerate(["Exp", "Off", "Age"]):
            p_txt = "\t with a p-value of {:1.4f}".format(ps[ind]) if isinstance(ps, np.ndarray) else ""
            print(("The corr of {} to {} is {:1.2f}" + p_txt).format(ratio_type, param, corr[ind]))


def get_non_ratio_band(ratio_type):
    """Returns non-ratio band spectral features.

    Parameters
    ----------
    ratio_type : String
        name of ratio. {"TBR", "TAR", "ABR"}

    Return
    ------
    list of non ratio band spectral features.
    """

    if ratio_type == "TBR":
        nrb = "Alpha"
    elif ratio_type == "ABR":
        nrb = "Theta"
    elif ratio_type == "TAR":
        nrb = "Beta"

    return [nrb + "_" + feat for feat in FEATURE_LABELS]


def param_ratio_corr(df, ratio_type, ch_inds, func=nan_corr_pearson):
    """Finds correlation between spectral params & ratios.

    Parameters
    ----------
    df : 2D DataFrame
        Container which holds ratio, channels, and peak values.
    ratio_type : string
        Ratio measure to run correlations across. ex: "TBR".
    ch_inds : list of ints
        Channels to run correlations over.
    func : callable
        Correlation function to use.

    Return
    ------
    2x3 ndarray of periodic param correlations
    2x1 ndarray of aperiodic param correlations
    """

    # Select relevant rows from df
    rel_df = df.loc[df['Chan_ID'].isin(ch_inds)]

    # Average across selected channels per subject
    rel_df = rel_df.groupby("Subj_ID").mean()

    # Get columns to correlate with
    theta = get_wave_params("T")
    alpha = get_wave_params("A")
    beta = get_wave_params("B")

    # Initialize variables to store periodic & aperiodic correlation results
    per_corrs = np.zeros([3, 3])
    per_ps = np.zeros([3, 3])
    ap_corrs = np.zeros(3)
    ap_ps = np.zeros(3)

    # Ratio vs spectral params correlation
    for ind in range(3):
        per_corrs[0, ind], per_ps[0, ind] = \
            func(rel_df[theta[ind]], rel_df[ratio_type])
        per_corrs[1, ind], per_ps[1, ind] = \
            func(rel_df[alpha[ind]], rel_df[ratio_type])
        per_corrs[2, ind], per_ps[2, ind] = \
            func(rel_df[beta[ind]], rel_df[ratio_type])

    # Ratio vs aperiodic params correlation
    ap_corrs[0], ap_ps[0] = func(rel_df["Exp"], rel_df[ratio_type])
    ap_corrs[1], ap_ps[1] = func(rel_df["Off"], rel_df[ratio_type])
    ap_corrs[2], ap_ps[2] = func(rel_df["Age"], rel_df[ratio_type])

    return per_corrs, ap_corrs, per_ps, ap_ps


def _add_params(curr_row, theta_params, beta_params, alpha_params, ap):
    """Adds fooof-obtained parameters to current row which will be added to DataFrame.

    Parameters
    ----------
    curr_row : dict
        Container to hold params and to be added to DataFrame.
    theta_params : list
        Peak params in theta range [CF, PW, Bw].
    beta_params : list
        Peak params in beta range [CF, PW, Bw].
    alpha_params : list
        Peak params in alpha range [CF, PW, Bw].
    ap : list
        Aperiodic params

    Returns
    -------
    dict populated with fooof params.
    """

    curr_row["Theta_CF"] = theta_params[0]
    curr_row["Theta_PW"] = theta_params[1]
    curr_row["Theta_BW"] = theta_params[2]

    curr_row["Beta_CF"] = beta_params[0]
    curr_row["Beta_PW"] = beta_params[1]
    curr_row["Beta_BW"] = beta_params[2]

    curr_row["Alpha_CF"] = alpha_params[0]
    curr_row["Alpha_PW"] = alpha_params[1]
    curr_row["Alpha_BW"] = alpha_params[2]

    curr_row["Off"] = ap[0]
    curr_row["Exp"] = ap[1]

    return curr_row


def get_all_data(df, chs, block=0, state='ec', verbose=False):
    """This function will return a DataFrame populated with all subjects, channels,
    spectral parameters, band ratios, and age - all from the ChildMind dataset.

    Parameters
    ----------
    df : Dataframe
        Container holding subjects' psds.
    chs : list of int
        Channels corresponding to each psd.
    block : int
        Which block to populate data for.
    state : {'ec', 'eo'}
        Whether to run for eyes closed or eyes open data.
    verbose : bool
        Whether to print out updates.

    Outputs
    -------
    DataFrame
    """

    res = pd.DataFrame()

    for filename in df.ID.values:
        try:

            # Load current subjects data
            curr_data = np.load(dp.make_file_path(dp.eeg_psds, filename + '_' + state + '_psds', 'npz'))
            freqs = curr_data['arr_0']

            for ch in chs:

                # Initialize collection of subject info
                curr_row = dict()
                curr_row["Subj_ID"] = filename
                curr_row["Chan_ID"] = ch

                ps = curr_data['arr_1'][block][ch]

                # Initialize and fit FOOOF model
                fm = FOOOF(*FOOOF_SETTINGS, verbose=False)
                fm.fit(freqs, ps)

                # Extract and add periodic and aperiodic metrics from FOOOF
                theta_params = get_band_peak_fm(fm, BANDS['theta'])
                beta_params = get_band_peak_fm(fm, BANDS['beta'])
                alpha_params = get_band_peak_fm(fm, BANDS['alpha'])
                ap = fm.aperiodic_params_

                curr_row = _add_params(curr_row, theta_params, beta_params, alpha_params, ap)

                # Extract and add FOOOF model fit metrics
                curr_row["fit_error"] = fm.error_
                curr_row["fit_r2"] = fm.r_squared_
                curr_row["fit_n_peaks"] = fm.peak_params_.shape[0]

                # Calculate and add band ratio measures
                tbr = calc_band_ratio(freqs, ps, BANDS['theta'], BANDS['beta'])
                tar = calc_band_ratio(freqs, ps, BANDS['theta'], BANDS['alpha'])
                abr = calc_band_ratio(freqs, ps, BANDS['alpha'], BANDS['beta'])

                curr_row["TBR"] = tbr
                curr_row["TAR"] = tar
                curr_row["ABR"] = abr

                # Extract and add age of the subject
                ages = df[df['ID'] == filename].Age.values[0]
                curr_row["Age"] = ages

                # Collect subject data into group dataframe
                curr_row = pd.Series(curr_row)
                res = res.append(curr_row, ignore_index=True)

        except FileNotFoundError:
            if verbose:
                print("FileNotFound: ", filename)

    return res


def prep_single_sims(data, varied_param, periodic_param=1):
    """Creates dataframe containing all ratio types.

    Parameters
    ----------
    data : array
        Array of PSDs and varied_param values.
    varied_param : String
        Parameter which is varied.
    periodic_param : int
        1 if varied_param is periodic, 0 else.

    Returns
    -------
    dataframe containing ratio measures and each value of varied_param.
    """

    tbr = []
    tar = []
    abr = []

    freqs = gen_freqs(FREQ_RANGE, FREQ_RES)
    param_values = []
    param_array = np.asarray(data[1])

    for val in param_array:
        param_values.append(np.array(val[periodic_param])[SINGLE_SIM_PARAM_IND[varied_param]])

    for param in data[0]:
        tbr.append(calc_theta_beta_ratio(freqs, param))
        tar.append(calc_theta_alpha_ratio(freqs, param))
        abr.append(calc_alpha_beta_ratio(freqs, param))

    # Make DataFrame of Center Frequencies and coresponding ratio values
    cols = np.array([tbr, tar, abr, param_values]).T.tolist()

    df = pd.DataFrame(cols, columns=["TBR", "TAR", "ABR", varied_param])

    return df


def param_corr(df, corr_label_1, corr_label_2, chan_inds, func):
    """Calculates correlation between two entries in dataframe.

    Parameters
    ----------
    df : DataFrame
        Pandas DataFrame from get_all_data().
    corr_label_1 : String
        Label from dataframe to correlate.
    corr_label_2 : String
        Label from dataframe to correlate.
    chan_inds : list of ints
        Channels to correlate features from.
    func : function
        Correlation function.

    Returns
    -------
    R-value and p-value from the correlation function.
    """

    # Select relevant rows from df
    rel_df = df.loc[df['Chan_ID'].isin(chan_inds)]

    # Average across selected channels per subject
    rel_df = rel_df.groupby("Subj_ID").mean()

    return func(rel_df[corr_label_1], rel_df[corr_label_2])
