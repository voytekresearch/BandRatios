"""This file simulates power spectral data where two parameters are varied in isolation"""
import sys
sys.path.append('../bratios')
import numpy as np

from fooof import FOOOFGroup
from fooof.sim import *

from settings import *
from interacting_params_generation import *

def main():
    
    # Aperiodic Periodic
    gen_interacting_aper_per("EXP","Low_CF", '../dat/interacting_param_sims/exp_lowcf_data')
    gen_interacting_aper_per("EXP","High_CF", '../dat/interacting_param_sims/exp_highcf_data')
    gen_interacting_aper_per("EXP","Low_PW", '../dat/interacting_param_sims/exp_lowpw_data')
    gen_interacting_aper_per("EXP","High_PW", '../dat/interacting_param_sims/exp_highpw_data')
    gen_interacting_aper_per("EXP","Low_BW", '../dat/interacting_param_sims/exp_lowbw_data')
    gen_interacting_aper_per("EXP","High_BW", '../dat/interacting_param_sims/exp_highbw_data')

    # Periodic Periodic
    gen_interacting_per_per("Low_CF","High_CF", '../dat/interacting_param_sims/lowcf_highcf_data')
    gen_interacting_per_per("Low_CF","Low_PW", '../dat/interacting_param_sims/lowcf_lowpw_data')
    gen_interacting_per_per("Low_CF","High_PW", '../dat/interacting_param_sims/lowcf_highpw_data')
    gen_interacting_per_per("Low_CF","Low_BW", '../dat/interacting_param_sims/lowcf_lowbw_data')
    gen_interacting_per_per("Low_CF","High_BW", '../dat/interacting_param_sims/lowcf_highbw_data')

    gen_interacting_per_per("High_CF","Low_PW", '../dat/interacting_param_sims/highcf_lowpw_data')
    gen_interacting_per_per("High_CF","High_PW", '../dat/interacting_param_sims/highcf_highpw_data')
    gen_interacting_per_per("High_CF","Low_BW", '../dat/interacting_param_sims/highcf_lowbw_data')
    gen_interacting_per_per("High_CF","High_BW", '../dat/interacting_param_sims/highcf_highbw_data')

    gen_interacting_per_per("Low_PW","High_PW", '../dat/interacting_param_sims/lowpw_highpw_data')
    gen_interacting_per_per("Low_PW","Low_BW", '../dat/interacting_param_sims/lowpw_lowbw_data')
    gen_interacting_per_per("Low_PW","High_BW", '../dat/interacting_param_sims/lowpw_highbw_data')

    gen_interacting_per_per("High_PW","Low_BW", '../dat/interacting_param_sims/highpw_lowbw_data')
    gen_interacting_per_per("High_PW","High_BW", '../dat/interacting_param_sims/highpw_highbw_data')

    gen_interacting_per_per("Low_BW","High_BW", '../dat/interacting_param_sims/lowbw_highbw_data')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#     ############## Power and Exponent ###########################

#     fs = gen_freqs(FREQ_RANGE, FREQ_RES)

#     # This block generates PSDs where power and apc change for low band
    
#     output = np.zeros(shape=(len(APCS), len(PWS), len(fs)))
#     apc_step = Stepper(APC_START, APC_END, APC_INC)
#     for sl_ind, sl_val in enumerate(apc_step):

#         # Low band sweeps through power range
#         pw_low_step = Stepper(PW_START, PW_END, PW_INC)
#         pw_iter_low = param_iter([CF_LOW_DEF, pw_low_step, BW_DEF, CF_HIGH_DEF, PW_DEF, BW_DEF])

#         for pw_ind, pw_val in enumerate(pw_iter_low):        
#             fs, pw_low_ps = gen_power_spectrum(FREQ_RANGE, [0, sl_val], pw_val)
#             output[sl_ind, pw_ind, :] = pw_low_ps

#     np.save(APC_PW_LOW_PATH, output)

#     ###############################################################
    
#     output = np.zeros(shape=(len(APCS), len(PWS), len(fs)))
#     apc_step = Stepper(APC_START, APC_END, APC_INC)
#     for sl_ind, sl_val in enumerate(apc_step):

#         # High band sweeps through pwlitude range
#         pw_high_step = Stepper(PW_START, PW_END, PW_INC)
#         pw_iter_high = param_iter([CF_LOW_DEF, PW_DEF, BW_DEF, CF_HIGH_DEF, pw_high_step, BW_DEF])

#         for pw_ind, pw_val in enumerate(pw_iter_high):        
#             fs, pw_high_ps = gen_power_spectrum(FREQ_RANGE, [0, sl_val], pw_val)
#             output[sl_ind, pw_ind, :] = pw_high_ps

#     np.save(APC_PW_HIGH_PATH, output)
#     ################# Center Frequency and BandWidth ####################
    
#     # This block generates PSDs where center frequency changes for
#     # low band | High band is stationary cf and bw move both in the same band

#     output = np.zeros(shape=(len(CFS_LOW), len(BWS), len(fs)))
#     cf_low_step = Stepper(LOW_BAND[0], LOW_BAND[1], CF_LOW_INC)

#     for cf_ind, cf_val in enumerate(cf_low_step):

#         bw_step = Stepper(BW_START, BW_END, BW_INC)
#         params = [cf_val, PW_DEF, bw_step, CF_HIGH_DEF, PW_DEF, BW_DEF]
#         for bw_ind, bw_val in enumerate(bw_step):
#             curr_osc = params
#             curr_osc[2] = bw_val
#             fs, bw_ps, = gen_power_spectrum(FREQ_RANGE, [0, APC_DEF], curr_osc)

#             output[cf_ind, bw_ind, :] = bw_ps

#     np.save(CF_BW_LOW_PATH, output)
    
    
#     output = np.zeros(shape=(len(CFS_HIGH), len(BWS), len(fs)))
#     cf_high_step = Stepper(HIGH_BAND[0], HIGH_BAND[1], CF_HIGH_INC)

#     for cf_ind, cf_val in enumerate(cf_high_step):

#         bw_step = Stepper(BW_START, BW_END, BW_INC)
#         params = [CF_LOW_DEF, PW_DEF, BW_DEF, cf_val, PW_DEF, bw_step]
#         for bw_ind, bw_val in enumerate(bw_step):
#             curr_osc = params
#             curr_osc[5] = bw_val
#             fs, bw_ps, = gen_power_spectrum(FREQ_RANGE, [0, APC_DEF], curr_osc)

#             output[cf_ind, bw_ind, :] = bw_ps

#     np.save(CF_BW_HIGH_PATH, output)

#     ##################### Rotation frequency and delta_f #################
    
#     # This block generates PSDS where rotation occurs at varying varying frequencys at varying rotational amounts
#     # [rotation_freqs, deltas, powers]
#     fs, ps = gen_power_spectrum(FREQ_RANGE, AP_DEF, ROT_OSC)
#     output = np.zeros(shape=(len(ROTS), len(DELS), len(fs)))
                      
#     rot_freq_step = Stepper(ROT_FREQS[0], ROT_FREQS[1], ROT_INC)

#     for rot_ind, rot_val in enumerate(rot_freq_step):
#         delta_step = Stepper(DEL_RANGE[0], DEL_RANGE[1], DEL_INC)
#         for del_ind, del_val, in enumerate(delta_step):
#             output[rot_ind, del_ind, :] = rotate_spectrum(fs, ps, del_val, rot_val)

#     np.save(ROT_DEL_PATH, output)

    
    
if __name__ == "__main__":
    main()
