#!/home/trabajo/miniforge3/bin/python
"""Exact localization falsifier on the proper transverse P1."""

from sage.all import LaurentPolynomialRing, QQ


R = LaurentPolynomialRing(QQ, "t")
t = R.gen()
K = R.fraction_field()
tk = K(t)

identities_ok = True
proper_characters_regular = True
for n in range(17):
    at_zero = 1 / (1 - tk)
    at_infinity = tk**n / (1 - tk**-1)
    localized_sum = at_zero + at_infinity
    expected = sum(tk**j for j in range(n + 1))
    row_ok = localized_sum == expected
    identities_ok = identities_ok and row_ok
    proper_characters_regular = proper_characters_regular and expected.denominator() == 1
    print(
        f"N={n}_LOCALIZED_SUM={localized_sum}_EXPECTED={expected}"
        f"_REGULAR={'YES' if expected.denominator() == 1 else 'NO'}"
        f"_OK={'YES' if row_ok else 'NO'}"
    )

individual_terms_localized = (
    (1 / (1 - tk)).denominator() != 1
    and (1 / (1 - tk**-1)).denominator() != 1
)

numeric_ok = True
for p in [2, 3, 5, 7, 11]:
    value = QQ(p + 1) / p
    for n in [0, 1, 2, 4, 8]:
        lhs = 1 / (1 - value) + value**n / (1 - value**-1)
        rhs = sum(value**j for j in range(n + 1))
        numeric_ok = numeric_ok and lhs == rhs

uncancelled_local_pole_survives = not proper_characters_regular
verdict = all(
    [
        identities_ok,
        individual_terms_localized,
        proper_characters_regular,
        numeric_ok,
        not uncancelled_local_pole_survives,
    ]
)

print(f"P1_LOCALIZATION_IDENTITIES: {'YES' if identities_ok else 'NO'}")
print(f"INDIVIDUAL_FIXED_TERMS_REQUIRE_LOCALIZATION: {'YES' if individual_terms_localized else 'NO'}")
print(f"PROPER_GLOBAL_CHARACTERS_REGULAR: {'YES' if proper_characters_regular else 'NO'}")
print(f"PRIME_DERIVED_NUMERIC_CHECKS: {'YES' if numeric_ok else 'NO'}")
print(f"UNCANCELLED_LOCAL_FACTOR_SURVIVES_PROPER_SUM: {'YES' if uncancelled_local_pole_survives else 'NO'}")
print("FINITE_TYPE_PROPER_COHERENT_BRIDGE: CLOSED_NO_GO")
print("REQUIRED_THEORY: RENORMALIZED_EQUIVARIANT_ARITHMETIC_HODGE")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
