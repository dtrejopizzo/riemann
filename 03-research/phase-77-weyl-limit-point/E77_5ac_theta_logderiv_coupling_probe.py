#!/usr/bin/env python3
"""E77.5ac coupled theta log-derivative diagnostics."""

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
from E77_3c_two_generator_ident_probe import GAMMA, serial  # noqa: E402
from E77_5aa_schur_logt_functional_probe import prepare_schur, section, schur_logt_parts  # noqa: E402


def cserial(z, digits=18):
    return {"re": serial(mp.re(z), digits), "im": serial(mp.im(z), digits)}


def arg_or_none(z):
    if abs(z) == 0:
        return None
    return serial(mp.arg(z), 18)


def safe_scalar(z):
    return 2 * mp.re(1j * z)


def q_from_deltas(delta_rows, field):
    by_key = {(r["sigma"], r["N"]): r for r in delta_rows}
    out = {}
    for row in delta_rows:
        n = row["N"]
        nxt = by_key.get((row["sigma"], n + 2))
        if nxt is None:
            continue
        out[(row["sigma"], n)] = n * n * (n * row[field] - (n + 2) * nxt[field])
    return out


def run_build(label, planted, lam_int, max_modes, dps, sigmas):
    Hmax, idxmax, L = build_mp(lam_int, max_modes, dps, planted=planted)
    point_rows = []
    delta_rows = []
    for n in range(8, max_modes - 1, 2):
        common_nodes = list(range(-n + 2, n - 1))
        Hn, idxn = section(Hmax, idxmax, max_modes, n)
        Hm, idxm = section(Hmax, idxmax, max_modes, n + 2)
        old_prepared = prepare_schur(Hn, idxn, common_nodes)
        new_prepared = prepare_schur(Hm, idxm, common_nodes)
        for sigma in sigmas:
            old = schur_logt_parts(old_prepared, L, sigma)
            new = schur_logt_parts(new_prepared, L, sigma)
            old_u = old["theta_part"]
            new_u = new["theta_part"]
            for tag, section_n, data, u in [("old", n, old, old_u), ("new", n + 2, new, new_u)]:
                point_rows.append(
                    {
                        "sigma": serial(sigma),
                        "step_N": n,
                        "section_N": section_n,
                        "tag": tag,
                        "theta": cserial(data["theta"]),
                        "theta_prime": cserial(data["theta_prime"]),
                        "one_minus_theta": cserial(1 - data["theta"]),
                        "u": cserial(u),
                        "u_abs": serial(abs(u), 18),
                        "u_arg": arg_or_none(u),
                        "safe_u": serial(safe_scalar(u), 18),
                        "theta_abs": serial(abs(data["theta"]), 18),
                        "one_minus_theta_abs": serial(abs(1 - data["theta"]), 18),
                        "theta_prime_abs": serial(abs(data["theta_prime"]), 18),
                        "theta_prime_over_den_abs": serial(
                            abs(data["theta_prime"]) / abs(1 - data["theta"]) if abs(1 - data["theta"]) else mp.inf,
                            18,
                        ),
                    }
                )
            delta_u = safe_scalar(old_u) - safe_scalar(new_u)
            delta_rows.append(
                {
                    "sigma": serial(sigma),
                    "N": n,
                    "to_N": n + 2,
                    "delta_u_safe": delta_u,
                    "delta_den_abs": abs(1 - old["theta"]) - abs(1 - new["theta"]),
                    "delta_theta_prime_abs": abs(old["theta_prime"]) - abs(new["theta_prime"]),
                    "new_u_abs": abs(new_u),
                    "new_u_arg": arg_or_none(new_u),
                    "new_den_abs": abs(1 - new["theta"]),
                    "new_theta_prime_abs": abs(new["theta_prime"]),
                }
            )
    q_u = q_from_deltas(delta_rows, "delta_u_safe")
    q_den = q_from_deltas(delta_rows, "delta_den_abs")
    q_num = q_from_deltas(delta_rows, "delta_theta_prime_abs")
    qrows = []
    for row in delta_rows:
        key = (row["sigma"], row["N"])
        if key not in q_u:
            continue
        qrows.append(
            {
                "sigma": row["sigma"],
                "N": row["N"],
                "mod4": row["N"] % 4,
                "Q_theta": float(q_u[key]),
                "Q_den_abs": float(q_den[key]),
                "Q_theta_prime_abs": float(q_num[key]),
                "new_u_abs": float(row["new_u_abs"]),
                "new_u_arg": row["new_u_arg"],
                "new_den_abs": float(row["new_den_abs"]),
                "new_theta_prime_abs": float(row["new_theta_prime_abs"]),
            }
        )
    serial_deltas = []
    for row in delta_rows:
        serial_deltas.append(
            {
                "sigma": row["sigma"],
                "N": row["N"],
                "to_N": row["to_N"],
                "delta_u_safe": float(row["delta_u_safe"]),
                "delta_den_abs": float(row["delta_den_abs"]),
                "delta_theta_prime_abs": float(row["delta_theta_prime_abs"]),
                "new_u_abs": float(row["new_u_abs"]),
                "new_u_arg": row["new_u_arg"],
                "new_den_abs": float(row["new_den_abs"]),
                "new_theta_prime_abs": float(row["new_theta_prime_abs"]),
            }
        )
    return {"label": label, "points": point_rows, "deltas": serial_deltas, "qrows": qrows}


def run(lam_int, max_modes, dps, sigmas, case_filter):
    mp.mp.dps = dps
    specs = []
    if case_filter in {"zeta", "both"}:
        specs.append((f"zeta-lam{lam_int}", None))
    if case_filter in {"plant", "both"}:
        specs.append((f"plant-lam{lam_int}", (GAMMA, "0.30", "5.0")))
    return {
        "statement": "Coupled theta log-derivative u=-theta_prime/(1-theta)",
        "parameters": {
            "lambda": lam_int,
            "max_modes": max_modes,
            "dps": dps,
            "sigmas": [serial(s) for s in sigmas],
        },
        "cases": [run_build(label, planted, lam_int, max_modes, dps, sigmas) for label, planted in specs],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=22)
    parser.add_argument("--dps", type=int, default=70)
    parser.add_argument("--sigmas", default="1.0,3.0")
    parser.add_argument("--case", choices=["zeta", "plant", "both"], default="both")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5ac_theta_logderiv_coupling_results.json")
    args = parser.parse_args()
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = run(args.lam, args.max_modes, args.dps, sigmas, args.case)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for row in case["qrows"]:
            print(
                f"ROW s={row['sigma']} N={row['N']:2d} mod{row['mod4']} "
                f"Qtheta={row['Q_theta']:.9g} Qden={row['Q_den_abs']:.9g} "
                f"Qnum={row['Q_theta_prime_abs']:.9g} "
                f"|u|new={row['new_u_abs']:.9g} arg={row['new_u_arg']}",
                flush=True,
            )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
