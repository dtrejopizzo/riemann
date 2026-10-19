# PRECHECK_T1_001 part 2: exterior continuation y_k(t) (regular solution of the prolate ODE at t=1, y(1)=1), t in [1,Ω0],
# + asymptotic series y = Re[B e^{ict} Σ β_m t^{-m-1}] for t ≥ Ω0. Double precision after an mp Frobenius start.
import mpmath as mp, numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicHermiteSpline
def frob(chi,c,us,K=300):
    mp.mp.dps=60; chi=mp.mpf(chi); c=mp.mpf(c); e=[mp.mpf(1)]
    for k in range(K):
        em1=e[k-1] if k>=1 else 0; em2=e[k-2] if k>=2 else 0
        e.append(((chi-c*c-k*(k+1))*e[k]-2*c*c*em1-c*c*em2)/(2*(k+1)**2))
    Y=[];YP=[]
    for u0 in us:
        u=mp.mpf(u0); Y.append(float(mp.fsum(e[k]*u**k for k in range(K+1)))); YP.append(float(mp.fsum(k*e[k]*u**(k-1) for k in range(1,K+1))))
        assert abs(e[K]*u**K)<1e-30*max(1,abs(Y[-1]))
    return np.array(Y),np.array(YP)
def asym_beta(chi,c,M=60):
    b=[1+0j]
    for m in range(1,M+1):
        bm1=b[m-1]; bm2=b[m-2] if m>=2 else 0; bm3=b[m-3] if m>=3 else 0
        b.append(-((-m*(m+1)+2*m+chi-c*c)*bm1-2j*c*(m-1)*bm2+(m-2)*(m-1)*bm3)/(2j*c*m))
    return np.array(b)
def wser(beta,c,t):
    m=np.arange(len(beta)); tt=np.asarray(t)[...,None]
    w=(beta*tt**(-m-1.)).sum(-1); wp=(beta*(-(m+1.))*tt**(-m-2.)).sum(-1)
    return w,wp   # y = Re[B e^{ict} w],  y' = Re[B e^{ict}(w'+icw)]
class Ext:
    def __init__(s,chi,c,Om,ppw=48):
        s.c=c; s.chi=chi
        f=lambda t,Y:[Y[1],(2*t*Y[1]-(chi-c*c*t*t)*Y[0])/(1-t*t)]
        dP=2*np.pi/ppw; PhM=c*np.sqrt(Om*Om-1)          # grid uniform in the Langer phase c*sqrt(t^2-1)
        s.t=np.sqrt(1+(np.arange(int(PhM/dP)+1)*dP/c)**2)
        nf=int(np.searchsorted(s.t,1+0.3/c))+1   # Frobenius on first nf points
        Y=np.empty(len(s.t)); Yp=np.empty(len(s.t))
        Y[:nf],Yp[:nf]=frob(chi,c,s.t[:nf]-1)
        sol=solve_ivp(f,(s.t[nf-1],s.t[-1]),[Y[nf-1],Yp[nf-1]],t_eval=s.t[nf-1:],method='DOP853',rtol=1e-13,atol=1e-300)
        Y[nf-1:]=sol.y[0]; Yp[nf-1:]=sol.y[1]
        s.spl=CubicHermiteSpline(s.t,Y,Yp); s.Om=s.t[-1]
        s.beta=asym_beta(chi,c)
        # fit B at several points near Om (consistency)
        Bs=[]
        for tm in s.t[-200::40]:
            w,wp=wser(s.beta,c,tm); E=np.exp(1j*c*tm)
            # y=Re[B E w], y'=Re[B E (wp+icw)]  -> solve for (Re B, Im B)
            a1=E*w; a2=E*(wp+1j*c*w)
            A=np.array([[a1.real,-a1.imag],[a2.real,-a2.imag]]); yv=s.spl(tm); ypv=s.spl(tm,1)
            x=np.linalg.solve(A,[yv,ypv]); Bs.append(x[0]+1j*x[1])
        s.B=Bs[-1]; s.Bspread=np.max(np.abs(np.array(Bs)-s.B))/abs(s.B)
    def __call__(s,t):
        t=np.asarray(t,float); out=np.empty_like(t); m=t<=s.Om
        out[m]=s.spl(t[m]); 
        if (~m).any():
            w,_=wser(s.beta,s.c,t[~m]); out[~m]=np.real(s.B*np.exp(1j*s.c*t[~m])*w)
        return out
