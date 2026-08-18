#!/usr/bin/env python3
"""Closure gate for current row (c) under the current local target."""

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
        "prime": int(prime),
        "role": role,
        "genus": int(1),
        "a_p": int(E.ap(prime)),
        "kodaira": str(ld.kodaira_symbol()),
        "cp": int(ld.tamagawa_number()),
        "reduction": reduction_label(ld),
        "supersingular": bool(E.is_supersingular(prime)),
    })

x = polygen(QQ)
H = HyperellipticCurve(x**5 + x + 1)
rows.append({
    "kind": "hyperelliptic",
    "name": "y^2=x^5+x+1@5",
    "prime": int(5),
    "role": "genus2_control",
    "genus": int(H.genus()),
    "point_counts": [int(v) for v in H.change_ring(GF(5)).count_points(2)],
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


def source_packet(row: dict[str, object]) -> tuple[object, ...]:
    prime = int(row["prime"])
    reduction = str(row["reduction"])
    local_factor = "1" if reduction == "additive" else "euler"
    return (math.log(prime), math.log(prime), prime ** (-0.5), int(row["a_p"]), local_factor)


def target_packet(row: dict[str, object]) -> tuple[str, ...]:
    return (str(row["kodaira"]), str(row["cp"]), str(row["reduction"]))


def main() -> None:
    payload = run_sage_json()
    rows = payload["rows"]

    elliptic_rows = [row for row in rows if row["kind"] == "elliptic"]
    forcing_rows = [row for row in elliptic_rows if row["role"] == "forcing_pair"]
    genus2_rows = [row for row in rows if int(row["genus"]) >= 2]
    supersingular_rows = [row for row in elliptic_rows if bool(row["supersingular"])]

    assert len(rows) >= 5
    assert len(forcing_rows) == 2
    assert genus2_rows
    assert supersingular_rows

    left, right = forcing_rows
    same_source = source_packet(left) == source_packet(right)
    same_kodaira = str(left["kodaira"]) == str(right["kodaira"])
    same_reduction = str(left["reduction"]) == str(right["reduction"])
    different_cp = int(left["cp"]) != int(right["cp"])
    different_target = target_packet(left) != target_packet(right)

    print("Current row (c) closure atlas:")
    for row in rows:
        if row["kind"] == "elliptic":
            print(
                f"  {row['name']}: role={row['role']}, supersingular={row['supersingular']}, "
                f"source={source_packet(row)}, target={target_packet(row)}"
            )
        else:
            print(
                f"  {row['name']}: role={row['role']}, genus={row['genus']}, "
                f"point_counts={tuple(row['point_counts'])}"
            )

    print()
    print(f"ATLAS_SIZE: {len(rows)}")
    print(f"TARGET_RETAINS_CP: {different_cp}")
    print(f"HAS_GENUS_GE_2_CONTROL: {bool(genus2_rows)}")
    print(f"HAS_SUPERSINGULAR_CONTROL: {bool(supersingular_rows)}")
    print(f"FORCING_PAIR_SAME_SOURCE: {same_source}")
    print(f"FORCING_PAIR_SAME_KODAIRA: {same_kodaira}")
    print(f"FORCING_PAIR_SAME_REDUCTION: {same_reduction}")
    print(f"FORCING_PAIR_DIFFERENT_TARGET: {different_target}")

    print()
    if same_source and same_kodaira and same_reduction and different_cp and different_target:
        print("ROW_C_STATUS: CLOSED_BY_NO_GO")
        print("VERDICT: NO")
        print("Reason: under the current target with c_p, the current finite source-rule vocabulary collapses the forcing pair on the fixed real atlas.")
    else:
        print("ROW_C_STATUS: OPEN")
        print("VERDICT: YES")
        print("Reason: the fixed real atlas does not currently force closure of row (c) by no-go.")


if __name__ == "__main__":
    main()
