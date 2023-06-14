import presses
import pyscf
import sys
import time

keywords = {}
keywords['scf_method'] = 'dft' # If dft is chosen, the user should specify the desired exchange-correlation functional
keywords['subsystem_method'] = 'mp2'
keywords['xc'] = 'b3lyp'
keywords['split_spade'] = True
keywords['atom'] = '''
    C            0.365661580116     0.342340264928    -1.842717453297
    H            1.418472424923     0.599849296647    -1.723974857314
    C           -0.192019155806     0.452129710304    -3.159347651786
    H           -1.245940065048     0.192210332049    -3.270293032234
    C            0.495828245864     0.853082795996    -4.264260451294
    H            1.549013189695     1.115788978869    -4.167452019657
    C           -0.092145835120     0.952562411812    -5.569771661921
    H           -1.148013180060     0.685462437993    -5.651291383421
    H            0.823559715401    -1.021063437731     6.877345841406
    C            0.398120652540    -1.170912740902     5.877601593484
    H           -0.229839697998    -2.068791093383     5.938511780941
    C            1.515365520151    -1.392992228802     4.857457408919
    H            2.323294069968    -0.661235614558     5.026653339551
    H            1.982452458663    -2.374940571886     5.013503642920
    C            1.071469156249    -1.281547006019     3.410869020687
    C            2.053465460886    -1.898663730011     2.441638928400
    C           -0.097434130932    -0.690387297584     3.048172464749
    C           -1.111506888379    -0.142019690123     4.083186081518
    C           -1.634929711043     1.245060462964     3.644411304316
    C           -2.314477841041    -1.110037022076     4.199607095968
    C           -0.443717369957     0.033720301602     5.466412800328
    H            0.203267138257     0.922257232541     5.436661552085
    H           -1.222293537718     0.240564721696     6.212467968471
    H            2.426420731958    -2.850714172159     2.840507685456
    H            2.936642145535    -1.257491543947     2.304031746951
    H            1.622632058470    -2.085584635406     1.456589198056
    H           -2.210520208899     1.198974635530     2.714228767280
    H           -0.807854339054     1.947382071178     3.490137478539
    H           -2.290893737279     1.659727552032     4.419822794624
    H           -2.816966657697    -1.252519137704     3.236361421856
    H           -3.058588009579    -0.708551043974     4.898852423205
    H           -2.007226868905    -2.097604590188     4.558259310219
    C           -0.535002366224    -0.562682898495     1.650659777605
    C            0.199426946265    -0.176088291724     0.577676374253
    H           -1.596375315925    -0.742424632149     1.470201906399
    C           -0.340698618402    -0.061341588202    -0.751765715725
    H            1.246578838743     0.090883536318     0.707198088213
    H           -1.393416112258    -0.318719219263    -0.879067597348
    C            0.552496156823     1.347802903716    -6.696667674505
    C           -0.136368205576     1.416667074286    -7.981543892815
    H            1.603907926459     1.627607098340    -6.684894091661
    O            0.380409259037     1.763345596398    -9.031657012068
    H           -1.211050721010     1.121293076565    -7.947070340357
'''
keywords['active_space_atoms'] = 8
keywords['basis'] = '6-31G*'
keywords['spin'] = 0 # in PySCF this is the number of unpaired electrons, not 2s+1
keywords['charge'] = 0
keywords['conv_tol_grad'] = 1e-5
keywords['output_name'] = '180'
keywords['spectrum'] = True

start = time.time()
e, mf, ec = presses.run_embed(keywords)
finish = time.time()-start
print('time elapsed: ', finish)
