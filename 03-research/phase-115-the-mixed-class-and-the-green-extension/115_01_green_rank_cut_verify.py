#!/usr/bin/env python3
"""
115.01 - The row-(a) Green term is a rank cut.  Verification of the block identities.

Everything here is finite linear algebra on the ruling model of main.tex
eq:Dpr / eq:Clambda / eq:cotangentRRform, so it is exact up to rounding.

Claims checked
--------------
(1) Both row-(a) forms are purely OFF-DIAGONAL in the two rulings, so each is
    carried by a single (primes x primes) matrix M:

        form(x,y) = x1.M.y2 + x2.M^T.y1      i.e.   [[0, M], [M^T, 0]]

    with     M(C_Lambda) = diag(ell),   M(B_int) = ell ell^T,   ell_p = log p.

(2) Hence  M(G) = ell ell^T - diag(ell).   The Green term of eq:greenline in
    one line: the rank-one global outer product minus the local diagonal.

(3) Inertia of [[0,M],[M^T,0]] is (rank M, rank M, .).  So
        C_Lambda : rank r  ->  (r, r, 0)          one hyperbolic plane per prime
        B_int    : rank 1  ->  (1, 1, 2r-2)       signature (1,1) + radical
    i.e. the Green term CUTS THE RANK FROM r TO 1.  That is exactly
    "a global Green term which couples distinct primes (the outer product)
    while preserving their local contact (the diagonal it subtracts)".

(4) On the radical of B_int (both degrees zero) one has G = -C_Lambda exactly.
    So row (a) achieves  B = 0  identically on its primitive space.

(5) The two contact shapes of row (d) on prime powers:
        SELF  K_S(e_m,e_n) = Lambda(mn)      -> (r, 0, |S|-r)   positive index r
        CROSS [[0,M],[M,0]] , same M         -> (r, r, .)       hyperbolic
    In both cases rank M = r, so a Green term still has to cut r -> 1.
"""

import numpy as np

np.set_printoptions(precision=4, suppress=True, linewidth=140)


def inertia(A, tol=1e-9):
    ev = np.linalg.eigvalsh(0.5 * (A + A.T))
    return int((ev > tol).sum()), int((ev < -tol).sum()), int((abs(ev) <= tol).sum())


def cross(M):
    """[[0, M], [M^T, 0]] -- the block form of an off-diagonal ruling pairing."""
    n = M.shape[0]
    Z = np.zeros((n, n))
    return np.block([[Z, M], [M.T, Z]])


def prime_powers(limit):
    """[(n, p)] for prime powers 2 <= n < limit."""
    out = []
    for n in range(2, limit):
        m, p = n, None
        for q in range(2, n + 1):
            if n % q == 0:
                p = q
                break
        t = n
        while t % p == 0:
            t //= p
        if t == 1:
            out.append((n, p))
    return out


def main():
    primes = [2, 3, 5, 7, 11, 13, 17]
    r = len(primes)
    ell = np.array([np.log(p) for p in primes])
    D, L = np.diag(ell), np.outer(ell, ell)

    B_int, C_lam = cross(L), cross(D)
    G = B_int - C_lam

    print("=" * 74)
    print("(1) the block forms reproduce the paper's formulas")
    print("=" * 74)
    rng = np.random.default_rng(1)
    e1 = e2 = 0.0
    for _ in range(500):
        x, y = rng.normal(size=2 * r), rng.normal(size=2 * r)
        d1x, d2x, d1y, d2y = ell @ x[:r], ell @ x[r:], ell @ y[:r], ell @ y[r:]
        e1 = max(e1, abs((d1x * d2y + d2x * d1y) - x @ B_int @ y))
        c = sum((x[i] * y[r + i] + x[r + i] * y[i]) * ell[i] for i in range(r))
        e2 = max(e2, abs(c - x @ C_lam @ y))
    print(f"  B_int  vs  d1(x)d2(y)+d2(x)d1(y)   max err = {e1:.2e}")
    print(f"  C_lam  vs  sum_p (x_p1 y_p2 + x_p2 y_p1) log p   max err = {e2:.2e}")

    print()
    print("=" * 74)
    print("(2) the Green term, in closed form")
    print("=" * 74)
    print(f"  max | M_G  -  ( ell ell^T - diag(ell) ) | = "
          f"{abs(G[:r, r:] - (L - D)).max():.2e}")

    print()
    print("=" * 74)
    print("(3) the rank cut")
    print("=" * 74)
    print(f"  r = {r}")
    print(f"  rank M(C_Lambda) = {np.linalg.matrix_rank(D)}   "
          f"inertia C_Lambda = {inertia(C_lam)}   expect ({r},{r},0)")
    print(f"  rank M(B_int)    = {np.linalg.matrix_rank(L)}   "
          f"inertia B_int    = {inertia(B_int)}   expect (1,1,{2*r-2})")
    print("  -> the Green term cuts the rank from r to 1.")

    print()
    print("=" * 74)
    print("(4) on the radical of B_int, G = -C_Lambda exactly")
    print("=" * 74)
    Q, _ = np.linalg.qr(ell.reshape(-1, 1))
    P = np.eye(r) - Q @ Q.T
    Z = np.zeros((r, r))
    Pb = np.block([[P, Z], [Z, P]])
    print(f"  ||B_int|| on the radical      = {abs(Pb @ B_int @ Pb).max():.2e}  (=0)")
    print(f"  ||G + C_Lambda|| there        = {abs(Pb @ (G + C_lam) @ Pb).max():.2e}  (=0)")
    print(f"  inertia of C_Lambda there     = {inertia(Pb @ C_lam @ Pb)}"
          f"   expect ({r-1},{r-1},2)")
    print("  -> row (a) achieves B = 0 IDENTICALLY on its primitive space.")

    print()
    print("=" * 74)
    print("(5) the two contact shapes on prime powers")
    print("=" * 74)
    for lim in (30, 60, 120):
        pw = prime_powers(lim)
        S = [n for n, _ in pw]
        pof = dict(pw)
        k, rr = len(S), len(set(pof.values()))
        M = np.zeros((k, k))
        for i, m in enumerate(S):
            for j, n in enumerate(S):
                M[i, j] = np.log(pof[m]) if pof[m] == pof[n] else 0.0
        print(f"  prime powers < {lim:4d}:  |S| = {k:3d}   r = {rr:3d}   "
              f"rank M = {np.linalg.matrix_rank(M):3d}")
        print(f"      SELF   K_S(e_m,e_n)=Lambda(mn)   inertia = {inertia(M)}"
              f"   expect ({rr},0,{k-rr})")
        print(f"      CROSS  [[0,M],[M,0]]             inertia = {inertia(cross(M))}"
              f"   expect ({rr},{rr},{2*k-2*rr})")

    print()
    print("  In both shapes rank M = r, so the Green term must still cut r -> 1.")
    print("  The difference is what the leftover directions are:")
    print("    SELF  leaves them at 0 and puts r POSITIVE directions in the way;")
    print("    CROSS pairs them off, so the leftovers are hyperbolic --")
    print("    which is the situation row (a) demonstrably knows how to cancel.")


if __name__ == "__main__":
    main()
