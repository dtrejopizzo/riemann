# F0_TEST_001 step 1b: pole 2AB and prime comb sum_n 2Lambda(n) n^-1/2 c_g(log n) on g* at 420 bits (GL exact for polynomials).
import json,time
from pathlib import Path
from multiprocessing import Pool
from flint import arb,ctx
ctx.prec=420
DATA=Path('/home/trabajo/Documentos/research/riemann/03-research/phase-199-frontier-pattern/proof-L-sharp/MORI15_EXTREMAL_001_data')
E=json.load(open(DATA/'p0_eig.json')); V=[arb(arb(x).mid()) for x in E['vectors'][0]]
N=1664; L=arb(15).log()/2
coef=[arb(0)]*N
for t,j in enumerate(range(0,N,2)): coef[j]=V[t]*(arb(2*j+1)/(2*L)).sqrt()
def g_at(x):
    s_=(x/L).mid(); P0,P1=arb(1),s_; s=coef[0]
    for n in range(1,N-1):
        P0,P1=P1,(((2*n+1)*s_*P1-n*P0)/(n+1)).mid()
        if coef[n+1]!=0: s+=coef[n+1]*P1
    return s
NQ=1700
G=[arb.legendre_p_root(NQ,k,weight=True) for k in range(NQ)]
def task(n):
    ctx.prec=420
    if n==0:
        h=L; A=sum(w*g_at(h*x)*(h*x/2).exp() for x,w in G)*h; B=sum(w*g_at(h*x)*(-h*x/2).exp() for x,w in G)*h
        return n,A.str(100,radius=False),B.str(100,radius=False)
    u=arb(n).log(); lo=-L; hi=L-u; h=(hi-lo)/2; c=(hi+lo)/2
    cc=sum(w*g_at(c+h*x)*g_at(c+h*x+u) for x,w in G)*h
    return n,cc.str(100,radius=False),None
vm={2:2,3:3,4:2,5:5,7:7,8:2,9:3,11:11,13:13}
if __name__=='__main__':
    t0=time.time()
    with Pool(10) as P: R=P.map(task,[0]+list(vm))
    out={}
    tot=arb(0)
    for n,a,b in R:
        if n==0: A=arb(a);B=arb(b); out['A']=a; out['B']=b; out['pole 2AB']=(2*A*B).str(90,radius=False)
        else:
            w=2*arb(vm[n]).log()/arb(n).sqrt(); out[f'c(log {n})']=a; tot+=w*arb(a)
    out['comb']=tot.str(90,radius=False)
    s1=json.load(open('step1_arch_NQ110.json'))
    Q=arb(s1['arch_Omega'])+arb(s1['gamma(norm2-band)'])+2*A*B-tot
    out['Q_indep = arch_Omega + gamma(1-band) + pole - comb']=Q.str(30,radius=False)
    out['W* (Mori Galerkin, p0_eig)']='4.763466135565557249946609107758437122988e-70'
    out['time']=time.time()-t0
    json.dump(out,open('step1_comb.json','w'),indent=1); print(json.dumps(out,indent=1))
