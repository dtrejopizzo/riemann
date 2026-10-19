# ROUGH_COMPLEMENT_001 step 3 (double on data ×1e35, as TEST_BRIDGE_001_analysis.py): for ρ_{g*}, ρ_p, ρ_δ (exterior OMX=48):
#  (1) ω-mass distribution of ρ_δ², prolate vs non-prolate share of the min-gauge leak, ω-spectrum (frequencies c/n);
#  (2) dilate matrices X^{pp}, X^{δδ}, cross X^{pδ} = ½(X^{g*} − X^{pp} − X^{δδ}) (polarization; E_001 Cor E.3 form);
#  (3) comb (log) parts −(log m + log n)⟨φ_m,φ_n⟩ per n ∈ {2,3,4,5,7} on pp, pδ, δδ (κ-derivative of the exterior form).
import json,os,sys,numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import digamma
from scipy.integrate import simpson
SP=os.environ['SP']; D=json.load(open(f'{SP}/rc/exterior_OMX48_NP900.json')); G=json.load(open(f'{SP}/rc/galerkin_J50.json'))
mu=15; lam=np.sqrt(mu); c=2*np.pi*mu; SC=1e35; Wst=4.763466135565557e-70
om=np.array(D['omega']); rho=np.array([[float(x) for x in r] for r in D['rho']])*SC; names=D['names']; print(names)
iq={'g*':0,'δ':names.index('v_delta'),'p':names.index('v_p')}
LK=np.array([[float(x.strip('[]').split('+/-')[0]) for x in r] for r in D['leak_bilinear']])*SC**2
ak=np.array([[float(x.strip('[]').split('+/-')[0]) for x in r] for r in D['a_k']])*SC; Dk=np.array([float(x.strip('[]').split('+/-')[0]) for x in D['one_minus_lam']])
out={'linearity_check_max|ρg−ρp−ρδ|/max|ρg|':float(np.max(np.abs(rho[:,0]-rho[:,iq['p']]-rho[:,iq['δ']]))/np.max(np.abs(rho[:,0])))}
def wfun(o):
    o=np.asarray(o,float); N=int(np.floor(o.max()))+2; n=np.arange(1,N+1)
    Hc=np.concatenate([[0],np.cumsum(1/n)]); H1c=np.concatenate([[0],np.cumsum(np.log(n)/n)]); fl=np.floor(o).astype(int)
    with np.errstate(divide='ignore'): return Hc[fl]*np.log(mu*o**2/np.sqrt(o**2-1))-2*H1c[fl], Hc[fl], H1c[fl]
w,Hw,H1w=wfun(om[1:])
for nm,q in iq.items():
    r=rho[:,q]; tot=LK[q,q]/(2*lam); rec={'one-sided mass total (leak/2λ)':tot}
    for a,b in [(1,1.01),(1,1.118034),(1,2),(2,4),(4,48)]:
        m=(om>=a)&(om<=b); rec[f'mass[{a},{b}]/total']=simpson(r[m]**2,x=om[m])/tot
    rec['tail(>48)/total']=1-simpson(r**2,x=om)/tot
    # diagonal ∫𝔴ρ² split: layer (1,2) vs cells ≥2, and the comb part −2H₁ (κ-sensitive diagonal)
    m2=om[1:]<2
    rec['S_layer(1,2)/W*']=lam*simpson(np.where(m2,w*r[1:]**2,0),x=om[1:])/SC**2/Wst
    rec['S_cells≥2 (to 48)/W*']=lam*simpson(np.where(~m2,w*r[1:]**2,0),x=om[1:])/SC**2/Wst
    rec['comb diag −2∫H₁ρ² (to 48)/W*']=-2*lam*simpson(H1w*r[1:]**2,x=om[1:])/SC**2/Wst
    pro=np.sum(ak[:,q]**2*Dk); rec['leak prolate share Σã²(1−λ)/leak']=pro/LK[q,q]; rec['leak non-prolate share']=1-pro/LK[q,q]
    a2=ak[:,q]**2; rec['prolate coef energy share k<=16, 16<k<=60, k>60']=[float(a2[:9].sum()/a2.sum()),float(a2[9:31].sum()/a2.sum()),float(a2[31:].sum()/a2.sum())]
    # ω-spectrum on [2,48]: power near angular frequencies c/n (ρ(ω)=∫f(u)cos(2πλωu)du, frequency 2πλu ≤ c)
    m=om>=2; x=om[m]; y=r[m]*x  # remove 1/ω envelope
    F=np.abs(np.fft.rfft(y*np.hanning(len(y)),8*len(y)))**2; fr=2*np.pi*np.fft.rfftfreq(8*len(y),x[1]-x[0]); Pt=F.sum()
    rec['ω-spectrum power share near c/n (±3%)']={f'c/{n}':float(F[np.abs(fr-c/n)<0.03*c/n].sum()/Pt) for n in (1,2,3,4,5,7)}
    rec['ω-spectrum power share freq<c/8']=float(F[fr<c/8].sum()/Pt); rec['ω-spectrum power share freq>1.03c']=float(F[fr>1.03*c].sum()/Pt)
    out[nm]=rec; print(nm,json.dumps(rec,default=float),flush=True)
