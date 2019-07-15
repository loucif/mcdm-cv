# Filename: VIKOR_ISOCOV.py
# Description: VIKOR_ISOCOV method

from VIKOR import *
from normalisation_fuc import isocov_normalisation
import BWM


# Step 1*:
#   change SR fucntion to adapt isocov approch
#   normalise and compute the values S_i and R_i


def SR_isocov(D, f, w, p, v, t):
    """ 
        calculate Si and Ri with 

            Si = sum(wj * Dij * fij)
            Ri = max [Si]

        the output is two array S and R
    """
    minmax = BWM.min_max(D)

    s = zeros(D.shape[0])
    r = zeros(D.shape[0])

    for i in range(D.shape[0]):
        k = 0
        u = 0
        n = 0
        for j in range(D.shape[1]):

            # calculate fij and sum with weights *fij
            if p[j] == 'max':
                n = w[j] * ((D[i, j] - minmax[j, 1])
                            / (minmax[j, 0] - minmax[j, 1])) * f[i, j]
                k = k + n
            elif p[j] == 'min':
                n = w[j] * ((minmax[j, 0] - D[i, j])
                            / (minmax[j, 0] - minmax[j, 1])) * f[i, j]
                k = k + n

            # determine Ri (max{si})
            if n > u:
                u = n
                r[i] = round(n, 3)
            else:
                r[i] = round(u, 3)
        # test is the type is weather hard or soft

        s[i] = round(k, 3)

        if (t == 'hard' and v[i] == 0):
            s[i] = s[i] - 1
            r[i] = r[i] - 1

    return s, r


# VIKOR OMRI version
def vikor_isocov(D, w, p, AB, t):
    """ 
        ranking criteria using isocov approch with vikor
        D is the matrix of the population, 
        w is the criteria's weights array 
        p is the criteria benifit/cost (min/max) values, 
        v is the binary variable hat indicates
            whether it satisfies all the constraints or not 
        t is the type of ranking (hard/soft)
        the output is two array S and R
    """

    # calculate fij with isocov
    f = isocov_normalisation(D, p, AB)

    # calculate the binary array
    vi = BWM.v(D, AB)

    # calculate Si, Ri
    s, r = SR_isocov(D, f, w, p, vi, t)

    # determine the values S-, S*, R-, R*
    # and calculate Qi
    q = Q(s, r, len(w))

    return s, r, q
