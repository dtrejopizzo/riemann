# AUDIT_L_SHARP_14: numerical spot-check of CC_001 (prolate envelope, layer diagonal). Scale-invariant quantities only (psi(1)=1).
import numpy as np, mpmath as mp
from scipy.integrate import solve_ivp, quad
def theta_k(c,k,n=400):
    # Legendre tridiagonal (Bouwkamp) for -( (1-x^2)psi')' + c^2 x^2 psi = theta psi
    r=np.arange(n,dtype=float); d=r*(r+1)+c*c*(2*r*(r+1)-1)/((2*r+3)*(2*r-1))
    e=c*c*(r[:-2]+2)*(r[:-2]+1)/((2*r[:-2]+3)*np.sqrt((2*r[:-2]+1)*(2*r[:-2]+5)))
    par=k%2; idx=np.arange(par,n,2); A=np.diag(d[idx])+np.diag(e[idx[:-1]],1)+np.diag(e[idx[:-1]],-1)
    return np.sort(np.linalg.eigvalsh(A))[k//2]
def run(c,k,s0=None):
    th=theta_k(c,k); mp.mp.dps=60
    if s0 is None: s0=0.3/c**2*4
    # Taylor at s=t-1: 2(n+1)^2 a_{n+1} = -[n(n+1)+c^2-th]a_n -2c^2 a_{n-1} - c^2 a_{n-2}
    a=[mp.mpf(1)]; C=mp.mpf(c); T=mp.mpf(th)
    for n in range(0,400):
        am1=a[n-1] if n>=1 else 0; am2=a[n-2] if n>=2 else 0
        a.append(-((n*(n+1)+C**2-T)*a[n]+2*C**2*am1+C**2*am2)/(2*(n+1)**2))
    s=mp.mpf(s0); psi=sum(a[i]*s**i for i in range(len(a))); dpsi=sum(i*a[i]*s**(i-1) for i in range(1,len(a)))
    t0=1+s0; psi=float(psi); dpsi=float(dpsi)
    def f(t,y): # y=[psi, p psi', I1 mass, Iw layer]
        p=t*t-1; q=c*c*t*t-th; N=c/(2*np.pi)
        w=np.log(N*t*t/np.sqrt(p)) if t<2 else 0.0
        return [y[1]/p, -q*y[0], y[0]**2, w*y[0]**2]
    ts=np.concatenate([1+s0*np.logspace(0,np.log10(1/s0),4000)[:-1], np.linspace(2,60,20000)])
    ts=np.unique(ts); ts=ts[ts>=t0]
    sol=solve_ivp(f,(t0,ts[-1]),[psi,(t0*t0-1)*dpsi,0,0],t_eval=ts,rtol=1e-11,atol=1e-14,method='DOP853',max_step=0.002)
    t=sol.t; ps,pp=sol.y[0],sol.y[1]; p=t*t-1; q=c*c*t*t-th; P=p*q
    G=np.sqrt(P)*ps**2+pp**2/np.sqrt(P); E=G/np.sqrt(P)
    # G_inf: average of G at large t (G oscillates with amplitude ~rho)
    Ginf=np.mean(G[t>50]); x=np.log(G/Ginf); sig=(1.45/np.sqrt(p)+2.77)/c
    # tail beyond 60: mass ~ (Ginf/c)*(1/2)*int_60^inf dt/(t sqrt p)
    mass=sol.y[2][-1]+(Ginf/(2*c))*np.arcsin(1/t[-1])+ s0*1.0  # [1,t0] psi~1
    layer=sol.y[3][-1]
    N=c/(2*np.pi); Dl=2/3*np.log(4*N)-0.107689
    eta=layer/(mass*Dl)-1
    Cc2=Ginf/c; z=c*np.sqrt(p); m=z>=2
    env=np.max(np.abs(ps[m])/(np.sqrt(Cc2)*(t[m]**2*p[m])**-0.25))
    bz=np.max(np.abs(ps[t<=2])/(np.sqrt(Cc2*c)*(1+z[t<=2])**-0.5))
    nu=th/c**2
    e1b=0.77*nu+(5.14*np.log(c/2)+106.2)/c; etab=(21.4*np.log(c)+1.54*nu*c+523)/c/(1-e1b)
    print(f"c={c:.2f} k={k} theta={th:.3f} nu={nu:.4f}  Edecr={np.all(np.diff(E)<=1e-12*E[:-1])}  max|x|/sigma={np.max(np.abs(x)/sig):.3f}  max|x|(z>=2)={np.max(np.abs(x[m])):.4f}")
    print(f"   env ratio max(z>=2)={env:.4f} (claim 1.57)  Bessel-zone ratio={bz:.4f} (claim 10.3)  psi(1)^2/Ginf={1/Ginf:.3f} (claim<=35)")
    print(f"   C_c^2/((2/pi)(1-chi))-1 = {Cc2/((2/np.pi)*2*mass)-1:.5f}   layer eta_actual={eta:.5f}  claimed |eta|<= {etab:.3f}  e1bound={e1b:.3f}")
for c,k in [(2*np.pi*32,0),(2*np.pi*32,4),(2*np.pi*32,24),(2*np.pi*15,0),(2*np.pi*15,4),(2*np.pi*128,0),(2*np.pi*128,4)]:
    run(c,k)
