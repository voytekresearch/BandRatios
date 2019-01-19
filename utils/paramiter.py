import numpy as np
import warnings

from utils.ratios import *

def _number_iter(start, stop, step):
    """
    Generator used to iterate 'start' to 'stop' in increments of 'step'
    
    Parameters
    ----------
    start : float
        starting position to generate from
    stop : float
        last generated value
    step : float
        instructions on how to generate the next value t reach 'stop'
        
    Yields
    ------
    float
        next generated value
    """

    current = start
    while current <= stop:
        yield current
        current += step


def param_iter(params):
    """
    This generator finds which parameter will be iterated through then
    genertaes those iterations. params is a list given either as 
    [cf, amp, bw] or [offset, slope]. The intended parameter to iterate
    over will be replaced with a list in the form of [start, stop, step].
    
    Example: if we want to iterate over center frequency values from
    8 to 12 in increments of .25, params = [[8,12,.25], amp, bw]
    
    Parameter
    ---------
    params : list
        each element is a float except the parameter to be iterated over
        that is a list itself
        
    yield
    -----
        a list of the parameters with the next generated interated parametric value
    """
    # Find index we're going to iterate
    for ind, el in enumerate(params):
        if isinstance(el, list):
            iter_index = ind
            break
    
    temp = params
    lst = params[iter_index]
    length = int((lst[1] -lst[0])/lst[2]+1)
    
    for step in _number_iter(*params[iter_index]):
        temp[iter_index] = step
        yield (temp,int(length))
        
def osc_param_iter(cf=[10, 20, 1], amp=1, bw=1):
    """
    Helper function to organize data to send to param_iter
    
    Parameters
    ----------
    cf, amp, bw : float
        values for parameters. The parameter to iterate over should be given
        as a list of floats. See param_iter() for more details
        
    yield
    -----
        a list of the parameters with the next generated interated parametric value
    """
    # Helper function, nicer API
    # What it does: takes inputs, passes them into param_iter
    x = param_iter([cf,amp,bw])
    while True:
        yield next(x)

def bg_param_iter(off=0, sl=[0, 3, 0.1]):
    """
    Helper function to organize data to send to param_iter
    
    Parameters
    ----------
    off, sl : float
        values for parameters. The parameter to iterate over should be given
        as a list of floats. See param_iter() for more details
        
    yield
    -----
        a list of the parameters with the next generated interated parametric value
    """
    # Helper function, nicer API
    # What it does: takes inputs, passes them into param_iter
    x = param_iter([off, sl])
    while True:        
        yield next(x)
