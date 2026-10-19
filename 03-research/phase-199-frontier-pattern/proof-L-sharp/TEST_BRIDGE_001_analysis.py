# TEST_BRIDGE_001 step 4 (double precision on data scaled by 1e35; no cancellation at this stage):
#  (a) S = λ∫_1^∞ 𝔴_15(ω)|Πρ_v|² dω on [1,OMX] + tail bracket from the exact min-gauge leak (Parseval budget);
#  (b) θ_emp = 1 − b*²/(e₂ S*), C*/S* (P3a), with b*, e₂, C* from the Galerkin step;
#  (c) dilate decomposition of the Λ-free exterior form (E_001 Cor E.3) on ρ_v:  𝔔 = Σ_{m,n} X_mn,
#      X_mn = 𝒜(φ_m,φ_n) − (log m + log n)⟨φ_m,φ_n⟩ + A_mB_n + A_nB_m,  φ_n(s) = e^{s/2}ρ(n e^s) (s>0),  W_ext = λ𝔔.
import json,sys,os,numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import digamma
SP=os.environ['SP']; F=sys.argv[1]; GAL=os.environ.get('GAL',f'{SP}/tb/galerkin_rungs_QF1.5.pkl.json')
D=json.load(open(F)); G=json.load(open(GAL))
mu=15; lam=np.sqrt(mu); c=2*np.pi*mu; SC=1e35
om=np.array(D['omega']); rho=np.array([[float(x) for x in r] for r in D['rho']])*SC; names=D['names']
LK=np.array([[float(x.strip('[]').split('+/-')[0]) for x in r] for r in D['leak_bilinear']])*SC**2
def wfun(o):
    o=np.asarray(o,float); N=int(np.floor(o.max()))+2; n=np.arange(1,N+1)
    Hc=np.concatenate([[0],np.cumsum(1/n)]); H1c=np.concatenate([[0],np.cumsum(np.log(n)/n)]); fl=np.floor(o).astype(int)
    with np.errstate(divide='ignore'): return Hc[fl]*np.log(mu*o**2/np.sqrt(o**2-1))-2*H1c[fl]
def simpson(y,x):
    from scipy.integrate import simpson as S; return S(y,x=x)
w=wfun(om[1:]); OMX=om[-1]
def arb_mid(s): return float(s.strip('[').split('+/-')[0])
def mid(s):
    s=s.strip(); 
    return float(s.strip('[]').split('+/-')[0]) if '+/-' in s else float(s.strip('[]'))
out={}
for q,nm in enumerate(names):
    r=rho[:,q]; m1=simpson(r**2,om); mw=simpson(w*r[1:]**2,om[1:])
    # near ω=1 the weight has an integrable log singularity: handle [1,1.002] by the endpoint value (tiny correction)
    leak2=LK[q,q]; tot1=leak2/(2*lam)        # one-sided mass ∫_1^∞ρ² from the min-gauge leak (two-sided ℓ = 2λ∫_1^∞)
    tail=tot1-m1; wt_lo=wfun(np.array([OMX]))[0]; wt_hi=wfun(np.array([200.0]))[0]
    rec=dict(mass_1_OMX=m1,mass_total=tot1,tail_mass=tail,tail_frac=tail/tot1,
             S_1_OMX=lam*mw/SC**2,S_lo=lam*(mw+max(tail,0)*np.log(2*mu))/SC**2,S_tail_w24=lam*(mw+max(tail,0)*wt_lo)/SC**2,
             S_tail_w200=lam*(mw+max(tail,0)*wt_hi)/SC**2,leak_twosided=leak2/SC**2, wbar_1_OMX=mw/m1)
    key=None if nm=='g*' else nm[2:]
    if key is not None and key.startswith('low'):
        T=G['task1'][key[3:]]; C=mid(T['low-block core u_J: W/W*'])*4.763466135565557e-70; rec.update(C=C)
        for k in ('S_1_OMX','S_lo','S_tail_w24','S_tail_w200'): rec['C/'+k]=C/rec[k]
    elif key is not None:
        T=G['task1']['global'] if key=='glob' else G['task1'][str(key)]
        if key=='glob': e2=mid(T['e2']); b=0.0; C=mid(T['C*/W*'])*4.763466135565557e-70
        else: e2=mid(T['e2']); b=mid(T['b*']); C=mid(T['C*=W(v*)'])
        rec.update(e2=e2,b=b,C=C)
        for k in ('S_1_OMX','S_lo','S_tail_w24','S_tail_w200'):
            rec['theta_'+k]=1-b*b/(e2*rec[k]); rec['C/'+k]=C/rec[k]
    out[nm]=rec; print(nm,{k:('%.6g'%v) for k,v in rec.items()},flush=True)
