""" Creates super figure with interacting parameter plots"""
import sys
sys.path.append('../bratios')

import numpy as np
import matplotlib.pyplot as plt

from plot import *
def main():
    
    #Create figure for paper
    plt.figure(figsize=(14,12))

    #Import data
    exp_lowcf_data = np.load('../dat/interacting_param_sims/exp_lowcf_data.npy')
    lowpw_lowbw_data = np.load('../dat/interacting_param_sims/lowpw_lowbw_data.npy')
    lowcf_highbw_data = np.load('../dat/interacting_param_sims/lowcf_highbw_data.npy')
    highcf_highpw_data = np.load('../dat/interacting_param_sims/highcf_highpw_data.npy')

    ax1 = plt.subplot(221)
    ax1 = plot_interacting_sims_paper(calc_interacting_param_ratios(exp_lowcf_data),  CFS_LOW, EXPS,ax=ax1)
    plt.xticks(rotation=45, horizontalalignment='right');
    plt.yticks(rotation=0)
    
    ax2 = plt.subplot(222)
    ax2 = plot_interacting_sims_paper(calc_interacting_param_ratios(lowpw_lowbw_data), BWS, PWS ,ax=ax2)
    plt.xticks(rotation=45, horizontalalignment='right');
    plt.yticks(rotation=0)
    
    ax3 = plt.subplot(223)
    ax3 = plot_interacting_sims_paper(calc_interacting_param_ratios(lowcf_highbw_data), BWS, CFS_LOW,ax=ax3)
    plt.xticks(rotation=45, horizontalalignment='right');
    plt.yticks(rotation=0)
    
    ax4 = plt.subplot(224)
    ax4 = plot_interacting_sims_paper(calc_interacting_param_ratios(highcf_highpw_data), PWS, CFS_HIGH ,ax=ax4)   
    plt.xticks(rotation=45, horizontalalignment='right');
    plt.yticks(rotation=0)
    
    plt.savefig("../figures/InteractingSims/interacting_params_paper_fig",dpi=400)

    
if __name__ == "__main__":
    main()