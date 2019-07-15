# Filename: SAW_RIM.py
# Description: SAW_RIM method

from numpy import *
import BWM
import timeit
from  normalisation_fuc import rim_normalisation

# Step 1+2: normalise and compute the values S_i


def saw_rim(D, w, ab):
    """ 
        D is the matrix of the population, 
        w is the criteria's weights array 
        p is the criteria min/max values, 
    """
    
    #calculate normalised dataset 
    nD = rim_normalisation(D, ab)

    s = zeros(D.shape[0])

    # calculate fij and sum  wj*fij
    for i in range(D.shape[0]):
        k = 0
        for j in range(D.shape[1]):
            nD[i,j] = nD[i,j] * w[j]
        s[i] = round(sum(nD[i,:]),3)

    return s
