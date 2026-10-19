# TEST_BRIDGE_001 step 1: Legendre (Mori even basis, 832 modes, L=T=½log15) coefficients of the rungs E ψ_k, k = 0,4,...,KMAX,
# f = λ^{-1/2}ψ_k(u/λ), (Ef)(x) = e^{x/2} Σ_{n: n e^x ≤ λ} f(n e^x)  (inverse of the Möbius map of MECH Prop 3.1).
# Piecewise Gauss–Legendre on [log(λ/(n+1)), log(λ/n)], n=1..14; arb at PREC bits. Output: pickle of strings.
import json,sys,os,time,pickle
from pathlib import Path
from flint import arb,arb_mat,ctx
SP=Path(os.environ['SP']); OUT=SP/'tb'; DATA=Path(__file__).parent/'MORI15_EXTREMAL_001_data'
PREC=int(os.environ.get('PREC','360')); ctx.prec=PREC
KMAX=int(os.environ.get('KMAX','200')); QF=float(os.environ.get('QF','1.0'))
mu=15; L=arb(mu).log()/2; lam=arb(mu).sqrt(); pi=arb.pi(); c=2*pi*mu
N=1664; I=list(range(0,N,2)); d=len(I)
t0=time.time()
# ---- prolates (even block, normalised Legendre on [-1,1]), as MORI15_EXTREMAL_001_prolate_M28.py
n=300
diag=[];off=[]
for t in range(n):
    j=2*t
    diag.append(arb(j*(j+1))+c*c*(2*j*(j+1)-1)/((2*j+3)*(2*j-1)))
    off.append(c*c*(j+2)*(j+1)/((2*j+3)*(arb((2*j+1)*(2*j+5))).sqrt()))
import numpy as np
Md=np.diag([float(x) for x in diag])+np.diag([float(x) for x in off[:-1]],1)+np.diag([float(x) for x in off[:-1]],-1)
evd,evecd=np.linalg.eigh(Md)
def thomas(sig,rhs):
    a=[off[t-1] for t in range(1,n)]; b=[diag[t]-sig for t in range(n)]; cc=[off[t] for t in range(n-1)]
    cp=[arb(0)]*n; dp=[arb(0)]*n
    cp[0]=cc[0]/b[0]; dp[0]=rhs[0]/b[0]
    for i in range(1,n):
        den=b[i]-a[i-1]*cp[i-1]
        cp[i]=(cc[i]/den) if i<n-1 else arb(0); dp[i]=(rhs[i]-a[i-1]*dp[i-1])/den
    x=[arb(0)]*n; x[n-1]=dp[n-1]
    for i in range(n-2,-1,-1): x[i]=dp[i]-cp[i]*x[i+1]
    return x
P0h=[((-1)**t)*arb.fac_ui(2*t)/(arb(2)**(2*t)*arb.fac_ui(t)**2) for t in range(n)]
nf=[(arb(4*t+1)/2).sqrt() for t in range(n)]
ks=list(range(0,KMAX+1,4)); betas=[]; info={}
for k in ks:
    kk=k//2; sig=arb(evd[kk])*(1+arb(1e-9)); x=[arb(evecd[t,kk]) for t in range(n)]
    for it in range(16):
        x=thomas(sig,x); nr=sum(a*a for a in x).sqrt(); x=[(a/nr).mid() for a in x]
    Tx=[diag[t]*x[t]+(off[t-1]*x[t-1] if t>0 else 0)+(off[t]*x[t+1] if t<n-1 else 0) for t in range(n)]
    chi=sum(a*b for a,b in zip(x,Tx))
    res=sum((Tx[t]-chi*x[t])**2 for t in range(n)).sqrt()
    if x[0]<0: x=[-a for a in x]
    psi0=sum(x[t]*nf[t]*P0h[t] for t in range(n)); psi1=sum(x[t]*nf[t] for t in range(n))
    muk=arb(2).sqrt()*x[0]/psi0; lk=c/(2*pi)*muk*muk
    betas.append(x); info[k]=dict(chi=chi.str(30),psi0=psi0.str(125),psi1=psi1.str(125),one_minus=(1-lk).str(20),res=res.str(5),muk=muk.str(125))
