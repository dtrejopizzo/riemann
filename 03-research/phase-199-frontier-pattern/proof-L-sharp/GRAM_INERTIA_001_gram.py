# GRAM_INERTIA_001 step 2 (numpy, NUMÉRICO): Gram G_{mm'} = W_ext(Zσ^(m), Zσ^(m')) on the Möbius lattice lines of p = g*_50,
# μ = 15, with the EXTERIOR_DATUM_001 pipeline: same ω-grid [1,48] Δω=0.002, same ρ_p column (min-leak gauge, Tate rows),
# same X-form discretisation (EXTERIOR_DATUM_001_analysis.py Xbil, summed over all dilate pairs = 'total'), same normalisation
# λ/SC²/W*. Line m column: ρ_m(ω) = 2∫ H(m u) cos(2πλωu) du = (2/m) Σ_v w_v h(v) cos(2πλωv/m) on the 14×900 GL cell nodes of
# [1/λ,λ] (h from step 1, arb). φ̂₀ column := ρ_p − Σ_m μ(m) ρ_m (exact identity D.1/D.2 restricted to the grid).
# Totals use the bilinear identity Σ_ij X_ij(r1,r2) = arch(ΣF1,ΣF2) + diag-tail term − ⟨Ψlog1,Ψ2⟩ − ⟨Ψ1,Ψlog2⟩ + A1B2 + A2B1.
import json,os,numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import digamma
SP=os.environ['SP']; OUTD=os.environ.get('OUTD','.')
D=json.load(open(f'{SP}/ed1/exterior_decomp_v2_OMX48_NP900.json')); HN=json.load(open(f'{SP}/gi/hnodes_NP900.json'))
mu=15; lam=np.sqrt(mu); c=2*np.pi*mu; SC=1e35; Wst=4.763466135565557e-70
mob=[0,1,-1,-1,0,-1,1,-1,0,0,1,-1,0,-1,1,1]
om=np.array(D['omega']); rho_p=np.array([float(r[0]) for r in D['rho']])*SC
v=np.array([float(x) for x in HN['v']]); w=np.array([float(x) for x in HN['w']]); h=np.array([float(x) for x in HN['h']])
cols={}
for m in range(1,15):
    acc=np.zeros(len(om))
    for i0 in range(0,len(om),1500):
        o=om[i0:i0+1500]; acc[i0:i0+1500]=(2/m)*np.cos(2*np.pi*lam*np.outer(o,v)/m)@(w*h)
    cols[m]=acc*SC
