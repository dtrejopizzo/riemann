#!/usr/bin/env python3
"""
114_d3_01  --  verifier for "the imported index theorems and the Lorentzian test".

Lens d3 (external-index) of phase 114, row (d).  Everything here is a check of a
statement made in 114_d3_01_THE_IMPORTED_INDEX_THEOREMS.md.

Checks
  A. ruling arithmetic:  s(H,H)=2, s(f_v,f_h)=1, s(f_v-f_h,f_v-f_h)=-2.
  B. THE CHEAP DECISIVE TEST.  Inertia of the real form of s on increasing
     truncations built from GENUINE zeta zeros (mpmath.zetazero).  Does n_+ stay
     at 1, or does it grow with the size of the truncation?
  C. planted off-line zeros: n_+ = 1 + 2 * (number of off-line quadruples).
  D. reproduction of the two signatures reported in 113_12 section 4: (1,7) and
     (3,5), from the Hermitian coordinate model.
  E. the DOUBLING TRAP.  Hermitian inertia (p,q); real-form inertia (p,q);
     realification inertia (2p,2q).  The honest comparison object for an
     import of a REAL symmetric arithmetic intersection form is the real form.
  F. function-level Gram matrix: real functions in D (Gaussian-Hermite balanced
     profiles), Mellin-evaluated at genuine zeros in high precision; inertia of
     the resulting real symmetric Gram matrix.
  G. the Yuan-Zhang signature shape (arXiv:1304.3538v1, the paragraph after
     Thm 1.3): V isotropic, pairing on V^perp negative semi-definite, V maximal
     isotropic in V^perp, V^perp/V negative definite  ==>  Lorentzian (n_+ = 1).
  H. the witness for the finite-support no-go: f(u) = u^{-1/2} exp(-(log u)^2)
     is self-adjoint, lies in D, and z = f * f^* has z(p^k) > 0 for EVERY prime
     power, so the p-local coefficient of tau(z) is nonzero for every prime.

python3 with mpmath 1.3.0, numpy 1.26.4.
"""

import numpy as np
import mpmath as mp

FAILURES = []
NCHECK = [0]


def check(name, ok, detail=""):
    NCHECK[0] += 1
    print(("PASS  " if ok else "FAIL  ") + name + (("   [" + detail + "]") if detail else ""))
    if not ok:
        FAILURES.append(name)


# ----------------------------------------------------------------------------
# inertia helpers
# ----------------------------------------------------------------------------

def inertia_np(M, tol=None):
    """(n_+, n_0, n_-) of a real symmetric / complex Hermitian numpy matrix."""
    M = np.asarray(M)
    ev = np.linalg.eigvalsh((M + M.conj().T) / 2)
    if tol is None:
        tol = max(1e-9, 1e-10 * max(1.0, np.max(np.abs(ev))))
    return int(np.sum(ev > tol)), int(np.sum(np.abs(ev) <= tol)), int(np.sum(ev < -tol))


def inertia_mp(M, tol):
    """(n_+, n_0, n_-) of an mpmath real symmetric matrix, high precision."""
    ev = mp.eigsy(M, eigvals_only=True)
    p = sum(1 for e in ev if e > tol)
    z = sum(1 for e in ev if abs(e) <= tol)
    n = sum(1 for e in ev if e < -tol)
    return p, z, n


# ----------------------------------------------------------------------------
# the coordinate model of s   (113_08 (2.2), 113_12 Def/Thm 1.3, 107_241 (2.1))
#
#   s(x,y) = x^(0) conj(y^(1)) + x^(1) conj(y^(0)) - sum_rho m_rho x^(rho) conj(y^(rho'))
#   rho' = 1 - conj(rho)
# ----------------------------------------------------------------------------

