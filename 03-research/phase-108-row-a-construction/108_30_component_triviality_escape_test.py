#!/usr/bin/env python3
"""108.30 -- component-triviality escape test. Plain python3, no Sage.

Curve data for 20a1@2 and 36a4@2 is taken verbatim from 107_144 (cited, not
recomputed). 14a1@5 and 11a1@5 triviality is derived from conductors alone.
The genus-2 control is computed directly over GF(5) with no dependency.
"""

from __future__ import annotations


# ---------------------------------------------------------------------------
# 1. Forcing pair -- data cited from 107_144 SS3-4 (not recomputed)
# ---------------------------------------------------------------------------

FORCING_PAIR = {
    "20a1": {
        "p": 2,
        "component_group_order": 3,   # 107_144 (3.1): c_2 = 3
        "witness_point": "P_+ = (0, 2)",
        "witness_order": 3,
        "smooth_reduction": False,    # 107_144 SS3: does not have smooth reduction at 2
    },
    "36a4": {
        "p": 2,
        "component_group_order": 1,   # 107_144 (3.1): c_2 = 1
        "witness_point": "T = (-6, 0)",
        "witness_order": 2,
        "smooth_reduction": True,     # forced: only one component exists
    },
}


def check_forcing_pair_gives_counterexample() -> bool:
    row = FORCING_PAIR["20a1"]
    # a witness point of order > 1, in a component group of order > 1, that
    # is NOT smooth-reducing is exactly a non-identity-component realized
    # divisor (P) - (O).
    return (
        row["component_group_order"] > 1
        and row["witness_order"] > 1
        and not row["smooth_reduction"]
    )


# ---------------------------------------------------------------------------
# 2. Good-reduction controls -- derived from conductors, no lookup needed
#    beyond the conductor itself (elementary factorization).
# ---------------------------------------------------------------------------

CONDUCTORS = {
    "14a1": 14,   # = 2 * 7
    "11a1": 11,
}


def good_reduction_at(label: str, p: int) -> bool:
    N = CONDUCTORS[label]
    return N % p != 0


def check_controls_trivial() -> dict:
    out = {}
    for label in ("14a1", "11a1"):
        out[label] = good_reduction_at(label, 5)
    return out


# ---------------------------------------------------------------------------
# 3. Genus-2 control over GF(5): f = x^5 + x + 1, no Sage.
# ---------------------------------------------------------------------------

P = 5


def poly_trim(a: list) -> list:
    a = a[:]
    while len(a) > 1 and a[-1] % P == 0:
        a.pop()
    return [c % P for c in a]


def poly_mod_reduce(a: list) -> list:
    return [c % P for c in a]


def poly_deg(a: list) -> int:
    a = poly_trim(a)
    if len(a) == 1 and a[0] == 0:
        return -1
    return len(a) - 1


def poly_sub(a: list, b: list) -> list:
    n = max(len(a), len(b))
    a = a + [0] * (n - len(a))
    b = b + [0] * (n - len(b))
    return poly_trim([(x - y) % P for x, y in zip(a, b)])


def poly_mul_scalar(a: list, c: int) -> list:
    return poly_trim([(x * c) % P for x in a])


def poly_mul_xk(a: list, k: int) -> list:
    return poly_trim([0] * k + a)


def modinv(a: int, p: int) -> int:
    return pow(a % p, p - 2, p)


def poly_divmod(a: list, b: list):
    a = poly_trim(a)
    b = poly_trim(b)
    db = poly_deg(b)
    assert db >= 0, "division by zero polynomial"
    inv_lead = modinv(b[-1], P)
    rem = a[:]
    q = [0] * max(1, len(a) - len(b) + 1)
    while poly_deg(rem) >= db:
        dr = poly_deg(rem)
        shift = dr - db
        coeff = (rem[dr] * inv_lead) % P
        q[shift] = (q[shift] + coeff) % P
        sub_term = poly_mul_xk(poly_mul_scalar(b, coeff), shift)
        rem = poly_sub(rem, sub_term)
    return poly_trim(q), poly_trim(rem)


