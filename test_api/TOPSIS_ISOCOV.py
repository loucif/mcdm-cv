

from numpy import *
from TOPSIS import *
from normalisation_fuc import isocov_normalisation
from BWM import v


def p(nD, w, f):
    """ 
        calculate pij = dij * wj
    """
    P = zeros([nD.shape[0], nD.shape[1]])

    for i in range(nD.shape[0]):
        for j in range(nD.shape[1]):
            P[i, j] = nD[i, j] * w[j] * f[i, j]
    return P


def topsis_isocov(D, w, m, ab, t):

    """ 
        ranking criteria using isocov approch with topsis
        D is the matrix of the population, 
        w is the criteria's weights array 
        m is the criteria benifit/cost (min/max) values, 
        t is the type of ranking (hard/soft)
        ab is the array of constraint ranges

        the output is a matrix of weighted normlised alternatives   
    """
    # calculate vi
    vi = v(D, ab)

    # calculate isocov transformation
    fij = isocov_normalisation(D, m, ab)

    nij = norm(D)

    pij = p(nij, w, fij)

    Rp, Rm = ideal_anti_ideal(pij, m)

    Sp, Sm = distance(pij, Rp, Rm)

    if t == 'hard':
        final_s = array([(Sm[i] / (Sm[i] + Sp[i])) if (vi[i] == 1) else (Sm[i] / (Sm[i] + Sp[i]) - 1)
                         for i in range(Sp.shape[0])])
    else:
        final_s = array([(Sm[i] / (Sm[i] + Sp[i]))
                         for i in range(Sp.shape[0])])

    return final_s
