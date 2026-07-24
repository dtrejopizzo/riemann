#!/usr/bin/env python3
"""E77.3c two-generator IDENT interface.

This probe connects MOM-RATIO to the Phase-76 two-generator formula:

    T_b(z) = F_b(z)/(z-d_b),
    F_b(z) = 1 + a_b(U(z)+U_b) + b_b(V(z)+V_b).

It verifies the exact formula and measures the safe logarithmic derivative
against the zeta target.  A planted build must fail the zeta target.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(PHASE76))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from P76_018_boundary_characteristic_probe import transfer  # noqa: E402
from P76_035_safe_log_derivative_probe import target_log_derivative, transfer_prime  # noqa: E402
from P76_037_core_log_derivative_probe import external_tail  # noqa: E402
from E77_2_commutator_probe import sine_symbol  # noqa: E402


GAMMA = "14.134725141734693790"


def serial(x: mp.mpf, digits: int = 24) -> str:
    return mp.nstr(x, digits)


def norm(v: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(v[j]) ** 2 for j in range(v.rows)))


def right_transfer_data(H: mp.matrix, idx: list[int]):
    vals, _ = mp.eigsy(H)
    mu = vals[0]
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    inner = idx[1:-1]
    b = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    x = mp.lu_solve(A, b)
    return mu, A, idx[-1], inner, x


def two_generator_data(A, inner, db_idx, L, lam, planted):
    d = [2 * mp.pi * n / L for n in inner]
    D = mp.diag(d)
    s = mp.matrix([sine_symbol(dn, L, lam, planted) for dn in d])
    one = mp.matrix([1 for _ in d])
    u = mp.lu_solve(A, s)
    v = mp.lu_solve(A, one)
    db = 2 * mp.pi * db_idx / L
    sb = sine_symbol(db, L, lam, planted)
    Rb = (D - db * mp.eye(D.rows)) ** -1
    source = s - sb * one
    p = (v.T * Rb * source)[0]
    q = (u.T * Rb * source)[0]
    aa = 2 / L + 4 * p / L**2
    bb = -2 * sb / L - 4 * q / L**2
    ub = mp.fsum(u[j] / (d[j] - db) for j in range(len(d)))
    vb = mp.fsum(v[j] / (d[j] - db) for j in range(len(d)))
    return d, u, v, db, aa, bb, ub, vb


def generated_values(z, d, u, v, db, aa, bb, ub, vb):
    U = mp.fsum(u[j] / (z - d[j]) for j in range(len(d)))
    V = mp.fsum(v[j] / (z - d[j]) for j in range(len(d)))
    Up = mp.fsum(-u[j] / (z - d[j]) ** 2 for j in range(len(d)))
    Vp = mp.fsum(-v[j] / (z - d[j]) ** 2 for j in range(len(d)))
    F = 1 + aa * (U + ub) + bb * (V + vb)
    Fp = aa * Up + bb * Vp
    T = F / (z - db)
    log_derivative = Fp / F - 1 / (z - db)
    package = aa * (U + ub) + bb * (V + vb)
    return T, log_derivative, F, package


def run_case(label, lam_int, max_modes, dps, sigmas, planted):
    mp.mp.dps = dps
    lam = mp.mpf(lam_int)
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    rows = []
    for n_modes in range(8, max_modes + 1, 2):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        _mu, A, db_idx, inner, x = right_transfer_data(H, idx)
        d, u, v, db, aa, bb, ub, vb = two_generator_data(A, inner, db_idx, L, lam, planted)
        sigma_rows = []
        max_ident = mp.mpf(0)
        max_target = mp.mpf(0)
        for sigma in sigmas:
            z = 1j * sigma
            T, logd, F, package = generated_values(z, d, u, v, db, aa, bb, ub, vb)
            direct_t = transfer(z, db_idx, inner, x, L)
            direct_tp = transfer_prime(z, db_idx, inner, x, L)
            ident_err = max(
                abs(T - direct_t) / max(1, abs(direct_t)),
                abs(logd - direct_tp / direct_t) / max(1, abs(direct_tp / direct_t)),
            )
            core = L * mp.coth(sigma * L / 2) + 2 * mp.re(1j * logd) - external_tail(sigma, L, n_modes)
            target = target_log_derivative(sigma)
            target_rel = abs(core - target) / abs(target)
            max_ident = max(max_ident, ident_err)
            max_target = max(max_target, target_rel)
            sigma_rows.append(
                {
                    "sigma": serial(sigma),
                    "two_generator_identity_error": serial(ident_err),
                    "core_log_derivative": serial(core),
                    "zeta_target": serial(target),
                    "target_relative_error": serial(target_rel),
                    "F_abs": serial(abs(F)),
                    "package_abs": serial(abs(package)),
                }
            )
        rows.append(
            {
                "N": n_modes,
                "energy": serial(norm(x) ** 2),
                "a_abs": serial(abs(aa)),
                "b_abs": serial(abs(bb)),
                "max_two_generator_identity_error": serial(max_ident),
                "max_zeta_target_relative_error": serial(max_target),
                "sigmas": sigma_rows,
            }
        )
        print(
            f"ROW {label:12s} lam={lam_int} N={n_modes:2d} "
            f"id={serial(max_ident, 8):>12s} target={serial(max_target, 8):>12s} "
            f"|a|={serial(abs(aa), 8):>12s} |b|={serial(abs(bb), 8):>12s}",
            flush=True,
        )
    return {
        "label": label,
        "lambda": lam_int,
        "dps": dps,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambdas", default="6,7,8")
    parser.add_argument("--max-modes", type=int, default=18)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--sigmas", default="0.6,0.75,1.0,1.5,2.0")
    parser.add_argument("--output", type=Path, default=HERE / "E77_3c_two_generator_ident_results.json")
    args = parser.parse_args()
    if args.dps < 50:
        parser.error("E77.3c requires dps >= 50")
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = {
        "statement": "Two-generator formula and safe log-derivative target",
        "parameters": {
            "lambdas": [int(x) for x in args.lambdas.split(",") if x],
            "max_modes": args.max_modes,
            "dps": args.dps,
            "sigmas": [serial(s) for s in sigmas],
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "cases": [],
    }
    for lam in result["parameters"]["lambdas"]:
        for label, planted in [
            (f"zeta-lam{lam}", None),
            (f"plant-lam{lam}", (GAMMA, "0.30", "5.0")),
        ]:
            print(f"BUILD {label}", flush=True)
            result["cases"].append(run_case(label, lam, args.max_modes, args.dps, sigmas, planted))
            args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
