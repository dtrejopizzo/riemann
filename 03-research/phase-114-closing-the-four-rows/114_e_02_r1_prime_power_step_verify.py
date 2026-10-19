#!/usr/bin/env python3
"""E.02 verifier — R1: exactness of the step between consecutive prime powers.

Let  2=q_1<q_2<... be the sequence of prime powers and  tau_j = (1/2) log q_j.

Verified:
  R1.a  the contact list {n : 2 <= n < e^{2T}} is constant on (tau_j, tau_{j+1}]
  R1.b  the birth is null: the incoming contact q_j has shift log q_j = 2 tau_j,
        exactly the width of the old window, so <S F, F> = 0 for F supported on I_{tau_j}
  R1.c  the Gamma channel is independent of the window on functions extended by zero
  R1.d  CONSEQUENCE: A_{tau_{j+1}} compressed to the transported old core is EXACTLY
        A_{tau_j}.  The old block receives no correction from the newly born contact.
  R1.e  structure of the corona: A = C^perp within P_{tau_{j+1}} consists of the
        primitive functions supported on the ring PLUS at most 2 Tate directions
        supported on the core.
"""
import numpy as np
from sympy import factorint

CHECKS = 0
def check(cond, label):
    global CHECKS
    assert cond, f"FAILURE: {label}"
    CHECKS += 1
    print(f"  ok  {label}")


def prime_powers(limit):
    out = []
    for n in range(2, limit + 1):
        if len(factorint(n)) == 1:
            out.append(n)
    return out

QS = prime_powers(60)
print(f"prime powers: {QS[:14]} ...\n")

# ---------------------------------------------------------------- R1.a
print("R1.a  the contact list is constant on (tau_j, tau_{j+1}]")
ok = True
for j in range(len(QS) - 1):
    qj, qj1 = QS[j], QS[j + 1]
    tj, tj1 = 0.5 * np.log(qj), 0.5 * np.log(qj1)
    base = None
    for frac in [1e-9, 0.01, 0.25, 0.5, 0.75, 1.0]:
        T = tj + frac * (tj1 - tj)
        # compare in log space: n < e^{2T}  <=>  log n < 2T.  Avoids exp() rounding
        # above q_{j+1} right at the endpoint T = tau_{j+1}.
        contacts = tuple(q for q in QS if np.log(q) < 2 * T)
        if base is None:
            base = contacts
        elif contacts != base:
            ok = False
    # and it must be exactly {q_1..q_j}
    if base != tuple(QS[:j + 1]):
        ok = False
check(ok, f"constant and equal to {{q_1..q_j}} in the {len(QS)-1} steps tested")

# ---------------------------------------------------------------- R1.b
print("R1.b  the birth is null (translated supports disjoint)")
def overlap_measure(T, a):
    """measure of  (-T,T) inter (-T-a, T-a)  = support where <S_a F, F> can be != 0."""
    lo, hi = max(-T, -T - a), min(T, T - a)
    return max(0.0, hi - lo)

ok = True
for j in range(len(QS)):
    tj = 0.5 * np.log(QS[j])
    a = np.log(QS[j])                      # shift of the incoming contact = 2 tau_j
    if overlap_measure(tj, a) > 1e-12:
        ok = False
check(ok, "log q_j = 2 tau_j  =>  null overlap at the instant of birth")

# and the overlap opens strictly afterward
ok = all(overlap_measure(0.5 * np.log(QS[j]) + 1e-3, np.log(QS[j])) > 0
         for j in range(len(QS)))
check(ok, "the overlap opens strictly for T > tau_j")

# direct numerical verification of the inner product, not only of the supports
def shift_form(T, a, n=800):
    """<S_a F, F> + c.c. for F=indicator of a subcell, in the window (-T,T)."""
    h = 2 * T / n
    grid = -T + (np.arange(n) + 0.5) * h
    k = a / h
    k0, frac = int(np.floor(k)), k - int(np.floor(k))
    S = np.zeros((n, n))
    for i in range(n):
        for (kk, w) in ((k0, 1 - frac), (k0 + 1, frac)):
            if 0 <= i + kk < n:
                S[i, i + kk] += w
    return (S + S.T) * h

worst = 0.0
for j in range(len(QS)):
    tj = 0.5 * np.log(QS[j])
    M = shift_form(tj, np.log(QS[j]))
    worst = max(worst, np.abs(M).max())
check(worst < 1e-12, f"shift form identically null at T=tau_j (max |.| = {worst:.2e})")

# ---------------------------------------------------------------- R1.c
print("R1.c  the Gamma channel does not depend on the window on functions extended by zero")
# <G_{Gamma,T} F, F> = (1/2pi) int g(tau) |FT(Ftilde)(tau)|^2 dtau  -- depends only on Ftilde.
# Confirmed by comparing the form computed in two different windows for the same F.
try:
    from scipy.special import psi as _psi          # vectorized over complex numbers
    def g_gamma(tau):
        return np.real(_psi(0.25 + 0.5j * np.abs(tau))) - float(_psi(0.25).real)
except ImportError:                                 # slow fallback
    import mpmath as mp
    mp.mp.dps = 25
    _p0 = float(mp.digamma(mp.mpf(1) / 4))
    def g_gamma(tau):
        return np.array([float(mp.re(mp.digamma(mp.mpf(1)/4 + 1j*abs(t)/2))) - _p0
                         for t in np.atleast_1d(tau)])

