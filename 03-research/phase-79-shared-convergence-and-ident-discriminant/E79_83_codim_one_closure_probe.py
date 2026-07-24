#!/usr/bin/env python3
"""E79.83 - codim-one closure defect and cloud coherence audit.

Measures, on the lambda=6 ladder:

  c_N = 1 - sum_j x_j
  sum_x = sum_j x_j

for several builds, together with the stepwise coherence fraction of the
spectral-shift cloud:

  coh_frac = Pxpos / total

from the E78.154 M_N-profile audit.  The purpose is to test whether "small c"
is a robust zeta-only codimension-one signature, and whether it travels with
cloud coherence across more than one planted off-line falsifier.
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
sys.path.insert(0, str(PHASE76))
sys.path.insert(0, str(PHASE77))
sys.path.insert(0, str(PHASE78))

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402
from E77_3c_two_generator_ident_probe import right_transfer_data  # noqa: E402
from E78_153_spectral_shift_counting_sum_probe import nu_atoms  # noqa: E402
from E78_154_MN_profile_probe import analyze  # noqa: E402


GAMMA1 = "14.134725141734693790"
GAMMA2 = "21.022039638771554992"


def serial(x: mp.mpf, digits: int = 18) -> str:
    return mp.nstr(x, digits)


def section_closure(H, idx):
    _mu, _A, _db_idx, _inner, x = right_transfer_data(H, idx)
    sum_x = mp.fsum(x[j] for j in range(x.rows))
    c = 1 - sum_x
    return {
        "sum_x": sum_x,
        "c": c,
        "abs_c": abs(c),
        "minus_log10_abs_c": mp.inf if c == 0 else -mp.log10(abs(c)),
    }


def run_case(label, planted, lam_int=6, max_n=18, dps=60):
    mp.mp.dps = dps
    Hmax, idxmax, L = build_mp(lam_int, max_n, dps, planted=planted)
    section_rows = []
    step_rows = []

    for n in range(8, max_n + 1, 2):
        Hn, idxn = section(Hmax, idxmax, max_n, n)
        clos = section_closure(Hn, idxn)
        section_rows.append(
            {
                "N": n,
                "sum_x": serial(clos["sum_x"]),
                "c": serial(clos["c"]),
                "abs_c": serial(clos["abs_c"]),
                "minus_log10_abs_c": None
                if clos["minus_log10_abs_c"] == mp.inf
                else serial(clos["minus_log10_abs_c"]),
            }
        )

    for n in range(8, max_n - 1, 2):
        Hn, idxn = section(Hmax, idxmax, max_n, n)
        Hm, idxm = section(Hmax, idxmax, max_n, n + 2)
        atoms_n, _ = nu_atoms(Hn, idxn, L)
        atoms_m, _ = nu_atoms(Hm, idxm, L)
        prof = analyze(atoms_n, atoms_m, L, n)
        total = prof["total"]
        coh = prof["Pxpos"] / total if total else mp.mpf(0)
        edge = prof["edge"] / total if total else mp.mpf(0)
        step_rows.append(
            {
                "from_N": n,
                "to_N": n + 2,
                "coherence_fraction": serial(coh),
                "edge_fraction": serial(edge),
                "total_bound_mass": serial(total),
                "peak_mass": serial(prof["peakval"]),
                "peak_x": serial(prof["peakx"]),
            }
        )

    zeta_like_count = sum(1 for row in step_rows if mp.mpf(row["coherence_fraction"]) > mp.mpf("0.99"))
    small_c_count = sum(1 for row in section_rows if mp.mpf(row["abs_c"]) < mp.mpf("1e-5"))
    return {
        "label": label,
        "lambda": lam_int,
        "dps": dps,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "section_rows": section_rows,
        "step_rows": step_rows,
        "summary": {
            "small_c_sections_lt_1e-5": small_c_count,
            "coherent_steps_gt_0.99": zeta_like_count,
            "max_abs_c": serial(max(mp.mpf(r["abs_c"]) for r in section_rows)),
            "min_abs_c": serial(min(mp.mpf(r["abs_c"]) for r in section_rows)),
            "min_coherence_fraction": serial(min(mp.mpf(r["coherence_fraction"]) for r in step_rows)),
            "max_coherence_fraction": serial(max(mp.mpf(r["coherence_fraction"]) for r in step_rows)),
        },
    }


def main():
    out = {
        "statement": "E79.83 codim-one closure defect and cloud coherence audit",
        "parameters": {"lambda": 6, "max_n": 18, "dps": 60},
        "cases": [],
    }
    cases = [
        ("zeta", None),
        ("plant_gamma1_beta030", (GAMMA1, "0.30", "5.0")),
        ("plant_gamma2_beta030", (GAMMA2, "0.30", "5.0")),
    ]
    for label, planted in cases:
        case = run_case(label, planted)
        out["cases"].append(case)
        print(
            f"{label:20s} max|c|={case['summary']['max_abs_c']:>12s} "
            f"min|c|={case['summary']['min_abs_c']:>12s} "
            f"min coh={case['summary']['min_coherence_fraction']:>10s} "
            f"coh>0.99={case['summary']['coherent_steps_gt_0.99']}",
            flush=True,
        )
    out_path = HERE / "E79_83_codim_one_closure_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
