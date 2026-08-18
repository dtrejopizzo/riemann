#!/usr/bin/env python3
"""Finite-lattice audit of D.183 killed-path domination."""

import itertools
import numpy as np

rng = np.random.default_rng(183)
M = 181

# Positive symmetric convolution probability on a large cyclic dilation.
nu = np.zeros(M)
nu[0] = 0.44
for j, mass in [(1, 0.16), (3, 0.10), (8, 0.07), (21, 0.05)]:
    nu[j] += mass
    nu[-j] += mass
nu /= nu.sum()

def conv(v):
    return np.fft.ifft(np.fft.fft(nu) * np.fft.fft(v)).real

# Kill outside an interval; K=P C P is pointwise dominated by C.
mask = np.zeros(M)
mask[25:156] = 1.0

def killed(v):
    return mask * conv(mask * v)

def shift(v, j):
    return np.roll(v, j)

# Additive labels model logarithms; ordered words group by their sum, exactly
# as multiplicative labels group by their product.
labels = [7, 13, 24]
weights = {7: 0.8, 13: 0.51, 24: 0.34}
k = 3
source = np.zeros(M)
source[31] = 1.0

actual = np.zeros(M)
raw = np.zeros(M)
for word in itertools.product(labels, repeat=k):
    coeff = np.prod([weights[j] for j in word])
    v = source.copy()
    for pos, j in enumerate(word):
        v = mask * shift(v, j)
        if pos < k - 1:
            v = killed(v)
    actual += coeff * v
    raw += coeff * shift(source, sum(word))

majorant = conv(conv(raw))
assert np.max(np.abs(actual) - majorant) < 3e-12
assert np.linalg.norm(actual) <= np.linalg.norm(raw) + 3e-12

# Signed input: positivity gives |actual(f)| <= majorant(|f|).
f = np.zeros(M)
f[31:35] = rng.normal(size=4)
actual_f = np.zeros(M)
raw_abs = np.zeros(M)
for word in itertools.product(labels, repeat=k):
    coeff = np.prod([weights[j] for j in word])
    v = f.copy()
    for pos, j in enumerate(word):
        v = mask * shift(v, j)
        if pos < k - 1:
            v = killed(v)
    actual_f += coeff * v
    raw_abs += coeff * shift(np.abs(f), sum(word))
maj_abs = conv(conv(raw_abs))
assert np.max(np.abs(actual_f) - maj_abs) < 4e-12

print("actual/raw norm ratio =", np.linalg.norm(actual), np.linalg.norm(raw))
print("D183 killed paths preserve Witt simplex: PASS")

