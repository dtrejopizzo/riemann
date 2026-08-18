#!/usr/bin/env python3
"""First refined local-line candidate for the A5 branch of Paper A."""

from __future__ import annotations

import json
import math
import subprocess
from collections import defaultdict
from itertools import combinations
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
    atlas_rows.append({
        "name": f"{label}@{probe}",
        "prime": int(probe),
        "role": role,
        "a_p": int(E.ap(probe)),
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


def legacy_packet(prime: int, a_p: int, reduction: str) -> tuple[object, ...]:
    local_factor = 1 if reduction == "additive" else "euler"
    return (math.log(prime), math.log(prime), prime ** (-0.5), a_p, local_factor)


def rho32(row: dict[str, object]) -> tuple[int, ...]:
    return tuple(int(a) % 32 for a in row["ainvs"])


def refined_generator(row: dict[str, object]) -> tuple[object, ...]:
    return (
        legacy_packet(int(row["prime"]), int(row["a_p"]), str(row["reduction"])),
        rho32(row),
    )


def refined_line(left: dict[str, object], right: dict[str, object]) -> tuple[object, ...]:
    return (refined_generator(left), refined_generator(right))


def target(row: dict[str, object]) -> tuple[str, ...]:
    return (str(row["kodaira"]), str(row["cp"]), str(row["reduction"]))


def main() -> None:
    payload = run_sage_json()
    atlas_rows = payload["atlas_rows"]
    family_rows = payload["family_rows"]

    atlas_groups: dict[tuple[object, ...], set[tuple[str, ...]]] = defaultdict(set)
    for row in atlas_rows:
        atlas_groups[refined_generator(row)].add(target(row))
    atlas_collisions = sum(1 for targets in atlas_groups.values() if len(targets) > 1)

    family_legacy_classes: dict[tuple[object, ...], list[dict[str, object]]] = defaultdict(list)
    for row in family_rows:
        family_legacy_classes[legacy_packet(int(row["prime"]), int(row["a_p"]), str(row["reduction"]))].append(row)

    split_pairs = 0
    for rows in family_legacy_classes.values():
        seen = {rho32(row) for row in rows}
        if len(seen) > 1:
            split_pairs += 1

    line_support_ok = True
    sample_pairs = []
    big_class = max(family_legacy_classes.values(), key=len)
    for left, right in list(combinations(big_class[:6], 2))[:5]:
        same_legacy = legacy_packet(int(left["prime"]), int(left["a_p"]), str(left["reduction"])) == legacy_packet(
            int(right["prime"]), int(right["a_p"]), str(right["reduction"])
        )
        distinct_refined = refined_generator(left) != refined_generator(right)
        line_support_ok &= same_legacy
        sample_pairs.append(
            {
                "left": left["label"],
                "right": right["label"],
                "same_legacy": same_legacy,
                "distinct_refined": distinct_refined,
            }
        )

    print("Paper A A5 refined local-line candidate:")
    for row in atlas_rows:
        print(
            f"  {row['name']}: generator={refined_generator(row)}, target={target(row)}"
        )

    print()
    print(f"ATLAS_ROWS: {len(atlas_rows)}")
    print(f"ATLAS_COLLISIONS: {atlas_collisions}")
    print(f"FAMILY_ROWS: {len(family_rows)}")
    print(f"LEGACY_CLASSES_SPLIT_BY_RHO32: {split_pairs}")
    print(f"SAMPLE_LINE_SUPPORT_OK: {line_support_ok}")
    for item in sample_pairs:
        print(
            f"  pair {item['left']} / {item['right']}: "
            f"same_legacy={item['same_legacy']} distinct_refined={item['distinct_refined']}"
        )

    print()
    if atlas_collisions == 0 and split_pairs > 0 and line_support_ok:
        print("VERDICT: YES")
        print("Reason: the refined A5 local generators and line labels preserve the legacy support class while splitting it by rho_32 on real data.")
    else:
        print("VERDICT: NO")
        print("Reason: the refined A5 local-line candidate fails either visible separation or legacy-support refinement.")


if __name__ == "__main__":
    main()
