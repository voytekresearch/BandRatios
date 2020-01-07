"""This script calculates ratios and plots from simulated power spectra, with 2 varying parameters."""

import numpy as np

import sys
sys.path.append('../bratios')
from ratios import *
from settings import *
from paths import DATA_PATHS as dp
from plot import plot_interacting_sims

###################################################################################################
###################################################################################################

# Settings
PLOT_LOG = True
SAVE_FIG = True

COMBOS = ['EXP_lowCF', 'EXP_highCF',
          'EXP_lowPW', 'EXP_highPW',
          'EXP_lowBW', 'EXP_highBW',
          'lowCF_highCF',
          'lowCF_lowPW', 'lowCF_highPW',
          'lowCF_lowBW', 'lowCF_highBW',
          'highCF_lowPW', 'highCF_highPW',
          'highCF_lowBW', 'highCF_highBW',
          'lowPW_lowBW',
          'lowPW_highPW',
          'highPW_lowBW', 'lowPW_highBW',
          'highPW_highBW',
          'lowBW_highBW']

###################################################################################################
###################################################################################################

def main():

    for data_label in COMBOS:

        # Load the data
        data = np.load(dp.make_file_path(dp.sims_interacting, data_label, 'npy'))

        # Calculate ratios and create the plots
        plot_interacting_sims(data, *data_label.split('_'), plot_log=PLOT_LOG,
                              save_fig=SAVE_FIG, file_name=data_label)


if __name__ == "__main__":
    main()
