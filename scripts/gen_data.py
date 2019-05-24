"""This file simulates power spectral data where parameters are varied in isolation"""
import numpy as np

from fooof.synth import *

from settings import *


def main():

    #################### Center Frequency ####################

    # Low Band
    cf_low_step = Stepper(LOW_BAND[0], LOW_BAND[1], CF_LOW_INC)
    cf_iter_low = param_iter([cf_low_step, AMP_DEF, BW_DEF])
    cf_low_fs, cf_low_ps, cf_low_syns = gen_group_power_spectra(len(cf_low_step), FREQ_RANGE, AP_DEF, cf_iter_low)
    cf_low_save = [cf_low_ps, cf_low_syns]
    np.save(CF_PATH_LOW, cf_low_save)

    # High Band
    cf_high_step = Stepper(HIGH_BAND[0], HIGH_BAND[1], CF_HIGH_INC)
    cf_iter_high = param_iter([cf_high_step, AMP_DEF, BW_DEF])
    cf_high_fs, cf_high_ps, cf_high_syns = gen_group_power_spectra(len(cf_high_step), FREQ_RANGE, AP_DEF, cf_iter_high)
    cf_high_save = [cf_high_ps, cf_high_syns]
    np.save(CF_PATH_HIGH, cf_high_save)

    
    #################### Amplitude ####################
    
    # Low Band
    amp_low_step = Stepper(0, AMP_END, AMP_INC)
    amp_iter_low = param_iter([CF_LOW_DEF, amp_low_step, BW_DEF])
    amp_low_fs, amp_low_ps, amp_low_syns = gen_group_power_spectra(len(amp_low_step), FREQ_RANGE, AP_DEF, amp_iter_low)
    amp_low_save = [amp_low_ps, amp_low_syns]
    np.save(AMP_PATH_LOW, amp_low_save)

    # High Band
    amp_high_step = Stepper(0, AMP_END, AMP_INC)
    amp_iter_high = param_iter([CF_HIGH_DEF, amp_high_step, BW_DEF])
    amp_high_fs, amp_high_ps, amp_high_syns = gen_group_power_spectra(len(amp_high_step), FREQ_RANGE, AP_DEF, amp_iter_high)
    amp_high_save = [amp_high_ps, amp_high_syns]
    np.save(AMP_PATH_HIGH, amp_high_save)


    ##################### Band Width ####################

    # Low Band
    bw_low_step = Stepper(.5, BW_END, BW_INC)
    bw_iter_low = param_iter([CF_LOW_DEF, AMP_DEF, bw_low_step])
    bw_low_fs, bw_low_ps, bw_low_syns = gen_group_power_spectra(len(bw_low_step), FREQ_RANGE, AP_DEF, bw_iter_low)
    bw_low_save = [bw_low_ps, bw_low_syns]
    np.save(BW_PATH_LOW, bw_low_save)

    # High Band
    bw_high_step = Stepper(.5, BW_END, BW_INC)
    bw_iter_high = param_iter([CF_HIGH_DEF, AMP_DEF, bw_high_step])
    bw_high_fs, bw_high_ps, bw_high_syns = gen_group_power_spectra(len(bw_high_step), FREQ_RANGE, AP_DEF, bw_iter_high)
    bw_high_save = [bw_high_ps, bw_high_syns]
    np.save(BW_PATH_HIGH, bw_high_save)


    #################### Aperiodic component ####################

    apc_step = Stepper(APC_START, APC_END, APC_INC)
    apc_iter = param_iter([0, apc_step])
    apc_fs, apc_ps, apc_syns = gen_group_power_spectra(len(apc_step), FREQ_RANGE, apc_iter, [])
    apc_save = [apc_ps, apc_syns]
    np.save(APC_PATH, apc_save)


    #################### Offset ####################

    off_step = Stepper(OFF_START, OFF_END, OFF_INC)
    off_iter = param_iter([off_step, 0])
    off_fs, off_ps, off_syns = gen_group_power_spectra(len(off_step), FREQ_RANGE, off_iter, [], nlvs=0)
    off_save = [off_ps, off_syns]
    np.save(OFF_PATH, off_save)


    #################### Rotation ####################

    rot_save = []
    vals = []
    freqs, ps, _ = gen_group_power_spectra(50, [1, 50], [0, 1], [])
    for curr_ps in ps:
        curr_ps_array = []
        rot_step = Stepper(ROT_FREQS[0], ROT_FREQS[1], ROT_INC)

        #TODO change rot freq
        for delta in rot_step:
            r_ps = rotate_spectrum(freqs, curr_ps, delta, 20)
            curr_ps_array.append(r_ps)
        vals.append(curr_ps_array)
    rot_save.append((freqs, vals))
    np.save(ROT_PATH, rot_save)

    
    #################### No Oscillations - 1/f changes ####################
    
    f_step = Stepper(APC_START, APC_END, APC_INC)
    f_iter = param_iter([OFF_DEF, f_step])
    f_fs, f_ps, f_syns = gen_group_power_spectra(len(f_step), FREQ_RANGE, f_iter, [], nlvs=0)
    f_save = [f_fs, f_ps, f_syns]
    np.save(F_PATH, f_save)
    
if __name__ == "__main__":
    main()
