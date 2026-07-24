#!/usr/bin/env python3
"""Audit whether the three-dimensional package can be reduced to one or two coordinates."""

from __future__ import annotations

import json
from pathlib import Path
import sys

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1] / "phase-76-normalized-adjugate-arithmetic-lock"
sys.path.insert(0, str(ROOT))

from E78_128_package_span_probe import PLANTED, package  # noqa: E402
from P76_002_mp_entry_audit import build_mp  # noqa: E402


def serialize(x, digits=24):
    return mp.nstr(x, digits)


def inner(a, b):
    return (a.transpose_conj() * b)[0]


def norm(v):
    return mp.sqrt(mp.fsum(abs(v[j]) ** 2 for j in range(v.rows)))


def coordinate_fractions(target, basis_map, names):
    ortho = []
    kept = []
    for name in names:
        w = mp.matrix(basis_map[name])
        for q in ortho:
            w -= inner(q, w) * q
        nw = norm(w)
        if nw > mp.mpf("1e-20"):
            ortho.append(w / nw)
            kept.append(name)
    target_norm_sq = mp.fsum(abs(target[j]) ** 2 for j in range(target.rows))
    coords = []
    total = mp.mpf("0")
    for name, q in zip(kept, ortho):
        a = inner(q, target)
        frac = abs(a) ** 2 / target_norm_sq
        total += frac
        coords.append({"name": name, "fraction": serialize(frac), "coefficient": serialize(a)})
    return coords, total


def span_score(target, basis):
    ortho = []
    for vec in basis:
        w = mp.matrix(vec)
        for q in ortho:
            w -= inner(q, w) * q
        nw = norm(w)
        if nw > mp.mpf("1e-20"):
            ortho.append(w / nw)
    fit = mp.matrix([0] * target.rows)
    for q in ortho:
        fit += inner(q, target) * q
    resid = target - fit
    return 1 - norm(resid) / norm(target), len(ortho)


def run_case(label, planted):
    rows = []
    for n_modes in (8, 12):
        mp.mp.dps = 50
        H, idx, L = build_mp(6, n_modes, 50, planted=planted)
        A = H[1:-1, 1:-1]
        _vals, vecs = mp.eigsy(A)
        v2 = vecs[:, 2]
        inner_idx = idx[1:-1]
        slots = [j for j, n in enumerate(inner_idx) if n >= 0][:6]
        target = mp.matrix([v2[j] for j in slots])
        pkg = package(H, idx, L, planted)
        subv = {name: mp.matrix([pkg[name][j] for j in slots]) for name in ("u", "v", "c")}
        coords, total = coordinate_fractions(target, subv, ("u", "v", "c"))
        pair_rows = []
        for combo in (("u", "v"), ("u", "c"), ("v", "c")):
            score, dim = span_score(target, [subv[name] for name in combo])
            pair_rows.append({"combo": list(combo), "dim": dim, "score": serialize(score)})
        rows.append(
            {
                "N": n_modes,
                "coordinates": coords,
                "total_capture": serialize(total),
                "pair_scores": pair_rows,
            }
        )
    return {"label": label, "rows": rows}


def main():
    result = {
        "statement": "E78.129 package-dimension audit",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
        "quantity": "orthogonal package-coordinate fractions and two-dimensional capture scores",
    }
    out_path = Path(__file__).with_name("E78_129_package_dimension_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
