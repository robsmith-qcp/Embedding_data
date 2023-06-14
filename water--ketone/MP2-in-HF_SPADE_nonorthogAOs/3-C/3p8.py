import presses
import pyscf
import sys
import time

keywords = {}
keywords['scf_method'] = 'hf' # If dft is chosen, the user should specify the desired exchange-correlation functional
keywords['subsystem_method'] = 'mp2'
keywords['split_spade'] = False
keywords['atom'] = '''
O        0.0000000000      0.0000000000      5.9901250574                 
H        0.0000000000      0.0000000000      5.0252223669                 
H       -0.0266277560      0.9438037757      6.1890277934                 
O        0.0000000000      0.0000000000      1.2252223669                 
C        0.0000000000      0.0000000000      0.0000000000                 
C        1.0642710095     -0.7420505032     -0.7978666179                 
C       -1.0649656142      0.7478917103     -0.7954375138                 
H        1.7570660606     -1.1997606119     -0.0719665057                 
C        1.8304200960      0.1520835817     -1.7856446967                 
H        0.5697279010     -1.5596183003     -1.3575588343                 
H       -1.4155671146      0.0974826754     -1.6203114059                 
H       -0.5713740603      1.6079141349     -1.2894688381                 
C       -2.2310487488      1.2326590585      0.0634703733                 
H        2.2460406699      1.0232629037     -1.2434409540                 
H        1.1378406132      0.5541243981     -2.5479591522                 
C        2.9673419641     -0.5948991339     -2.4885542935                 
H       -1.8353893676      1.8571543134      0.8834446460                 
H       -2.7087178333      0.3628883435      0.5505969496                 
C       -3.2719807739      2.0156867603     -0.7390308429                 
H        3.6672576767     -0.9924761584     -1.7285907895                 
C        3.7378782727      0.2798179679     -3.4810852575                 
H        2.5523215930     -1.4741471493     -3.0189801208                 
H       -3.6596979835      1.3827653472     -1.5614672868                 
H       -2.7862896307      2.8862401909     -1.2224302199                 
C       -4.4447810259      2.5044051323      0.1153636559                 
H        4.1452481463      1.1593433410     -2.9480097812                 
H        3.0350654340      0.6740493497     -4.2390877808                 
C        4.8743828350     -0.4746672489     -4.1748216259                 
H       -4.0549408197      3.1341953223      0.9368320053                 
H       -4.9292711572      1.6338505967      0.5959297853                 
C       -5.4795332285      3.2905989461     -0.6927205194                 
H        5.6030124766     -0.8523700057     -3.4370731461                 
H        5.4161618170      0.1718133065     -4.8846912731                 
H        4.4856544651     -1.3419851358     -4.7357230923                 
H       -5.0216211785      4.1805718759     -1.1579663083                 
H       -6.3148437093      3.6325924638     -0.0595631224                 
H       -5.9009942094      2.6696776944     -1.5020689780                 
'''
keywords['active_space_atoms'] = 11
keywords['basis'] = 'cc-pVDZ'
keywords['spin'] = 0 # in PySCF this is the number of unpaired electrons, not 2s+1
keywords['charge'] = 0
keywords['conv_tol_grad'] = 1e-5
keywords['output_name'] = "3.8_nonorthog"
keywords['spectrum'] = True
keywords['orthog'] = False

start = time.time()
e, mf, ec = presses.run_embed(keywords)
finish = time.time()-start
print('time elapsed: ', finish)