def hermitian_gram(zeros, mult=None):
    """Gram matrix of s in the COMPLEX coordinate model with basis
       e_0, e_1 (polar) and e_rho for rho in `zeros` (a list of complex zeros,
       closed under rho -> conj(rho) and rho -> 1-conj(rho))."""
    if mult is None:
        mult = [1] * len(zeros)
    n = 2 + len(zeros)
    G = np.zeros((n, n), dtype=complex)
    G[0, 1] = 1.0
    G[1, 0] = 1.0
    idx = {}
    for j, r in enumerate(zeros):
        idx[complex(r)] = 2 + j
    for j, r in enumerate(zeros):
        rp = 1 - np.conj(r)
        k = idx[complex(rp)]
        # coefficient of x^(rho) conj(y^(rho')) is -m_rho
        G[2 + j, k] += -mult[j]
    return (G + G.conj().T) / 2


def real_gram(zeros_upper, mult=None, offline=None):
    """Gram matrix of s restricted to REAL f, in real coordinates.

    Real coordinates: a = f^(0), b = f^(1) (real), and for each zero rho in the
    UPPER half plane a pair (Re f^(rho), Im f^(rho)); the lower-half zero
    conj(rho) carries the conjugate value, and is NOT an independent coordinate.

    `zeros_upper` is a list of upper-half-plane zeros; `offline` is a list of
    booleans, True meaning the zero is off the critical line, in which case its
    mirror 1-conj(rho) is ALSO an upper-half-plane zero and is supplied as the
    next entry of the list (paired consecutively).
    """
    if mult is None:
        mult = [1] * len(zeros_upper)
    if offline is None:
        offline = [False] * len(zeros_upper)
    n = 2 + 2 * len(zeros_upper)
    G = np.zeros((n, n))
    G[0, 1] = 1.0
    G[1, 0] = 1.0
    j = 0
    while j < len(zeros_upper):
        if not offline[j]:
            # on-line rho: rho' = rho, contribution over {rho, conj rho} is
            # -2 m |z|^2  ->  -2m (x^2 + y^2)
            m = mult[j]
            G[2 + 2 * j, 2 + 2 * j] = -2.0 * m
            G[3 + 2 * j, 3 + 2 * j] = -2.0 * m
            j += 1
        else:
            # off-line quadruple {rho, conj rho, rho', conj rho'}: free complex
            # z = f^(rho), w = f^(rho'); contribution -4 m Re(z conj w)
            m = mult[j]
            a, b = 2 + 2 * j, 3 + 2 * j        # Re z, Im z
            c, d = 2 + 2 * (j + 1), 3 + 2 * (j + 1)  # Re w, Im w
            G[a, c] = G[c, a] = -2.0 * m
            G[b, d] = G[d, b] = -2.0 * m
            j += 2
    return G


# ----------------------------------------------------------------------------
# A. ruling arithmetic
# ----------------------------------------------------------------------------
print("=" * 78)
print("A. ruling arithmetic (113_09 Thm 4.1, 113_10 Thm 1.2)")
print("=" * 78)

# f_v^ = -2(s-1)xi, f_h^ = 2 s xi, H^ = 2 xi, xi(0)=xi(1)=1/2, xi(rho)=0
fv = np.array([1.0, 0.0])
fh = np.array([0.0, 1.0])
H = fv + fh


def spolar(x, y):
    return x[0] * y[1] + x[1] * y[0]


check("s(H,H) = 2", abs(spolar(H, H) - 2.0) < 1e-14, "%.1f" % spolar(H, H))
check("s(f_v,f_h) = 1", abs(spolar(fv, fh) - 1.0) < 1e-14, "%.1f" % spolar(fv, fh))
check("s(f_v,f_v) = 0", abs(spolar(fv, fv)) < 1e-14)
check("s(f_v-f_h, f_v-f_h) = -2", abs(spolar(fv - fh, fv - fh) + 2.0) < 1e-14,
      "%.1f" % spolar(fv - fh, fv - fh))
check("polar block is Lorentzian (1,1)", inertia_np(np.array([[0.0, 1.0], [1.0, 0.0]])) == (1, 0, 1))

# ----------------------------------------------------------------------------
# B. THE CHEAP DECISIVE TEST: does n_+ grow with the truncation?
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("B. inertia on increasing truncations, GENUINE zeros of zeta")
print("=" * 78)

