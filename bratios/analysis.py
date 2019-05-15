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
    """
    vec1 = np.asarray(vec1)
    vec2 = np.asarray(vec2)
    
    nan_mask_1 = np.isnan(vec1)
    nan_mask_2 = np.isnan(vec2)
    
    mask = np.logical_and(~nan_mask_1, ~nan_mask_2)

    return pearsonr(vec1[mask], vec2[mask])

def nan_corr_spearman(vec1, vec2):
    """Correlation of two vectors with NaN values.
    Note: assumes the vectors have NaN in the same indices.
    """
    
    vec1 = np.asarray(vec1)
    vec2 = np.asarray(vec2)
    
    nan_mask_1 = np.isnan(vec1)
    nan_mask_2 = np.isnan(vec2)
    
    mask = np.logical_and(~nan_mask_1, ~nan_mask_2)
    return spearmanr(vec1[mask], vec2[mask])


def get_wave_params(ratio_type):
    
    #Deduce bands
    sw = ""
    fw = ""
    if ratio_type[0] == "T":
        sw = "Theta"
    elif ratio_type[0] == "A":
        sw = "Alpha"
    else:
        #TODO input error
        pass
        
    # find Fast Wave
    if ratio_type[1] == "A":
        fw = "Alpha"
    elif ratio_type[1] == "B":
        fw = "Beta"
    else:
        #TODO input error
        pass
    # Build column strings
    sw_params = [sw+"_CF", sw+"_PW", sw+"_BW"]
    fw_params = [fw+"_CF", fw+"_PW", fw+"_BW"]
    
    return sw_params, fw_params


def peak_param_ratio_corr(df, ratio_type, ch_inds, func=nan_corr_pearson):
    """Finds correlation between peak params & ratios.

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
    2x3 ndarray or correlations
    """
    
    # Select relevant rows from df
    rel_df = df.loc[df['Chan_ID'].isin(ch_inds)]
    
    # Get columns to correlate with
    sw, fw = get_wave_params(ratio_type)
    
    sw_corrs = np.zeros(3)
    fw_corrs = np.zeros(3)
    
    for ind in range(3):
        sw_corrs[ind] = func(df[sw[ind]],df[ratio_type])[0]
        fw_corrs[ind] = func(df[fw[ind]],df[ratio_type])[0]
        
    
    return np.stack((sw_corrs, fw_corrs))
                           
                       
def get_data_matrix():
    pass


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
                
                fm = FOOOF(verbose=False)      
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
                curr_row["ABR"] = tbr
                curr_row["Age"] = ages
                
                curr_row = pd.Series(curr_row)
               
                res = res.append(curr_row,ignore_index=True)
            
        except FileNotFoundError or ValueError: 
            continue
        except LinAlgError:
            continue
        except IndexError:
            print("problem with index: ",filename)

    return res