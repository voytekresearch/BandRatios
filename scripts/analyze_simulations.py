""" This script calculates ratios and plots from simulated power spectral data where a parameter vary."""
import sys
sys.path.append('../bratios')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
sns.set_context('poster')

from fooof import FOOOF, FOOOFGroup

from ratios import *
from analysis import *
from settings import *

def main():

    # Load data
    cf_low = np.load("../dat/single_param_sims/cf_data_low.npy")
    cf_high = np.load("../dat/single_param_sims/cf_data_high.npy")
    pw_low = np.load("../dat/single_param_sims/pw_data_low.npy")
    pw_high = np.load("../dat/single_param_sims/pw_data_high.npy")
    bw_low = np.load("../dat/single_param_sims/bw_data_low.npy")
    bw_high = np.load("../dat/single_param_sims/bw_data_high.npy")
    f_data = np.load("../dat/single_param_sims/apc_data.npy")
    offset = np.load("../dat/single_param_sims/offset_data.npy")
    apc = np.load("../dat/single_param_sims/apc_data.npy")
    a_shift = np.load('../dat/single_param_sims/shifting_alpha.npy')
    
    # acquire dfs
    cf_low_df = prep_single_sims(cf_low, "CF")
    cf_high_df = prep_single_sims(cf_high, "CF")
    pw_low_df = prep_single_sims(pw_low, "PW")
    pw_high_df = prep_single_sims(pw_high, "PW")
    bw_low_df = prep_single_sims(bw_low, "BW")
    bw_high_df = prep_single_sims(bw_high, "BW")
    f_df = prep_single_sims(f_data, "EXP", spectral_param=0)
    offset_df = prep_single_sims(offset, "OFF", spectral_param=0)
    apc_df = prep_single_sims(apc, "EXP", spectral_param=0)
    a_shift_df = prep_single_sims(a_shift, "Alpha CF")
    
    # Plot
    plot_single_param_sims(cf_low_df, filename="cf_low")
    plot_single_param_sims(cf_high_df, filename="cf_high")
    plot_single_param_sims(pw_low_df, filename="pw_low")
    plot_single_param_sims(pw_high_df, filename="pw_high")
    plot_single_param_sims(bw_low_df, filename="bw_low")
    plot_single_param_sims(bw_high_df, filename="bw_high")
    plot_single_param_sims(apc_df, filename="apc")
    plot_single_param_sims(offset_df, filename="offset")
    plot_single_param_sims(f_df, filename="1f")
    plot_single_param_sims(a_shift_df, filename="shifting_alpha")
    
if __name__ == "__main__":
    main()
    