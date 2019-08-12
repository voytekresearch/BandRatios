""" This script calculates ratios and plots from simulated power spectral data where two parameters vary."""
import sys
sys.path.append('../bratios')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

from fooof import FOOOF, FOOOFGroup

from ratios import *
from settings import *
from plot import plot_interacting_sims

def main():
    
    exp_lowcf_data = np.load('../dat/interacting_param_sims/exp_lowcf_data.npy')
    exp_highcf_data = np.load('../dat/interacting_param_sims/exp_highcf_data.npy')
    exp_lowpw_data = np.load('../dat/interacting_param_sims/exp_lowpw_data.npy')
    exp_highpw_data = np.load('../dat/interacting_param_sims/exp_highpw_data.npy')
    exp_lowbw_data = np.load('../dat/interacting_param_sims/exp_lowbw_data.npy')
    exp_highbw_data = np.load('../dat/interacting_param_sims/exp_highbw_data.npy')
    lowcf_highcf_data = np.load('../dat/interacting_param_sims/lowcf_highcf_data.npy')
    lowcf_lowpw_data = np.load('../dat/interacting_param_sims/lowcf_lowpw_data.npy')
    lowcf_highpw_data = np.load('../dat/interacting_param_sims/lowcf_highpw_data.npy')
    lowcf_lowbw_data = np.load('../dat/interacting_param_sims/lowcf_lowbw_data.npy')
    lowcf_highbw_data = np.load('../dat/interacting_param_sims/lowcf_highbw_data.npy')
    highcf_lowpw_data = np.load('../dat/interacting_param_sims/highcf_lowpw_data.npy')
    highcf_highpw_data = np.load('../dat/interacting_param_sims/highcf_highpw_data.npy')
    highcf_lowbw_data = np.load('../dat/interacting_param_sims/highcf_lowbw_data.npy')
    highcf_highbw_data = np.load('../dat/interacting_param_sims/highcf_highbw_data.npy')
    lowpw_highpw_data = np.load('../dat/interacting_param_sims/lowpw_highpw_data.npy')
    lowpw_lowbw_data = np.load('../dat/interacting_param_sims/lowpw_lowbw_data.npy')
    lowpw_highbw_data = np.load('../dat/interacting_param_sims/lowpw_highbw_data.npy')
    highpw_lowbw_data = np.load('../dat/interacting_param_sims/highpw_lowbw_data.npy')
    highpw_highbw_data = np.load('../dat/interacting_param_sims/highpw_highbw_data.npy')
    lowbw_highbw_data = np.load('../dat/interacting_param_sims/lowbw_highbw_data.npy')


    plot_interacting_sims(exp_lowcf_data,"EXP", "Low_CF",'../figures/InteractingSims/exp_lowcf_data')
    plot_interacting_sims(exp_highcf_data,"EXP","High_CF",'../figures/InteractingSims/exp_highcf_data')
    plot_interacting_sims(exp_lowpw_data,"EXP","Low_PW",'../figures/InteractingSims/exp_lowpw_data')
    plot_interacting_sims(exp_highpw_data,"EXP","High_PW",'../figures/InteractingSims/exp_highpw_data')
    plot_interacting_sims(exp_lowbw_data,"EXP","Low_BW",'../figures/InteractingSims/exp_lowbw_data')
    plot_interacting_sims(exp_highbw_data,"EXP","High_BW",'../figures/InteractingSims/exp_highbw_data')
    plot_interacting_sims(lowcf_highcf_data,"Low_CF","High_CF",'../figures/InteractingSims/lowcf_highcf_data')
    plot_interacting_sims(lowcf_lowpw_data,"Low_CF","Low_PW",'../figures/InteractingSims/lowcf_lowpw_data')
    plot_interacting_sims(lowcf_highpw_data,"Low_CF","High_PW",'../figures/InteractingSims/lowcf_highpw_data')
    plot_interacting_sims(lowcf_lowbw_data,"Low_CF","Low_BW",'../figures/InteractingSims/lowcf_lowbw_data')
    plot_interacting_sims(lowcf_highbw_data,"Low_CF","High_BW",'../figures/InteractingSims/lowcf_highbw_data')
    plot_interacting_sims(highcf_lowpw_data,"High_CF","Low_PW",'../figures/InteractingSims/highcf_lowpw_data')
    plot_interacting_sims(highcf_highpw_data,"High_CF","High_PW",'../figures/InteractingSims/highcf_highpw_data')
    plot_interacting_sims(highcf_lowbw_data,"High_CF","Low_BW",'../figures/InteractingSims/highcf_lowbw_data')
    plot_interacting_sims(highcf_highbw_data,"High_CF","High_BW",'../figures/InteractingSims/highcf_highbw_data')
    plot_interacting_sims(lowpw_highpw_data,"Low_PW","High_PW" ,'../figures/InteractingSims/lowpw_highpw_data')
    plot_interacting_sims(lowpw_lowbw_data,"Low_PW","Low_BW",'../figures/InteractingSims/lowpw_lowbw_data')
    plot_interacting_sims(lowpw_highbw_data,"Low_PW","High_BW",'../figures/InteractingSims/lowpw_highbw_data')
    plot_interacting_sims(highpw_lowbw_data,"High_PW","Low_BW",'../figures/InteractingSims/highpw_lowbw_data')
    plot_interacting_sims(highpw_highbw_data,"High_PW","High_BW",'../figures/InteractingSims/highpw_highbw_data')
    plot_interacting_sims(lowbw_highbw_data,"Low_BW","High_BW",'../figures/InteractingSims/lowbw_highbw_data')















    
    
