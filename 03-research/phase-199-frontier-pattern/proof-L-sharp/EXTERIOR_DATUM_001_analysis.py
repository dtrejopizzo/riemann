# EXTERIOR_DATUM_001 step 2 (double on data ×1e35; X-matrix discretization = ROUGH_COMPLEMENT_001_analysis.py / TEST_BRIDGE):
# pointwise comparison ρ_p vs prolate tails, decomposition Δr = ρ_p − ρ_{pro04} into pieces, Möbius-jump model, and the
# (1,n) dilate resonances of every piece (quadratic X and bilinear cross terms by polarization).
import json,os,numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import digamma
from scipy.integrate import simpson
SP=os.environ['SP']; D=json.load(open(f'{SP}/ed1/exterior_decomp_v2_OMX48_NP900.json'))
mu=15; lam=np.sqrt(mu); c=2*np.pi*mu; SC=1e35; Wst=4.763466135565557e-70
fl=lambda x: float(x.strip('[]').split('+/-')[0])
om=np.array(D['omega']); R=np.array([[float(x) for x in r] for r in D['rho']])*SC; cols=D['cols']; C={k:R[:,i] for i,k in enumerate(cols)}
pT=fl(D['p(T)']); kap=pT/np.sqrt(lam)
jl={int(m):(fl(a)-fl(b)) for m,(a,b) in D['jumps_lam_over_m'].items()}   # f(λ/m−) − f(λ/m+)
mob=[0,1,-1,-1,0,-1,1,-1,0,0,1,-1,0,-1,1,1]
out={'p(T)':pT,'kappa0=p(T)/sqrt(lam)':kap,
     'μ(m)κ0 ×1e35':{m:mob[m]*kap*SC for m in range(1,15)},
     
     'pro_all(λ)':fl(D['pro_all(λ)']),'pro04(λ)':fl(D['pro04(λ)']),'tate_multipliers':D['tate_multipliers']}
p=C['p']; pro04=C['pro04']; pro8=C['pro8+']; tate=C['tate_shift']
dr=p-pro04; dr_in=C['inner_res']; dr_out=p-pro04-pro8-dr_in
# jump model: ρ_J(ω) = Σ_m J_m sin(cω/m)/(πλω)  (J_m = f(λ/m−) − f(λ/m+)); edge m=1 counted with the full value f(λ−)=κ0
def rhoJ(ms,Js): return sum(J*np.sin(c*om/m) for m,J in zip(ms,Js))/(np.pi*lam*om)
# J_m = μ(m)κ0 exactly (f₁ = Σ_{mu<λ} μ(m)(mu)^{-1/2}p(log mu): term m enters at u = λ/m with value μ(m)λ^{-1/2}p(T)); the
# printed node values have 20 digits only, so the analytic value is used; edge check: f(λ−) = jl[1] vs κ0.
out['edge check f(λ−)/κ0']=jl[1]/kap
Jm={m:mob[m]*kap for m in range(1,15)}
# junction u = 1/λ = λ/μ (filler | f₁): continuous to 20 digits; its 1e-35 jump J15 is fitted by least squares on Δr_out, ω ≥ 2
b15=np.sin(c*om/mu)/(np.pi*lam*om); mm=om>=2
_res=dr_out-rhoJ([m for m in Jm if m>1],[Jm[m]*SC for m in Jm if m>1])-(Jm[1]-out['pro_all(λ)'])*SC*np.sin(c*om)/(np.pi*lam*om)
J15=float(np.dot(_res[mm],b15[mm])/np.dot(b15[mm],b15[mm]))/SC; out['fitted junction jump J15 (u=1/λ) /κ0']=J15/kap
rJ_all=rhoJ(list(Jm)+[mu],[Jm[m]*SC for m in Jm]+[J15*SC])
rJ_int=rhoJ([m for m in Jm if m>1],[Jm[m]*SC for m in Jm if m>1])          # interior Möbius jumps only (absent from prolates)
edge_mis=(Jm[1]-out['pro_all(λ)'])*SC*np.sin(c*om)/(np.pi*lam*om)          # edge mismatch f(λ)−f_pro(λ)
pieces={'p':p,'pro04':pro04,'pro8+':pro8,'pro_all':pro04+pro8,'Δr':dr,'Δr_in(filler−pro)':dr_in,'Δr_out(E⁻¹p−pro)':dr_out,
        'jump_model_all':rJ_all,'jump_model_interior(m≥2)':rJ_int,'edge_mismatch':edge_mis,'Δr_out−jumpint−edge':dr_out-rJ_int-edge_mis,'tate_shift':tate,
        'p−jump_interior':p-rJ_int}