cols[0]=rho_p-sum(mob[m]*cols[m] for m in range(1,15))      # φ̂₀ (edge/φ₀ mode)
# ---- X-form, per column
NMAX=47
def Theta(t): return np.real(digamma(0.25+0.5j*t))-np.log(np.pi)
OMX=om[-1]; hs=np.pi/(8*c*OMX); S=np.log(OMX); s=np.arange(0,S,hs)+hs/2; ns=[n for n in range(1,NMAX+1) if n<OMX]
NF=1<<int(np.ceil(np.log2(8*len(s)))); tau=2*np.pi*np.arange(NF//2+1)/(NF*hs); dt=tau[1]; Th=Theta(tau); wq=np.full(len(tau),dt); wq[0]=dt/2; tauN=tau[-1]
kap=(np.log(tauN/(2*np.pi))+1)/(np.pi*tauN)
def phis_lists(r):
    spl=CubicSpline(om,r); return [np.where(n*np.exp(s)<=OMX,np.exp(s/2)*spl(np.minimum(n*np.exp(s),OMX)),0.0) for n in ns]
def pre_from_phis(P):
    Psi=sum(P); Psil=sum(np.log(n)*p for n,p in zip(ns,P))
    return dict(F=np.fft.rfft(Psi,NF)*hs,Psi=Psi,Psil=Psil,A=np.sum(Psi*np.exp(-s/2))*hs,B=np.sum(Psi*np.exp(s/2))*hs,P0=np.array([p[0] for p in P]))
def W(a,b):
    arch=np.sum(wq*Th*np.real(a['F']*np.conj(b['F'])))/np.pi+kap*np.dot(a['P0'],b['P0'])
    lg=-(np.dot(a['Psil'],b['Psi'])+np.dot(a['Psi'],b['Psil']))*hs
    return (arch+lg+a['A']*b['B']+b['A']*a['B'])*lam/SC**2/Wst
PL={k:phis_lists(r) for k,r in cols.items()}
pre={k:pre_from_phis(P) for k,P in PL.items()}
preP=pre_from_phis(phis_lists(rho_p))
res={'W(p) direct (pipeline total, EXTERIOR = 1.32681)':W(preP,preP),'W(p)/W* Galerkin (ROUGH)':1.232495}
res['sup|ρ_m| on [1,48] (×1e-35 units)']={m:float(np.abs(cols[m]).max()) for m in cols}
res['sup|ρ_p|']=float(np.abs(rho_p).max())
res['sup|ρ_m| on [4,48]']={m:float(np.abs(cols[m][om>=4]).max()) for m in cols}
keys_all=list(range(0,15)); G=np.array([[W(pre[a],pre[b]) for b in keys_all] for a in keys_all])
np.save(f'{OUTD}/G_all15.npy',G)
sqf=[0,1,2,3,5,6,7,10,11,13,14]; ix=[keys_all.index(k) for k in sqf]; Gs=G[np.ix_(ix,ix)]
def spec(M,labels):
    e,U=np.linalg.eigh(0.5*(M+M.T)); sc=np.abs(e).max()
    return dict(eig=e.tolist(),rel_eig=(e/sc).tolist(),inertia=[int((e>1e-12*sc).sum()),int((e<-1e-12*sc).sum()),int((abs(e)<=1e-12*sc).sum())],
                eigvec={f'{e[i]:.4e}':{str(l):round(float(U[j,i]),4) for j,l in enumerate(labels)} for i in range(len(e))})
res['G squarefree lines + φ0 (11x11)']=spec(Gs,sqf)
lines=[1,2,3,5,6,7,10,11,13,14]; il=[keys_all.index(k) for k in lines]
res['G lines only (10x10)']=spec(G[np.ix_(il,il)],lines)
vm=np.array([mob[k] if k else 1 for k in sqf],float)
res['vT G v, v=μ⊕1 (float, cancellation)']=float(vm@Gs@vm); res['|v|^2 * max|G|']=float(vm@vm*np.abs(Gs).max())
# combined column Σμρ_m+φ̂₀ re-assembled before the form (same as ρ_p up to float rounding): W of it
r_re=sum(mob[m]*cols[m] for m in range(1,15))+cols[0]; pr=pre_from_phis(phis_lists(r_re)); res['W(Σμρ_m+φ̂0) assembled first']=W(pr,pr)
# falsifier vectors (vector transport on the FIXED Gram; φ0 coefficient kept = 1, NOT a re-solved falsifier datum)
from math import comb
def gbin(c,k):
    out=1.0
    for i in range(k): out*=(c-i)/(i+1)
    return out
def muc(c,n):
    out=1.0; p=2
    while n>1:
        e=0
        while n%p==0: n//=p; e+=1
        if e: out*=(-1)**e*gbin(c,e)
        p+=1
    return out
fal={}
for c_ in (0.85,1.0,1.15):
    vv=np.array([1.0]+[muc(c_,m) for m in range(1,15)]); fal[f'μ_c c={c_}']=float(vv@G@vv)
vv=np.array([1.0]+[mob[m]*(m%2) for m in range(1,15)]); fal['μ without p=2 lines (a_2)']=float(vv@G@vv)
vv=np.array([1.0]+[mob[m]*(m%3!=0) for m in range(1,15)]); fal['μ without p=3 lines (a_3)']=float(vv@G@vv)
vv=np.array([0.0]+[mob[m] for m in range(1,15)]); fal['μ without φ0 (lines only)']=float(vv@G@vv)
res['falsifier vectors vT G v (/W*)']=fal
# ---- class (denominator a) decomposition: pair (line m, dilate n) belongs to class a = m/gcd(m,n)
from math import gcd
cls={}
for m in range(1,15):
    if mob[m]==0: continue
    for j,n in enumerate(ns):
        a=m//gcd(m,n); cls.setdefault(a,[np.zeros_like(s) for _ in ns]); cls[a][j]+=mob[m]*PL[m][j]
cls[0]=PL[0]; ck=sorted(cls)
pc={a:pre_from_phis(cls[a]) for a in ck}
K=np.array([[W(pc[a],pc[b]) for b in ck] for a in ck]); np.save(f'{OUTD}/K_classes.npy',K)
res['class Gram K (classes a incl. coefficients; 0 = φ0)']=spec(K,ck)
res['class diag K_aa']={a:float(K[i,i]) for i,a in enumerate(ck)}
res['class row sums (contribution of class a to total)']={a:float(K[i].sum()) for i,a in enumerate(ck)}
res['1T K 1']=float(K.sum())
cl_only=[i for i,a in enumerate(ck) if a]; res['class Gram without φ0']=spec(K[np.ix_(cl_only,cl_only)],[a for a in ck if a])
json.dump(res,open(f'{OUTD}/gram_inertia.json','w'),indent=1)
for k,x in res.items():
    if isinstance(x,dict) and 'eig' in x: print(k,'inertia(+,-,0)',x['inertia'],'eig',np.array(x['eig']).round(3))
    else: print(k,x)
