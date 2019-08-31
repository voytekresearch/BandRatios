"""A collection of functions to plot data."""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm
import mne

from ratios import calc_interacting_param_ratios
from settings import *

###################################################################################################
###################################################################################################

titles = {
    'CF' : 'Center Frequency',
    'PW' : 'Power',
    'BW' : 'Bandwidth',
    'exponent' : 'Exponent',
    'offset' : 'Offset'
}

###################################################################################################
###################################################################################################

def plot_paper_interacting_sims(data,xticklabs, yticklabs, plt_log=True,ax=None):
    """Plots interacting simulation figures used in paper. Expects psds."""

    fig = plt.figure(figsize=[20, 20])

    if not ax:
        _, ax = plt.subpplots()

    if plt_log:
        data = np.log10(data)
    ax = sns.heatmap(data, xticklabels=xticklabs, yticklabels=yticklabs)
    ax.invert_yaxis()

    return ax


#     # calculate ratios
#     apc_amp_low_ratios = calc_interacting_param_ratios(apc_amp_low)
#     cf_bw_low_ratios = calc_interacting_param_ratios(cf_bw_low)
#     cf_bw_high_ratios = calc_interacting_param_ratios(cf_bw_high)
#     apc_amp_high_ratios = calc_interacting_param_ratios(apc_amp_high)

#     ax= fig.add_subplot(221)

#     plt.xlabel("PW",{"fontsize": 18})
#     plt.ylabel("EXP",{"fontsize": 18})

#     ax= fig.add_subplot(222)
#     ax = sns.heatmap(np.log10(apc_amp_high_ratios), xticklabels=PWS, yticklabels=APCS)
#     ax.invert_yaxis()
#     plt.xlabel("PW",{"fontsize": 18})
#     plt.ylabel("EXP",{"fontsize": 18})


#     # Low band logged
#     ax = fig.add_subplot(223)
#     ax = sns.heatmap(np.log10(cf_bw_low_ratios), xticklabels=BWS, yticklabels=CFS_LOW)
#     ax.invert_yaxis()
#     plt.xlabel("BW",{"fontsize": 18})
#     plt.ylabel("CF",{"fontsize": 18})

#     ax = fig.add_subplot(224)
#     ax = sns.heatmap(np.log10(cf_bw_high_ratios), xticklabels=BWS, yticklabels=CFS_HIGH)
#     ax.invert_yaxis()
#     plt.xlabel("BW",{"fontsize": 18})
#     plt.ylabel("CF", {"fontsize": 18})


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


def plot_single_param_sims(df, filename="param_vs_ratios"):
    """Plots results of single parameter variation similations.

    Parameters
    ----------
    df : dataframe
        ratios and varied_param.
    filename : String
        path to save plot.

    Outputs
    -------
    Plot of each ratio by the varied param values.

    """

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


def plot_param_ratio_corr(data, exp, title="Ratio vs. Spectral Features",y_labels=["SW","FW", "NonRatioBand"], save_fig=False, file_path= HEATS_PATH, file_name="Spectral_Features_Ratio_corr"):
    """Plot correlations between BandRatio measures and spectral features.

    Parameters
    ----------
    data: 2x3 ndarray
        Correlations of BandRatios to Spectral Features.
    title: string
        Title of plot.
    y_labels: list of strings.
        Lables of slow and fast wave to use on y-axis.
    save_fig: boolean
        If True - save plot
    """

    if not np.all(data):
        raise RuntimeError("No data - cannot proceed.")

    fig, ax1 = plt.subplots()
    ax1 = sns.heatmap(exp[0].reshape((1,1)),cmap="bwr", annot=True, ax=ax1, vmin=-1, vmax=1, annot_kws={"size": 20})
    if save_fig:
        plt.savefig(file_path+file_name+"_exp.png")

    plt.clf()

    fig, ax2 = plt.subplots()
    ax2 = sns.heatmap(data,cmap="bwr", yticklabels=y_labels, xticklabels=FEATURE_LABELS,\
                      annot=True, ax=ax2, vmin=-1, vmax=1, annot_kws={"size": 20})
    if save_fig:
        plt.savefig(file_path+file_name+".png")


def plot_paper_single_sims():
    """Plots results of single param varation simulations used in paper."""

    fig, ax = plt.subplots(2, 4, figsize=[12, 6])
    for (f_name, field), axis in zip(list_of_files.items(), ax.flatten()):
        df = proc_single_param(f_name, field)
        plot_single_param(df, title=titles[field], ylabel='Ratio', ax=axis)

    plt.savefig("../figures/SingleParamSims.png", dpi=700)


def plot_param_topo(data,raw, filename="topo"):
    """Plots the topography of a spectral parameters."""

    fig, ax = plt.subplots();
    mne.viz.plot_topomap(data, raw.info, vmin=min(data), vmax=max(data), cmap=cm.viridis, contours=0, axes=ax);
    ax.set_title(filename)
    fig.savefig('../figures/RealData/'+filename, dpi=700);
