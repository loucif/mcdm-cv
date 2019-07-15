# Filename: normalisation_fuc.py
# Description: normalisation function RIM, OMRI, ISOCOV
# Authors: Loucif ghr.

from numpy import *
import BWM as bwm

"""
Description : 
    RIM Normalisation : This normalization has been proposed by Cables and al It is the first normalization approach defined to handle value constraints. This normalization proceeds by dividing the distance between the performance ratings by the distance between the maximum (or the minimum) performance rating and the reference ideal performance rating for that criterion. The reference ideal, given generally as an interval [A, B], represents the value constraints fixed by the user for the criterion .
    OMRI Normalisation : Extention from RIM Normalisation.
    ISOCOV Normalisation : Another extention from RIM Normalisation with the introduction of the new argument cost-benefit for criterion.
Usage :
    rim_normalisation(D, AB)
Arguments :
    D : The decision matrix (m x n) with the values of the m alternatives, for the n criterion
    AB :A matrix (2 x n). AB[0,:] corresponds with the A extrem, and AB[1,:] represents the B extrem of the domain of each criterion
    is_it_benfit_then_it_would_be_cost : boolean matrix (2 x 1) with true for benifit criterion and false if it is a cost criterion
Value :
    It returns the new normalized desision matrix
References :
Examples :
"""


def rim_normalisation(D, AB):

    D_temp = zeros([D.shape[0], D.shape[1]])

    d = bwm.min_max(D)

    for j in range(D.shape[1]):
        for i in range(D.shape[0]):
            if (AB[0, j] <= D[i, j] <= AB[1, j]):
                D_temp[i, j] = 1
            elif (d[j, 0] <= D[i, j] <= AB[0, j]):
                D_temp[i, j] = 1 - (AB[0, j] - D[i, j]) / \
                    (AB[0, j] - d[j, 0])
            else:
                D_temp[i, j] = 1 - (D[i, j] - AB[1, j]) / \
                    (d[j, 0] - AB[1, j])

    return D_temp


def omri_normalisation(D, AB):

    D_temp = zeros([D.shape[0], D.shape[1]])

    d = bwm.min_max(D)

    for j in range(D.shape[1]):
        for i in range(D.shape[0]):
            if (AB[0, j] <= D[i, j] <= AB[1, j]):
                D_temp[i, j] = 1
            elif (d[j, 1] <= D[i, j] <= AB[0, j]):
                D_temp[i, j] = 1 - (AB[0, j] - D[i, j])/max(
                    AB[0, j] - d[j, 1], d[j, 0] - AB[1, j])
            else:
                D_temp[i, j] = 1 - (D[i, j] - AB[1, j])/max(
                    AB[0, j] - d[j, 1], d[j, 0] - AB[1, j])

    return D_temp

def isocov_normalisation(D, p, AB):

    D_temp = zeros([D.shape[0], D.shape[1]])

    d = bwm.min_max(D)

    for i in range(D.shape[0]):
        for j in range(D.shape[1]):
            if p[j] == 'max':
                if (AB[0, j] <= D[i, j] <= AB[1, j]):
                    D_temp[i, j] = 1
                elif (d[j, 1] <= D[i, j] <= AB[0, j]):
                    D_temp[i, j] = 1 - (AB[0, j] - D[i, j]) / \
                        (max(AB[0, j] - d[j, 1], d[j, 0] - AB[1, j]) + 1)
                else:
                    D_temp[i, j] = 1 - (D[i, j] - AB[1, j]) / \
                        (max(AB[0, j] - d[j, 1], d[j, 0] - AB[1, j]) + 1)
            elif p[j] == 'min':
                if (AB[0, j] <= D[i, j] <= AB[1, j]):
                    D_temp[i, j] = 1 / \
                        (max(AB[0, j] - d[j, 1], d[j, 0] - AB[1, j]) + 1)
                elif (d[j, 1] <= D[i, j] <= AB[0, j]):
                    D_temp[i, j] = (AB[0, j] - D[i, j]) / \
                        (max(AB[0, j] - d[j, 1], d[j, 0] - AB[1, j]))
                else:
                    D_temp[i, j] = (D[i, j] - AB[1, j]) / \
                        (max(AB[0, j] - d[j, 1], d[j, 0] - AB[1, j]))
    return D_temp
