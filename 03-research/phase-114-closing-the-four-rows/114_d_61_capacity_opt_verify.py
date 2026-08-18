#!/usr/bin/env python3
"""High-precision diagnostic for D.61's optimized capacity constants."""
import mpmath as mp

mp.mp.dps = 100
D0 = mp.mpf("5.41312")
m0_upper = mp.mpf("5.372184")
c = mp.log(2) / mp.sqrt(2)


def Phi(h, R):
    return (D0 - m0_upper - 2*c*D0/mp.log(2*R)
            - 8*c*h*R/mp.pi)


h = mp.mpf(10) ** -61
R = mp.mpf(2) * mp.mpf(10) ** 57
assert Phi(h, R) > mp.mpf("0.00067")

G = D0 - m0_upper
A = 2*c*D0
Lstar = mp.findroot(lambda L: A*(1/L + 1/L**2) - G, 130)
hcap = mp.pi*D0*mp.exp(-Lstar)/(2*Lstar**2)
assert mp.mpf("130.6155") < Lstar < mp.mpf("130.6157")
assert mp.mpf("9.37e-61") < hcap < mp.mpf("9.38e-61")

print("PASS Phi(10^-61,2*10^57) =", mp.nstr(Phi(h, R), 30))
print("PASS L* =", mp.nstr(Lstar, 30))
print("PASS h_cap =", mp.nstr(hcap, 30))
