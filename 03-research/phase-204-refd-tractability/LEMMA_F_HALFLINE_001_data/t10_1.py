# LEMMA_F_HALFLINE_001 T10.1 (NUMERICO): sign of F''(0)=2 lam int_1^X (S1^2+S0 S2) ds, S_j(s)=sum_{ns<=X} log^j n rho(ns),
# same discretisation as F0_TEST_001_data/step3_F.py (lam=sqrt15, rho(om)=r(lam om), y=log s, dy grid).
# Basis: 12 even modes f_j(u)=P_{2j}(u/lam)-P_{2j+2}(u/lam) on |u|<=lam (vanish at the ends => r=O(xi^-2), admissible decay),
# r_j(xi)=Ff_j(xi) restricted to xi>lam.  Also: dilation counterexample rho=phi(om)+c phi(om/2). No gauge fixing (see memo).
import math,sys,json,numpy as np
from scipy.special import spherical_jn
lam=math.sqrt(15); X=float(sys.argv[1]) if len(sys.argv)>1 else 120; dy=float(sys.argv[2]) if len(sys.argv)>2 else 2e-5
def rho_mode(j,om):
    z=2*math.pi*lam*lam*om  # int_{-1}^1 P_k(t)cos(zt)dt = 2(-1)^{k/2} j_k(z)
    a=2*(-1)**j*spherical_jn(2*j,z); b=2*(-1)**(j+1)*spherical_jn(2*j+2,z); return lam*(a-b)
def phi(om,c0=1.5,w=0.04): t=(om-c0)/w; return np.where(np.abs(t)<1,np.exp(-1/np.maximum(1-t*t,1e-300)),0.0)
def bump_ex(c): return lambda om: phi(om)+c*phi(om/2)
funcs=[(lambda om,j=j: rho_mode(j,om)) for j in range(12)]+[bump_ex(c) for c in (-0.05,-0.2,0.05)]
ys=np.arange(0,math.log(X)+dy/2,dy); s=np.exp(ys); wq=np.full(len(s),dy); wq[0]=wq[-1]=dy/2; wq*=s
K=len(funcs); S=np.zeros((3,K,len(s)))
for n in range(1,int(X)+1):
    a=n*s; k=np.searchsorted(a,X,side='right')
    if k==0: break
    l=math.log(n)
    for i,f in enumerate(funcs):
        v=f(a[:k])
        for p in range(3): S[p,i,:k]+=l**p*v
ip=lambda A,B: lam*(A*wq)@B.T
Q=2*(ip(S[1],S[1])+0.5*(ip(S[0],S[2])+ip(S[2],S[0])))   # F''(0) bilinear (symmetrised)
F0=ip(S[0],S[0]); F1=ip(S[0],S[1])+ip(S[1],S[0])
# Gram of r on (lam,inf): ell = int_lam^inf r^2 dxi = lam int_1^inf rho^2 dom
om=np.arange(1,400,2e-4); R=np.array([f(om) for f in funcs]); G=lam*(R*2e-4)@R.T
m=slice(0,12); from scipy.linalg import eigh
gw,gv=np.linalg.eigh(G[m,m]); keep=gw>1e-9*gw.max(); Wh=gv[:,keep]/np.sqrt(gw[keep])
kap,U=np.linalg.eigh(Wh.T@Q[m,m]@Wh); V=Wh@U; print('G eig',gw); print('diag G',np.diag(G)[:12])
rng=np.random.default_rng(204); rand=[]
for t in range(12):
    c=rng.standard_normal(12); rand.append(((c@Q[m,m]@c)/(c@G[m,m]@c), (c@F0[m,m]@c)/(c@G[m,m]@c)))
out=dict(X=X,dy=dy,kappa=kap.tolist(),diagQ_over_ell=(np.diag(Q)[:12]/np.diag(G)[:12]).tolist(),
 random_F2_over_ell=[r[0] for r in rand],random_F0_over_ell=[r[1] for r in rand],
 bump={str(c):dict(F0=F0[12+i,12+i],F1=F1[12+i,12+i],F2=Q[12+i,12+i],ell=G[12+i,12+i]) for i,c in enumerate((-0.05,-0.2,0.05))},
 vmin=V[:,0].tolist())
print(json.dumps(out,indent=1)); json.dump(out,open(f't10_1_X{int(X)}.json','w'),indent=1)
# check of the minimal direction with an independent, longer G-quadrature
v=np.array(out['vmin']); r=lambda w: sum(v[j]*rho_mode(j,w) for j in range(12))
o2=np.arange(1,2000,1e-4); ell2=lam*np.sum(r(o2)**2)*1e-4
print('vmin: F2=',v@Q[m,m]@v,' ell(400)=',v@G[m,m]@v,' ell(2000)=',ell2,' F0=',v@F0[m,m]@v,' F1=',v@F1[m,m]@v)