# ###################### APERIODIC COMPONENT & AMPLITUDE ######################

#     # load data
#     apc_amp_low = np.load("../dat/interacting_param_sims/apc_amp_data_low.npy")
#     apc_amp_high = np.load("../dat/interacting_param_sims/apc_amp_data_high.npy")

#     # calculate ratios
#     apc_amp_low_ratios = calc_interacting_param_ratios(apc_amp_low)
#     apc_amp_high_ratios = calc_interacting_param_ratios(apc_amp_high)
    
#     # Low band amp apc modulation
#     fig, ax = plt.subplots()
#     ax = sns.heatmap(apc_amp_low_ratios, xticklabels=AMPS, yticklabels=APCS)
#     ax.invert_yaxis()
#     plt.xlabel("Amplitude")
#     plt.ylabel("Exponent")
#     plt.title("Low band amplitude and exponent modulation")
#     plt.savefig("../figures/InteractingSims/low_apc_amp.png",dpi=500)
    
#     plt.cla()
    
#     fig, ax = plt.subplots()
#     # Low band amp apc modulation with logged ratios
#     ax = sns.heatmap(np.log10(apc_amp_low_ratios), xticklabels=AMPS, yticklabels=APCS)
#     ax.invert_yaxis()
#     plt.xlabel("PW", {"fontsize": 18})
#     plt.ylabel("EXP", {"fontsize": 18})
#     plt.title("Low band PW and EXP",{"fontsize": 18})
#     plt.savefig("../figures/InteractingSims/low_apc_amp_log.png", dpi=500)
    
#     plt.cla()
    
#     #######
#     ## High band amp apc modulation
#     ######
    
#     fig, ax = plt.subplots()
#     ax = sns.heatmap(apc_amp_high_ratios, xticklabels=AMPS, yticklabels=APCS)
#     ax.invert_yaxis()
#     plt.xlabel("Amplitude")
#     plt.ylabel("Exponent")
#     plt.title("High band amplitude and exponent modulation")
#     plt.savefig("../figures/InteractingSims/high_apc_amp.png", dpi=500)
    
#     plt.cla()
    
#     fig, ax = plt.subplots()
#     ax = sns.heatmap(np.log10(apc_amp_high_ratios), xticklabels=AMPS, yticklabels=APCS)
#     ax.invert_yaxis()
#     plt.xlabel("PW", {"fontsize": 18})
#     plt.ylabel("EXP", {"fontsize": 18})
#     plt.title("High band PW vs EXP", {"fontsize": 18})
#     plt.tight_layout()
#     plt.savefig("../figures/InteractingSims/high_apc_amp_log.png", dpi=500)
    
#     plt.cla()
    
