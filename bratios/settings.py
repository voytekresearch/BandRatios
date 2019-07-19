"Settings for running simulations"

import numpy as np

from fooof.bands import Bands

FREQ_RANGE = [1, 50]
FREQ_RES = .5
ALPHA_BAND = [8,13]
LOW_BAND = [4, 8]
HIGH_BAND = [13, 30]
AP_DEF = [0, 1]
BANDS = Bands({'theta' : LOW_BAND, 'beta' : HIGH_BAND, "alpha":ALPHA_BAND })
RATIOS = {"TBR": ['theta','beta'], "TAR":['theta', 'alpha'],"ABR": ['alpha','beta']}
SINGLE_SIM_PARAM_IND = {"CF": (0,0), "PW": (0,1), "BW": (0,2), "EXP": (1), "OFF": (0), "Alpha CF": (1,0)}
BAND_LABELS = {'T':'Theta','A':"Alpha", "B":"Beta"}
FEATURE_LABELS = ['CF', 'PW', 'BW']

CF_ALPHA_DEF = 10
CF_LOW_DEF = np.mean(LOW_BAND)
CF_HIGH_DEF = np.mean(HIGH_BAND)
CF_HIGH_INC = 1
CF_LOW_INC = .25
CFS_LOW = np.round(np.arange(LOW_BAND[0], LOW_BAND[1], CF_LOW_INC), 2)
CFS_HIGH = np.round(np.arange(HIGH_BAND[0], HIGH_BAND[1], CF_HIGH_INC), 1)

PW_DEF = .5
PW_INC = .1
PW_START = 0
PW_END = 1.5
PWS = np.round(np.arange(PW_START, PW_END, PW_INC), 1)

BW_DEF = 1
BW_INC = .2
BW_START = .2
BW_END = 4
BWS = np.round(np.arange(BW_START, BW_END, BW_INC), 1)

APC_DEF = 1
APC_START = 0
APC_END = 2.4
APC_INC = .2
APCS = np.round(np.arange(APC_START, APC_END, APC_INC), 1)

OFF_DEF = 0
OFF_START = 0
OFF_END = 2.5
OFF_INC = .25

ROT_FREQS = [1,30]
ROT_INC = 1
ROT_OSC = [10, .5, .5]
ROTS = np.round(np.arange(ROT_FREQS[0], ROT_FREQS[1], ROT_INC), 1)
DEL_RANGE = [0, 3]
DEL_INC = .1
DELS = np.round(np.arange(DEL_RANGE[0], DEL_RANGE[1], DEL_INC), 1)

# Single varying parameter
APC_PATH = '../dat/single_param_sims/apc_data'
CF_PATH_LOW = '../dat/single_param_sims/cf_data_low'
CF_PATH_HIGH = '../dat/single_param_sims/cf_data_high'
PW_PATH_LOW = '../dat/single_param_sims/pw_data_low'
PW_PATH_HIGH = '../dat/single_param_sims/pw_data_high'
BW_PATH_LOW = '../dat/single_param_sims/bw_data_low'
BW_PATH_HIGH = '../dat/single_param_sims/bw_data_high'
OFF_PATH = '../dat/single_param_sims/offset_data'
ROT_PATH = '../dat/single_param_sims/rot_data'
F_PATH = '../dat/single_param_sims/1f_data'
ALPHA_SHIFT_PATH = '../dat/single_param_sims/shifting_alpha'

# interacting varying parameters
APC_PW_LOW_PATH = '../dat/interacting_param_sims/apc_pw_data_low'
APC_PW_HIGH_PATH = '../dat/interacting_param_sims/apc_pw_data_high'
CF_BW_LOW_PATH = '../dat/interacting_param_sims/cf_bw_data_low'
CF_BW_HIGH_PATH = '../dat/interacting_param_sims/cf_bw_data_high'
ROT_DEL_PATH = '../dat/interacting_param_sims/rot_del'

# Real data path to heatmap figures directory
HEATS_PATH = '../figures/RealData/Heatmaps/'