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
    trials = 555
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
    for i in range(len(trials)):
        
        assert bgs[i][0] in [-.02, .02]
        assert bgs[i][1] in [.98, 1.02]
        
    # Check bg and peaks when arguments are provided
    bgp_opts = param_sampler([[20, 2], [35, 2.5],])
    gauss_opts = param_sampler([[], [10, 0.5, 2], [10, 0.5, 2, 20, 0.3, 4]])
    fg = gen_trial(trials, bgp_opts, gauss_opts)
    bgs = fg.get_all_data('background_params')
    peaks = fg.get_all_data('peak_params')
    
    # Check 2 bg params
    for i in range(len(trials)):
        
        assert (bgs[i][0] in [19.98, 20.02]) or (bgs[i][0] in [34.98, 35.02])
        assert (bgs[i][1] in [1.98, 2.02]) or (bgs[i][1] in [2.48,2.52])
        
    # Check peak params
    for i in range(len(peaks)):
        assert (peaks[i][0] in [9.98, 10.02]) or (peaks[i][0] in [19.98, 20.02])
        assert (peaks[i][1] in [.48, .52]) or (peaks[1][0] in [.28, .32])
        assert (peaks[i][2] in [1.98, 2.02]) or (peaks[2][0] in [3.98, 4.02])
        
        
################~~~~ Slope TEST ~~~~################
     
def test_gen_varying_slope():
    
    # inc is not positive ; end_slope is below inc, n_trials is below 1
    assert gen_varying_slope([4,8],[15, 30], inc = -.0001) == None
    assert gen_varying_slope([4,8],[15, 30], end_slope = -.0001) == None
    assert gen_varying_slope([4,8],[15, 30], end_slope = .24) == None
    assert gen_varying_slope([4,8],[15, 30], end_slope = -4.4) == None
        
        
    gen_varying_slope([4,8],[15, 30], './test_dat/slope_test_1', n_trials = 100)
    
    test_out_1 = np.load('./test_dat/slope_test_1.npy')
    
    # checks if average of cannonical ratio of small slope is larger than average of cannonical ratio of large slope
    # The following line checks the same for power density
    assert np.mean(test_out_1[0][0]) > np.mean(test_out_1[9][0])
    assert np.mean(test_out_1[0][2]) > np.mean(test_out_1[9][2])
                
        
        
        
        