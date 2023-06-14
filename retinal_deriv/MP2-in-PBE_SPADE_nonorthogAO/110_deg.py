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
C        0.3656615801      0.3423402649     -1.8427174533                 
H        1.4184724249      0.5998492966     -1.7239748573                 
C       -0.1920191558      0.4521297103     -3.1593476518                 
H       -1.2459400650      0.1922103320     -3.2702930322                 
C        0.4958282459      0.8530827960     -4.2642604513                 
H        0.8055185205      1.8945796073     -4.3476946333                 
C        0.8428870788     -0.0273849809     -5.3432858890                 
H        0.5263981677     -1.0680896425     -5.2452436143                 
H        0.8235597154     -1.0210634377      6.8773458414                 
C        0.3981206525     -1.1709127409      5.8776015935                 
H       -0.2298396980     -2.0687910934      5.9385117809                 
C        1.5153655202     -1.3929922288      4.8574574089                 
H        2.3232940700     -0.6612356146      5.0266533396                 
H        1.9824524587     -2.3749405719      5.0135036429                 
C        1.0714691562     -1.2815470060      3.4108690207                 
C        2.0534654609     -1.8986637300      2.4416389284                 
C       -0.0974341309     -0.6903872976      3.0481724647                 
C       -1.1115068884     -0.1420196901      4.0831860815                 
C       -1.6349297110      1.2450604630      3.6444113043                 
C       -2.3144778410     -1.1100370221      4.1996070960                 
C       -0.4437173700      0.0337203016      5.4664128003                 
H        0.2032671383      0.9222572325      5.4366615521                 
H       -1.2222935377      0.2405647217      6.2124679685                 
H        2.4264207320     -2.8507141722      2.8405076855                 
H        2.9366421455     -1.2574915439      2.3040317470                 
H        1.6226320585     -2.0855846354      1.4565891981                 
H       -2.2105202089      1.1989746355      2.7142287673                 
H       -0.8078543391      1.9473820712      3.4901374785                 
H       -2.2908937373      1.6597275520      4.4198227946                 
H       -2.8169666577     -1.2525191377      3.2363614219                 
H       -3.0585880096     -0.7085510440      4.8988524232                 
H       -2.0072268689     -2.0976045902      4.5582593102                 
C       -0.5350023662     -0.5626828985      1.6506597776                 
C        0.1994269463     -0.1760882917      0.5776763743                 
H       -1.5963753159     -0.7424246321      1.4702019064                 
C       -0.3406986184     -0.0613415882     -0.7517657157                 
H        1.2465788387      0.0908835363      0.7071980882                 
H       -1.3934161123     -0.3187192193     -0.8790675973                 
C        1.5245020046      0.3271461262     -6.4619376464                 
C        1.8291796857     -0.6457730547     -7.5063432468                 
H        1.8683700104      1.3469488487     -6.6221029229                 
O        2.4359153962     -0.3962351347     -8.5357047542                 
H        1.4585306348     -1.6771262535     -7.3006575790                 
'''
keywords['active_space_atoms'] = 8
keywords['basis'] = '6-31G*'
keywords['spin'] = 0 # in PySCF this is the number of unpaired electrons, not 2s+1
keywords['charge'] = 0
keywords['conv_tol_grad'] = 1e-5
keywords['output_name'] = '110'
keywords['spectrum'] = True
keywords["orthog"] = False

start = time.time()
e, mf, ec = presses.run_embed(keywords)
finish = time.time()-start
print('time elapsed: ', finish)
