#!/home/trabajo/miniforge3/bin/python
"""Falsifier for the proper equivariant pushforward of the Euler numerator."""

from sympy import Matrix, Rational, simplify, symbols


t = symbols("t", nonzero=True)
x, y = symbols("x y")
PRIMES = (2, 3, 5, 7, 11)

euler_zero = 1 - t
euler_infinity = 1 - 1 / t

# Ordered local equations x-y and y-t*x for Delta and Gamma_t.
graph_diagonal_jacobian = Matrix([[1, -1], [-t, 1]])
graph_diagonal_ok = simplify(graph_diagonal_jacobian.det() - (1 - t)) == 0

# The supported class alpha_0=i_*(1-t) restricts by self-intersection.
alpha_at_zero = euler_zero**2
alpha_at_infinity = 0
supported_pushforward = simplify(
    alpha_at_zero / euler_zero + alpha_at_infinity / euler_infinity
)

supported_ok = simplify(supported_pushforward - (1 - t)) == 0

# By contrast, the proper structure sheaf has both fixed-point terms.
structure_pushforward = simplify(1 / euler_zero + 1 / euler_infinity)
structure_cancellation_ok = structure_pushforward == 1
structure_mutation_rejected = simplify(structure_pushforward - supported_pushforward) != 0

prime_evaluations_ok = True
for p in PRIMES:
    for exponent in (1, 2, 3):
        q = Rational(1, p**exponent)
        prime_evaluations_ok &= supported_pushforward.subs(t, q) == 1 - q

augmentation_kills_numerator = supported_pushforward.subs(t, 1) == 0
localized_pole_not_laurent = simplify(1 / (1 - t)).as_numer_denom()[1] != 1

verdict = (
    graph_diagonal_ok
    and supported_ok
    and structure_cancellation_ok
    and structure_mutation_rejected
    and prime_evaluations_ok
    and augmentation_kills_numerator
    and localized_pole_not_laurent
)

print(f"ACTUAL_PRIMES_TESTED: {len(PRIMES)}")
print("GRAPH_DIAGONAL_NORMAL_DETERMINANT: " + ("YES" if graph_diagonal_ok else "NO"))
print("PROPER_SUPPORTED_PUSHFORWARD: " + ("YES" if supported_ok else "NO"))
print("INFINITY_CONTAMINATION: " + ("NO" if supported_ok else "YES"))
print("STRUCTURE_SHEAF_DENOMINATORS_CANCEL: " + ("YES" if structure_cancellation_ok else "NO"))
print("STRUCTURE_SHEAF_MUTATION_REJECTED: " + ("YES" if structure_mutation_rejected else "NO"))
print("ORDINARY_AUGMENTATION_NONZERO: " + ("NO" if augmentation_kills_numerator else "YES"))
print("LOCALIZED_INVERSE_EULER_IS_COHERENT_PUSHFORWARD: NO")
print("PROPER_EQUIVARIANT_EULER_NUMERATOR: CONSTRUCTED")
print("RENORMALIZED_ARITHMETIC_HODGE_PUSHFORWARD: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
