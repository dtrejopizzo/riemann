"""
SURF-A step 2: the involution structure (Phase 17).
Verifies the elementary claims I1-I3 of 02-involution.md, including the CORRECTION:
the critical line is the fixed locus of the anti-holomorphic reflection j(s)=1-conj(s),
NOT of the functional equation iota(s)=1-s (whose only fixed point is s=1/2).

Symmetries of the zero set (s-plane):
    sigma(s) = conj(s)        (complex conjugation)
    iota(s)  = 1 - s          (functional equation xi(s)=xi(1-s))
    j(s)     = 1 - conj(s)    (= sigma.iota = iota.sigma : reflection across Re=1/2)
They generate the Klein four-group V = {id, sigma, iota, j}.
"""
import numpy as np

sigma = lambda s: np.conjugate(s)
iota  = lambda s: 1 - s
j     = lambda s: 1 - np.conjugate(s)
V = {"id": lambda s: s, "sigma": sigma, "iota": iota, "j": j}

def orbit(s):
    pts = [g(s) for g in V.values()]
    uniq = []
    for p in pts:
        if not any(abs(p-q) < 1e-12 for q in uniq):
            uniq.append(p)
    return uniq

def fixed_by(g, s, tol=1e-12):
    return abs(g(s) - s) < tol

print("="*70)
print("I1  |  Which involution fixes the critical line {Re s = 1/2}?")
print("="*70)
for label, gam in [("on-line  1/2+iy ", 7.0), ("on-line  1/2+iy ", 14.13)]:
    s = 0.5 + 1j*gam
    print(f"  s={s}:  fixed by iota(1-s)? {fixed_by(iota,s)!s:5}  "
          f"fixed by sigma(conj)? {fixed_by(sigma,s)!s:5}  "
          f"fixed by j(1-conj)? {fixed_by(j,s)!s:5}")
print("  --> iota fixes ONLY s=1/2:", fixed_by(iota, 0.5+0j), "| j fixes the whole line. (correction)")
print("  Fix(sigma) = real axis (Im s=0); e.g. s=0.3:", fixed_by(sigma, 0.3+0j))

print("\n" + "="*70)
print("I2  |  Orbits: off-line = free quartets (size 4), on-line = pairs (size 2)")
print("="*70)
for label, s in [("off-line 1/2+b+iy", 0.5+0.18+1j*14.13),
                 ("on-line  1/2+iy  ", 0.5+1j*14.13),
                 ("trivial-ish real ", 0.3+0j)]:
    orb = orbit(s)
    stab = [name for name, g in V.items() if fixed_by(g, s)]
    print(f"  {label}: |orbit|={len(orb)}  stabilizer={stab}")
print("  off-line quartet pts:", [np.round(p,3) for p in orbit(0.5+0.18+1j*14.13)])

print("\n" + "="*70)
print("I3  |  centered coord zeta=s-1/2: j(zeta)=-conj(zeta); b=Re(zeta) is transverse")
print("="*70)
print("    action on (b,gamma) = (Re zeta, Im zeta):")
for name, g in V.items():
    z = (0.18) + 1j*(14.13)          # zeta = b + i gamma
    s = 0.5 + z
    gz = g(s) - 0.5                   # image in zeta-coord
    print(f"     {name:6}: (b,gamma)=( {z.real:+.2f},{z.imag:+.2f}) -> "
          f"( {gz.real:+.2f},{gz.imag:+.2f})")
print("  --> j: (b,gamma)->(-b,gamma) flips ONLY b (transverse), fixes gamma (along the line).")
print("      Fix(j) = {b=0} = critical line; b=Re(s-1/2) is the transverse coordinate. QED I3.")

print("\n" + "="*70)
print("VERDICT: critical line = Fix(j), j(s)=1-conj(s) an ANTI-HOLOMORPHIC involution")
print("(a real structure). Off-line zeros = free Klein-4 orbits (quartets); on-line zeros")
print("sit ON Fix(j) so the orbit degenerates to a pair -- exactly where the (1,1) block")
print("degenerates to (1,0). b=Re(s-1/2) is the coordinate transverse to the fixed locus.")
print("="*70)
