#!/usr/bin/env python3
"""Nonlocal divisor storage: floating matrix checks, not a RH certificate."""

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh, solve

from verify_coherent_paths import build, inverse_sqrt
from verify_contact_response import mobius


def check(T, dimension, artificial=False):
    weights = [(2, 2, 100.0)] if artificial else None
    model = build(T, dimension, replace_weights=weights)
    B, E, C, J = (model[name] for name in ('B', 'E', 'C', 'J'))
    Bh = inverse_sqrt(B)
    cv, cu = eigh(C)
    Ch = (cu * np.sqrt(cv)) @ cu.T
    R, Y = Bh @ J @ Bh, Bh @ Ch
    rv, ru = eigh(R)
    assert max(abs(rv)) < 1
    G = (ru * (1 / (1 - rv))) @ ru.T
    K = Ch @ solve(E, Ch, assume_a='pos')
    assert np.linalg.norm(K - Y.T @ G @ Y, 2) < 1e-10
    h = 2 * T / dimension
    distances = (np.arange(dimension)[:, None] - np.arange(dimension)[None, :]) * h
    N = math.ceil(math.exp(2 * T)) - 1
    responses = []
    for d in (2, 3):
        M = np.zeros_like(R)
        for k in range(1, N // d + 1):
            n = d * k
            shift = np.maximum(0, 1 - abs(distances - math.log(n)) / h)
            M += mobius(k) / math.sqrt(n) * (shift + shift.T)
        responses.append(Bh @ M @ Bh)
    D = responses[0] @ responses[1] - responses[1] @ responses[0]
    raw_S = D.T @ D
    raw_norm = float(np.linalg.norm(raw_S, 2))
    assert raw_norm > 1e-16
    S = raw_S / raw_norm
    source = ru.T @ S @ ru
    cost = ru @ (source / (1 - rv[:, None] * rv[None, :])) @ ru.T
    cost = (cost + cost.T) / 2
    stein_error = float(np.linalg.norm(cost - R @ cost @ R - S, 2))
    assert stein_error < 1e-10
    assert eigh(cost, eigvals_only=True)[0] > -1e-10
    output_cost = Y.T @ cost @ Y
    output_cost = (output_cost + output_cost.T) / 2
    gain = float(eigh(K, eigvals_only=True)[-1])
    cost_norm = float(np.linalg.norm(output_cost, 2))
    margin = 1 - gain
    # This finite-model choice deliberately uses the measured margin.
    # It does NOT derive that margin from the divisor identities.
    eta = margin / (2 * cost_norm) if margin > 0 else 0.1
    Z = G + eta * cost
    identity_error = float(np.linalg.norm(Z - R @ Z @ R - np.eye(dimension) - R - eta * S, 2))
    assert identity_error < 1e-10
    assembled = Y.T @ Z @ Y
    assert np.linalg.norm(assembled - K - eta * output_cost, 2) < 1e-10
    new_gain = float(eigh(assembled, eigvals_only=True)[-1])
    assert new_gain >= gain - 1e-10
    if artificial:
        assert gain > 1 and new_gain > 1
    else:
        assert margin > 0
        assert new_gain <= 1 - margin / 2 + 1e-10
    return dict(T=T, dimension=dimension, artificial_weights=artificial,
                gain=gain, observed_margin=margin, eta_chosen_from_margin=eta,
                new_gain=new_gain, divisor_commutator_square_norm=raw_norm,
                normalized_output_cost_norm=cost_norm,
                stein_residual=stein_error, storage_identity_residual=identity_error,
                smallest_cost_eigenvalue=float(eigh(cost, eigvals_only=True)[0]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    cases = [check(T, n) for T in (1.0, 1.5) for n in (24, 48)]
    result = dict(status='PASS: nonlocal matrix construction; no global sign theorem',
                  cases=cases, falsifier=check(1.0, 48, artificial=True),
                  limitations=[
                      'eta uses the observed finite-dimensional margin.',
                      'No certified Galerkin remainder or interval arithmetic.',
                      'Observability of all continuum contact vectors is unproved.',
                  ])
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + '\n')
    for case in cases:
        print(f"T={case['T']} N={case['dimension']}: "
              f"gain={case['gain']:.9f}, "
              f"eta={case['eta_chosen_from_margin']:.6g}, "
              f"new gain={case['new_gain']:.9f}")
    print('Falsifier gains:', result['falsifier']['gain'], '->', result['falsifier']['new_gain'])
    print(result['status'])


if __name__ == '__main__':
    main()