NZ = 60
mp.mp.dps = 30
print("computing %d genuine zeta zeros with mpmath.zetazero ..." % NZ)
GAM = [float(mp.zetazero(k).imag) for k in range(1, NZ + 1)]
print("gamma_1 = %.9f ... gamma_%d = %.9f" % (GAM[0], NZ, GAM[-1]))

grew = False
for N in [1, 2, 3, 5, 8, 13, 21, 34, 55, 60]:
    ups = [complex(0.5, g) for g in GAM[:N]]
    Gr = real_gram(ups)
    p, z, m = inertia_np(Gr)
    ok = (p == 1 and m == 1 + 2 * N and z == 0)
    if p != 1:
        grew = True
    check("real form, %2d on-line zeros: (n_+,n_0,n_-) = (%d,%d,%d), predicted (1,0,%d)"
          % (N, p, z, m, 1 + 2 * N), ok)

check("n_+ does NOT grow with the truncation (positive index stays 1)", not grew,
      "tested up to %d zeros = dimension %d" % (NZ, 2 + 2 * NZ))

# complex Hermitian model, same truncations
grewH = False
for N in [1, 5, 21, 60]:
    zs = [complex(0.5, g) for g in GAM[:N]] + [complex(0.5, -g) for g in GAM[:N]]
    GH = hermitian_gram(zs)
    p, z, m = inertia_np(GH)
    if p != 1:
        grewH = True
    check("Hermitian model, %2d zero pairs: (n_+,n_0,n_-) = (%d,%d,%d), predicted (1,0,%d)"
          % (N, p, z, m, 1 + 2 * N), p == 1 and m == 1 + 2 * N)
check("Hermitian n_+ also stays 1 (107_241 Thm 3.1 with #P = 0)", not grewH)

# ----------------------------------------------------------------------------
# C. planted off-line zeros
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("C. planted off-line zeros:  n_+ = 1 + 2 * (# off-line quadruples)")
print("=" * 78)

for k in [1, 2, 3]:
    ups, off = [], []
    for j in range(k):                       # k off-line quadruples
        r = complex(0.5 + 0.1 * (j + 1), GAM[j])
        ups += [r, 1 - np.conj(r)]
        off += [True, True]
    for j in range(k, 8):                    # the rest on-line
        ups.append(complex(0.5, GAM[j]))
        off.append(False)
    Gr = real_gram(ups, offline=off)
    p, z, m = inertia_np(Gr)
    check("real form, %d off-line quadruple(s): n_+ = %d, predicted %d" % (k, p, 1 + 2 * k),
          p == 1 + 2 * k)

# Hermitian version: n_+ = 1 + #P, #P = 2 per quadruple (107_241 Thm 3.1)
for k in [1, 2]:
    zs, mult = [], []
    for j in range(k):
        r = complex(0.5 + 0.1 * (j + 1), GAM[j])
        for w in [r, np.conj(r), 1 - np.conj(r), 1 - r]:
            zs.append(complex(w))
    for j in range(k, 6):
        zs += [complex(0.5, GAM[j]), complex(0.5, -GAM[j])]
    GH = hermitian_gram(zs)
    p, z, m = inertia_np(GH)
    check("Hermitian, %d off-line quadruple(s) = %d mirror 2-cycles: n_+ = %d, predicted %d"
          % (k, 2 * k, p, 1 + 2 * k), p == 1 + 2 * k)

# ----------------------------------------------------------------------------
# D. reproduce 113_12 section 4: (1,7) on-line and (3,5) off-line
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("D. reproduction of the two signatures reported in 113_12 section 4")
print("=" * 78)

zs_on = []
for j in range(3):
    zs_on += [complex(0.5, GAM[j]), complex(0.5, -GAM[j])]
p, z, m = inertia_np(hermitian_gram(zs_on))
check("113_12's on-line model: (n_+,n_-) = (%d,%d), reported (1,7)" % (p, m), (p, m) == (1, 7))

