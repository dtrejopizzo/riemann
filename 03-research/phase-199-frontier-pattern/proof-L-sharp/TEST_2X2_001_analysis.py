# TEST_2X2_001 step 3 (double on data ×1e35; discretization of ROUGH_COMPLEMENT_001_analysis.py / TEST_BRIDGE_001_analysis.py):
# exterior 2×2 blocks for g* = p_J + δ_J (J = 1,2,3,5,10,20,50): a = X^{pp}, b = X^{δδ}, c = X^{pδ} = ½(X^{g*}−X^{pp}−X^{δδ}),
# each split into archimedean (Θ_∞), comb (−(log m+log n)⟨φ_m,φ_n⟩) and pole (A_mB_n+A_nB_m) parts; cancellation ratio
# Σ|parts|/|total|; positive majorant S = λ∫_1^{48}𝔴|ρ|² and θ'_ext = |c|/√(S(p)S(δ)).
import json,os,sys,numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import digamma
from scipy.integrate import simpson
SP=os.environ['SP']; D=json.load(open(f'{SP}/t2x2/exterior_OMX{os.environ.get("OMX","48")}_NP{os.environ.get("NP","900")}.json'))
G=json.load(open(os.path.join(os.path.dirname(__file__),'TEST_2X2_001_data','galerkin_2x2.json')))
mu=15; lam=np.sqrt(mu); c=2*np.pi*mu; SC=1e35; Wst=4.763466135565557e-70
om=np.array(D['omega']); rho=np.array([[float(x) for x in r] for r in D['rho']])*SC; names=D['names']
def wfun(o):
    o=np.asarray(o,float); N=int(np.floor(o.max()))+2; n=np.arange(1,N+1)
    Hc=np.concatenate([[0],np.cumsum(1/n)]); H1c=np.concatenate([[0],np.cumsum(np.log(n)/n)]); fl=np.floor(o).astype(int)
    with np.errstate(divide='ignore'): return Hc[fl]*np.log(mu*o**2/np.sqrt(o**2-1))-2*H1c[fl]
w=wfun(om[1:])
NMAX=47
def Theta(t): return np.real(digamma(0.25+0.5j*t))-np.log(np.pi)
OMX=om[-1]; h=np.pi/(8*c*OMX); S=np.log(OMX); s=np.arange(0,S,h)+h/2; ns=[n for n in range(1,NMAX+1) if n<OMX]
NF=1<<int(np.ceil(np.log2(8*len(s)))); tau=2*np.pi*np.arange(NF//2+1)/(NF*h); dt=tau[1]; Th=Theta(tau); wq=np.full(len(tau),dt); wq[0]=dt/2; tauN=tau[-1]
def Xparts(r):
    spl=CubicSpline(om,r); phis=[np.where(n*np.exp(s)<=OMX,np.exp(s/2)*spl(np.minimum(n*np.exp(s),OMX)),0.0) for n in ns]
    Fs=[np.fft.rfft(ph,NF)*h for ph in phis]; A=[np.sum(ph*np.exp(-s/2))*h for ph in phis]; B=[np.sum(ph*np.exp(s/2))*h for ph in phis]
    k=len(ns); AR=np.zeros((k,k)); LG=np.zeros((k,k)); PO=np.zeros((k,k))
    for i,m in enumerate(ns):
        for j in range(i,k):
            n=ns[j]; arch=np.sum(wq*Th*np.real(Fs[i]*np.conj(Fs[j])))/np.pi
            if i==j: arch+=phis[i][0]**2*(np.log(tauN/(2*np.pi))+1)/(np.pi*tauN)
            ip=np.sum(phis[i]*phis[j])*h
            AR[i,j]=AR[j,i]=arch; LG[i,j]=LG[j,i]=-(np.log(m)+np.log(n))*ip; PO[i,j]=PO[j,i]=A[i]*B[j]+A[j]*B[i]
    sc=lam/SC**2/Wst; return np.array([AR.sum(),LG.sum(),PO.sum()])*sc, np.array([np.trace(AR),np.trace(LG),np.trace(PO)])*sc
Smaj=lambda r: lam*simpson(w*r[1:]**2,x=om[1:])/SC**2/Wst
Xg,_=Xparts(rho[:,0]); out={'g*':{'arch,comb,pole':Xg.tolist(),'total':Xg.sum(),'S':Smaj(rho[:,0])}}
for J in (1,2,3,5,10,20,50):
    ip=names.index(f'v_p{J}'); idl=names.index(f'v_d{J}')
    Xp,dp=Xparts(rho[:,ip]); Xd,dd=Xparts(rho[:,idl]); Xc=0.5*(Xg-Xp-Xd)
    Sp=Smaj(rho[:,ip]); Sd=Smaj(rho[:,idl]); gj=G['J'][str(J)]
    cr=lambda X: float(np.abs(X).sum()/abs(X.sum()))
    rec={'a_ext=X^pp (arch,comb,pole)':Xp.tolist(),'a_ext':Xp.sum(),'a_gal':gj.get('W(p_J)/W*'),
         'b_ext=X^dd (arch,comb,pole)':Xd.tolist(),'b_ext':Xd.sum(),'b_gal':gj.get('W(δ_J)/W*'),
         'c_ext=X^pd (arch,comb,pole)':Xc.tolist(),'c_ext':Xc.sum(),'c_gal':gj.get('W(p_J,δ_J)/W*'),
         'cancel ratio Σ|parts|/|total| (a,b,c)':[cr(Xp),cr(Xd),cr(Xc)],'S(p)':Sp,'S(δ)':Sd,
         "θ'_ext=|c|/√(S(p)S(δ))":abs(Xc.sum())/np.sqrt(Sp*Sd),'a/S(p)':Xp.sum()/Sp,'b/S(δ)':Xd.sum()/Sd,
         'RC margin 1-θ\'/√((a/S_p)(b/S_δ))':1-abs(Xc.sum())/np.sqrt(Sp*Sd)/np.sqrt(abs(Xp.sum()/Sp*Xd.sum()/Sd)),
         'one-sided mass ρ_δ / ρ_g*':simpson(rho[:,idl]**2,x=om)/simpson(rho[:,0]**2,x=om)}
    out[J]=rec; print(J,json.dumps(rec,default=float),flush=True)
json.dump(out,open(os.path.join(os.path.dirname(__file__),'TEST_2X2_001_data',f'exterior_2x2_OMX{int(OMX)}.json'),'w'),indent=1,default=float)
