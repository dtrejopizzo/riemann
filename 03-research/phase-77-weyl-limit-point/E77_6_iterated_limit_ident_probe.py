#!/usr/bin/env python3
"""E77.6 iterated-limit IDENT audit.

The probe checks two independent derivative identities:

1. d/dsigma log(sinh(sigma L/2)^2 |T(i sigma)|^2)
   = L coth(sigma L/2) + 2 Re(i T'(i sigma)/T(i sigma)).
2. 2 Xi'(s)/Xi(s) equals its archimedean term minus the absolutely
   convergent von Mangoldt series in s=1/2+sigma>1.

It also records the finite-section error for zeta and the planted build.
The latter is an audit of the predicted break at arithmetic identification,
not a proof of either limiting theorem.
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
from P76_018_boundary_characteristic_probe import right_transfer_data, transfer  # noqa: E402
from P76_035_safe_log_derivative_probe import target_log_derivative, transfer_prime  # noqa: E402
from P76_037_core_log_derivative_probe import external_tail  # noqa: E402


GAMMA = "14.134725141734693790"


def serial(value, digits: int = 24) -> str:
    return mp.nstr(value, digits)


def von_mangoldt_table(limit: int) -> list[mp.mpf]:
    values = [mp.mpf(0) for _ in range(limit + 1)]
    sieve = [True] * (limit + 1)
    if limit >= 0:
        sieve[0] = False
    if limit >= 1:
        sieve[1] = False
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        for multiple in range(p * p, limit + 1, p):
            sieve[multiple] = False
        power = p
        logp = mp.log(p)
        while power <= limit:
            values[power] = logp
            if power > limit // p:
                break
            power *= p
    return values


def archimedean_target(s: mp.mpf) -> mp.mpf:
    return 2 / s + 2 / (s - 1) - mp.log(mp.pi) + mp.digamma(s / 2)


def run_build(label, lam, modes, dps, sigmas, planted, mangoldt):
    mp.mp.dps = dps
    H, idx, L = build_mp(lam, modes, dps, planted=planted)
    db_idx, inner, x = right_transfer_data(H, idx)
    rows = []
    for sigma in sigmas:
        z = 1j * sigma
        t = transfer(z, db_idx, inner, x, L)
        tp = transfer_prime(z, db_idx, inner, x, L)
        finite_derivative = L * mp.coth(sigma * L / 2) + 2 * mp.re(1j * tp / t)

        def finite_log(u):
            tu = transfer(1j * u, db_idx, inner, x, L)
            return 2 * mp.log(mp.sinh(u * L / 2)) + 2 * mp.log(abs(tu))

        numeric_derivative = mp.diff(finite_log, sigma)
        finite_identity_error = abs(finite_derivative - numeric_derivative) / max(
            1, abs(numeric_derivative)
        )

        core = finite_derivative - external_tail(sigma, L, modes)
        target = target_log_derivative(sigma)
        target_relative_error = abs(core - target) / abs(target)

        s = mp.mpf("0.5") + sigma
        prime_sum = mp.fsum(mangoldt[n] / mp.power(n, s) for n in range(2, len(mangoldt)))
        euler_truncation = archimedean_target(s) - 2 * prime_sum
        euler_relative_error = abs(euler_truncation - target) / abs(target)
        rows.append(
            {
                "sigma": serial(sigma),
                "finite_derivative": serial(finite_derivative),
                "independent_numeric_derivative": serial(numeric_derivative),
                "finite_derivative_identity_relative_error": serial(finite_identity_error),
                "external_tail": serial(external_tail(sigma, L, modes)),
                "core_derivative": serial(core),
                "xi_target": serial(target),
                "finite_to_xi_relative_error": serial(target_relative_error),
                "euler_truncation": serial(euler_truncation),
                "euler_to_xi_relative_error": serial(euler_relative_error),
            }
        )
    return {
        "label": label,
        "lambda": lam,
        "L": serial(L),
        "N": modes,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "max_finite_identity_error": serial(
            max(mp.mpf(row["finite_derivative_identity_relative_error"]) for row in rows)
        ),
        "max_finite_to_xi_error": serial(
            max(mp.mpf(row["finite_to_xi_relative_error"]) for row in rows)
        ),
        "max_euler_to_xi_error": serial(
            max(mp.mpf(row["euler_to_xi_relative_error"]) for row in rows)
        ),
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--modes", type=int, default=18)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--prime-cutoff", type=int, default=200000)
    parser.add_argument("--sigmas", default="0.55,0.6,0.75,1.0,1.5,2.0,3.0")
    parser.add_argument("--output", type=Path, default=HERE / "E77_6_iterated_limit_ident_results.json")
    args = parser.parse_args()
    if args.dps < 60:
        parser.error("E77.6 requires dps >= 60")
    if args.prime_cutoff < 100:
        parser.error("prime cutoff must be at least 100")

    mp.mp.dps = args.dps
    sigmas = [mp.mpf(value) for value in args.sigmas.split(",") if value]
    mangoldt = von_mangoldt_table(args.prime_cutoff)
    result = {
        "statement": "Iterated-limit IDENT derivative audit",
        "parameters": {
            "lambda": args.lam,
            "modes": args.modes,
            "dps": args.dps,
            "prime_cutoff": args.prime_cutoff,
            "sigmas": [serial(sigma) for sigma in sigmas],
            "plant": {"gamma": GAMMA, "beta": "0.30", "strength": "5.0"},
        },
        "predicted_falsifier_break": "B: SAFE-GAMMA-IDENT / OUTER-LIMIT",
        "cases": [],
    }
    for label, planted in [
        ("zeta", None),
        ("plant", (GAMMA, "0.30", "5.0")),
    ]:
        case = run_build(label, args.lam, args.modes, args.dps, sigmas, planted, mangoldt)
        result["cases"].append(case)
        print(
            f"{label:5s} finite-id={serial(case['max_finite_identity_error'], 8)} "
            f"finite/xi={serial(case['max_finite_to_xi_error'], 8)} "
            f"euler/xi={serial(case['max_euler_to_xi_error'], 8)}",
            flush=True,
        )
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
