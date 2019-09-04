""" Creates super figure with interacting parameter plots"""
import sys
sys.path.append('../bratios')

import numpy as np
import matplotlib.pyplot as plt

from plot import *
def main():
    
    #Create figure for paper
    sns.set_context("talk")
    plt.figure(figsize=(24,20))

    exp_lowpw_data = np.load('../dat/interacting_param_sims/exp_lowpw_data.npy')
    lowpw_lowbw_data = np.load('../dat/interacting_param_sims/lowpw_lowbw_data.npy')
    lowcf_highbw_data = np.load('../dat/interacting_param_sims/lowcf_highbw_data.npy')
    highcf_highpw_data = np.load('../dat/interacting_param_sims/highcf_highpw_data.npy')

    ax1 = plt.subplot(221)
    ax1 = plot_paper_interacting_sims(calc_interacting_param_ratios(exp_lowcf_data),  CFS_LOW, EXPS,ax=ax1)
    plt.xticks(rotation=45, horizontalalignment='right');
    plt.yticks(rotation=0)
    plt.xlabel("Low_PW")
    plt.ylabel("Exp")

    ax2 = plt.subplot(222)
    ax2 = plot_paper_interacting_sims(calc_interacting_param_ratios(lowpw_lowbw_data), BWS, PWS ,ax=ax2)
    plt.xticks(rotation=45, horizontalalignment='right');
    plt.yticks(rotation=0)
    plt.xlabel("Low_BW")
    plt.ylabel("Low_PW")

    ax3 = plt.subplot(223)
    ax3 = plot_paper_interacting_sims(calc_interacting_param_ratios(lowcf_highbw_data), BWS, CFS_LOW,ax=ax3)
    plt.xticks(rotation=45, horizontalalignment='right');
    plt.yticks(rotation=0)
    plt.xlabel("High_BW")
    plt.ylabel("Low_CF")

    ax4 = plt.subplot(224)
    ax4 = plot_paper_interacting_sims(calc_interacting_param_ratios(highcf_highpw_data), PWS, CFS_HIGH ,ax=ax4)   
    plt.xticks(rotation=45, horizontalalignment='right');
    plt.yticks(rotation=0)
    plt.xlabel("High_PW")
    plt.ylabel("High_CF")
    
    plt.savefig("../figures/InteractingSims/interacting_params_paper_fig",dpi=400)

if __name__ == "__main__":
    main()