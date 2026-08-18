#!/usr/bin/env python3
"""Formalization gate for the Paper A local-grammar bifurcation."""

from __future__ import annotations

import json
import math
import subprocess
from collections import defaultdict
from pathlib import Path


SAGE_BIN = Path("/home/trabajo/miniforge3/bin/sage")


def run_sage_json() -> dict[str, object]:
    code = r"""
from sage.all import EllipticCurve, GF, HyperellipticCurve, QQ, cremona_curves, polygen
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
    ("14a1", 5, "supersingular_control"),
]:
    E = EllipticCurve(label)
    ld = E.local_data(probe)
    vals = []
    for obj in [E.c4(), E.c6(), E.discriminant(), E.j_invariant()]:
        v = obj.valuation(probe)
        vals.append(None if str(v) == "+Infinity" else int(v))
    atlas_rows.append({
        "name": f"{label}@{probe}",
        "prime": int(probe),
        "role": role,
        "genus": int(1),
        "v_c4": vals[0],
        "v_c6": vals[1],
        "v_disc": vals[2],
        "v_j": vals[3],
        "kodaira": str(ld.kodaira_symbol()),
        "cp": int(ld.tamagawa_number()),
        "reduction": reduction_label(ld),
        "ainvs": tuple(int(a) for a in ld.minimal_model().ainvs()),
        "supersingular": bool(E.is_supersingular(probe)),
    })

x = polygen(QQ)
H = HyperellipticCurve(x**5 + x + 1)
atlas_rows.append({
    "name": "y^2=x^5+x+1@5",
    "prime": int(5),
    "role": "genus2_control",
    "genus": int(H.genus()),
    "point_counts": [int(v) for v in H.change_ring(GF(5)).count_points(2)],
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


def current_source_rule_packet(prime: int, a_p: int, reduction: str) -> tuple[object, ...]:
    local_factor = 1 if reduction == "additive" else "euler"
    return (math.log(prime), math.log(prime), prime ** (-0.5), a_p, local_factor)


def a5_packet(row: dict[str, object]) -> tuple[object, ...]:
    mod32 = tuple(int(a) % 32 for a in row["ainvs"])
    return (int(row["prime"]), row["v_c4"], row["v_c6"], row["v_disc"], row["v_j"], mod32)


def target_packet(row: dict[str, object]) -> tuple[str, ...]:
    return (str(row["kodaira"]), str(row["cp"]), str(row["reduction"]))


def main() -> None:
    payload = run_sage_json()
    atlas_rows = payload["atlas_rows"]
    family_rows = payload["family_rows"]

    elliptic_atlas = [row for row in atlas_rows if "kodaira" in row]
    cp_pair = [row for row in elliptic_atlas if row["role"] == "cp_pair"]
    left, right = cp_pair

    legacy_row_closed = (
        current_source_rule_packet(int(left["prime"]), 0, str(left["reduction"]))
        == current_source_rule_packet(int(right["prime"]), 0, str(right["reduction"]))
        and target_packet(left) != target_packet(right)
    )

    atlas_groups: dict[tuple[object, ...], set[tuple[str, ...]]] = defaultdict(set)
    for row in elliptic_atlas:
        atlas_groups[a5_packet(row)].add(target_packet(row))
    a5_atlas_live = all(len(targets) == 1 for targets in atlas_groups.values())

    family_groups: dict[tuple[int, ...], set[int]] = defaultdict(set)
    for row in family_rows:
        family_groups[tuple(int(a) % 32 for a in row["ainvs"])].add(int(row["cp"]))
    a5_family_live = all(len(cps) == 1 for cps in family_groups.values())

    a5_not_current = len(family_groups) > 1 and a5_family_live

    print("Paper A branch formalization gate:")
    print(f"LEGACY_ROW_C_STATUS: {'CLOSED' if legacy_row_closed else 'OPEN'}")
    print(f"A5_ATLAS_STATUS: {'LIVE' if a5_atlas_live else 'FAILED'}")
    print(f"A5_FAMILY_STATUS: {'LIVE' if a5_family_live else 'FAILED'}")
    print(f"A5_NOT_CURRENT_RULE: {a5_not_current}")
    print(f"FAMILY_ROWS: {len(family_rows)}")
    print(f"FAMILY_MOD32_CLASSES: {len(family_groups)}")

    print()
    if legacy_row_closed and a5_atlas_live and a5_family_live and a5_not_current:
        print("PAPER_A_LOCAL_BRANCH_STATE: BIFURCATED")
        print("VERDICT: YES")
        print("Reason: the legacy local grammar is closed, while A5 is a live non-legacy branch on real data.")
    else:
        print("PAPER_A_LOCAL_BRANCH_STATE: UNSET")
        print("VERDICT: NO")
        print("Reason: the branch bifurcation is not yet forced by the current real evidence.")


if __name__ == "__main__":
    main()
