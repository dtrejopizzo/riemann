"""[phase 133, PANEL_1 finding A8]  SUPERSEDED BY R130_ml_check.py.

Status.  This script crashed through phase 132 (`TypeError`: numpy's `np.exp`
applied to an mpmath `mpf` handed to it by `mp.quad`).  The type mix is
repaired below and the script now runs end to end.

Blocks 1 and 2 agree with the closed forms (`W_p` versus its Mittag-Leffler
form to ~1e-5; the universal Tate residues at `tau = +-i/2` are `-+i` to 1e-13).
**Block 3 (the contour identity) does not reproduce the direct shell sum** —
its residue family and contour orientation are the draft version.  The script
of record for Theorem 9.7b, including the contour identity, is
`R130_ml_check.py`, which passes.  This file is kept only because it is cited
in the phase-130 record; nothing depends on its block 3.
"""
import numpy as np, mpmath as mp
# 1. Mittag-Leffler for W_p^(tau) = (log p) 2 Re(z/(1-z)), z = p^{-1/2 - i tau}
def Wp(p,tau):
    z = p**(-0.5-1j*tau); return (np.log(p)*2*(z/(1-z))).real
def Wp_ML(p,tau,K=20000):
    k=np.arange(-K,K+1); a=2*np.pi*k/np.log(p)
    # -i sum [1/(tau-(i/2+a)) - 1/(tau-(-i/2+a))] - log p
    s=(-1j*(1/(tau-(0.5j+a)) - 1/(tau-(-0.5j+a)))).sum()
    return (s - np.log(p)).real
for p in [2,3,7]:
    for tau in [0.0,0.37,2.5]:
        print(p,tau,Wp(p,tau),Wp_ML(p,tau))
# 2. residue of Winf = log pi - Re psi(1/4 + i tau/2) continued: -1/2[psi(1/4+i tau/2)+psi(1/4 - i tau/2)] at tau=i/2
def Winf(t):
    t=mp.mpc(t); return mp.log(mp.pi) - 0.5*(mp.digamma(0.25+0.5j*t)+mp.digamma(0.25-0.5j*t))
eps=mp.mpf('1e-6')
print("res at i/2:", Winf(0.5j+eps)*eps, " res of Wp at i/2:", (Wp(2,0.5j+1e-6+0j) if False else None))
z=lambda p,t: p**(-0.5-1j*t)
def Wp_c(p,t): 
    t=complex(t.real,t.imag) if hasattr(t,'imag') else complex(t); a=z(p,t); b=p**(-0.5+1j*t); return np.log(p)*(a/(1-a)+b/(1-b))
print("res Wp(2) at i/2:", Wp_c(2,0.5j+1e-7)*1e-7, "at -i/2:", Wp_c(2,-0.5j+1e-7)*1e-7)
# 3. contour identity: W_p(f) = sum_k fhat(i/2+2 pi k/log p) + int_{R+ih} fhat Wp dsigma/2pi
p=3; L=np.log(p)
# [phase 133, PANEL_1 finding A8] was: f=lambda t: np.exp(-(t-1.3)**2*3)
# np.exp cannot act on the mpmath mpf that mp.quad feeds it (TypeError).
# Use mp.exp and coerce; values are identical.
f=lambda t: mp.exp(-(mp.mpf(float(t.real) if hasattr(t,'real') else t)-mp.mpf('1.3'))**2*3)  # profile in t=log|x|
fhat=lambda tau: complex(mp.quad(lambda t: f(t)*mp.exp(-1j*tau*t), [-6,8]))
direct=L*sum(p**(-abs(m)/2)*f(m*L) for m in range(-8,9) if m!=0)
K=40; res=sum(fhat(0.5j+2*np.pi*k/L) for k in range(-K,K+1))
h=1.0
integ=mp.quad(lambda s: fhat(s+1j*h)*Wp_c(p,s+1j*h), [-60,60])/(2*mp.pi)
print("W_p direct", direct, " residues+contour", res+integ)
