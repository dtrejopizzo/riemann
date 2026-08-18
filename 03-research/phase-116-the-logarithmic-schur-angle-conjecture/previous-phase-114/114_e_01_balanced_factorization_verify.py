#!/usr/bin/env python3
"""E.01 verifier — factorizacion de canal balanceada y contrato de un paso.

Verifica las afirmaciones numericas de 114_e_01_BALANCED_CHANNEL_FACTORIZATION.md:

  1. Lema 2.2   Jhat_{a,pm}^* Jhat_{a,pm} = I +- Re S_a   (codominio L^2(R))
                y por tanto  S_a + S_{-a} = J+*J+ - J-*J-
  2. Obs 2.3    la lectura truncada da 1-cos(pi/(2m+1)), no 1-cos(pi/(m+1))
  3. Seccion 1  g_Gamma >= 0  y  m_0 = log(pi)+gamma+pi/2+3log2
  4. Prop 4.1   sigma_N ~ 2 sqrt(N), alpha_N ~ sqrt(N), cociente -> 1/4
  5. Thm 5.1    D1 en forma regularizada, sobre matrices aleatorias

Solo requiere numpy, mpmath y sympy.  No usa flint: no certifica nada, verifica.
"""
import numpy as np
import mpmath as mp
from sympy import factorint

CHECKS = 0

def check(cond, label):
    global CHECKS
    assert cond, f"FALLO: {label}"
    CHECKS += 1
    print(f"  ok  {label}")


# ---------------------------------------------------------------- 1 y 2
def channels(T2, a, n=500):
    """Devuelve (I, Re S_a, J-*J-, J+*J+, J-*J- truncado) en la malla de n celdas."""
    h = T2 / n
    k = a / h
    k0, frac = int(np.floor(k)), k - int(np.floor(k))

    pad = k0 + 2                       # celdas a la izquierda de t=0
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

    Jm_tr = Jm[pad:pad + n, :]         # salida truncada a la ventana (lectura errada)
    return np.eye(n), ReS, Jm.T @ Jm, Jp.T @ Jp, Jm_tr.T @ Jm_tr


print("1. Lema 2.2 / Teorema 3.1  —  identidad de canal")
worst = 0.0
for (T2, a) in [(1.0, 0.6), (1.0, 0.4), (1.0, 0.26), (1.0, 0.9), (1.0, 0.21), (2.0, 0.7)]:
    I, ReS, JmJm, JpJp, _ = channels(T2, a)
    worst = max(worst,
                np.abs(JmJm - (I - ReS)).max(),
                np.abs(JpJp - (I + ReS)).max(),
                np.abs((JpJp - JmJm) - 2 * ReS).max())
check(worst < 1e-12, f"J(pm)*J(pm) = I +- Re S_a  y  S_a+S_-a = J+*J+ - J-*J-  (err {worst:.2e})")

print("2. Observacion 2.3  —  el codominio decide la constante espectral")
for (T2, a) in [(1.0, 0.6), (1.0, 0.4), (1.0, 0.26)]:
    m = int(np.ceil(T2 / a))
    I, ReS, JmJm, _, Jtr = channels(T2, a)
    lo_full = np.linalg.eigvalsh(JmJm)[0]
    lo_trunc = np.linalg.eigvalsh(Jtr)[0]
    check(abs(lo_full - (1 - np.cos(np.pi / (m + 1)))) < 1e-9,
          f"m={m}: codominio L2(R) da 1-cos(pi/(m+1)) = {lo_full:.9f}")
    check(abs(lo_trunc - (1 - np.cos(np.pi / (2 * m + 1)))) < 1e-9,
          f"m={m}: lectura truncada da 1-cos(pi/(2m+1)) = {lo_trunc:.9f}")

# ---------------------------------------------------------------- 3
print("3. Seccion 1  —  el canal Gamma es positivo, y el valor de m_0")
mp.mp.dps = 40
g = lambda tau: mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * tau / 2)) - mp.digamma(mp.mpf(1) / 4)
vals = [g(mp.mpf(t)) for t in [0, 0.5, 1, 2, 5, 20, 100, 1000]]
check(abs(vals[0]) < mp.mpf('1e-30'), "g_Gamma(0) = 0")
check(all(vals[i] < vals[i + 1] for i in range(len(vals) - 1)),
      "g_Gamma creciente en |tau| (=> g_Gamma >= 0)")
m0 = mp.log(mp.pi) + mp.euler + mp.pi / 2 + 3 * mp.log(2)
check(abs(m0 - mp.mpf('5.3721834192256662')) < mp.mpf('1e-15'),
      f"m_0 = {mp.nstr(m0, 17)}")

# ---------------------------------------------------------------- 4
print("4. Proposicion 4.1  —  el deficit escalar tiende a 1/4")

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
      f" {'cociente':>10} {'sig/sqrtN':>10} {'alp/sqrtN':>10}")
for r in rows:
    print(f"    {r[0]:>7} {r[1]:>10.4f} {r[2]:>10.4f} {r[3]:>11.4f}"
          f" {r[4]:>10.5f} {r[5]:>10.5f} {r[6]:>10.5f}")

check(all(rows[i][4] < rows[i + 1][4] for i in range(len(rows) - 1)),
      "el cociente alpha_N/(m0+2 sigma_N) crece monotonamente")
check(rows[-1][4] < 0.25, f"el cociente sigue por debajo de 1/4 (={rows[-1][4]:.5f})")
check(abs(rows[-1][5] - 2.0) < 0.02, f"sigma_N/sqrt(N) -> 2  (={rows[-1][5]:.5f})")
check(abs(rows[-1][6] - 1.0) < 0.04, f"alpha_N/sqrt(N) -> 1  (={rows[-1][6]:.5f})")
check(abs(rows[-1][4] - 0.25) < 0.01, f"cociente -> 1/4  (={rows[-1][4]:.5f})")

# ---------------------------------------------------------------- 5
print("5. Teorema 5.1 (D1)  —  positividad de bloque <=> capacidad regularizada")
rng = np.random.default_rng(20260806)
for trial in range(200):
    nc, na = 6, 4
    # old core con soporte deficiente a proposito (para ejercitar el pseudoinverso)
    U = np.linalg.qr(rng.standard_normal((nc, nc)))[0]
    d = np.abs(rng.standard_normal(nc)); d[0] = 0.0          # D_0 singular
    D0 = U @ np.diag(d) @ U.T
    R0h = np.eye(nc)                                          # R_0 = I  (sin perdida)
    Aold = D0
    Qc = rng.standard_normal((nc, na)) * 0.4
    if trial % 2:                                             # mitad de los casos: Qc en Ran D0
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
        raise AssertionError(f"D1 falla en trial {trial}")
check(True, "A >= 0  <=>  C_eps >= 0 para todo eps>0   (200 casos, D_0 singular)")

# monotonia en eps
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
check(mono, "C_eps decrece cuando eps baja (Teorema 5.1(1))")

print(f"\nVERDICT: {CHECKS} checks OK — la factorizacion balanceada y D1 se verifican.")
print("Esto NO certifica D2, D3 ni D4.  RH no esta probada.")
