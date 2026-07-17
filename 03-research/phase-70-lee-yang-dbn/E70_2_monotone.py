"""
E70.2 -- monotonicity of the Nevanlinna positivity under the dBN heat flow (true xi).

H_lambda(z) = int_0^inf e^{lambda u^2} Phi(u) cos(zu) du   (dBN flow; H_0 ~ xi, zeros at z=2 gamma_n).
N_lambda(z) = -H_lambda'(z)/H_lambda(z),  H_lambda'(z) = int e^{lambda u^2} Phi(u) (-u sin(zu)) du.
Omega_7-at-lambda <=> Im N_lambda(z) >= 0 on Im z > 0.  RH <=> holds at lambda=0 (Lambda<=0).

Test: min Im N_lambda over a grid in the upper half z-plane vs lambda. Expect: >=0 for lambda>=0,
threshold near lambda ~ 0 (Lambda ~ 0), dipping negative for lambda<0 -- i.e. the flow forces the
PROVEN direction (increasing lambda -> real zeros), not RH's needed Lambda<=0.
"""
import mpmath as mp
mp.mp.dps=18
def Phi(u,nmax=40):
    e4=mp.e**(4*u);e5=mp.e**(5*u);e9=mp.e**(9*u);s=mp.mpf(0)
    for n in range(1,nmax+1):
        t=(2*mp.pi**2*n**4*e9-3*mp.pi*n**2*e5)*mp.e**(-mp.pi*n**2*e4); s+=t
        if abs(t)<mp.mpf(10)**(-22) and n>4: break
    return s
def H(z,lam):  return mp.quadosc(lambda u: mp.e**(lam*u*u)*Phi(u)*mp.cos(z*u),[0,mp.inf],omega=abs(mp.re(z))+1)
def Hp(z,lam): return mp.quadosc(lambda u: mp.e**(lam*u*u)*Phi(u)*(-u)*mp.sin(z*u),[0,mp.inf],omega=abs(mp.re(z))+1)
def ImN(z,lam):
    return float(mp.im(-Hp(z,lam)/H(z,lam)))
# grid near first dBN zeros (z=2*14.13=28.27, 2*21=42), small imaginary parts
ZR=[26,28,30,42]; ZI=[0.2,0.5,1.0]
print("min Im N_lambda over grid (true xi) vs lambda:\n  lambda   min Im N")
for lam in (0.3,0.1,0.0,-0.1,-0.3):
    m=min(ImN(mp.mpf(str(zr))+1j*mp.mpf(str(zi)),mp.mpf(str(lam))) for zr in ZR for zi in ZI)
    print(f"  {lam:+.2f}    {m:+.4f}")
print("\nReading: monotone increasing in lambda + threshold ~0 => flow forces Lambda>=0 direction.")
