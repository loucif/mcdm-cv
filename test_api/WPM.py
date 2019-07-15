# Filename: WPM.py
# Description: WPM method

from numpy import *
import BWM
import timeit

# Step 1+2: normalise and compute the values S_i and R_i


def wpm(D, w, p):
    """ 
        D is the matrix of the population, 
        p is the criteria min/max values, 
        c is the criteria's weights array 
    """
    minmax = BWM.min_max(D)

    s = zeros(D.shape[0])
    r = zeros(D.shape[0])
    for i in range(D.shape[0]):
        k = 1
        for j in range(D.shape[1]):

            # calculate fij and sum with weights *fij
            if p[j] == 'max':
                k = k *  ((D[i, j] - minmax[j, 1]) \
                    / (minmax[j, 0] - minmax[j, 1])) ** w[j]
            elif p[j] == 'min':
                k = k * ((minmax[j, 0] - D[i, j]) \
                    / (minmax[j, 0] - minmax[j, 1])) ** w[j]
        s[i] = k
    return s
