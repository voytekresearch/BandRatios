""" This script calculates ratios and plots from simulated power spectral data where two parameters vary."""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

from fooof import FOOOF, FOOOFGroup

from ratios import *
from settings import *

def main():

###################### APERIODIC COMPONENT & AMPLITUDE ######################

    # load data
    apc_amp_low = np.load("../dat/interacting_param_sims/apc_amp_data_low.npy")
    apc_amp_high = np.load("../dat/interacting_param_sims/apc_amp_data_high.npy")

    # calculate ratios
    apc_amp_low_ratios = calc_interacting_param_ratios(apc_amp_low)
    apc_amp_high_ratios = calc_interacting_param_ratios(apc_amp_high)
    
    # Low band amp apc modulation
    fig, ax = plt.subplots()
    ax = sns.heatmap(apc_amp_low_ratios, xticklabels=AMPS, yticklabels=APCS)
    ax.invert_yaxis()
    plt.xlabel("Amplitude")
    plt.ylabel("Exponent")
    plt.title("Low band amplitude and exponent modulation")
    plt.savefig("../figures/InteractingSims/low_apc_amp.png",dpi=500)
    
    plt.cla()
    
    fig, ax = plt.subplots()
    # Low band amp apc modulation with logged ratios
    ax = sns.heatmap(np.log10(apc_amp_low_ratios), xticklabels=AMPS, yticklabels=APCS)
    ax.invert_yaxis()
    plt.xlabel("PW", {"fontsize": 18})
    plt.ylabel("EXP", {"fontsize": 18})
    plt.title("Low band PW and EXP",{"fontsize": 18})
    plt.savefig("../figures/InteractingSims/low_apc_amp_log.png", dpi=500)
    
    plt.cla()
    
    #######
    ## High band amp apc modulation
    ######
    
    fig, ax = plt.subplots()
    ax = sns.heatmap(apc_amp_high_ratios, xticklabels=AMPS, yticklabels=APCS)
    ax.invert_yaxis()
    plt.xlabel("Amplitude")
    plt.ylabel("Exponent")
    plt.title("High band amplitude and exponent modulation")
    plt.savefig("../figures/InteractingSims/high_apc_amp.png", dpi=500)
    
    plt.cla()
    
    fig, ax = plt.subplots()
    ax = sns.heatmap(np.log10(apc_amp_high_ratios), xticklabels=AMPS, yticklabels=APCS)
    ax.invert_yaxis()
    plt.xlabel("PW", {"fontsize": 18})
    plt.ylabel("EXP", {"fontsize": 18})
    plt.title("High band PW vs EXP", {"fontsize": 18})
    plt.tight_layout()
    plt.savefig("../figures/InteractingSims/high_apc_amp_log.png", dpi=500)
    
    plt.cla()
    
###################### CENTER FREQUENCY & BANDWIDTH ######################    
    
    # Load data
    cf_bw_low = np.load("../dat/interacting_param_sims/cf_bw_data_low.npy")
    cf_bw_high = np.load("../dat/interacting_param_sims/cf_bw_data_high.npy")
    
    # calculate ratios
    cf_bw_low_ratios = calc_interacting_param_ratios(cf_bw_low)
    cf_bw_high_ratios = calc_interacting_param_ratios(cf_bw_high)
    
    # Low band
    fig, ax = plt.subplots()
    ax = sns.heatmap(cf_bw_low_ratios, xticklabels=BWS, yticklabels=CFS_LOW)
    ax.invert_yaxis()
    plt.xlabel("Bandwidth", {"fontsize": 18})
    plt.ylabel("Low band center frequencies", {"fontsize": 18})
    plt.title("Low band bandwidth vs center frequency", {"fontsize": 18})
    plt.tight_layout()
    plt.savefig("../figures/InteractingSims/low_bw_cf.png", dpi=500)
    
    plt.cla()
    
    # Low band logged
    fig, ax = plt.subplots()
    ax = sns.heatmap(np.log10(cf_bw_low_ratios), xticklabels=BWS, yticklabels=CFS_LOW)
    ax.invert_yaxis()
    plt.xlabel("BW",{"fontsize": 18})
    plt.ylabel("CF",{"fontsize": 18})
    plt.title("Low band BW vs Low band CF",{"fontsize": 18})
    plt.tight_layout()
    plt.savefig("../figures/InteractingSims/low_bw_cf_log.png", dpi=500)
    
    plt.cla()
    
    # High band
    fig, ax = plt.subplots()
    ax = sns.heatmap(cf_bw_high_ratios, xticklabels=BWS, yticklabels=CFS_HIGH)
    ax.invert_yaxis()
    plt.xlabel("Bandwidth",{"fontsize": 18})
    plt.ylabel("Center Frequencies",{"fontsize": 18})
    #plt.title("High band bandwidth and center frequency modulation")
    plt.tight_layout()
    plt.savefig("../figures/InteractingSims/high_bw_cf.png", dpi=500)
    
    plt.cla()
    
    # High band logged
    fig, ax = plt.subplots()
    ax = sns.heatmap(np.log10(cf_bw_high_ratios), xticklabels=BWS, yticklabels=CFS_HIGH)
    ax.invert_yaxis()
    plt.xlabel("BW",{"fontsize": 18})
    plt.ylabel("CF", {"fontsize": 18})
    plt.title("High band BW vs CF", {"fontsize": 18})
    plt.tight_layout()
    plt.savefig("../figures/InteractingSims/high_bw_cf_log.png", dpi=500)
    
    plt.cla()  
    
###################### ROTATIONAL FREQUENCY & ROTATIONAL DELTA ######################

    #Load data
    rot_data = np.load("../dat/interacting_param_sims/rot_del.npy")
                       
    # calculate ratios
    rot_ratios = calc_interacting_param_ratios(rot_data)
                       
    # plot
    fig, ax = plt.subplots()
    ax = sns.heatmap(rot_ratios, xticklabels=DELS, yticklabels=ROTS)
    ax.invert_yaxis()
    plt.xlabel("Delta power law exponent")
    plt.ylabel("Rotational frequency")
    plt.title("Rotation frequency and rotation amount")
    plt.savefig("../figures/InteractingSims/rotation_delta.png", dpi=500)
    
    plt.cla()  
    
    fig, ax = plt.subplots()
    ax = sns.heatmap(np.log10(rot_ratios), xticklabels=DELS, yticklabels=ROTS)
    ax.invert_yaxis()
    plt.xlabel("Delta power law exponent")
    plt.ylabel("Rotational frequency")
    plt.title("Rotation frequency and rotation amount")
    plt.savefig("../figures/InteractingSims/rotation_delta_log.png", dpi=500)

if __name__ == "__main__":
    main()
    