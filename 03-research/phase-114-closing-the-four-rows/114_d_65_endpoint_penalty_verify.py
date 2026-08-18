#!/usr/bin/env python3
"""Directed endpoint certificate for the rescaled-boundary bridge.

Requires python-flint.  It proves positivity of q_19 + 10 H on the complete
space at T=log(2)/2, not merely on the primitive subspace.
"""

try:
    from flint import arb, arb_mat, ctx
except ImportError as exc:
    raise SystemExit("Install python-flint or use pip --target and PYTHONPATH") from exc

ctx.prec = 160
ctx.threads = 4
a = arb(2).log()
T = a / 2
pi = arb.pi()
c = a / arb(2).sqrt()
m0 = pi.log() + arb.const_euler() + pi / 2 + 3 * a
n = 347
length = 2 * T / n
left = [-T + k * length for k in range(n)]
right = [x + length for x in left]
bvals = [arb(2 * j) + arb("0.5") for j in range(20)]
C = sum((2 / b for b in bvals), arb(0)) - m0

# Stable cached endpoint factors.
cache = []
for b in bvals:
    cache.append(
        [
            (
                (b * left[i]).exp(),
                (-b * right[i]).exp(),
                (b * length).expm1(),
                (-b * length).expm1(),
            )
            for i in range(n)
        ]
    )

root_length = length.sqrt()
mp = [2 * ((right[i] / 2).exp() - (left[i] / 2).exp()) / root_length for i in range(n)]
mm = [2 * ((-left[i] / 2).exp() - (-right[i] / 2).exp()) / root_length for i in range(n)]


def kernel(i, j):
    if i == j:
        return sum(
            (
                2 * (length / b - (1 - (-b * length).exp()) / (b * b)) / length
                for b in bvals
            ),
            arb(0),
        )
    if i > j:
        i, j = j, i
    value = arb(0)
    for k, b in enumerate(bvals):
        # (e^(bv)-e^(bu))(e^(-br)-e^(-bs)), evaluated with expm1.
        first = cache[k][i][0] * cache[k][i][2]
        second = cache[k][j][1] * cache[k][j][2]
        value += first * second / (b * b * length)
    return value


def entry(i, j):
    value = C if i == j else arb(0)
    value -= kernel(i, j)
    value += 10 * (mp[i] * mp[j] + mm[i] * mm[j])
    return value


half = n // 2
sqrt2 = arb(2).sqrt()
even = [[arb(0) for _ in range(half + 1)] for _ in range(half + 1)]
odd = [[arb(0) for _ in range(half)] for _ in range(half)]
for i in range(half):
    for j in range(half):
        even[i][j] = entry(i, j) + entry(i, n - 1 - j)
        odd[i][j] = entry(i, j) - entry(i, n - 1 - j)
    even[i][half] = sqrt2 * entry(i, half)
    even[half][i] = even[i][half]
even[half][half] = entry(half, half)

threshold = arb("0.1714")
for block, name in ((even, "even"), (odd, "odd")):
    for i in range(len(block)):
        block[i][i] -= threshold
    eig = arb_mat(block).eig(multiple=True)
    least = min(z.real.lower() for z in eig)
    assert arb(least) > 0
    assert all(z.imag.contains(0) for z in eig)
    print(f"PASS endpoint {name}: lambda_min(R)>0.1714; shifted lower={least}")

# Analytic projection residuals, enclosed by the same formulas as D.63.
I19 = 4 * T * sum(
    (
        bi * bj * (1 - (-2 * T * (bi + bj)).exp()) / (bi + bj)
        for bi in bvals
        for bj in bvals
    ),
    arb(0),
)
eps_k = 2 * length / pi * I19.sqrt()
h_norm_sq = 2 * T.sinh()
eps_h = 20 * length * h_norm_sq / pi
eps_total = eps_k + eps_h
assert eps_total < arb("0.0931")
print(f"PASS endpoint residual={eps_total}")
print("PASS q_19 + 10 H > 0.0783 I at T=log(2)/2")

