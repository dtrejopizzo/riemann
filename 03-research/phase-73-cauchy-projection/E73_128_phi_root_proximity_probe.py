#!/usr/bin/env python3
import sys
import math
import numpy as np
from scipy.optimize import brentq

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact, cauchy_real  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def cauchy_prime(t, d, xi):
    return -float(np.sum(xi / ((t - d) ** 2)))


def phi(t, L, d, xi):
    return (2.0 / math.sqrt(L)) * math.sin(t * L / 2.0) * cauchy_real(t, d, xi)


def phi_prime(t, L, d, xi):
    c = cauchy_real(t, d, xi)
    cp = cauchy_prime(t, d, xi)
    return (2.0 / math.sqrt(L)) * (
        (L / 2.0) * math.cos(t * L / 2.0) * c + math.sin(t * L / 2.0) * cp
    )


def finite_roots_signed(d, xi, hmax):
    roots = []
    ds = np.sort(d)
    for left_pole, right_pole in zip(ds[:-1], ds[1:]):
        left = left_pole + 1e-8
        right = right_pole - 1e-8
        if right <= left:
            continue
        try:
            fa = cauchy_real(left, d, xi)
            fb = cauchy_real(right, d, xi)
            if np.isfinite(fa) and np.isfinite(fb) and fa * fb < 0:
                root = brentq(lambda x: cauchy_real(x, d, xi), left, right, xtol=1e-13)
                if -hmax <= root <= hmax:
                    roots.append(root)
        except Exception:
            pass
    return np.array(sorted(roots))


def run():
    print("E73.128 Phi root-proximity probe")
    print("Tests Phi(-gamma) ~= Phi'(root)*(distance to nearest Cauchy root).")
    print(" lam     L gamma      rootDistB    phiB  phiPrimeB predictedB ratio")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        d, L, xi, _ = setup_exact(lam, n_modes)
        roots = finite_roots_signed(d, xi, hmax=60.0)
        for gamma in GAMMAS[:3]:
            t = -gamma
            root = roots[int(np.argmin(np.abs(roots - t)))]
            dist = abs(t - root)
            ph = abs(phi(t, L, d, xi))
            der = abs(phi_prime(root, L, d, xi))
            pred = der * dist
            ratio = ph / max(pred, 1e-300)
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {bexp(dist, L):10.3f} {bexp(ph, L):7.3f}"
                f" {bexp(der, L):10.3f} {bexp(pred, L):10.3f}"
                f" {ratio:7.3f}"
            )


if __name__ == "__main__":
    run()

