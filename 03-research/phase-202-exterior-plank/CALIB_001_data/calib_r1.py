# CALIB_R1 (phase 202): decomposition by ratio classes of the exterior form (★★) at r* (Mori μ=15). NUMERICAL.
# Data: rho*.json from F0_TEST_001 (ρ(ω)=r*(λω)·1e35 from f* at arb 400/256 bits, min-leak gauge M=28).
# Quadratic units: 1e-70.  Conventions = F0_TEST_001 step3_F.py.
import json,math,sys,os,time
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import digamma
from sympy import factorint
F0=('/home/trabajo/Documentos/research/riemann/03-research/phase-200-sign-object/F0_TEST_001_data/')
lam=math.sqrt(15); binf=float(digamma(0.25))-math.log(math.pi)
X=float(os.environ.get('XC','240')); DY=float(os.environ.get('DY','1.5e-5')); NT=int(os.environ.get('NT','36'))
t0=time.time()
Rs=json.load(open(F0+'rho_sigma.json')); rs=np.array([float(x) for x in Rs['rho']])*1e35; sg=Rs['dsig']*np.arange(len(rs)); spS=CubicSpline(sg,rs)
R1=json.load(open(F0+'rho.json')); r1=np.array([float(x) for x in R1['rho']])*1e35; o1=R1['omega0']+R1['dom']*np.arange(len(r1)); sp1=CubicSpline(o1,r1)
R2=json.load(open(F0+'rho_60_240.json')); r2=np.array([float(x) for x in R2['rho']])*1e35; o2=R2['omega0']+R2['dom']*np.arange(len(r2)); sp2=CubicSpline(o2,r2)
def rho(x):
    x=np.asarray(x,float); out=np.zeros_like(x)
    m=x<2; out[m]=spS(np.sqrt(np.maximum(x[m]-1,0)))
    m=(x>=2)&(x<=60); out[m]=sp1(x[m]); m=(x>60)&(x<=240); out[m]=sp2(x[m]); return out
# fine table in u=log ω for fast interpolation
DU=2e-6; ug=np.arange(0,math.log(240)+DU,DU); rg=rho(np.exp(ug))
def rho_f(om): return np.where(om<=X,np.interp(np.log(np.maximum(om,1.0)),ug,rg),0.0)
print('tables',time.time()-t0,flush=True)
# ---------- combs: L_X = Λ_X * 1
NMAX=int(X)
def Lam_zeta(n):
    f=factorint(n); return math.log(list(f)[0]) if len(f)==1 else 0.0
LQ=json.load(open('/home/trabajo/Documentos/research/riemann/03-research/phase-200-sign-object/LEMMA_E_EPSTEIN_001_data/lambdaQ_exact.json'))
def Lam_Q(n):
    d=LQ.get(str(n)); 
    if not d: return 0.0
    from fractions import Fraction as Fr
    return float(sum(Fr(q)*math.log(int(p)) for p,q in d.items()))
