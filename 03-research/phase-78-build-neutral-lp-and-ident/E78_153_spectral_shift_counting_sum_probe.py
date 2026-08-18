#!/usr/bin/env python3
"""E78.153 - SPECTRAL-SHIFT-COUNTING-SUM: is the counting bound summable?

Verified (E78.152): kappa_j (eigenvalues of K_N = D + (1/c) x q^T) are REAL, and
  T_N'/T_N = Tr(zI-K_N)^{-1} - Tr(zI-D)^{-1} - 1/(z-d_b).
So on z=i sigma, with nu_N = sum delta_{kappa_j} - sum delta_{d_j} - delta_{d_b},
  2 Re( i T_N'/T_N )(i sigma) = integral 2 sigma/(x^2+sigma^2) d nu_N(x).

Consecutive difference: Delta nu_N = nu_N - nu_{N+2} (total mass 0),
  M_N(x) = Delta nu_N((-inf, x])  (piecewise constant, -> 0 at +-inf).
Stieltjes bound:
  | integral 2 sigma/(x^2+sigma^2) d Delta nu_N |
      <= integral |M_N(x)| * 4 sigma |x|/(x^2+sigma^2)^2 dx.
Uniform over safe K: w(x) = sup_{sigma in K} 4 sigma|x|/(x^2+sigma^2)^2.

This probe computes, for each step N->N+2 and both builds:
  bound_N = integral |M_N(x)| w(x) dx        (the SPECTRAL-SHIFT-COUNTING bound)
  true_N  = max_{sigma in K} |2 Re i (T'/T)_{N+2} - 2 Re i (T'/T)_N|  (actual)
and reports bound_N, its step-ratio (geometric? N^{-p}?), and where |M_N| lives
(bulk vs moving edge). Summability of sum_N bound_N closes the fixed-L
convergence half of point 6 with a well-conditioned object.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
sys.path.insert(0, str(PHASE76))
sys.path.insert(0, str(PHASE77))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from P76_018_boundary_characteristic_probe import transfer  # noqa: E402
from P76_035_safe_log_derivative_probe import transfer_prime  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402

KSIG = [mp.mpf(x) for x in ["0.55", "0.75", "1.0", "1.5", "2.0", "3.0"]]


def nu_atoms(H, idx, L):
    """Return list of (position, weight) atoms of nu_N (kappa:+1, d_j:-1, d_b:-1)."""
    mu, A, db_idx, inner, x = right_transfer_data(H, idx)
    d = [2 * mp.pi * n / L for n in inner]
    db = 2 * mp.pi * db_idx / L
    n = len(d)
    xv = mp.matrix([x[j] for j in range(n)])
    q = mp.matrix([d[j] - db for j in range(n)])
    c = 1 - mp.fsum(x[j] for j in range(n))
    K = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            K[a, b] = (d[a] if a == b else mp.mpf(0)) + xv[a] * q[b] / c
    E, _ = mp.eig(K)
    kappa = [mp.re(e) for e in E]
    atoms = [(k, mp.mpf(1)) for k in kappa] + [(dj, mp.mpf(-1)) for dj in d] + [(db, mp.mpf(-1))]
    return atoms, (db_idx, inner, x, db)


def w_sup(x):
    ax = abs(x)
    if ax < mp.mpf("1e-9"):
        return mp.mpf(0)
    best = mp.mpf(0)
    for s in KSIG:
        val = 4 * s * ax / (x * x + s * s) ** 2
        if val > best:
            best = val
    # also the interior maximizer sigma=|x|/sqrt3 if in [min,max]
    s0 = ax / mp.sqrt(3)
    if KSIG[0] <= s0 <= KSIG[-1]:
        val = 4 * s0 * ax / (x * x + s0 * s0) ** 2
        if val > best:
            best = val
    return best


def counting_bound(atoms_N, atoms_M):
    """integral |M_N| w dx, M_N = cumulative of (nu_N - nu_{N+2})."""
    # combined signed atoms of Delta nu = nu_N - nu_{N+2}
    combined = [(p, wgt) for (p, wgt) in atoms_N] + [(p, -wgt) for (p, wgt) in atoms_M]
    combined.sort(key=lambda t: t[0])
    # M(x) piecewise constant; jumps at atom positions. Integrate |M|*w over gaps.
    total = mp.mpf(0)
    running = mp.mpf(0)
    for i in range(len(combined) - 1):
        running += combined[i][1]
        x0 = combined[i][0]
        x1 = combined[i + 1][0]
        if abs(running) < mp.mpf("1e-30"):
            continue
        # integral_{x0}^{x1} w(x) dx via midpoint-refined Simpson (w smooth here)
        mids = 8
        seg = (x1 - x0) / mids
        acc = mp.mpf(0)
        for m in range(mids):
            a = x0 + m * seg
            b = a + seg
            acc += (seg / 6) * (w_sup(a) + 4 * w_sup((a + b) / 2) + w_sup(b))
        total += abs(running) * acc
    return total


def logT_val(H, idx, L, sigma):
    mu, A, db_idx, inner, x = right_transfer_data(H, idx)
    z = 1j * sigma
    T = transfer(z, db_idx, inner, x, L)
    Tp = transfer_prime(z, db_idx, inner, x, L)
    return 2 * mp.re(1j * Tp / T)


def run(label, planted, lam_int, dps, max_modes):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    steps = []
    prev = None
    for N in range(8, max_modes - 1, 2):
        Hn, idxn = section(Hmax, idxmax, max_modes, N)
        Hm, idxm = section(Hmax, idxmax, max_modes, N + 2)
        atoms_N, _ = nu_atoms(Hn, idxn, L)
        atoms_M, _ = nu_atoms(Hm, idxm, L)
        bound = counting_bound(atoms_N, atoms_M)
        true = max(abs(logT_val(Hm, idxm, L, s) - logT_val(Hn, idxn, L, s)) for s in KSIG)
        ratio = "" if prev is None else mp.nstr(bound / prev, 5)
        prev = bound
        steps.append({"from_N": N, "bound": mp.nstr(bound, 8), "true": mp.nstr(true, 8),
                      "ratio": ratio, "N2bound": mp.nstr(N * N * bound, 6)})
        print(f"{label:6s} {N:2d}->{N+2:2d}  bound={mp.nstr(bound,6):>11s}  "
              f"true={mp.nstr(true,6):>11s}  ratio={ratio:>9s}  N^2*bound={mp.nstr(N*N*bound,5)}",
              flush=True)
    return {"label": label, "steps": steps}


def main():
    dps = 50
    lam_int = 6
    max_modes = 18
    result = {"statement": "SPECTRAL-SHIFT-COUNTING-SUM bound vs true, both builds", "cases": []}
    for label, planted in [("zeta", None), ("plant", (GAMMA, "0.30", "5.0"))]:
        result["cases"].append(run(label, planted, lam_int, dps, max_modes))
    (HERE / "E78_153_spectral_shift_counting_sum_results.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="ascii")
    print("WROTE E78_153_spectral_shift_counting_sum_results.json")


if __name__ == "__main__":
    main()
