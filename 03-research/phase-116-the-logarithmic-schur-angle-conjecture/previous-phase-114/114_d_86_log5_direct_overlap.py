#!/usr/bin/env python3
"""Independent common-refinement audit of the log(5)/2 contact overlaps.

This imports the floating candidate selected by the D.86 term breakdown, but
does not reuse its midpoint-matching contact rule.  On every component of the
common refinement of the original mesh and its translate, both factors are
polynomials of degree nine.  Ten-point Gauss--Legendre therefore integrates
their product exactly up to binary floating roundoff.
"""
from pathlib import Path
import math
import runpy
import numpy as np
from numpy.polynomial.legendre import leggauss, legval

ns = runpy.run_path(str(Path(__file__).with_name("114_d_86_log5_term_breakdown.py")))
coef = ns["coef"]
hs = np.asarray(ns["hs"])
left = np.asarray(ns["left"])
mid = np.asarray(ns["mid"])
T = float(ns["T"])
D = int(ns["D"])
edges = np.r_[left, T]
gx, gw = leggauss(10)


def value_scalar(x):
    """Evaluate the cellwise orthonormal Legendre expansion."""
    idx = np.searchsorted(edges, x, side="right") - 1
    idx = np.clip(idx, 0, len(hs) - 1)
    u = 2 * (x - mid[idx]) / hs[idx]
    scale = np.sqrt(np.arange(1, 2 * D, 2) / hs[idx])
    return legval(u, coef[idx * D:(idx + 1) * D] * scale)


def value(x):
    return np.asarray([value_scalar(float(y)) for y in np.atleast_1d(x)])


def correlation(a):
    lo, hi = -T, T - a
    cuts = [lo, hi]
    cuts.extend(x for x in edges if lo < x < hi)
    cuts.extend(x - a for x in edges if lo < x - a < hi)
    cuts = np.asarray(sorted(set(round(float(x), 15) for x in cuts)))
    ans = 0.0
    for l, r in zip(cuts[:-1], cuts[1:]):
        x = (l + r) / 2 + (r - l) * gx / 2
        ans += (r - l) / 2 * np.dot(gw, value(x) * value(x + a))
    return ans


total = 0.0
for n, a, w in [
    (2, math.log(2), math.log(2) / math.sqrt(2)),
    (3, math.log(3), math.log(3) / math.sqrt(3)),
    (4, math.log(4), math.log(2) / 2),
]:
    c = correlation(a)
    term = -2 * w * c
    total += term
    print(f"n={n}: direct correlation={c:.17g}, QW term={term:.17g}")

print("direct contact total:", total)
print("term-breakdown common-refinement total:", ns["contact_total"])
assert abs(correlation(math.log(3))) > 1e-12
assert abs(total - ns["contact_total"]) < 1e-10
print("PASS independent common-refinement overlap audit")
