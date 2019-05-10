"""Tools to analyze band ratio data"""
import numpy as np
from numpy.linalg import LinAlgError
import pandas as pd
from scipy.stats import pearsonr, spearmanr

from fooof import FOOOF, FOOOFGroup
from fooof.analysis import get_band_peak_fm
from fooof.funcs import average_fg


from settings import *
from ratios import *



def nan_corr_pearson(vec1, vec2):
    """Correlation of two vectors with NaN values.
    Note: assumes the vectors have NaN in the same indices.
    """
    vec1 = np.asarray(vec1)
    vec2 = np.asarray(vec2)
    nan_inds = np.isnan(vec1)

    return pearsonr(vec1[~nan_inds], vec2[~nan_inds])

def nan_corr_spearman(vec1, vec2):
    """Correlation of two vectors with NaN values.
    Note: assumes the vectors have NaN in the same indices.
    """
    
    vec1 = np.asarray(vec1)
    vec2 = np.asarray(vec2)

    nan_inds = np.isnan(vec1)

    return spearmanr(vec1[~nan_inds], vec2[~nan_inds])

def _get_age_range(df, age=[0,100]):
    age_range = df[(df['Age'] >= age[0]) & (df['Age'] <= age[1])]
    return age_range.ID.values


def get_data_matrix():
    pass


def add_params(curr_row, theta_params, beta_params, alpha_params,ap):
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

def get_all_data(df, chs, age=[0,100],block=0):
    """This function will return the fooof parameters for each channel and 
       theircorresponding tb ratio.

    Parameters
    ----------


    Outputs
    -------
    
    """
    
    res = pd.DataFrame()
    age_range_ids = _get_age_range(df, age)
    row_ind = 0
    for filename in age_range_ids:
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
                
                fm = FOOOF(verbose=False)      
                fm.add_data(freqs, ps)
                fm.fit() 
                
                theta_params = get_band_peak_fm(fm, BANDS['theta'])
                beta_params = get_band_peak_fm(fm, BANDS['beta'])
                alpha_params = get_band_peak_fm(fm, BANDS['alpha'])
                ap = fm.aperiodic_params_
                                                
                curr_row = add_params(curr_row, theta_params, beta_params, alpha_params, ap)


                tbr = calc_band_ratio(freqs, ps, BANDS['theta'], BANDS['beta'])
                tar = calc_band_ratio(freqs, ps, BANDS['theta'], BANDS['alpha'])
                abr = calc_band_ratio(freqs, ps, BANDS['alpha'], BANDS['beta'])
                ages = df[df['ID'] == filename].Age.values[0]
                
                curr_row["TBR"] = tbr
                curr_row["TAR"] = tar
                curr_row["ABR"] = tbr
                curr_row["Age"] = ages
                
                curr_row = pd.Series(curr_row)
               
                res = res.append(curr_row,ignore_index=True)
                
                row_ind+=1
            
        except FileNotFoundError or ValueError: 
            continue
        except LinAlgError:
            continue
        except IndexError:
            print("problem with index: ",filename)

    return res