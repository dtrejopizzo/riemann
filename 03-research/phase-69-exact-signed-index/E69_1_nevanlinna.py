"""
E69.1 -- the gauge-invariant object: Nevanlinna condition of -xi'/xi (no gauge z0).

In the z-variable s = 1/2 + i z, the critical line is z real; xi has zeros at z_rho (real <=> RH).
xi'/xi(z) = sum_rho 1/(z - z_rho). If all z_rho real, -i*xi'/xi is a Nevanlinna (Herglotz) function
of z: Im >= 0 on the upper half-plane Im z > 0. An off-line zero (complex z_rho) breaks the sign.

  Omega_7 <=> N(z) := -i * (d/dz) log xi(1/2 + i z)  has  Im N(z) >= 0  for all Im z > 0.

This is gauge-free (no z0). Test: sample Im N(z) on a grid in the upper half-plane for the true xi
(RH holds in this range) vs xi with a planted off-line zero. Faithful gauge-invariant detector.
"""
import mpmath as mp
mp.mp.dps=30

def xi(s):
    return 0.5*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)

def xi_planted(s, rho):
    # multiply xi by (s-rho)(s-(1-rho)) to inject an off-line zero pair
    return xi(s)*(s-rho)*(s-(1-rho))

def N_of_z(z, xifun):
    s = mp.mpf('0.5') + 1j*z
    # d/dz log xi(1/2+iz) = i * xi'/xi(s);  N = -i * d/dz log xi = xi'/xi(s)
    dlog = mp.diff(lambda w: mp.log(xifun(mp.mpf('0.5')+1j*w)), z)
    return -dlog

def scan(xifun, tag, zr_list, zi_list):
    mn = mp.inf; worst=None
    for zr in zr_list:
        for zi in zi_list:
            val = N_of_z(mp.mpf(str(zr))+1j*mp.mpf(str(zi)), xifun)
            im = float(mp.im(val))
            if im < mn: mn=im; worst=(zr,zi)
    print(f"  [{tag}]  min Im N(z) over grid = {mn:+.4f}   at z={worst}")

zr_list=[10,20,30,40,50]         # real part (height) -- below first off-line region
zi_list=[0.3,0.7,1.2,2.0]        # imaginary part > 0 (upper half-plane)
print("Nevanlinna check: Im N(z) >= 0 on upper half-plane  <=>  RH (gauge-free).\n")
scan(xi, "true xi (RH holds here)", zr_list, zi_list)
for beta in ('0.7','0.9'):
    rho = mp.mpf(beta)+1j*mp.mpf('30')   # off-line zero at height 30
    scan(lambda s,r=rho: xi_planted(s,r), f"planted off-line beta={beta} at t=30", zr_list, zi_list)