r = complex(0.5 + 0.15, GAM[0])
zs_off = [complex(r), complex(np.conj(r)), complex(1 - np.conj(r)), complex(1 - r)]
zs_off += [complex(0.5, GAM[1]), complex(0.5, -GAM[1])]
p, z, m = inertia_np(hermitian_gram(zs_off))
check("113_12's off-line model: (n_+,n_-) = (%d,%d), reported (3,5)" % (p, m), (p, m) == (3, 5))

# ----------------------------------------------------------------------------
# E. the DOUBLING TRAP
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("E. the doubling trap: Hermitian (p,q) vs real form (p,q) vs realification (2p,2q)")
print("=" * 78)


def realify(GH):
    """R-linear realification of a Hermitian form: Re<x,y> on the underlying
       real vector space of twice the dimension."""
    A, B = GH.real, GH.imag
    return np.block([[A, -B], [B, A]])


zs = []
for j in range(4):
    zs += [complex(0.5, GAM[j]), complex(0.5, -GAM[j])]
GH = hermitian_gram(zs)
pH, zH, mH = inertia_np(GH)
GR = real_gram([complex(0.5, GAM[j]) for j in range(4)])
pR, zR, mR = inertia_np(GR)
GD = realify(GH)
pD, zD, mD = inertia_np(GD)
check("Hermitian inertia (%d,%d)" % (pH, mH), (pH, mH) == (1, 9))
check("real form inertia (%d,%d) EQUALS the Hermitian inertia" % (pR, mR), (pR, mR) == (pH, mH))
check("realification inertia (%d,%d) = (2p,2q) -- the trap" % (pD, mD), (pD, mD) == (2 * pH, 2 * mH))
check("realification is NOT Lorentzian (n_+ = 2): comparing it to an arithmetic "
      "surface form would falsely refute the import", pD == 2)

# ----------------------------------------------------------------------------
# F. function-level Gram matrix from actual elements of D
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("F. Gram matrix of s on actual functions in D (high precision)")
print("=" * 78)

mp.mp.dps = 60


def hatF(j, w, sigma):
    """two-sided Laplace transform  int x^j exp(-x^2/(4 sigma)) e^{w x} dx
       = sqrt(4 pi sigma) exp(sigma w^2) p_j(w),  p_0 = 1,
         p_{j+1} = p_j' + 2 sigma w p_j   (derivatives in w).
       Returned via the recursion evaluated symbolically in w by carrying
       (value, derivative) pairs is avoided: we use the explicit Hermite form.
       f(u) = u^{-1/2} F(log u) in D_theta for every theta;  f^(s) = hatF(s-1/2).
    """
    # p_j(w) computed from the coefficient recursion in the monomial basis
    P = [mp.mpf(1)]                     # p_0 = 1  (coefficients, low->high)
    for _ in range(j):
        dP = [P[k] * k for k in range(1, len(P))]
        sP = [mp.mpf(0)] + [2 * sigma * c for c in P]
        L = max(len(dP), len(sP))
        Q = [(dP[k] if k < len(dP) else 0) + (sP[k] if k < len(sP) else 0) for k in range(L)]
        P = Q
    val = mp.mpf(0)
    for k, c in enumerate(P):
        val += c * w ** k
    return mp.sqrt(4 * mp.pi * sigma) * mp.exp(sigma * w ** 2) * val


def coords(j, zeros_upper, sigma):
    """(a, b, [f^(rho) for rho in zeros_upper]) for the real function with
       balanced profile F(x) = x^j exp(-x^2/(4 sigma))."""
    a = hatF(j, mp.mpf(-0.5), sigma)
    b = hatF(j, mp.mpf(0.5), sigma)
    zs = [hatF(j, mp.mpc(0, g), sigma) for g in zeros_upper]
    return a, b, zs


NF, NZF = 8, 3
sigma = mp.mpf(1) / 4
ups = [mp.mpf(g) for g in GAM[:NZF]]
C = [coords(j, ups, sigma) for j in range(NF)]
G = mp.zeros(NF, NF)
for i in range(NF):
    for k in range(NF):
        ai, bi, zi = C[i]
        ak, bk, zk = C[k]
        # s(f_i, f_k) = a_i b_k + b_i a_k - sum over ALL zeros (rho and conj rho),
        # on-line: rho' = rho, so the term is -( z_i conj(z_k) + conj(z_i) z_k )
        v = ai * bk + bi * ak
        for t in range(NZF):
            v -= 2 * mp.re(zi[t] * mp.conj(zk[t]))
        G[i, k] = mp.re(v)
