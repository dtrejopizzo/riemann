#!/usr/bin/env python3
"""
113_06 verifier -- the canonical Weil decomposition on the admissible class,
and the log p defect in 113_01/113_02/113_03.

Checks:
 1. Theorem 2.1 (canonical decomposition), on five independent probes:
        hhat(0) + hhat(1) - sum_rho m_rho hhat(rho)
      = sum_p log p [ A_p(h) + B_p(h) ]  -  A(h)
 2. The identity FAILS with the unweighted finite sum used in 113_01/02/03
    (the log p defect is real, not a normalization convention).
 3. The defect is not a single global constant: (weighted - unweighted)
    is not proportional to hhat(1) across probes.
 4. Theorem 3.1: the eta > 1 threshold is unchanged by the log p weight
    (A_p drives it, B_p is slack by a full power of p).
 5. Theorem 4.1: with h(1) = 0 the archimedean integrand
    h(u^{-1}) / |1 - u| is bounded at u = 1; with h(1) != 0 it blows up.

Zeros of xi are used ONLY here, inside a numerical check of a classical
identity that this file quotes; no definition in 113_06 uses a zero, a Li
coefficient, or a positive part of a Weil-type form.
"""
import numpy as np
import mpmath as mp

try:
    from scipy.special import digamma as _digamma
    def psi(z):
        return _digamma(z)
except Exception:                                   # pragma: no cover
    def psi(z):
        z = np.asarray(z)
        return np.array([complex(mp.digamma(complex(v))) for v in z.ravel()]).reshape(z.shape)

PASS = []


def check(name, cond, detail=""):
    PASS.append(bool(cond))
    print(("PASS" if cond else "FAIL") + f": {name}" + (f" ({detail})" if detail else ""))


# ----------------------------------------------------------------------
# grids
# ----------------------------------------------------------------------
XCUT, NX = 14.0, 800
_n, _w = np.polynomial.legendre.leggauss(NX)
X, WX = XCUT * _n, XCUT * _w                        # log-variable grid

TCUT, NT = 40.0, 1200
_m, _v = np.polynomial.legendre.leggauss(NT)
T, WT = TCUT * _m, TCUT * _v                        # critical-line grid

PMAX = 3000                                         # primes used in the finite sum
KMAX = 60                                           # prime powers per prime


