#!/usr/bin/env python3
import sys
import math
import cmath

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_071_packet_mellin_formula_verifier import h0  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp, coeffs  # noqa: E402
from E73_116_box_domination_pilot import compatible_top_triples, far_box_budget, out_row_bounds  # noqa: E402
from E73_117_exact_local_box_verifier import local_window_breakpoints  # noqa: E402


def coeff_derivs(z, w, L):
    ez = cmath.exp(z * L)
    ew = cmath.exp(w * L)
    emw = cmath.exp(-w * L)

    n_a = (ew - 1.0) + ez * (emw - 1.0)
    dn_a = L * ez * (emw - 1.0)
    den_a = w - z
    da = 1j * (dn_a / den_a + n_a / (den_a * den_a))

    n_b = ez * (ew - 1.0) + (emw - 1.0)
    dn_b = L * ez * (ew - 1.0)
    den_b = w + z
    db = -1j * (dn_b / den_b - n_b / (den_b * den_b))
    return da, db


def hwin_and_deriv(z, ws, L, d, xi):
    total = 0.0
    deriv = 0.0
    for w in ws:
        a, b = coeffs(z, w, L)
        da, db = coeff_derivs(z, w, L)
        hw = h0(w, d, xi)
        hmw = h0(-w, d, xi)
        total += abs(a * hw) + abs(b * hmw)
        deriv += abs(da * hw) + abs(db * hmw)
    return total, deriv


def pref_up_for_row(row, gamma, d, xi):
    c = abs(sum(xi / (-gamma - d)))
    return row["up"] / max(c, 1e-300)


def lock_interval_upper(L, d, xi, triple, alpha0, alpha1, ws, nsub=16):
    worst = 0.0
    for j in range(nsub):
        a0 = alpha0 + (alpha1 - alpha0) * j / nsub
        a1 = alpha0 + (alpha1 - alpha0) * (j + 1) / nsub
        ac = 0.5 * (a0 + a1)
        rad = 0.5 * (a1 - a0)
        total = 0.0
        deriv = 0.0
        for row in triple:
            gamma = row["gamma"]
            zc = ac + 1j * gamma
            pref = pref_up_for_row(row, gamma, d, xi)
            val, der = hwin_and_deriv(zc, ws, L, d, xi)
            # The derivative of the exponential coefficient is increasing
            # over these positive-alpha base boxes.  Inflate by exp(rad L)
            # to cover the subinterval from its midpoint.
            infl = math.exp(rad * L)
            total += pref * val
            deriv += pref * der * infl
        worst = max(worst, total + deriv * rad)
    return worst


def verify_low_box(lam, n_modes, alpha0, alpha1, tau0, tau1, m, nsub=16):
    d, L, xi, rows, poss, _, main_box = far_box_budget(
        lam, n_modes, alpha0, alpha1, tau0, tau1, m
    )
    out_bounds = out_row_bounds(L, d, xi, [], alpha0, alpha1, tau0, tau1, m, rows)
    poss_gammas = {row["gamma"] for row in poss}
    triples = compatible_top_triples(out_bounds, poss_gammas)
    if not triples:
        return L, main_box, 0, float("inf")

    taus = local_window_breakpoints(tau0, tau1, list(GAMMAS[:12]))
    worst = 0.0
    for tau in taus:
        ws_g = sorted(list(GAMMAS[:12]), key=lambda g: (abs(g - tau), g))[:3]
        ws = [1j * g for g in ws_g]
        for triple in triples:
            worst = max(worst, lock_interval_upper(L, d, xi, triple, alpha0, alpha1, ws, nsub))
    return L, main_box, len(triples), worst


def run():
    print("E73.119 low-scale LOCK alpha-interval certificate")
    print("Uses analytic coefficient derivatives and finite alpha subintervals.")
    print(" lam     L box                         lockIntB mainBox nTri status")
    for tau in [GAMMAS[0], GAMMAS[1]]:
        L, main_box, ntri, lock = verify_low_box(16, 20, 0.15, 0.25, tau - 0.50, tau + 0.50, 3)
        lock_b = bexp(lock, L)
        ok = lock_b <= -5.0 and main_box <= 1.0
        print(
            f"{16:4d} {L:7.3f} [{0.15:.2f},{0.25:.2f}]x[{tau-0.50:5.2f},{tau+0.50:5.2f}]"
            f" {lock_b:9.3f} {main_box:7.3e} {ntri:4d} {'PASS' if ok else 'FAIL'}"
        )


if __name__ == "__main__":
    run()

