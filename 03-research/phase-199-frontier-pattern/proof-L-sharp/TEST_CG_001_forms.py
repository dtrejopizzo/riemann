# TEST_CG_001: converged Galerkin matrices of Q(F,F), Q(F0,F), 2AB, Gram on PW_mu data restricted to (1,inf).
# NUMERICO. Quadrature in float64; zeta/chi/digamma tables from TEST_CG_001_zeta_tables.py (mpmath dps=30).
# Usage: python3 TEST_CG_001_forms.py MU K J M N NODEFAC TABLE.npz OUT.npz [MR (radical exponent, default M)]
#  basis PW_mu : g_k(t) = t^2 (1-(t/mu)^2)^M P_{2k}(t/mu), k<K      (supp [-mu,mu], g(0)=0, g(mu)=0)
#  radical     : chi_j(t) = t^2 (1-t^2)^MR P_{2j}(t), j<J            (supp [-1,1]; generators of G_1 after ghat(0)=0)
#  rho = ghat|_(1,N+1), ghat(X) = 2 int_0^L g(t) cos(2 pi X t) dt.
# Forms (memo P, F): Q(U,V) line form, Theta = Re psi(1/4+i tau/2) - log pi;
#  Q(F,F) on Re s=1/2 directly; Q(F0_i,F_j) = R_i(0)[log(2pi)A_j + FL_j(1)] + I_c (P.2, right shift, c=3/2) with
#  integrand R_i(1-s)[(zeta'(s) - zeta(s) chi'/chi(s)) F_j(s) - zeta(s) FL_j(s)]  (= -chi(s)zeta'(1-s)F - zeta FL).
#  Tails beyond T added analytically from F ~ a/(s-1), FL ~ b/(s-1), R(1-s) ~ -rho(1)/s, a=sum rho(n), b=sum rho(n)log n.
import sys, numpy as np, time
from numpy.polynomial.legendre import leggauss, legval
MU=float(sys.argv[1]); K=int(sys.argv[2]); J=int(sys.argv[3]); M=int(sys.argv[4]); N=int(sys.argv[5])
NF=float(sys.argv[6]); TAB=np.load(sys.argv[7]); OUT=sys.argv[8]; MR=int(sys.argv[9]) if len(sys.argv)>9 else M
CUTS=[500.,1000.,2000.]
tau=TAB['tau']; wt=TAB['wt']; c=float(TAB['C']); TMAX=tau.max()
def P2(k,x): cf=np.zeros(2*k+1); cf[2*k]=1; return legval(x,cf)
funcs=[(MU,lambda t,k=k: t**2*(1-(t/MU)**2)**M*P2(k,t/MU)) for k in range(K)]+\
      [(1.0,lambda t,j=j: t**2*(1-t**2)**MR*P2(j,t)) for j in range(J)]
nb=len(funcs)
def ghat(X):
    out=np.zeros((nb,len(X)))
    for i,(L,g) in enumerate(funcs):
        P=int(np.ceil(2*np.pi*max(X.max(),1)*L/20))+2
        x,w=leggauss(48); tt=np.concatenate([(x+1)/2*L/P+p*L/P for p in range(P)]); ww=np.tile(w*L/(2*P),P)
        gv=g(tt)*ww
        for a in range(0,len(X),2000):
            out[i,a:a+2000]=2*np.cos(2*np.pi*np.outer(X[a:a+2000],tt))@gv
    return out
x,w=leggauss(200); g0=np.array([2*np.sum(g((x+1)/2*L)*w*L/2) for L,g in funcs])
# X nodes
Xs=[];Ws=[];Ix=[]
for n in range(1,N+1):
    m=int(np.ceil(NF*(TMAX*np.log1p(1/n)+2*np.pi*MU)))+30
    x,w=leggauss(m); Xs.append(n+(x+1)/2); Ws.append(w/2); Ix.append(np.full(m,n-1))
