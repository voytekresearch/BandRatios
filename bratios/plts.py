"""Tools to plot band ratios"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import pandas as pd

from ratios import *
from settings import *

def plot_heatmap(param_marker, ratios, stationary='low'):
    """ Plots heatmap of ratios as two parameters are varied.
    Only pass in data generated from ../scripts/.
        
    Parameters
    ----------
    param_marker : string
        First varied parameter. Either 'apc' or 'cf'.
    ratios : list of floats
        Ratios generated from calc_interacting_param_ratios().
    stationary: string
        Either 'low' or 'high' indicating which band's parameters are being modulated.
    
    Outputs
    -------
    Displays Heatmap
    """
    
    if param_marker == 'apc':
        p1 = _get_ptable_param1_col(param_marker, stationary)
        p2 = _get_ptable_param2_col(param_marker, ratios)
        lab1 = "Aperiodic Component"
        lab2 = "Amplitude"
        title = "Amplitude and Aperiodic modulation "+ stationary+ " band"
        
    elif param_marker == 'cf':
        p1 = _get_ptable_param1_col(param_marker, stationary)
        p2 = _get_ptable_param2_col(param_marker, ratios)
        print("center freqs", len(p1))
        print("bandwidths", len(p2))
        print("ratios", len(ratios))
        lab1 = "Center frequecy"
        lab2 = "Bandwidth"
        title = "Center frequency and bandwidth modulation "+ stationary+ " band"
        
    cols = {lab1: p1, lab2: p2, "Ratio": ratios}
    df = pd.DataFrame(cols)
    pivot = df.pivot(lab1, lab2, "Ratio")
    
    ax = plt.axes()
    ax.set_title(title)
    sb.heatmap(pivot)
    
    
def plot_apc_amp_heatmap(ratios, stationary='low'):
    
    p_apcs = _get_ptable_apc_col()  
    p_amps = _get_ptable_amp_col(ratios)
    
    cols = {"Aperiodic Component": p_apcs, "Amplitude": p_amps, "Ratio": ratios}
    df = pd.DataFrame(cols)
    pivot = df.pivot("Aperiodic Component", "Amplitude", "Ratio")
    
    ax = plt.axes()
    ax.set_title(title)
    sb.heatmap(pivot)
    

def _get_ptable_param1_col(param_marker, stationary):
    """Creates a list of apc values which cycle. Used with list of amps to identify
    corresponding calculated ratio.
    
    Parameters
    ----------
    param_marker : string
        Either 'apc' or 'cf'
    stationary : string
        Only used if param_marker is 'cf'. Indicates which band to modulate over
    
    Outputs
    -------
    p_apcs : list of apc values to insert in Dataframe which correspond to specific
    ratio.
    """
    
    if param_marker == "apc":
        prange1 = APCS
        prange2 = AMPS
        
    elif param_marker == "cf":        
        if stationary == 'low':
            prange1 = CFS_LOW
        elif stationary == 'high':
            prange1 = CFS_HIGH
        
        prange2 = BWS
    
    res = []
    
    for param1 in prange1:
        for param2 in prange2:
            res.append(param1)
    return res

def _get_ptable_param2_col(param_marker, ratios):
    """creates a list of amplitude values which cycle. Used with list of amps
    to identify corresponding calculated ratio.
    
    Parameters
    ----------
    None.
    
    Outputs
    -------
    p_apcs : list of apc values to insert in Dataframe which correspond to specific
    ratio.
    """
    
    if param_marker == 'apc':
        param = AMPS
    elif param_marker == 'cf':
        param = BWS
    
    res = []
    param_modulo_val = len(param)

    for ind, val in enumerate(ratios):
        res.append(round(param[ind % param_modulo_val],1)) 
        
    return res