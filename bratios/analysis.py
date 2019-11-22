"""Tools to analyze band ratio data"""

import numpy as np
from numpy.linalg import LinAlgError
import pandas as pd
from scipy.stats import pearsonr, spearmanr
import matplotlib.pyplot as plt
import seaborn as sns

from fooof import FOOOF, FOOOFGroup
from fooof.analysis import get_band_peak_fm
from fooof.funcs import average_fg

from settings import *
from ratios import *


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
    """Obtain labels of slow and fast wave spectral parameters
    
    Parameters
    ----------
    band_label: character
        Character corrsponding to frequency band.
    
    Return
    ------
    list of strings containing spectral labels.
        ex) [Theta_CF, Theta_PW, Theta_BW]
    
    """
    curr_band = BAND_LABELS[band_label]
    
    return [curr_band+"_" + feat for feat in FEATURE_LABELS]


def print_aperiodic_correlation(ratio_type, corr):
    """Prints out the correlation between ratio and aperiodic parameters
    
    Parameters
    ----------
    ratio_type : String
        Which specific ratio measure to use.
            ex) TBR
    corr : list of floats
        Correlation r-values for aperiodic params.
        
    Outputs
    -------
    Prints formatted sentences of correlations between ratio and aperiodic parameters.
    """
    
    for ind, param in enumerate(["Exp","Off","Age"]):
        print("The corr of {} to {} is {:1.2f}".format(ratio_type, param,  corr[ind]))


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
    return [nrb+"_" + feat for feat in FEATURE_LABELS]

        
def param_ratio_corr(df, ratio_type, ch_inds, func=nan_corr_pearson):
    """Finds correlation between spectral params & ratios.

    Parameters
    ----------
    df : 2D DataFrame
        Container which holds ratio, channels, and peak values.
    ratio_type : string 
        Ratio measure to run correlations across.
        ex) "TBR"
    ch_inds : list of ints
        Channels to run correlations over.
    func : Correlation function
        
        
    Return
    ------
    2x3 ndarray of periodic param correlations
    2x1 ndarray of aperiodic param correltations
    """
    
    # Select relevant rows from df
    rel_df = df.loc[df['Chan_ID'].isin(ch_inds)]
    
    # Get columns to correlate with
    theta = get_wave_params("T")
    alpha = get_wave_params("A")
    beta = get_wave_params("B")
    
    theta_corrs = np.zeros(3)
    alpha_corrs = np.zeros(3)
    beta_corrs = np.zeros(3)
    ap_corrs = np.zeros(3)
    
    # Ratio vs spectral params correlation
    for ind in range(3):
        theta_corrs[ind] = func(rel_df[theta[ind]],rel_df[ratio_type])[0]
        alpha_corrs[ind] = func(rel_df[alpha[ind]],rel_df[ratio_type])[0]
        beta_corrs[ind] = func(rel_df[beta[ind]],rel_df[ratio_type])[0]
        
    # Ratio vs aperiodic params correlation
    ap_corrs[0] = func(rel_df["Exp"], rel_df[ratio_type])[0]
    ap_corrs[1] = func(rel_df["Off"], rel_df[ratio_type])[0]
    ap_corrs[2] = func(rel_df["Age"], rel_df[ratio_type])[0]

    return np.stack((theta_corrs, alpha_corrs,beta_corrs)), ap_corrs
        
        
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

def get_all_data(df, chs ,block=0):
    """This function will return a DataFrame populated with all subjects, channels,
    spectral parameters, band ratios, and age - all from the ChildMind dataset.

    Parameters
    ----------
    df : Dataframe
        Container holding subjects' psds.
    chs : list of ints
        Channels corresponding to each psd.
    block : int
        Which block to populate data for.

    Outputs
    -------
    DataFrame
    """
    
    res = pd.DataFrame()

    for filename in df.ID.values:
        try:
            
            curr_data = np.load('../dat/psds/'+ filename + '_ec_psds.npz')
            freqs = curr_data['arr_0']
            for ch in chs:
                curr_row = dict()
                curr_row["Subj_ID"] = filename
                curr_row["Chan_ID"] = ch
                ps = curr_data['arr_1'][block][ch]
                if isinstance(ps, float):

                    continue
                
                fm = FOOOF(verbose=False, peak_width_limits=(1,8))      
                fm.add_data(freqs, ps)
                fm.fit() 
                
                theta_params = get_band_peak_fm(fm, BANDS['theta'])
                beta_params = get_band_peak_fm(fm, BANDS['beta'])
                alpha_params = get_band_peak_fm(fm, BANDS['alpha'])
                ap = fm.aperiodic_params_
                                                
                curr_row = _add_params(curr_row, theta_params, beta_params, alpha_params, ap)


                tbr = calc_band_ratio(freqs, ps, BANDS['theta'], BANDS['beta'])
                tar = calc_band_ratio(freqs, ps, BANDS['theta'], BANDS['alpha'])
                abr = calc_band_ratio(freqs, ps, BANDS['alpha'], BANDS['beta'])
                ages = df[df['ID'] == filename].Age.values[0]
                
                curr_row["TBR"] = tbr
                curr_row["TAR"] = tar
                curr_row["ABR"] = abr
                curr_row["Age"] = ages
                
                curr_row = pd.Series(curr_row)
               
                res = res.append(curr_row,ignore_index=True)
            
        except FileNotFoundError or ValueError: 
            print("FileNotFound or ValueError: ",filename)
        except LinAlgError:
            print("LinAlgError: ",filename)
        except IndexError:
            print("IndexError: ",filename)

    return res


def get_len_ratio_subjects():
    """Calculates number of subjects for tbr, tar, and abr measures.
    
    Returns
    -------
    tuple : length of tbr, tar, abr
    
    """
    df_tbr = df[np.isnan(df.Theta_CF)==False]
    df_tbr = df_tbr[np.isnan(df_tbr.Beta_CF)==False]

    df_tar = df[np.isnan(df.Theta_CF)==False]
    df_tar = df_tar[np.isnan(df_tar.Alpha_CF)==False]

    df_abr = df[np.isnan(df.Alpha_CF)==False]
    df_abr = df_abr[np.isnan(df_abr.Beta_CF)==False]

    print("len_tbr:", len(df_tbr),"len_tar",len(df_tar), len("abr"),len(abr) )
    return len(df_tbr), len(df_tar), len(abr)


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
    
    if varied_param=="PW":
        print(tar)
    # Make DataFrame of Center Frequencies and coresponding ratio values
    cols = np.array([tbr, tar, abr,param_values]).T.tolist()
    
    df = pd.DataFrame(cols, columns=["TBR","TAR","ABR", varied_param])
    
    return df