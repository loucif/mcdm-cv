
import os, shutil
import numpy as np
import TOPSIS as topsis
import VIKOR as vikor
import SAW as saw
import WPM as wpm
import normalisation_fuc as normfunc
import VIKOR_RIM as vikor_rim
import SAW_RIM as saw_rim
import WPM_RIM as wpm_rim
import VIKOR_OMRI as vikor_omri
import SAW_OMRI as saw_omri
import WPM_OMRI as wpm_omri
import BWM
import TOPSIS_ISOCOV as topsis_isocov
import VIKOR_ISOCOV as vikor_isocov
import SAW_ISOCOV as saw_isocov
import WPM_ISOCOV as wpm_isocov

# Introduce dataset and parameters

""" data_set = np.array([   [45, 27.2, 58],
                        [71.75, 14.6, 86],
                        [117, 23.4, 59],
                        [70, 5.4, 91],
                        [105.2, 18.2, 91],
                        [224, 24.6, 88]])

weights = np.array([0.2, 0.4, 0.4])

p = np.array(['min', 'max', 'max'])

constraint_AB = np.array([[50, 12, 30], [100, 25, 90]])
 """
""" # Second dataset and para

data_set = np.genfromtxt('QWS_dataset.csv',delimiter=',', skip_header=1)
print(data_set)
weights = np.array([0.11, 0.11, 0.11, 0.11, 0.11, 0.11, 0.11, 0.11, 0.11])

p = np.array(['min', 'max', 'max', 'max', 'max', 'max', 'min', 'max', 'max'])

constraint_AB = np.array([  [45, 60, 2, 60, 60 , 70, 80, 10, 8], 
                            [224, 75, 29.5, 80, 75, 85, 90, 200, 97]]) """

data_set = np.array([   [10, 3, 10, 8, 5],
                        [8, 7, 7, 8, 7],
                        [8, 5, 7, 10, 10],
                        [8, 7, 7, 8, 7],
                        [7, 8, 7, 8, 7],
                        [8, 3, 6, 10, 8],
                        [10, 7, 8, 6, 7],
                        [4, 10, 4, 8, 10]])

""" data_set = np.array([   [8, 7, 7, 8, 7],
                        [8, 5, 7, 10, 10],
                        [8, 7, 7, 8, 7],
                        [7, 8, 7, 8, 7]])
 """
weights = np.array([0.3, 0.2, 0.2, 0.1, 0.1])

p = np.array(['max', 'max', 'min', 'max','max'])

constraint_AB = np.array([  [4, 5, 2, 5, 5], 
                            [8, 10, 8, 10, 11]])


# Running TOPSIS

""" Normalisation_matrix = topsis.norm(data_set)
np.savetxt('TOPSIS_normalisation_matrix.csv', Normalisation_matrix, delimiter=',')
pij = topsis.mul_w(weights, Normalisation_matrix)
np.savetxt('TOPSIS_weighted_matrix.csv', pij, delimiter=',')
Rp, Rm = topsis.ideal_anti_ideal(pij, p)
np.savetxt('TOPSIS_Rp_Rm_matrix.csv', [Rp, Rm], delimiter=',')
Sp, Sm = topsis.distance(pij, Rp, Rm)
np.savetxt('TOPSIS_Sp_Sm_matrix.csv', [Sp, Sm], delimiter=',')
final_s = np.array([(Sm[i] / (Sm[i] + Sp[i])) for i in range(Sp.shape[0])])
np.savetxt('TOPSIS_Ranking_matrix.csv', final_s, delimiter=',') """

# Running VIKOR

""" fij = vikor.min_max_normalization(data_set, p)
np.savetxt('VIKOR_fij_matrix.csv', fij, delimiter=',')
s, r = vikor.SR(data_set, weights, p)
np.savetxt('VIKOR_Si_Ri_matrix.csv', np.transpose([s, r]), delimiter=',')
Qi = vikor.Q(s, r, len(weights))
np.savetxt('VIKOR_Qi_matrix.csv', np.transpose(Qi), delimiter=',') """

# Running SAW

""" fij = saw.saw(data_set, weights, p)
np.savetxt('SAW_Qi_matrix.csv', np.transpose(fij), delimiter=',') """

# Running WBM

""" fij = wpm.wpm(data_set, weights, p)
np.savetxt('WPM_Qi_matrix.csv', np.transpose(fij), delimiter=',') """

# Running TOPSIS_RIM

""" Normalisation_matrix = normfunc.rim_normalisation(data_set, constraint_AB)
np.savetxt('TOPSIS_RIM_normalisation_matrix.csv', Normalisation_matrix, delimiter=',')
pij = topsis.mul_w(weights, Normalisation_matrix)
np.savetxt('TOPSIS_RIM_weighted_matrix.csv', pij, delimiter=',')
Rp, Rm = np.array([1 for i in range(data_set.shape[0])]) , np.array([0 for i in range(data_set.shape[0])])
Sp, Sm = topsis.distance(pij, Rp, Rm)
np.savetxt('TOPSIS_RIM_Sp_Sm_matrix.csv', [Sp, Sm], delimiter=',')
final_s = np.array([(Sm[i] / (Sm[i] + Sp[i])) for i in range(Sp.shape[0])])
np.savetxt('TOPSIS_RIM_Ranking_matrix.csv', final_s, delimiter=',') """

