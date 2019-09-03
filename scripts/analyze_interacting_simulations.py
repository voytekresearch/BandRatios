"""This script calculates ratios and plots from simulated power spectra, with 2 varying parameters."""

import numpy as np

import sys
sys.path.append('../bratios')
from ratios import *
from settings import *
from plot import plot_interacting_sims

###################################################################################################
###################################################################################################

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


if __name__ == "__main__":
    main()
