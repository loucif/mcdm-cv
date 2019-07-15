# Filename: TOPSIS.py
# Description: TOPSIS method


from numpy import *
import BWM as bwm
import timeit

# Step 1: normalize the decision matrix
def norm(D):
    """ 
        D is the population array
        the output is a normalized array
        """
    k = sum(D**2, axis=0)
    return array([[round(D[i, j] / sqrt(k[j]), 4) for j in range(D.shape[1])] for i in range(D.shape[0])])

# Step 2: find the weighted normalized decision matrix


def mul_w(w, t):
    """ 
        multiplication of each evaluation by the associate weight
        r stands for the weights matrix 
        t is the normalized matrix resulting from norm()
        """
    return array([[t[i, j] * w[j] for j in range(t.shape[1])] for i in range(t.shape[0])])

# Step 3: calculate the ideal and anti-ideal solutions


def ideal_anti_ideal(x, p):
    """ 
        x is the weighted normalized decision matrix 
        p is the min/max criteria
        output y = R+, z =R-
    """
    f = bwm.best_worst_fij(x, p).transpose()
    y, z = f[0], f[1]
    return y, z

# Step 4: determine the distance to the ideal and anti-ideal solutions


def distance(x, y, z):
    """ 
        calculate the distances from the positive ideal solution (R+)
        and the negative ideal solution (R-); 
        x is the weighted normalized decision matrix 
        and y, z the results of ideal_anti_ideal()
    """
    Sp = array([[(x[i, j] - y[j])**2 for j in range(x.shape[1])]
                for i in range(x.shape[0])])
    Sm = array([[(x[i, j] - z[j])**2 for j in range(x.shape[1])]
                for i in range(x.shape[0])])
    return sqrt(sum(Sp, 1)), sqrt(sum(Sm,1))

# TOPSIS method: it calls the other functions and includes
# step 5


def topsis(D, w,  p):
    """ 
        D is the initial decision matrix, 
        w is the weights matrix, 
        p is the min/max criteria
        """
    pij = mul_w(w, norm(D))

    Rp, Rm = ideal_anti_ideal(pij, p)

    Sp, Sm = distance(pij, Rp, Rm)

    final_s = array([(Sm[i] / (Sm[i] + Sp[i]))
                     for i in range(Sp.shape[0])])
    return final_s