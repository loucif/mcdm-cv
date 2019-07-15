# Filename: BWM.py
# Description: BWM method

from numpy import *
"""
    Determine the best and worst values
    for all criteria functions
"""


def best_worst_fij(D, p):
    """
        D is the data of the population
        p is the criteria min/max array
        the output is an 2D matrix of min/max values
	"""
    f = zeros((p.shape[0], 2))
    for i in range(p.shape[0]):
        if p[i] == 'max':
            f[i, 0] = D.max(0)[i]
            f[i, 1] = D.min(0)[i]
        elif p[i] == 'min':
            f[i, 0] = D.min(0)[i]
            f[i, 1] = D.max(0)[i]
    return f


def min_max(D):
    f = zeros((D.shape[1], 2))
    for i in range(D.shape[1]):
        f[i, 0] = D.max(0)[i]
        f[i, 1] = D.min(0)[i]
    return f 

def v(D, ab):
    vi = ones(D.shape[0])

    for i in range(D.shape[0]):
        for j in range(D.shape[1]):
            if (D[i, j] < ab[0, j] or D[i, j] > ab[1, j]):
                vi[i] = 0
                break
    return vi

def normaliseWeights(w) : 
    s = sum(w)
    return array([x/s for x in list(w)])

def rank_mcdm(D):
    b = [(ob,index+1) for index, ob in enumerate(list(D))]
    sortedD = sorted(b,reverse=True)
    sortedD = [(a[1], a[0], str(i+1)) for i , a in enumerate(sortedD)]
    return sorted(sortedD)