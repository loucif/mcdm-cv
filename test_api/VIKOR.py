# Filename: VIKOR.py
# Description: VIKOR method


from numpy import *
import BWM
import timeit




# Step 1+2: normalise and compute the values S_i and R_i
def SR(D, w, p):
    """ 
        D is the matrix of the population, 
        w is the criteria's weights array 
        p is the criteria min/max values, 
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
                n = w[j] * (D[i, j] - minmax[j, 1]) \
                    / (minmax[j, 0] - minmax[j, 1])
                k = k + n
            elif p[j] == 'min':
                n = w[j] * (minmax[j, 0] - D[i, j]) \
                    / (minmax[j, 0] - minmax[j, 1])
                k = k + n

            # determine Ri
            if n > u:
                u = n 
                r[i] = round(n, 3)
            else:
                r[i] = round(u, 3)
        s[i] = round(k, 3)
    return s, r



# step 3 : determine S- S* R- R*
def min_max_s_r(s, r):
    return min(s), max(s), min(r), max(r)

# Step 3: compute the values Q_i


def Q(s, r, n):
    """ 
        s is the vector with the S_i values, 
        r is the vector with the R_i values, 
        n is the number of criteria 
        """
    v = 0.5
    q = zeros(s.shape[0])
    minS, maxS, minR, maxR = min_max_s_r(s, r)
    # The next line is a quick fix for testing, must be removed in the api final release
    # The tepm directory my cause error
    savetxt('VIKOR_minS_maxS_minR_maxR_matrix.csv', [minS, maxS, minR, maxR], delimiter=',')
    for i in range(s.shape[0]):
        q[i] = round((v * (s[i] - minS) / (maxS - minS) +
                      (1-v) * (r[i] - minR) / (maxR - minR)), 3)
    return q

# VIKOR method: it calls the other functions


def vikor(D, w, p):
    """ 
        D is the data of the population
        w is the weights matrix, 
        p is the criteria 	min/max array, 
    """

    s, r = SR(D, w, p)
    Qi = Q(s, r, len(w))
    return s, r, Qi

def min_max_normalization(D, p):

    minmax = BWM.min_max(D)
    for i in range(D.shape[0]):
        for j in range(D.shape[1]):
            # calculate fij and sum with weights *fij
            if p[j] == 'max':
                D[i, j] = (D[i, j] - minmax[j, 1]) \
                    / (minmax[j, 0] - minmax[j, 1])
            elif p[j] == 'min':
                D[i, j] = (minmax[j, 0] - D[i, j]) \
                    / (minmax[j, 0] - minmax[j, 1])

    return D