print('prolates',time.time()-t0,flush=True)
Bm=arb_mat([[betas[q][t]*nf[t] for q in range(len(ks))] for t in range(n)])   # ψ_q(y)=Σ_t Bm[t,q] P_{2t}(y)
# ---- quadrature nodes on pieces
def gl(m):
    xs=[];ws=[]
    for k in range(m):
        x,w=arb.legendre_p_root(m,k,weight=True); xs.append(x); ws.append(w)
    return xs,ws
nodes=[]  # (x, weight, nmax); pieces split at equal arccos-steps (P_1662 oscillates like cos(1662 θ), x = L cos θ)
import math
DTH=float(os.environ.get('DTH','0.04'))/QF; NQ=int(os.environ.get('NQ','90'))
glc={}
for nn in range(1,15):
    lo=(lam/(nn+1)).log(); hi=(lam/nn).log()
    if nn==14: lo=-L
    if nn==1: hi=L
    tlo=math.acos(max(-1.0,min(1.0,float(hi/L)))); thi=math.acos(max(-1.0,min(1.0,float(lo/L))))
    ns=max(1,math.ceil((thi-tlo)/DTH))
    cuts=[hi]+[L*arb(math.cos(tlo+(thi-tlo)*i/ns)) for i in range(1,ns)]+[lo]
    if NQ not in glc: glc[NQ]=gl(NQ)
    xs,ws=glc[NQ]
    for a_,b_ in zip(cuts[1:],cuts[:-1]):
        h=(b_-a_)/2; ce=(b_+a_)/2
        for x,w in zip(xs,ws): nodes.append((ce+h*x,w*h,nn))
print('nodes',len(nodes),time.time()-t0,flush=True)
# prolate values at y = m e^x/λ
ys=[]; idx=[]
for qi,(x,w,nn) in enumerate(nodes):
    ex=x.exp()
    for m in range(1,nn+1): ys.append((m*ex/lam).mid()); idx.append(qi)
Prow=[]
for y in ys:
    P=[arb(1),y]
    for m in range(1,2*n-1): P.append((((2*m+1)*y*P[m]-m*P[m-1])/(m+1)).mid())
    Prow.append([P[2*t] for t in range(n)])
PV=arb_mat(Prow)*Bm   # len(ys) x nk
print('psi at nodes',len(ys),time.time()-t0,flush=True)
nk=len(ks)
Gv=[[arb(0)]*nk for _ in nodes]
for r,qi in enumerate(idx):
    for q in range(nk): Gv[qi][q]+=PV[r,q]
# times λ^{-1/2} e^{x/2} * weight
WG=[]
for qi,(x,w,nn) in enumerate(nodes):
    s=w*(x/2).exp()/lam.sqrt(); WG.append([Gv[qi][q]*s for q in range(nk)])
WG=arb_mat(WG)
# Legendre basis values φ_j(x)=sqrt((2j+1)/2L) P_j(x/L), even j
Lrows=[]
for (x,w,nn) in nodes:
    xi=(x/L).mid(); P0,P1=arb(1),xi; row=[P0]
    for m in range(1,N-1):
        P0,P1=P1,(((2*m+1)*xi*P1-m*P0)/(m+1)).mid()
        if (m+1)%2==0: row.append(P1)
    Lrows.append([row[t]*((arb(2*I[t]+1)/(2*L)).sqrt()) for t in range(d)])
PhiT=arb_mat(Lrows).transpose()
C=PhiT*WG   # d x nk Legendre coefficients of E ψ_k
print('coeffs',time.time()-t0,flush=True)
out={'ks':ks,'info':info,'coef':[[C[i,q].mid().str(110,radius=False) for q in range(nk)] for i in range(d)],
     'rad_max':max(float(C[i,q].rad()) for i in range(d) for q in range(nk)),'nodes':len(nodes),'QF':QF,'PREC':PREC}
pickle.dump(out,open(OUT/f'rungs_QF{QF}.pkl','wb'))
print('done',time.time()-t0,flush=True)