win=[(1,1.01),(1,1.118034),(1.118034,2),(2,4),(4,48)]
tab={}
for k,v in pieces.items():
    tab[k]={f'rms{a}-{b}':float(np.sqrt(np.mean(v[(om>=a)&(om<=b)]**2))) for a,b in win}
    tab[k]['one-sided mass ∫_1^48 ρ²']=float(simpson(v**2,x=om))
out['rms_table(×1e35)']=tab
# pointwise sample table ω ∈ (1,4)
sam=[1.002,1.01,1.05,1.118,1.2,1.5,1.9,2.0,2.24,2.5,3.0,3.5,4.0]
out['pointwise']={str(o):{k:float(pieces[k][np.argmin(abs(om-o))]) for k in ('p','pro04','Δr','jump_model_interior(m≥2)','Δr_out(E⁻¹p−pro)','Δr_in(filler−pro)')} for o in sam}
# correlation of Δr_out with the interior jump model, on windows
for a,b in [(1.118,2),(2,4),(4,48),(1,48)]:
    m=(om>=a)&(om<=b); x=dr_out[m]; y=rJ_int[m]+edge_mis[m]
    out[f'corr(Δr_out, jumpint+edge) on {a}-{b}']=float(np.dot(x,y)/np.sqrt(np.dot(x,x)*np.dot(y,y)))
    out[f'resid share 1−|Δr_out−model|²/|Δr_out|² on {a}-{b}']=float(1-np.sum((x-y)**2)/np.sum(x**2))
