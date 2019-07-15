# Filename: WPM_ISOCOV.py
# Description: WPM_ISOCOV method

from numpy import *
from  BWM import min_max, v
from  normalisation_fuc import isocov_normalisation

# Step 1: normalise and compute the values S_i


def S_isocov(D, f, w, p, v, t):
    """ 
        calculate Si with 

            Si = sum(wj * Dij * fij)

        the output is an array S 
    """
    minmax = min_max(D)

    s = zeros(D.shape[0])

    for i in range(D.shape[0]):
        k = 1
        n = 1
        for j in range(D.shape[1]):

            # calculate fij and sum with weights *fij
            if p[j] == 'max':
                n =  ((D[i, j] - minmax[j, 1])
                            / (minmax[j, 0] - minmax[j, 1])) ** (w[j]* f[i, j])
                k = k * n
            elif p[j] == 'min':
                n = ((minmax[j, 0] - D[i, j])
                            / (minmax[j, 0] - minmax[j, 1])) ** (w[j]* f[i, j])
                k = k * n

        # s[i] = round(k, 3)
        s[i] =  k

        # test is the type is weather hard or soft
        if (t == 'hard' and v[i] == 0):
            s[i] = s[i] - 1

    return s


def wpm_isocov(D, w, p, ab, t):
    """ 
        D is the matrix of the population, 
        w is the criteria's weights array 
        p is the criteria min/max values, 
    """

    # calculate fij with isocov
    f = isocov_normalisation(D, p, ab)

    # calculate the binary array
    vi = v(D, ab)

    # calculate Si
    s = S_isocov(D, f, w, p, vi, t)


    return s