def gamma_form(F, x, L, nfft=1 << 13):
    """(1/2pi) int g_Gamma(tau) |hat F(tau)|^2 dtau  via FFT over [-L,L]."""
    h = x[1] - x[0]
    pad = np.zeros(nfft); pad[:len(F)] = F
    Fh = np.fft.fft(pad) * h
    tau = 2 * np.pi * np.fft.fftfreq(nfft, d=h)
    dtau = abs(tau[1] - tau[0])
    return float((g_gamma(tau) * np.abs(Fh) ** 2).sum() * dtau / (2 * np.pi))

rng = np.random.default_rng(7)
T_small, T_big = 0.5 * np.log(5), 0.5 * np.log(7)
n_small = 600
h = 2 * T_small / n_small
xs = -T_small + (np.arange(n_small) + 0.5) * h
Fvals = rng.standard_normal(n_small)
# same F, embedded in the small window and in the big one (extension by zero)
n_big = int(np.round(2 * T_big / h))
xb = -T_big + (np.arange(n_big) + 0.5) * h
Fbig = np.zeros(n_big)
i0 = int(np.round((xs[0] - xb[0]) / h))
Fbig[i0:i0 + n_small] = Fvals
v1 = gamma_form(Fvals, xs, T_small)
v2 = gamma_form(Fbig, xb, T_big)
rel = abs(v1 - v2) / max(abs(v1), 1e-30)
check(rel < 1e-10, f"identical Gamma form in both windows (relative diff. {rel:.2e})")

# ---------------------------------------------------------------- R1.d
print("R1.d  CONSEQUENCE: the old core block is exactly A_{tau_j}")
# A_{T'} - A_T on functions supp. in I_T  =  - sum_{e^{2T} <= n < e^{2T'}} w_n (S+S*)
# The only n in that range with Lambda(n)!=0 is q_j, and its form is null by R1.b.
ok = True
for j in range(len(QS) - 1):
    qj, qj1 = QS[j], QS[j + 1]
    extra = [n for n in range(qj, qj1) if len(factorint(n)) == 1]
    if extra != [qj]:
        ok = False
check(ok, "the only contact entering [q_j, q_{j+1}) is q_j")
check(worst < 1e-12,
      "and its form vanishes on the core  =>  A_old = A_{tau_j}  WITHOUT correction")

# ---------------------------------------------------------------- R1.e
print("R1.e  corona structure A = C^perp within P_{tau_{j+1}}")
def primitive_basis(T, n):
    """orthonormal basis of P_T = ker M_- ∩ ker M_+ on the n-cell mesh."""
    h = 2 * T / n
    x = -T + (np.arange(n) + 0.5) * h
    M = np.vstack([np.exp(-x / 2), np.exp(x / 2)]) * h        # the two Tate functionals
    # kernel of M
    U, s, Vt = np.linalg.svd(M)
    return Vt[2:].T / np.sqrt(h), x, h                        # orthonormal in L^2

for (qj, qj1) in [(4, 5), (5, 7), (7, 8), (8, 9)]:
    tj, tj1 = 0.5 * np.log(qj), 0.5 * np.log(qj1)
    # Choose the mesh so that the core is an INTEGER number of cells of the large mesh:
    # fix h from the core, and adjust the outer window to n_out*h (differs from 2*tau_{j+1}
    # by less than one cell).  Without this the nesting is only exact to O(h).
    n_in = 700
    h = 2 * tj / n_in
    n_out = int(np.round(2 * tj1 / h))
    if (n_out - n_in) % 2:
        n_out += 1                                             # centered core
    tj1_grid = n_out * h / 2
    Pbig, xb, hb = primitive_basis(tj1_grid, n_out)
    # transported old core: primitives of the small window, extended by zero
    Psmall, xs2, hs = primitive_basis(tj, n_in)
    i0 = (n_out - n_in) // 2
    C = np.zeros((n_out, Psmall.shape[1]))
    C[i0:i0 + n_in, :] = Psmall
    # project C onto P_big (it should already be inside: nesting)
    coeff = Pbig.T @ C * hb
    resid = np.abs(C - Pbig @ coeff).max()
    # dimension of the corona within P_big
    dimP, dimC = Pbig.shape[1], np.linalg.matrix_rank(coeff, tol=1e-8)
    # primitive functions supported on the ring
    ann = np.zeros((n_out, 0))
    mask = np.ones(n_out, bool); mask[i0:i0 + n_in] = False
    Ann = np.eye(n_out)[:, mask]
    Mt = np.vstack([np.exp(-xb / 2), np.exp(xb / 2)]) * hb
    K = Mt @ Ann
    ns = np.linalg.svd(K)[2][2:].T
    dim_ann_prim = ns.shape[1]
    print(f"     q_j={qj}->{qj1}:  dim P={dimP}  dim C={dimC}  dim A={dimP-dimC}"
          f"  dim(ring∩P)={dim_ann_prim}  extra={dimP-dimC-dim_ann_prim}"
          f"  resid_nesting={resid:.1e}")
    check(resid < 1e-8, f"  q_j={qj}: isometric nesting, C subset P_{{tau_{{j+1}}}}")
    check(dimP - dimC - dim_ann_prim == 2,
          f"  q_j={qj}: dim A = dim(ring∩P) + 2  (the two Tate directions)")

print(f"\nVERDICT: {CHECKS} checks OK — R1 is verified.")
print("The jump q_j -> q_{j+1} is an exact step: the old core block receives no")
print("correction from the incoming contact, and the corona = (ring ∩ P) + 2 Tate modes.")
