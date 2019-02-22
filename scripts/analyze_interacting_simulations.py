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
    apc_amp_low = np.load("../dat/apc_amp_data_low.npy")
    apc_amp_high = np.load("../dat/apc_amp_data_high.npy")

    # calculate ratios
    apc_amp_low_ratios = calc_interacting_param_ratios(apc_amp_low)
    apc_amp_high_ratios = calc_interacting_param_ratios(apc_amp_high)
    
    # Low band amp apc modulation
    fig, ax = plt.subplots()
    ax = sns.heatmap(apc_amp_low_ratios, xticklabels=AMPS, yticklabels=APCS)
    ax.invert_yaxis()
    plt.xlabel("Amplitude")
    plt.ylabel("Aperiodic component")
    plt.title("Low band amplitude and aperiodic component modulation")
    plt.savefig("../figures/low_apc_amp.pdf")
    
    plt.cla()
    
    fig, ax = plt.subplots()
    # Low band amp apc modulation with logged ratios
    ax = sns.heatmap(np.log10(apc_amp_low_ratios), xticklabels=AMPS, yticklabels=APCS)
    ax.invert_yaxis()
    plt.xlabel("Amplitude")
    plt.ylabel("Aperiodic component")
    plt.title("Low band amplitude and aperiodic component modulation (logged ratios)")
    plt.savefig("../figures/low_apc_amp_log.pdf")
    
    plt.cla()
    
    #######
    ## High band amp apc modulation
    ######
    
    fig, ax = plt.subplots()
    ax = sns.heatmap(apc_amp_high_ratios, xticklabels=AMPS, yticklabels=APCS)
    ax.invert_yaxis()
    plt.xlabel("Amplitude")
    plt.ylabel("Aperiodic component")
    plt.title("High band amplitude and aperiodic component modulation")
    plt.savefig("../figures/high_apc_amp.pdf")
    
    plt.cla()
    
    fig, ax = plt.subplots()
    ax = sns.heatmap(np.log10(apc_amp_high_ratios), xticklabels=AMPS, yticklabels=APCS)
    ax.invert_yaxis()
    plt.xlabel("Amplitude")
    plt.ylabel("Aperiodic component")
    plt.title("High band amplitude and aperiodic component modulation (logged ratios)")
    plt.savefig("../figures/high_apc_amp_log.pdf")
    
    plt.cla()
    
###################### CENTER FREQUENCY & BANDWIDTH ######################    
    
    # Load data
    cf_bw_low = np.load("../dat/cf_bw_data_low.npy")
    cf_bw_high = np.load("../dat/cf_bw_data_high.npy")
    
    # calculate ratios
    cf_bw_low_ratios = calc_interacting_param_ratios(cf_bw_low)
    cf_bw_high_ratios = calc_interacting_param_ratios(cf_bw_high)
    
    # Low band
    fig, ax = plt.subplots()
    ax = sns.heatmap(cf_bw_low_ratios, xticklabels=BWS, yticklabels=CFS_LOW)
    ax.invert_yaxis()
    plt.xlabel("Bandwidth")
    plt.ylabel("Low band center frequencies")
    plt.title("Low band bandwidth and center frequency modulation")
    plt.savefig("../figures/low_bw_cf.pdf")
    
    plt.cla()
    
    # Low band logged
    fig, ax = plt.subplots()
    ax = sns.heatmap(np.log10(cf_bw_low_ratios), xticklabels=BWS, yticklabels=CFS_LOW)
    ax.invert_yaxis()
    plt.xlabel("Bandwidth")
    plt.ylabel("Low band center frequencies")
    plt.title("Low band bandwidth and center frequency modulation (logged ratios)")
    plt.savefig("../figures/low_bw_cf_log.pdf")
    
    plt.cla()
    
    # High band
    fig, ax = plt.subplots()
    ax = sns.heatmap(cf_bw_high_ratios, xticklabels=BWS, yticklabels=CFS_HIGH)
    ax.invert_yaxis()
    plt.xlabel("Bandwidth")
    plt.ylabel("High band center frequencies")
    plt.title("High band bandwidth and center frequency modulation")
    plt.savefig("../figures/high_bw_cf.pdf")
    
    plt.cla()
    
    # High band logged
    fig, ax = plt.subplots()
    ax = sns.heatmap(np.log10(cf_bw_high_ratios), xticklabels=BWS, yticklabels=CFS_HIGH)
    ax.invert_yaxis()
    plt.xlabel("Bandwidth")
    plt.ylabel("High band center frequencies")
    plt.title("High band bandwidth and center frequency modulation (logged ratios)")
    plt.savefig("../figures/high_bw_cf_log.pdf")
    
    plt.cla()  
    
###################### ROTATIONAL FREQUENCY & ROTATIONAL DELTA ######################

    #Load data
    rot_data = np.load("../dat/rot_del.npy")
                       
    # calculate ratios
    rot_ratios = calc_interacting_param_ratios(rot_data)
                       
    # plot
    fig, ax = plt.subplots()
    ax = sns.heatmap(rot_ratios, xticklabels=DELS, yticklabels=ROTS)
    ax.invert_yaxis()
    plt.xlabel("Delta power law exponent")
    plt.ylabel("Rotational frequency")
    plt.title("Rotation frequency and rotation amount")
    plt.savefig("../figures/rotation_delta.pdf")
    
    plt.cla()  
    
    fig, ax = plt.subplots()
    ax = sns.heatmap(np.log10(rot_ratios), xticklabels=DELS, yticklabels=ROTS)
    ax.invert_yaxis()
    plt.xlabel("Delta power law exponent")
    plt.ylabel("Rotational frequency")
    plt.title("Rotation frequency and rotation amount (logged ratios")
    plt.savefig("../figures/rotation_delta_log.pdf")

if __name__ == "__main__":
    main()
    