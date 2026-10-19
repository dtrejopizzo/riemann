# PRECHECK_T1_001 main: exact Λ-free exterior form  𝔔[ρ] = 𝒜[φ] − 2⟨φ,φ_log⟩ + 2A B  (E_001 Cor E.3, ρ-units, U_001 §2)
#   φ(s) = e^{s/2} Σ_n ρ(n e^s), φ_log(s) = e^{s/2} Σ_n log n ρ(n e^s), s>0;  W_ext = λ 𝔔[ρ];  ∫_λ^∞|r|² = λ∫_1^∞ρ²
#   𝒜[φ] = (1/2π)∫ Θ_∞(τ)|Fφ(τ)|² dτ,  Θ_∞(τ) = Re ψ(1/4+iτ/2) − log π  (complete archimedean form incl. killing term)
#   A = ∫φ e^{−s/2}, B = ∫φ e^{s/2}.  No zeros, no Λ: only a_n ≡ 1 and log n.
import numpy as np, mpmath as mp, sys, json, pickle
from scipy.interpolate import CubicHermiteSpline
from scipy.special import psi as digamma, spherical_jn
from polyl import funcs
from ext import wser
def Theta(tau): return np.real(digamma(0.25+0.5j*tau))-np.log(np.pi)
def wfun(om,mu):   # 𝔴_μ(ω) = H(ω) log(μω²/√(ω²−1)) − 2 H₁(ω)
    om=np.asarray(om,float); N=int(np.floor(om.max()))+1; n=np.arange(1,N+1)
    Hc=np.concatenate([[0],np.cumsum(1/n)]); H1c=np.concatenate([[0],np.cumsum(np.log(n)/n)])
    fl=np.floor(om).astype(int)
    return Hc[fl]*np.log(mu*om**2/np.sqrt(om**2-1))-2*H1c[fl]
def D4(mu):        # D(μ)=∫𝔴 dm, m=(2/π)dω/(ω√(ω²−1)); substitute ω=sec θ: dm=(2/π)dθ
    th=np.linspace(0,np.pi/2,2000001)[1:-1]; om=1/np.cos(th)
    return np.trapz(wfun(om,mu),th)*2/np.pi + 0.0
class Combo:
    def __init__(s,D,coef):
        s.c=D['c']; s.mu=D['mu']; t=D['t']; s.Om=D['Om']
        Ss={k:D['k'][k]['S'] for k in coef}; s.scale=max(abs(mp.mpf(coef[k])*Ss[k]) for k in coef)
        w={k:float(mp.mpf(coef[k])*Ss[k]/s.scale) for k in coef}
        Y=sum(w[k]*D['k'][k]['Y'] for k in coef); Yp=sum(w[k]*D['k'][k]['Yp'] for k in coef)
        s.spl=CubicHermiteSpline(t,Y,Yp); s.t=t; s.Y=Y
        s.b=sum(w[k]*D['k'][k]['B']*D['k'][k]['beta'] for k in coef)   # ρ ~ Re[e^{ict} Σ b_m t^{-m-1}]
    def rho(s,t):
        t=np.asarray(t,float); out=np.empty_like(t); m=t<=s.Om
        out[m]=s.spl(t[m])
        if (~m).any():
            mm=np.arange(len(s.b)); tt=t[~m][:,None]
            out[~m]=np.real(np.exp(1j*s.c*t[~m])*(s.b*tt**(-mm-1.)).sum(-1))
        return out
    def rho01(s,t):
        e=np.exp(1j*s.c*t); return np.real(s.b[0]*e)/t+np.real(s.b[1]*e)/t**2
