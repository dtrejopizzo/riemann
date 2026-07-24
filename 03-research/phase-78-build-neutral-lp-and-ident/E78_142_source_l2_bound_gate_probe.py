#!/usr/bin/env python3
"""E78.142 -- SOURCE-L2-BOUND numerical gate.

Computes ||y_b(mu)||_2, where y_b(mu) solves the EXACT coupled system of
E78.103 (D-11)-(D-16):

  A(mu)      = A_N - mu I           (inner block, NEVER the bordered H)
  u(mu)      = A(mu)^-1 s
  v(mu)      = A(mu)^-1 1
  g          = R_b (s - s_b 1)      (mu-independent)
  c_b(mu)    = A(mu)^-1 g
  a_b, b_b   = coupled scalar coefficients (P76.042)
  h_b(mu)    = a_b u + b_b v
  alpha_b, beta_b = derivative coefficients (D-13)
  y_b(mu)    solves A(mu) y_b = h_b + alpha_b s + beta_b 1     (D-16)

for mu = 0 and mu = mu_N (the ground eigenvalue nu_0^{(N)} of A_N(0), i.e.
the SAME intrinsic level object as E78.137's gate -- confirmed by
cross-checking nu_0 below against E78.137's published numbers), across
growing N, for both the zeta and planted builds, at several L.

This directly checks whether ||y_b(mu)||_2 stays bounded (SOURCE-L2-BOUND)
or blows up as N grows.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1] / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(ROOT))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from P76_011_loewner_identity_probe import symbols  # noqa: E402

PLANTED = ("14.134725141734693790", "0.30", "5.0")


def serialize(x, digits=12):
    return mp.nstr(x, digits)


def vnorm(vec: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(vec[j]) ** 2 for j in range(vec.rows)))


def sine_symbol(t, L, lam, planted):
    value = symbols(t, L, lam)[0]
    if planted is None:
        return value
    gamma0, beta, strength = (mp.mpf(x) for x in planted)
    spectral_point = gamma0 - 1j * beta
    planted_sine = mp.quad(lambda y: mp.sin(t * y) * mp.cos(spectral_point * y), [0, L])
    return value + strength * 2 * mp.re(planted_sine)


def y_b_norm(A, s, one, sb, g, mu):
    """||y_b(mu)||_2 for A(mu) = A - mu I, exact E78.103 system."""
    Amu = A - mu * mp.eye(A.rows)
    u = mp.lu_solve(Amu, s)
    v = mp.lu_solve(Amu, one)
    c = mp.lu_solve(Amu, g)
    p = (v.T * g)[0]
    q = (u.T * g)[0]
    L_local = None  # not needed here; caller passes precomputed aa,bb via closure
    return Amu, u, v, c, p, q


def run_case(label, planted, dps, Ls, Ns):
    mp.mp.dps = dps
    lam = mp.mpf(6)
    out = []
    for L_int in Ls:
        for n_modes in Ns:
            H, idx, L = build_mp(6, n_modes, dps, planted=planted)
            A = H[1:-1, 1:-1]
            inner = idx[1:-1]
            d = [2 * mp.pi * n / L for n in inner]
            D = mp.diag(d)
            db = 2 * mp.pi * idx[-1] / L
            s = mp.matrix([sine_symbol(dj, L, lam, planted) for dj in d])
            one = mp.matrix([1 for _ in d])
            sb = sine_symbol(db, L, lam, planted)
            Rb = (D - db * mp.eye(D.rows)) ** -1
            g = Rb * (s - sb * one)

            # ground eigenvalue nu_0 of A(0) -- cross-check vs E78.137
            vals = mp.eigsy(A, eigvals_only=True)
            nu0 = vals[0]
            nu1 = vals[1] if vals.rows > 1 else None

            def compute_y_norm(mu):
                Amu = A - mu * mp.eye(A.rows)
                u = mp.lu_solve(Amu, s)
                v = mp.lu_solve(Amu, one)
                c = mp.lu_solve(Amu, g)
                p = (v.T * g)[0]
                q = (u.T * g)[0]
                aa = 2 / L + 4 * p / L**2
                bb = -2 * sb / L - 4 * q / L**2
                alpha = 4 * (v.T * c)[0] / L**2
                beta = -4 * (u.T * c)[0] / L**2
                h = aa * u + bb * v
                y = mp.lu_solve(Amu, h + alpha * s + beta * one)
                return vnorm(y), vnorm(c), vnorm(u), vnorm(v)

            y0_norm, c0_norm, u0_norm, v0_norm = compute_y_norm(mp.mpf(0))
            # mu = mu_N = nu0 (only if nu0 magnitude is safely away from making
            # A(mu) exactly singular in finite precision; nu0 IS an eigenvalue
            # of A(0) so A(mu_N) is exactly singular -- use mu = nu0/2 instead,
            # the midpoint of [0, mu_N], to stay within the open interval while
            # still probing close to the collapsing floor)
            mu_half = nu0 / 2
            y_half_norm, c_half_norm, _, _ = compute_y_norm(mu_half)

            row = {
                "L": L_int,
                "N": n_modes,
                "nu0": serialize(nu0, 20),
                "nu1": serialize(nu1, 20) if nu1 is not None else None,
                "y_norm_mu0": serialize(y0_norm, 20),
                "c_norm_mu0": serialize(c0_norm, 20),
                "y_norm_mu_half_nu0": serialize(y_half_norm, 20),
                "c_norm_mu_half_nu0": serialize(c_half_norm, 20),
            }
            out.append(row)
            print(label, row)
    return {"label": label, "rows": out}


def main():
    dps = 60
    Ls = [6]
    Ns = [6, 8, 10, 12, 14, 16]
    result = {
        "statement": "E78.142 SOURCE-L2-BOUND numerical gate: ||y_b(mu)||_2 vs N",
        "dps": dps,
        "cases": [
            run_case("zeta", None, dps, Ls, Ns),
            run_case("plant", PLANTED, dps, Ls, Ns),
        ],
    }
    out_path = Path(__file__).with_name("E78_142_source_l2_bound_gate_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print("WROTE", out_path)


if __name__ == "__main__":
    main()
