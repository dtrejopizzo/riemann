#!/usr/bin/env python3
"""First decorated determinant-line candidate for the A5 branch."""

from __future__ import annotations

import json
import math
import subprocess
from collections import defaultdict
from pathlib import Path


SAGE_BIN = Path("/home/trabajo/miniforge3/bin/sage")


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
    vals = []
    for obj in [E.c4(), E.c6(), E.discriminant(), E.j_invariant()]:
        v = obj.valuation(probe)
        vals.append(None if str(v) == "+Infinity" else int(v))
    atlas_rows.append({
        "name": f"{label}@{probe}",
        "prime": int(probe),
        "role": role,
        "a_p": int(E.ap(probe)),
        "v_c4": vals[0],
        "v_c6": vals[1],
        "v_disc": vals[2],
        "v_j": vals[3],
        "kodaira": str(ld.kodaira_symbol()),
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
                "prime": int(2),
                "a_p": int(E.ap(2)),
                "cp": int(ld.tamagawa_number()),
                "reduction": reduction_label(ld),
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


def legacy_scalar(row: dict[str, object]) -> tuple[object, ...]:
    prime = int(row["prime"])
    local_factor = 1 if str(row["reduction"]) == "additive" else "euler"
    return (math.log(prime), math.log(prime), prime ** (-0.5), int(row["a_p"]), local_factor)


def rho32(row: dict[str, object]) -> tuple[int, ...]:
    return tuple(int(a) % 32 for a in row["ainvs"])


def decorated_line(row: dict[str, object]) -> tuple[object, ...]:
    return (legacy_scalar(row), rho32(row))


def target(row: dict[str, object]) -> tuple[str, ...]:
    return (str(row["kodaira"]), str(row["cp"]), str(row["reduction"]))


def main() -> None:
    payload = run_sage_json()
    atlas_rows = payload["atlas_rows"]
    family_rows = payload["family_rows"]

    atlas_groups: dict[tuple[object, ...], set[tuple[str, ...]]] = defaultdict(set)
    for row in atlas_rows:
        atlas_groups[decorated_line(row)].add(target(row))
    atlas_collisions = sum(1 for targets in atlas_groups.values() if len(targets) > 1)

    family_groups: dict[tuple[object, ...], set[int]] = defaultdict(set)
    scalar_groups: dict[tuple[object, ...], set[tuple[int, ...]]] = defaultdict(set)
    for row in family_rows:
        family_groups[decorated_line(row)].add(int(row["cp"]))
        scalar_groups[legacy_scalar(row)].add(rho32(row))

    mixed_decorated = sum(1 for cps in family_groups.values() if len(cps) > 1)
    refined_scalar_classes = sum(1 for residues in scalar_groups.values() if len(residues) > 1)
    scalar_projection_constant = len(scalar_groups) == 1

    print("Paper A A5 decorated determinant-line candidate:")
    for row in atlas_rows:
        print(
            f"  {row['name']}: scalar={legacy_scalar(row)}, rho32={rho32(row)}, decorated={decorated_line(row)}, target={target(row)}"
        )

    print()
    print(f"ATLAS_COLLISIONS: {atlas_collisions}")
    print(f"FAMILY_ROWS: {len(family_rows)}")
    print(f"MIXED_DECORATED_CLASSES: {mixed_decorated}")
    print(f"REFINED_SCALAR_CLASSES: {refined_scalar_classes}")
    print(f"SCALAR_PROJECTION_CONSTANT_ON_IVSTAR: {scalar_projection_constant}")

    print()
    if atlas_collisions == 0 and mixed_decorated == 0 and refined_scalar_classes > 0 and scalar_projection_constant:
        print("VERDICT: YES")
        print("Reason: the decorated determinant-line candidate preserves the legacy scalar projection while rho_32 splits the blind IV* source class on real data.")
    else:
        print("VERDICT: NO")
        print("Reason: the decorated determinant-line candidate fails either scalar compatibility or visible separation.")


if __name__ == "__main__":
    main()
