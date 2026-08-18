#!/usr/bin/env python3
"""First positive Paper A source-extension candidate for the A5 branch."""

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
    atlas_rows.append({
        "kind": "elliptic",
        "name": f"{label}@{probe}",
        "prime": int(probe),
        "role": role,
        "genus": int(1),
        "a_p": int(E.ap(probe)),
        "kodaira": str(ld.kodaira_symbol()),
        "cp": int(ld.tamagawa_number()),
        "reduction": reduction_label(ld),
        "ainvs": tuple(int(a) for a in ld.minimal_model().ainvs()),
        "supersingular": bool(E.is_supersingular(probe)),
    })

x = polygen(QQ)
H = HyperellipticCurve(x**5 + x + 1)
atlas_rows.append({
    "kind": "hyperelliptic",
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


def legacy_packet(prime: int, a_p: int, reduction: str) -> tuple[object, ...]:
    local_factor = 1 if reduction == "additive" else "euler"
    return (math.log(prime), math.log(prime), prime ** (-0.5), a_p, local_factor)


def residue_symbol(ainvs: list[int] | tuple[int, ...]) -> tuple[int, ...]:
    return tuple(int(a) % 32 for a in ainvs)


def a5_extension_packet(row: dict[str, object]) -> tuple[object, ...]:
    return (
        legacy_packet(int(row["prime"]), int(row["a_p"]), str(row["reduction"])),
        residue_symbol(row["ainvs"]),
    )


def target_packet(row: dict[str, object]) -> tuple[str, ...]:
    return (str(row["kodaira"]), str(row["cp"]), str(row["reduction"]))


def main() -> None:
    payload = run_sage_json()
    atlas_rows = payload["atlas_rows"]
    family_rows = payload["family_rows"]

    elliptic_atlas = [row for row in atlas_rows if row["kind"] == "elliptic"]
    genus2_controls = [row for row in atlas_rows if int(row["genus"]) >= 2]
    supersingular_controls = [row for row in elliptic_atlas if bool(row["supersingular"])]

    atlas_groups: dict[tuple[object, ...], set[tuple[str, ...]]] = defaultdict(set)
    for row in elliptic_atlas:
        atlas_groups[a5_extension_packet(row)].add(target_packet(row))
    atlas_collisions = sum(1 for targets in atlas_groups.values() if len(targets) > 1)

    family_groups: dict[tuple[object, ...], set[int]] = defaultdict(set)
    legacy_groups: dict[tuple[object, ...], set[tuple[int, ...]]] = defaultdict(set)
    for row in family_rows:
        ext = a5_extension_packet(row)
        family_groups[ext].add(int(row["cp"]))
        legacy_groups[legacy_packet(int(row["prime"]), int(row["a_p"]), str(row["reduction"]))].add(
            residue_symbol(row["ainvs"])
        )
    family_mixed = sum(1 for cps in family_groups.values() if len(cps) > 1)
    refined_legacy_classes = sum(1 for residues in legacy_groups.values() if len(residues) > 1)

    print("Paper A A5 source-extension candidate:")
    for row in atlas_rows:
        if row["kind"] == "elliptic":
            print(
                f"  {row['name']}: legacy={legacy_packet(int(row['prime']), int(row['a_p']), str(row['reduction']))}, "
                f"rho32={residue_symbol(row['ainvs'])}, target={target_packet(row)}"
            )
        else:
            print(
                f"  {row['name']}: genus={row['genus']}, point_counts={tuple(row['point_counts'])}"
            )

    print()
    print(f"ATLAS_SIZE: {len(atlas_rows)}")
    print(f"HAS_GENUS_GE_2_CONTROL: {bool(genus2_controls)}")
    print(f"HAS_SUPERSINGULAR_CONTROL: {bool(supersingular_controls)}")
    print(f"ATLAS_COLLISIONS: {atlas_collisions}")
    print(f"FAMILY_ROWS: {len(family_rows)}")
    print(f"FAMILY_MIXED_EXTENSION_CLASSES: {family_mixed}")
    print(f"LEGACY_CLASSES_REFINED_BY_RHO32: {refined_legacy_classes}")

    print()
    if atlas_collisions == 0 and family_mixed == 0 and refined_legacy_classes > 0:
        print("VERDICT: YES")
        print("Reason: the A5 extension refines the current source packet by adjoining rho_32 and separates the visible target on both atlas and enlarged IV* family.")
    else:
        print("VERDICT: NO")
        print("Reason: the proposed A5 source extension does not yet pass the visible refinement/separation tests.")


if __name__ == "__main__":
    main()
