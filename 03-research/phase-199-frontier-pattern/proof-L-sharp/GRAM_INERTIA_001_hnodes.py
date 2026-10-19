# GRAM_INERTIA_001 step 1 (arb): values of h(v) = v^{-1/2} p(log v) on the SAME 14 Möbius cells × NP Gauss–Legendre nodes as
# EXTERIOR_DATUM_001_exterior.py (cell m: v ∈ [λ/(m+1), λ/m]; union = [1/λ, λ] = supp H). p = g*_50 (ROUGH pvecs), same
# Legendre normalisation (Cm). Output: nodes v, weights w, h(v) as strings (arb mid), for the numpy step 2.
import json,os,pickle,time
from pathlib import Path
from flint import arb,arb_mat,ctx
SP=Path(os.environ['SP']); ctx.prec=int(os.environ.get('PREC','320')); NP=int(os.environ.get('NP','900'))
mu=15; N=1664; I=list(range(0,N,2)); L=arb(mu).log()/2; lam=arb(mu).sqrt()
v=[arb(x) for x in pickle.load(open(SP/'rc'/'pvecs.pkl','rb'))['pvecs']['p']]
C=[arb(0)]*N
for t,j in enumerate(I): C[j]=v[t]*(arb(2*j+1)/(2*L)).sqrt()
def pval(x):
    xi=(x/L).mid(); P0,P1=arb(1),xi; s=C[0]
    for n in range(1,N):
        if n>1: P0,P1=P1,(((2*n-1)*xi*P1-(n-1)*P0)/n).mid()
        if n%2==0: s+=C[n]*P1
    return s
xs=[];ws=[]
for k in range(NP):
    x,w=arb.legendre_p_root(NP,k,weight=True); xs.append(x); ws.append(w)
out={'v':[],'w':[],'h':[],'cell':[]}; t0=time.time()
for m in range(1,15):
    lo=lam/(m+1); hi=lam/m; half=(hi-lo)/2; cen=(hi+lo)/2
    for x,w in zip(xs,ws):
        u=cen+half*x; out['v'].append(u.mid().str(30,radius=False)); out['w'].append((w*half).mid().str(30,radius=False))
        out['h'].append((pval(u.log())/u.sqrt()).mid().str(25,radius=False)); out['cell'].append(m)
    print('cell',m,time.time()-t0,flush=True)
out['p(T)/sqrt(lam)']=(pval(L)/lam.sqrt()).str(20)
json.dump(out,open(SP/'gi'/f'hnodes_NP{NP}.json','w'))