"""
#Running VIKOR_RIM

s, r = vikor_rim.SR_rim(data_set, weights, constraint_AB)
np.savetxt('VIKOR_RIM_Si_Ri_matrix.csv', np.transpose([s, r]), delimiter=',')
Qi = vikor.Q(s, r, len(weights))
np.savetxt('VIKOR_RIM_Qi_matrix.csv', np.transpose(Qi), delimiter=',')

# Running SAW_RIM

fij = saw_rim.saw_rim(data_set, weights, constraint_AB)
np.savetxt('SAW_RIM_Qi_matrix.csv', np.transpose(fij), delimiter=',')

# Running WBM_RIM

fij = wpm_rim.wpm_rim(data_set, weights, constraint_AB)
np.savetxt('WPM_RIM_Qi_matrix.csv', np.transpose(fij), delimiter=',')
"""
# Running TOPSIS_OMRI

""" Normalisation_matrix = normfunc.omri_normalisation(data_set, constraint_AB)
np.savetxt('TOPSIS_OMRI_normalisation_matrix.csv', Normalisation_matrix, delimiter=',')
pij = topsis.mul_w(weights, Normalisation_matrix)
np.savetxt('TOPSIS_OMRI_weighted_matrix.csv', pij, delimiter=',')
Rp, Rm = np.array([1 for i in range(data_set.shape[0])]) , np.array([0 for i in range(data_set.shape[0])])
Sp, Sm = topsis.distance(pij, Rp, Rm)
np.savetxt('TOPSIS_OMRI_Sp_Sm_matrix.csv', [Sp, Sm], delimiter=',')
final_s = np.array([(Sm[i] / (Sm[i] + Sp[i])) for i in range(Sp.shape[0])])
np.savetxt('TOPSIS_OMRI_Ranking_matrix.csv', final_s, delimiter=',') """

""" Normalisation_matrix = normfunc.omri_normalisation(data_set, constraint_AB)
np.savetxt('TOPSIS_OMRI_normalisation_matrix.csv', Normalisation_matrix, delimiter=',')
s, r = vikor_omri.SR_omri(data_set, weights, constraint_AB)
np.savetxt('VIKOR_OMRI_Si_Ri_matrix.csv', np.transpose([s, r]), delimiter=',')
Qi = vikor.Q(s, r, len(weights))
np.savetxt('VIKOR_OMRI_Qi_matrix.csv', np.transpose(Qi), delimiter=',') """
"""
"""
 # Running SAW_OMRI

""" fij = saw_omri.saw_omri(data_set, weights, constraint_AB)
np.savetxt('SAW_OMRI_Qi_matrix.csv', np.transpose(fij), delimiter=',') """

# Running WBM_OMRI

""" fij = wpm_omri.wpm_omri(data_set, weights, constraint_AB)
np.savetxt('WPM_OMRI_Qi_matrix.csv', np.transpose(fij), delimiter=',') """

# Running idesl TOPSIS

""" vi =  BWM.v(data_set, constraint_AB)
np.savetxt('TOPSIS_ISOCOV_Vi.csv', np.transpose(vi), delimiter=',')
fij = normfunc.isocov_normalisation(data_set, p, constraint_AB)
np.savetxt('TOPSIS_ISOCOV_normalisation_matrix_fij.csv', fij, delimiter=',')
nij = topsis.norm(data_set)
np.savetxt('TOPSIS_ISOCOV_normalisation_matrix_nij.csv', nij, delimiter=',')
pij = topsis_isocov.p(nij, weights, fij)
np.savetxt('TOPSIS_ISOCOV_pij_matrix.csv', pij, delimiter=',')
Rp, Rm = topsis.ideal_anti_ideal(pij, p)
np.savetxt('TOPSIS_ISOCOV_Rp_Rm_matrix.csv', [Rp, Rm], delimiter=',')
Sp, Sm = topsis.distance(pij, Rp, Rm)
np.savetxt('TOPSIS_ISOCOV_Sp_Sm_matrix.csv', np.transpose([Sp, Sm]), delimiter=',')
final_s_hard = np.array([(Sm[i] / (Sm[i] + Sp[i])) if (vi[i] == 1) else (Sm[i] / (Sm[i] + Sp[i]) - 1)
                         for i in range(Sp.shape[0])])
np.savetxt('TOPSIS_ISOCOV_Ranking_matrix_hard.csv', np.transpose(final_s_hard), delimiter=',')
final_s_soft = np.array([(Sm[i] / (Sm[i] + Sp[i]))
                         for i in range(Sp.shape[0])])
np.savetxt('TOPSIS_ISOCOV_Ranking_matrix_soft.csv', np.transpose(final_s_soft), delimiter=',')
print(final_s_hard)
print(final_s_soft) """

# Running ideal VIKOR

""" vi =  BWM.v(data_set, constraint_AB)
np.savetxt('VIKOR_ISOCOV_Vi.csv', np.transpose(vi), delimiter=',')
fij = normfunc.isocov_normalisation(data_set, p, constraint_AB)
np.savetxt('VIKOR_ISOCOV_normalisation_matrix_fij.csv', fij, delimiter=',')
s, r = vikor_isocov.SR_isocov(data_set, fij, weights, p, vi, 'hardsdsd')
np.savetxt('VIKOR_ISOCOV_Si_Ri_matrix.csv', np.transpose([s, r]), delimiter=',')
q = vikor.Q(s, r, len(weights))
np.savetxt('VIKOR_ISOCOV_Qi_matrix.csv', np.transpose(q), delimiter=',') """

# Running ideal SAW

""" s = saw_isocov.saw_isocov(data_set, weights, p, constraint_AB, 'harfdfdfd')
np.savetxt('SAW_ISOCOV_Qi_matrix.csv', np.transpose(s), delimiter=',') """

# Running ideal WPM

s = wpm_isocov.wpm_isocov(data_set, weights, p, constraint_AB, 'harrered')
np.savetxt('WPM_ISOCOV_Qi_matrix.csv', np.transpose(s), delimiter=',')
