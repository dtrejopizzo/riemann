# Prime-free R-cell form regrouped by coprime ratio q=a/b: N=ka, N'=kb.
# Q[F] = sum_{(a,b)=1} Q_{a,b}[F] + 2A B ; Q_{a,b} = sum_k (k^2ab)^{-1/2}[Arch(G_ka,G_kb) - (log ka + log kb)<G_ka,G_kb>]
import os,sys; HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE+'/..')
import galerkin_mp as Gm, numpy as np, scipy.linalg as sl
from math import gcd
R=int(sys.argv[1]); Nb=int(sys.argv[2]); T=float(sys.argv[3])
ell=np.log(R); Dd=Gm.build(ell/2,Nb,dps=20,verbose=False,cache=False,errcheck=False)
f2n=lambda M: np.array([[float(M[i,j]) for j in range(Nb)] for i in range(Nb)])
Ar=f2n(Dd['Arch']); Pi=f2n(Dd['Pi'])
z=np.linspace(-ell/2,ell/2,20001)
bas=lambda zz: np.array([np.sin(k*np.pi*(zz+ell/2)/ell)/np.sqrt(ell/2) for k in range(1,Nb+1)])
E=bas(z); Tm={}
for N in range(1,R):
    zs=z-np.log(N); Es=np.where((zs>-ell/2)[None,:],bas(zs),0)
    Tm[N]=np.trapz(E[:,None,:]*Es[None,:,:],z,axis=2)   # unweighted shift+cut; G_N = N^{-1/2} Tm[N] F
G=sum(N**-0.5*Tm[N] for N in Tm)
xw=z-T-ell/2
a_=G.T@np.trapz(E*np.exp(xw/2)[None,:],z,axis=1); b_=G.T@np.trapz(E*np.exp(-xw/2)[None,:],z,axis=1)
Pol=np.outer(a_,b_)+np.outer(b_,a_)
Qdir=G.T@(Ar-Pi)@G+Pol
cls={}
for N in Tm:
  for M in Tm:
    g=gcd(N,M); a,b=N//g,M//g; key=(min(a,b),max(a,b))
    blk=(N*M)**-0.5*Tm[N].T@(Ar@Tm[M]-(np.log(N)+np.log(M))*Tm[M])
    cls[key]=cls.get(key,0)+blk
for k in cls: cls[k]=(cls[k]+cls[k].T)/2
Qpf=sum(cls.values())+Pol
ev=lambda M: np.linalg.eigvalsh((M+M.T)/2)
print(f'R={R} Nb={Nb} T={T}: |Qpf-Qdir|/|Qdir| = {np.abs(Qpf-Qdir).max()/np.abs(Qdir).max():.2e}; min eig Qdir {ev(Qdir)[0]:.4f}')
print(' comb identity |Pi_Lambda - prime-free comb|:', np.abs(G.T@Pi@G - sum((N*M)**-0.5*(np.log(N)+np.log(M))*Tm[N].T@Tm[M] for N in Tm for M in Tm)).max())
for k in sorted(cls):
    e=ev(cls[k]); print(f'  class q={k[0]}/{k[1]}: eig min {e[0]:+.4f} max {e[-1]:+.4f}  (#neg {np.sum(e<-1e-9)})')
# truncations by height and by prime support
def pset(n):
    s=set();p=2
    while n>1:
        while n%p==0: s.add(p); n//=p
        p+=1
    return s
for H in range(1,R):
    S=sum(v for k,v in cls.items() if k[1]<=H)
    print(f'  height<= {H}: min eig (no polar) {ev(S)[0]:+.4f}  (+polar) {ev(S+Pol)[0]:+.4f}')
primes=[p for p in range(2,R) if all(p%d for d in range(2,p))]
for P in [1]+primes:
    S=sum(v for k,v in cls.items() if all(p<=P for p in pset(k[0])|pset(k[1])))
    print(f'  q S-unit, primes<= {P}: min eig {ev(S+Pol)[0]:+.4f}')
# archimedean-only and comb-only of q=1 class (diagonal N=N')
