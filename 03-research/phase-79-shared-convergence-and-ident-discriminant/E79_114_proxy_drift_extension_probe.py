#!/usr/bin/env python3
"""E79.114 - decide the E79.113 drift question by pushing the ladder to N=36.

E79.113 found that the zeta relative proxy gap |gap_N/alpha_N| rises
monotonically over the last four audited rows:

    N=20: 0.0303 -> N=22: 0.0717 -> N=24: 0.0787 -> N=26: 0.0867

Two readings are consistent with that:

    (D-continues) the proxy is a finite-window fit whose error keeps growing,
    (D-turns)     the rise is a local bump and the tail turns over.

This probe computes rows N=24..36 and reports which. Rows 24 and 26 are
recomputed as OVERLAP ANCHORS against E79_113_proxy_ladder_extension_results
.json -- if they disagree, nothing else in this file may be trusted.

Both builds per phase discipline: zeta and plant_gamma1_beta030.
Reuses row_metrics from the E79.113 probe unchanged (same alpha/proxy/gap
definitions, same E79.105 mean_d convention).
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

_spec = importlib.util.spec_from_file_location(
    "e79_113", HERE / "E79_113_proxy_ladder_extension_probe.py"
)
_e113 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_e113)

row_metrics = _e113.row_metrics
serial = _e113.serial
sign_pattern = _e113.sign_pattern
crossings = _e113.crossings

from P76_002_mp_entry_audit import build_mp  # noqa: E402
from E78_9_w_quotient_delta_probe import section  # noqa: E402
from E77_3c_two_generator_ident_probe import GAMMA  # noqa: E402

MAX_N = 36
MIN_N = 24
DPS = 70
ANCHOR_FILE = "E79_113_proxy_ladder_extension_results.json"
ANCHOR_ROWS = (24, 26)
# RELATIVE tolerance. The anchor file stores gaps via serial(..., digits=18),
# so a correct rerun can only agree to ~1e-18 relative -- an absolute 1e-25
# test is unpassable by construction and flags spurious MISMATCHes.
ANCHOR_TOL = mp.mpf("1e-16")


def load_anchors(label):
    data = json.loads((HERE / ANCHOR_FILE).read_text())
    for case in data["cases"]:
        if case["label"] == label:
            return {r["N"]: mp.mpf(r["gap"]) for r in case["rows"] if r["N"] in ANCHOR_ROWS}
    return {}


def run_case(label, planted):
    mp.mp.dps = DPS
    anchors = load_anchors(label)
    Hmax, idxmax, L = build_mp(6, MAX_N, DPS, planted=planted)
    rows, anchor_report = [], []
    for N in range(MIN_N, MAX_N + 1, 2):
        H, idx = section(Hmax, idxmax, MAX_N, N)
        m = row_metrics(H, idx, L, N)
        rows.append({"N": N, **{k: serial(v) for k, v in m.items()}})
        rel = abs(m["gap"] / m["alpha"])
        note = ""
        if N in anchors:
            delta = abs(m["gap"] - anchors[N])
            rel_delta = delta / abs(anchors[N]) if anchors[N] != 0 else delta
            ok = rel_delta < ANCHOR_TOL
            anchor_report.append(
                {
                    "N": N,
                    "abs_delta_vs_E79_113": serial(delta),
                    "rel_delta_vs_E79_113": serial(rel_delta),
                    "match": bool(ok),
                }
            )
            note = f"  [ANCHOR {'OK' if ok else 'MISMATCH'} delta={mp.nstr(delta, 3)}]"
        print(
            f"  {label:22s} N={N:3d} alpha={serial(m['alpha'], 8)} "
            f"gap={serial(m['gap'], 8)} |gap/alpha|={mp.nstr(rel, 5)}{note}",
            flush=True,
        )

    ns = [r["N"] for r in rows]
    gaps = [mp.mpf(r["gap"]) for r in rows]
    rel = [abs(mp.mpf(r["gap_over_alpha"])) for r in rows]

    # Is the relative gap monotone increasing across the NEW rows (N>=26)?
    new = [(n, v) for n, v in zip(ns, rel) if n >= 26]
    mono_inc = all(new[i][1] < new[i + 1][1] for i in range(len(new) - 1))
    mono_dec = all(new[i][1] > new[i + 1][1] for i in range(len(new) - 1))
    turned = any(
        new[i][1] > new[i + 1][1] for i in range(len(new) - 1)
    ) and any(new[i][1] < new[i + 1][1] for i in range(len(new) - 1))

    return {
        "label": label,
        "planted": None
        if planted is None
        else {"gamma": planted[0], "beta": planted[1], "strength": planted[2]},
        "rows": rows,
        "anchor_check": anchor_report,
        "summary": {
            "gap_sign_pattern": sign_pattern(gaps),
            "crossings": crossings(ns, gaps),
            "rel_gap_by_N": {str(n): serial(v, 8) for n, v in zip(ns, rel)},
            "new_rows_monotone_increasing": bool(mono_inc),
            "new_rows_monotone_decreasing": bool(mono_dec),
            "new_rows_turned_over": bool(turned),
            "max_abs_rel_gap": serial(max(rel)),
            "verdict": "D-continues"
            if mono_inc
            else ("D-turns" if (mono_dec or turned) else "inconclusive"),
        },
    }


def main():
    out = {
        "statement": "E79.114 proxy drift extension, N=24..36",
        "question": "does |gap_N/alpha_N| keep rising past N=26 (D-continues) or turn over (D-turns)?",
        "parameters": {"lambda": 6, "min_n": MIN_N, "max_n": MAX_N, "dps": DPS},
        "cases": [],
    }
    for label, planted in [("zeta", None), ("plant_gamma1_beta030", (GAMMA, "0.30", "5.0"))]:
        case = run_case(label, planted)
        out["cases"].append(case)
        s = case["summary"]
        bad = [a for a in case["anchor_check"] if not a["match"]]
        print(
            f"{label:22s} VERDICT={s['verdict']} max|gap/alpha|={s['max_abs_rel_gap']} "
            f"anchors={'OK' if not bad else 'MISMATCH ' + str(bad)}",
            flush=True,
        )
    out_path = HERE / "E79_114_proxy_drift_extension_results.json"
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="ascii")
    print(f"WROTE {out_path.name}")


if __name__ == "__main__":
    main()
