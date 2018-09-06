"""Test functions for simulating Band Ratio data"""
import numpy as np

from utils.sims import *


###################################################

def test_set_vary_bands():
    
    # theta beta ; low is stationary
    assert set_vary_bands([4,8], [15,30],'low') == ([15,30], [4,8])
    
    # beta/theta ; high is stationary
    assert set_vary_bands([4,8], [15,30],'high') == ([4,8], [15,30])
    
def test_gen_trials():
    # Check n_trials
    trials = 5
    fg = gen_trials(trials)
    sls = fg.get_all_data('background_params', 'slope')
    assert len(sls) == trials
    
    #check bg and peaks when no argument is provided
    fg = gen_trials(trials)
    bgs = fg.get_all_data('background_params')
    peaks = fg.get_all_data('peak_params')
    
    # Check no peaks
    assert len(peaks) == 0
    
    # Check bg with noise
    for i in range(trials):
        
        assert (bgs[i][0] > -.02 and bgs[i][0] < .02)
        assert (bgs[i][1] >.98 and bgs[i][1] < 1.02)
        
    # Check bg and peaks when arguments are provided
    bgp_opts = param_sampler([[20, 2], [35, 2.5],])
    gauss_opts = param_sampler([[], [10, 0.5, 2], [10, 0.5, 2, 20, 0.3, 4]])
    fg = gen_trials(trials, bgp_opts, gauss_opts)
    bgs = fg.get_all_data('background_params')
    peaks = fg.get_all_data('peak_params')
    
    # Check 2 bg params
    for i in range(trials):
        
        assert (bgs[i][0] > 19.98 and bgs[i][0] < 20.02) or (bgs[i][0] > 34.98 and bgs[i][0] < 35.02)
        assert (bgs[i][1] > 1.98 and bgs[i][1] < 2.02) or (bgs[i][1] > 2.48 and bgs[i][1] < 2.52)
        
    # Check peak params
    #TODO BREAKS here
    for i in range(len(peaks)):
        assert (peaks[i][0] > 9.98 and peaks[i][0] < 10.02) or (peaks[i][0] > 19.98 and peaks[i][0] < 20.02)
        assert (peaks[i][1] > .48 and peaks[i][1] < .52) or (peaks[i][1] > .28 and peak[1][1] < .32)
        assert (peaks[i][2] > 1.98 and  peaks[i][2] < 2.02) or (peaks[i][2] > 3.98 and peaks[i][2] < 4.02)
        
        
################~~~~ Slope TEST ~~~~################
     
def test_gen_varying_slope():
    
    # inc is not positive ; end_slope is below inc, n_trials is below 1
    assert gen_varying_slope([4,8],[15, 30], inc = -.0001, n_trials = 5) == None
    assert gen_varying_slope([4,8],[15, 30], end_slope = -.0001,n_trials = 5) == None
    assert gen_varying_slope([4,8],[15, 30], end_slope = .24, n_trials = 5) == None
    assert gen_varying_slope([4,8],[15, 30], end_slope = -4.4, n_trials = 5) == None
        
        
    gen_varying_slope([4,8], [15, 30], './tests/test_dat/slope_test_1', n_trials = 10)
    
    test_out_1 = np.load('./tests/test_dat/slope_test_1.npy')
    
    # checks if average of cannonical ratio of small slope is larger than average of cannonical ratio of large slope
    # The following line checks the same for power density
    assert np.mean(test_out_1[0][0]) < np.mean(test_out_1[9][0])
    assert np.mean(test_out_1[0][2]) < np.mean(test_out_1[9][2])
                
        
        
        
        