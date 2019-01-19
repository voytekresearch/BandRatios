import numpy as np

from fooof import FOOOFGroup
from fooof.synth import *
###############################################
########## Settings ###########################
###############################################

FREQ_RANGE = [1,50]
LOW_BAND = [4,8]
HIGH_BAND = [15,25]
DEF_AMP = 1
DEF_BW = 1
DEF_BG = [0,1]
DEF_CF_LOW = np.mean(LOW_BAND)
DEF_CF_HIGH = np.mean(HIGH_BAND)

START_SLOPE = .25
END_SLOPE = 3
SLOPE_INC = .25
SLOPE_PATH = './dat/slope_data'

CF_STATIONARY = 'low'
CF_INC = .1
CF_TRIALS = 50
CF_PATH_LOW = './dat/cf_data_low'
CF_PATH_HIGH = './dat/cf_data_high'

AMP_STATIONARY = 'low'
AMP_INC = .1
END_AMP = 1.5
AMP_TRIALS = 50
AMP_PATH_LOW = './dat/amp_data_low'
AMP_PATH_HIGH = './dat/amp_data_high'

BW_STATIONARY = 'low'
BW_INC = .1
END_BW = 2
BW_TRIALS = 50
BW_PATH_LOW = './dat/bw_data_low'
BW_PATH_HIGH = './dat/bw_data_high'

START_OFF = 0
END_OFF = 2.5
OFF_INC = .25
OFF_PATH = './dat/offset_data'

ROT_START = -1.5
ROT_END = 1.5
ROT_INC = .2
ROT_FREQ = 20
ROT_PATH = './dat/rot_data'

##################################################

def main():

    # Generate varying Center Frequency Data
    # Low Band
    cf_low_step = Stepper(LOW_BAND[0], LOW_BAND[1], CF_INC)
    cf_iter_low = param_iter([cf_low_step,DEF_AMP,DEF_BW])
    cf_low_fs, cf_low_ps, cf_low_syns = gen_group_power_spectra(len(cf_low_step),FREQ_RANGE, DEF_BG, cf_iter_low)
    cf_low_save = [cf_low_fs,cf_low_ps,cf_low_syns]
    np.save(CF_PATH_LOW,cf_low_save)


    # High Band
    cf_high_step = Stepper(HIGH_BAND[0],HIGH_BAND[1],CF_INC)
    cf_iter_high = param_iter([cf_high_step,DEF_AMP,DEF_BW])
    cf_high_fs, cf_high_ps, cf_high_syns = gen_group_power_spectra(len(cf_high_step),FREQ_RANGE, DEF_BG, cf_iter_high)
    cf_high_save = [cf_high_fs,cf_high_ps,cf_high_syns]
    np.save(CF_PATH_HIGH,cf_high_save)





    # Generate varying Amplitude Data
    # Low Band
    amp_low_step = Stepper(0,END_AMP,AMP_INC)
    amp_iter_low = param_iter([DEF_CF_LOW, amp_low_step, DEF_BW])
    amp_low_fs, amp_low_ps, amp_low_syns = gen_group_power_spectra(len(amp_low_step), FREQ_RANGE, DEF_BG, amp_iter_low)
    amp_low_save = [amp_low_fs, amp_low_ps, amp_low_syns]
    np.save(AMP_PATH_LOW, amp_low_save)

    # High Band
    amp_high_step = Stepper(0,END_AMP,AMP_INC)
    amp_iter_high = param_iter([DEF_CF_HIGH, amp_high_step, DEF_BW])
    amp_high_fs, amp_high_ps, amp_high_syns = gen_group_power_spectra(len(amp_high_step), FREQ_RANGE, DEF_BG, amp_iter_high)
    amp_high_save = [amp_high_fs,amp_high_ps,amp_high_syns]
    np.save(AMP_PATH_HIGH, amp_high_save)





    # Generate varying BandWidth data
    # Low Band
    bw_low_step = Stepper(.5, END_BW, BW_INC)
    bw_iter_low = param_iter([DEF_CF_LOW, DEF_AMP, bw_low_step])
    bw_low_fs, bw_low_ps, bw_low_syns = gen_group_power_spectra(len(bw_low_step), FREQ_RANGE, DEF_BG, bw_iter_low)
    bw_low_save = [bw_low_fs,bw_low_ps,bw_low_syns]
    np.save(BW_PATH_LOW, bw_low_save)


    # High Band
    bw_high_step = Stepper(.5, END_BW, BW_INC)
    bw_iter_high = param_iter([DEF_CF_HIGH, DEF_AMP, bw_high_step])
    bw_high_fs, bw_high_ps, bw_high_syns = gen_group_power_spectra(len(bw_high_step), FREQ_RANGE, DEF_BG, bw_iter_high)
    bw_high_save = [bw_high_fs,bw_high_ps,bw_high_syns]
    np.save(BW_PATH_HIGH, bw_high_save)

    # Generate varying slope data
    sl_step = Stepper(START_SLOPE, END_SLOPE, SLOPE_INC)
    sl_iter = param_iter([0, sl_step])
    sl_fs, sl_ps, sl_syns = gen_group_power_spectra(len(sl_step), FREQ_RANGE,sl_iter,[])
    sl_save = [sl_fs, sl_ps, sl_syns]
    np.save(SLOPE_PATH, sl_save)
    
    
    
    # Generate varying offset data #TODO
    off_step = Stepper(START_OFF, END_OFF, OFF_INC)
    off_iter = param_iter([0, off_step])
    off_fs, off_ps, off_syns = gen_group_power_spectra(len(off_step), FREQ_RANGE,off_iter,[])
    off_save = [off_fs, off_ps, off_syns]
    np.save(OFF_PATH, off_save)
    
    # Generate varying rotation data
    # rot is not a parameter in fooof 
    # Generate freqs and powers
    rot_save = []
    vals = []
    freqs, ps, _ = gen_group_power_spectra(50,[1,50], [0,1],[] )
    for curr_ps in ps:
        curr_ps_array = []
        rot_step = Stepper(ROT_START, ROT_END, ROT_INC)

        for delta in rot_step:
            r_ps = rotate_spectrum(freqs, curr_ps, delta, ROT_FREQ)
            curr_ps_array.append(r_ps)
        vals.append(curr_ps_array)
    rot_save.append( (freqs,vals) )
    np.save(ROT_PATH, rot_save) 
    
if __name__ == "__main__":
    main()
