# ρ_pro(ω) = √λ Σ_t C_t 2(−1)^t j_{2t}(30πω), C_t = Σ_k a_k β_{k,t} nf_t  (81 prolatas c=30π, gauge.json de F0_TEST_001).
# arb, recurrencia hacia adelante de j_n (radio controlado por arb). Dos versiones: pro04 (k=0,2 ↔ ψ0,ψ4) y pro_all. NUMÉRICO.
import json,math,sys,time
import numpy as np
from flint import arb,ctx
from multiprocessing import Pool
F0='/home/trabajo/Documentos/research/riemann/03-research/phase-200-sign-object/F0_TEST_001_data/'
PREC=int(sys.argv[1]) if len(sys.argv)>1 else 640
def setup():
    ctx.prec=PREC
    G=json.load(open(F0+'gauge.json')); a=[arb(x) for x in G['a_k']]; B=G['betas_prolate']; n=len(B[0])
    nf=[(arb(4*t+1)/2).sqrt() for t in range(n)]
    Call=[sum((a[k]*arb(B[k][t]) for k in range(len(a))),arb(0))*nf[t] for t in range(n)]
    C04=[(a[0]*arb(B[0][t])+a[2]*arb(B[2][t]))*nf[t] for t in range(n)]
    return Call,C04
CC=None
def work(oms):
    global CC
    if CC is None: CC=setup()
    ctx.prec=PREC; Call,C04=CC; n=len(Call); lam=arb(15).sqrt(); out=[]
    for om in oms:
        z=30*arb.pi()*arb(om); s,c=z.sin(),z.cos(); j=[s/z, s/(z*z)-c/z]
        for m in range(1,2*n): j.append((2*m+1)/z*j[m]-j[m-1])
        ra=2*lam.sqrt()*sum((Call[t]*(-1)**t*j[2*t] for t in range(n)),arb(0))
        r4=2*lam.sqrt()*sum((C04[t]*(-1)**t*j[2*t] for t in range(n)),arb(0))
        out.append((float(ra.mid())*1e35,float(ra.rad())*1e35,float(r4.mid())*1e35))
    return out
if __name__=='__main__':
    t0=time.time()
    Rs=json.load(open(F0+'rho_sigma.json')); sg=Rs['dsig']*np.arange(len(Rs['rho'])); oS=1+sg**2
    R1=json.load(open(F0+'rho.json')); o1=R1['omega0']+R1['dom']*np.arange(len(R1['rho']))
    R2=json.load(open(F0+'rho_60_240.json')); o2=R2['omega0']+R2['dom']*np.arange(len(R2['rho']))
    allo=[repr(float(x)) for x in np.concatenate([oS,o1,o2])]
    if len(sys.argv)>2: allo=allo[:int(sys.argv[2])]
    ch=[allo[i::200] for i in range(200)]
    with Pool(20) as P: R=P.map(work,ch)
    res=[None]*len(allo)
    for i,r in enumerate(R):
        for k,v in enumerate(r): res[i+k*200]=v
    res=np.array(res); np.save('rho_pro.npy',res); print(len(allo),'maxrad',res[:,1].max(),time.time()-t0)
    print(res[:5]); print([Rs['rho'][i] for i in range(5)])
