#!/usr/bin/env python3
"""E.01 verifier — balanced channel factorization and single-step contract.

Verifies the numerical claims of 114_e_01_BALANCED_CHANNEL_FACTORIZATION.md:

  1. Lemma 2.2   Jhat_{a,pm}^* Jhat_{a,pm} = I +- Re S_a   (codomain L^2(R))
                and hence  S_a + S_{-a} = J+*J+ - J-*J-
  2. Obs 2.3    the truncated reading gives 1-cos(pi/(2m+1)), not 1-cos(pi/(m+1))
  3. Section 1   g_Gamma >= 0  and  m_0 = log(pi)+gamma+pi/2+3log2
  4. Prop 4.1   sigma_N ~ 2 sqrt(N), alpha_N ~ sqrt(N), ratio -> 1/4
  5. Thm 5.1    D1 in regularized form, on random matrices

Requires only numpy, mpmath and sympy.  Does not use flint: it certifies nothing, it verifies.
"""
import numpy as np
import mpmath as mp
from sympy import factorint

CHECKS = 0

def check(cond, label):
    global CHECKS
    assert cond, f"FAILURE: {label}"
    CHECKS += 1
    print(f"  ok  {label}")


# ---------------------------------------------------------------- 1 and 2
def channels(T2, a, n=500):
    """Returns (I, Re S_a, J-*J-, J+*J+, truncated J-*J-) on the n-cell mesh."""
    h = T2 / n
    k = a / h
    k0, frac = int(np.floor(k)), k - int(np.floor(k))

    pad = k0 + 2                       # cells to the left of t=0
    N = pad + n + k0 + 2
    P = np.zeros((N, n)); P[pad:pad + n, :] = np.eye(n)
    Sh = np.zeros((N, N))
    for i in range(N):
        for (kk, w) in ((k0, 1 - frac), (k0 + 1, frac)):
            if 0 <= i + kk < N:
                Sh[i, i + kk] += w
    E = Sh @ P
    Jm, Jp = (E - P) / np.sqrt(2.0), (E + P) / np.sqrt(2.0)

    S = np.zeros((n, n))
    for i in range(n):
        for (kk, w) in ((k0, 1 - frac), (k0 + 1, frac)):
            if 0 <= i + kk < n:
                S[i, i + kk] += w
    ReS = 0.5 * (S + S.T)

    Jm_tr = Jm[pad:pad + n, :]         # output truncated to the window (erroneous reading)
    return np.eye(n), ReS, Jm.T @ Jm, Jp.T @ Jp, Jm_tr.T @ Jm_tr


print("1. Lemma 2.2 / Theorem 3.1  —  channel identity")
worst = 0.0
for (T2, a) in [(1.0, 0.6), (1.0, 0.4), (1.0, 0.26), (1.0, 0.9), (1.0, 0.21), (2.0, 0.7)]:
    I, ReS, JmJm, JpJp, _ = channels(T2, a)
    worst = max(worst,
                np.abs(JmJm - (I - ReS)).max(),
                np.abs(JpJp - (I + ReS)).max(),
                np.abs((JpJp - JmJm) - 2 * ReS).max())
check(worst < 1e-12, f"J(pm)*J(pm) = I +- Re S_a  and  S_a+S_-a = J+*J+ - J-*J-  (err {worst:.2e})")

print("2. Observation 2.3  —  the codomain decides the spectral constant")
for (T2, a) in [(1.0, 0.6), (1.0, 0.4), (1.0, 0.26)]:
    m = int(np.ceil(T2 / a))
    I, ReS, JmJm, _, Jtr = channels(T2, a)
    lo_full = np.linalg.eigvalsh(JmJm)[0]
    lo_trunc = np.linalg.eigvalsh(Jtr)[0]
    check(abs(lo_full - (1 - np.cos(np.pi / (m + 1)))) < 1e-9,
          f"m={m}: codomain L2(R) gives 1-cos(pi/(m+1)) = {lo_full:.9f}")
    check(abs(lo_trunc - (1 - np.cos(np.pi / (2 * m + 1)))) < 1e-9,
          f"m={m}: truncated reading gives 1-cos(pi/(2m+1)) = {lo_trunc:.9f}")

# ---------------------------------------------------------------- 3
print("3. Section 1  —  the Gamma channel is positive, and the value of m_0")
mp.mp.dps = 40
g = lambda tau: mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * tau / 2)) - mp.digamma(mp.mpf(1) / 4)
vals = [g(mp.mpf(t)) for t in [0, 0.5, 1, 2, 5, 20, 100, 1000]]
check(abs(vals[0]) < mp.mpf('1e-30'), "g_Gamma(0) = 0")
check(all(vals[i] < vals[i + 1] for i in range(len(vals) - 1)),
      "g_Gamma increasing in |tau| (=> g_Gamma >= 0)")
