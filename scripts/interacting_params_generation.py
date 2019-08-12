""" Functions to generate PSDs where two parameters vary simultaneously"""

from fooof.sim import *
import sys
sys.path.append('../bratios')

import numpy as np
from settings import *


def gen_interacting_per_per(param1, param2, save_path):
    fs = gen_freqs(FREQ_RANGE, FREQ_RES)
    check_per_params(param1, param2)
    out = np.zeros(shape=(len(PARAMS[param1]), len(PARAMS[param2]), len(fs) ))
    p1_stepper = Stepper(*STEPPERS[param1])

    for p1_ind, p1_val in enumerate(p1_stepper):

        p2_stepper = Stepper(*STEPPERS[param2])
        def_per_params = DEF_PARAMITER

        #Change def parameters to include stepper object
        def_per_params[PERIODIC_INDICES[param1]] = p1_val
        def_per_params[PERIODIC_INDICES[param2]] = p2_stepper
        paramiter = param_iter(def_per_params)

        for p2_ind, p2_val in enumerate(paramiter):

            fs, pws = gen_power_spectrum(FREQ_RANGE, AP_DEF, p2_val )            
            out[p1_ind, p2_ind,:] = pws
    np.save(save_path, out)


def check_per_params(param1, param2):
    if param1 not in PERIODIC or param2 not in PERIODIC:
        raise ValueError("Please provide two periodic parameters")


def gen_interacting_aper_per(param1, param2, save_path):
    fs = gen_freqs(FREQ_RANGE, FREQ_RES)

    # Set Aperiodic to param1
    aperiodic_param, periodic_param = check_interacting_params(param1, param2)
    out = np.zeros(shape=(len(PARAMS[aperiodic_param]), len(PARAMS[periodic_param]), len(fs) ))
    p1_stepper = Stepper(*STEPPERS[aperiodic_param])

    for p1_ind, p1_val in enumerate(p1_stepper):

        aperiodic_set = set_aperiodic(aperiodic_param, p1_val)
        p2_stepper = Stepper(*STEPPERS[periodic_param])
        def_per_params = DEF_PARAMITER

        #Change def parameters to include stepper object
        def_per_params[PERIODIC_INDICES[periodic_param]] = p2_stepper
        paramiter = param_iter(def_per_params)

        for p2_ind, p2_val in enumerate(paramiter):

            fs, pws = gen_power_spectrum(FREQ_RANGE, aperiodic_set, p2_val )            
            out[p1_ind, p2_ind,:] = pws

    np.save(save_path, out)

def check_interacting_params(param1, param2):
    if param1 in APERIODIC and param2 in PERIODIC:
        return param1, param2
    elif param2 in APERIODIC and param1 in PERIODIC:
        return param2, param1
    else:
        raise ValueError("Please provide both a periodic and aperiodic parameter")

def set_aperiodic(param, val):
    if param == "EXP":
        return [OFF_DEF, val]
    elif param == "OFF":
        return [val, EXP_DEF]
    else:
        raise ValueError("Please provide either 'OFF' or 'EXP' as aperiodic parameter")    