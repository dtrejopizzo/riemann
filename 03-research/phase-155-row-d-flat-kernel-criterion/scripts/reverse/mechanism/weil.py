"""Prime-side Weil functional for real F supported in (-U,U):  W(F) = sum_rho |Fhat(gamma)|^2 (under RH)
  = pole + gamma + prime,   pole = 2 M+ M-  (M± = ∫F e^{±u/2}),  gamma = (1/2π)∫ m(τ)|Fhat|^2 dτ, m = Re ψ(1/4+iτ/2) - log π,
  prime = - Σ_n v_n (F*F~)(log n),  v_n = 2Λ(n)/√n.   Normalisation of phase-118 W0_weil_identity.py."""
import numpy as np
from math import log, sqrt, pi
from scipy.special import digamma
from scipy.integrate import quad
Z=np.loadtxt('/home/trabajo/Documentos/research/riemann/03-research/phase-155-row-d-flat-kernel-criterion/scripts/reverse/zeros1.txt')
def vm(N):
    lam=[0.0]*(N+1); s=[True]*(N+1)
    for p in range(2,N+1):
        if s[p]:
            for m in range(p*p,N+1,p): s[m]=False
            q=p
            while q<=N: lam[q]=log(p); q*=p
    return lam
class TestF:
    def __init__(self,U,coef,freqs,phases,n=4001):
        self.U=U; self.u=np.linspace(-U,U,n); u=self.u
        x=u/U; bump=np.where(abs(x)<1,np.exp(-1/np.clip(1-x*x,1e-300,None)),0.0)
        F=bump*sum(c*np.cos(f*u+p) for c,f,p in zip(coef,freqs,phases))
        self.F=F/np.sqrt(np.trapz(F*F,u)); self.du=u[1]-u[0]
    def Fhat(self,t):
        t=np.atleast_1d(t).astype(float)
        out=np.empty(t.size,dtype=complex)
        for i in range(0,t.size,2000):
            tt=t[i:i+2000]; out[i:i+2000]=(self.F[None,:]*np.exp(1j*np.outer(tt,self.u))).sum(1)*self.du
        return out
    def autocorr(self,a):   # ∫F(t)F(t+a)dt
        return np.trapz(self.F*np.interp(self.u+a,self.u,self.F,left=0,right=0),self.u)
    def parts(self):
        u,F=self.u,self.F
        Mp=np.trapz(F*np.exp(u/2),u); Mm=np.trapz(F*np.exp(-u/2),u); pole=2*Mp*Mm
        m=lambda t: digamma(0.25+0.5j*t).real-log(pi)
        # |Fhat|^2 decays fast (C_c^inf); integrate to 600 adaptively on a fine grid
        tau=np.linspace(0,600,240001); h=abs(self.Fhat(tau))**2
        gam=2*np.trapz(m(tau)*h,tau)/(2*pi)
        N=int(np.exp(2*self.U))+1; lam=vm(max(N,2))
        prime=-sum(2*lam[n]/sqrt(n)*self.autocorr(log(n)) for n in range(2,N+1) if lam[n]>0 and log(n)<2*self.U)
        return pole,gam,prime
    def zero_side(self,nz):
        return 2*(abs(self.Fhat(Z[:nz]))**2).sum()
if __name__=="__main__":
    rng=np.random.default_rng(3)
    for U in (0.30,0.55,0.70):
        f=TestF(U,rng.standard_normal(3),rng.uniform(0,6,3),rng.uniform(0,2*pi,3))
        po,ga,pr=f.parts(); print("U=%.2f pole %+.6f gamma %+.6f prime %+.6f  W=%.6f | zeros(1000) %.6f zeros(100000) %.6f"%(U,po,ga,pr,po+ga+pr,f.zero_side(1000),f.zero_side(100000)))
