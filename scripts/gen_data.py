"""This file simulates power spectra which one parameter varying."""

import numpy as np

from fooof.sim import *

import sys
sys.path.append('../bratios')
from settings import *
from paths import DATA_PATHS as dp

###################################################################################################
###################################################################################################

def main():

    #################### Center Frequency ####################

    # Theta Band
    cf_theta_step = Stepper(THETA_BAND[0], THETA_BAND[1], CF_INC)
    cf_iter_theta = param_iter([cf_theta_step, PW_DEF, BW_DEF])
    cf_theta_fs, cf_theta_ps, cf_theta_syns = \
        gen_group_power_spectra(len(cf_theta_step), FREQ_RANGE, AP_DEF, cf_iter_theta)
    cf_theta_save = [cf_theta_ps, cf_theta_syns]
    cf_theta_save_final = np.empty(len(cf_theta_save), dtype=object)
    cf_theta_save_final[:] = cf_theta_save
    np.save(dp.make_file_path(dp.sims_single, 'cf_theta'), cf_theta_save_final)

    # Alpha Band
    cf_alpha_step = Stepper(ALPHA_BAND[0], ALPHA_BAND[1], CF_INC)
    cf_iter_alpha = param_iter([cf_alpha_step, PW_DEF, BW_DEF])
    cf_alpha_fs, cf_alpha_ps, cf_alpha_syns = \
        gen_group_power_spectra(len(cf_alpha_step), FREQ_RANGE, AP_DEF, cf_iter_alpha)
    cf_alpha_save = [cf_alpha_ps, cf_alpha_syns]
    cf_alpha_save_final = np.empty(len(cf_alpha_save), dtype=object)
    cf_alpha_save_final[:] = cf_alpha_save
    np.save(dp.make_file_path(dp.sims_single, 'cf_alpha'), cf_alpha_save_final)

    # Beta Band
    cf_beta_step = Stepper(BETA_BAND[0], BETA_BAND[1], CF_INC)
    cf_iter_beta = param_iter([cf_beta_step, PW_DEF, BW_DEF])
    cf_beta_fs, cf_beta_ps, cf_beta_syns = \
        gen_group_power_spectra(len(cf_beta_step), FREQ_RANGE, AP_DEF, cf_iter_beta)
    cf_beta_save = [cf_beta_ps, cf_beta_syns]
    cf_beta_save_final = np.empty(len(cf_beta_save), dtype=object)
    cf_beta_save_final[:] = cf_beta_save
    np.save(dp.make_file_path(dp.sims_single, 'cf_beta'), cf_beta_save_final)


    #################### Power ####################

    # Theta Band
    pw_theta_step = Stepper(0, PW_END, PW_INC)
    pw_iter_theta = param_iter([np.mean(THETA_BAND), pw_theta_step, BW_DEF])
    pw_theta_fs, pw_theta_ps, pw_theta_syns = \
        gen_group_power_spectra(len(pw_theta_step), FREQ_RANGE, AP_DEF, pw_iter_theta)
    pw_theta_save = [pw_theta_ps, pw_theta_syns]
    pw_theta_save_final = np.empty(len(pw_theta_save), dtype=object)
    pw_theta_save_final[:] = pw_theta_save
    np.save(dp.make_file_path(dp.sims_single, 'pw_theta'), pw_theta_save_final)

    # Alpha Band
    pw_alpha_step = Stepper(0, PW_END, PW_INC)
    pw_iter_alpha = param_iter([np.mean(ALPHA_BAND), pw_alpha_step, BW_DEF])
    pw_alpha_fs, pw_alpha_ps, pw_alpha_syns = \
        gen_group_power_spectra(len(pw_alpha_step), FREQ_RANGE, AP_DEF, pw_iter_alpha)
    pw_alpha_save = [pw_alpha_ps, pw_alpha_syns]
    pw_alpha_save_final = np.empty(len(pw_alpha_save), dtype=object)
    pw_alpha_save_final[:] = pw_alpha_save
    np.save(dp.make_file_path(dp.sims_single, 'pw_alpha'), pw_alpha_save_final)

    # Off Band
    pw_beta_step = Stepper(0, PW_END, PW_INC)
    pw_iter_beta = param_iter([np.mean(BETA_BAND), pw_beta_step, BW_DEF])
    pw_beta_fs, pw_beta_ps, pw_beta_syns = \
        gen_group_power_spectra(len(pw_beta_step), FREQ_RANGE, AP_DEF, pw_iter_beta)
    pw_beta_save = [pw_beta_ps, pw_beta_syns]
    pw_beta_save_final = np.empty(len(pw_beta_save), dtype=object)
    pw_beta_save_final[:] = pw_beta_save
    np.save(dp.make_file_path(dp.sims_single, 'pw_beta'), pw_beta_save_final)


    ##################### Band Width ####################

    # Theta Band
    bw_theta_step = Stepper(.5, BW_END, BW_INC)
    bw_iter_theta = param_iter([np.mean(THETA_BAND), PW_DEF, bw_theta_step])
    bw_theta_fs, bw_theta_ps, bw_theta_syns = \
        gen_group_power_spectra(len(bw_theta_step), FREQ_RANGE, AP_DEF, bw_iter_theta)
    bw_theta_save = [bw_theta_ps, bw_theta_syns]
    bw_theta_save_final = np.empty(len(bw_theta_save),dtype=object)
    bw_theta_save_final[:] = bw_theta_save
    np.save(dp.make_file_path(dp.sims_single, 'bw_theta'), bw_theta_save_final)

    # Alpha Band
    bw_alpha_step = Stepper(.5, BW_END, BW_INC)
    bw_iter_alpha = param_iter([np.mean(ALPHA_BAND), PW_DEF, bw_alpha_step])
    bw_alpha_fs, bw_alpha_ps, bw_alpha_syns = \
        gen_group_power_spectra(len(bw_alpha_step), FREQ_RANGE, AP_DEF, bw_iter_alpha)
    bw_alpha_save = [bw_alpha_ps, bw_alpha_syns]
    bw_alpha_save_final = np.empty(len(bw_alpha_save), dtype=object)
    bw_alpha_save_final[:] = bw_alpha_save
    np.save(dp.make_file_path(dp.sims_single, 'bw_alpha'), bw_alpha_save_final)

    # Beta Band
    bw_beta_step = Stepper(.5, BW_END, BW_INC)
    bw_iter_beta = param_iter([np.mean(BETA_BAND), PW_DEF, bw_beta_step])
    bw_beta_fs, bw_beta_ps, bw_beta_syns = \
        gen_group_power_spectra(len(bw_beta_step), FREQ_RANGE, AP_DEF, bw_iter_beta)
    bw_beta_save = [bw_beta_ps, bw_beta_syns]
    bw_beta_save_final = np.empty(len(bw_beta_save), dtype=object)
    bw_beta_save_final[:] = bw_beta_save
    np.save(dp.make_file_path(dp.sims_single, 'bw_beta'), bw_beta_save_final)

    #################### Exponent ####################

    exp_step = Stepper(EXP_START, EXP_END, EXP_INC)
    exp_iter = param_iter([0, exp_step])
    exp_fs, exp_ps, exp_syns = \
        gen_group_power_spectra(len(exp_step), FREQ_RANGE, exp_iter, [])
    exp_save = [exp_ps, exp_syns]
    exp_save_final = np.empty(len(exp_save), dtype=object)
    exp_save_final[:] = exp_save
    np.save(dp.make_file_path(dp.sims_single, 'exp_data'), exp_save_final)


    #################### Offset ####################

    off_step = Stepper(OFF_START, OFF_END, OFF_INC)
    off_iter = param_iter([off_step, 0])
    off_fs, off_ps, off_syns = \
        gen_group_power_spectra(len(off_step), FREQ_RANGE, off_iter, [], nlvs=0)
    off_save = [off_ps, off_syns]
    off_save_final = np.empty(len(off_save), dtype=object)
    off_save_final[:] = off_save
    np.save(dp.make_file_path(dp.sims_single, 'offset_data'), off_save_final)


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
#     np.save(dp.make_file_path(dp.sims_single, 'rot_data'), rot_save)


    #################### No Oscillations - 1/f changes ####################

    f_step = Stepper(EXP_START, EXP_END, EXP_INC)
    f_iter = param_iter([OFF_DEF, f_step])
    f_fs, f_ps, f_syns = \
        gen_group_power_spectra(len(f_step), FREQ_RANGE, f_iter, [], nlvs=0)
    f_save = [f_ps, f_syns]
    f_save_final = np.empty(len(f_save), dtype=object)
    f_save_final[:] = f_save
    np.save(dp.make_file_path(dp.sims_single, '1f_data'), f_save_final)


    #################### Shifting Alpha ####################
    a_step = Stepper(ALPHA_BAND[0], ALPHA_BAND[1], CF_INC)
    a_iter = param_iter([ a_step, PW_DEF, BW_DEF, CF_LOW_DEF, PW_DEF, BW_DEF, CF_HIGH_DEF, PW_DEF, BW_DEF])
    a_fs, a_ps, a_syns = \
        gen_group_power_spectra(len(a_step), FREQ_RANGE, AP_DEF, a_iter, nlvs=0)
    a_save = [a_ps, a_syns]
    a_save_final = np.empty(len(a_save), dtype=object)
    a_save_final[:] = a_save
    np.save(dp.make_file_path(dp.sims_single, 'shifting_alpha'), a_save_final)


if __name__ == "__main__":
    main()
