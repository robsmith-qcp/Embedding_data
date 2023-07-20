import presses
import pyscf
import sys
import time

keywords = {}
keywords['scf_method'] = 'dft' # If dft is chosen, the user should specify the desired exchange-correlation functional
keywords['subsystem_method'] = 'mp2'
keywords['xc'] = 'pbe'
keywords['split_spade'] = False
keywords['atom'] = '''
Fe     0.0006   0.0007   0.1423
N    -2.0114   0.0001   0.0007
N    -0.0059   -2.0122   -0.0007
N     2.0112   0.0001   0.0007
N     0.0061   2.012   -0.0007
N     -0.0021   -0.002   2.1062
C    -2.845   -1.0918   -0.0438
C    -2.8376   1.0976   0.0024
C    -1.1005   -2.8423   -0.0469
C     1.0889   -2.8419   -0.0003
C     2.8374   -1.0972   0.003
C     2.8443   1.0916   -0.0441
C     -1.0885   2.8418   0.0013
C     1.1004   2.8415   -0.0469
C     -0.7332   -0.7867   2.8752
C     0.7452   0.8002   2.9437
C     -2.4247   -2.4174   -0.0572
C     -2.412   2.4201   0.0192
C     2.4242   2.4168   -0.0593
C     2.4124   -2.4196   0.0185
C    -4.2277   -0.6723   -0.0702
H    -5.0767   -1.3434   -0.1156
C    -4.2226   0.688   -0.0396
H    -5.0665   1.3666   -0.0549
C     0.675   -4.2254   -0.0454
H     1.3505   -5.0719   -0.0626
C     -0.6854   -4.226   -0.0762
H     -1.3594   -5.0727   -0.1234
C     4.2227   -0.6875   -0.0384
H     5.0667   -1.366   -0.052
C     4.2273   0.6725   -0.0698
H     5.0758   1.3441   -0.1132
C     0.6858   4.2256   -0.0745
H     1.3603   5.0718   -0.1192
C     -0.6742   4.2257   -0.0425
H     -1.3496   5.0723   -0.0569
H     -3.1941   -3.1841   -0.094
H     -3.1793   3.1895   0.0183
H     3.1934   3.1835   -0.0948
H     3.18   -3.1888   0.017
N     -0.4857   -0.5207   4.1817
C     0.4545   0.4886   4.2436
H     -1.4294   -1.5335   2.5257
H     -0.918   -0.9848   4.9666
H     0.8188   0.88   5.1805
H     1.4295   1.5338   2.5479
'''
keywords['active_space_atoms'] = 16
keywords['basis'] = 'def2-svp'
keywords['spin'] = 0 # in PySCF this is the number of unpaired electrons, not 2s+1
keywords['charge'] = 0
keywords['conv_tol_grad'] = 1e-6
keywords['output_name'] = 'reactant'
keywords['spectrum'] = True

start = time.time()
e, mf, ec = presses.run_embed(keywords)
finish = time.time()-start
print('time elapsed: ', finish)
