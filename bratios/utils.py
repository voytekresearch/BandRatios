"""Utilties."""

import numpy as np

###################################################################################################
###################################################################################################

def print_ap_corrs(ratio_type, corr, cis=None, ps=None, show=True):
    """Prints out the correlation between ratio and aperiodic parameters.

    Parameters
    ----------
    ratio_type : string
        Which specific ratio measure to report (ex. "TBR").
    corr : list of float
        Correlation r-values for aperiodic params.
    ps : list of float
        P-values for the correlations.
    show : boolean
        Whether to display the print out.

    Outputs
    -------
    Prints formatted sentences of correlations between ratio and aperiodic parameters.
    """

    if show:
        for ind, param in enumerate(["Exp", "Off", "Age"]):

            ci_txt = '[{:+1.4f}, {:+1.4f}]'
            ci_txt = ci_txt.format(*cis[ind, :]) if isinstance(cis, np.ndarray) else ""

            p_txt = "    {:1.4f}"
            p_txt = p_txt.format(ps[ind]) if isinstance(ps, np.ndarray) else ""

            template = "Corr of {} to {}:    {:+1.2f}    " + ci_txt + p_txt
            print(template.format(ratio_type, param, corr[ind]))


def print_stats(rs, cis, ps, labels1, labels2, show=True):
    """Print out a table of statistics.

    Parameters
    ----------
    rs : 2d array
        Correlation values.
    cis : 2d array
        Confidence intervals.
    ps : 2d array
        P values.
    labels1, labels2 : list of str
        Labels for annotate print outs.
    """

    if show:
        for r_row, ci_row, p_row, label1 in zip(rs, cis, ps, labels1):
            print(label1)
            for r_val, ci_vals, p_val, label2 in zip(r_row, ci_row, p_row, labels2):
                print_stat(label2, r_val, ci_vals, p_val)


def print_stat(label, r_val, ci_vals, p_val):
    """Print out a row of statistics."""

    template = '\t {} \t {:+1.4f}    [{:+1.4f}, {:+1.4f}]    {:1.4f}'
    print(template.format(label, r_val, *ci_vals, p_val))
