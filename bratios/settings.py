"Settings for running simulations"

import numpy as np

FREQ_RANGE = [1, 50]
LOW_BAND = [4, 8]
HIGH_BAND = [13, 30]
BG_DEF = [0, 1]

CF_LOW_DEF = np.mean(LOW_BAND)
CF_HIGH_DEF = np.mean(HIGH_BAND)
CF_INC = .1
CFS_LOW = np.round(np.arange(LOW_BAND[0], LOW_BAND[1], CF_INC), 1)
CFS_HIGH = np.round(np.arange(HIGH_BAND[0], HIGH_BAND[1], CF_INC), 1)

AMP_DEF = .75
AMP_INC = .1
AMP_START = 0
AMP_END = 1.5
AMPS = np.round(np.arange(AMP_START, AMP_END, AMP_INC), 1)

BW_DEF = 1
BW_INC = .1
BW_START = .2
BW_END = 4
BWS = np.round(np.arange(BW_START, BW_END, BW_INC), 1)

APC_DEF = 1
APC_START = 0
APC_END = 3
APC_INC = .2
APCS = np.round(np.arange(APC_START, APC_END, APC_INC), 1)

OFF_START = 0
OFF_END = 2.5
OFF_INC = .25

ROT_START = -1.5
ROT_END = 1.5
ROT_INC = .2

APC_PATH = '../dat/apc_data'
CF_PATH_LOW = '../dat/cf_data_low'
CF_PATH_HIGH = '../dat/cf_data_high'
AMP_PATH_LOW = '../dat/amp_data_low'
AMP_PATH_HIGH = '../dat/amp_data_high'
BW_PATH_LOW = '../dat/bw_data_low'
BW_PATH_HIGH = '../dat/bw_data_high'
OFF_PATH = '../dat/offset_data'
ROT_PATH = '../dat/rot_data'

APC_AMP_LOW_PATH = '../dat/apc_amp_data_low'
APC_AMP_HIGH_PATH = '../dat/apc_amp_data_high'
CF_BW_LOW_PATH = '../dat/cf_bw_data_low'
CF_BW_HIGH_PATH = '../dat/cf_bw_data_high'