# ---- dilate matrices (as ROUGH_COMPLEMENT_001_analysis.py)
NMAX=47
def Theta(t): return np.real(digamma(0.25+0.5j*t))-np.log(np.pi)
OMX=om[-1]; h=np.pi/(8*c*OMX); S=np.log(OMX); s=np.arange(0,S,h)+h/2; ns=[n for n in range(1,NMAX+1) if n<OMX]
NF=1<<int(np.ceil(np.log2(8*len(s)))); tau=2*np.pi*np.arange(NF//2+1)/(NF*h); dt=tau[1]; Th=Theta(tau); wq=np.full(len(tau),dt); wq[0]=dt/2; tauN=tau[-1]
def phis_of(r):
    spl=CubicSpline(om,r); return [np.where(n*np.exp(s)<=OMX,np.exp(s/2)*spl(np.minimum(n*np.exp(s),OMX)),0.0) for n in ns]
def Xbil(r1,r2):
    P1=phis_of(r1); P2=phis_of(r2); F1=[np.fft.rfft(ph,NF)*h for ph in P1]; F2=[np.fft.rfft(ph,NF)*h for ph in P2]
    A1=[np.sum(ph*np.exp(-s/2))*h for ph in P1]; B1=[np.sum(ph*np.exp(s/2))*h for ph in P1]
    A2=[np.sum(ph*np.exp(-s/2))*h for ph in P2]; B2=[np.sum(ph*np.exp(s/2))*h for ph in P2]
    k=len(ns); X=np.zeros((k,k)); AR=np.zeros((k,k)); LG=np.zeros((k,k))
    for i,m in enumerate(ns):
        for j,n in enumerate(ns):
            arch=np.sum(wq*Th*np.real(F1[i]*np.conj(F2[j])))/np.pi
            if i==j: arch+=P1[i][0]*P2[j][0]*(np.log(tauN/(2*np.pi))+1)/(np.pi*tauN)
            ip=np.sum(P1[i]*P2[j])*h
            AR[i,j]=arch; LG[i,j]=-(np.log(m)+np.log(n))*ip
            X[i,j]=arch+LG[i,j]+A1[i]*B2[j]+A2[j]*B1[i]
    return X*lam/SC**2/Wst,AR*lam/SC**2/Wst,LG*lam/SC**2/Wst
def summ(X):
    X=0.5*(X+X.T); return dict(total=X.sum(),X11=X[0,0],diag=np.trace(X),**{f'(1,{n})':2*X[0,j] for j,n in enumerate(ns) if n in (2,3,4,5,6,7)},
        offdiag_all=X.sum()-np.trace(X))
dil={}
for k in ('p','pro04','pro_all','pro8+','Δr','Δr_in(filler−pro)','Δr_out(E⁻¹p−pro)','jump_model_interior(m≥2)','jump_model_all','tate_shift'):
    X,AR,LG=Xbil(pieces[k],pieces[k]); r=summ(X); r['(1,2)/X11']=r['(1,2)']/r['X11']; r['(1,3)/X11']=r['(1,3)']/r['X11']; r['(1,5)/X11']=r['(1,5)']/r['X11']
    r['arch(1,2)']=2*AR[0,1]; r['comb(1,2)']=2*LG[0,1]; dil[k]=r; print(k,{a:round(float(b),4) for a,b in r.items()},flush=True)
# bilinear split of p's pairs: p = pro04 + Δr
Xpd,_,_=Xbil(pieces['pro04'],dr); Xpd=0.5*(Xpd+Xpd.T)
dil['cross pro04×Δr (enters ×2)']=summ(Xpd)
# who resonates with whom: pair (1,2) in X(a,b) is X_ab[0,1]+X_ab[1,0]; a in dilate 1, b in dilate 2
Xa,_,_=Xbil(pieces['pro04'],dr); Xb,_,_=Xbil(dr,pieces['pro04'])
dil['(1,2) split: pro04@dil1×Δr@dil2, Δr@dil1×pro04@dil2']=[2*Xa[0,1],2*Xb[0,1]]
for k in ('pro8+','Δr_in(filler−pro)','Δr_out(E⁻¹p−pro)','jump_model_interior(m≥2)','tate_shift'):
    Xa,_,_=Xbil(pieces['pro04'],pieces[k]); Xb,_,_=Xbil(pieces[k],pieces['pro04'])
    dil[f'(1,n) bilinear pro04@1 × {k}@n, and reverse']={str(n):[2*Xa[0,j],2*Xb[0,j]] for j,n in enumerate(ns) if n in (2,3,5)}
for k in dil: print(k,dil[k] if not isinstance(dil[k],dict) else {a:(round(float(b),4) if not isinstance(b,list) else [round(float(x),4) for x in b]) for a,b in dil[k].items()})
# S = λ∫𝔴ρ² (one-sided, to 48), as ROUGH
def wfun(o):
    N=int(np.floor(o.max()))+2; n=np.arange(1,N+1); Hc=np.concatenate([[0],np.cumsum(1/n)]); H1c=np.concatenate([[0],np.cumsum(np.log(n)/n)]); f=np.floor(o).astype(int)
    return Hc[f]*np.log(mu*o**2/np.sqrt(o**2-1))-2*H1c[f]
w=wfun(om[1:])
Sv={k:float(lam*simpson(w*pieces[k][1:]**2,x=om[1:])/SC**2/Wst) for k in ('p','pro04','pro_all','Δr','jump_model_interior(m≥2)')}
Sv['cross 2λ∫𝔴 pro04·Δr']=float(2*lam*simpson(w*pro04[1:]*dr[1:],x=om[1:])/SC**2/Wst)
out['S=λ∫𝔴ρ² /W* (to 48)']=Sv; out['W(p)/W* (Galerkin, ROUGH)']=1.232495; out['S(p)/W(p)']=Sv['p']/1.232495
out['dilate']=dil
# ---- ω-frequency (= u-position) attribution. ρ(ω) = ∫f(u)cos(2πλωu)du, so a singularity of f at u = λ/m is an ω-frequency
# line at 2πλ·λ/m = c/m. Band-pass ρ_p around c/m (m = 1..15; 15 ↔ junction u = 1/λ) on ω ∈ [ω₁,48] (Tukey taper):
#  (i) band powers (prediction: no line for μ(m) = 0, i.e. m = 4, 8, 9, 12, since f₁ = Σ μ(m)h(mu) has no term there);
#  (ii) dilation identity test ρ^{(m)}(ω) ≈ (μ(m)/m)·ρ^{(1)}(ω/m) (term m is μ(m)h(m·): same edge profile, dilated);
#  (iii) plain resonant overlaps P_n(a,b) = ∫ρ^{(a)}(ω)ρ^{(b)}(nω)dω (prediction: concentrated on b = n·a, sign μ(a)μ(na)).
def bands(r,w1):
    m_=om>=w1; x=om[m_]; y=r[m_].copy(); Nn=len(y); tw=np.ones(Nn); L0=int(0.02*Nn)
    tw[:L0]=0.5-0.5*np.cos(np.pi*np.arange(L0)/L0); tw[-L0:]=tw[:L0][::-1]
    Y=np.fft.rfft(y*tw,4*Nn); fr=2*np.pi*np.fft.rfftfreq(4*Nn,x[1]-x[0]); comp={}
    cen={m:c/m for m in range(1,16)}
    for m in range(1,16):
        lo=c/m-0.5*(c/m-c/(m+1)); hi=c/m+0.5*((c/(m-1) if m>1 else 1.5*c)-c/m)
        comp[m]=np.fft.irfft(np.where((fr>=lo)&(fr<hi),Y,0),4*Nn)[:Nn]
    comp['low']=np.fft.irfft(np.where(fr<c/15-0.5*(c/15-c/16),Y,0),4*Nn)[:Nn]
    comp['high']=np.fft.irfft(np.where(fr>=c+0.5*(1.5*c-c),Y,0),4*Nn)[:Nn]
    return x,comp,float(np.sum(y**2))
band={}
for w1 in (1.2,2.0):
    x,comp,tot=bands(p,w1); rec={}
    rec['band power share']={str(k):float(np.sum(v**2)/tot) for k,v in comp.items()}
    # (ii) dilation identity: compare ρ^{(m)}(ω) with (μ(m)/m)ρ^{(1)}(ω/m) on ω/m ≥ w1+0.3, ω ≤ 46
    c1=CubicSpline(x,comp[1]); dil_={}
    for m in range(2,15):
        sel=(x/m>=w1+0.3)&(x<=46)
        if sel.sum()<200: continue
        a=comp[m][sel]; b=c1(x[sel]/m)/m
        coef=float(np.dot(a,b)/np.dot(b,b)) if np.dot(b,b)>0 else None
        dil_[str(m)]={'μ(m)':mob[m],'fitted coefficient a in ρ^(m)(ω) ≈ a·ρ^(1)(ω/m)/m':coef,
                      'corr':float(np.dot(a,b)/np.sqrt(np.dot(a,a)*np.dot(b,b))),'rms ρ^(m) ×1e35':float(np.sqrt(np.mean(a**2)))}
    rec['dilation identity test']=dil_
    # (iii) plain resonant overlaps
    keys=list(range(1,16))
    for n in (2,3,5):
        sp={k:CubicSpline(x,comp[k]) for k in keys}; sel=(x>=w1)&(n*x<=48)
        P={f'{a},{b}':float(simpson(comp[a][sel]*sp[b](n*x[sel]),x=x[sel])) for a in keys for b in keys}
        full=float(simpson(p[(om>=w1)&(n*om<=48)]*CubicSpline(om,p)(n*om[(om>=w1)&(n*om<=48)]),x=om[(om>=w1)&(n*om<=48)]))
        resn=sum(v for k,v in P.items() if int(k.split(',')[1])==n*int(k.split(',')[0]))
        rec[f'overlap n={n}']={'full ∫ρ(ω)ρ(nω)':full,'Σ band pairs':sum(P.values()),'resonant (b=na) part':resn,
                               'top6':sorted(P.items(),key=lambda kv:-abs(kv[1]))[:6]}
    band[str(w1)]=rec; print('BAND',w1,json.dumps(rec,default=float)[:3000],flush=True)
out['band_attribution']=band
json.dump(out,open(f'{SP}/ed1/analysis.json','w'),indent=1,default=float)
print(json.dumps({k:v for k,v in out.items() if k!='dilate'},indent=1,default=float))
