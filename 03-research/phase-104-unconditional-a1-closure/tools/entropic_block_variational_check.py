#!/usr/bin/env python3
"""Finite checks for 104_71 (stdlib only; no RH claim)."""

from fractions import Fraction
from itertools import product
from math import exp, isclose, log, log1p


def block(length: int) -> list[int]:
    return list(range(length * length, length * length + length))


def frac_product(values) -> Fraction:
    out = Fraction(1)
    for value in values:
        out *= value
    return out


def binary_kl(q: float, p: float) -> float:
    out = 0.0
    if q > 0.0:
        out += q * log(q / p)
    if q < 1.0:
        out += (1.0 - q) * log((1.0 - q) / (1.0 - p))
    return out


def laguerre_one(degree: int, x: float) -> float:
    """L_degree^(1)(x), via the three-term recurrence."""
    if degree == 0:
        return 1.0
    previous = 1.0
    current = 2.0 - x
    if degree == 1:
        return current
    for k in range(1, degree):
        following = ((2.0 * k + 2.0 - x) * current - (k + 1.0) * previous) / (
            k + 1.0
        )
        previous, current = current, following
    return current


def quartet(n: int) -> Fraction:
    if n % 2:
        return Fraction(4)
    magnitude = Fraction(2**n) + Fraction(1, 2**n)
    if n % 4 == 0:
        return Fraction(4) - 2 * magnitude
    return Fraction(4) + 2 * magnitude


def exact_bernoulli_and_telescoping() -> None:
    # Work with r_n=e^{-lambda_n} as arbitrary positive rationals.
    length = 4
    indices = block(length)
    activities = [
        Fraction(2, 3),
        Fraction(5, 7),
        Fraction(11, 5),
        Fraction(13, 17),
    ]
    probabilities = [Fraction(1, n + 2) for n in indices]

    telescoping = frac_product(
        Fraction(n + 1, n + 2) for n in indices
    )
    expected_telescoping = Fraction(length * length + 1, length * length + length + 1)
    constant = Fraction(length * length + length + 1, length * length + 1)
    assert telescoping == expected_telescoping
    assert constant * telescoping == 1

    partition_inverse = frac_product(
        1 + activity / (n + 1)
        for n, activity in zip(indices, activities)
    )
    expectation_product = frac_product(
        (1 - probability) + probability * activity
        for probability, activity in zip(probabilities, activities)
    )
    assert partition_inverse == constant * expectation_product

    # Direct enumeration of all Bernoulli configurations, still exact.
    expectation_enumerated = Fraction(0)
    for bits in product((0, 1), repeat=length):
        probability = Fraction(1)
        observable = Fraction(1)
        for bit, bernoulli_p, activity in zip(bits, probabilities, activities):
            probability *= bernoulli_p if bit else 1 - bernoulli_p
            if bit:
                observable *= activity
        expectation_enumerated += probability * observable
    assert expectation_enumerated == expectation_product


def numerical_gibbs_duality() -> None:
    indices = [4, 5, 6]
    lambdas = [-1.7, 0.35, 2.1]
    probabilities = [1.0 / (n + 2.0) for n in indices]

    factors = [
        1.0 - p + p * exp(-value)
        for p, value in zip(probabilities, lambdas)
    ]
    log_partition = sum(log(value) for value in factors)
    q_star = [
        p * exp(-value) / factor
        for p, value, factor in zip(probabilities, lambdas, factors)
    ]
    product_objective = -sum(q * value for q, value in zip(q_star, lambdas)) - sum(
        binary_kl(q, p) for q, p in zip(q_star, probabilities)
    )
    assert isclose(product_objective, log_partition, rel_tol=2e-13, abs_tol=2e-13)

    configurations = list(product((0, 1), repeat=len(indices)))
    nu = []
    energies = []
    tilted_weights = []
    for bits in configurations:
        probability = 1.0
        energy = 0.0
        for bit, p, value in zip(bits, probabilities, lambdas):
            probability *= p if bit else 1.0 - p
            energy += bit * value
        nu.append(probability)
        energies.append(energy)
        tilted_weights.append(probability * exp(-energy))
    partition = sum(tilted_weights)
    assert isclose(log(partition), log_partition, rel_tol=2e-13, abs_tol=2e-13)
    mu_star = [weight / partition for weight in tilted_weights]
    full_objective = -sum(
        probability * energy for probability, energy in zip(mu_star, energies)
    ) - sum(
        probability * log(probability / reference)
        for probability, reference in zip(mu_star, nu)
    )
    assert isclose(full_objective, log_partition, rel_tol=2e-13, abs_tol=2e-13)

    # Entropy chain rule for a deliberately correlated full-support law.
    raw_mu = [1.0 + ((7 * j + 3) % 11) for j in range(len(configurations))]
    normalizer = sum(raw_mu)
    mu = [value / normalizer for value in raw_mu]
    marginals = [
        sum(probability * bits[j] for probability, bits in zip(mu, configurations))
        for j in range(len(indices))
    ]
    product_marginal = []
    for bits in configurations:
        probability = 1.0
        for bit, q in zip(bits, marginals):
            probability *= q if bit else 1.0 - q
        product_marginal.append(probability)
    d_mu_nu = sum(
        probability * log(probability / reference)
        for probability, reference in zip(mu, nu)
    )
    mutual_information = sum(
        probability * log(probability / reference)
        for probability, reference in zip(mu, product_marginal)
    )
    marginal_entropy = sum(
        binary_kl(q, p) for q, p in zip(marginals, probabilities)
    )
    assert isclose(
        d_mu_nu,
        mutual_information + marginal_entropy,
        rel_tol=2e-13,
        abs_tol=2e-13,
    )

    # A coarse grid cannot beat the analytic product optimizer.
    for q_vector in product((0.0, 0.2, 0.5, 0.8, 1.0), repeat=len(indices)):
        objective = -sum(q * value for q, value in zip(q_vector, lambdas)) - sum(
            binary_kl(q, p) for q, p in zip(q_vector, probabilities)
        )
        assert objective <= log_partition + 1e-12


