""" A collection of functions to plot data"""
import sys
sys.path.append('../bratios')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from ratios import calc_interacting_param_ratios
from settings import *

titles = {
    'CF' : 'Center Frequency',
    'PW' : 'Power', 
    'BW' : 'Bandwidth', 
    'exponent' : 'Exponent', 
    'offset' : 'Offset'
}


def plot_paper_interacting_sims():
    fig = plt.figure(figsize=[20, 20])

    # load data
    apc_amp_low = np.load("../dat/interacting_param_sims/apc_pw_data_low.npy")
    apc_amp_high = np.load("../dat/interacting_param_sims/apc_pw_data_high.npy")
    cf_bw_low = np.load("../dat/interacting_param_sims/cf_bw_data_low.npy")
    cf_bw_high = np.load("../dat/interacting_param_sims/cf_bw_data_high.npy")

    # calculate ratios
    apc_amp_low_ratios = calc_interacting_param_ratios(apc_amp_low)
    cf_bw_low_ratios = calc_interacting_param_ratios(cf_bw_low)
    cf_bw_high_ratios = calc_interacting_param_ratios(cf_bw_high)
    apc_amp_high_ratios = calc_interacting_param_ratios(apc_amp_high)

    ax= fig.add_subplot(221)
    ax = sns.heatmap(np.log10(apc_amp_low_ratios), xticklabels=PWS, yticklabels=APCS)
    ax.invert_yaxis()
    plt.xlabel("PW",{"fontsize": 18})
    plt.ylabel("EXP",{"fontsize": 18})

    ax= fig.add_subplot(222)
    ax = sns.heatmap(np.log10(apc_amp_high_ratios), xticklabels=PWS, yticklabels=APCS)
    ax.invert_yaxis()
    plt.xlabel("PW",{"fontsize": 18})
    plt.ylabel("EXP",{"fontsize": 18})


    # Low band logged
    ax = fig.add_subplot(223)
    ax = sns.heatmap(np.log10(cf_bw_low_ratios), xticklabels=BWS, yticklabels=CFS_LOW)
    ax.invert_yaxis()
    plt.xlabel("BW",{"fontsize": 18})
    plt.ylabel("CF",{"fontsize": 18})

    ax = fig.add_subplot(224)
    ax = sns.heatmap(np.log10(cf_bw_high_ratios), xticklabels=BWS, yticklabels=CFS_HIGH)
    ax.invert_yaxis()
    plt.xlabel("BW",{"fontsize": 18})
    plt.ylabel("CF", {"fontsize": 18})

    
def plot_interacting_sims(data, param1, param2, savepath):
    """ Plots heatmaps for interacting parameter simulations.
    
    Parameters
    ----------
    data : list of lists
        List of power spectra.
    param1 : String
        Param used in simulation.
    param2 : String
        Param used in simulation.
    savepath : string
        Path to save plots.
        
    """
    
    #calculate ratios
    ratios = calc_interacting_param_ratios(data)

    fig, ax = plt.subplots()
    sns.heatmap(ratios, xticklabels=PARAMS[param2], yticklabels=PARAMS[param1])
    ax.invert_yaxis()
    plt.xlabel(param1)
    plt.ylabel(param2)
    plt.savefig(savepath, dpi=500)
    plt.close()
    
    
def plot_single_param_sims(df,filename="param_vs_ratios"):

    # Get param name
    param_name = df.columns[3]
    
    # Subplots - define the figure
    fig = plt.figure(figsize=[10, 14])

    #TBR by PW
    ax1= fig.add_subplot(321)
    ax1.set_xlabel(param_name,{"fontsize": 18})
    ax1.set_ylabel("TBR",{"fontsize": 18})
    ax1.plot(df[param_name], df.TBR, color='r')

    ax11= fig.add_subplot(322)
    ax11.set_xlabel(param_name,{"fontsize": 18})
    ax11.set_ylabel("TBR",{"fontsize": 18})
    ax11.set_yscale('log')
    ax11.plot(df[param_name], df.TBR, color='r')

    #TAR by PW
    ax2= fig.add_subplot(323)
    ax2.set_xlabel(param_name,{"fontsize": 18})
    ax2.set_ylabel("TAR",{"fontsize": 18})
    ax2.plot(df[param_name], df.TAR, color='r')

    ax21= fig.add_subplot(324)
    ax21.set_xlabel(param_name,{"fontsize": 18})
    ax21.set_ylabel("TAR",{"fontsize": 18})
    ax21.set_yscale('log')
    ax21.plot(df[param_name], df.TAR, color='r')

    #ABR by BW
    ax3= fig.add_subplot(325)
    ax3.set_xlabel(param_name,{"fontsize": 18})
    ax3.set_ylabel("ABR",{"fontsize": 18})
    ax3.plot(df[param_name], df.ABR, color='r')

    ax31= fig.add_subplot(326)
    ax31.set_xlabel(param_name,{"fontsize": 18})
    ax31.set_ylabel("ABR",{"fontsize": 18})
    ax31.set_yscale('log')
    ax31.plot(df[param_name], df.ABR, color='r')

    plt.tight_layout()
    plt.savefig("../figures/SingleParamSims/"+filename, dpi=700)
    
    
def plot_single_param(df, title=None, xlabel=None, ylabel=None, ax=None):    
    """plots ratios by param value.
    
    Parameters
    ----------
    df : Dataframe
        Data structure holding ratios and parameter values
    title : String
        Title on plot.
    xlabel : String
        Lablel used on x axis.
    ylabel : String
        Lablel used on y axis.
    ax : axes
        Optional plotting axis.
    
    """
    
    if not ax:
        _, ax = plt.subplots(figsize=[4, 4])

    ax.set_title(title, {"fontsize": 18})

    ax.set_xlabel(xlabel, {"fontsize": 18})
    ax.set_ylabel(ylabel, {"fontsize": 18})

    ax.plot(df.param, df.ratio, color='r', linewidth=2)

    plt.tight_layout()
    
    
def plot_paper_single_sims():
    fig, ax = plt.subplots(2, 4, figsize=[12, 6])
    for (f_name, field), axis in zip(list_of_files.items(), ax.flatten()):
        df = proc_single_param(f_name, field)
        plot_single_param(df, title=titles[field], ylabel='Ratio', ax=axis)

    plt.savefig("../figures/SingleParamSims.png", dpi=700)
