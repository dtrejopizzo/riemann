#!/usr/bin/env python3
"""Rejected monolithic-leaf pilot retained as negative evidence.

The single interval attempted below does *not* certify the claimed range:
its interval variation is too large.  The accepted replacement is
``114_d_66_delta_cover_verify.py``, which uses strict adaptive leaves.
This source is retained to document the failed design and must not be cited
as a certificate.
"""

print("REJECTED_PILOT: monolithic interval variation is too large; "
      "run 114_d_66_delta_cover_verify.py")
raise SystemExit(0)

try:
    from flint import arb, arb_mat, ctx
except ImportError as exc:
    raise SystemExit("Install python-flint or expose it through PYTHONPATH") from exc

ctx.prec = 160
ctx.threads = 4
a = arb(2).log()
T_left = a / 2 + arb("0.0000005")
T_right = arb("0.347")
T_center = (T_left + T_right) / 2
T_radius = (T_right - T_left) / 2
T = arb(T_center.mid(), T_radius.upper() + T_center.rad())
pi = arb.pi()
c = a / arb(2).sqrt()
m0 = pi.log() + arb.const_euler() + pi / 2 + 3 * a
rho = arb(10)
mb, mm = 1, 347

segments = ((-T, T - a, mb), (T - a, a - T, mm), (a - T, T, mb))
left = []
right = []
for lo, hi, count in segments:
    step = (hi - lo) / count
    for k in range(count):
        left.append(lo + k * step)
        right.append(lo + (k + 1) * step)
n = len(left)
assert n == 349
length = [right[i] - left[i] for i in range(n)]
bvals = [arb(2 * j) + arb("0.5") for j in range(20)]
C = sum((2 / b for b in bvals), arb(0)) - m0

# Stable factors for the disjoint-cell integral.
cache = []
for b in bvals:
    cache.append(
        [
            (
                (b * left[i]).exp(),
                (-b * right[i]).exp(),
                (b * length[i]).expm1(),
            )
            for i in range(n)
        ]
    )

mp = []
mmom = []
for i in range(n):
    root = length[i].sqrt()
    mp.append(2 * (left[i] / 2).exp() * (length[i] / 2).expm1() / root)
    mmom.append(2 * (-right[i] / 2).exp() * (length[i] / 2).expm1() / root)


def kernel(i, j):
    if i == j:
        ell = length[i]
        return sum(
            (
                2 * (ell / b + (-b * ell).expm1() / (b * b)) / ell
                for b in bvals
            ),
            arb(0),
        )
    if i > j:
        i, j = j, i
    value = arb(0)
    root = (length[i] * length[j]).sqrt()
    for k, b in enumerate(bvals):
        first = cache[k][i][0] * cache[k][i][2]
        second = cache[k][j][1] * cache[k][j][2]
        value += first * second / (b * b * root)
    return value


def shift(i, j):
    return (i == 0 and j == n - 1) or (j == 0 and i == n - 1)


def entry(i, j):
    value = C if i == j else arb(0)
    if shift(i, j):
        value -= c
    value -= kernel(i, j)
    value += rho * (mp[i] * mp[j] + mmom[i] * mmom[j])
    return value


# Worst analytic residual on the whole leaf.
length_upper = max(x.upper() for x in length)
hmax = arb(length_upper)
Tr = arb(T_right.upper())
I19 = 4 * Tr * sum(
    (
        bi * bj * (1 - (-2 * Tr * (bi + bj)).exp()) / (bi + bj)
        for bi in bvals
        for bj in bvals
    ),
    arb(0),
)
eps_k = 2 * hmax / pi * I19.sqrt()
h_norm_sq = 2 * Tr.sinh()
eps_h = 20 * hmax * h_norm_sq / pi
eps = arb((eps_k + eps_h).upper())


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
for block in (even, odd):
    for i in range(len(block)):
        block[i][i] -= eps


def certify(block, name):
    center = [[x.mid() for x in row] for row in block]
    eig = arb_mat(center).eig(multiple=True)
    midpoint_lower = min(z.real.lower() for z in eig)
    assert all(z.imag.contains(0) for z in eig)
    variation = sum((x.rad() ** 2 for row in block for x in row), arb(0)).sqrt()
    margin = arb(midpoint_lower) - variation
    assert margin > 0, (name, midpoint_lower, variation)
    print(f"PASS {name}: midpoint lower={midpoint_lower}")
    print(f"PASS {name}: Frobenius variation={variation}")
    print(f"PASS {name}: certified margin={margin}")
    return margin


me = certify(even, "even")
mo = certify(odd, "odd")
print(f"PASS residual upper={eps}")
print("PASS first leaf covers [log(2)/2+5e-7, 0.347]")
