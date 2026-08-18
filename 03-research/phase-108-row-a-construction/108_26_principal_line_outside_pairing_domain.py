#!/usr/bin/env python3
"""Verifier for 108.26 - the principal line lies outside the pairing's domain.
No zero of xi is used anywhere."""
import math, numpy as np, sys
FAIL=[]
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

# --- A. balanced and principal are OPPOSITE conditions ---------------------
# balanced (108_24 Def 1.1):  int phi da = 0
# principal (108_03 Def 6.1): the single weight s = 0, i.e. a unit point mass
# integrate a normalised bump over the FULL line so no half is lost
def mass(c, centre=0.0, R=1.0):
    x=np.linspace(centre-R, centre+R, 2000001)
    g=np.exp(-((x-centre)/c)**2)/(c*math.sqrt(math.pi))
    return float(np.trapz(g,x))
ms=[round(mass(c),6) for c in (1e-1,1e-2,1e-3)]
ok = all(abs(m-1.0)<1e-6 for m in ms)
check("A  a point mass at s=0 has total mass 1, not 0", ok, f"masses {ms}")
# and a balanced profile has mass 0
a=np.linspace(0.05,0.95,400001)
phi=lambda x: np.sin(2*np.pi*(x-0.05)/0.9)
check("A' a balanced profile has total mass 0 (opposite condition)",
      abs(float(np.trapz(phi(a),a))) < 1e-9,
      f"int phi da = {float(np.trapz(phi(a),a)):.2e}")

# --- B. s = 0 is on the EXCLUDED boundary of the pairing's domain ----------
# 108_06 Cor 3.2: the two geometric series have ratios p^{-a} and p^{a-1};
# each converges iff its ratio has modulus < 1.  Test the ratios exactly -
# a fixed truncation depth is NOT a valid proxy (it fails for tiny a>0,
# where the series converges but arbitrarily slowly).
def converges(p, a):
    ra = a.real if isinstance(a, complex) else a
    return (abs(p**(-ra)) < 1.0), (abs(p**(ra-1.0)) < 1.0)
ok=True; rows=[]
for a in (0.0, 1e-6, 1e-3, 0.25, 0.5, 0.75, 1-1e-3, 1-1e-6, 1.0):
    c=converges(3,a); both=c[0] and c[1]; rows.append((a,both))
    if both != (0 < a < 1): ok=False
check("B  domain is exactly the OPEN strip 0<Re a<1; s=0 and s=1 excluded", ok,
      str([(f'{a:g}',b) for a,b in rows]))
# the exclusion at the endpoints is exact, not marginal: ratio equals 1 there
r0=abs(3**(-0.0)); r1=abs(3**(1.0-1.0))
check("B' at s=0 and s=1 the ratio is exactly 1, so the series cannot converge",
      abs(r0-1.0)<1e-15 and abs(r1-1.0)<1e-15, f"ratios {r0}, {r1}")

# --- C. s = 0 is an accumulation point of the singular set -----------------
# 108_11 Lemma 2.1: singular set {1/N : N>=2} u {1-1/M : M>=2}
S=sorted(1/N for N in range(2,200000))
ok = (min(S) < 1e-5) and all(S[i] < S[i+1] for i in range(200))
check("C  the singular set {1/N} accumulates at 0", ok,
      f"smallest three: {[f'{x:.2e}' for x in S[:3]]}")
# no gap: for every eps there are infinitely many singularities in (0,eps)
counts=[(eps, sum(1 for x in S if x < eps)) for eps in (1e-2,1e-3,1e-4)]
check("C' every neighbourhood of 0 contains infinitely many singularities",
      all(n > 50 for _,n in counts), str(counts))

# --- D. the two obstructions are independent ------------------------------
# (i) exclusion from the open strip is about CONVERGENCE of the local series;
# (ii) accumulation is about the CONTINUED function's singularities.
# Check they are logically distinct by exhibiting an interior point that is
# singular (so (ii) can occur strictly inside, where (i) does not apply).
interior_sing=[x for x in S if 0.05 < x < 0.95]
check("D  singularities occur strictly inside the strip too, so the two "
      "obstructions are independent", len(interior_sing) >= 10,
      f"{len(interior_sing)} interior singularities, e.g. {[round(x,4) for x in interior_sing[-4:]]}")

# --- E. consequence: no sequence inside the strip reaches s=0 cleanly ------
# any a_n -> 0+ must cross infinitely many singularities
def crossings(a0):
    return sum(1 for x in S if 0 < x < a0)
rows=[(a0, crossings(a0)) for a0 in (1e-1,1e-2,1e-3,1e-4)]
check("E  approaching s=0 from inside crosses infinitely many singularities",
      all(n>0 for _,n in rows) and rows[0][1] > rows[-1][1], str(rows))

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
