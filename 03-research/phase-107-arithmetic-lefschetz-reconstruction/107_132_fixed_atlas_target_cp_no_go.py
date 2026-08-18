#!/usr/bin/env python3
"""Fixed-atlas c_p no-go for the current Phase 107 local target."""

from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path


SAGE_BIN = Path("/home/trabajo/miniforge3/bin/sage")


def run_sage_json() -> dict[str, object]:
    code = r"""
from sage.all import EllipticCurve, HyperellipticCurve, GF, QQ, polygen
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


rows = []
for label, prime, role in [
    ("20a1", 2, "forcing_pair"),
    ("36a4", 2, "forcing_pair"),
    ("14a1", 5, "supersingular_control"),
    ("11a1", 5, "ordinary_control"),
]:
    E = EllipticCurve(label)
    ld = E.local_data(prime)
    rows.append({
        "kind": "elliptic",
        "name": f"{label}@{prime}",
        "label": label,
        "prime": int(prime),
        "role": role,
        "genus": 1,
        "a_p": int(E.ap(prime)),
        "kodaira": str(ld.kodaira_symbol()),
        "cp": int(ld.tamagawa_number()),
        "reduction": reduction_label(ld),
        "supersingular": bool(E.is_supersingular(prime)),
    })

x = polygen(QQ)
H = HyperellipticCurve(x**5 + x + 1)
H5 = H.change_ring(GF(5))
rows.append({
    "kind": "hyperelliptic",
    "name": "y^2=x^5+x+1@5",
    "prime": int(5),
    "role": "genus2_control",
    "genus": int(H.genus()),
    "point_counts": [int(v) for v in H5.count_points(2)],
})

print(json.dumps({"rows": rows}, default=int))
"""
    result = subprocess.run(
        [str(SAGE_BIN), "-c", code],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def elliptic_source_packet(row: dict[str, object]) -> tuple[object, ...]:
    prime = int(row["prime"])
    reduction = str(row["reduction"])
    local_factor = "1" if reduction == "additive" else "euler"
    return (math.log(prime), math.log(prime), prime ** (-0.5), int(row["a_p"]), local_factor)


def elliptic_target(row: dict[str, object]) -> tuple[str, ...]:
    return (str(row["kodaira"]), str(row["cp"]), str(row["reduction"]))


def main() -> None:
    payload = run_sage_json()
    rows = payload["rows"]

    elliptic_rows = [row for row in rows if row["kind"] == "elliptic"]
    forcing_rows = [row for row in elliptic_rows if row["role"] == "forcing_pair"]
    supersingular_rows = [row for row in elliptic_rows if row["supersingular"]]
    genus2_rows = [row for row in rows if int(row["genus"]) >= 2]

    assert len(rows) >= 5
    assert len(forcing_rows) == 2
    assert supersingular_rows
    assert genus2_rows

    first, second = forcing_rows
    first_source = elliptic_source_packet(first)
    second_source = elliptic_source_packet(second)
    first_target = elliptic_target(first)
    second_target = elliptic_target(second)

    same_source = first_source == second_source
    same_kodaira = first["kodaira"] == second["kodaira"]
    same_reduction = first["reduction"] == second["reduction"]
    different_cp = first["cp"] != second["cp"]
    different_target = first_target != second_target

    print("Fixed atlas:")
    for row in rows:
        if row["kind"] == "elliptic":
            source = elliptic_source_packet(row)
            target = elliptic_target(row)
            print(
                f"  {row['name']}: genus={row['genus']}, role={row['role']}, "
                f"supersingular={row['supersingular']}, source={source}, target={target}"
            )
        else:
            print(
                f"  {row['name']}: genus={row['genus']}, role={row['role']}, "
                f"point_counts={tuple(row['point_counts'])}"
            )

    print()
    print(f"ATLAS_SIZE: {len(rows)}")
    print(f"HAS_GENUS_GE_2: {bool(genus2_rows)}")
    print(f"HAS_SUPERSINGULAR_CONTROL: {bool(supersingular_rows)}")
    print(f"FORCING_PAIR_SAME_SOURCE: {same_source}")
    print(f"FORCING_PAIR_SAME_KODAIRA: {same_kodaira}")
    print(f"FORCING_PAIR_SAME_REDUCTION: {same_reduction}")
    print(f"FORCING_PAIR_DIFFERENT_CP: {different_cp}")
    print(f"FORCING_PAIR_DIFFERENT_TARGET: {different_target}")

    print()
    if same_source and same_kodaira and same_reduction and different_cp and different_target:
        print("VERDICT: NO")
        print("Reason: on the fixed real atlas, the current local target keeps c_p, and the current source-rule packet collapses the forcing pair.")
    else:
        print("VERDICT: YES")
        print("Reason: the fixed atlas does not witness a c_p obstruction for the current local target.")


if __name__ == "__main__":
    main()
