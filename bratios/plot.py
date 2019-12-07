"""A collection of functions to plot data."""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm
import mne

from ratios import calc_interacting_param_ratios
from settings import *
from paths import FIGS_PATHS as fp

###################################################################################################
###################################################################################################

def plot_interacting_sims(data, param1, param2, savepath):
    """Plots heatmaps for interacting parameter simulations.

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

    # Calculate ratios
    ratios = calc_interacting_param_ratios(data)

    fig, ax = plt.subplots()
    sns.heatmap(ratios, xticklabels=PARAMS[param2], yticklabels=PARAMS[param1])

    ax.invert_yaxis()
    plt.xlabel(param1)
    plt.ylabel(param2)
    plt.savefig(savepath+".pdf", dpi=500)
    plt.close()


def plot_param_ratio_corr(data, title="Ratio vs. Spectral Features",
                          y_labels=["Theta", "Alpha", "Beta"], show=True,
                          save_fig=False, file_path=fp.eeg_corrs, file_name="Spectral_Features_Ratio_corr"):
    """Plot correlations between BandRatio measures and spectral features.

    Parameters
    ----------
    data: 2x3 ndarray
        Correlations of BandRatios to Spectral Features.
    title: string
        Title of plot.
    y_labels: list of strings
        Labels of slow and fast wave to use on y-axis.
    save_fig: boolean
        If True - save plot.
    """

    if not np.all(data):
        raise RuntimeError("No data - cannot proceed.")

    fig, ax2 = plt.subplots()
    ax2 = sns.heatmap(data, cmap="bwr", yticklabels=y_labels, xticklabels=FEATURE_LABELS,
                      annot=True, ax=ax2, vmin=-1, vmax=1, annot_kws={"size": 20});
    plt.yticks(rotation=45, verticalalignment='center');

    if save_fig:
        plt.savefig(fp.make_file_path(file_path, file_name, 'pdf'));

    if not show:
        plt.close()


def plot_param_ratio_corr_exp(exp, title="Ratio vs. Spectral Features",  show=False,
                              save_fig=False, file_path=fp.eeg_corrs,
                              file_name="Spectral_Features_Ratio_corr",):
    """Same as `plot_param_ratio_corr`, but for the exponent."""

    fig, ax1 = plt.subplots();
    ax1 = sns.heatmap(exp[0].reshape((1,1)), cmap="bwr", annot=True,
                      ax=ax1, vmin=-1, vmax=1, annot_kws={"size": 35});

    plt.tick_params(axis='both', which='both', bottom=False, top=False,
                    labelbottom=False, left=False, labelleft=False);

    if save_fig:
        plt.savefig(fp.make_file_path(file_path, file_name + '_exp', 'pdf'));

    if not show:
        plt.close()


def plot_param_topo(data, raw, label='', save=False):
    """Plots the topography of a spectral parameter."""

    fig, ax = plt.subplots();
    mne.viz.plot_topomap(data, raw.info, vmin=min(data), vmax=max(data),
                         cmap=cm.viridis, contours=0, axes=ax);
    ax.set_title(label)

    if save:
        fig.savefig(fp.make_file_path(fp.eeg_topos, label + '-topo', 'pdf'));
