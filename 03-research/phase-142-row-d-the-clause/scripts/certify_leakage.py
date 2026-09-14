# Certifies the leakage bound L for F_0(u) = exp(-u^2/(2 sigma^2)) sin(g1 u), sigma = 3:
#   L := sum_{rho != rho_1, conj(rho_1)} |Phi_{F_0}(1-rho)|
#      <= G e^{sigma^2/8} * sum_rho [ e^{-sigma^2 (gamma-g1)^2/2} + e^{-sigma^2 (gamma+g1)^2/2} ],
# valid unconditionally, using only 0 < Re(rho) < 1 (import (E2)) -- the Gaussian prefactor
# e^{sigma^2 c^2/2} <= e^{sigma^2/8} is uniform in the real part, so only the imaginary
# separation matters and hypothetical off-line zeros are covered.
#
# PROOF OF RECORD (round 2, finding H6 of R142_002): the zero-list-free bound.  It uses only
# (V2) "no zero other than rho_1, conj(rho_1) has |Im rho| <= 21" and the unconditional
# Riemann-von Mangoldt count #{gamma in [T,T+1]} <= log T (which counts off-line zeros too).
# Round 1 instead summed the explicit ordinates gamma_2..gamma_200 from mpmath.zetazero, i.e. it
# silently used the completeness of the standard zero list to height ~236, which (V2) does not
# assert.  That sharper sum is kept below as an ILLUSTRATION only.
from mpmath import mp, mpf, exp, sqrt, pi, log, zetazero, im
mp.dps = 30
sig = mpf(3); g1 = mpf('14.134725141734693790')
G = sig*sqrt(2*pi)/2
pref = G*exp(sig**2/8)
margin = G*mpf('0.00153983728119')          # G*(1-s_1), the quantity L must stay below

# ---- proof of record: (V2) + Riemann-von Mangoldt, no zero list ----
S = mpf(0); T = 21
while T < 400:
    S += 2*log(T)*exp(-sig**2*(mpf(T)-g1)**2/2); T += 1
L_record = pref*S
print("G                      =", mp.nstr(G, 12))
print("prefactor G*e^{9/8}    =", mp.nstr(pref, 12))
print("L (proof of record)   <=", mp.nstr(L_record, 6))
print("margin G*(1-s_1)       =", mp.nstr(margin, 6))
print("record << margin       :", L_record < margin/mpf(10)**80)

# ---- illustration only: explicit ordinates (needs the standard zero list) ----
def term(gam): return exp(-sig**2*(gam-g1)**2/2) + exp(-sig**2*(gam+g1)**2/2)
S2 = mpf(0); NZ = 60
for k in range(2, NZ+1):
    S2 += 2*term(im(zetazero(k)))
T = int(im(zetazero(NZ)))
while T < int(im(zetazero(NZ)))+200:
    S2 += 2*log(T)*exp(-sig**2*(mpf(T)-g1)**2/2); T += 1
print("L (illustration only) <=", mp.nstr(pref*S2, 6))