def primes_upto(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    return np.nonzero(sieve)[0]


PRIMES = primes_upto(PMAX)
LOGP = np.log(PRIMES.astype(float))

# nontrivial zeros: rho = 1/2 +- i gamma_n.  Criticality of these particular
# zeros is a verified computation, not an assumption; and for every probe
# below the tail past gamma_1 = 14.13 is smaller than 1e-20 anyway.
NZ = 20
GAMMAS = np.array([float(mp.im(mp.zetazero(n))) for n in range(1, NZ + 1)])


# ----------------------------------------------------------------------
# probes: real profiles h~(x) with h~(0) = h(1) = 0
# ----------------------------------------------------------------------
PROBES = {
    "x e^{-x^2}":          lambda x: x * np.exp(-x * x),
    "x e^{-2x^2}":         lambda x: x * np.exp(-2 * x * x),
    "x^3 e^{-x^2}":        lambda x: x ** 3 * np.exp(-x * x),
    "sin(x) e^{-x^2}":     lambda x: np.sin(x) * np.exp(-x * x),
    "x e^{-x^2} cos(2x)":  lambda x: x * np.exp(-x * x) * np.cos(2 * x),
}


def hhat(prof, s):
    """convention B: hhat(s) = int h~(x) e^{sx} dx"""
    s = np.asarray(s, dtype=complex)
    return (prof(X)[None, :] * np.exp(np.outer(s, X)) * WX[None, :]).sum(axis=1)


def finite_sum(prof, weighted=True):
    """sum_p w_p [ A_p + B_p ],  A_p = sum_k h(p^k),  B_p = sum_m h(p^-m) p^-m"""
    k = np.arange(1, KMAX + 1)[None, :]
    lp = LOGP[:, None]
    A = prof(k * lp).sum(axis=1)
    B = (prof(-k * lp) * np.exp(-k * lp)).sum(axis=1)
    w = LOGP if weighted else np.ones_like(LOGP)
    return float(np.dot(w, A + B))


def archimedean(prof):
    """A(h) = (1/2pi) int [ (1/2)Re psi(1/4 + it/2) - (1/2)log pi ] G(1/2+it) dt,
       G(1/2+it) = hhat(1/2+it) + hhat(1/2-it)   (even in t)."""
    ker = 0.5 * np.real(psi(0.25 + 0.5j * T)) - 0.5 * np.log(np.pi)
    G = hhat(prof, 0.5 + 1j * T) + hhat(prof, 0.5 - 1j * T)
    return float(np.real(np.dot(WT, ker * G)) / (2 * np.pi))


def zero_sum(prof):
    rr = np.concatenate([0.5 + 1j * GAMMAS, 0.5 - 1j * GAMMAS])
    return complex(hhat(prof, rr).sum())


# ----------------------------------------------------------------------
# 1./2./3.
# ----------------------------------------------------------------------
print("probe                 |    LHS (Weil)  |  P(h)-A(h)   |   residual   |  unweighted err")
print("-" * 88)
gaps = []
for name, prof in PROBES.items():
    h0, h1 = [complex(v) for v in hhat(prof, [0.0, 1.0])]
    zs = zero_sum(prof)
    lhs = h0 + h1 - zs
    P = finite_sum(prof, weighted=True)
    P0 = finite_sum(prof, weighted=False)
    A = archimedean(prof)
    rhs = P - A
    rhs0 = P0 - A
    res = abs(lhs - rhs)
    scale = 1 + abs(lhs)
    print(f"{name:21s} | {lhs.real:14.9f} | {rhs:12.9f} | {res:12.3e} | {abs(lhs-rhs0):12.3e}")
    check(f"Theorem 2.1 canonical decomposition holds for {name}",
          res < 1e-8 * scale, f"residual={res:.3e}")
    check(f"log p defect is real for {name}: the unweighted sum does NOT satisfy it",
          abs(lhs - rhs0) > 1e-3 * scale, f"unweighted error={abs(lhs-rhs0):.6f}")
    gaps.append((abs(P - P0), abs(h1)))

# the defect is not a single global factor
ratios = [g / m for g, m in gaps]
check("the log p defect is not proportional to hhat(1) (so it is not a global rescaling)",
      max(ratios) / min(ratios) > 1.5,
      f"ratio spread {min(ratios):.4f} .. {max(ratios):.4f}")

# ----------------------------------------------------------------------
# 4. the eta > 1 threshold is unchanged by the log p weight
#
# Diagnostic: for sum_p (log p) p^{-a}, the prime number theorem gives an
# increment over the block [N, 4N] asymptotic to int_N^{4N} t^{-a} dt, so
# successive block increments have ratio exactly 4^{1-a}.  That ratio is
# < 1 iff a > 1.  Testing the ratio AGAINST its predicted value is a far
# stronger check than testing convergence by eye: it pins the exponent.
# ----------------------------------------------------------------------
print()
CUTS = (400, 1600, 6400, 25600)


def block_ratio(prof, part_kind):
    part = []
    for cut in CUTS:
        pp = primes_upto(cut).astype(float)
        k = np.arange(1, 40)[None, :]
        lp = np.log(pp)[:, None]
        if part_kind == "A":
            S = prof(k * lp).sum(axis=1)
        else:
            S = (prof(-k * lp) * np.exp(-k * lp)).sum(axis=1)
        part.append(float(np.dot(np.log(pp), S)))
    incs = np.diff(part)
    return incs[-1] / incs[-2], incs


for eta in (1.4, 1.2, 1.0, 0.8):
    pr = lambda x, e=eta: np.sign(x) * np.exp(-e * np.abs(x))
    r, incs = block_ratio(pr, "A")
    pred = 4.0 ** (1 - eta)
    check(f"eta={eta}: sum_p log p A_p has block ratio {r:.4f}, predicted 4^(1-eta)={pred:.4f}",
          abs(r - pred) < 0.06, f"increments {incs[-2]:.4e} -> {incs[-1]:.4e}")
    check(f"eta={eta}: {'converges' if eta > 1 else 'DIVERGES'}, as the threshold requires",
          (r < 0.95) == (eta > 1), f"ratio={r:.4f}")

# B_p is slack by a full power of p: its exponent is eta+1, so it converges
# for every eta > 0 -- verified at eta = 0.5, where A_p diverges badly.
pr = lambda x: np.sign(x) * np.exp(-0.5 * np.abs(x))
rB, incsB = block_ratio(pr, "B")
check("B_p is slack: sum_p log p B_p has block ratio 4^(1-(eta+1))=0.5 at eta=0.5",
      abs(rB - 0.5) < 0.06, f"ratio={rB:.4f}, increments {incsB[-2]:.4e} -> {incsB[-1]:.4e}")
rA, _ = block_ratio(pr, "A")
check("at eta=0.5 the A_p half diverges while the B_p half converges (A_p is what sets the threshold)",
      rA > 1.0 and rB < 0.95, f"ratio_A={rA:.4f}, ratio_B={rB:.4f}")

# ----------------------------------------------------------------------
# 5. h(1) = 0 removes the archimedean singularity at u = 1
# ----------------------------------------------------------------------
print()
prof0 = PROBES["x e^{-x^2}"]                 # h(1) = 0
prof1 = lambda x: np.exp(-x * x)             # h(1) = 1
eps = np.array([1e-2, 1e-3, 1e-4, 1e-5])
for nm, pr_, want_bounded in [("h(1)=0 probe", prof0, True), ("h(1)=1 probe", prof1, False)]:
    u = 1 + eps
    val = np.abs(pr_(-np.log(u)) / np.abs(1 - u))
    if want_bounded:
        check(f"Theorem 4.1 {nm}: |h(1/u)|/|1-u| stays bounded as u -> 1",
              val.max() < 10, f"max={val.max():.4f}")
    else:
        check(f"Theorem 4.1 {nm}: |h(1/u)|/|1-u| blows up as u -> 1 (test not vacuous)",
              val[-1] > 1e4, f"values {val[0]:.1f} .. {val[-1]:.3e}")

# ----------------------------------------------------------------------
print()
if all(PASS):
    print("VERDICT: ALL CHECKS PASS")
    raise SystemExit(0)
print("VERDICT: SOME CHECKS FAILED")
raise SystemExit(1)
