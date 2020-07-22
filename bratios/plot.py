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

def plot_interacting_sims(data, param1, param2, plot_log=False, show=False, save_fig=False,
                          file_path=fp.sims_interacting, file_name='InteractingSims'):
    """Plots heatmaps for interacting parameter simulations.

    Parameters
    ----------
    data : list of lists
        List of power spectra.
    param1 : string
        Param used in simulation.
    param2 : string
        Param used in simulation.
    plot_log : boolean
        Whether to log values before plotting the heatmap.
    show : boolean
        Whether to display to plot.
    save_fig : boolean
        Whether to save out the figure.
    file_path : string
        Path to save the plot to.
    file_name : string
        File name to save the plot with.
    """

    # Calculate ratios
    ratios = calc_interacting_param_ratios(data)

    if plot_log:
        ratios = np.log10(ratios)
        vmin, vmax = 0, 1.6
    else:
        vmin, vmax = None, None

    fig, ax = plt.subplots()
    sns.heatmap(ratios, vmin, vmax, xticklabels=PARAMS[param2], yticklabels=PARAMS[param1])
    plt.yticks(rotation=0)

    ax.invert_yaxis()
    plt.xlabel(param2, {'fontsize' : 14})
    plt.ylabel(param1, {'fontsize' : 14})
    plt.tight_layout()

    if save_fig:
        plt.savefig(fp.make_file_path(file_path, file_name, 'pdf'));

    if not show:
        plt.close()


def plot_param_ratio_corr(data, x_labels=FEATURE_LABELS, y_labels=BAND_LABELS.values(),
                          yrotation=45, show=True, save_fig=False,
                          file_path=fp.eeg_corrs, file_name="corrplot"):
    """Plot correlations between BandRatio measures and spectral features.

    Parameters
    ----------
    data: 2x3 ndarray
        Correlations of BandRatios to Spectral Features.
    y_labels: list of strings
        Labels of slow and fast wave to use on y-axis.
    show : boolean
        Whether to display to plot.
    save_fig: boolean
        If True - save plot.
    file_path : string
        Path to save the plot to.
    file_name : string
        File name to save the plot with.
    """

    if not np.all(data):
        raise RuntimeError("No data - cannot proceed.")

    fig, ax2 = plt.subplots()
    ax2 = sns.heatmap(data, cmap="bwr", yticklabels=y_labels, xticklabels=x_labels,
                      annot=True, fmt='1.2f', vmin=-1, vmax=1, annot_kws={"size": 20}, ax=ax2);
    plt.yticks(rotation=yrotation, verticalalignment='center');

    plt.tight_layout()

    if save_fig:
        plt.savefig(fp.make_file_path(file_path, file_name, 'pdf'));

    if not show:
        plt.close()


def plot_param_ratio_corr_exp(exp, cbar=False, show=False, save_fig=False,
                              file_path=fp.eeg_corrs, file_name="exp_corrplot"):
    """Same as `plot_param_ratio_corr`, but for the exponent."""

    fig, ax1 = plt.subplots(figsize=(2.5, 1.75));
    ax1 = sns.heatmap(exp[0].reshape((1, 1)), cmap="bwr", annot=True, fmt='1.2f',
                      cbar=cbar, vmin=-1, vmax=1, annot_kws={"size": 30}, ax=ax1);

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
