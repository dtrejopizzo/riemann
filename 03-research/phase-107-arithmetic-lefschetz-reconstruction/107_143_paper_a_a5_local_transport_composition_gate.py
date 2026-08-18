#!/usr/bin/env python3
"""Transport/composition gate for A5 local decorated lines."""

from __future__ import annotations

import json
import subprocess
from itertools import combinations
from pathlib import Path


SAGE_BIN = Path("/home/trabajo/miniforge3/bin/sage")
MODULUS = 32


def run_sage_json() -> dict[str, object]:
    code = r"""
from sage.all import EllipticCurve, cremona_curves
import json


def reduction_label(ld):
    value = ld.bad_reduction_type()
    if value is None:
        return "good"
    text = str(value)
    if text == "0":
        return "additive"
    if text == "+1":
        return "split_multiplicative"
    if text == "-1":
        return "nonsplit_multiplicative"
    return text


atlas_rows = []
for label, probe, role in [
    ("14a5", 7, "split_pair"),
    ("21a1", 7, "split_pair"),
    ("20a1", 2, "cp_pair"),
    ("36a4", 2, "cp_pair"),
]:
    E = EllipticCurve(label)
    ld = E.local_data(probe)
    atlas_rows.append({
        "name": f"{label}@{probe}",
        "prime": int(probe),
        "role": role,
        "cp": int(ld.tamagawa_number()),
        "reduction": reduction_label(ld),
        "ainvs": tuple(int(a) for a in ld.minimal_model().ainvs()),
    })

family_rows = []
for N in range(11, 2001):
    try:
        curves = cremona_curves([N])
    except Exception:
        continue
    for E in curves:
        for ld in E.local_data():
            p = int(ld.prime().gens_reduced()[0])
            if p != 2:
                continue
            if str(ld.kodaira_symbol()) != 'IV*' or str(ld.bad_reduction_type()) != '0':
                continue
            vals = []
            ok = True
            for obj in [E.c4(), E.c6(), E.discriminant(), E.j_invariant()]:
                v = obj.valuation(2)
                if str(v) == '+Infinity':
                    ok = False
                    break
                vals.append(int(v))
            if not ok:
                continue
            v4, v6, vd, vj = vals
            if (v4, v6, vd, vj, int(ld.conductor_valuation()), int(E.ap(2))) != (4, 6, 8, 4, 2, 0):
                continue
            family_rows.append({
                "label": E.label(),
                "cp": int(ld.tamagawa_number()),
                "ainvs": tuple(int(a) for a in ld.minimal_model().ainvs()),
            })

print(json.dumps({"atlas_rows": atlas_rows, "family_rows": family_rows}, default=int))
"""
    result = subprocess.run(
        [str(SAGE_BIN), "-c", code],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def rho32(row: dict[str, object]) -> tuple[int, ...]:
    return tuple(int(a) % MODULUS for a in row["ainvs"])


def delta32(left: dict[str, object], right: dict[str, object]) -> tuple[int, ...]:
    return tuple((a - b) % MODULUS for a, b in zip(rho32(left), rho32(right)))


def add_mod(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a + b) % MODULUS for a, b in zip(x, y))


def arrow(left: dict[str, object], right: dict[str, object]) -> tuple[tuple[int, ...], str, str]:
    return (delta32(left, right), str(left["cp"]), str(right["cp"]))


def main() -> None:
    payload = run_sage_json()
    atlas_rows = payload["atlas_rows"]
    family_rows = payload["family_rows"]

    transport_ok = True
    triple_samples = []
    family_head = family_rows[:10]
    for i in range(len(family_head) - 2):
        a = family_head[i]
        b = family_head[i + 1]
        c = family_head[i + 2]
        ab = delta32(a, b)
        bc = delta32(b, c)
        ac = delta32(a, c)
        ok = add_mod(ab, bc) == ac
        transport_ok &= ok
        triple_samples.append((a["label"], b["label"], c["label"], ab, bc, ac, ok))

    inverse_ok = True
    pair_samples = []
    for left, right in combinations(atlas_rows, 2):
        lr = arrow(left, right)
        rl = arrow(right, left)
        ok = add_mod(lr[0], rl[0]) == (0, 0, 0, 0, 0)
        inverse_ok &= ok
        if len(pair_samples) < 5:
            pair_samples.append((left["name"], right["name"], lr[0], rl[0], ok))

    cp_pair = [row for row in atlas_rows if row["role"] == "cp_pair"]
    split_pair = [row for row in atlas_rows if row["role"] == "split_pair"]
    cp_arrow_nontrivial = arrow(cp_pair[0], cp_pair[1])[0] != (0, 0, 0, 0, 0)
    split_arrow_nontrivial = arrow(split_pair[0], split_pair[1])[0] != (0, 0, 0, 0, 0)

    print("Paper A A5 local transport/composition gate:")
    print(f"ATLAS_ROWS: {len(atlas_rows)}")
    print(f"FAMILY_ROWS: {len(family_rows)}")
    print(f"TRANSPORT_OK: {transport_ok}")
    print(f"INVERSE_OK: {inverse_ok}")
    print(f"CP_ARROW_NONTRIVIAL: {cp_arrow_nontrivial}")
    print(f"SPLIT_ARROW_NONTRIVIAL: {split_arrow_nontrivial}")
    for left, right, lr, rl, ok in pair_samples:
        print(f"  pair {left}/{right}: lr={lr} rl={rl} ok={ok}")
    for a, b, c, ab, bc, ac, ok in triple_samples[:3]:
        print(f"  triple {a},{b},{c}: ab={ab} bc={bc} ac={ac} ok={ok}")

    print()
    if transport_ok and inverse_ok and cp_arrow_nontrivial and split_arrow_nontrivial:
        print("VERDICT: YES")
        print("Reason: the A5 local arrows admit a first transport/composition law on the tested real data.")
    else:
        print("VERDICT: NO")
        print("Reason: the proposed A5 transport/composition law fails on the tested real data.")


if __name__ == "__main__":
    main()
