"""This file simulates power spectra in which two parameters are varied together."""

import numpy as np

from fooof import FOOOFGroup
from fooof.sim import *

import sys
sys.path.append('../bratios')
from settings import *
from paths import DATA_PATHS as dp
from sims import *

###################################################################################################
###################################################################################################

def main():

    # Aperiodic Periodic
    gen_interacting_aper_per("EXP", "lowCF", dp.make_file_path(dp.sims_interacting, 'EXP_lowCF'))
    gen_interacting_aper_per("EXP", "highCF", dp.make_file_path(dp.sims_interacting, 'EXP_highCF'))
    gen_interacting_aper_per("EXP", "lowPW", dp.make_file_path(dp.sims_interacting, 'EXP_lowPW'))
    gen_interacting_aper_per("EXP", "highPW", dp.make_file_path(dp.sims_interacting, 'EXP_highPW'))
    gen_interacting_aper_per("EXP", "lowBW", dp.make_file_path(dp.sims_interacting, 'EXP_lowBW'))
    gen_interacting_aper_per("EXP", "highBW", dp.make_file_path(dp.sims_interacting, 'EXP_highBW'))

    # Periodic Periodic
    gen_interacting_per_per("lowCF", "highCF", dp.make_file_path(dp.sims_interacting, 'lowCF_highCF'))
    gen_interacting_per_per("lowCF", "lowPW", dp.make_file_path(dp.sims_interacting, 'lowCF_lowPW'))
    gen_interacting_per_per("lowCF", "highPW", dp.make_file_path(dp.sims_interacting, 'lowCF_highPW'))
    gen_interacting_per_per("lowCF", "lowBW", dp.make_file_path(dp.sims_interacting, 'lowCF_lowBW'))
    gen_interacting_per_per("lowCF", "highBW", dp.make_file_path(dp.sims_interacting, 'lowCF_highBW'))

    gen_interacting_per_per("highCF", "lowPW", dp.make_file_path(dp.sims_interacting, 'highCF_lowPW'))
    gen_interacting_per_per("highCF", "highPW", dp.make_file_path(dp.sims_interacting, 'highCF_highPW'))
    gen_interacting_per_per("highCF", "lowBW", dp.make_file_path(dp.sims_interacting, 'highCF_lowBW'))
    gen_interacting_per_per("highCF", "highBW", dp.make_file_path(dp.sims_interacting, 'highCF_highBW'))

    gen_interacting_per_per("lowPW", "highPW", dp.make_file_path(dp.sims_interacting, 'lowPW_highPW'))
    gen_interacting_per_per("lowPW", "lowBW", dp.make_file_path(dp.sims_interacting, 'lowPW_lowBW'))
    gen_interacting_per_per("lowPW", "highBW", dp.make_file_path(dp.sims_interacting, 'lowPW_highBW'))

    gen_interacting_per_per("highPW", "lowBW", dp.make_file_path(dp.sims_interacting, 'highPW_lowBW'))
    gen_interacting_per_per("highPW", "highBW", dp.make_file_path(dp.sims_interacting, 'highPW_highBW'))

    gen_interacting_per_per("lowBW", "highBW", dp.make_file_path(dp.sims_interacting, 'lowBW_highBW'))


if __name__ == "__main__":
    main()
