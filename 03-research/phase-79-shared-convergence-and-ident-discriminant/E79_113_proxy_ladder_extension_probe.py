#!/usr/bin/env python3
"""E79.113 - extend the residual-coefficient proxy audit past the E79.90/E79.101 ladder.

E79.108-E79.112 read alpha_N, proxy_N and gap_N off two frozen result files whose
ladder stops at N=18 (six rows). This probe recomputes every ingredient from
scratch in ONE place and pushes the ladder to N=26, so the claims

    - |gap_N| stays uniformly tiny on zeta,
    - the zeta sign pattern crosses exactly once, near mid-ladder,
    - the planted controls never enter that regime,

can be tested against rows the earlier docs never saw.

Definitions (identical to E79.90/E79.101/E79.108):

    alpha_N := [outlier_abs - escape_scale - mean(d)] / second_abs
    proxy_N := 1/sqrt(outlier_fraction) - mesh_radius/second_abs
    gap_N   := alpha_N - proxy_N
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
PHASE76 = HERE.parent / "phase-76-normalized-adjugate-arithmetic-lock"
PHASE77 = HERE.parent / "phase-77-weyl-limit-point"
PHASE78 = HERE.parent / "phase-78-build-neutral-lp-and-ident"
for path in (PHASE76, PHASE77, PHASE78):
    sys.path.insert(0, str(path))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data  # noqa: E402

GAMMA2 = "21.022039638771554992"
MAX_N = 26
DPS = 70
LAMBDA = mp.mpf("6")


def serial(x: mp.mpf, digits: int = 18) -> str:
    return mp.nstr(x, digits)


def row_metrics(H, idx, L, N):
    _mu, _A, db_idx, inner, x = right_transfer_data(H, idx)
    d = [2 * mp.pi * n / L for n in inner]
    db = 2 * mp.pi * db_idx / L
    xv = [x[j] for j in range(x.rows)]
    q = [dj - db for dj in d]
    c = 1 - mp.fsum(xv)
    qTx = mp.fsum(q[j] * xv[j] for j in range(len(q)))

    n = len(d)
    K = mp.matrix(n, n)
    for a in range(n):
        for b in range(n):
            K[a, b] = (d[a] if a == b else mp.mpf("0")) + x[a] * q[b] / c
    eigvals, _ = mp.eig(K)
    kappas = sorted([mp.re(ev) for ev in eigvals], key=lambda t: abs(t), reverse=True)

    outlier_abs = abs(kappas[0])
    second_abs = abs(kappas[1])
    outlier_fraction = outlier_abs / second_abs
    escape_scale = abs(qTx / c)
    mesh_radius = max(abs(dj) for dj in d)
    # Phase convention, fixed in E79.105: mean_d = pi*(N-1)/LAMBDA.
    # NOTE this is NOT the arithmetic mean of the inner d vector -- the inner
    # index set is symmetric, so mp.fsum(d)/len(d) is identically 0. The
    # E79.105 quantity is the one every alpha_N in E79.105-E79.112 uses, so it
    # is what the extension must use to stay comparable. The mismatch is
    # flagged as an open naming defect in E79.113.
    mean_d = mp.pi * (N - 1) / LAMBDA

    alpha = (outlier_abs - escape_scale - mean_d) / second_abs
    proxy = 1 / mp.sqrt(outlier_fraction) - mesh_radius / second_abs
    gap = alpha - proxy

    return {
        "outlier_abs": outlier_abs,
        "second_abs": second_abs,
        "outlier_fraction": outlier_fraction,
        "escape_scale": escape_scale,
        "mesh_radius": mesh_radius,
        "mean_d": mean_d,
        "outlier_over_escape": outlier_abs / escape_scale,
        "alpha": alpha,
        "proxy": proxy,
        "gap": gap,
        "gap_over_alpha": gap / alpha if alpha != 0 else mp.mpf("nan"),
    }


def sign_pattern(vals):
    return "".join("+" if v > 0 else ("-" if v < 0 else "0") for v in vals)


def crossings(ns, vals):
    """Interpolated sign-change locations."""
    out = []
    for i in range(len(vals) - 1):
        a, b = vals[i], vals[i + 1]
        if (a > 0) != (b > 0) and a != b:
            t = float(-a / (b - a))
            out.append(round(ns[i] + t * (ns[i + 1] - ns[i]), 3))
    return out


def run_case(label, planted):
    mp.mp.dps = DPS
    Hmax, idxmax, L = build_mp(6, MAX_N, DPS, planted=planted)
    rows = []
    for N in range(8, MAX_N + 1, 2):
        H, idx = section(Hmax, idxmax, MAX_N, N)
        m = row_metrics(H, idx, L, N)
        rows.append({"N": N, **{k: serial(v) for k, v in m.items()}})
        print(
            f"  {label:22s} N={N:3d} alpha={serial(m['alpha'], 8)} "
            f"proxy={serial(m['proxy'], 8)} gap={serial(m['gap'], 8)}",
            flush=True,
        )

    ns = [r["N"] for r in rows]
    gaps = [mp.mpf(r["gap"]) for r in rows]
    alphas = [mp.mpf(r["alpha"]) for r in rows]
    rel = [abs(mp.mpf(r["gap_over_alpha"])) for r in rows]

    return {
        "label": label,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
        "summary": {
            "gap_sign_pattern": sign_pattern(gaps),
            "n_sign_changes": sum(
                1 for i in range(len(gaps) - 1) if (gaps[i] > 0) != (gaps[i + 1] > 0)
            ),
            "crossings": crossings(ns, gaps),
            "mean_abs_gap": serial(mp.fsum(abs(g) for g in gaps) / len(gaps)),
            "max_abs_gap": serial(max(abs(g) for g in gaps)),
            "mean_abs_alpha": serial(mp.fsum(abs(a) for a in alphas) / len(alphas)),
            "mean_abs_rel_gap": serial(mp.fsum(rel) / len(rel)),
            "max_abs_rel_gap": serial(max(rel)),
        },
    }


def main():
    out = {
        "statement": "E79.113 extended proxy/gap ladder (N=8..26, recomputed from scratch)",
        "parameters": {"lambda": 6, "max_n": MAX_N, "dps": DPS},
        "definitions": {
            "alpha_N": "(outlier_abs - escape_scale - mean(d)) / second_abs",
            "proxy_N": "1/sqrt(outlier_fraction) - mesh_radius/second_abs",
            "gap_N": "alpha_N - proxy_N",
        },
        "cases": [],
    }
    cases = [
        ("zeta", None),
        ("plant_gamma1_beta030", (GAMMA, "0.30", "5.0")),
        ("plant_gamma2_beta030", (GAMMA2, "0.30", "5.0")),
    ]
    for label, planted in cases:
        case = run_case(label, planted)
        out["cases"].append(case)
        s = case["summary"]
        print(
            f"{label:22s} signs={s['gap_sign_pattern']} "
            f"crossings={s['crossings']} "
            f"mean|gap|={s['mean_abs_gap']} mean|gap/alpha|={s['mean_abs_rel_gap']}",
            flush=True,
        )
    out_path = HERE / "E79_113_proxy_ladder_extension_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
