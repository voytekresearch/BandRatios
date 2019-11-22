"""This file simulates power spectra in which two parameters are varied together."""

import numpy as np

from fooof import FOOOFGroup
from fooof.sim import *

import sys
sys.path.append('../bratios')
from settings import *
from paths import DATA_PATHS as dp
from interacting_params_generation import *

###################################################################################################
###################################################################################################

def main():

    # Aperiodic Periodic
    gen_interacting_aper_per("EXP", "Low_CF", dp.sims_interacting + 'exp_lowcf_data')
    gen_interacting_aper_per("EXP", "High_CF", dp.sims_interacting + 'exp_highcf_data')
    gen_interacting_aper_per("EXP", "Low_PW", dp.sims_interacting + 'exp_lowpw_data')
    gen_interacting_aper_per("EXP", "High_PW", dp.sims_interacting + 'exp_highpw_data')
    gen_interacting_aper_per("EXP", "Low_BW", dp.sims_interacting + 'exp_lowbw_data')
    gen_interacting_aper_per("EXP", "High_BW", dp.sims_interacting + 'exp_highbw_data')

    # Periodic Periodic
    gen_interacting_per_per("Low_CF", "High_CF", dp.sims_interacting + 'lowcf_highcf_data')
    gen_interacting_per_per("Low_CF", "Low_PW", dp.sims_interacting + 'lowcf_lowpw_data')
    gen_interacting_per_per("Low_CF", "High_PW", dp.sims_interacting + 'lowcf_highpw_data')
    gen_interacting_per_per("Low_CF", "Low_BW", dp.sims_interacting + 'lowcf_lowbw_data')
    gen_interacting_per_per("Low_CF", "High_BW", dp.sims_interacting + 'lowcf_highbw_data')

    gen_interacting_per_per("High_CF", "Low_PW", dp.sims_interacting + 'highcf_lowpw_data')
    gen_interacting_per_per("High_CF", "High_PW", dp.sims_interacting + 'highcf_highpw_data')
    gen_interacting_per_per("High_CF", "Low_BW", dp.sims_interacting + 'highcf_lowbw_data')
    gen_interacting_per_per("High_CF", "High_BW", dp.sims_interacting + 'highcf_highbw_data')

    gen_interacting_per_per("Low_PW", "High_PW", dp.sims_interacting + 'lowpw_highpw_data')
    gen_interacting_per_per("Low_PW", "Low_BW", dp.sims_interacting + 'lowpw_lowbw_data')
    gen_interacting_per_per("Low_PW", "High_BW", dp.sims_interacting + 'lowpw_highbw_data')

    gen_interacting_per_per("High_PW", "Low_BW", dp.sims_interacting + 'highpw_lowbw_data')
    gen_interacting_per_per("High_PW", "High_BW", dp.sims_interacting + 'highpw_highbw_data')

    gen_interacting_per_per("Low_BW", "High_BW", dp.sims_interacting + 'lowbw_highbw_data')


if __name__ == "__main__":
    main()
