#!/usr/bin/env python3
"""Directed fixed Gauss--Bernstein moments for the D.160 flat column.

Each unit frequency cell uses a certified Q-point Gauss--Legendre rule.
The quadrature remainder is bounded by a Chebyshev/Bernstein-ellipse
estimate.  A single Arb evaluation on a rectangle containing the ellipse
supplies its maximum modulus.  All four multiplier powers reuse the same
Fourier data.

Smoke test:
  PYTHONPATH=/tmp/d61-flint D162_R=4 D162_Q=16 python3 this_file.py

Target:
  PYTHONPATH=/tmp/d61-flint D162_R=4096 D162_Q=64 python3 this_file.py
"""

from __future__ import annotations

import math
import os
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from flint import acb,acb_poly, arb, ctx


N = int(os.environ.get("D162_N", "170"))
DPS = int(os.environ.get("D162_DPS", "180"))
RMAX = int(os.environ.get("D162_R", "4"))
RSTART = int(os.environ.get("D162_START", "0"))
Q = int(os.environ.get("D162_Q", "16"))
MFLAT = int(os.environ.get("D162_M", "20"))
SWITCH = int(os.environ.get("D162_SWITCH", "64"))
ctx.dps = DPS

source = np.load(Path(os.environ.get(
    "D162_COLUMN", "/tmp/d160_flat_arb_column_300.npz"
)))
source_c=np.asarray(source["C"]);source_r=np.asarray(source["R"])
if source_c.ndim==1:source_c=source_c[:,None];source_r=source_r[:,None]
KSEL=source_c.shape[1]
coeff=[[arb(repr(float(source_c[n,a])),repr(float(source_r[n,a]))) for a in range(KSEL)] for n in range(N)]
dn=np.atleast_1d(source["derivative_norm2"])
derivative_norm2=[arb(repr(float(dn[a]))) for a in range(KSEL)]
# Directed L2 norm enclosure of the source.  The serialized coefficient
# balls are independent, so the direct sum is a safe (slightly widened)
# bound.  It gives a dependency-free Bernstein-ellipse majorant below.
source_norm2=[sum((coeff[n][a]*coeff[n][a] for n in range(N)),arb(0)) for a in range(KSEL)]
el=np.asarray(source["EL"]);er=np.asarray(source["ER"])
if el.ndim==1:el=el[:,None];er=er[:,None]
endpoint_left=[[arb(str(el[n,a])) for a in range(KSEL)] for n in range(N)]
endpoint_right=[[arb(str(er[n,a])) for a in range(KSEL)] for n in range(N)]
endpoint_left_c=[[acb(endpoint_left[n][a]) for a in range(KSEL)] for n in range(N)]
endpoint_right_c=[[acb(endpoint_right[n][a]) for a in range(KSEL)] for n in range(N)]
left_poly=[acb_poly([acb(0)]*(MFLAT+1)+[endpoint_left_c[r][a] for r in range(MFLAT,N)]) for a in range(KSEL)]
right_poly=[acb_poly([acb(0)]*(MFLAT+1)+[endpoint_right_c[r][a] for r in range(MFLAT,N)]) for a in range(KSEL)]

T = arb(5).log() / 2
quarter = arb(1) / 4
phase_minus = [acb(1), acb(0, -1), acb(-1), acb(0, 1)]
phase_plus = [acb(1), acb(0, 1), acb(-1), acb(0, -1)]
roots_norm = [arb(2 * n + 1).sqrt() for n in range(N)]


def legvals(x: arb, nmax: int) -> list[arb]:
    out = [arb(1)]
    if nmax == 1:
        return out
    out.append(x)
    for n in range(1, nmax - 1):
        out.append(((2 * n + 1) * x * out[-1] - n * out[-2]) / (n + 1))
    return out