def poly_gcd(a: list, b: list) -> list:
    a, b = poly_trim(a), poly_trim(b)
    while not (poly_deg(b) == -1):
        _, r = poly_divmod(a, b)
        a, b = b, r
    return a


def derivative(coeffs: list) -> list:
    # coeffs[i] is coefficient of x^i
    d = [(i * coeffs[i]) % P for i in range(1, len(coeffs))]
    return poly_trim(d) if d else [0]


def check_genus2_control() -> dict:
    # f = x^5 + x + 1  -> coeffs [1,1,0,0,0,1] (const term first)
    f = [1, 1, 0, 0, 0, 1]
    fprime = derivative(f)
    g = poly_gcd(f, fprime)
    is_constant = poly_deg(g) == 0
    genus = (poly_deg(f) - 1) // 2
    return {
        "f_deg": poly_deg(f),
        "fprime": fprime,
        "fprime_is_nonzero_constant": fprime == [1],
        "gcd_deg": poly_deg(g),
        "squarefree": is_constant,
        "genus": genus,
    }


def main() -> None:
    counterexample = check_forcing_pair_gives_counterexample()
    controls = check_controls_trivial()
    genus2 = check_genus2_control()

    print("Forcing pair (source: 107_144 SS3-4, cited not recomputed):")
    for label, row in FORCING_PAIR.items():
        print(f"  {label}@{row['p']}: |component group|={row['component_group_order']}, "
              f"witness={row['witness_point']} order={row['witness_order']}, "
              f"smooth_reduction={row['smooth_reduction']}")
    print(f"  => non-identity-component realized divisor exists on 20a1: "
          f"{'YES' if counterexample else 'NO'}")
    print()
    print("Good-reduction controls (derived from conductor alone):")
    for label, ok in controls.items():
        print(f"  {label}@5: good reduction (5 does not divide conductor "
              f"{CONDUCTORS[label]}) = {ok}  => component group trivial => "
              f"triviality holds vacuously")
    print()
    print("Genus-2 control over GF(5), f = x^5 + x + 1:")
    print(f"  f' = {genus2['fprime']}  (nonzero constant: "
          f"{genus2['fprime_is_nonzero_constant']})")
    print(f"  gcd(f, f') has degree {genus2['gcd_deg']} "
          f"(squarefree: {genus2['squarefree']})")
    print(f"  genus = floor((deg f - 1)/2) = {genus2['genus']}")

    reading_a_well_posed = False  # SS1: no map from D_f / U_s to Neron models exists

    all_controls_trivial = all(controls.values())
    genus2_ok = (
        genus2["fprime_is_nonzero_constant"]
        and genus2["squarefree"]
        and genus2["genus"] == 2
    )

    verdict_reading_b_universal_triviality = not counterexample  # NO if counterexample found

    print()
    print(f"READING_A_LITERAL_D_F_WELL_POSED: {'YES' if reading_a_well_posed else 'NOT_WELL_POSED'}")
    print(f"CONTROLS_TRIVIAL_AS_EXPECTED: {'YES' if all_controls_trivial else 'NO'}")
    print(f"GENUS2_CONTROL_OK: {'YES' if genus2_ok else 'NO'}")
    print(f"READING_B_COUNTEREXAMPLE_FOUND (20a1, P_+): {'YES' if counterexample else 'NO'}")
    print(f"UNIVERSAL_COMPONENT_TRIVIALITY_READING_B: "
          f"{'YES' if verdict_reading_b_universal_triviality else 'NO'}")

    all_checks_consistent = (
        counterexample
        and all_controls_trivial
        and genus2_ok
        and not reading_a_well_posed
    )

    print()
    print(f"VERDICT: {'NO' if all_checks_consistent else 'INCONCLUSIVE'}")

    if not all_checks_consistent:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
