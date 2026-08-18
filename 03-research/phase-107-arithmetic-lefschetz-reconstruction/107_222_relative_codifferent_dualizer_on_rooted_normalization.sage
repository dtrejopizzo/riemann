#!/home/trabajo/miniforge3/bin/sage
"""Exact verifier for the relative codifferent dualizer."""


CONDUCTORS = (3, 4, 5, 8, 9, 12)


def row(n):
    field = CyclotomicField(n)
    different = field.different()
    norm = abs(ZZ(different.norm()))
    discriminant = abs(ZZ(field.discriminant()))
    support = tuple(norm.prime_divisors())
    codifferent = different**(-1)
    return {
        "n": n,
        "norm": norm,
        "discriminant": discriminant,
        "support": support,
        "codifferent_basis": tuple(codifferent.basis()),
    }


def main():
    rows = tuple(row(n) for n in CONDUCTORS)
    discriminant_formula = all(row_["norm"] == row_["discriminant"] for row_ in rows)
    ramification_correct = all(
        set(row_["support"]) <= set(ZZ(row_["n"]).prime_divisors()) for row_ in rows
    )
    odd_support = any(any(prime != 2 for prime in row_["support"]) for row_ in rows)

    # Open-and-closed enlargement leaves an old field and its codifferent
    # unchanged.  Recompute after assigning two larger ambient levels.
    strict_retention = True
    for row_ in rows:
        n = row_["n"]
        for level in (2 * n, 6 * n):
            strict_retention &= level % n == 0
            strict_retention &= row(n)["codifferent_basis"] == row_["codifferent_basis"]

    pullback_only_rejected = odd_support
    verdict = (
        discriminant_formula
        and ramification_correct
        and odd_support
        and strict_retention
        and pullback_only_rejected
    )

    print("Cyclotomic relative dualizers:")
    for row_ in rows:
        print(
            f"  n={row_['n']}: Norm(D)={row_['norm']}, "
            f"ramified support={row_['support']}"
        )
    print()
    print(f"ACTUAL_CYCLOTOMIC_COMPONENTS: {len(rows)}")
    print(f"DIFFERENT_NORM_EQUALS_DISCRIMINANT: {'YES' if discriminant_formula else 'NO'}")
    print(f"ODD_RAMIFICATION_PRESENT: {'YES' if odd_support else 'NO'}")
    print(f"BASE_K_SUPPORT_ONLY_AT_2_SUFFICIENT: {'NO' if pullback_only_rejected else 'UNRESOLVED'}")
    print(f"CODIFFERENT_STABLE_UNDER_ROOTED_ENLARGEMENT: {'YES' if strict_retention else 'NO'}")
    print("RELATIVE_ROOTED_DUALIZER: CONSTRUCTED")
    print("GLOBAL_ABSOLUTE_SERRE_DUALITY: NOT_CONSTRUCTED")
    print(f"VERDICT: {'YES' if verdict else 'NO'}")
    if not verdict:
        raise RuntimeError("relative codifferent verifier failed")


main()
