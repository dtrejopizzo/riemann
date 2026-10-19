# TEST_KINKS_001 steps 2-3 (double, ×1e35; same ω-grid, gauge and X-matrix discretization as EXTERIOR_DATUM_001_analysis.py).
# Jet-tail kink model: jump at u0 = λ/m of f (left−right) J0,J1,J2 = μ(m)(h, m h', m² h'')(λ) (measured, jets.json) gives,
# by integration by parts of ρ(ω) = 2∫_0^λ f(u)cos(ku)du, k = 2πλω, the tail
#   K_m(ω) = 2[ J0 sin(k u0)/k + J1 cos(k u0)/k² − J2 sin(k u0)/k³ ]   (orders 0,1,2).
import json,os,numpy as np
from pathlib import Path
from scipy.interpolate import CubicSpline
from scipy.special import digamma
SP=os.environ['SP']; HERE=Path(__file__).parent; D=json.load(open(f'{SP}/ed1/exterior_decomp_v2_OMX48_NP900.json'))
JT=json.load(open(HERE/'TEST_KINKS_001_data'/'jets.json'))
mu=15; lam=np.sqrt(mu); c=2*np.pi*mu; SC=1e35; Wst=4.763466135565557e-70
fl=lambda x: float(x.strip('[]').split('+/-')[0])
om=np.array(D['omega']); R=np.array([[float(x) for x in r] for r in D['rho']])*SC; C={k:R[:,i] for i,k in enumerate(D['cols'])}
p=C['p']; pro04=C['pro04']; pro8=C['pro8+']; dr=p-pro04; dr_out=p-pro04-pro8-C['inner_res']
mob=[0,1,-1,-1,0,-1,1,-1,0,0,1,-1,0,-1,1,1]
k=2*np.pi*lam*om
Jm={int(m):[float(x)*SC for x in v['J0,J1,J2']] for m,v in JT['p']['jumps'].items()}
def Kterm(m,order):
    J0,J1,J2=Jm[m]; ph=k*lam/m; out=[2*J0*np.sin(ph)/k,2*J1*np.cos(ph)/k**2,-2*J2*np.sin(ph)/k**3]
    return sum(out[:order+1])
out={'jet ratios (u-units) h\'/h, h\'\'/h':[Jm[1][1]/Jm[1][0],Jm[1][2]/Jm[1][0]],
     'order-1/order-0 amplitude at ω (m·(h\'/h)/k)':{f'm={m},ω={w}':m*Jm[1][1]/Jm[1][0]/(2*np.pi*lam*w) for m in (2,7,14) for w in (1,2,8,48)},
     'order-2/order-0 amplitude':{f'm={m},ω={w}':m*m*Jm[1][2]/Jm[1][0]/(2*np.pi*lam*w)**2 for m in (2,7,14) for w in (1,2,8,48)}}
win=[(1,2),(2,4),(4,8),(8,48)]
def relL2(t,mdl,a,b):
    s=(om>a)&(om<b); return float(np.sqrt(np.sum((t[s]-mdl[s])**2)/np.sum(t[s]**2)))
def corr(t,mdl,a,b):
    s=(om>a)&(om<b); return float(np.dot(t[s],mdl[s])/np.sqrt(np.dot(t[s],t[s])*np.dot(mdl[s],mdl[s])))
def rms(v,a,b):
    s=(om>a)&(om<b); return float(np.sqrt(np.mean(v[s]**2)))
models={}
for o in (0,1,2):
    models[f'ΣμK_m order≤{o} (m=2..14)']=sum(Kterm(m,o) for m in range(2,15) if mob[m])
# best scalar refit (does any rescaling of the order-0 / order-1 model help?)
cmp={}
for tn,t in (('Δr_out',dr_out),('Δr',dr)):
    for mn,mdl in models.items():
        cmp[f'{tn} vs {mn}']={f'({a},{b})':{'relL2':relL2(t,mdl,a,b),'corr':corr(t,mdl,a,b),'rms target':rms(t,a,b),'rms model':rms(mdl,a,b)} for a,b in win}
