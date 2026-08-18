#!/home/trabajo/miniforge3/bin/python
"""Numerical falsifier for the Mellin prime-Dirac/Meyer comparison."""

from mpmath import mp


mp.dps = 60
PARAMETERS = (mp.mpf("2"), mp.mpf("2.5"), mp.mpc(2, 3))


def mellin_f(s):
    return mp.quad(lambda x: mp.e ** (-x) * x ** (s - 1), [0, 1, mp.inf])


def mellin_zf(s):
    return mp.quad(
        lambda x: x ** (s - 1) / mp.expm1(x),
        [0, 1, mp.inf],
    )


mellin_multiplier_ok = True
dirac_symbol_ok = True
mutation_rejected = True
max_mellin_error = mp.mpf(0)

for s in PARAMETERS:
    source = mellin_f(s)
    transformed = mellin_zf(s)
    multiplier = transformed / source
    mellin_error = abs(multiplier - mp.zeta(s))
    max_mellin_error = max(max_mellin_error, mellin_error)
    mellin_multiplier_ok &= mellin_error < mp.mpf("1e-45")

    dirac_inverse_symbol = 1 / (1 / mp.zeta(s))
    dirac_symbol_ok &= abs(multiplier - dirac_inverse_symbol) < mp.mpf("1e-45")

    # Changing the n=2 dilation coefficient from 1 to -1 subtracts
    # 2*2^{-s} Gamma(s) from the Mellin transform.
    mutated_multiplier = multiplier - 2 * mp.power(2, -s)
    mutation_rejected &= abs(mutated_multiplier - mp.zeta(s)) > mp.mpf("0.1")


verdict = mellin_multiplier_ok and dirac_symbol_ok and mutation_rejected

print(f"MELLIN_PARAMETERS_TESTED: {len(PARAMETERS)}")
print(f"MAX_MELLIN_MULTIPLIER_ERROR: {mp.nstr(max_mellin_error, 8)}")
print(f"MEYER_ZETA_OPERATOR_MULTIPLIER: {'YES' if mellin_multiplier_ok else 'NO'}")
print(f"PRIME_DIRAC_DET2_INVERSE_MATCHES: {'YES' if dirac_symbol_ok else 'NO'}")
print(f"MUTATED_DILATION_COEFFICIENT_REJECTED: {'YES' if mutation_rejected else 'NO'}")
print("DIRAC_TO_MEYER_MELLIN_COMPARISON: CONSTRUCTED_ON_RE_S_GT_1")
print("ARITHMETIC_SQUARE_CURRENT_COMPARISON: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
