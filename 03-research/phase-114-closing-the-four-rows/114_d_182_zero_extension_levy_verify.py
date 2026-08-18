#!/usr/bin/env python3
"""Finite-cell certificates for D.182 zero-extension Lévy dilation."""

import numpy as np

rng = np.random.default_rng(182)

# 1. Regional versus zero-extension balanced channels.
n = 83
f = rng.normal(size=n)
for jump in (1, 7, 19, 41):
    reg_plus = (f[jump:] + f[:-jump]) / np.sqrt(2.0)
    reg_minus = (f[jump:] - f[:-jump]) / np.sqrt(2.0)
    z = np.pad(f, (jump, jump))
    # t ranges over the padded lattice; the two translates have equal size.
    full_plus = (z[jump:] + z[:-jump]) / np.sqrt(2.0)
    full_minus = (z[jump:] - z[:-jump]) / np.sqrt(2.0)
    regional_diff = np.dot(reg_plus, reg_plus) - np.dot(reg_minus, reg_minus)
    full_diff = np.dot(full_plus, full_plus) - np.dot(full_minus, full_minus)
    boundary = 0.5 * (np.dot(f[:jump], f[:jump]) + np.dot(f[-jump:], f[-jump:]))
    assert abs(full_diff - regional_diff) < 2e-11
    assert abs(np.dot(full_plus, full_plus) - np.dot(reg_plus, reg_plus) - boundary) < 2e-11
    assert abs(np.dot(full_minus, full_minus) - np.dot(reg_minus, reg_minus) - boundary) < 2e-11

# 2. A periodic compound-Poisson/Gamma surrogate.  The Fourier exponential
# has a nonnegative probability convolution kernel, and its massive
# resolvent has total mass 1/lambda independently of all jump weights.
N = 257
freq = 2.0 * np.pi * np.arange(N) / N
symbol = 0.43 * (1.0 - np.cos(freq))
for jump, weight in [(2, 0.9), (5, 1.7), (13, 0.4), (37, 2.3)]:
    symbol += weight * (1.0 - np.cos(jump * freq))
lam = 0.61
times = (0.03, 0.2, 0.9)
for t in times:
    kernel = np.fft.ifft(np.exp(-t * symbol)).real
    assert kernel.min() > -2e-12
    assert abs(kernel.sum() - 1.0) < 2e-12
res_kernel = np.fft.ifft(1.0 / (lam + symbol)).real
assert res_kernel.min() > -2e-12
assert abs(res_kernel.sum() - 1.0 / lam) < 3e-12

# 3. Killed restriction of a symmetric Markov generator is dominated by
# the full periodic semigroup on nonnegative data.
weights = [(1, 0.43), (2, 0.9), (5, 1.7), (13, 0.4), (37, 2.3)]
Lfull = np.zeros((N, N))
for jump, weight in weights:
    for i in range(N):
        for j in ((i + jump) % N, (i - jump) % N):
            Lfull[i, i] += weight / 2.0
            Lfull[i, j] -= weight / 2.0
keep = np.arange(70, 187)
Lpart = Lfull[np.ix_(keep, keep)]
ef, Uf = np.linalg.eigh(Lfull)
ep, Up = np.linalg.eigh(Lpart)
g = rng.random(keep.size)
gfull = np.zeros(N)
gfull[keep] = g
for t in times:
    full = (Uf * np.exp(-t * ef)) @ (Uf.T @ gfull)
    part = (Up * np.exp(-t * ep)) @ (Up.T @ g)
    assert part.min() > -3e-12
    assert np.max(part - full[keep]) < 4e-11

print("massive convolution mass =", res_kernel.sum(), 1.0 / lam)
print("zero-extension channels and killed domination: PASS")
print("D182 zero-extension Levy dilation: PASS")