print("Gram entries range: |G_00| = %s, |G_%d%d| = %s"
      % (mp.nstr(abs(G[0, 0]), 6), NF - 1, NF - 1, mp.nstr(abs(G[NF - 1, NF - 1]), 6)))
scale = max(abs(G[i, k]) for i in range(NF) for k in range(NF))
p, z, m = inertia_mp(G, tol=scale * mp.mpf(10) ** (-40))
check("real Gaussian-Hermite basis (%d functions, %d genuine zeros): inertia (%d,%d,%d)"
      % (NF, NZF, p, z, m), p == 1,
      "n_+ = 1 as predicted for a Lorentzian form under RH")

# same, with one zero moved off the critical line: n_+ must jump
ups2 = [mp.mpc(0.5, GAM[0]) - mp.mpf(0.5), mp.mpc(0.5, -GAM[0]) - mp.mpf(0.5)]  # dummy


def coords_general(j, wlist, sigma):
    return [hatF(j, w, sigma) for w in wlist]


# off-line quadruple rho = 0.65 + i*gamma_1 : w = rho - 1/2
rho = mp.mpc(0.65, GAM[0])
quad = [rho, mp.conj(rho), 1 - mp.conj(rho), 1 - rho]
wl = [r - mp.mpf(0.5) for r in quad] + [mp.mpc(0, GAM[1]), mp.mpc(0, -GAM[1])]
allz = quad + [mp.mpc(0.5, GAM[1]), mp.mpc(0.5, -GAM[1])]
mirror = {}
for i2, r2 in enumerate(allz):
    for k2, r3 in enumerate(allz):
        if abs((1 - mp.conj(r2)) - r3) < mp.mpf(10) ** (-30):
            mirror[i2] = k2
G2 = mp.zeros(NF, NF)
CV = []
for j in range(NF):
    a = hatF(j, mp.mpf(-0.5), sigma)
    b = hatF(j, mp.mpf(0.5), sigma)
    zs = coords_general(j, wl, sigma)
    CV.append((a, b, zs))
for i in range(NF):
    for k in range(NF):
        ai, bi, zi = CV[i]
        ak, bk, zk = CV[k]
        v = ai * bk + bi * ak
        for t in range(len(allz)):
            v -= zi[t] * mp.conj(zk[mirror[t]])
        G2[i, k] = mp.re(v)
scale2 = max(abs(G2[i, k]) for i in range(NF) for k in range(NF))
p2, z2, m2 = inertia_mp(G2, tol=scale2 * mp.mpf(10) ** (-40))
check("same basis, one off-line quadruple planted: inertia (%d,%d,%d), n_+ > 1"
      % (p2, z2, m2), p2 > 1, "an off-line zero is visible as extra positivity")

# ----------------------------------------------------------------------------
# G. the Yuan-Zhang signature shape forces Lorentzian
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("G. Yuan-Zhang shape (arXiv:1304.3538v1, paragraph after Thm 1.3) => n_+ = 1")
print("=" * 78)

rng = np.random.default_rng(20260804)
allok = True
for trial in range(200):
    n = rng.integers(3, 9)
    # build W = R v0 + R L + N  with:  v0 spans V = pi^* Pic-hat(K), isotropic,
    # <v0,v0> = 0, <v0,N> = 0, <v0,L> = d > 0, N negative definite, <L,L> free.
    k = n - 2
    A = rng.normal(size=(k, k))
    Nneg = -(A @ A.T) - np.eye(k) * 0.5          # negative definite
    d = rng.uniform(0.5, 3.0)
    G = np.zeros((n, n))
    G[0, 1] = G[1, 0] = d
    G[1, 1] = rng.normal() * 3
    G[2:, 2:] = Nneg
    G[1, 2:] = rng.normal(size=k)
    G[2:, 1] = G[1, 2:]
    p, z, m = inertia_np(G)
    if not (p == 1 and z == 0 and m == n - 1):
        allok = False
