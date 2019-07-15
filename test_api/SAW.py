# Filename: SAW.py
# Description: SAW method

from numpy import *
import BWM
import timeit

# Step 1+2: normalise and compute the values S_i 


def saw(D, w, p):
    """ 
        D is the matrix of the population, 
        w is the criteria's weights array 
        p is the criteria min/max values, 
    """
    minmax = BWM.min_max(D)

    s = zeros(D.shape[0])

    for i in range(D.shape[0]):
        k = 0
        for j in range(D.shape[1]):

            # calculate fij and sum with weights *fij
            if p[j] == 'max':
                k = k + w[j] * (D[i, j] - minmax[j, 1]) \
                    / (minmax[j, 0] - minmax[j, 1])
            elif p[j] == 'min':
                k = k + w[j] * (minmax[j, 0] - D[i, j]) \
                    / (minmax[j, 0] - minmax[j, 1])

        s[i] = round(k, 3)
    return s