Xs=np.concatenate(Xs);Ws=np.concatenate(Ws);Ix=np.concatenate(Ix); lX=np.log(Xs)
t0=time.time(); V=ghat(Xs); Vw=V*Ws
rn=ghat(np.arange(1,N+1,dtype=float)); print("nodes",len(Xs),"ghat time",time.time()-t0,flush=True)
ns=np.arange(1,N+1,dtype=float)
Gram=Vw@V.T
a=rn.sum(1); b=rn@np.log(ns); rho1=rn[:,0]
# scalar functionals
Tn=lambda s: np.stack([np.bincount(Ix,weights=Vw[i]*np.exp(-s*lX),minlength=N) for i in range(nb)])  # int_n^{n+1} rho X^-s
I1=Tn(1.0); I0=Tn(0.0)
tail1=np.cumsum(I1[:,::-1],1)[:,::-1]; tail0=np.cumsum(I0[:,::-1],1)[:,::-1]   # int_n^inf
A=tail1.sum(1); B=(tail0/ns).sum(1); FL1=(tail1*np.log(ns)).sum(1); R0=I0.sum(1); R1=I1.sum(1)
# tau loop
def acc_init(): return {T:np.zeros((nb,nb)) for T in CUTS}
QF=acc_init(); C0c=acc_init(); C0l=acc_init(); C0o=acc_init()
lnn=np.log(ns)
def FFL(s):  # s: (m,) complex -> F, FL, R(s), X^{s-1}-integral R(1-s): each (m,nb)
    E=np.exp(-np.outer(s,lX))
    P=np.exp(np.outer(s-1,lnn)); Z=np.cumsum(P,1); Lc=np.cumsum(P*lnn,1)
    F=(E*Z[:,Ix])@Vw.T; FL=(E*Lc[:,Ix])@Vw.T; R=E@Vw.T
    return F,FL,R
t0=time.time(); CH=128
for a0 in range(0,len(tau),CH):
    tt=tau[a0:a0+CH]; ww=wt[a0:a0+CH]/np.pi; sl=slice(a0,a0+CH)
    # line
    s=0.5+1j*tt; F,FL,R=FFL(s); R1ms=np.conj(R)
    th=TAB['th'][sl]
    I=(th*ww)[:,None,None]*(np.conj(F)[:,:,None]*F[:,None,:]).real-ww[:,None,None]*((np.conj(F)[:,:,None]*FL[:,None,:]).real+(np.conj(FL)[:,:,None]*F[:,None,:]).real)
    z,zp,cl=TAB['zl'][sl],TAB['zpl'][sl],TAB['cll'][sl]
    H=(zp-z*cl)[:,None]*F-z[:,None]*FL
    Il=ww[:,None,None]*(R1ms[:,:,None]*H[:,None,:]).real
    F0=np.conj(z)[:,None]*R; F0L=-np.conj(zp)[:,None]*R
    Io=(th*ww)[:,None,None]*(np.conj(F0)[:,:,None]*F[:,None,:]).real-ww[:,None,None]*((np.conj(F0)[:,:,None]*FL[:,None,:]).real+(np.conj(F0L)[:,:,None]*F[:,None,:]).real)
    # contour Re s = c
    s=c+1j*tt; F,FL,_=FFL(s); _,_,R1ms=FFL(1-s)
    z,zp,cl=TAB['zc'][sl],TAB['zpc'][sl],TAB['clc'][sl]
    H=(zp-z*cl)[:,None]*F-z[:,None]*FL
    Ic=ww[:,None,None]*(R1ms[:,:,None]*H[:,None,:]).real
    for T in CUTS:
        msk=tt<T
        QF[T]+=I[msk].sum(0); C0l[T]+=Il[msk].sum(0); C0o[T]+=Io[msk].sum(0); C0c[T]+=Ic[msk].sum(0)
    if a0%(CH*40)==0: print("tau",tt[0],time.time()-t0,flush=True)
res=R0[:,None]*(np.log(2*np.pi)*A+FL1)[None,:]
out=dict(Gram=Gram,A=A,B=B,FL1=FL1,R0=R0,R1=R1,a=a,b=b,rho1=rho1,g0=g0,K=K,J=J,mu=MU)
for T in CUTS:
    LT=(np.log(T/(2*np.pi))+1)/T
    tQ=(np.outer(a,a)*LT-(np.outer(a,b)+np.outer(b,a))/T)/np.pi
    tC=np.outer(rho1,a*LT-b/T)/np.pi
    out['QF_%d'%T]=QF[T]; out['QFt_%d'%T]=QF[T]+tQ
    out['C0c_%d'%T]=C0c[T]+res; out['C0ct_%d'%T]=C0c[T]+res+tC
    out['C0l_%d'%T]=C0l[T]; out['C0lt_%d'%T]=C0l[T]+tC
    out['C0o_%d'%T]=C0o[T]; out['C0ot_%d'%T]=C0o[T]+tC
np.savez(OUT,**out); print("saved",OUT,time.time()-t0)
