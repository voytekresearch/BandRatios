"""This file simulates power spectral data where two parameters are varied in isolation"""
import numpy as np

from fooof import FOOOFGroup
from fooof.synth import *

from settings import *

def main():

    ############## Amplitude and Slope ###########################

    # This block generates PSDs where amplitude and slope change for low band
    data = []
    slope_step = Stepper(APC_START, APC_END, APC_INC)
    for sl in slope_step:

        # Low band sweeps through amplitude range
        amp_low_step = Stepper(0, AMP_END, AMP_INC)
        amp_iter_low = param_iter([CF_LOW_DEF, amp_low_step, BW_DEF, CF_HIGH_DEF, AMP_DEF, BW_DEF])
        amp_low_fs, amp_low_ps, amp_low_syns = gen_group_power_spectra(len(amp_low_step), FREQ_RANGE, [0, sl], amp_iter_low)
        data.append(np.array([sl, amp_low_fs, amp_low_ps, amp_low_syns], dtype=object))

    np.save(APC_AMP_LOW_PATH, data)


    # This block generates PSDs where amplitude and slope change for high band
    data = []
    slope_step = Stepper(APC_START, APC_END, APC_INC)
    for sl in slope_step:

        # high band sweeps through amplitude range
        amp_high_step = Stepper(0, AMP_END, AMP_INC)
        amp_iter_high = param_iter([CF_LOW_DEF, AMP_DEF, BW_DEF, CF_HIGH_DEF, amp_high_step, BW_DEF])
        amp_high_fs, amp_high_ps, amp_high_syns = gen_group_power_spectra(len(amp_high_step), FREQ_RANGE, [0, sl], amp_iter_high)
        data.append(np.array([sl, amp_high_fs, amp_high_ps, amp_high_syns], dtype=object))

    np.save(APC_AMP_HIGH_PATH, data)


    ################# Center Frequency and BandWidth ####################
    
    # This block generates PSDs where center frequency changes for
    # low band | High band is stationary cf and bw move both in the same band

    data = []
    cf_low_step = Stepper(LOW_BAND[0], LOW_BAND[1], CF_LOW_INC)
   
    for cf in cf_low_step:

        bw_step = Stepper(BW_START, BW_END, BW_INC)
        bw_iter = param_iter([cf, AMP_DEF, bw_step, CF_HIGH_DEF, AMP_DEF, BW_DEF])
        bw_fs, bw_ps, bw_syns = gen_group_power_spectra(len(bw_step), FREQ_RANGE, [0, APC_DEF], bw_iter)
        data.append(np.array([cf, bw_fs, bw_ps, bw_syns], dtype=object))

    np.save(CF_BW_LOW_PATH, data)

    data = []
    cf_high_step = Stepper(HIGH_BAND[0], HIGH_BAND[1], CF_HIGH_INC)
    for cf in cf_high_step:

        bw_step = Stepper(BW_START, BW_END, BW_INC)
        bw_iter = param_iter([cf, AMP_DEF, bw_step, CF_HIGH_DEF, AMP_DEF, BW_DEF])
        bw_fs, bw_ps, bw_syns = gen_group_power_spectra(len(bw_step), FREQ_RANGE, [0, APC_DEF], bw_iter)
        data.append(np.array([cf, bw_fs, bw_ps, bw_syns], dtype=object))

    np.save(CF_BW_HIGH_PATH, data)

    ##################### Rotation frequency and delta_f #################
    
    # This block generates PSDS where rotation occurs at varying varying frequencys at varying rotational amounts
    
    fs, ps = gen_power_spectrum(FREQ_RANGE, AP_DEF, ROT_OSC)
    data = []
    rot_freq_step = Stepper(ROT_FREQS[0], ROT_FREQS[1], ROT_INC)

    for rf in rot_freq_step:
        deltas = []
        delta_step = Stepper(DEL_RANGE[0], DEL_RANGE[1], DEL_INC)

        for delta in delta_step:
            curr_rot_ps = rotate_spectrum(fs, ps, delta, rf)
            deltas.append(curr_rot_ps)
            
        data.append(np.array([rf, fs, deltas], dtype=object))

    np.save(ROT_DEL_PATH, data)

    
    
if __name__ == "__main__":
    main()
