"""This script calculates ratios and plots from simulated power spectral with 1 varying parameter."""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('poster')

import sys
sys.path.append('../bratios')
from ratios import *
from analysis import *
from settings import *
from plot import *
from paths import DATA_PATHS as dp
from paths import FIGS_PATHS as fp

###################################################################################################
###################################################################################################

# PLOT SETTINGS
PE_FIG_SIZE = (20, 18)
AP_FIG_SIZE = (8, 12)
SAVE_FORMAT = 'pdf'
LW = 4

###################################################################################################
###################################################################################################

def main():

    ## Load data

    cf_theta = np.load(dp.make_file_path(dp.sims_single, 'cf_theta', 'npy'))
    cf_alpha = np.load(dp.make_file_path(dp.sims_single, 'cf_alpha', 'npy'))
    cf_beta = np.load(dp.make_file_path(dp.sims_single, 'cf_beta', 'npy'))

    pw_theta = np.load(dp.make_file_path(dp.sims_single, 'pw_theta', 'npy'))
    pw_alpha = np.load(dp.make_file_path(dp.sims_single, 'pw_alpha', 'npy'))
    pw_beta = np.load(dp.make_file_path(dp.sims_single, 'pw_beta', 'npy'))

    bw_theta = np.load(dp.make_file_path(dp.sims_single, 'bw_theta', 'npy'))
    bw_alpha = np.load(dp.make_file_path(dp.sims_single, 'bw_alpha', 'npy'))
    bw_beta = np.load(dp.make_file_path(dp.sims_single, 'bw_beta', 'npy'))

    f_data = np.load(dp.make_file_path(dp.sims_single, 'exp_data', 'npy'))
    offset = np.load(dp.make_file_path(dp.sims_single, 'offset_data', 'npy'))
    exp = np.load(dp.make_file_path(dp.sims_single, 'exp_data', 'npy'))
    a_shift = np.load(dp.make_file_path(dp.sims_single, 'shifting_alpha', 'npy'))

    cf_theta_df = prep_single_sims(cf_theta, "CF")
    cf_alpha_df = prep_single_sims(cf_alpha, "CF")
    cf_beta_df = prep_single_sims(cf_beta, "CF")

    pw_theta_df = prep_single_sims(pw_theta, "PW")
    pw_alpha_df = prep_single_sims(pw_alpha, "PW")
    pw_beta_df = prep_single_sims(pw_beta, "PW")

    bw_theta_df = prep_single_sims(bw_theta, "BW")
    bw_alpha_df = prep_single_sims(bw_alpha, "BW")
    bw_beta_df = prep_single_sims(bw_beta, "BW")

    for ratio in ["TAR", "TBR", "ABR"]:

        fig = plt.figure(figsize=PE_FIG_SIZE)

        # low cf
        ax = fig.add_subplot(331)
        ax.set_xlabel("CF")
        ax.set_ylabel(ratio)
        ax.plot(cf_theta_df.iloc[:, 3], cf_theta_df[ratio], linewidth=LW)

        # low pw
        ax = fig.add_subplot(332)
        ax.set_xlabel("PW")
        ax.set_ylabel(ratio)
        ax.plot(pw_theta_df.iloc[:, 3], pw_theta_df[ratio], linewidth=LW)

        if max(pw_theta_df[ratio]) - min(pw_theta_df[ratio]) < .5:

            maxx = np.max(pw_theta_df[ratio])
            ax.set_ylim([maxx-.3, maxx+.1])

        # low bw
        ax = fig.add_subplot(333)
        ax.set_xlabel("BW")
        ax.set_ylabel(ratio)
        ax.plot(bw_theta_df.iloc[:, 3], bw_theta_df[ratio], linewidth=LW)

        if max(bw_theta_df[ratio]) - min(bw_theta_df[ratio]) < .3:

            maxx = np.max(bw_theta_df[ratio])
            ax.set_ylim([maxx-.3, maxx+.1])

        # middle cf
        ax = fig.add_subplot(334)
        ax.set_xlabel("CF")
        ax.set_ylabel(ratio)
        ax.plot(cf_alpha_df.iloc[:, 3], cf_alpha_df[ratio], linewidth=LW)

        # middle pw
        ax = fig.add_subplot(335)
        ax.set_xlabel("PW")
        ax.set_ylabel(ratio)
        ax.plot(pw_alpha_df.iloc[:, 3], pw_alpha_df[ratio], linewidth=LW)

        if max(pw_alpha_df[ratio]) - min(pw_alpha_df[ratio]) < .3:

            maxx = np.max(pw_alpha_df[ratio])
            ax.set_ylim([maxx-.3, maxx+.1])

        # middle bw
        ax = fig.add_subplot(336)
        ax.set_xlabel("BW")
        ax.set_ylabel(ratio)
        ax.plot(bw_alpha_df.iloc[:, 3], bw_alpha_df[ratio], linewidth=LW)

        if max(bw_alpha_df[ratio]) - min(bw_alpha_df[ratio]) < .3:

            maxx = np.max(bw_alpha_df[ratio])
            ax.set_ylim([maxx-.3, maxx+.1])

        # high cf
        ax = fig.add_subplot(337)
        ax.set_xlabel("CF")
        ax.set_ylabel(ratio)
        ax.plot(cf_beta_df.iloc[:, 3], cf_beta_df[ratio], linewidth=LW)

        # high pw
        ax = fig.add_subplot(338)
        ax.set_xlabel("PW")
        ax.set_ylabel(ratio)
        ax.plot(pw_beta_df.iloc[:, 3], pw_beta_df[ratio], linewidth=LW)

        if max(pw_beta_df[ratio]) - min(pw_beta_df[ratio]) < .3:

            maxx = np.max(pw_beta_df[ratio])
            ax.set_ylim([maxx-.3, maxx+.1])

        # high bw
        ax = fig.add_subplot(339)
        ax.set_xlabel("BW")
        ax.set_ylabel(ratio)
        ax.plot(bw_beta_df.iloc[:, 3], bw_beta_df[ratio], linewidth=LW)

        if max(bw_beta_df[ratio]) - min(bw_beta_df[ratio]) < .3:

            maxx = np.max(bw_beta_df[ratio])
            ax.set_ylim([maxx-.3, maxx+.1])


        plt.tight_layout()
        plt.savefig(fp.make_file_path(fp.sims_single, 'periodic_' + ratio, SAVE_FORMAT))
        plt.clf()

        ################################################

        f_df = prep_single_sims(f_data, "EXP", periodic_param=0)
        offset_df = prep_single_sims(offset, "OFF", periodic_param=0)
        exp_df = prep_single_sims(exp, "EXP", periodic_param=0)
        a_shift_df = prep_single_sims(a_shift, "Alpha CF")

        fig = plt.figure(figsize=AP_FIG_SIZE)

        # offset
        ax = fig.add_subplot(211)
        ax.set_xlabel("Off")
        ax.set_ylabel(ratio)
        ax.plot(offset_df.iloc[:, 3], offset_df[ratio], linewidth=LW)

        # exponent
        ax = fig.add_subplot(212)
        ax.set_xlabel("Exp")
        ax.set_ylabel(ratio)
        ax.plot(exp_df.iloc[:, 3], exp_df[ratio], linewidth=LW)

        plt.tight_layout()
        plt.savefig(fp.make_file_path(fp.sims_single, 'aperiodic_' + ratio, SAVE_FORMAT))


if __name__ == "__main__":
    main()
