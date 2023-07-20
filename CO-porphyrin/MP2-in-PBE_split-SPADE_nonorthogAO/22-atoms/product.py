import presses
import pyscf
import sys
import time

keywords = {}
keywords['scf_method'] = 'dft' # If dft is chosen, the user should specify the desired exchange-correlation functional
keywords['subsystem_method'] = 'mp2'
keywords['xc'] = 'pbe'
keywords['split_spade'] = True
keywords['atom'] = '''
C      -0.0026   -0.0016   -3.3372
O      -0.0016   -0.0012   -2.2085
Fe     -0.0009   -0.0009   0.0732
N     -2.0193   -0.0001   -0.0001
N     -0.0065   -2.0194   0.0001
N      2.0195   -0.0001   -0.0001
N      0.0063   2.0196   0.0001
N      0.0009   0.0013   2.0556
C     -2.8483   -1.0921   -0.0421
C     -2.8413   1.0973   0.0221
C     -1.101   -2.8451   -0.0419
C      1.0882   -2.8448   0.0222
C      2.8415   -1.0979   0.0223
C      2.8492   1.0923   -0.0388
C      -1.0888   2.845   0.0226
C      1.1012   2.8458   -0.0385
C      -0.7759   -0.7695   2.8954
C      0.7618   0.7573   2.824
C      -2.4256   -2.4181   -0.0635
C      -2.4131   2.4203   0.0448
C      2.4263   2.4188   -0.0569
C      2.4126   -2.4209   0.0445
C     -4.2323   -0.6726   -0.0459
H     -5.0814   -1.3439   -0.0791
C     -4.2279   0.6872   -0.003
H     -5.0732   1.3644   0.0045
C      0.6738   -4.2303   -0.0028
H      1.3484   -5.0777   0.0046
C      -0.6859   -4.2303   -0.0457
H      -1.3598   -5.0774   -0.0788
C      4.2279   -0.6879   -0.0002
H      5.0731   -1.3653   0.0064
C      4.2329   0.6723   -0.0406
H      5.0824   1.3432   -0.0729
C      0.6858   4.2308   -0.0399
H      1.3594   5.0783   -0.0719
C      -0.6744   4.2301   0.0005
H      -1.3491   5.0775   0.0075
H      -3.195   -3.1849   -0.0962
H      -3.1804   3.1897   0.0606
H      3.1958   3.1857   -0.0877
H      3.1797   -3.1906   0.0601
N      0.5057   0.5036   4.1311
C      -0.4733   -0.4682   4.1949
H      -1.4883   -1.4771   2.5023
H      -0.8519   -0.8437   5.1327
H      0.9565   0.9516   4.915
H      1.4865   1.4767   2.475
'''
keywords['active_space_atoms'] = 22
keywords['basis'] = 'def2-svp'
keywords['spin'] = 0 # in PySCF this is the number of unpaired electrons, not 2s+1
keywords['charge'] = 0
keywords['conv_tol_grad'] = 1e-6
keywords['output_name'] = 'product'
keywords['spectrum'] = True
keywords['orthog'] = False
start = time.time()
e, mf, ec = presses.run_embed(keywords)
finish = time.time()-start
print('time elapsed: ', finish)