# ---- (c) dilate decomposition on the core vectors
NMAX=int(os.environ.get('NMAX','8'))
def Theta(t): return np.real(digamma(0.25+0.5j*t))-np.log(np.pi)
res3={}
for q,nm in enumerate(names):
    if nm=='g*': continue
    spl=CubicSpline(om,rho[:,q])
    h=np.pi/(8*c*OMX); S=np.log(OMX); s=np.arange(0,S,h)+h/2; M=len(s)
    phis=[]; ns=[n for n in range(1,NMAX+1) if n<OMX]
    for n in ns:
        x=n*np.exp(s); ph=np.where(x<=OMX,np.exp(s/2)*spl(np.minimum(x,OMX)),0.0); phis.append(ph)
    NF=1<<int(np.ceil(np.log2(8*M))); Fs=[np.fft.rfft(ph,NF)*h for ph in phis]
    tau=2*np.pi*np.arange(NF//2+1)/(NF*h); dt=tau[1]; Th=Theta(tau); wq=np.full(len(tau),dt); wq[0]=dt/2
    A=[np.sum(ph*np.exp(-s/2))*h for ph in phis]; B=[np.sum(ph*np.exp(s/2))*h for ph in phis]
    tauN=tau[-1]; X=np.zeros((len(ns),len(ns))); parts={}
    for i,m in enumerate(ns):
        for j,n in enumerate(ns):
            if j<i: X[i,j]=X[j,i]; continue
            arch=np.sum(wq*Th*np.real(Fs[i]*np.conj(Fs[j])))/np.pi
            if i==j:  # jump tail beyond Nyquist: jumps at s=0 and at the truncation ω=OMX
                J0=phis[i][0]; arch+=J0**2*(np.log(tauN/(2*np.pi))+1)/(np.pi*tauN)
            ip=np.sum(phis[i]*phis[j])*h
            X[i,j]=arch-(np.log(m)+np.log(n))*ip+A[i]*B[j]+A[j]*B[i]
            if i==0 and n<=5: parts[(m,n)]=dict(arch=arch,log=-(np.log(m)+np.log(n))*ip,pole=A[i]*B[j]+A[j]*B[i],inner=ip)
    tot=X.sum(); diag=np.trace(X); off=tot-diag
    # resonant pairs (1,n)
    r1={f'(1,{n})':2*X[0,j]/SC**2*lam for j,n in enumerate(ns) if n>1}
    W=lambda x: x*lam/SC**2
    key=nm[2:]
    if key.startswith('low'): Cst=mid(G['task1'][key[3:]]['low-block core u_J: W/W*'])*4.763466135565557e-70
    else:
        T=G['task1']['global'] if key=='glob' else G['task1'][key]; Cst=(mid(T['C*/W*'])*4.763466135565557e-70)
    Sv=out[nm]['S_1_OMX']
    rec=dict(sum_all=W(tot),C_galerkin=Cst,ratio_sum_over_C=W(tot)/Cst,X11=W(X[0,0]),diag_n_ge2=W(diag-X[0,0]),offdiag=W(off),
             offdiag_over_S=W(off)/Sv,X11_over_S=W(X[0,0])/Sv,diag_over_S=W(diag)/Sv,
             resonant_1n=r1,resonant_1n_over_X11={k:v/W(X[0,0]) for k,v in r1.items()},
             nonresonant_offdiag=W(off)-sum(r1.values()),M=M,h=h,ns=ns,
             parts_rel_X11={f'{k}':{a:(b/X[0,0]) for a,b in v.items()} for k,v in parts.items()},
             A_tot=sum(A),B_tot=sum(B),X_first4_overS=(X[:4,:4]*lam/SC**2/Sv).tolist(),pole_total_over_S=W(2*sum(A)*sum(B))/Sv)
    res3[nm]=rec; print('dilate',nm,json.dumps(rec,default=float)[:1500],flush=True)
json.dump({'S':out,'dilate':res3},open(F.replace('.json','_analysis.json'),'w'),default=float,indent=1)
