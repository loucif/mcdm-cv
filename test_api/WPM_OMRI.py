# Filename: wpm_OMRI.py
# Description: wpm_OMRI method

from numpy import *
import BWM
import timeit
from  normalisation_fuc import omri_normalisation

# Step 1+2: normalise and compute the values S_i 


def wpm_omri(D, w, ab):
    """ 
        D is the matrix of the population, 
        w is the criteria's weights array 
        p is the criteria min/max values, 
    """
    
    #calculate normalised dataset 
    nD = omri_normalisation(D, ab)

    s = zeros(D.shape[0])

    # calculate fij and sum  wj*fij
    for i in range(D.shape[0]):
        k = 0
        for j in range(D.shape[1]):
            nD[i,j] = nD[i,j] ** w[j]
        s[i] = prod(nD[i,:])

    return s