# ---- dilate matrices (same discretization as TEST_BRIDGE_001_analysis.py)
NMAX=47
def Theta(t): return np.real(digamma(0.25+0.5j*t))-np.log(np.pi)
OMX=om[-1]; h=np.pi/(8*c*OMX); S=np.log(OMX); s=np.arange(0,S,h)+h/2; M=len(s); ns=[n for n in range(1,NMAX+1) if n<OMX]
NF=1<<int(np.ceil(np.log2(8*M))); tau=2*np.pi*np.arange(NF//2+1)/(NF*h); dt=tau[1]; Th=Theta(tau); wq=np.full(len(tau),dt); wq[0]=dt/2; tauN=tau[-1]
def Xmat(r):
    spl=CubicSpline(om,r); phis=[]
    for n in ns:
        xx=n*np.exp(s); phis.append(np.where(xx<=OMX,np.exp(s/2)*spl(np.minimum(xx,OMX)),0.0))
    Fs=[np.fft.rfft(ph,NF)*h for ph in phis]; A=[np.sum(ph*np.exp(-s/2))*h for ph in phis]; B=[np.sum(ph*np.exp(s/2))*h for ph in phis]
    k=len(ns); X=np.zeros((k,k)); AR=np.zeros((k,k)); LG=np.zeros((k,k)); PO=np.zeros((k,k))
    for i,m in enumerate(ns):
        for j in range(i,k):
            n=ns[j]; arch=np.sum(wq*Th*np.real(Fs[i]*np.conj(Fs[j])))/np.pi
            if i==j: arch+=phis[i][0]**2*(np.log(tauN/(2*np.pi))+1)/(np.pi*tauN)
            ip=np.sum(phis[i]*phis[j])*h
            AR[i,j]=AR[j,i]=arch; LG[i,j]=LG[j,i]=-(np.log(m)+np.log(n))*ip; PO[i,j]=PO[j,i]=A[i]*B[j]+A[j]*B[i]
    X=AR+LG+PO; return X,AR,LG,PO
sc=lambda x: x*lam/SC**2/Wst
Xs={nm:[sc(a) for a in Xmat(rho[:,q])] for nm,q in iq.items()}
cross=[0.5*(Xs['g*'][t]-Xs['p'][t]-Xs['δ'][t]) for t in range(4)]
Xs['pδ']=cross
gal={'pp':float(G['W(p)/W*'].strip('[]').split('+/-')[0]),'δδ':float(G['W(δ)/W*'].strip('[]').split('+/-')[0]),'pδ':float(G['W(p,δ)/W*'].strip('[]').split('+/-')[0])}
res={}
for key,nm in (('pp','p'),('pδ','pδ'),('δδ','δ'),('g*','g*')):
    X,AR,LG,PO=Xs[nm]; tot=X.sum(); dg=np.trace(X); r1={f'(1,{n})':2*X[0,j] for j,n in enumerate(ns) if n>1}
    rec=dict(total_ext=tot,galerkin=gal.get(key,1.0),X11=X[0,0],diag=dg,offdiag=tot-dg,resonant_1n={k:r1[k] for k in list(r1)[:6]},
             res_1n_over_X11={k:r1[k]/X[0,0] for k in list(r1)[:6]},nonres_offdiag=tot-dg-sum(r1.values()),
             arch_total=AR.sum(),comb_log_total=LG.sum(),pole_total=PO.sum(),
             comb_log_by_n={str(n):{'diag(n,n)':LG[j,j],'pair(1,n)':2*LG[0,j],'all pairs involving n':2*LG[j,:].sum()-LG[j,j]} for j,n in enumerate(ns) if n in (2,3,4,5,7)},
             arch_pair_1n={str(n):2*AR[0,j] for j,n in enumerate(ns) if n in (2,3,4,5,7)},
             inner_1n_corr={str(n):X[0,j]/np.sqrt(abs(X[0,0]*X[j,j])) if key!='pδ' else None for j,n in enumerate(ns) if n in (2,3,5)})
    res[key]=rec; print(key,json.dumps(rec,default=float),flush=True)
res['note']='units W*; pδ entries are the bilinear W(p,δ) pieces (W(g*) = pp + 2·pδ + δδ)'
res['check pp+2pδ+δδ vs g* (ext)']=res['pp']['total_ext']+2*res['pδ']['total_ext']+res['δδ']['total_ext']-res['g*']['total_ext']
json.dump({'rho':out,'dilate':res},open(f'{SP}/rc/analysis.json','w'),indent=1,default=float)
