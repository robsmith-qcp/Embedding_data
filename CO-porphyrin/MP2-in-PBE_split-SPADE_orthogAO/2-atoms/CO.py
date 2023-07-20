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
C       -0.0025992439     -0.0015996976     -3.3363466315                 
O       -0.0016007561     -0.0012003024     -2.2093533685                 
'''
keywords['active_space_atoms'] = 2
keywords['basis'] = 'def2-svp'
keywords['spin'] = 0 # in PySCF this is the number of unpaired electrons, not 2s+1
keywords['charge'] = 0
keywords['conv_tol_grad'] = 1e-6
keywords['output_name'] = 'CO'
keywords['spectrum'] = True
keywords['split_cutoff'] = False
start = time.time()
e, mf, ec = presses.run_embed(keywords)
finish = time.time()-start
print('time elapsed: ', finish)
