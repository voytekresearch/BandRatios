"""Tools to analyze band ratio data"""
import numpy as np

def nan_corr_pearson(vec1, vec2):
    """Correlation of two vectors with NaN values.
    Note: assumes the vectors have NaN in the same indices.
    """
    vec1 = np.asarray(vec1)
    vec2 = np.asarray(vec2)
    nan_inds = np.isnan(vec1)

    return pearsonr(vec1[~nan_inds], vec2[~nan_inds])

def nan_corr_spearman(vec1, vec2):
    """Correlation of two vectors with NaN values.
    Note: assumes the vectors have NaN in the same indices.
    """
    
    vec1 = np.asarray(vec1)
    vec2 = np.asarray(vec2)

    nan_inds = np.isnan(vec1)

    return spearmanr(vec1[~nan_inds], vec2[~nan_inds])