import numpy as np

from fooof import FOOOFGroup
from fooof.synth import *
###############################################
########## Settings ###########################
###############################################

FREQ_RANGE = [1, 50]

LOW_BAND = [4,8]
HIGH_BAND = [15,25]

START_SLOPE = .25
END_SLOPE = 3
SLOPE_INC = .25

AMP_STATIONARY = 'low'
AMP_INC = .1
END_AMP = 1.5
DEF_AMP = .75

CF_LOW = np.mean(LOW_BAND)
CF_HIGH = np.mean(HIGH_BAND)
CF_INC = .1


DEF_BW = 1
BW_INIT = .25
BW_INC = .25
BW_MAX = 1.5

DEF_SL = 1

SL_AMP_LOW_PATH = './dat/sl_amp_data_low'
SL_AMP_HIGH_PATH= './dat/sl_amp_data_high'

CF_BW_LOW_PATH = './dat/cf_bw_data_low'
CF_BW_HIGH_PATH= './dat/cf_bw_data_high'

def main():
    
    ############## Amplitude and Slope ###########################
    
    # This block generates PSDs where amplitude and slope change for low band
    data = []
    slope_step = Stepper(START_SLOPE, END_SLOPE, SLOPE_INC)
    for sl in slope_step:
        
        # Low band sweeps through amplitude range
        amp_low_step = Stepper(0, END_AMP, AMP_INC)
        amp_iter_low = param_iter( [CF_LOW, amp_low_step, DEF_BW, CF_HIGH, DEF_AMP, DEF_BW])
        amp_low_fs, amp_low_ps, amp_low_syns = gen_group_power_spectra( len(amp_low_step), FREQ_RANGE, [0, sl], amp_iter_low)
        data.append(np.array([sl, amp_low_fs, amp_low_ps, amp_low_syns], dtype=object))
        
    np.save(SL_AMP_LOW_PATH, data)
        
        
    # This block generates PSDs where amplitude and slope change for high band  
    data = []
    slope_step = Stepper(START_SLOPE, END_SLOPE, SLOPE_INC)
    for sl in slope_step:
        
        # high band sweeps through amplitude range
        amp_high_step = Stepper(0, END_AMP, AMP_INC)
        amp_iter_high = param_iter( [CF_LOW, DEF_AMP, DEF_BW, CF_HIGH, amp_high_step, DEF_BW])
        amp_high_fs, amp_high_ps, amp_high_syns = gen_group_power_spectra( len(amp_high_step), FREQ_RANGE, [0, sl], amp_iter_high)
        data.append(np.array([sl, amp_high_fs, amp_high_ps, amp_high_syns], dtype=object))
        
    np.save(SL_AMP_HIGH_PATH, data)
        
        
    ################# Center Frequency and BandWidth ####################
    # This block generates PSDs where center frequency changes for low band | High band is stationary
    # cf and bw move both in the same band
    
    data = []
    cf_low_step = Stepper( LOW_BAND[0], LOW_BAND[1], CF_INC)
    for cf in cf_low_step:
        
        bw_step = Stepper(BW_INIT, BW_MAX, BW_INC)
        bw_iter = param_iter( [cf, DEF_AMP, bw_step, CF_HIGH, DEF_AMP, DEF_BW])
        bw_fs, bw_ps, bw_syns = gen_group_power_spectra( len(bw_step), FREQ_RANGE, [0, DEF_SL], bw_iter)
        data.append(np.array([cf, bw_fs, bw_ps, bw_syns], dtype=object)) 
        
    np.save(CF_BW_LOW_PATH, data)
    
    data = []
    cf_high_step = Stepper( HIGH_BAND[0], HIGH_BAND[1], CF_INC)
    for cf in cf_high_step:
        
        bw_step = Stepper(BW_INIT, BW_MAX, BW_INC)
        bw_iter = param_iter( [cf, DEF_AMP, bw_step, CF_HIGH, DEF_AMP, DEF_BW])
        bw_fs, bw_ps, bw_syns = gen_group_power_spectra( len(bw_step), FREQ_RANGE, [0, DEF_SL], bw_iter)
        data.append(np.array([cf, bw_fs, bw_ps, bw_syns], dtype=object)) 
    
    np.save(CF_BW_HIGH_PATH, data) 
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    