def combined_laguerre_identity() -> None:
    indices = [3, 4, 5]
    q = [0.15, 0.6, 0.35]
    probabilities = [1.0 / (n + 2.0) for n in indices]
    archimedean = [0.7, 1.2, 1.8]
    polar = [-0.1, 0.25, 0.05]

    # Mock finite Euler measure: (log m, Lambda(m)m^{-1-epsilon}).
    euler_atoms = [(0.7, 0.31), (1.1, 0.17), (1.8, 0.09)]
    q_terms = []
    for n in indices:
        q_terms.append(
            sum(weight * laguerre_one(n - 1, x) for x, weight in euler_atoms)
        )
    regulated_lambdas = [
        a + pole - q_term
        for a, pole, q_term in zip(archimedean, polar, q_terms)
    ]
    entropy = sum(binary_kl(value, p) for value, p in zip(q, probabilities))
    site_form = -sum(
        value * coefficient for value, coefficient in zip(q, regulated_lambdas)
    ) - entropy

    combined_euler = 0.0
    for x, weight in euler_atoms:
        g_lq = sum(
            value * laguerre_one(n - 1, x)
            for n, value in zip(indices, q)
        )
        combined_euler += weight * g_lq
    combined_form = combined_euler - sum(
        value * (a + pole)
        for value, a, pole in zip(q, archimedean, polar)
    ) - entropy
    assert isclose(site_form, combined_form, rel_tol=2e-12, abs_tol=2e-12)


def diagonal_and_offline_checks() -> None:
    eta = 0.01 - log(200.0 / 199.0)
    assert eta > 0.0
    envelopes = []
    for length in (20, 50, 100):
        n_max = length * length + length - 1
        # The omitted fixed constant 2M does not affect convergence.
        envelopes.append(length * n_max * exp(-eta * n_max))
    assert envelopes[-1] < 1e-10
    assert envelopes[-1] < envelopes[-2]

    witness_values = []
    for length in (4, 8, 12, 20):
        indices = block(length)
        d = next(n for n in indices if n % 4 == 0)
        q_value = quartet(d)
        assert -q_value >= 2**d
        constant = (length * length + length + 1.0) / (length * length + 1.0)
        witness = -float(q_value) - log(d + 1.0) - log(constant)
        lower_bound = float(2**d) - log(d + 1.0) - log(constant)
        assert witness >= lower_bound
        # Direct log of the Bernoulli product, evaluated by log-sum-exp.
        log_partition = 0.0
        for n in indices:
            p = 1.0 / (n + 2.0)
            first = log(1.0 - p)
            second = log(p) - float(quartet(n))
            maximum = max(first, second)
            log_partition += maximum + log1p(exp(min(first, second) - maximum))
        assert log_partition + 1e-9 * max(1.0, abs(witness)) >= witness
        # B_L=e^L is already an exp(o(L^2)) slack and is defeated here.
        assert witness > exp(length)
        witness_values.append((length, d, witness))
    assert all(
        current[2] > previous[2]
        for previous, current in zip(witness_values, witness_values[1:])
    )
    for length, d, witness in witness_values:
        print(f"L={length:2d} offline_site={d:4d} variational_witness={witness:.6e}")


def main() -> None:
    exact_bernoulli_and_telescoping()
    numerical_gibbs_duality()
    combined_laguerre_identity()
    diagonal_and_offline_checks()
    print("entropic_block_variational_check: PASS")


if __name__ == "__main__":
    main()