m0 = mp.log(mp.pi) + mp.euler + mp.pi / 2 + 3 * mp.log(2)
check(abs(m0 - mp.mpf('5.3721834192256662')) < mp.mpf('1e-15'),
      f"m_0 = {mp.nstr(m0, 17)}")

# ---------------------------------------------------------------- 4
print("4. Proposition 4.1  —  the scalar deficit tends to 1/4")

def mangoldt_table(maxN):
    lam = np.zeros(maxN + 1)
    for n in range(2, maxN + 1):
        f = factorint(n)
        if len(f) == 1:
            lam[n] = float(np.log(next(iter(f))))
    return lam

MAXN = 100000
lam = mangoldt_table(MAXN)
m0f = float(m0)
rows = []
for N in [5, 10, 50, 200, 1000, 5000, 20000, 100000]:
    T2 = np.log(N)
    idx = np.nonzero(lam[2:N])[0] + 2
    w = lam[idx] / np.sqrt(idx)
    sigma = w.sum()
    mvec = np.ceil(T2 / np.log(idx))
    alpha = (w * (1 - np.cos(np.pi / (mvec + 1)))).sum()
    rows.append((N, sigma, alpha, m0f + 2 * sigma, alpha / (m0f + 2 * sigma),
                 sigma / np.sqrt(N), alpha / np.sqrt(N)))

print(f"    {'N':>7} {'sigma_N':>10} {'alpha_N':>10} {'m0+2sig':>11}"
      f" {'ratio':>10} {'sig/sqrtN':>10} {'alp/sqrtN':>10}")
for r in rows:
    print(f"    {r[0]:>7} {r[1]:>10.4f} {r[2]:>10.4f} {r[3]:>11.4f}"
          f" {r[4]:>10.5f} {r[5]:>10.5f} {r[6]:>10.5f}")

check(all(rows[i][4] < rows[i + 1][4] for i in range(len(rows) - 1)),
      "the ratio alpha_N/(m0+2 sigma_N) grows monotonically")
check(rows[-1][4] < 0.25, f"the ratio stays below 1/4 (={rows[-1][4]:.5f})")
check(abs(rows[-1][5] - 2.0) < 0.02, f"sigma_N/sqrt(N) -> 2  (={rows[-1][5]:.5f})")
check(abs(rows[-1][6] - 1.0) < 0.04, f"alpha_N/sqrt(N) -> 1  (={rows[-1][6]:.5f})")
check(abs(rows[-1][4] - 0.25) < 0.01, f"ratio -> 1/4  (={rows[-1][4]:.5f})")

# ---------------------------------------------------------------- 5
print("5. Theorem 5.1 (D1)  —  block positivity <=> regularized capacity")
rng = np.random.default_rng(20260806)
for trial in range(200):
    nc, na = 6, 4
    # old core with deliberately deficient support (to exercise the pseudoinverse)
    U = np.linalg.qr(rng.standard_normal((nc, nc)))[0]
    d = np.abs(rng.standard_normal(nc)); d[0] = 0.0          # D_0 singular
    D0 = U @ np.diag(d) @ U.T
    R0h = np.eye(nc)                                          # R_0 = I  (no loss)
    Aold = D0
    Qc = rng.standard_normal((nc, na)) * 0.4
    if trial % 2:                                             # half the cases: Qc in Ran D0
        Qc = D0 @ rng.standard_normal((nc, na)) * 0.6
    frak = np.eye(na)
    B = Qc
    Anew = frak
    A = np.block([[Aold, B], [B.T, Anew]])

    pos_direct = np.linalg.eigvalsh(A)[0] > -1e-11
    eps_ok = True
    for eps in [1e-1, 1e-3, 1e-5, 1e-7]:
        Ce = frak - B.T @ np.linalg.solve(Aold + eps * np.eye(nc), B)
        if np.linalg.eigvalsh(Ce)[0] < -1e-9:
            eps_ok = False
            break
    if pos_direct != eps_ok:
        raise AssertionError(f"D1 fails at trial {trial}")
check(True, "A >= 0  <=>  C_eps >= 0 for all eps>0   (200 cases, D_0 singular)")

# monotonicity in eps
mono = True
for trial in range(50):
    nc, na = 5, 3
    U = np.linalg.qr(rng.standard_normal((nc, nc)))[0]
    d = np.abs(rng.standard_normal(nc)); d[0] = 0.0
    D0 = U @ np.diag(d) @ U.T
    Qc = D0 @ rng.standard_normal((nc, na)) * 0.5
    prev = None
    for eps in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:
        Ce = np.eye(na) - Qc.T @ np.linalg.solve(D0 + eps * np.eye(nc), Qc)
        if prev is not None and np.linalg.eigvalsh(prev - Ce)[0] < -1e-9:
            mono = False
        prev = Ce
check(mono, "C_eps decreases as eps decreases (Theorem 5.1(1))")

print(f"\nVERDICT: {CHECKS} checks OK — the balanced factorization and D1 are verified.")
print("This does NOT certify D2, D3 or D4.  RH is not proved.")
