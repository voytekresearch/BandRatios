"""This file simulates power spectral data where two parameters are varied in isolation"""
import numpy as np

from fooof import FOOOFGroup
from fooof.synth import *

from settings import *

def main():

    ############## Power and Exponent ###########################

    fs = gen_freqs(FREQ_RANGE, FREQ_RES)

    # This block generates PSDs where amplitude and apc change for low band
    # [Amplitude, apcs, Powers]
    output = np.zeros(shape=(len(APCS), len(AMPS), len(fs)))
    apc_step = Stepper(APC_START, APC_END, APC_INC)
    for sl_ind, sl_val in enumerate(apc_step):

        # Low band sweeps through amplitude range
        amp_low_step = Stepper(AMP_START, AMP_END, AMP_INC)
        amp_iter_low = param_iter([CF_LOW_DEF, amp_low_step, BW_DEF, CF_HIGH_DEF, AMP_DEF, BW_DEF])

        for amp_ind, amp_val in enumerate(amp_iter_low):        
            fs, amp_low_ps = gen_power_spectrum(FREQ_RANGE, [0, sl_val], amp_val)
            output[sl_ind, amp_ind, :] = amp_low_ps

    np.save(APC_AMP_LOW_PATH, output)

    ###############################################################
    
    output = np.zeros(shape=(len(APCS), len(AMPS), len(fs)))
    apc_step = Stepper(APC_START, APC_END, APC_INC)
    for sl_ind, sl_val in enumerate(apc_step):

        # High band sweeps through amplitude range
        amp_high_step = Stepper(AMP_START, AMP_END, AMP_INC)
        amp_iter_high = param_iter([CF_LOW_DEF, AMP_DEF, BW_DEF, CF_HIGH_DEF, amp_high_step, BW_DEF])

        for amp_ind, amp_val in enumerate(amp_iter_high):        
            fs, amp_high_ps = gen_power_spectrum(FREQ_RANGE, [0, sl_val], amp_val)
            output[sl_ind, amp_ind, :] = amp_high_ps

    np.save(APC_AMP_HIGH_PATH, output)
    ################# Center Frequency and BandWidth ####################
    
    # This block generates PSDs where center frequency changes for
    # low band | High band is stationary cf and bw move both in the same band

    output = np.zeros(shape=(len(CFS_LOW), len(BWS), len(fs)))
    cf_low_step = Stepper(LOW_BAND[0], LOW_BAND[1], CF_LOW_INC)

    for cf_ind, cf_val in enumerate(cf_low_step):

        bw_step = Stepper(BW_START, BW_END, BW_INC)
        params = [cf_val, AMP_DEF, bw_step, CF_HIGH_DEF, AMP_DEF, BW_DEF]
        for bw_ind, bw_val in enumerate(bw_step):
            curr_osc = params
            curr_osc[2] = bw_val
            fs, bw_ps, = gen_power_spectrum(FREQ_RANGE, [0, APC_DEF], curr_osc)

            output[cf_ind, bw_ind, :] = bw_ps

    np.save(CF_BW_LOW_PATH, output)
    
    
    output = np.zeros(shape=(len(CFS_HIGH), len(BWS), len(fs)))
    cf_high_step = Stepper(HIGH_BAND[0], HIGH_BAND[1], CF_HIGH_INC)

    for cf_ind, cf_val in enumerate(cf_high_step):

        bw_step = Stepper(BW_START, BW_END, BW_INC)
        params = [CF_LOW_DEF, AMP_DEF, BW_DEF, cf_val, AMP_DEF, bw_step]
        for bw_ind, bw_val in enumerate(bw_step):
            curr_osc = params
            curr_osc[5] = bw_val
            fs, bw_ps, = gen_power_spectrum(FREQ_RANGE, [0, APC_DEF], curr_osc)

            output[cf_ind, bw_ind, :] = bw_ps

    np.save(CF_BW_HIGH_PATH, output)

    ##################### Rotation frequency and delta_f #################
    
    # This block generates PSDS where rotation occurs at varying varying frequencys at varying rotational amounts
    # [rotation_freqs, deltas, powers]
    fs, ps = gen_power_spectrum(FREQ_RANGE, AP_DEF, ROT_OSC)
    output = np.zeros(shape=(len(ROTS), len(DELS), len(fs)))
                      
    rot_freq_step = Stepper(ROT_FREQS[0], ROT_FREQS[1], ROT_INC)

    for rot_ind, rot_val in enumerate(rot_freq_step):
        delta_step = Stepper(DEL_RANGE[0], DEL_RANGE[1], DEL_INC)
        for del_ind, del_val, in enumerate(delta_step):
            output[rot_ind, del_ind, :] = rotate_spectrum(fs, ps, del_val, rot_val)

    np.save(ROT_DEL_PATH, output)

    
    
if __name__ == "__main__":
    main()
