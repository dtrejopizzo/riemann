# Pipeline check (exact zero): pure-gauge datum. f = gauge φ, supp ⊂ [−1/λ,1/λ], φ(0)=φ̂(0)=0, C² ⇒ Ef ≡ 0 on the window
# ⇒ W_T = 0 ⇒ 𝒲_ext[Zr_φ] = 0 (A_001 Thm 1.1). In ρ-units ρ(t)=ψ̂(t), ψ(y)=y²(1−y²)³(1−b y²), ∫ψ=0.
import numpy as np, numpy.polynomial.legendre as L, numpy.polynomial.polynomial as P
from scipy.special import spherical_jn
from scipy.interpolate import CubicHermiteSpline
import wext
pc=P.polymul(P.polymul([0,0,1],P.polypow([1,0,-1],3)),[1])
I=lambda p: P.polyval(1,P.polyint(p))-P.polyval(-1,P.polyint(p))
b=I(pc)/I(P.polymul(pc,[0,0,1])); pc=P.polymul(pc,[1,0,-b])
print('∫ψ =',I(pc),' ψ(0)=',P.polyval(0,pc))
lc=L.poly2leg(pc)
def rho(t,d=0):
    out=0
    for j,a in enumerate(lc):
        if abs(a)<1e-15 or j%2: continue
        # ∫_{-1}^1 P_j(y) e^{-2πiyt} dy = 2(-i)^j j_j(2πt)
        if d==0: out=out+a*2*(-1)**(j//2)*spherical_jn(j,2*np.pi*t)
        else: out=out+a*2*(-1)**(j//2)*spherical_jn(j,2*np.pi*t,derivative=True)*2*np.pi
    return out
for mu in [10,15]:
    Om=3000.; t=np.linspace(1,Om,3000000)
    class Cmb: pass
    C=Cmb(); C.c=2*np.pi; C.mu=mu; C.Om=Om; C.t=t; C.Y=rho(t); C.spl=CubicHermiteSpline(t,C.Y,rho(t,1)); C.b=np.zeros(3,complex)
    C.rho01=lambda tt: 0*tt; C.rho=lambda tt: np.where(tt<=Om,C.spl(np.minimum(tt,Om)),0.0)
    o,(s,phi,phil)=wext.evaluate(C,V=200,Q=2e4,h=np.pi/(4*2e4),verbose=False)
    print('mu',mu,'arch',o['arch'],'prime',o['prime'],'pole',o['pole'],'SUM 𝔔 =',o['Qform'],' ‖φ‖²',o['N2'],' rel',o['Qform']/o['arch'])
