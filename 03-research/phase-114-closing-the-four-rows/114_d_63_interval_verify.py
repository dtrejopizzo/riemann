#!/usr/bin/env python3
"""Directed ball certificate for D.63.

Dependency: python-flint >= 0.8.0.  Every transcendental and every matrix
entry is evaluated as an Arb ball.  The input T itself is the full interval
0.4 +/- 1e-12, so the final eigenvalue balls certify that whole interval,
not merely its midpoint.
"""
try:
    from flint import arb, arb_mat, ctx
except ImportError as exc:
    raise SystemExit("Install the reproducible backend with: pip install python-flint") from exc

ctx.prec = 128
ctx.threads = 4

T = arb("0.4 +/- 1e-12")
a = arb(2).log()
pi = arb.pi()
c = a / arb(2).sqrt()
m0 = pi.log() + arb.const_euler() + pi/2 + 3*a
mb, mm = 36, 196

# Interval endpoints.  The left and right boundary cells are exact
# translates by a for every T in the input ball.
segments = ((-T, T-a, mb), (T-a, a-T, mm), (a-T, T, mb))
left = []
right = []
for lo, hi, count in segments:
    step = (hi-lo)/count
    for k in range(count):
        left.append(lo+k*step)
        right.append(lo+(k+1)*step)

n = len(left)
assert n == 268
length = [right[i]-left[i] for i in range(n)]
bvals = [arb(2*j)+arb("0.5") for j in range(20)]
C = sum((2/b for b in bvals), arb(0))-m0

# Build the upper triangle from closed integrals, then symmetrize.
R = [[arb(0) for _ in range(n)] for _ in range(n)]
for i in range(n):
    R[i][i] = C
for i in range(mb):
    R[i][n-mb+i] -= c
    R[n-mb+i][i] -= c

for b in bvals:
    b2 = b*b
    for i in range(n):
        ell = length[i]
        diag = 2*(ell/b-(1-(-b*ell).exp())/b2)/ell
        R[i][i] -= diag
        for j in range(i+1, n):
            # Cells are ordered and disjoint: right[i] <= left[j].
            value = (
                (-b*(left[j]-right[i])).exp()
                - (-b*(right[j]-right[i])).exp()
                - (-b*(left[j]-left[i])).exp()
                + (-b*(right[j]-left[i])).exp()
            )/(b2*(length[i]*length[j]).sqrt())
            R[i][j] -= value
            R[j][i] -= value

# Exact rank-two penalty rho H, rho=10.
mp = []
mmom = []
for i in range(n):
    rootlen = length[i].sqrt()
    mp.append(2*((right[i]/2).exp()-(left[i]/2).exp())/rootlen)
    mmom.append(2*((-left[i]/2).exp()-(-right[i]/2).exp())/rootlen)
for i in range(n):
    for j in range(i, n):
        value = 10*(mp[i]*mp[j]+mmom[i]*mmom[j])
        R[i][j] += value
        if i != j:
            R[j][i] += value

# Reflection sends index i to n-1-i.  In normalized even/odd coordinates,
# block entries are R_ij +/- R_i,rev(j).
half = n//2
even = [[R[i][j]+R[i][n-1-j] for j in range(half)] for i in range(half)]
odd = [[R[i][j]-R[i][n-1-j] for j in range(half)] for i in range(half)]

threshold = arb("0.15530")
for block in (even, odd):
    for i in range(half):
        block[i][i] -= threshold


def certify_shifted_positive(entries, name):
    """Midpoint eigenballs plus a rigorous Frobenius variation bound."""
    center = [[x.mid() for x in row] for row in entries]
    eig = arb_mat(center).eig(multiple=True)
    # The interval dependency in T makes direct interval eigensolving much
    # wider than necessary.  Weyl's inequality instead bounds the family by
    # the midpoint plus the Frobenius norm of all entry radii.
    variation_sq = arb(0)
    for row in entries:
        for x in row:
            variation_sq += x.rad()**2
    variation = variation_sq.sqrt()
    lows = []
    for z in eig:
        if not (z.real > 0):
            raise AssertionError(f"{name}: midpoint shifted eigenball not positive {z}")
        if not z.imag.contains(0):
            raise AssertionError(f"{name}: imaginary enclosure misses zero {z}")
        lows.append(z.real.lower())
    least = min(lows)
    if not (arb(least)-variation > 0):
        raise AssertionError(f"{name}: variation {variation} reaches midpoint gap {least}")
    print(f"PASS {name}: dim={len(entries)}, R-0.15530 I uniformly positive")
    print(f"  midpoint shifted lower endpoint: {least}")
    print(f"  certified Frobenius variation: {variation}")


certify_shifted_positive(even, "even")
certify_shifted_positive(odd, "odd")
print("PASS uniform directed certificate for |T-2/5| <= 1e-12")
