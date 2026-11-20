import sys, math, time, pickle, numpy as np, mpmath as mp
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import galerkin_mp as G
from prolate_defect import prolate
T=float(sys.argv[1]); Nb=int(sys.argv[2]); dps=int(sys.argv[3]); KMAX=int(sys.argv[4]) if len(sys.argv)>4 else 12
D=G.build(T,Nb,dps=dps,verbose=False)
mp.mp.dps=dps+20
Tm=D['T']; lam=mp.exp(Tm); NN=lam**2; c=2*mp.pi*NN
ks_e,De=prolate(c,dps=dps+20,parity=0,nfun=KMAX//2+1)
kmaxdeg=ks_e[-1]
def legvals(x):
    v=[mp.mpf(1),x]; a,b=v
    for k in range(2,kmaxdeg+1): a,b=b,((2*k-1)*x*b-(k-1)*a)/k; v.append(b)
    return v
sq=[mp.sqrt(k+mp.mpf(1)/2) for k in range(kmaxdeg+1)]
def psis(u):  # all even prolates at u in [-1,1]
    v=legvals(u); return [mp.fsum(d*sq[k]*v[k] for d,k in zip(dd,ks_e)) for dd in De]
nP=len(De)
xs,ws=G.gl_nodes(40)
bps=sorted(set([-Tm,Tm]+[Tm-mp.log(n) for n in range(2,int(NN)+1) if Tm-mp.log(n)>-Tm]))
al=[k*mp.pi/(2*Tm) for k in range(1,Nb+1)]; sT=1/mp.sqrt(Tm)
C=[[mp.mpf(0)]*Nb for _ in range(nP)]; nrm=[mp.mpf(0)]*nP
t0=time.time()
for a,b in zip(bps[:-1],bps[1:]):
    npan=int(float((b-a)/0.04))+1; h=(b-a)/npan
    for p in range(npan):
        lo=a+p*h
        for x,w in zip(xs,ws):
            t=lo+h*(x+1)/2; wt=w*h/2; et=mp.exp(t)
            g=[mp.mpf(0)]*nP; n=1
            while n*et<lam:
                vals=psis(n*et/lam)
                for i in range(nP): g[i]+=vals[i]
                n+=1
            g=[gi*mp.exp(t/2) for gi in g]
            s1=mp.sin(al[0]*(t+Tm)); c1=mp.cos(al[0]*(t+Tm)); s,cc=s1,c1
            for j in range(Nb):
                if j: s,cc=s*c1+cc*s1, cc*c1-s*s1
                for i in range(nP): C[i][j]+=wt*g[i]*s*sT
            for i in range(nP): nrm[i]+=wt*g[i]**2
print("quad time",round(time.time()-t0,1),flush=True)
pickle.dump(dict(T=T,Nb=Nb,C=[[mp.nstr(x,dps+15) for x in r] for r in C],nrm=[mp.nstr(x,dps+15) for x in nrm]),open(f'cache/eproj_T{T}_N{Nb}.pkl','wb'))
