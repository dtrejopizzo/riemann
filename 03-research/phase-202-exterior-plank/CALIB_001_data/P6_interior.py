# pairing interior: ΔW_X = −Σ_{n<15} 2(Λ_X(n)−Λ(n)) n^{-1/2} c_{g*}(log n), c de g* verdadero (arb 420 bits, como step1_comb). NUMÉRICO.
import json,sys,math
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-200-sign-object/F0_TEST_001_data')
from multiprocessing import Pool
import step1_comb as S
from flint import arb
if __name__=='__main__':
    with Pool(13) as P: R=P.map(S.task,list(range(2,15)))
    c={n:float(arb(a)) for n,a,_ in R}
    sys.argv=['x']; src=open('calib_r1.py').read(); ns={}
    exec("import json,math,numpy as np\nfrom sympy import factorint\nX=240.0\n"+src.split('# ---------- y-grid')[0].split('# ---------- combs: L_X = Λ_X * 1')[1],ns)
    C=ns['COMBS']; ext=json.load(open('calib_r1_X240.json'))['G']; out={'c_log_n':c}
    for x in ('epstein','DH'):
        dl={n:C[x][n]-C['zeta'][n] for n in range(2,15)}
        inter=-sum(2*dl[n]/math.sqrt(n)*c[n] for n in range(2,15))
        exter=-2*sum((C[x][int(d)]-C['zeta'][int(d)])*g for d,g in ext.items())
        exter14=-2*sum((C[x][int(d)]-C['zeta'][int(d)])*g for d,g in ext.items() if int(d)<15)
        out[x]=dict(interior_DeltaW=inter,exterior_DeltaLHS_all_d=exter,exterior_d_lt_15=exter14,
                    per_n={n:dict(dLam=dl[n],interior=-2*dl[n]/math.sqrt(n)*c[n],exterior=-2*dl[n]*ext[str(n)]) for n in range(2,15)})
        print(x,inter,exter,exter14)
    json.dump(out,open('P6_interior.json','w'),indent=1)
