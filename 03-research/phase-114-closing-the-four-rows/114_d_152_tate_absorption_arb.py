#!/usr/bin/env python3
"""Directed D.152 bound on the truncated two-Tate plane."""

from flint import arb, ctx


ctx.dps = 1000
N = 170
T = arb(5).log() / 2
k = T / 2


def endpoint_derivative(n: int, r: int) -> int:
    import math
    return math.factorial(n + r) // (
        2**r * math.factorial(r) * math.factorial(n-r)
    )


def g_bound(n: int) -> arb:
    double_factorial = arb(1)
    for j in range(n + 1):
        double_factorial *= 2*j + 1
    ib = k**n / double_factorial * (k*k/(2*(2*n+3))).exp()
    return (2*T*(2*n+1)).sqrt() * ib


gb = [g_bound(n) for n in range(N)]
D = []
for r in range(N):
    total = arb(0)
    for n in range(r, N):
        norm = (arb(2*n+1)/(2*T)).sqrt() * T**(-r)
        total += gb[n] * norm * endpoint_derivative(n, r)
    D.append(total)

# Exact integral of [2+2T-(1/2)log(2x)]^2 over (0,2T).
L = 2*T
c = 2+2*T-arb(2).log()/2
logL = L.log()
h1_sq = L*(c*c-c*(logL-1)+(logL*logL-2*logL+2)/4)
h1_norm = h1_sq.sqrt()

boundary = 2*D[0]*h1_norm
interior = arb(0)
root_length = (2*T).sqrt()
quarter = arb(1)/4
for r in range(1, N):
    H0 = arb(r+1).zeta(quarter)/arb(2)**(r+1)
    boundary += 2*root_length*D[r]*H0
    if r >= 2 and r % 2 == 0:
        interior += 2*root_length*D[r]*H0

gamma_bound = boundary+interior
m0 = arb.pi().log()+arb.const_euler()+arb.pi()/2+3*arb(2).log()
weights = arb(2).log()/arb(2).sqrt()+arb(3).log()/arb(3).sqrt()+arb(2).log()/2
unorm = (2*T.sinh()).sqrt()
base_bound = gamma_bound+(m0+2*weights)*unorm

# Tail and coefficient normalization, as in D.151.
gN = g_bound(N)
ratio = k/(2*N+3)*(arb(2*N+3)/(2*N+1)).sqrt()
tail = gN*gN/(1-ratio*ratio)
gq = 2*tail
low_gram = 2*(T.sinh()-T)-gq
C = arb(2).sqrt()*base_bound/low_gram.sqrt()
eta = (gq/low_gram).sqrt()
gap = (arb("0.219")-2*C*eta-arb("8.315")*eta*eta)/(1+eta*eta)

assert C < arb("1e5")
assert eta < arb("1e-424")
assert gap > arb("0.218")

print("D152 directed Tate-defect absorption: PASS")
print("Gamma plane bound =", gamma_bound)
print("C_170 upper =", C)
print("primitive complement gap lower =", gap)

