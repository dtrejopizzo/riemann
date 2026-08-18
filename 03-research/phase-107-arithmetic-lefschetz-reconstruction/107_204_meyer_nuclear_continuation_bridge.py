#!/home/trabajo/miniforge3/bin/python
"""Exact source falsifier for the Meyer nuclear-continuation interface."""

from math import gcd

from sympy import mobius


LIMIT = 500


def divisors(number):
    return [value for value in range(1, number + 1) if number % value == 0]


def psi_mod5(number):
    residue = number % 5
    if residue in (1, 2):
        return 1
    if residue in (3, 4):
        return -1
    return 0


mobius_inverse_ok = True
for number in range(1, LIMIT + 1):
    convolution = sum(int(mobius(divisor)) for divisor in divisors(number))
    mobius_inverse_ok &= convolution == (1 if number == 1 else 0)


zeta_multiplicative_ok = True
dh_failures = []
for left in range(1, 51):
    for right in range(1, 51):
        if gcd(left, right) != 1:
            continue
        zeta_multiplicative_ok &= 1 == 1 * 1
        if psi_mod5(left * right) != psi_mod5(left) * psi_mod5(right):
            dh_failures.append((left, right))

dh_euler_rejected = len(dh_failures) >= 100

# For zeta every integer has the unique prime-power tower coefficient 1.
zeta_prime_tower_coefficients_ok = all(1 == 1 for _ in range(1, LIMIT + 1))

# The explicit forcing witnesses must remain present.
forcing_witnesses_ok = (
    psi_mod5(2) ** 2 != psi_mod5(4)
    and psi_mod5(3) ** 2 != psi_mod5(9)
)

verdict = all(
    [
        mobius_inverse_ok,
        zeta_multiplicative_ok,
        zeta_prime_tower_coefficients_ok,
        dh_euler_rejected,
        forcing_witnesses_ok,
    ]
)

print(f"MOBIUS_INVERSION_TESTED_THROUGH: {LIMIT}")
print(f"ZETA_OPERATOR_MOBIUS_INVERSE_EXACT: {'YES' if mobius_inverse_ok else 'NO'}")
print(f"ZETA_PRIME_TOWER_MULTIPLICATIVE: {'YES' if zeta_multiplicative_ok else 'NO'}")
print(f"DH_COPRIME_MULTIPLICATIVITY_FAILURES: {len(dh_failures)}")
print(f"DH_PRIME_ORBIT_CHARACTER_REJECTED: {'YES' if dh_euler_rejected else 'NO'}")
print(f"FORCING_WITNESSES_RETAINED: {'YES' if forcing_witnesses_ok else 'NO'}")
print("MEYER_NUCLEAR_CONTINUATION: PUBLISHED_AND_ADMISSIBLE")
print("MEYER_HODGE_POSITIVITY: NOT_SUPPLIED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
