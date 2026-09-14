#!/usr/bin/env python3
"""Calibrate the corrected phase-106 heat gradient against paper 42's
forced Gamma matrix at T=log(2).

This tests the archimedean channel only. It does not test the still-missing
map from the positive P3 pushout to the physical primitive defect.
"""

import math
import os
import pathlib
import sys

import numpy as np
from scipy.integrate import quad_vec

HERE = pathlib.Path(__file__).resolve()
PHASE118 = HERE.parents[2] / "phase-118-the-exact-threshold-inequality" / "scripts"
sys.path.insert(0, str(PHASE118))
import rowd_assembly as ra  # noqa: E402


T = math.log(2)
REFINE = int(os.environ.get("P3_REFINE", "4"))
c, d = ra.build_mesh(T, refine=REFINE)
gram = ra.gram_matrix(c, d)
forced = ra.gamma_form(c, d)


def density(u):
    return math.exp(-u / 2) / (-math.expm1(-2 * u))


def integrand(u):
    if u == 0:
        return np.zeros_like(gram)
    shift = ra.shift_form(c, d, u)
    return density(u) * (2 * gram - shift - shift.T)


# All changes in the overlap matrix occur at differences of mesh endpoints.
edges = np.unique(np.concatenate([c, d]))
breaks = sorted(
    {float(abs(x - y)) for x in edges for y in edges if 1e-14 < abs(x - y) < 2 * T - 1e-14}
)
points = [0.0] + breaks + [2 * T]

heat = np.zeros_like(gram)
error_bound = 0.0
for lo, hi in zip(points[:-1], points[1:]):
    value, error = quad_vec(integrand, lo, hi, epsabs=2e-11, epsrel=2e-11)
    heat += value
    error_bound += float(error)
value, error = quad_vec(integrand, 2 * T, np.inf, epsabs=2e-11, epsrel=2e-11)
heat += value
error_bound += float(error)

delta = heat - forced
print(f"T=log2, mesh dimension={len(c)}")
print(f"quad_vec accumulated error estimate: {error_bound:.3e}")
print(f"max |corrected heat Gram - forced Gamma Gram|: {np.max(np.abs(delta)):.3e}")
print(f"Frobenius relative error: {np.linalg.norm(delta)/np.linalg.norm(forced):.3e}")

assert np.max(np.abs(delta)) < 2e-8

# The uncorrected phase-106 normalization was exactly twice this heat Gram.
wrong_delta = 2 * heat - forced
print(f"max |old two-component Gram - forced Gamma Gram|: {np.max(np.abs(wrong_delta)):.6e}")
assert np.max(np.abs(wrong_delta)) > 1e-2
