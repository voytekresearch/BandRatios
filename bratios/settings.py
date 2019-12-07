""""Settings for running simulations."""

import numpy as np

from fooof.bands import Bands

###################################################################################################
###################################################################################################

#####################################
#### DEFINE LABELS & DEFINITIONS ####
#####################################

# Define spectra definitions
FREQ_RANGE = [1, 50]
FREQ_RES = .5

# Define band definitions
THETA_BAND = [4, 8]
ALPHA_BAND = [8, 13]
BETA_BAND = [13, 30]

# Alias relative band labels
LOW_BAND = THETA_BAND
MIDDLE_BAND = ALPHA_BAND
HIGH_BAND = BETA_BAND

# Define default aperiodic definition
AP_DEF = [0, 1]

# Define bands
BANDS = Bands({"theta" : THETA_BAND, "beta" : BETA_BAND, "alpha" : ALPHA_BAND})
BAND_LABELS = {"T" : "Theta", "A" : "Alpha", "B" : "Beta"}

# Define ratio
RATIOS = {"TBR": ["theta", "beta"], "TAR" : ["theta", "alpha"] , "ABR" : ["alpha", "beta"]}

# Define labels & indices
SINGLE_SIM_PARAM_IND = {"CF" : (0, 0), "PW" : (0, 1), "BW" : (0, 2),
                        "EXP" : (1), "OFF" : (0), "Alpha CF" : (1, 0)}

FEATURE_LABELS = ["CF", "PW", "BW"]
PERIODIC = ["Low_CF", "High_CF", "Low_PW", "High_PW", "Low_BW", "High_BW"]
APERIODIC = ["EXP", "OFF"]

PERIODIC_INDICES = {
    "Low_CF" : 0,
    "High_CF" : 3,
    "Low_PW" : 1,
    "High_PW" : 4,
    "Low_BW" : 2,
    "High_BW" : 5,
    }

#################################
#### DEFINE PARAMETER RANGES ####
#################################

# Define ranges for varying center frequency
CF_LOW_DEF = np.mean(LOW_BAND)
CF_ALPHA_DEF = 10
CF_HIGH_DEF = np.mean(HIGH_BAND)
CF_INC = .5
CFS_LOW = np.round(np.arange(LOW_BAND[0], LOW_BAND[1], CF_INC), 3)
CFS_HIGH = np.round(np.arange(HIGH_BAND[0], HIGH_BAND[1], CF_INC), 3)

# Define ranges for varying power
PW_DEF = .5
PW_INC = .1
PW_START = 0
PW_END = 1.0
PWS = np.round(np.arange(PW_START, PW_END, PW_INC), 2)

# Define ranges for varying bandwidth
BW_DEF = 1
BW_INC = .2
BW_START = .2
BW_END = 4
BWS = np.round(np.arange(BW_START, BW_END, BW_INC), 2)

# Define ranges for varying aperiodic exponents
EXP_DEF = 1
EXP_START = 0
EXP_END = 2.5
EXP_INC = .25
EXPS = np.round(np.arange(EXP_START, EXP_END, EXP_INC), 2)

# Define ranges for varying offset
OFF_DEF = 0
OFF_START = 0
OFF_END = 2.5
OFF_INC = .25
OFFS = np.round(np.arange(OFF_START, OFF_END, OFF_INC), 2)

# Define ranges for varying rotation frequencies
ROT_FREQS = [1, 30]
ROT_INC = 1
ROT_OSC = [10, .5, .5]
ROTS = np.round(np.arange(ROT_FREQS[0], ROT_FREQS[1], ROT_INC), 2)

# Define ranges for the delta of exponent changes, for exponent rotations
DEL_RANGE = [0, 3]
DEL_INC = .1
DELS = np.round(np.arange(DEL_RANGE[0], DEL_RANGE[1], DEL_INC), 2)

#######################################
#### COLLECT PARAMETER DEFINITIONS ####
#######################################

# Collect together periodic definitions for param iter
DEF_PARAMITER = [CF_LOW_DEF, PW_DEF, BW_DEF, CF_HIGH_DEF, PW_DEF, BW_DEF]

# Collect all parameter ranges together
PARAMS = {
    "Low_CF" : CFS_LOW,
    "High_CF": CFS_HIGH,
    "Low_PW" : PWS,
    "High_PW" : PWS,
    "Low_BW" : BWS,
    "High_BW" : BWS,
    "EXP" : EXPS,
    "OFF" : OFFS
    }

# Collect together stepper parameters
STEPPERS = {
    "Low_CF" : (LOW_BAND[0], LOW_BAND[1], CF_INC),
    "High_CF" : (HIGH_BAND[0], HIGH_BAND[1], CF_INC),
    "Low_PW" : (PW_START, PW_END, PW_INC),
    "High_PW" : (PW_START, PW_END, PW_INC),
    "Low_BW" : (BW_START, BW_END, BW_INC),
    "High_BW" : (BW_START, BW_END, BW_INC),
    "EXP" : (EXP_START, EXP_END, EXP_INC),
    "OFF" : (OFF_START, OFF_END, OFF_INC)
    }