out['comparison']=cmp
# per-m order contributions rms in windows
out['rms of each order, m=2 and m=14']={f'm={m},order {o}':{f'({a},{b})':rms(Kterm(m,o)-(Kterm(m,o-1) if o else 0),a,b) for a,b in win} for m in (2,14) for o in (0,1,2)}
sam=[1.05,1.5,2.0,2.5,3.0,3.5,4.0,5.0,6.0,8.0]
out['pointwise']={str(w):{'Δr':float(dr[np.argmin(abs(om-w))]),'Δr_out':float(dr_out[np.argmin(abs(om-w))]),**{mn:float(v[np.argmin(abs(om-w))]) for mn,v in models.items()}} for w in sam}
# ---- dilate cross terms (X-matrix as EXTERIOR_DATUM_001_analysis.py)
NMAX=47
def Theta(t): return np.real(digamma(0.25+0.5j*t))-np.log(np.pi)
OMX=om[-1]; h=np.pi/(8*c*OMX); S=np.log(OMX); s=np.arange(0,S,h)+h/2; ns=[n for n in range(1,NMAX+1) if n<OMX]
NF=1<<int(np.ceil(np.log2(8*len(s)))); tau=2*np.pi*np.arange(NF//2+1)/(NF*h); dt=tau[1]; Th=Theta(tau); wq=np.full(len(tau),dt); wq[0]=dt/2; tauN=tau[-1]
def phis_of(r):
    spl=CubicSpline(om,r); return [np.where(n*np.exp(s)<=OMX,np.exp(s/2)*spl(np.minimum(n*np.exp(s),OMX)),0.0) for n in ns]
def Xbil(r1,r2,only=(0,)):   # rows i in `only` (dilate 1), all columns
    P1=phis_of(r1); P2=phis_of(r2); F1=[np.fft.rfft(ph,NF)*h for ph in P1]; F2=[np.fft.rfft(ph,NF)*h for ph in P2]
    A1=[np.sum(ph*np.exp(-s/2))*h for ph in P1]; B1=[np.sum(ph*np.exp(s/2))*h for ph in P1]
    A2=[np.sum(ph*np.exp(-s/2))*h for ph in P2]; B2=[np.sum(ph*np.exp(s/2))*h for ph in P2]
    X=np.zeros((len(ns),len(ns)))
    for i in range(len(ns)):
        for j,n in enumerate(ns):
            if i not in only and j not in only: continue
            arch=np.sum(wq*Th*np.real(F1[i]*np.conj(F2[j])))/np.pi
            if i==j: arch+=P1[i][0]*P2[j][0]*(np.log(tauN/(2*np.pi))+1)/(np.pi*tauN)
            X[i,j]=arch-(np.log(ns[i])+np.log(n))*np.sum(P1[i]*P2[j])*h+A1[i]*B2[j]+A2[j]*B1[i]
    return X*lam/SC**2/Wst
def pairs(r):
    X=Xbil(r,r); return {'X11':X[0,0],**{f'(1,{n})/X11':(X[0,j]+X[j,0])/X[0,0] for j,n in enumerate(ns) if n in (2,3,5)}}
dl={}
cands={'p (measured)':p,'pro04+Δr_out':pro04+dr_out}
for mn,mdl in models.items(): cands[f'pro04+{mn}']=pro04+mdl
for o in (0,1): cands[f'pro_all+ΣμK order≤{o}']=pro04+pro8+models[f'ΣμK_m order≤{o} (m=2..14)']
for kk,v in cands.items():
    dl[kk]=pairs(v); print(kk,dl[kk],flush=True)
# directional: prolate pro04 at dilate 1 × piece at dilate n
X11p=Xbil(p,p)[0,0]
for nm,v in [('Δr_out',dr_out)]+list(models.items()):
    Xa=Xbil(pro04,v)
    dl[f'directional pro04@1 × {nm}@n (/X11(p))']={str(n):2*Xa[0,j]/X11p for j,n in enumerate(ns) if n in (2,3,5)}
    print(nm,dl[f'directional pro04@1 × {nm}@n (/X11(p))'],flush=True)
out['dilate']=dl
# residual Δr_out − ΣμK (order 0) localisation
for o in (0,1):
    res=dr_out-models[f'ΣμK_m order≤{o} (m=2..14)']
    out[f'residual order≤{o}: rms by window']={f'({a},{b})':rms(res,a,b) for a,b in win+[(1,48)]}
out['Δr_out rms by window']={f'({a},{b})':rms(dr_out,a,b) for a,b in win+[(1,48)]}
json.dump(out,open(HERE/'TEST_KINKS_001_data'/'analysis.json','w'),indent=1,default=float)
print(json.dumps({a:b for a,b in out.items() if a not in ('pointwise',)},indent=1,default=float))
print(json.dumps(out['pointwise'],indent=1))