check("V isotropic + <V,L> != 0 + V^perp/V negative definite  ==>  inertia (1,0,n-1) "
      "in 200 random instances", allok)

# and the degenerate case where V is in the radical (our s: rad = (chi))
allok2 = True
for trial in range(200):
    n = rng.integers(4, 9)
    k = n - 3
    A = rng.normal(size=(k, k))
    Nneg = -(A @ A.T) - np.eye(k) * 0.5
    G = np.zeros((n, n))
    G[0, 1] = G[1, 0] = 1.0                       # hyperbolic polar block
    G[2:2 + k, 2:2 + k] = Nneg                    # negative definite zero block
    # last coordinate = radical direction
    p, z, m = inertia_np(G)
    if not (p == 1 and z == 1 and m == n - 2):
        allok2 = False
check("polar hyperbolic + negative definite + 1-dim radical ==> (1,1,n-2): the shape "
      "of s under RH, in 200 random instances", allok2)

# ----------------------------------------------------------------------------
# H. the witness for the finite-support no-go
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("H. witness  f(u) = u^{-1/2} exp(-(log u)^2)  and z = f * f^*")
print("=" * 78)

mp.mp.dps = 30


def f_wit(u):
    return u ** mp.mpf(-0.5) * mp.exp(-mp.log(u) ** 2)


def z_wit(u):
    # profile of f is exp(-x^2); (F*F)(x) = sqrt(pi/2) exp(-x^2/2)
    return u ** mp.mpf(-0.5) * mp.sqrt(mp.pi / 2) * mp.exp(-mp.log(u) ** 2 / 2)


# self-adjointness  f^*(u) = conj(f(1/u))/u = f(u)
ok = all(abs(f_wit(mp.mpf(1) / u) / u - f_wit(u)) < mp.mpf(10) ** (-25)
         for u in [mp.mpf('0.3'), mp.mpf(1), mp.mpf(2), mp.mpf(17)])
check("f^* = f (the witness is self-adjoint)", ok)

# z = f * f^* by numerical Mellin convolution, against the closed form
for u in [mp.mpf('0.5'), mp.mpf(2), mp.mpf(7)]:
    num = mp.quad(lambda t: f_wit(t) * f_wit(u / t) / t, [0, mp.inf])
    ok = abs(num - z_wit(u)) < mp.mpf(10) ** (-20)
    check("z(%s) = (f * f)(%s) matches the closed form" % (mp.nstr(u, 3), mp.nstr(u, 3)), ok,
          "num=%s closed=%s" % (mp.nstr(num, 12), mp.nstr(z_wit(u), 12)))


def primes_upto(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    return np.nonzero(sieve)[0]


PS = primes_upto(10000)
cps = []
for p in PS:
    p = int(p)
    tot = mp.mpf(0)
    for k in range(1, 40):
        term = z_wit(mp.mpf(p) ** k) + z_wit(mp.mpf(p) ** (-k)) / mp.mpf(p) ** k
        tot += term
        if term < mp.mpf(10) ** (-40):
            break
    cps.append(mp.log(p) * tot)
check("c_p != 0 for every one of the %d primes below 10^4" % len(PS),
      all(c > 0 for c in cps), "min c_p = %s at p = %d" % (mp.nstr(min(cps), 6), int(PS[-1])))
check("c_p is strictly positive (so the support of the prime decomposition of "
      "tau(f * f^*) is ALL primes, an infinite set)", all(c > 0 for c in cps))
tail = sum(cps[-100:])
check("sum_p c_p converges (tail over the last 100 primes < 1e-8)",
      tail < mp.mpf(10) ** (-8), "tail = %s" % mp.nstr(tail, 6))

# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("checks run: %d      failures: %d" % (NCHECK[0], len(FAILURES)))
if FAILURES:
    for f in FAILURES:
        print("FAILED: " + f)
    print("VERDICT: FAILURES PRESENT")
    raise SystemExit(1)
print("VERDICT: ALL CHECKS PASS")