def evaluate(C,V=60.0,Q=None,h=None,verbose=True):
    c=C.c; mu=C.mu; Om=C.Om
    import os; QF=float(os.environ.get("QFAC","1")); HF=float(os.environ.get("HFAC","1"))
    if Q is None: Q=QF*max(2e5, 10*c*V)
    if h is None: h=np.pi/(4*max(c*Om,Q))/HF
    S=np.log(V); s=(np.arange(int(S/h))+0.5)*h; v=np.exp(s); M=len(s)   # midpoint grid (v=m/μ are resonances)
    th=c*v
    Li1,Li2,L1,L2=funcs(th)
    b0,b1,b2=C.b[0],C.b[1],C.b[2]
    sm=np.real(b0*Li1)/v+np.real(b1*Li2)/v**2
    sl=np.real(b0*L1)/v+np.real(b1*L2)/v**2
    # direct part: Σ_{n v ≤ Om} ρ_rest(nv)
    nmax=int(Om)
    for n in range(1,nmax+1):
        jn=np.searchsorted(v,Om/n,side='right')
        if jn==0: break
        tt=n*v[:jn]; rr=C.spl(tt)-C.rho01(tt)
        sm[:jn]+=rr; sl[:jn]+=np.log(n)*rr
    # remainder beyond n > Om/v : b2 term, geometric approximation
    N=np.floor(Om/v)+1; z=np.exp(1j*th); q=((N)/(N+1))**3
    T2=z**N*N**-3./(1-z*q); sm+=np.real(b2*T2)/v**3
    Nl=np.maximum(N,2.0); q2=(np.log(Nl+1)/np.log(Nl))*(Nl/(Nl+1))**3
    T2l=z**Nl*np.log(Nl)*Nl**-3./(1-z*q2)+np.where(N<2,0*z,0); sl+=np.real(b2*T2l)/v**3
    phi=np.exp(s/2)*sm; phil=np.exp(s/2)*sl
    wt=np.full(M,h)
    N2=np.sum(wt*phi**2); A=np.sum(wt*phi*np.exp(-s/2)); B=np.sum(wt*phi*np.exp(s/2)); P=np.sum(wt*phi*phil)
    # archimedean form by FFT
    NF=1<<int(np.ceil(np.log2(2*M)))
    F=np.fft.rfft(wt*phi/h,NF)*h; tau=2*np.pi*np.arange(len(F))/(NF*h); dtau=tau[1]
    sel=tau<=Q; Th=Theta(tau[sel]); E=np.abs(F[sel])**2
    arch_low=(np.sum(Th*E)*2-Th[0]*E[0])*dtau/(2*np.pi)
    pars_low=(np.sum(E)*2-E[0])*dtau/(2*np.pi)
    # singular tail: jumps at s=0, s=S and at θ=2πm (sawtooth from Im b0), logs from Re b0
    vm=2*np.pi*np.arange(int(np.ceil(c/(2*np.pi))),int(c*V/(2*np.pi))+1)/c; vm=vm[(vm>1)&(vm<V)]
    Csum=phi[0]**2+phi[-1]**2+np.sum((np.pi*b0.imag)**2/vm)+np.pi**2*np.sum((b0.real)**2/vm)
    arch_tail=Csum/np.pi*(np.log(Q/(2*np.pi))+1)/Q
    pars_tail=Csum/(np.pi*Q)
    arch=arch_low+arch_tail
    Qf=arch-2*P+2*A*B
    # norms of ρ and leading-order prediction
    tg=C.t; rg=C.Y; wg=wfun(tg[1:],mu)
    R2=np.trapz(rg**2,tg); Pw=np.trapz(wg*rg[1:]**2,tg[1:])
    t2=np.linspace(Om,40*Om,4000001); r2=C.rho(t2); R2+=np.trapz(r2**2,t2); Pw+=np.trapz(wfun(t2,mu)*r2**2,t2)
    # far tail (t>40 Om): ρ² ≈ |b0|²/(2t²) (+ |b1|²/2t⁴); 𝔴 ≈ log μ·log t + γ log(μ t) − 2γ₁ + ...
    T=40*Om; R2+=abs(b0)**2/(2*T); Pw+=abs(b0)**2/2*float(mp.quad(lambda x: (np.log(mu)+float(mp.euler))*mp.log(x)/x**2+float(mp.euler)*np.log(mu)/x**2,[T,mp.inf]))
    out=dict(mu=mu,c=c,V=V,Q=Q,h=h,M=M,N2=N2,A=A,B=B,pole=2*A*B,prime=-2*P,arch=arch,arch_tail=arch_tail,Qform=Qf,
             parseval=(pars_low+pars_tail)/N2,R2=R2,Pw=Pw,ratio=Qf/R2,pred=Pw/R2,b0=abs(b0),phi0=phi[0])
    if verbose: print({k:(float(x) if not isinstance(x,(int,)) else x) for k,x in out.items()},flush=True)
    return out,(s,phi,phil)