# DH: a_n = Re chi(n)+kappa Im chi(n), chi(2)=i mod 5; b_n recursion (CERT_DH_001)
s5=math.sqrt(5); kap=(math.sqrt(10-2*s5)-2)/(s5-1); CHI={1:(1,0),2:(0,1),3:(0,-1),4:(-1,0),0:(0,0)}
def a_dh(n): re,im=CHI[n%5]; return re+kap*im
Bdh={}
for n in range(2,NMAX+1): Bdh[n]=a_dh(n)*math.log(n)-sum(a_dh(d)*Bdh[n//d] for d in range(2,n) if n%d==0)
COMBS={'zeta':{n:Lam_zeta(n) for n in range(2,NMAX+1)},'epstein':{n:Lam_Q(n) for n in range(2,NMAX+1)},'DH':{n:Bdh[n] for n in range(2,NMAX+1)}}
Lconv={k:np.array([0.0]+[sum(v[d] for d in range(2,n+1) if n%d==0) for n in range(1,NMAX+1)]) for k,v in COMBS.items()}
assert np.allclose(Lconv['zeta'][1:],np.log(np.arange(1,NMAX+1)))
# ---------- y-grid quantities (as step3)
ys=np.arange(0,math.log(X)+DY/2,DY); s=np.exp(ys); wq=np.full(len(s),DY); wq[0]=wq[-1]=DY/2; wq=wq*s
S0=np.zeros(len(s)); S1={k:np.zeros(len(s)) for k in COMBS}; rows=[]
for n in range(1,NMAX+1):
    a=n*s; k=np.searchsorted(a,X,side='right')
    if k==0: break
    rn=np.zeros(len(s)); rn[:k]=rho_f(a[:k]); S0+=rn
    for c in COMBS: S1[c]+=Lconv[c][n]*rn
    if n<=NT: rows.append(rn)
print('sums',time.time()-t0,flush=True)
A_tot=lam*np.sum(wq*S0); B_tot=np.sum(wq*S0/s)
def cfun(f,g):
    m=1<<int(math.ceil(math.log2(2*len(f)))); Ff=np.fft.rfft(f,m); Fg=np.fft.rfft(g,m)
    c1=np.fft.irfft(np.conj(Ff)*Fg,m)[:len(f)]*DY; c2=np.fft.irfft(np.conj(Fg)*Ff,m)[:len(f)]*DY; return 0.5*(c1+c2)
v=np.arange(len(s))*DY; nu=np.zeros(len(s)); nu[1:]=np.exp(-v[1:]/2)/(-np.expm1(-2*v[1:]))
V=v[-1]; tailnu=sum(math.exp(-(0.5+2*k)*V)/(0.5+2*k) for k in range(200))
def arch(f,g):
    c=cfun(f,g); c0=c[0]; integ=(c0-c)*nu; integ[0]=0
    return binf*c0+2*(np.sum(integ)-integ[-1]/2)*DY+2*c0*tailnu
sq=np.sqrt(lam*s)
PsiZ=sq*S0; Arch=arch(PsiZ,PsiZ)
ZZlog={c:lam*np.sum(wq*S0*S1[c]) for c in COMBS}
LHS={c:Arch+2*A_tot*B_tot-2*ZZlog[c] for c in COMBS}
res=dict(X=X,DY=DY,A=A_tot,B=B_tot,twoAB=2*A_tot*B_tot,Arch=Arch,normZ2=lam*np.sum(wq*S0*S0),ZZlog=ZZlog,LHS=LHS)
print(json.dumps(res,indent=1),flush=True)
# ---------- G(d)=<Zr, D_d Zr> = λ∫ S0(s) S0(ds) ds  (Z_log^X r = Σ_d Λ_X(d) D_d Zr)
spZ=None
G={}
for d in range(2,NMAX+1):
    k=np.searchsorted(s,X/d,side='right')
    if k<2: break
    S0d=np.interp(ys[:k]+math.log(d),ys,S0)
    G[d]=lam*np.sum(wq[:k]*S0[:k]*S0d)
res['G']=G; res['sum_Lambda_G']={c:sum(COMBS[c][d]*G[d] for d in G) for c in COMBS}
# ---------- pair matrix n<=NT: Gram P[m,n]=λ∫ρ(ms)ρ(ns)ds, arch, pole, full X matrix
k=len(rows); R=np.array(rows)
P=np.array([[lam*np.sum(wq*R[i]*R[j]) for j in range(k)] for i in range(k)])
An=np.array([lam*np.sum(wq*R[i]) for i in range(k)]); Bn=np.array([np.sum(wq*R[i]/s) for i in range(k)])
Psi=[sq*R[i] for i in range(k)]
AR=np.zeros((k,k))
for i in range(k):
    for j in range(i,k): AR[i,j]=AR[j,i]=arch(Psi[i],Psi[j])
print('arch matrix',time.time()-t0,flush=True)
ln=np.log(np.arange(1,k+1))
XM={c:AR+np.outer(An,Bn)+np.outer(Bn,An)-(np.outer(np.ones(k),Lconv[c][1:k+1])+np.outer(Lconv[c][1:k+1],np.ones(k)))*P for c in COMBS}
res['pairs']=dict(P=P.tolist(),I=(P*np.sqrt(np.outer(np.arange(1,k+1),np.arange(1,k+1)))).tolist(),AR=AR.tolist(),A_n=An.tolist(),B_n=Bn.tolist(),
                  XM={c:XM[c].tolist() for c in COMBS})
# ---------- angles
nr=lambda f: math.sqrt(np.sum(f*f)*DY)
Psi1=Psi[0]; Zl=sq*S1['zeta']; ang={}
for n in range(2,11):
    j=np.searchsorted(ys,math.log(X)-math.log(n),side='right')
    Dn=np.zeros(len(s)); Dn[:j]=np.interp(ys[:j]+math.log(n),ys,Psi1)
    DZ=np.zeros(len(s)); DZ[:j]=np.interp(ys[:j]+math.log(n),ys,Zl)
    ip=np.sum(Psi1*Dn)*DY; aA=arch(Psi1,Dn); a11=arch(Psi1,Psi1); ann=arch(Dn,Dn)
    ang[n]=dict(cosL2=ip/(nr(Psi1)*nr(Dn)),cosArch=(aA/math.sqrt(a11*ann) if a11>0 and ann>0 else None),arch11=a11,archnn=ann,
                cosL2_Z_DnZlog=np.sum(PsiZ*DZ)*DY/(nr(PsiZ)*nr(DZ)))
res['angles']=ang
json.dump(res,open(f'calib_r1_X{int(X)}.json','w'),indent=1,default=float)
print('done',time.time()-t0)