def certified_gauss(q: int) -> tuple[list[arb], list[arb]]:
    approx = leggauss(q)[0]
    roots = []
    for guess in approx:
        lo = arb(repr(float(guess - 1.0e-10)))
        hi = arb(repr(float(guess + 1.0e-10)))
        flo = legvals(lo, q + 1)[q]
        fhi = legvals(hi, q + 1)[q]
        assert (flo < 0) != (fhi < 0)
        for _ in range(min(700, int(2.5 * DPS))):
            mid = (lo + hi) / 2
            fm = legvals(mid, q + 1)[q]
            if not (fm < 0 or fm > 0):
                break
            if (fm < 0) == (flo < 0):
                lo, flo = mid, fm
            else:
                hi = mid
        mid = (lo + hi) / 2
        roots.append(arb(mid.mid(), (hi - lo) / 2 + mid.rad()))
    weights = []
    for x in roots:
        vals = legvals(x, q + 1)
        der = q * (x * vals[q] - vals[q - 1]) / (x * x - 1)
        weights.append(2 / ((1 - x * x) * der * der))
    assert abs(sum(weights, arb(0)) - 2) < arb(10) ** (-(DPS // 2))
    return roots, weights


print("constructing certified Gauss rule", Q, flush=True)
nodes, weights = certified_gauss(Q)


def entire_spherical_sequence(x: acb) -> list[acb]:
    out = []
    odd_double_factorial = 1
    for n in range(N):
        if n:
            odd_double_factorial *= 2 * n + 1
        out.append(
            x**n / odd_double_factorial
            * (-x * x / 4).hypgeom_0f1(arb(2 * n + 3) / 2)
        )
    return out


def bessel_spherical_sequence(x: acb) -> list[acb]:
    pref = (acb(arb.pi()) / (2 * x)).sqrt()
    return [pref * x.bessel_j(arb(2 * n + 1) / 2) for n in range(N)]


def endpoint_pair(tau: acb) -> tuple[acb, acb]:
    ip = acb(0, 1)
    eplus = (ip * tau * T).exp()
    eminus = (-ip * tau * T).exp()
    qf=1/(ip*tau);qb=-qf
    return ([eplus*qf*left_poly[a](qf)-eminus*qf*right_poly[a](qf) for a in range(KSEL)],
            [eminus*qb*left_poly[a](qb)-eplus*qb*right_poly[a](qb) for a in range(KSEL)])


def direct_pair(tau: acb, force_entire: bool = False) -> tuple[acb, acb]:
    if not force_entire and tau.real > SWITCH:
        return endpoint_pair(tau)
    x = acb(T) * tau
    if force_entire or not (tau.real > 0):
        seq = entire_spherical_sequence(x)
    else:
        seq = bessel_spherical_sequence(x)
    forward=[acb(0) for _ in range(KSEL)];backward=[acb(0) for _ in range(KSEL)]
    for n in range(N):
        for a in range(KSEL):
            term=acb(coeff[n][a]*roots_norm[n])*seq[n]
            forward[a]+=phase_minus[n%4]*term;backward[a]+=phase_plus[n%4]*term
    scale = acb((2 * T).sqrt())
    return [scale*x for x in forward],[scale*x for x in backward]


def multiplier(tau: acb) -> acb:
    ip = acb(0, 1)
    def shifted_digamma(z: acb) -> acb:
        shifted = z + 20
        value = shifted.digamma()
        for k in range(20):
            value -= 1 / (z + k)
        return value

    value = (shifted_digamma(acb(quarter) + ip * tau / 2)
             + shifted_digamma(acb(quarter) - ip * tau / 2)) / 2
    value -= acb(arb.pi().log())
    for n, lam in ((2, arb(2).log()), (3, arb(3).log()), (4, arb(2).log())):
        value -= 2 * acb(lam / arb(n).sqrt()) * (tau * arb(n).log()).cos()
    return value


def values(tau: acb, force_entire: bool = False) -> list[acb]:
    forward, backward = direct_pair(tau, force_entire=force_entire)
    base = multiplier(tau)
    return [[[base**power*(forward[a]*backward[b]+backward[a]*forward[b])/(2*acb(arb.pi()))
              for b in range(KSEL)] for a in range(KSEL)] for power in range(1,5)]


def multiplier_rectangle_bound(centre: arb) -> arb:
    """A source-independent bound for |r| on the Bernstein rectangle.

    On |Im tau|<=0.4 the two digamma arguments have real part at least
    0.05.  Shift each argument by 20.  The recurrence contributes at most
    1/0.05 + H_19 < 24, while the standard first-term asymptotic bound at
    real part >=20 contributes less than log(|tau|+21)+1.  The contacts and
    log(pi) contribute less than six.  The rounded constant 31 therefore
    bounds the complete multiplier on the whole rectangle.
    """
    return (abs(centre) + amajor + 21).log() + 31


# Bernstein ellipse: reference-cell semimajor and semiminor axes.  B=0.20
# stays strictly inside the nearest digamma poles at imaginary height 1/2.
bminor = arb(os.environ.get("D162_BMINOR", "0.40"))
rho = 2 * bminor + (1 + 4 * bminor * bminor).sqrt()
amajor = (rho + 1 / rho) / 4  # physical half-width is 1/2
bernstein_factor = 8 * rho ** (-2 * Q) / (rho - 1)

totals=[[[arb(0) for _ in range(KSEL)] for _ in range(KSEL)] for _ in range(4)]
errors=[[[arb(0) for _ in range(KSEL)] for _ in range(KSEL)] for _ in range(4)]
assert 0 <= RSTART < RMAX
for left in range(RSTART, RMAX):
    centre = arb(left) + arb(1) / 2
    # Directed Gauss sum on the real cell.
    local=[[[acb(0) for _ in range(KSEL)] for _ in range(KSEL)] for _ in range(4)]
    for x, w in zip(nodes, weights):
        tau = acb(centre + x / 2)
        point = values(tau)
        for j in range(4):
            for a in range(KSEL):
                for b in range(KSEL):local[j][a][b]+=w*point[j][a][b]/2
    # Rectangle containing the Bernstein ellipse.  The first cells use the
    # entire representation; high cells use the exact endpoint expansion.
    # Do not evaluate the highly cancelling endpoint series on one complex
    # rectangle: interval dependency makes that bound useless at high
    # frequency.  Cauchy--Schwarz directly gives, for |Im tau|<=bminor,
    # |Fhat(tau)| <= sqrt(2T)||F||_2 exp(T*bminor).  This uniform entire
    # bound is modest and, multiplied by rho^(-2Q), is much sharper.
    rbound = multiplier_rectangle_bound(centre)
    for j in range(4):
        for a in range(KSEL):
            for b in range(KSEL):
                assert local[j][a][b].imag.contains(0)
                totals[j][a][b]+=local[j][a][b].real
                pb=2*T*(source_norm2[a]*source_norm2[b]).sqrt()*(2*T*bminor).exp()/arb.pi()
                errors[j][a][b]+=bernstein_factor*pb*rbound**(j+1)
    if (left + 1) % 16 == 0 or left + 1 == RMAX:
        print("completed frequency cells", left + 1, flush=True)


def tail(power: int,aidx: int) -> arb:
    if RSTART or RMAX < 150:
        return arb(0)
    a = 2 * MFLAT
    r = arb(RMAX)
    ell = r.log() + 5
    series = arb(0)
    for j in range(power + 1):
        series += (
            math.comb(power, j) * ell ** (power - j) * math.factorial(j)
            / (a - 1) ** (j + 1)
        )
    return 2*T*derivative_norm2[aidx]/arb.pi()*r**(1-a)*series


centres=np.zeros((4,KSEL,KSEL));radii=np.zeros_like(centres)
for j in range(4):
    for a in range(KSEL):
        for b in range(KSEL):
            tb=(tail(j+1,a)*tail(j+1,b)).sqrt()
            enclosure=arb(totals[j][a][b].mid(),totals[j][a][b].rad()+errors[j][a][b].upper()+tb.upper())
            centres[j,a,b]=float(enclosure.mid());radii[j,a,b]=float(enclosure.rad())
    print(f"H{j+1} max radius =",np.max(radii[j]))

save = Path(os.environ.get("D162_SAVE", f"/tmp/d162_moments_R{RMAX}_Q{Q}.npz"))
saved_radii = np.nextafter(
    radii + np.abs(np.spacing(centres)) / 2,
    np.inf,
)
if KSEL==1:centres=centres[:,0,0];saved_radii=saved_radii[:,0,0]
np.savez(
    save, C=centres, R=saved_radii,
    start=RSTART, cutoff=RMAX, order=Q,
)
print("saved", save)
if RSTART == 0 and RMAX >= 150:
    print("D162 fixed Gauss--Bernstein moments INCLUDING TAIL: PASS")
else:
    print("D162 fixed Gauss--Bernstein directed finite band: PASS")