# ###################### CENTER FREQUENCY & BANDWIDTH ######################    
    
#     # Load data
#     cf_bw_low = np.load("../dat/interacting_param_sims/cf_bw_data_low.npy")
#     cf_bw_high = np.load("../dat/interacting_param_sims/cf_bw_data_high.npy")
    
#     # calculate ratios
#     cf_bw_low_ratios = calc_interacting_param_ratios(cf_bw_low)
#     cf_bw_high_ratios = calc_interacting_param_ratios(cf_bw_high)
    
#     # Low band
#     fig, ax = plt.subplots()
#     ax = sns.heatmap(cf_bw_low_ratios, xticklabels=BWS, yticklabels=CFS_LOW)
#     ax.invert_yaxis()
#     plt.xlabel("Bandwidth", {"fontsize": 18})
#     plt.ylabel("Low band center frequencies", {"fontsize": 18})
#     plt.title("Low band bandwidth vs center frequency", {"fontsize": 18})
#     plt.tight_layout()
#     plt.savefig("../figures/InteractingSims/low_bw_cf.png", dpi=500)
    
#     plt.cla()
    
#     # Low band logged
#     fig, ax = plt.subplots()
#     ax = sns.heatmap(np.log10(cf_bw_low_ratios), xticklabels=BWS, yticklabels=CFS_LOW)
#     ax.invert_yaxis()
#     plt.xlabel("BW",{"fontsize": 18})
#     plt.ylabel("CF",{"fontsize": 18})
#     plt.title("Low band BW vs Low band CF",{"fontsize": 18})
#     plt.tight_layout()
#     plt.savefig("../figures/InteractingSims/low_bw_cf_log.png", dpi=500)
    
#     plt.cla()
    
#     # High band
#     fig, ax = plt.subplots()
#     ax = sns.heatmap(cf_bw_high_ratios, xticklabels=BWS, yticklabels=CFS_HIGH)
#     ax.invert_yaxis()
#     plt.xlabel("Bandwidth",{"fontsize": 18})
#     plt.ylabel("Center Frequencies",{"fontsize": 18})
#     #plt.title("High band bandwidth and center frequency modulation")
#     plt.tight_layout()
#     plt.savefig("../figures/InteractingSims/high_bw_cf.png", dpi=500)
    
#     plt.cla()
    
#     # High band logged
#     fig, ax = plt.subplots()
#     ax = sns.heatmap(np.log10(cf_bw_high_ratios), xticklabels=BWS, yticklabels=CFS_HIGH)
#     ax.invert_yaxis()
#     plt.xlabel("BW",{"fontsize": 18})
#     plt.ylabel("CF", {"fontsize": 18})
#     plt.title("High band BW vs CF", {"fontsize": 18})
#     plt.tight_layout()
#     plt.savefig("../figures/InteractingSims/high_bw_cf_log.png", dpi=500)
    
#     plt.cla()  
    
# ###################### ROTATIONAL FREQUENCY & ROTATIONAL DELTA ######################

#     #Load data
#     rot_data = np.load("../dat/interacting_param_sims/rot_del.npy")
                       
#     # calculate ratios
#     rot_ratios = calc_interacting_param_ratios(rot_data)
                       
#     # plot
#     fig, ax = plt.subplots()
#     ax = sns.heatmap(rot_ratios, xticklabels=DELS, yticklabels=ROTS)
#     ax.invert_yaxis()
#     plt.xlabel("Delta power law exponent")
#     plt.ylabel("Rotational frequency")
#     plt.title("Rotation frequency and rotation amount")
#     plt.savefig("../figures/InteractingSims/rotation_delta.png", dpi=500)
    
#     plt.cla()  
    
#     fig, ax = plt.subplots()
#     ax = sns.heatmap(np.log10(rot_ratios), xticklabels=DELS, yticklabels=ROTS)
#     ax.invert_yaxis()
#     plt.xlabel("Delta power law exponent")
#     plt.ylabel("Rotational frequency")
#     plt.title("Rotation frequency and rotation amount")
#     plt.savefig("../figures/InteractingSims/rotation_delta_log.png", dpi=500)

if __name__ == "__main__":
    main()
    