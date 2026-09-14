import numpy as np, math
from math import log, sqrt

# ---------------------------------------------------------------
# This is the rational-prime NORM-PUSHFORWARD Hankel
#     B_p = [ Lambda(p^{i+j}) ]_{i,j>=1}
# For a local factor  prod_r (1 - alpha_r p^{-s})^{-1}  of degree d,
#     Lambda(p^k) = (log p) * sum_r alpha_r^k
# so formally B_p = (log p) * sum_r v_r v_r^T, v_r=(alpha_r^j)_j,
# in the unit-mass case.  For general masses c_r, positivity is equivalent
# to real alpha_r and positive c_r after repeated atoms are collected.
# It is not the invariant place-indexed package. At one geometric place v,
# that package is the all-one block log(Nv), always PSD of rank one.
# ---------------------------------------------------------------
def hankel_block(coeffs, K):
    """coeffs[k] = Lambda(p^k), k>=1; returns [coeffs[i+j]]_{i,j=1..K}"""
    return np.array([[coeffs[i+j] for j in range(1, K+1)] for i in range(1, K+1)])

def inertia(M, tol=1e-10):
    w = np.linalg.eigvalsh(M); sc = max(1.0, abs(w).max())
    return int((w > tol*sc).sum()), int((w < -tol*sc).sum()), w

p, K = 7, 6
LOGP = log(p)
cases = {}

# 1. zeta: single Frobenius eigenvalue alpha = 1
cases["zeta  (deg 1, alpha=1)"] = [0]+[LOGP*1.0 for k in range(1, 2*K+2)]

# 2. Dedekind, p inert of residue degree f: N(P)=p^f, Lambda = f*log p on p^{fk}
for f in (2, 3, 4):
    c = [0.0]*(2*K+2)
    for k in range(1, 2*K+2):
        c[k] = f*LOGP if k % f == 0 else 0.0
    cases[f"Dedekind (p inert, f={f})"] = c

# 3. Dedekind, p split into two deg-1 primes: alpha = 1,1
c = [0]+[2*LOGP for k in range(1, 2*K+2)]
cases["Dedekind (p split, f=1,1)"] = c

# 4. degree-2 Ramanujan-type local factor: alpha = e^{i th}, e^{-i th}
for th in (0.7, 1.3):
    c = [0.0]*(2*K+2)
    for k in range(1, 2*K+2):
        c[k] = LOGP*2*math.cos(k*th)
    cases[f"deg 2, |alpha|=1, th={th}"] = c

print(f"Norm-pushforward Hankel at p={p}, size {K}x{K}   (P2_norm test)")
print("-"*72)
for name, c in cases.items():
    B = hankel_block(c, K)
    pos, neg, w = inertia(B)
    P0 = all(x >= -1e-12 for x in c[1:])      # Lambda >= 0 on prime powers
    print(f"{name:30s} P0(Lam>=0)={str(P0):5s}  (+,-)=({pos},{neg})  lam_min={w[0]:+9.4f}")
