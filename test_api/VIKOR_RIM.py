

import VIKOR as vikor
import numpy as np
from  normalisation_fuc import rim_normalisation

# Step 2*: change SR fucntion to adapt rim version
def SR_rim(D, w, AB):
    nD = rim_normalisation(D, AB)
    
    S = np.zeros(nD.shape[0])
    R = np.zeros(nD.shape[0])

    for i in range(nD.shape[0]):
        for j in range(nD.shape[1]):
         nD[i,j] = nD[i,j] * w[j]
        S[i] = sum (nD[i,:])
        R[i] = max (nD[i,:])
    return S, R


# VIKOR OMRI version
def vikor_rim(D, w, AB):
    s, r = SR_rim(D, w, AB)
    q = vikor.Q(s, r, len(w))
    return s, r, q

    # 002932529 15
    # Boumaad Omar 
    # 0561910256