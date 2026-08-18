#!/usr/bin/env python3
"""Classical Jacobian control for Phase 107 Work Package III-B."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


SAGE_BIN = Path("/home/trabajo/miniforge3/bin/sage")


def run_sage() -> dict[str, object]:
    code = r'''
from sage.all import EllipticCurve, GF, HyperellipticCurve, PolynomialRing, QQ
import json


def elliptic_record(label):
    E = EllipticCurve(label)
    torsion = E.torsion_points()
    torsion_heights = [
        float(P.height()) for P in torsion
    ]
    generators = list(E.gens())
    samples = []
    if len(generators) == 1:
        P = generators[0]
        for n in (-3, -2, -1, 1, 2, 3):
            Q = n * P
            samples.append({
                "coeffs": [int(n)],
                "height": float(Q.height()),
            })
    elif len(generators) == 2:
        P, Q = generators
        for a, b in [(-1, -1), (-1, 1), (1, -1), (1, 1), (2, 1), (1, 2)]:
            R = a * P + b * Q
            samples.append({
                "coeffs": [int(a), int(b)],
                "height": float(R.height()),
            })
    gram = []
    if generators:
        matrix = E.height_pairing_matrix(generators)
        gram = [
            [float(matrix[i, j]) for j in range(matrix.ncols())]
            for i in range(matrix.nrows())
        ]
    return {
        "label": label,
        "rank": int(E.rank()),
        "torsion_order": int(E.torsion_subgroup().order()),
        "torsion_heights": torsion_heights,
        "generators": [str(P) for P in generators],
        "sample_heights": samples,
        "height_gram": gram,
    }


paper0 = EllipticCurve(GF(5), [1, 1])
paper0_points = [
    {
        "point": str(P),
        "order": int(P.order()),
    }
    for P in paper0.points()
]

R = PolynomialRing(GF(5), "x")
x = R.gen()
genus2 = HyperellipticCurve(x**5 + x + 1)
J = genus2.jacobian()(GF(5))
points = genus2.rational_points()
genus2_records = []
for P in points[1:]:
    cls = J(P)
    genus2_records.append({
        "point": str(P),
        "class": str(cls),
        "order": int(cls.order()),
    })

pair_checks = []
for P in points[1:]:
    if int(P[2]) == 0:
        continue
    x0 = P[0]
    y0 = P[1]
    mate = genus2([x0, -y0, 1])
    pair_checks.append({
        "point": str(P),
        "mate": str(mate),
        "inverse": bool(J(mate) == -J(P)),
    })

print(json.dumps({
    "elliptic_q": [elliptic_record(label) for label in ["20a1", "36a4", "11a1", "37a1", "389a1"]],
    "paper0": {
        "order": int(paper0.order()),
        "points": paper0_points,
    },
    "genus2": {
        "genus": int(genus2.genus()),
        "jacobian_order": int(J.order()),
        "classes": genus2_records,
        "inverse_pairs": pair_checks,
    },
}))
'''
    result = subprocess.run(
        [str(SAGE_BIN), "-c", code],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def determinant_1x1_or_2x2(matrix: list[list[float]]) -> float:
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    raise ValueError("Only rank-1 or rank-2 Gram matrices are expected")


def near_zero(x: float, tol: float = 1e-12) -> bool:
    return abs(x) <= tol


def main() -> None:
    data = run_sage()

    elliptic_q = data["elliptic_q"]
    torsion_real_kernel_only = True
    free_height_nondegenerate = True
    curves_checked = len(elliptic_q)

    print("Elliptic controls over Q:")
    for row in elliptic_q:
        label = row["label"]
        rank = row["rank"]
        tors = row["torsion_order"]
        print(f"  {label}: rank={rank}, torsion={tors}")
        if not all(near_zero(h) for h in row["torsion_heights"]):
            torsion_real_kernel_only = False
        if rank > 0:
            if not all(sample["height"] > 1e-9 for sample in row["sample_heights"]):
                free_height_nondegenerate = False
            det = determinant_1x1_or_2x2(row["height_gram"])
            print(f"    height Gram determinant={det:.12f}")
            if det <= 1e-9:
                free_height_nondegenerate = False

    paper0 = data["paper0"]
    paper0_jacobian_control = (
        paper0["order"] == 9
        and any(point["order"] == 9 for point in paper0["points"])
        and any(point["order"] == 3 for point in paper0["points"])
    )
    print(f"Paper 0 control E/F5 order={paper0['order']}")

    genus2 = data["genus2"]
    genus2_orders = [row["order"] for row in genus2["classes"]]
    genus2_jacobian_separation = (
        genus2["genus"] == 2
        and genus2["jacobian_order"] == 36
        and any(order == 2 for order in genus2_orders)
        and any(order == 6 for order in genus2_orders)
        and all(row["inverse"] for row in genus2["inverse_pairs"])
    )
    print(
        f"Genus-2 control J(F5) order={genus2['jacobian_order']}, "
        f"class orders={genus2_orders}"
    )

    divisor_to_picard_faithful_mod_torsion = (
        torsion_real_kernel_only and free_height_nondegenerate
    )
    verdict = (
        divisor_to_picard_faithful_mod_torsion
        and paper0_jacobian_control
        and genus2_jacobian_separation
    )

    print()
    print(f"ELLIPTIC_CURVES_CHECKED: {curves_checked}")
    print(
        "TORSION_REAL_KERNEL_ONLY: "
        + ("YES" if torsion_real_kernel_only else "NO")
    )
    print(
        "FREE_HEIGHT_NONDEGENERATE: "
        + ("YES" if free_height_nondegenerate else "NO")
    )
    print(
        "DIVISOR_TO_PICARD_FAITHFUL_MOD_TORSION: "
        + ("YES" if divisor_to_picard_faithful_mod_torsion else "NO")
    )
    print(
        "PAPER0_JACOBIAN_CONTROL: "
        + ("YES" if paper0_jacobian_control else "NO")
    )
    print(
        "GENUS2_JACOBIAN_SEPARATION: "
        + ("YES" if genus2_jacobian_separation else "NO")
    )
    print("VERDICT: " + ("YES" if verdict else "NO"))


if __name__ == "__main__":
    main()
