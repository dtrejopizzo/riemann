"""
E69.1b -- gauge-free Nevanlinna detector, with the grid covering the off-line zero's z-image.

z-variable s=1/2+iz. A zero at s_rho = (1/2 - b) + i a  maps to z_rho = a + i b.
Plant an off-line zero at s = 20i  (Re=0, i.e. b=1/2, a=20) -> z_rho = 20 + 0.5 i (upper half).
Near z_rho, N(z) = -F'/F(z) ~ -1/(z - z_rho), whose Im goes NEGATIVE on one side -> violates
the Nevanlinna condition. True xi (RH) must keep Im N >= 0 throughout the upper half-plane.
"""
import mpmath as mp
mp.mp.dps=30
def xi(s): return 0.5*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def xi_planted(s, rho): return xi(s)*(s-rho)*(s-(1-rho))
def N(z, xifun):
    dlog = mp.diff(lambda w: mp.log(xifun(mp.mpf('0.5')+1j*w)), z)
    return -dlog
def scan(xifun, tag, ZR, ZI):
    mn=mp.inf; at=None
    for zr in ZR:
        for zi in ZI:
            im=float(mp.im(N(mp.mpf(str(zr))+1j*mp.mpf(str(zi)), xifun)))
            if im<mn: mn=im; at=(zr,zi)
    print(f"  [{tag}]  min Im N = {mn:+.4f}  at z={at}")
ZR=[16,18,20,22,24]; ZI=[0.1,0.3,0.5,0.8,1.2]
print("gauge-free Nevanlinna: Im N(z)>=0 on Im z>0 <=> RH; scanning near z=20+0.5i.\n")
scan(xi, "true xi (RH)", ZR, ZI)
scan(lambda s: xi_planted(s, 20j), "planted off-line zero at s=20i (z-image 20+0.5i)", ZR, ZI)
