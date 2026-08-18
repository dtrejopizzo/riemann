#!/usr/bin/env python3
"""E79.115 - precision control for the large rows of the E79.114 ladder.

E79.114 produced an erratic zeta tail (alpha jumping 0.663 -> 0.825 -> 0.390
across N=32,34,36). Before that is interpreted as a real breakdown of the
regime, it must be shown NOT to be arithmetic noise.

The E79.113 dps control was run only at N<=18. It was never valid evidence
about N=28..36. K_N has large dynamic range (c is tiny, outlier ~1e3), and
second_abs is the second-largest-modulus eigenvalue of an mp.eig on a matrix
of order ~35, so eigenvalue resolution is the obvious suspect.

This probe recomputes the large rows at THREE precisions and reports whether
alpha/gap are stable. If they move with dps, E79.114 rows 28..36 are void.

It also reports the spectral separation |kappa_1|/|kappa_2| and the gap
between kappa_2 and kappa_3, since a near-degenerate kappa_2/kappa_3 pair
would make second_abs ill-conditioned and is the mechanism most likely to
produce exactly the observed jumpiness.
"""

from __future__ import annotations

import importlib.util
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
from E77_3c_two_generator_ident_probe import right_transfer_data  # noqa: E402

LAMBDA = mp.mpf("6")
MAX_N = 36
TEST_ROWS = (26, 28, 30, 32, 34, 36)
PRECISIONS = (70, 110, 150)


def serial(x, digits=25):
    return mp.nstr(x, digits)


def row_full(H, idx, L, N):
    """row_metrics plus the conditioning diagnostics E79.114 lacked."""
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
    kap = sorted([mp.re(ev) for ev in eigvals], key=lambda t: abs(t), reverse=True)

    outlier_abs, second_abs, third_abs = abs(kap[0]), abs(kap[1]), abs(kap[2])
    escape_scale = abs(qTx / c)
    mesh_radius = max(abs(dj) for dj in d)
    mean_d = mp.pi * (N - 1) / LAMBDA
    alpha = (outlier_abs - escape_scale - mean_d) / second_abs
    proxy = 1 / mp.sqrt(outlier_abs / second_abs) - mesh_radius / second_abs

    # max imaginary part: K_N is non-symmetric; kappa_j are asserted REAL
    # (E78.152). If eig starts returning complex pairs the reading is invalid.
    max_imag = max(abs(mp.im(ev)) for ev in eigvals)

    return {
        "alpha": alpha,
        "gap": alpha - proxy,
        "second_abs": second_abs,
        "outlier_abs": outlier_abs,
        "abs_c": abs(c),
        "sep_1_2": outlier_abs / second_abs,
        "sep_2_3": second_abs / third_abs,
        "max_abs_imag_eig": max_imag,
    }


def main():
    results = {}
    for dps in PRECISIONS:
        mp.mp.dps = dps
        Hmax, idxmax, L = build_mp(6, MAX_N, dps, planted=None)
        for N in TEST_ROWS:
            H, idx = section(Hmax, idxmax, MAX_N, N)
            m = row_full(H, idx, L, N)
            results.setdefault(N, {})[dps] = {k: serial(v) for k, v in m.items()}
            print(
                f"  N={N:3d} dps={dps:4d} alpha={mp.nstr(m['alpha'],12)} "
                f"gap={mp.nstr(m['gap'],10)} sep23={mp.nstr(m['sep_2_3'],8)} "
                f"maximag={mp.nstr(m['max_abs_imag_eig'],4)}",
                flush=True,
            )

    verdict_rows = {}
    for N in TEST_ROWS:
        a = [mp.mpf(results[N][p]["alpha"]) for p in PRECISIONS]
        spread = max(a) - min(a)
        rel = spread / abs(a[-1]) if a[-1] != 0 else spread
        stable = rel < mp.mpf("1e-12")
        verdict_rows[N] = {
            "alpha_by_dps": {str(p): results[N][p]["alpha"] for p in PRECISIONS},
            "alpha_rel_spread": serial(rel),
            "STABLE": bool(stable),
            "sep_2_3_at_max_dps": results[N][PRECISIONS[-1]]["sep_2_3"],
            "max_abs_imag_at_max_dps": results[N][PRECISIONS[-1]]["max_abs_imag_eig"],
        }
        print(f"N={N:3d} rel_spread={mp.nstr(rel,6)} STABLE={stable}", flush=True)

    unstable = [N for N in TEST_ROWS if not verdict_rows[N]["STABLE"]]
    out = {
        "statement": "E79.115 precision control on E79.114 large rows",
        "precisions": list(PRECISIONS),
        "rows": {str(N): verdict_rows[N] for N in TEST_ROWS},
        "unstable_rows": unstable,
        "verdict": "ALL-STABLE" if not unstable else f"UNSTABLE at N={unstable}",
    }
    (HERE / "E79_115_large_row_precision_control_results.json").write_text(
        json.dumps(out, indent=2) + "\n", encoding="ascii"
    )
    print(f"VERDICT: {out['verdict']}")
    print("WROTE E79_115_large_row_precision_control_results.json")


if __name__ == "__main__":
    main()
