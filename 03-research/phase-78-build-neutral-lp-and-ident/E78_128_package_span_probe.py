#!/usr/bin/env python3
"""Audit whether the five-shell mode-2 profile lies in a low-dimensional coupled span."""

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


def serialize(x, digits=24):
    return mp.nstr(x, digits)


def sine_symbol(t, L, lam, planted):
    value = symbols(t, L, lam)[0]
    if planted is None:
        return value
    gamma0, beta, strength = (mp.mpf(x) for x in planted)
    spectral_point = gamma0 - 1j * beta
    planted_sine = mp.quad(lambda y: mp.sin(t * y) * mp.cos(spectral_point * y), [0, L])
    return value + strength * 2 * mp.re(planted_sine)


def package(H, idx, L, planted):
    lam = mp.mpf(6)
    A = H[1:-1, 1:-1]
    inner = idx[1:-1]
    d = [2 * mp.pi * n / L for n in inner]
    D = mp.diag(d)
    db_idx = idx[-1]
    db = 2 * mp.pi * db_idx / L
    s = mp.matrix([sine_symbol(dj, L, lam, planted) for dj in d])
    one = mp.matrix([1 for _ in d])
    u = mp.lu_solve(A, s)
    v = mp.lu_solve(A, one)
    sb = sine_symbol(db, L, lam, planted)
    Rb = (D - db * mp.eye(D.rows)) ** -1
    source = s - sb * one
    g = Rb * source
    c = mp.lu_solve(A, g)
    p = (v.T * g)[0]
    q = (u.T * g)[0]
    aa = 2 / L + 4 * p / L**2
    bb = -2 * sb / L - 4 * q / L**2
    h = aa * u + bb * v
    return {"u": u, "v": v, "c": c, "h": h}


def inner(a, b):
    return (a.T * b)[0]


def norm(v):
    return mp.sqrt(mp.fsum(abs(v[j]) ** 2 for j in range(v.rows)))


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
    mp.mp.dps = 50
    rows = []
    for n_modes in (8, 12):
        H, idx, L = build_mp(6, n_modes, 50, planted=planted)
        A = H[1:-1, 1:-1]
        _vals, vecs = mp.eigsy(A)
        v2 = vecs[:, 2]
        inner_idx = idx[1:-1]
        slots = [j for j, n in enumerate(inner_idx) if n >= 0][:6]
        target = mp.matrix([v2[j] for j in slots])
        pkg = package(H, idx, L, planted)
        subv = {name: mp.matrix([pkg[name][j] for j in slots]) for name in pkg}
        combos = [
            ("u",),
            ("v",),
            ("c",),
            ("h",),
            ("u", "v"),
            ("u", "c"),
            ("v", "c"),
            ("u", "v", "c"),
            ("u", "v", "h"),
            ("u", "c", "h"),
        ]
        combo_rows = []
        for names in combos:
            score, dim = span_score(target, [subv[n] for n in names])
            combo_rows.append({"combo": list(names), "dim": dim, "score": serialize(score)})
        rows.append({"N": n_modes, "combos": combo_rows})
    return {"label": label, "rows": rows}


def main():
    result = {
        "statement": "E78.128 package-span audit",
        "cases": [
            run_case("zeta", None),
            run_case("plant", PLANTED),
        ],
        "quantity": "fraction of the five-shell mode-2 profile captured by low-dimensional spans of {u,v,c,h}",
    }
    out_path = Path(__file__).with_name("E78_128_package_span_results.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
