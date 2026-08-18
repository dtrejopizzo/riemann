#!/usr/bin/env python3
"""Binary S3 gate for attempt A5 using local minimal-model residues mod 32."""

from __future__ import annotations

import json
import subprocess
from collections import defaultdict
from pathlib import Path


SAGE_BIN = Path("/home/trabajo/miniforge3/bin/sage")


def run_sage_json() -> dict[str, object]:
    code = r"""
from sage.all import EllipticCurve, GF, HyperellipticCurve, QQ, polygen
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

    rows.append({
        "kind": "elliptic",
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
    mod32 = tuple(int(a) % 32 for a in row["ainvs"])
    return (
        int(row["prime"]),
        row["v_c4"],
        row["v_c6"],
        row["v_disc"],
        row["v_j"],
        mod32,
    )


def target_packet(row: dict[str, object]) -> tuple[str, ...]:
    return (str(row["kodaira"]), str(row["cp"]), str(row["reduction"]))


def main() -> None:
    payload = run_sage_json()
    rows = payload["rows"]

    elliptic_rows = [row for row in rows if row["kind"] == "elliptic"]
    genus2_rows = [row for row in rows if int(row["genus"]) >= 2]
    supersingular_rows = [row for row in elliptic_rows if bool(row["supersingular"])]

    assert len(rows) >= 5
    assert len(elliptic_rows) >= 4
    assert genus2_rows
    assert supersingular_rows

    grouped_targets: dict[tuple[object, ...], set[tuple[str, ...]]] = defaultdict(set)
    for row in elliptic_rows:
        grouped_targets[source_packet(row)].add(target_packet(row))

    collisions = {
        packet: sorted(targets)
        for packet, targets in grouped_targets.items()
        if len(targets) > 1
    }

    print("A5 fixed atlas:")
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
    print(f"HAS_GENUS_GE_2_CONTROL: {bool(genus2_rows)}")
    print(f"HAS_SUPERSINGULAR_CONTROL: {bool(supersingular_rows)}")
    print(f"ELLIPTIC_ROWS: {len(elliptic_rows)}")
    print(f"COLLISION_COUNT: {len(collisions)}")
    if collisions:
        for packet, targets in collisions.items():
            print(f"  collision source={packet} -> targets={targets}")

    print()
    if not collisions:
        print("VERDICT: YES")
        print("Reason: the valuative plus mod-32 minimal-model residue packet separates every elliptic target state on the fixed atlas.")
    else:
        print("VERDICT: NO")
        print("Reason: at least one elliptic source packet still maps to multiple target states on the fixed atlas.")


if __name__ == "__main__":
    main()
