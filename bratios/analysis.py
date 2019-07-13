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
    for ind, param in enumerate(["Exp","Off","Age"]):
        print("The corr of {} to {} is {:1.2f}".format(ratio_type, param,  corr[ind]))

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
    sw = get_wave_params(ratio_type[0])
    fw = get_wave_params(ratio_type[1])
    
    sw_corrs = np.zeros(3)
    fw_corrs = np.zeros(3)
    ap_corrs = np.zeros(3)
    
    # Ratio vs spectral params correlation
    for ind in range(3):
        sw_corrs[ind] = func(rel_df[sw[ind]],rel_df[ratio_type])[0]
        fw_corrs[ind] = func(rel_df[fw[ind]],rel_df[ratio_type])[0]
        print(func(rel_df[sw[ind]],rel_df[ratio_type]))
        print(func(rel_df[fw[ind]],rel_df[ratio_type]))
        
    # Ratio vs aperiodic params correlation
    ap_corrs[0] = func(rel_df["Exp"], rel_df[ratio_type])[0]
    ap_corrs[1] = func(rel_df["Off"], rel_df[ratio_type])[0]
    ap_corrs[2] = func(rel_df["Age"], rel_df[ratio_type])[0]
    print(func(rel_df["Exp"], rel_df[ratio_type]))
    print(func(rel_df["Off"], rel_df[ratio_type]))
    print(func(rel_df["Age"], rel_df[ratio_type]))
    return np.stack((sw_corrs, fw_corrs)), ap_corrs
                           
                       
def plot_param_ratio_corr(data, title="Ratio vs. Spectral Features",y_labels=["SW","FW"], save_fig=False, file_path= HEATS_PATH, file_name="Spectral_Features_Ratio_corr"):
    """Plot correlations between BandRatio measures and spectral features.
    
    Parameters
    ----------
    data: 2x3 ndarray
        Correlations of BandRatios to Spectral Features.
    title: string
        Title of plot.
    y_labels: list of strings.
        Lables of slow and fast wave to use on y-axis.
    save_fig: boolean
        If True - save plot
        
    """
    
    if not np.all(data):
        raise RuntimeError("No data - cannot proceed.")
        
    ax = plt.axes()
    sns.heatmap(data,cmap="bone", yticklabels=y_labels, xticklabels=FEATURE_LABELS,annot=True, ax=ax)
    ax.set_title(title)
    plt.show()
    
    if save_fig:
        plt.savefig(file_path+file_name+".png")
        
        
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
            print("FileNotFound or ValueError: ",filename)
        except LinAlgError:
            print("LinAlgError: ",filename)
        except IndexError:
            print("IndexError: ",filename)

    return res