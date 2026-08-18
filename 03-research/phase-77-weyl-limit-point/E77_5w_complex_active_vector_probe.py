#!/usr/bin/env python3
"""E77.5w full complex active-vector diagnostics for the mod2 spike."""

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
from E77_5k_moving_boundary_four_node_probe import section  # noqa: E402
from E77_5t_weighted_parity_cell_probe import active_detail, q_lookup  # noqa: E402


ACTIVE_ORDER = ("left_outer", "left_boundary", "left_inner", "right_inner", "right_boundary", "right_outer")


def cserial(z, digits=18):
    return {"re": serial(mp.re(z), digits), "im": serial(mp.im(z), digits)}


def carg(z):
    if abs(z) == 0:
        return None
    return serial(mp.arg(z), 18)


def phase_align(vec, anchor):
    if abs(anchor) == 0:
        return list(vec), mp.mpf("0")
    rot = mp.conj(anchor) / abs(anchor)
    return [rot * z for z in vec], mp.arg(anchor)


def l2_norm(vec):
    return mp.sqrt(mp.fsum(abs(z) ** 2 for z in vec))


def normalize(vec):
    nrm = l2_norm(vec)
    if nrm == 0:
        return list(vec), nrm
    return [z / nrm for z in vec], nrm


def dist(v, w):
    return mp.sqrt(mp.fsum(abs(a - b) ** 2 for a, b in zip(v, w)))


def phase_gap(a, b):
    if abs(a) == 0 or abs(b) == 0:
        return None
    return serial(mp.arg(b / a), 18)


def vector_row(H, idx, L, qcase, n, sigma):
    common_nodes = list(range(-n + 2, n - 1))
    active_nodes, contribs = active_detail(H, idx, L, common_nodes, sigma)
    by_node = {node: contribs[j] for j, node in enumerate(active_nodes)}
    nodes = [-n - 1, -n, -n + 1, n - 1, n, n + 1]
    raw = [by_node.get(node, mp.mpc(0)) for node in nodes]
    inserted_anchor = raw[0] + raw[1] + raw[4] + raw[5]
    aligned, anchor_phase = phase_align(raw, inserted_anchor)
    unit, unit_norm = normalize(aligned)
    left = raw[0] + raw[1] + raw[2]
    right = raw[3] + raw[4] + raw[5]
    return {
        "N": n,
        "mod4": n % 4,
        "sigma": serial(sigma),
        "Q": q_lookup(qcase, serial(sigma), n),
        "nodes": nodes,
        "order": list(ACTIVE_ORDER),
        "anchor_phase": serial(anchor_phase, 18),
        "unit_norm": serial(unit_norm, 18),
        "left_right_gap": phase_gap(left, right),
        "outer_gap": phase_gap(raw[0], raw[5]),
        "boundary_gap": phase_gap(raw[1], raw[4]),
        "inner_gap": phase_gap(raw[2], raw[3]),
        "inserted_imbalance_abs": serial(abs((raw[4] + raw[5]) - (raw[0] + raw[1])), 18),
        "inserted_abs": serial(abs(inserted_anchor), 18),
        "aligned_unit": [cserial(z) for z in unit],
    }


def branch_distances(rows):
    out = []
    by_key = {(r["sigma"], r["N"]): r for r in rows}
    by_sigma = sorted({r["sigma"] for r in rows})
    for sigma in by_sigma:
        srows = [r for r in rows if r["sigma"] == sigma]
        for mod4 in [0, 2]:
            branch = sorted([r for r in srows if r["mod4"] == mod4], key=lambda r: r["N"])
            for a, b in zip(branch, branch[1:]):
                out.append(distance_record("successive", sigma, mod4, a, b))
        for n0 in sorted(r["N"] for r in srows if r["mod4"] == 0):
            for n2 in [n0 + 2, n0 - 2]:
                other = by_key.get((sigma, n2))
                here = by_key.get((sigma, n0))
                if here is not None and other is not None and other["mod4"] == 2:
                    out.append(distance_record("cross_mod_near", sigma, None, here, other))
    return out


def complex_vec(row):
    return [mp.mpc(x["re"], x["im"]) for x in row["aligned_unit"]]


def distance_record(kind, sigma, mod4, a, b):
    return {
        "kind": kind,
        "sigma": sigma,
        "mod4": mod4,
        "from_N": a["N"],
        "to_N": b["N"],
        "from_Q": a["Q"],
        "to_Q": b["Q"],
        "distance": serial(dist(complex_vec(a), complex_vec(b)), 18),
    }


def run(q_path: Path, lam_int: int, max_modes: int, dps: int, sigmas, case_filter: str):
    mp.mp.dps = dps
    qdata = json.loads(q_path.read_text(encoding="ascii"))
    result = {"statement": "Full complex active-vector law for common-core updates", "cases": []}
    specs = []
    if case_filter in {"zeta", "both"}:
        specs.append(("zeta-lam6", None, qdata["cases"][0]))
    if case_filter in {"plant", "both"}:
        specs.append(("plant-lam6", (GAMMA, "0.30", "5.0"), qdata["cases"][1]))
    for label, planted, qcase in specs:
        Hm, idxm, L = build_mp(lam_int, max_modes, dps, planted=planted)
        rows = []
        for n in range(8, max_modes - 1, 2):
            H, idx = section(Hm, idxm, max_modes, n + 2)
            for sigma in sigmas:
                rows.append(vector_row(H, idx, L, qcase, n, sigma))
        result["cases"].append({"label": label, "rows": rows, "distances": branch_distances(rows)})
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=Path, default=HERE / "E77_5q_mod4_drift_split_results.json")
    parser.add_argument("--lambda", dest="lam", type=int, default=6)
    parser.add_argument("--max-modes", type=int, default=20)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--sigmas", default="1.0,3.0")
    parser.add_argument("--case", choices=["zeta", "plant", "both"], default="both")
    parser.add_argument("--output", type=Path, default=HERE / "E77_5w_complex_active_vector_results.json")
    args = parser.parse_args()
    sigmas = [mp.mpf(x) for x in args.sigmas.split(",") if x]
    result = run(args.q, args.lam, args.max_modes, args.dps, sigmas, args.case)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
    for case in result["cases"]:
        print(f"CASE {case['label']}")
        for row in case["rows"]:
            if row["sigma"] == "3.0":
                print(
                    "ROW "
                    f"N={row['N']:2d} mod4={row['mod4']} Q={row['Q']} "
                    f"LRgap={row['left_right_gap']} Bgap={row['boundary_gap']} "
                    f"Iabs={row['inserted_abs']}",
                    flush=True,
                )
        for drow in case["distances"]:
            if drow["sigma"] == "3.0":
                print(
                    "DIST "
                    f"{drow['kind']} {drow['from_N']}->{drow['to_N']} "
                    f"mod4={drow['mod4']} dist={drow['distance']}",
                    flush=True,
                )
    print(f"WROTE {args.output}")


if __name__ == "__main__":
    main()
