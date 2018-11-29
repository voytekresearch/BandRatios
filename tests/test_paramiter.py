""" Tests for generators which iterate through a parameter """

from utils.paramiter import *
import numpy as np
import types

####################################

def test_param_iter():
    
    # Tests CF
    cfs = [8,12,.25] 
    test_cf = param_iter([cfs, 1, 1])
    
    i=0
    num_iters = (int(cfs[1]-cfs[0]) /cfs[2]) 
    while i < num_iters:
        x = next(test_cf)
        assert isinstance(test_cf,types.GeneratorType)
        assert np.isclose(x[0], [cfs[0]+(cfs[2]*i),1,1]).all()
        assert isinstance(x,tuple)
        assert isinstance(x[0], list)
        assert isinstance(x[1], int)
        i+=1
               
    # Tests Amp
    amps = [0,2,.25]
    test_amp = param_iter([8, amps, 1])
    
    i = 0
    num_iters = (int(amps[1]-amps[0]) /amps[2]) 
    while i < num_iters:
        x = next(test_amp)
        assert isinstance(test_amp,types.GeneratorType)
        assert np.isclose(x[0], [8,amps[0]+(amps[2]*i),1]).all()
        assert isinstance(x,tuple)
        assert isinstance(x[0], list)
        assert isinstance(x[1], int)
        i += 1
        
    #Tests BW
    bws = [0, 2.5, .1]
    test_bws = param_iter([8,1,bws])
    
    i = 0
    num_iters = (int(bws[1]-bws[0]) /bws[2]) 
    while i < num_iters:
        x = next(test_bws)
        assert isinstance(test_bws,types.GeneratorType)
        assert np.isclose(x[0],[8,1,bws[0]+(bws[2]*i)]).all()
        assert isinstance(x,tuple)
        assert isinstance(x[0], list)
        assert isinstance(x[1], int)
        i += 1
        
        
def test_osc_param_iter():
    
    # Test defaults
    
    i=0
    test_default = osc_param_iter()
    # 20 and 10 come from default values of function
    num_iters = 20-10
    while i <= num_iters:
        x = next(test_default)
        assert isinstance(test_default,types.GeneratorType)
        assert np.isclose(x[0], [10+i,1,1]).all()
        assert isinstance(x,tuple)
        assert isinstance(x[0], list)
        assert isinstance(x[1], int)
        i+=1
        
    # Tests CF
    cfs = [8,12,.25] 
    test_cf =  osc_param_iter(cfs, 1, 1)
    
    i=0
    num_iters = (int(cfs[1]-cfs[0]) /cfs[2]) 
    while i < num_iters:
        x = next(test_cf)
        assert isinstance(test_cf,types.GeneratorType)
        assert np.isclose(x[0], [cfs[0]+(cfs[2]*i),1,1]).all()
        assert isinstance(x,tuple)
        assert isinstance(x[0], list)
        assert isinstance(x[1], int)
        i+=1    
        
    # Tests Amp
    
    amps = [0,2,.25]
    test_amp = osc_param_iter(8, amps, 1)
    
    i = 0
    num_iters = (int(amps[1]-amps[0]) /amps[2]) 
    while i < num_iters:
        x = next(test_amp)
        assert isinstance(test_amp,types.GeneratorType)
        assert np.isclose(x[0], [8,amps[0]+(amps[2]*i),1]).all()
        assert isinstance(x,tuple)
        assert isinstance(x[0], list)
        assert isinstance(x[1], int)
        i += 1
               
    #Tests BW
    bws = [0, 2.5, .1]
    test_bws = osc_param_iter(8,1,bws)
    
    i = 0
    num_iters = (int(bws[1]-bws[0]) /bws[2]) 
    while i < num_iters:
        x = next(test_bws)
        assert isinstance(test_bws,types.GeneratorType)
        assert np.isclose(x[0], [8,1,bws[0]+(bws[2]*i)]).all()
        assert isinstance(x,tuple)
        assert isinstance(x[0], list)
        assert isinstance(x[1], int)
        i += 1
        
def test_bg_param_iter():
  
    # Test defaults
    i=0
    test_default = bg_param_iter()
    # 20 and 10 come from default values of function
    num_iters = int(3/.25) - 1
    while i <= num_iters:
        x = next(test_default)
        assert isinstance(test_default,types.GeneratorType)
        assert np.isclose(x[0], [0,.25*i]).all()
        assert isinstance(x,tuple)
        assert isinstance(x[0], list)
        assert isinstance(x[1], int)
        i+=1
        
    # Test offset
    
    offs = [0,2,.1]
    test_off = bg_param_iter(offs, 1)
    i = 0
    
    num_iters = (int(offs[1]-offs[0]) /offs[2])
    while i < num_iters:
        x = next(test_off)
        assert isinstance(test_off,types.GeneratorType)
        assert np.isclose(x[0], [offs[0] + (offs[2]*i), 1]).all()
        assert isinstance(x,tuple)
        assert isinstance(x[0], list)
        assert isinstance(x[1], int)
        i+=1
        
    # Test slope
    
    sl = [0, 3, .25]
    test_sl = bg_param_iter(0, sl)
    i = 0
    
    num_iters = (int(sl[1]-sl[0]) /sl[2])
    while i < num_iters:
        x = next(test_sl)
        assert isinstance(test_sl,types.GeneratorType)
        assert np.isclose(x[0], [0,sl[0] + (sl[2]*i)]).all()
        assert isinstance(x,tuple)
        assert isinstance(x[0], list)
        assert isinstance(x[1], int)
        i+=1
    
    