# NUMERICO check for PROOF_L_SHARP_MM_001 (Barkhausen memo). Values of zeta only (no zero data).
import mpmath as mp
mp.mp.dps=30
# (1) Re zeta(1/2+it) takes negative values: first t on grid with Re<0
neg=[t for t in [k*0.05 for k in range(1,1200)] if mp.re(mp.zeta(mp.mpf(0.5)+1j*t))<0]
print("first t with Re zeta(1/2+it)<0:", neg[0] if neg else None)
# (2) Re zeta(sigma+it) <0 for sigma slightly >1 (van de Lune): scan sigma=1.1 over t
s=1.1; m=min((mp.re(mp.zeta(s+1j*t)),t) for t in range(1,20000,7)); print("min Re zeta(1.1+it) on coarse grid:",m)
# (3) local loop Re 1/(1-p^{-s}) >= 1/(1+p^{-sigma}) on Re s = 1/2
for p in [2,3,5]:
  print(p, min(mp.re(1/(1-mp.power(p,-(0.5+1j*t)))) for t in [k*0.01 for k in range(0,1000)]), 1/(1+p**-0.5))
# (4) archimedean symbol Theta(t)=Re psi(1/4+it/2)-log pi: sign change
f=lambda t: mp.re(mp.digamma(0.25+0.5j*t))-mp.log(mp.pi)
print("Theta(0)=",f(0)," root t0=",mp.findroot(f,8))
# (5) d/dsigma |Gamma_R zeta|^2 at sigma=1/2 vanishes
G=lambda s: mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
for t in [3,10,33.3]:
  print(t, mp.diff(lambda x: abs(G(x+1j*t))**2, 0.5))
