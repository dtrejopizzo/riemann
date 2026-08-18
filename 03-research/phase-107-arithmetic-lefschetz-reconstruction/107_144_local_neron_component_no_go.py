#!/usr/bin/env python3
"""Real-curve no-go for the legacy local row and descent test for A5."""

from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path


SAGE_BIN = Path("/home/trabajo/miniforge3/bin/sage")


def run_sage() -> dict[str, object]:
    code = r'''
from sage.all import EllipticCurve, GF, HyperellipticCurve, NumberField, PolynomialRing, QQ, ZZ, polygen
import json


def local_row(label, p):
    E = EllipticCurve(label)
    ld = E.local_data(p)
    vals = []
    for value in (E.c4(), E.c6(), E.discriminant(), E.j_invariant()):
        vals.append(int(value.valuation(p)))
    reduction = str(ld.bad_reduction_type())
    local_factor = "1" if reduction == "0" else "nontrivial"
    return {
        "label": label,
        "p": int(p),
        "v_c4": vals[0],
        "v_c6": vals[1],
        "v_disc": vals[2],
        "v_j": vals[3],
        "kodaira": str(ld.kodaira_symbol()),
        "conductor_exponent": int(ld.conductor_valuation()),
        "ap": int(E.ap(p)),
        "local_factor": local_factor,
        "cp": int(ld.tamagawa_number()),
        "rank": int(E.rank()),
        "torsion_order": int(E.torsion_subgroup().order()),
    }


forcing = [local_row("20a1", 2), local_row("36a4", 2)]

E20 = EllipticCurve("20a1").local_minimal_model(2)
P20 = E20(0, 2)
E36 = EllipticCurve("36a4").local_minimal_model(2)
T36 = E36(-6, 0)

R = PolynomialRing(QQ, "x")
x = R.gen()
K = NumberField(x**2 + x + 1, "w")
w = K.gen()
prime = K.prime_above(2)

base_change = []
for label in ("20a1", "36a4"):
    EK = EllipticCurve(label).base_extend(K)
    ld = EK.local_data(prime)
    base_change.append({
        "label": label,
        "kodaira": str(ld.kodaira_symbol()),
        "cp": int(ld.tamagawa_number()),
    })

E36K = EllipticCurve("36a4").base_extend(K)
Q36 = E36K(-9, -12*w - 6)
Q36_conj = E36K(-9, 12*w + 6)

rho_tests = []
for label in ("20a1", "36a4"):
    E = EllipticCurve(label).local_minimal_model(2)
    F = E.rst_transform(1, 0, 0)
    rho_tests.append({
        "label": label,
        "before": [int(ZZ(a) % 32) for a in E.ainvs()],
        "after": [int(ZZ(a) % 32) for a in F.ainvs()],
        "before_v_disc": int(E.discriminant().valuation(2)),
        "after_v_disc": int(F.discriminant().valuation(2)),
        "after_integral": bool(F.is_local_integral_model(2)),
        "isomorphic": bool(E.is_isomorphic(F)),
    })

split_E = EllipticCurve("14a5")
nonsplit_E = EllipticCurve("21a1")
super_E = EllipticCurve("14a1")
hx = polygen(QQ)
H = HyperellipticCurve(hx**5 + hx + 1)

controls = {
    "split": str(split_E.local_data(7).bad_reduction_type()),
    "nonsplit": str(nonsplit_E.local_data(7).bad_reduction_type()),
    "supersingular": bool(super_E.is_supersingular(5)),
    "genus2": int(H.genus()),
    "genus2_counts": [int(v) for v in H.change_ring(GF(5)).count_points(2)],
}

print(json.dumps({
    "forcing": forcing,
    "P20": {
        "order": int(P20.order()),
        "smooth_reduction": bool(P20.has_good_reduction(2)),
    },
    "T36": {
        "order": int(T36.order()),
        "smooth_reduction": bool(T36.has_good_reduction(2)),
    },
    "extension": {
        "polynomial": "x^2+x+1",
        "ramification_index": int(prime.ramification_index()),
        "residue_degree": int(prime.residue_class_degree()),
        "base_change": base_change,
        "Q36_order": int(Q36.order()),
        "Q36_smooth_reduction": bool(Q36.has_good_reduction(prime)),
        "Q36_conjugate_is_negative": bool(Q36_conj == -Q36),
    },
    "rho_tests": rho_tests,
    "controls": controls,
}))
'''
    result = subprocess.run(
        [str(SAGE_BIN), "-c", code],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def invert(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(matrix)
    augmented = [
        row[:] + [Fraction(int(i == j)) for j in range(n)]
        for i, row in enumerate(matrix)
    ]
    for column in range(n):
        pivot = next(i for i in range(column, n) if augmented[i][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            scale = augmented[row][column]
            augmented[row] = [
                left - scale * right
                for left, right in zip(augmented[row], augmented[column])
            ]
    return [row[n:] for row in augmented]


def affine_e6() -> tuple[list[list[int]], list[int]]:
    matrix = [[-2 if i == j else 0 for j in range(7)] for i in range(7)]
    edges = ((1, 3), (3, 4), (4, 5), (5, 6), (2, 4), (0, 2))
    for i, j in edges:
        matrix[i][j] = matrix[j][i] = 1
    multiplicities = [1, 1, 2, 2, 3, 2, 1]
    return matrix, multiplicities


def source_packet(row: dict[str, object]) -> tuple[object, ...]:
    return (
        row["p"],
        row["v_c4"],
        row["v_c6"],
        row["v_disc"],
        row["v_j"],
        row["kodaira"],
        row["conductor_exponent"],
        row["ap"],
        row["local_factor"],
    )


def main() -> None:
    data = run_sage()
    forcing = data["forcing"]
    first, second = forcing

    affine, multiplicities = affine_e6()
    kernel = [
        sum(affine[i][j] * multiplicities[j] for j in range(7))
        for i in range(7)
    ]
    assert kernel == [0] * 7

    # Remove the affine identity node. The negative is the E6 Cartan matrix.
    cartan = [
        [Fraction(-affine[i][j]) for j in range(1, 7)]
        for i in range(1, 7)
    ]
    inverse = invert(cartan)
    correction_left = inverse[0][0]
    correction_right = inverse[5][5]
    assert correction_left == correction_right == Fraction(4, 3)

    same_source = source_packet(first) == source_packet(second)
    component_orders_differ = first["cp"] == 3 and second["cp"] == 1
    rational_witness = (
        data["P20"]["order"] == 3
        and not data["P20"]["smooth_reduction"]
        and data["T36"]["smooth_reduction"]
    )
    extension = data["extension"]
    explicit_splitting = (
        extension["ramification_index"] == 1
        and extension["residue_degree"] == 2
        and all(row["cp"] == 3 for row in extension["base_change"])
        and extension["Q36_order"] == 3
        and not extension["Q36_smooth_reduction"]
        and extension["Q36_conjugate_is_negative"]
    )

    local_pairing_different = component_orders_differ and rational_witness
    target_component_data_necessary = (
        same_source and local_pairing_different and explicit_splitting
    )

    rho_tests = data["rho_tests"]
    rho_descends = all(
        row["before"] == row["after"]
        for row in rho_tests
        if row["after_integral"]
        and row["before_v_disc"] == row["after_v_disc"]
    )
    same_curve_changed_rho = any(
        row["isomorphic"]
        and row["after_integral"]
        and row["before_v_disc"] == row["after_v_disc"]
        and row["before"] != row["after"]
        for row in rho_tests
    )
    rho_from_zeta = not same_curve_changed_rho

    controls = data["controls"]
    controls_ok = (
        controls["split"] == "1"
        and controls["nonsplit"] == "-1"
        and controls["supersingular"]
        and controls["genus2"] >= 2
    )

    verdict = (
        target_component_data_necessary
        and same_source
        and local_pairing_different
        and not rho_descends
        and not rho_from_zeta
        and controls_ok
    )

    print("Forcing pair:")
    for row in forcing:
        print(f"  {row['label']}@{row['p']}: source={source_packet(row)}, c_p={row['cp']}")
    print(f"Affine E6 kernel vector: {tuple(multiplicities)}")
    print(f"Nonidentity component correction: {correction_left} * log(2)")
    print(
        "Unramified splitting extension: "
        f"{extension['polynomial']}, e={extension['ramification_index']}, "
        f"f={extension['residue_degree']}"
    )
    for row in rho_tests:
        print(f"  rho32 {row['label']}: {tuple(row['before'])} -> {tuple(row['after'])}")
    print()
    print(f"TARGET_COMPONENT_DATA_NECESSARY: {'YES' if target_component_data_necessary else 'NO'}")
    print(f"SOURCE_PACKET_EQUAL: {'YES' if same_source else 'NO'}")
    print(f"LOCAL_PAIRING_DIFFERENT: {'YES' if local_pairing_different else 'NO'}")
    print(f"RHO32_DESCENDS: {'YES' if rho_descends else 'NO'}")
    print(f"RHO32_DEFINABLE_FROM_ZETA: {'YES' if rho_from_zeta else 'NO'}")
    print(
        "LEGACY_ROW_C: "
        + ("CLOSED_NO_GO" if target_component_data_necessary else "REOPENED_REDUCED_TARGET")
    )
    print(
        "A5_STATUS: "
        + ("ADMISSIBLE" if rho_descends and rho_from_zeta else "REJECTED_NONINVARIANT")
    )
    print(f"VERDICT: {'YES' if verdict else 'NO'}")


if __name__ == "__main__":
    main()
