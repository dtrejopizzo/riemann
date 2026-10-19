# LEMMA_I3_001: full block V_M = G_M (9-dim gauge, P2 pipeline) ⊕ span{Ψ_j} (compact bumps on the line).
# Computes P = arch+pol, Q = comb_Λ on all blocks; checks A_R⊥(1)=P_R⊥−Q_R⊥≈0; In(C_RR); quotient A_⊥⊥(1);
# Schur identity A(c) = Lᵀ[(1−c)C ⊕ (A⊥⊥(1)+(1−c)Q/C)]L.  NUMÉRICO (float64 + mpmath ζ dps 20).
import numpy as np, mpmath as mp, sys, json
from scipy.special import digamma
from numpy.polynomial import legendre as Lg, polynomial as Pn
mu=int(sys.argv[1]); J=int(sys.argv[2]) if len(sys.argv)>2 else 8; r=float(sys.argv[3]) if len(sys.argv)>3 else 3.0
lam=np.sqrt(mu); T=np.log(mu)/2
d=np.load(f'../P2_GAUGE_RADICAL_001_data/gauge_mu{mu}.npz'); C=d['C']; Mg,deg=C.shape
archRR=d['arch']; QRR=d['combL']; ABRR=d['AB']; G0RR=d['c0']
PRR=archRR+ABRR
# gauge A,B exactly as P2
mp.mp.dps=20
def phit(s,k): return lam**(-s)*sum(C[k,j]/(j+s) for j in range(deg) if C[k,j]!=0)
Ag=np.array([float(mp.diff(lambda s: phit(s,k),1)) for k in range(Mg)])
Bg=np.array([-0.5*float(sum(C[k,j]/j for j in range(1,deg))) for k in range(Mg)])
# complement Ψ_j(x)=w(y)P_j(y), y=(x-x0)/r, w=(1-y^2)^4, x0=-T
x0=-T
yq,wq=Lg.leggauss(600); xq=x0+r*yq; wx=wq*r
def Psi(y): 
    w=np.where(np.abs(y)<1,(1-y**2)**4,0.0); return np.array([w*Lg.legval(y,np.eye(J)[j]) for j in range(J)])
Pq=Psi(yq)                                   # J x nq
Apsi=Pq@(wx*np.exp(xq/2)); Bpsi=Pq@(wx*np.exp(-xq/2))
# S(v)=Σ_k φ_k(kv) for gauge basis, on log grid v∈[vmin,1/λ]
vs=np.exp(np.linspace(np.log(1e-5/lam),np.log(1/lam),6000))
Sv=np.zeros((Mg,len(vs)))
for i,v in enumerate(vs):
    kk=np.arange(1,int(1/(lam*v))+1); x=lam*kk*v; x=x[x<=1]
    V=np.vander(x,deg,increasing=True)       # nk x deg
    Sv[:,i]=(V@C.T).sum(0)
from scipy.interpolate import CubicSpline
Ssp=CubicSpline(np.log(vs),Sv,axis=1)
def S(v):
    v=np.asarray(v); out=np.zeros((Mg,)+v.shape); m=(v>=vs[0])&(v<=1/lam)
    out[:,m]=Ssp(np.log(v[m])); return out
# Φ_k(x)=e^{x/2}S(e^x); R_j(u)=u^{-1/2}Ψ_j(log u)
# L2 cross Gram <Φ_k,Ψ_j> = ∫Φ(x)Ψ(x)dx
Phq=np.exp(xq/2)*S(np.exp(xq))               # Mg x nq
G_Rp=(Phq*wx)@Pq.T; G_pp=(Pq*wx)@Pq.T
# primes
def mang(n):
    for p in range(2,int(n**0.5)+1):
        if n%p==0:
            m=n
            while m%p==0: m//=p
            return np.log(p) if m==1 else 0.0
    return np.log(n)
NC=int(sys.argv[4]) if len(sys.argv)>4 else 200000
v_n=[(n,2*mang(n)/np.sqrt(n)) for n in range(2,NC)]; v_n=[(n,v) for n,v in v_n if v>0]
# comb cross: ∫Φ(t)Ψ(t-log n)+∫Ψ(t)Φ(t-log n), times ½ (symmetrised bilinear) ; Ψ at nodes xq
QRp=np.zeros((Mg,J)); Qpp=np.zeros((J,J))
for n,v in v_n:
    L=np.log(n)
    # ∫Ψ(t)Φ(t-L)dt
    t=xq; X1=(np.exp((t-L)/2)*S(np.exp(t-L))*wx)@Pq.T
    # ∫Φ(t)Ψ(t-L)dt = ∫Φ(s+L)Ψ(s)ds
    X2=(np.exp((t+L)/2)*S(np.exp(t+L))*wx)@Pq.T
    QRp+=v*0.5*(X1+X2)
    if L<2*r:
        yy=(xq-L-x0)/r; Ps=Psi(yy)          # Ψ(t-L) at t=xq
        X=(Pq*wx)@Ps.T; Qpp+=v*0.5*(X+X.T)
# arch cross via Mellin side, same τ grid as P2
taus=np.concatenate([np.linspace(0,50,20001)[:-1],np.linspace(50,600,22001)])
wt=np.zeros(len(taus))
for a,b in [(0,20000),(20000,len(taus))]:
    h=taus[a+1]-taus[a]; wt[a:b]+=h; wt[a]-=h/2; wt[b-1]-=h/2
zeta=np.array([complex(mp.zeta(0.5+1j*t)) for t in taus])
mm=np.real(digamma(0.25+0.5j*taus))-np.log(np.pi)
s=0.5+1j*taus
Fh=np.array([zeta*lam**(-s)*sum(C[k,j]/(j+s) for j in range(deg) if C[k,j]!=0) for k in range(Mg)])
E=np.exp(1j*np.outer(taus,xq))              # Ψ̂(τ)=∫Ψe^{iτx}
Ph=(Pq*wx)@E.T                               # J x ntau
archRp=np.real((Fh*(wt*mm))@Ph.conj().T)/np.pi
archpp=np.real((Ph*(wt*mm))@Ph.conj().T)/np.pi
parsRp=np.real((Fh*wt)@Ph.conj().T)/np.pi    # Parseval check vs G_Rp
PRp=archRp+np.outer(Ag,Bpsi)+np.outer(Bg,Apsi)
Ppp=archpp+np.outer(Apsi,Bpsi)+np.outer(Bpsi,Apsi)
np.savez(f'block_mu{mu}_J{J}.npz',PRR=PRR,QRR=QRR,PRp=PRp,QRp=QRp,Ppp=Ppp,Qpp=Qpp,G_RR=G0RR,G_Rp=G_Rp,G_pp=G_pp,
         parsRp=parsRp,Ag=Ag,Bg=Bg,Apsi=Apsi,Bpsi=Bpsi)
print(json.dumps(dict(mu=mu,J=J,r=r,Parseval_Rp=float(np.abs(parsRp-G_Rp).max()/np.abs(G_Rp).max()),
  ARp1_max=float(np.abs(PRp-QRp).max()),PRp_max=float(np.abs(PRp).max()),QRp_max=float(np.abs(QRp).max())),indent=1))
