#!/usr/bin/env python3
import sys
import math
import cmath
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_055_far3_nodewise_verifier import setup_full, finite_roots_signed, hermite_kernel_bound, cauchy_real  # noqa: E402


def corners(alpha0, alpha1, tau0, tau1):
    return [
        alpha0 + 1j * tau0,
        alpha0 + 1j * tau1,
        alpha1 + 1j * tau0,
        alpha1 + 1j * tau1,
    ]


def min_abs_rect(alpha0, alpha1, tau0, tau1):
    # Minimum |alpha+i tau| over rectangle.
    ar = 0.0 if alpha0 <= 0.0 <= alpha1 else min(abs(alpha0), abs(alpha1))
    ti = 0.0 if tau0 <= 0.0 <= tau1 else min(abs(tau0), abs(tau1))
    return math.hypot(ar, ti)


def min_abs_shift_rect(x0, x1, y0, y1):
    return min_abs_rect(x0, x1, y0, y1)


def min_d_sample(alpha0, alpha1, tau0, tau1, gamma, grid_n=7):
    vals = []
    for alpha in np.linspace(alpha0, alpha1, grid_n):
        for tau in np.linspace(tau0, tau1, grid_n):
            a = alpha + 1j * tau
            beta = 1j * gamma - a
            vals.append(abs(1.0 / beta + 1.0 / (2.0 * a)))
    return max(min(vals), 1e-12)


def max_abs_w0(alpha0, alpha1, tau0, tau1):
    amin = max(min_abs_rect(alpha0, alpha1, tau0, tau1), 1e-12)
    return 0.5 / amin


def herm_derivative_lip(alpha0, alpha1, tau0, tau1, gamma, m, theta=0.5):
    amin = max(min_abs_rect(alpha0, alpha1, tau0, tau1), 1e-12)
    # beta=i gamma-a has real interval [-alpha1,-alpha0], imag [gamma-tau1,gamma-tau0].
    bmin = max(min_abs_shift_rect(-alpha1, -alpha0, gamma - tau1, gamma - tau0), 1e-12)
    dmin = min_d_sample(alpha0, alpha1, tau0, tau1, gamma)
    w0max = max_abs_w0(alpha0, alpha1, tau0, tau1)

    du = amin ** -2
    dv = bmin ** -2
    dd = dv + 0.5 * du
    beta_log = bmin ** -1 * dv
    d_log = dmin ** -1 * dd
    pref = 1.0 / ((1.0 - theta) * bmin * dmin)
    pref_der = pref * (beta_log + d_log)

    s = 0.0
    s_der = 0.0
    for p in range(m):
        for q in range(p, m):
            r = q - p
            coeff = math.comb(q, p) / math.factorial(p) * (theta ** (-q))
            mon = coeff * (w0max ** r) * (dmin ** (-q))
            if r == 0:
                w_part = 0.0
            else:
                w_part = r * (0.5 * du) * (w0max ** max(r - 1, 0)) * (dmin ** (-q)) * coeff
            if q == 0:
                d_part = 0.0
            else:
                d_part = coeff * (w0max ** r) * q * (dmin ** (-q - 1)) * dd
            s += mon
            s_der += w_part + d_part
    return pref_der * s + pref * s_der


def herm_box_upper_derivative(alpha0, alpha1, tau0, tau1, gamma, m, grid_n=5):
    alphas = np.linspace(alpha0, alpha1, grid_n)
    taus = np.linspace(tau0, tau1, grid_n)
    max_upper = 0.0
    max_infl = 1.0
    for ia in range(grid_n - 1):
        for it in range(grid_n - 1):
            a0, a1 = alphas[ia], alphas[ia + 1]
            t0, t1 = taus[it], taus[it + 1]
            ac = 0.5 * (a0 + a1)
            tc = 0.5 * (t0 + t1)
            center = hermite_kernel_bound(ac + 1j * tc, 1j * gamma, m)
            lip = herm_derivative_lip(a0, a1, t0, t1, gamma, m)
            radius = 0.5 * math.hypot(a1 - a0, t1 - t0)
            upper = center + lip * radius
            max_upper = max(max_upper, upper)
            max_infl = max(max_infl, upper / max(center, 1e-300))
    return max_upper, max_infl


def box_certificate(lam, n_modes, alpha0, alpha1, tau0, tau1, m, ncrit=12, grid_n=5):
    d, L, xi = setup_full(lam, n_modes)
    roots = finite_roots_signed(d, xi, hmax=max(GAMMAS[:ncrit]) + 10.0)
    rows = []
    for gamma in GAMMAS[:ncrit]:
        g_up, infl = herm_box_upper_derivative(alpha0, alpha1, tau0, tau1, gamma, m, grid_n)
        mesh = abs(1.0 - cmath.exp(1j * gamma * L))
        w_up = math.exp(alpha1 * L) * g_up * mesh
        t = -gamma
        c = abs(cauchy_real(t, d, xi))
        r = float(np.min(np.abs(t - roots))) if len(roots) else 1.0
        rows.append({"gamma": gamma, "far_up": w_up * r, "budget_up": (L**5) * w_up * c, "infl": infl})
    selected = sorted(rows, reverse=True, key=lambda row: row["far_up"])[:3]
    return L, selected, sum(row["budget_up"] for row in selected), max(row["infl"] for row in selected)


def run():
    print("E73.111 HERM-BOX derivative probe")
    print("Uses analytic derivative envelopes from E73.110 on subboxes.")
    print(" lam     L box                         selected        CmainUp  maxInfl status")
    boxes = []
    for tau in [GAMMAS[0], GAMMAS[1]]:
        boxes.append((0.18, 0.22, tau - 0.20, tau + 0.20))
        boxes.append((0.15, 0.25, tau - 0.50, tau + 0.50))
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32)]:
        for alpha0, alpha1, tau0, tau1 in boxes:
            L, selected, budget, infl = box_certificate(lam, n_modes, alpha0, alpha1, tau0, tau1, 3)
            names = ",".join(f"{row['gamma']:.1f}" for row in selected)
            print(
                f"{lam:4d} {L:7.3f} [{alpha0:.2f},{alpha1:.2f}]x[{tau0:5.2f},{tau1:5.2f}]"
                f" {names:17s} {budget:8.3e} {infl:8.3f} {'PASS' if budget <= 1.0 else 'FAIL'}"
            )


if __name__ == "__main__":
    run()
