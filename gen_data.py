import numpy as np

from fooof import FOOOFGroup
from fooof.synth import gen_group_power_spectra

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

def param_iter(params):
    """
    This generator finds which parameter will be iterated through then
    genertaes those iterations. params is a list given either as 
    [cf, amp, bw] or [offset, slope]. The intended parameter to iterate
    over will be replaced with a list in the form of [start, stop, step].
    
    Parameter
    ---------
    params : list
        each element is a float except the parameter to be iterated over
        that is a list itself
        
    Yields
    -----
        A 2 element tuple where the first value is a list of the next iterated 
        parameters and the second element is the length of the generator

    Example
    -------
    Example: if we want to iterate over center frequency values from
    8 to 12 in increments of .25: params = [[8,12,.25], amp, bw]
    """
    
    num_iters = 0
    
    for i in range(len(params)):
        if isinstance(params[i], range):
            length = len(params[i])
            num_iters += 1
            ind = i
    
        if num_iters > 1:
            raise Warning("Iteration is only supported on one parameter")
            
    temp = params
    c = ( func(params,ind,x) for x in params[ind])     
    return (c, length)

def _param_generator(params, ind, chg):
    params[ind] = chg
    return params


def main():

   # Generate varying Center Frequency Data
   # Low Band
   cf_iter_low, cf_n_low = param_iter([range(LOW_BAND[0],LOW_BAND[1],CF_INC),DEF_AMP,DEF_BW])
   cf_low_fs, cf_low_ps, cf_low_syns = gen_group_power_spectra(cf_n_low,FREQ_RANGE, DEF_BG, cf_iter_low)
   cf_low_save = []
   cf_low_save = cf_low_save.append(cf_low_fs).append(cf_low_ps).append(cf_low_syns)
   np.save(CF_PATH_LOW,cf_low_save)


   # High Band
   cf_iter_high, cf_n_high = param_iter([range(HIGH_BAND[0],HIGH_BAND[1],CF_INC),DEF_AMP,DEF_BW])
   cf_high_fs, cf_high_ps, cf_high_syns = gen_group_power_spectra(cf_n_high,FREQ_RANGE, DEF_BG, cf_iter_high)
   cf_high_save = []
   cf_high_save = cf_low_save.append(cf_high_fs).append(cf_high_ps).append(cf_high_syns)
   np.save(CF_PATH_HIGH,cf_high_save)





   # Generate varying Amplitude Data
   # Low Band
   amp_iter_low, amp_n_low = param_iter([DEF_CF_LOW, range(0,END_AMP,AMP_INC),DEF_BW])
   amp_low_fs, amp_low_ps, amp_low_syns = gen_group_power_spectra(amp_n_low, FREQ_RANGE, DEF_BG, amp_iter_low)
   amp_low_save = []
   amp_low_save = amp_low_save.append(amp_low_fs).append(amp_low_ps).append(amp_low_syns)
   np.save(AMP_PATH_LOW, amp_low_save)

   # High Band
   amp_iter_high, amp_n_high = param_iter([DEF_CF_HIGH, range(0,END_AMP,AMP_INC),DEF_BW])
   amp_high_fs, amp_high_ps, amp_high_syns = gen_group_power_spectra(amp_n_high, FREQ_RANGE, DEF_BG, amp_iter_high)
   amp_high_save = []
   amp_high_save = amp_high_save.append(amp_high_fs).append(amp_high_ps).append(amp_high_syns)
   np.save(AMP_PATH_HIGH, amp_high_save)





   # Generate varying BandWidth data
   # Low Band
   bw_iter_low, bw_n_low = param_iter(DEF_CF_LOW, DEF_AMP, range(0, END_BW, BW_INC))
   bw_low_fs, bw_low_ps, bw_low_syns = gen_group_power_spectra(bw_n_low, FREQ_RANGE, DEF_BG, bw_iter_low)
   bw_low_save = []
   bw_low_save = bw_low_save.append(bw_low_fs).append(bw_low_ps).append(bw_low_syns)
   np.save(BW_PATH_LOW, bw_low_save)


   # High Band
   bw_iter_high, bw_n_high = param_iter(DEF_CF_HIGH, DEF_AMP, range(0, END_BW, BW_INC))
   bw_high_fs, bw_high_ps, bw_high_syns = gen_group_power_spectra(bw_n_high, FREQ_RANGE, DEF_BG, bw_iter_high)
   bw_high_save = []
   bw_high_save = bw_high_save.append(bw_high_fs).append(bw_high_ps).append(bw_high_syns)
   np.save(BW_PATH_HIGH, bw_high_save)






   # Generate varying slope data
   sl_iter, sl_n = param_iter([0,range(START_SLOPE,END_SLOPE,SLOPE_INC)])
   sl_fs, sl_ps, sl_syns = gen_group_power_spectra(sl_n, FREQ_RANGE,sl_iter,[])
   sl_save = []
   sl_save = sl_save.append(sl_fs).append(sl_ps).append(sl_syns)
   np.save(SLOPE_PATH, sl_save)

if __name__ == "__main__":
	main()
