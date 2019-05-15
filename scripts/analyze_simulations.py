""" This script calculates ratios and plots from simulated power spectral data where a parameter vary."""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
sns.set_context('poster')

from fooof import FOOOF, FOOOFGroup

from ratios import *
from settings import *

def main():

    ###################### CENTER FREQUENCY ######################
    # Load data
    cf_low = np.load("../dat/cf_data_low.npy")
    cf_high = np.load("../dat/cf_data_high.npy")

    # Gather center frequency values iterated across for both low and high band
    cf_low_syns = []
    cf_high_syns = []

    for val in cf_low[2]:
        cf_low_syns.append(val.gaussian_params[0][0])
    for val in cf_high[2]:
        cf_high_syns.append(val.gaussian_params[0][0])

    # Calculate ratios
    cf_low_tbr = []
    cf_low_tar = []
    cf_low_abr = []
    cf_high_tbr = []
    cf_high_tar = []
    cf_high_abr = []

    for cf in cf_low[1]:
        cf_low_tbr.append(calc_theta_beta_ratio(cf_low[0], cf))
        cf_low_tar.append(calc_theta_alpha_ratio(cf_low[0], cf))
        cf_low_abr.append(calc_alpha_beta_ratio(cf_low[0], cf))

    for cf in cf_high[1]:
        cf_high_tbr.append(calc_theta_beta_ratio(cf_high[0], cf))
        cf_high_tar.append(calc_theta_alpha_ratio(cf_high[0], cf))
        cf_high_abr.append(calc_alpha_beta_ratio(cf_high[0], cf))

    # Make DataFrame of Center Frequencies and coresponding ratio values
    df_cf_low_cols = np.array([cf_low_tbr, cf_low_tar, cf_low_abr, cf_low_syns]).T.tolist()
    df_cf_high_cols = np.array([cf_high_tbr, cf_high_tar, cf_high_abr, cf_high_syns]).T.tolist()

    df_cf_low = pd.DataFrame(df_cf_low_cols, columns=["TBR","TAR","ABR", "CF"])
    df_cf_high = pd.DataFrame(df_cf_high_cols, columns=["TBR","TAR","ABR", "CF"])

    # Subplots - define the figure
    fig = plt.figure(figsize=[8, 4])
    
    #TBR by PW
    ax1= fig.add_subplot(121)
    ax1.set_xlabel("CF_low",{"fontsize": 18})
    ax1.set_ylabel("TBR",{"fontsize": 18})
    ax1.plot(df_cf_low.CF, df_cf_low.TBR, color='r')
    
    ax11= fig.add_subplot(122)
    ax11.set_xlabel("CF_low",{"fontsize": 18})
    ax11.set_ylabel("TBR",{"fontsize": 18})
    ax11.set_yscale('log')
    ax11.plot(df_cf_low.CF, df_cf_low.TBR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/cf_low_vs_TBR.png", dpi=700)
    plt.clf() 
    
    #TAR by PW
    ax2= fig.add_subplot(121)
    ax2.set_xlabel("CF_low",{"fontsize": 18})
    ax2.set_ylabel("TAR",{"fontsize": 18})
    ax2.plot(df_cf_low.CF, df_cf_low.TAR, color='r')
    
    ax21= fig.add_subplot(122)
    ax21.set_xlabel("CF_low",{"fontsize": 18})
    ax21.set_ylabel("TAR",{"fontsize": 18})
    ax21.set_yscale('log')
    ax21.plot(df_cf_low.CF, df_cf_low.TAR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/cf_low_vs_TAR.png", dpi=700)
    plt.clf() 
    
    #ABR by BW
    ax3= fig.add_subplot(121)
    ax3.set_xlabel("CF_low",{"fontsize": 18})
    ax3.set_ylabel("ABR",{"fontsize": 18})
    ax3.plot(df_cf_low.CF, df_cf_low.ABR, color='r')
    
    ax31= fig.add_subplot(122)
    ax31.set_xlabel("CF_low",{"fontsize": 18})
    ax31.set_ylabel("ABR",{"fontsize": 18})
    ax31.set_yscale('log')
    ax31.plot(df_cf_low.CF, df_cf_low.ABR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/cf_low_vs_ABR.png", dpi=700)
    plt.clf() 

    #TBR by BW
    ax1= fig.add_subplot(121)
    ax1.set_xlabel("CF_high",{"fontsize": 18})
    ax1.set_ylabel("TBR",{"fontsize": 18})
    ax1.plot(df_cf_high.CF, df_cf_high.TBR, color='r')
    
    ax11= fig.add_subplot(122)
    ax11.set_xlabel("CF_high",{"fontsize": 18})
    ax11.set_ylabel("TBR",{"fontsize": 18})
    ax11.set_yscale('log')
    ax11.plot(df_cf_high.CF, df_cf_high.TBR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/cf_high_vs_TBR.png", dpi=700)
    plt.clf() 
    
    #TAR by BW
    ax2= fig.add_subplot(121)
    ax2.set_xlabel("BW_high",{"fontsize": 18})
    ax2.set_ylabel("TAR",{"fontsize": 18})
    ax2.plot(df_cf_high.CF, df_cf_high.TAR, color='r')
    
    ax21= fig.add_subplot(122)
    ax21.set_xlabel("CF_high",{"fontsize": 18})
    ax21.set_ylabel("TAR",{"fontsize": 18})
    ax21.set_yscale('log')
    ax21.plot(df_cf_high.CF, df_cf_high.TAR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/cf_high_vs_TAR.png", dpi=700)
    plt.clf() 
    
    #ABR by BW
    ax3= fig.add_subplot(121)
    ax3.set_xlabel("CF_high",{"fontsize": 18})
    ax3.set_ylabel("ABR",{"fontsize": 18})
    ax3.plot(df_cf_high.CF, df_cf_high.ABR, color='r')
    
    ax31= fig.add_subplot(122)
    ax31.set_xlabel("CF_high",{"fontsize": 18})
    ax31.set_ylabel("ABR",{"fontsize": 18})
    ax31.set_yscale('log')
    ax31.plot(df_cf_high.CF, df_cf_high.ABR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/cf_high_vs_ABR.png", dpi=700)
    plt.clf() 


    ###################### Amplitude ######################

    # Load data
    amp_low = np.load("../dat/amp_data_low.npy")
    amp_high = np.load("../dat/amp_data_high.npy")

    # Gather Amplitude vales
    amp_low_syns = []
    amp_high_syns = []

    for val in amp_low[2]:
        amp_low_syns.append(val.gaussian_params[0][1])
    for val in amp_high[2]:
        amp_high_syns.append(val.gaussian_params[0][1])

    # Calculate band ratios
    amp_low_tbr = []
    amp_low_tar = []
    amp_low_abr = []
    amp_high_tbr = []
    amp_high_tar = []
    amp_high_abr = []

    for amp in amp_low[1]:
        amp_low_tbr.append(calc_theta_beta_ratio(amp_low[0], amp))
        amp_low_tar.append(calc_theta_alpha_ratio(amp_low[0], amp))
        amp_low_abr.append(calc_alpha_beta_ratio(amp_low[0], amp))

    for amp in amp_high[1]:
        amp_high_tbr.append(calc_theta_beta_ratio(amp_high[0], amp))
        amp_high_tar.append(calc_theta_alpha_ratio(amp_high[0], amp))
        amp_high_abr.append(calc_alpha_beta_ratio(amp_high[0], amp))

    # Create DataFrame
    df_amp_low_cols = np.array([amp_low_tbr, amp_low_tar, amp_low_abr, amp_low_syns]).T.tolist()
    df_amp_high_cols = np.array([amp_high_tbr, amp_high_tar, amp_high_abr, amp_high_syns]).T.tolist()

    df_amp_low = pd.DataFrame(df_amp_low_cols, columns=["TBR","TAR","ABR", "Power"])
    df_amp_high = pd.DataFrame(df_amp_high_cols, columns=["TBR","TAR", "ABR", "Power"])

    # Subplots - define the figure
    fig = plt.figure(figsize=[8, 4])
    
    #TBR by PW
    ax1= fig.add_subplot(121)
    ax1.set_xlabel("PW_low",{"fontsize": 18})
    ax1.set_ylabel("TBR",{"fontsize": 18})
    ax1.plot(df_amp_low.Power, df_amp_low.TBR, color='r')
    
    ax11= fig.add_subplot(122)
    ax11.set_xlabel("PW_low",{"fontsize": 18})
    ax11.set_ylabel("TBR",{"fontsize": 18})
    ax11.set_yscale('log')
    ax11.plot(df_amp_low.Power, df_amp_low.TBR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/pw_low_vs_TBR.png", dpi=700)
    plt.clf() 
    
    #TAR by PW
    ax2= fig.add_subplot(121)
    ax2.set_xlabel("PW_low",{"fontsize": 18})
    ax2.set_ylabel("TAR",{"fontsize": 18})
    ax2.plot(df_amp_low.Power, df_amp_low.TAR, color='r')
    
    ax21= fig.add_subplot(122)
    ax21.set_xlabel("PW_low",{"fontsize": 18})
    ax21.set_ylabel("TAR",{"fontsize": 18})
    ax21.set_yscale('log')
    ax21.plot(df_amp_low.Power, df_amp_low.TAR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/pw_low_vs_TAR.png", dpi=700)
    plt.clf() 
    
    #ABR by BW
    ax3= fig.add_subplot(121)
    ax3.set_xlabel("PW_low",{"fontsize": 18})
    ax3.set_ylabel("ABR",{"fontsize": 18})
    ax3.plot(df_amp_low.Power, df_amp_low.ABR, color='r')
    
    ax31= fig.add_subplot(122)
    ax31.set_xlabel("PW_low",{"fontsize": 18})
    ax31.set_ylabel("ABR",{"fontsize": 18})
    ax31.set_yscale('log')
    ax31.plot(df_amp_low.Power, df_amp_low.ABR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/pw_low_vs_ABR.png", dpi=700)
    plt.clf() 

    #TBR by BW
    ax1= fig.add_subplot(121)
    ax1.set_xlabel("PW_high",{"fontsize": 18})
    ax1.set_ylabel("TBR",{"fontsize": 18})
    ax1.plot(df_amp_high.Power, df_amp_high.TBR, color='r')
    
    ax11= fig.add_subplot(122)
    ax11.set_xlabel("PW_high",{"fontsize": 18})
    ax11.set_ylabel("TBR",{"fontsize": 18})
    ax11.set_yscale('log')
    ax11.plot(df_amp_high.Power, df_amp_high.TBR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/pw_high_vs_TBR.png", dpi=700)
    plt.clf() 
    
    #TAR by BW
    ax2= fig.add_subplot(121)
    ax2.set_xlabel("PW_high",{"fontsize": 18})
    ax2.set_ylabel("TAR",{"fontsize": 18})
    ax2.plot(df_amp_high.Power, df_amp_high.TAR, color='r')
    
    ax21= fig.add_subplot(122)
    ax21.set_xlabel("PW_high",{"fontsize": 18})
    ax21.set_ylabel("TAR",{"fontsize": 18})
    ax21.set_yscale('log')
    ax21.plot(df_amp_high.Power, df_amp_high.TAR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/pw_high_vs_TAR.png", dpi=700)
    plt.clf() 
    
    #ABR by BW
    ax3= fig.add_subplot(121)
    ax3.set_xlabel("PW_high",{"fontsize": 18})
    ax3.set_ylabel("ABR",{"fontsize": 18})
    ax3.plot(df_amp_high.Power, df_amp_high.ABR, color='r')
    
    ax31= fig.add_subplot(122)
    ax31.set_xlabel("PW_high",{"fontsize": 18})
    ax31.set_ylabel("ABR",{"fontsize": 18})
    ax31.set_yscale('log')
    ax31.plot(df_amp_high.Power, df_amp_high.ABR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/pw_high_vs_ABR.png", dpi=700)
    plt.clf() 
    

    ###################### BAND WIDTH ######################

    bw_low = np.load("../dat/bw_data_low.npy")
    bw_high = np.load("../dat/bw_data_high.npy")

    bw_low_syns = []
    bw_high_syns = []

    for val in bw_low[2]:
        bw_low_syns.append(val.gaussian_params[0][2])
    for val in bw_high[2]:
        bw_high_syns.append(val.gaussian_params[0][2])

    bw_low_tbr = []
    bw_low_tar = []
    bw_low_abr = []
    
    bw_high_tbr = []
    bw_high_tar = []
    bw_high_abr = []

    for bw in bw_low[1]:
        bw_low_tbr.append(calc_theta_beta_ratio(bw_low[0], bw))
        bw_low_tar.append(calc_theta_alpha_ratio(bw_low[0], bw))
        bw_low_abr.append(calc_alpha_beta_ratio(bw_low[0], bw))

    for bw in bw_high[1]:
        bw_high_tbr.append(calc_theta_beta_ratio(bw_high[0], bw))
        bw_high_tar.append(calc_theta_alpha_ratio(bw_high[0], bw))
        bw_high_abr.append(calc_alpha_beta_ratio(bw_high[0], bw))

    df_bw_low_cols = np.array([bw_low_tbr, bw_low_tar, bw_low_abr, bw_low_syns]).T.tolist()
    df_bw_high_cols = np.array([bw_high_tbr, bw_high_tar, bw_high_abr, bw_high_syns]).T.tolist()

    df_bw_low = pd.DataFrame(df_bw_low_cols, columns=["TBR","TAR", "ABR", "BandWidth"])
    df_bw_high = pd.DataFrame(df_bw_high_cols, columns=["TBR","TAR", "ABR","BandWidth"])

    # Subplots - define the figure
    fig = plt.figure(figsize=[8, 4])
    
    #TBR by BW
    ax1= fig.add_subplot(121)
    ax1.set_xlabel("BW_low",{"fontsize": 18})
    ax1.set_ylabel("TBR",{"fontsize": 18})
    ax1.plot(df_bw_low.BandWidth, df_bw_low.TBR, color='r')
    
    ax11= fig.add_subplot(122)
    ax11.set_xlabel("BW_low",{"fontsize": 18})
    ax11.set_ylabel("TBR",{"fontsize": 18})
    ax11.set_yscale('log')
    ax11.plot(df_bw_low.BandWidth, df_bw_low.TBR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/bw_low_vs_TBR.png", dpi=700)
    plt.clf() 
    
    #TAR by BW
    ax2= fig.add_subplot(121)
    ax2.set_xlabel("BW_low",{"fontsize": 18})
    ax2.set_ylabel("TAR",{"fontsize": 18})
    ax2.plot(df_bw_low.BandWidth, df_bw_low.TAR, color='r')
    
    ax21= fig.add_subplot(122)
    ax21.set_xlabel("BW_low",{"fontsize": 18})
    ax21.set_ylabel("TAR",{"fontsize": 18})
    ax21.set_yscale('log')
    ax21.plot(df_bw_low.BandWidth, df_bw_low.TAR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/bw_low_vs_TAR.png", dpi=700)
    plt.clf() 
    
    #ABR by BW
    ax3= fig.add_subplot(121)
    ax3.set_xlabel("BW_low",{"fontsize": 18})
    ax3.set_ylabel("ABR",{"fontsize": 18})
    ax3.plot(df_bw_low.BandWidth, df_bw_low.ABR, color='r')
    
    ax31= fig.add_subplot(122)
    ax31.set_xlabel("BW_low",{"fontsize": 18})
    ax31.set_ylabel("ABR",{"fontsize": 18})
    ax31.set_yscale('log')
    ax31.plot(df_bw_low.BandWidth, df_bw_low.ABR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/bw_low_vs_ABR.png", dpi=700)
    plt.clf() 
 



    #TBR by BW
    ax1= fig.add_subplot(121)
    ax1.set_xlabel("BW_high",{"fontsize": 18})
    ax1.set_ylabel("TBR",{"fontsize": 18})
    ax1.plot(df_bw_high.BandWidth, df_bw_high.TBR, color='r')
    
    ax11= fig.add_subplot(122)
    ax11.set_xlabel("BW_low",{"fontsize": 18})
    ax11.set_ylabel("TBR",{"fontsize": 18})
    ax11.set_yscale('log')
    ax11.plot(df_bw_high.BandWidth, df_bw_high.TBR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/bw_high_vs_TBR.png", dpi=700)
    plt.clf() 
    
    #TAR by BW
    ax2= fig.add_subplot(121)
    ax2.set_xlabel("BW_high",{"fontsize": 18})
    ax2.set_ylabel("TAR",{"fontsize": 18})
    ax2.plot(df_bw_high.BandWidth, df_bw_high.TAR, color='r')
    
    ax21= fig.add_subplot(122)
    ax21.set_xlabel("BW_high",{"fontsize": 18})
    ax21.set_ylabel("TAR",{"fontsize": 18})
    ax21.set_yscale('log')
    ax21.plot(df_bw_high.BandWidth, df_bw_high.TAR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/bw_high_vs_TAR.png", dpi=700)
    plt.clf() 
    
    #ABR by BW
    ax3= fig.add_subplot(121)
    ax3.set_xlabel("BW_high",{"fontsize": 18})
    ax3.set_ylabel("ABR",{"fontsize": 18})
    ax3.plot(df_bw_high.BandWidth, df_bw_high.ABR, color='r')
    
    ax31= fig.add_subplot(122)
    ax31.set_xlabel("BW_high",{"fontsize": 18})
    ax31.set_ylabel("ABR",{"fontsize": 18})
    ax31.set_yscale('log')
    ax31.plot(df_bw_high.BandWidth, df_bw_high.ABR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/bw_high_vs_ABR.png", dpi=700)
    plt.clf() 
    
    

    ###################### Aperiodic Component ######################

    apc = np.load("../dat/apc_data.npy")

    apc_syns = []

    for val in apc[2]:
        apc_syns.append(val.aperiodic_params[1])

    apc_tbr = []
    apc_tar = []
    apc_abr = []

    for ap in apc[1]:
        apc_tbr.append(calc_theta_beta_ratio(apc[0], ap))
        apc_tar.append(calc_theta_alpha_ratio(apc[0], ap))
        apc_abr.append(calc_alpha_beta_ratio(apc[0], ap))

    apc_cols = np.array([apc_tbr, apc_tar, apc_abr, apc_syns]).T.tolist()

    df_apc = pd.DataFrame(apc_cols, columns=["TBR", "TAR", "ABR", "APC"])

    fig = plt.figure(figsize=[8, 4])
    
    #TBR by APC
    ax1= fig.add_subplot(121)
    ax1.set_xlabel("Exponent",{"fontsize": 18})
    ax1.set_ylabel("TBR",{"fontsize": 18})
    ax1.plot(df_apc.APC, df_apc.TBR, color='r')
    
    ax11= fig.add_subplot(122)
    ax11.set_xlabel("Exponent",{"fontsize": 18})
    ax11.set_ylabel("TBR",{"fontsize": 18})
    ax11.set_yscale('log')
    ax11.plot(df_apc.APC, df_apc.TBR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/APC_vs_TBR.png", dpi=700)
    plt.clf() 
    
    #TAR by APC
    ax2= fig.add_subplot(121)
    ax2.set_xlabel("Exponent",{"fontsize": 18})
    ax2.set_ylabel("TAR",{"fontsize": 18})
    ax2.plot(df_apc.APC, df_apc.TAR, color='r')
    
    ax21= fig.add_subplot(122)
    ax21.set_xlabel("Exponent",{"fontsize": 18})
    ax21.set_ylabel("TAR",{"fontsize": 18})
    ax21.set_yscale('log')
    ax21.plot(df_apc.APC, df_apc.TAR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/APC_vs_TAR.png", dpi=700)
    plt.clf() 
    
    #ABR by APC
    ax3= fig.add_subplot(121)
    ax3.set_xlabel("Exponent",{"fontsize": 18})
    ax3.set_ylabel("ABR",{"fontsize": 18})
    ax3.plot(df_apc.APC, df_apc.ABR, color='r')
    
    ax31= fig.add_subplot(122)
    ax31.set_xlabel("Exponent",{"fontsize": 18})
    ax31.set_ylabel("ABR",{"fontsize": 18})
    ax31.set_yscale('log')
    ax31.plot(df_apc.APC, df_apc.ABR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/APC_vs_ABR.png", dpi=700)
    plt.clf() 
    
    
    
    ###################### OFFSET ######################
    
    offset = np.load("../dat/offset_data.npy")

    offset_syns = []

    for val in offset[2]:
        offset_syns.append(val.aperiodic_params[0])

    off_tbr = []
    off_tar = []
    off_abr = []

    for os in offset[1]:
        off_tbr.append(calc_theta_beta_ratio(offset[0], os))
        off_tar.append(calc_theta_alpha_ratio(offset[0], os))
        off_abr.append(calc_alpha_beta_ratio(offset[0], os))


    offset_cols = np.array([off_tbr, off_tar, off_abr, offset_syns]).T.tolist()

    df_off = pd.DataFrame(offset_cols, columns=["TBR","TAR", "ABR", "Offset"])

    fig = plt.figure(figsize=[8, 4])
    
    
    #TBR by offset
    ax1= fig.add_subplot(121)
    ax1.set_xlabel("Offset",{"fontsize": 18})
    ax1.set_ylabel("TBR",{"fontsize": 18})
    ax1.plot(df_off.Offset, df_off.TBR, color='r')
    
    ax11= fig.add_subplot(122)
    ax11.set_xlabel("Offset",{"fontsize": 18})
    ax11.set_ylabel("TBR",{"fontsize": 18})
    ax11.set_yscale('log')
    ax11.plot(df_off.Offset, df_off.TBR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/offset_vs_TBR.png", dpi=700)
    plt.clf() 
    
    #TAR by offset
    ax2= fig.add_subplot(121)
    ax2.set_xlabel("Offset",{"fontsize": 18})
    ax2.set_ylabel("TAR",{"fontsize": 18})
    ax2.plot(df_off.Offset, df_off.TAR, color='r')
    
    ax21= fig.add_subplot(122)
    ax21.set_xlabel("Offset",{"fontsize": 18})
    ax21.set_ylabel("TAR",{"fontsize": 18})
    ax21.set_yscale('log')
    ax21.plot(df_off.Offset, df_off.TAR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/offset_vs_TAR.png", dpi=700)
    plt.clf() 
    
    #ABR by offset
    ax3= fig.add_subplot(121)
    ax3.set_xlabel("Offset",{"fontsize": 18})
    ax3.set_ylabel("ABR",{"fontsize": 18})
    ax3.plot(df_off.Offset, df_off.ABR, color='r')
    
    ax31= fig.add_subplot(122)
    ax31.set_xlabel("Offset",{"fontsize": 18})
    ax31.set_ylabel("ABR",{"fontsize": 18})
    ax31.set_yscale('log')
    ax31.plot(df_off.Offset, df_off.ABR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/offset_vs_ABR.png", dpi=700)
    plt.clf() 


    ###################### No Oscillation - 1/f ######################
    
    f_data = np.load("../dat/apc_data.npy")

    f_syns = []

    for val in f_data[2]:
        f_syns.append(val.aperiodic_params[1])

    f_tbr = []
    f_tar = []
    f_abr = []

    for f in f_data[1]:
        f_tbr.append(calc_theta_beta_ratio(f_data[0], f))
        f_tar.append(calc_theta_alpha_ratio(f_data[0], f))
        f_abr.append(calc_alpha_beta_ratio(f_data[0], f))
        

    f_cols = np.array([f_tbr, f_tar, f_abr, f_syns]).T.tolist()

    df_f = pd.DataFrame(f_cols, columns=["TBR","TAR", "ABR", "Slope"])

    fig = plt.figure(figsize=[8, 4])
    
    
    #TBR by 1/f
    ax1= fig.add_subplot(121)
    ax1.set_xlabel("Exponent",{"fontsize": 18})
    ax1.set_ylabel("TBR",{"fontsize": 18})
    ax1.plot(df_f.Slope, df_f.TBR, color='r')
    
    ax11= fig.add_subplot(122)
    ax11.set_xlabel("Exponent",{"fontsize": 18})
    ax11.set_ylabel("TBR",{"fontsize": 18})
    ax11.set_yscale('log')
    ax11.plot(df_f.Slope, df_f.TBR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/1f_vs_TBR(no_osc).png", dpi=700)
    plt.clf() 
    
    #TAR by 1/f
    ax2= fig.add_subplot(121)
    ax2.set_xlabel("Exponent",{"fontsize": 18})
    ax2.set_ylabel("TAR",{"fontsize": 18})
    ax2.plot(df_f.Slope, df_f.TAR, color='r')
    
    ax21= fig.add_subplot(122)
    ax21.set_xlabel("Exponent",{"fontsize": 18})
    ax21.set_ylabel("TAR",{"fontsize": 18})
    ax21.set_yscale('log')
    ax21.plot(df_f.Slope, df_f.TAR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/1f_vs_TAR(no_osc).png", dpi=700)
    plt.clf() 
    
    #ABR by 1/f
    ax3= fig.add_subplot(121)
    ax3.set_xlabel("Exponent",{"fontsize": 18})
    ax3.set_ylabel("TAR",{"fontsize": 18})
    ax3.plot(df_f.Slope, df_f.ABR, color='r')
    
    ax31= fig.add_subplot(122)
    ax31.set_xlabel("Exponent",{"fontsize": 18})
    ax31.set_ylabel("ABR",{"fontsize": 18})
    ax31.set_yscale('log')
    ax31.plot(df_f.Slope, df_f.ABR, color='r')
    
    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/1f_vs_ABR(no_osc).png", dpi=700)
    plt.clf() 
    
    

    ######################################################
    ################### Relative Power ###################
    ######################################################


    ###################### RELATIVE CENTER FREQUENCY ######################

    rel_t_ps_cf_low = calc_group_relative_power(cf_low[0], cf_low[1], THETA_BAND)
    rel_b_ps_cf_low = calc_group_relative_power(cf_low[0], cf_low[1], BETA_BAND)

    rel_t_ps_cf_high = calc_group_relative_power(cf_high[0], cf_high[1], THETA_BAND)
    rel_b_ps_cf_high = calc_group_relative_power(cf_high[0], cf_high[1], BETA_BAND)

    cf_r_ratios_low = calc_group_rel_ratios(rel_t_ps_cf_low, rel_b_ps_cf_low)
    cf_r_ratios_high = calc_group_rel_ratios(rel_t_ps_cf_high, rel_b_ps_cf_high)

    # Make DataFrame of Center Frequencies and coresponding ratio values
    df_cf_low_cols = np.array([cf_r_ratios_low, cf_low_syns]).T.tolist()
    df_cf_high_cols = np.array([cf_r_ratios_high, cf_high_syns]).T.tolist()

    df_cf_low = pd.DataFrame(df_cf_low_cols, columns=["Relative_Ratio", "Low_Center_Frequency"])
    df_cf_high = pd.DataFrame(df_cf_high_cols, columns=["Relative_Ratio", "High_Center_Frequency"])

    # Subplots - define the figure
    fig, ax = plt.subplots(2, 1, figsize=[6, 7])

    ax[0].set_xlabel("Low_Center_Freq")
    ax[1].set_xlabel("High_Center_Freq")
    ax[0].set_ylabel("Band_Ratio")
    ax[1].set_ylabel("Band_Ratio")

    # Fill in axes
    ax[0].plot(df_cf_low.Low_Center_Frequency, df_cf_low.Relative_Ratio, color='r')
    ax[1].plot(df_cf_high.High_Center_Frequency, df_cf_high.Relative_Ratio, color='r')

    plt.savefig("../figures/SingleParamSims/rel_cf_vs_bandratio.png", dpi=700)
    ###################### RELATIVE AMPLITUDE ######################

    rel_t_ps_amp_low = calc_group_relative_power(amp_low[0], amp_low[1], THETA_BAND)
    rel_b_ps_amp_low = calc_group_relative_power(amp_low[0], amp_low[1], BETA_BAND)

    rel_t_ps_amp_high = calc_group_relative_power(amp_high[0], amp_high[1], THETA_BAND)
    rel_b_ps_amp_high = calc_group_relative_power(amp_high[0], amp_high[1], BETA_BAND)

    amp_r_ratios_low = calc_group_rel_ratios(rel_t_ps_amp_low, rel_b_ps_amp_low)
    amp_r_ratios_high = calc_group_rel_ratios(rel_t_ps_amp_high, rel_b_ps_amp_high)

    # Create DataFrame
    df_amp_low_cols = np.array([amp_r_ratios_low, amp_low_syns]).T.tolist()
    df_amp_high_cols = np.array([amp_r_ratios_high, amp_high_syns]).T.tolist()

    df_amp_low = pd.DataFrame(df_amp_low_cols, columns=["Relative_Ratio", "Low_Amplitude"])
    df_amp_high = pd.DataFrame(df_amp_high_cols, columns=["Relative_Ratio", "High_Amplitude"])

    # Subplots - define the figure
    fig, ax = plt.subplots(2, 1, figsize=[6, 7])

    ax[0].set_xlabel("Low_Amplitude")
    ax[1].set_xlabel("High_Amplitude")
    ax[0].set_ylabel("Band_Ratio")
    ax[1].set_ylabel("Band_Ratio")

    # Fill in axes
    ax[0].plot(df_amp_low.Low_Amplitude, df_amp_low.Relative_Ratio, color='r')
    ax[1].plot(df_amp_high.High_Amplitude, df_amp_high.Relative_Ratio, color='r')

    plt.savefig("../figures/SingleParamSims/rel_amp_vs_bandratio.png", dpi=700)

    ###################### RELATIVE BAND WIDTH ######################

    bw_low = np.load("../dat/bw_data_low.npy")
    bw_high = np.load("../dat/bw_data_high.npy")

    rel_t_ps_bw_low = calc_group_relative_power(bw_low[0], bw_low[1], THETA_BAND)
    rel_b_ps_bw_low = calc_group_relative_power(bw_low[0], bw_low[1], BETA_BAND)

    rel_t_ps_bw_high = calc_group_relative_power(bw_high[0], bw_high[1], THETA_BAND)
    rel_b_ps_bw_high = calc_group_relative_power(bw_high[0], bw_high[1], BETA_BAND)

    bw_r_ratios_low = calc_group_rel_ratios(rel_t_ps_bw_low, rel_b_ps_bw_low)
    bw_r_ratios_high = calc_group_rel_ratios(rel_t_ps_bw_high, rel_b_ps_bw_high)

    df_bw_low_cols = np.array([bw_r_ratios_low, bw_low_syns]).T.tolist()
    df_bw_high_cols = np.array([bw_r_ratios_high, bw_high_syns]).T.tolist()

    df_bw_low = pd.DataFrame(df_bw_low_cols, columns=["Relative_Ratio", "Low_BandWidth"])
    df_bw_high = pd.DataFrame(df_bw_high_cols, columns=["Relative_Ratio", "High_BandWidth"])

    # Subplots - define the figure
    fig, ax = plt.subplots(2, 1, figsize=[6, 7])

    ax[0].set_xlabel("Low_Band_Width")
    ax[1].set_xlabel("High_Band_Width")
    ax[0].set_ylabel("Relative_Ratio")
    ax[1].set_ylabel("Relative_Ratio")

    ax[0].plot(df_bw_low.Low_BandWidth, df_bw_low.Relative_Ratio, color='r')
    ax[1].plot(df_bw_high.High_BandWidth, df_bw_high.Relative_Ratio, color='r')

    plt.savefig("../figures/SingleParamSims/rel_bw_vs_bandratio.png", dpi=700)

    ###################### RELATIVE APERIODIC COMPONENT ######################

    slope = np.load("../dat/apc_data.npy")

    rel_t_ps_sl = calc_group_relative_power(slope[0], slope[1], THETA_BAND)
    rel_b_ps_sl = calc_group_relative_power(slope[0], slope[1], BETA_BAND)

    slope_r_ratios_low = calc_group_rel_ratios(rel_t_ps_sl, rel_b_ps_sl)

    slope_cols = np.array([slope_r_ratios_low, apc_syns]).T.tolist()

    df_slope = pd.DataFrame(slope_cols, columns=["Relative_Ratio", "Slope"])

    fig, ax = plt.subplots(2, 1, figsize=[6, 7])

    ax[0].set_xlabel("Slope_Value")
    ax[1].set_xlabel("Slope_Value")
    ax[0].set_ylabel("Relative_Ratio_Log")
    ax[1].set_ylabel("Relative_Ratio")

    # LOG SCALING
    ax[0].set_yscale('log')
    #ax[0].set_xscale('log')

    ax[0].plot(df_slope.Slope, df_slope.Relative_Ratio, color='r')
    ax[1].plot(df_slope.Slope, df_slope.Relative_Ratio, color='r')

    plt.savefig("../figures/SingleParamSims/rel_apc_vs_bandratio.png", dpi=700)

if __name__ == "__main__":
    main()
    