"""This file simulates power spectra which one parameter varying."""

import numpy as np

from fooof.sim import *

import sys
sys.path.append('../bratios')
from settings import *

###################################################################################################
###################################################################################################

def main():

    #################### Center Frequency ####################

    # Low Band
    cf_low_step = Stepper(LOW_BAND[0], LOW_BAND[1], CF_LOW_INC)
    cf_iter_low = param_iter([cf_low_step, PW_DEF, BW_DEF])
    cf_low_fs, cf_low_ps, cf_low_syns = gen_group_power_spectra(len(cf_low_step), FREQ_RANGE, AP_DEF, cf_iter_low)
    cf_low_save = [cf_low_ps, cf_low_syns]
    cf_low_save_final = np.empty(len(cf_low_save),dtype=object)
    cf_low_save_final[:] = cf_low_save
    np.save(CF_PATH_LOW, cf_low_save_final)

    # High Band
    cf_high_step = Stepper(HIGH_BAND[0], HIGH_BAND[1], CF_HIGH_INC)
    cf_iter_high = param_iter([cf_high_step, PW_DEF, BW_DEF])
    cf_high_fs, cf_high_ps, cf_high_syns = gen_group_power_spectra(len(cf_high_step), FREQ_RANGE, AP_DEF, cf_iter_high)
    cf_high_save = [cf_high_ps, cf_high_syns]
    cf_high_save_final = np.empty(len(cf_high_save),dtype=object)
    cf_high_save_final[:] = cf_high_save
    np.save(CF_PATH_HIGH, cf_high_save_final)


    #################### Power ####################

    # Low Band
    pw_low_step = Stepper(0, PW_END, PW_INC)
    pw_iter_low = param_iter([CF_LOW_DEF, pw_low_step, BW_DEF])
    pw_low_fs, pw_low_ps, pw_low_syns = gen_group_power_spectra(len(pw_low_step), FREQ_RANGE, AP_DEF, pw_iter_low)
    pw_low_save = [pw_low_ps, pw_low_syns]
    pw_low_save_final = np.empty(len(pw_low_save),dtype=object)
    pw_low_save_final[:] = pw_low_save
    np.save(PW_PATH_LOW, pw_low_save_final)

    # High Band
    pw_high_step = Stepper(0, PW_END, PW_INC)
    pw_iter_high = param_iter([CF_HIGH_DEF, pw_high_step, BW_DEF])
    pw_high_fs, pw_high_ps, pw_high_syns = gen_group_power_spectra(len(pw_high_step), FREQ_RANGE, AP_DEF, pw_iter_high)
    pw_high_save = [pw_high_ps, pw_high_syns]
    pw_high_save_final = np.empty(len(pw_high_save),dtype=object)
    pw_high_save_final[:] = pw_high_save
    np.save(PW_PATH_HIGH, pw_high_save_final)


    ##################### Band Width ####################

    # Low Band
    bw_low_step = Stepper(.5, BW_END, BW_INC)
    bw_iter_low = param_iter([CF_LOW_DEF, PW_DEF, bw_low_step])
    bw_low_fs, bw_low_ps, bw_low_syns = gen_group_power_spectra(len(bw_low_step), FREQ_RANGE, AP_DEF, bw_iter_low)
    bw_low_save = [bw_low_ps, bw_low_syns]
    bw_low_save_final = np.empty(len(bw_low_save),dtype=object)
    bw_low_save_final[:] = bw_low_save
    np.save(BW_PATH_LOW, bw_low_save_final)

    # High Band
    bw_high_step = Stepper(.5, BW_END, BW_INC)
    bw_iter_high = param_iter([CF_HIGH_DEF, PW_DEF, bw_high_step])
    bw_high_fs, bw_high_ps, bw_high_syns = gen_group_power_spectra(len(bw_high_step), FREQ_RANGE, AP_DEF, bw_iter_high)
    bw_high_save = [bw_high_ps, bw_high_syns]
    bw_high_save_final = np.empty(len(bw_high_save),dtype=object)
    bw_high_save_final[:] = bw_high_save
    np.save(BW_PATH_HIGH, bw_high_save_final)


    #################### Exponent ####################

    exp_step = Stepper(EXP_START, EXP_END, EXP_INC)
    exp_iter = param_iter([0, exp_step])
    exp_fs, exp_ps, exp_syns = gen_group_power_spectra(len(exp_step), FREQ_RANGE, exp_iter, [])
    exp_save = [exp_ps, exp_syns]
    exp_save_final = np.empty(len(exp_save),dtype=object)
    exp_save_final[:] = exp_save
    np.save(EXP_PATH, exp_save_final)


    #################### Offset ####################

    off_step = Stepper(OFF_START, OFF_END, OFF_INC)
    off_iter = param_iter([off_step, 0])
    off_fs, off_ps, off_syns = gen_group_power_spectra(len(off_step), FREQ_RANGE, off_iter, [], nlvs=0)
    off_save = [off_ps, off_syns]
    off_save_final = np.empty(len(off_save),dtype=object)
    off_save_final[:] = off_save
    np.save(OFF_PATH, off_save_final)


    #################### Rotation ####################

#     rot_save = []
#     vals = []
#     freqs, ps, _ = gen_group_power_spectra(50, [1, 50], [0, 1], [])
#     for curr_ps in ps:
#         curr_ps_array = []
#         rot_step = Stepper(ROT_FREQS[0], ROT_FREQS[1], ROT_INC)

#         #TODO change rot freq
#         for delta in rot_step:
#             r_ps = rotate_spectrum(freqs, curr_ps, delta, 20)
#             curr_ps_array.append(r_ps)
#         vals.append(curr_ps_array)
#     rot_save.append((freqs, vals))
#     np.save(ROT_PATH, rot_save)


    #################### No Oscillations - 1/f changes ####################

    f_step = Stepper(EXP_START, EXP_END, EXP_INC)
    f_iter = param_iter([OFF_DEF, f_step])
    f_fs, f_ps, f_syns = gen_group_power_spectra(len(f_step), FREQ_RANGE, f_iter, [], nlvs=0)
    f_save = [f_ps, f_syns]
    f_save_final = np.empty(len(f_save),dtype=object)
    f_save_final[:] = f_save
    np.save(F_PATH, f_save_final)


    #################### Shifting Alpha ####################
    a_step = Stepper(ALPHA_BAND[0], ALPHA_BAND[1], CF_LOW_INC)
    a_iter = param_iter([ a_step, PW_DEF, BW_DEF, CF_LOW_DEF, PW_DEF, BW_DEF, CF_HIGH_DEF, PW_DEF, BW_DEF])
    a_fs, a_ps, a_syns = gen_group_power_spectra(len(a_step), FREQ_RANGE, AP_DEF, a_iter, nlvs=0)
    a_save = [a_ps, a_syns]
    a_save_final = np.empty(len(a_save),dtype=object)
    a_save_final[:] = a_save
    np.save(ALPHA_SHIFT_PATH, a_save_final)


if __name__ == "__main__":
    main()
