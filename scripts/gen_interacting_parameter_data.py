"""This file simulates power spectra in which two parameters are varied together."""

import numpy as np

from fooof import FOOOFGroup
from fooof.sim import *

import sys
sys.path.append('../bratios')
from settings import *
from interacting_params_generation import *

###################################################################################################
###################################################################################################

def main():

    # Aperiodic Periodic
    gen_interacting_aper_per("EXP","Low_CF", '../dat/interacting_param_sims/exp_lowcf_data')
    gen_interacting_aper_per("EXP","High_CF", '../dat/interacting_param_sims/exp_highcf_data')
    gen_interacting_aper_per("EXP","Low_PW", '../dat/interacting_param_sims/exp_lowpw_data')
    gen_interacting_aper_per("EXP","High_PW", '../dat/interacting_param_sims/exp_highpw_data')
    gen_interacting_aper_per("EXP","Low_BW", '../dat/interacting_param_sims/exp_lowbw_data')
    gen_interacting_aper_per("EXP","High_BW", '../dat/interacting_param_sims/exp_highbw_data')

    # Periodic Periodic
    gen_interacting_per_per("Low_CF","High_CF", '../dat/interacting_param_sims/lowcf_highcf_data')
    gen_interacting_per_per("Low_CF","Low_PW", '../dat/interacting_param_sims/lowcf_lowpw_data')
    gen_interacting_per_per("Low_CF","High_PW", '../dat/interacting_param_sims/lowcf_highpw_data')
    gen_interacting_per_per("Low_CF","Low_BW", '../dat/interacting_param_sims/lowcf_lowbw_data')
    gen_interacting_per_per("Low_CF","High_BW", '../dat/interacting_param_sims/lowcf_highbw_data')

    gen_interacting_per_per("High_CF","Low_PW", '../dat/interacting_param_sims/highcf_lowpw_data')
    gen_interacting_per_per("High_CF","High_PW", '../dat/interacting_param_sims/highcf_highpw_data')
    gen_interacting_per_per("High_CF","Low_BW", '../dat/interacting_param_sims/highcf_lowbw_data')
    gen_interacting_per_per("High_CF","High_BW", '../dat/interacting_param_sims/highcf_highbw_data')

    gen_interacting_per_per("Low_PW","High_PW", '../dat/interacting_param_sims/lowpw_highpw_data')
    gen_interacting_per_per("Low_PW","Low_BW", '../dat/interacting_param_sims/lowpw_lowbw_data')
    gen_interacting_per_per("Low_PW","High_BW", '../dat/interacting_param_sims/lowpw_highbw_data')

    gen_interacting_per_per("High_PW","Low_BW", '../dat/interacting_param_sims/highpw_lowbw_data')
    gen_interacting_per_per("High_PW","High_BW", '../dat/interacting_param_sims/highpw_highbw_data')

    gen_interacting_per_per("Low_BW","High_BW", '../dat/interacting_param_sims/lowbw_highbw_data')


if __name__ == "__main__":
    main()
