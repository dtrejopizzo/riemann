#!/usr/bin/env python3
"""Numerical checks for "The localized Weil form on a Hermite-Gauss basis".

Requires numpy, scipy, mpmath.  Run:  python3 numerics.py [output_dir]
Writes plain-text tables to output_dir (default: results/ next to this file).

Notation as in the paper:
  psi_j        L^2-normalised Hermite functions,
  phi_j(t)   = sigma^{-1/2} psi_j((t-T0)/sigma),      Phi = (phi_0..phi_{J-1})^T,
  F(z)       = Phi(z) Phi(z)^T,
  P(gamma,d) = F(gamma-i d) + F(gamma+i d) - 2 F(gamma),
  A(gamma)   = -F''(gamma),   a(gamma) = -lambda_min(A(gamma)),
  g(u)       = (1/2pi) e^{-i T0 u} K(sigma u),  K_jk(w) = int psi_j psi_k e^{-iwx} dx.
"""
import os
import sys
import math
import numpy as np
import mpmath as mp
from scipy import special

mp.mp.dps = 50
C0 = 1.03883  # Rosser-Schoenfeld: psi(x) < 1.03883 x for x > 0


# ---------------------------------------------------------------- Hermite side
def psi_list(x, n):
    """psi_0(x),...,psi_{n-1}(x) for real or complex mp number x."""
    out = [mp.pi ** (-mp.mpf(1) / 4) * mp.exp(-x * x / 2)]
    if n > 1:
        out.append(mp.sqrt(2) * x * out[0])
    for j in range(1, n - 1):
        out.append(mp.sqrt(mp.mpf(2) / (j + 1)) * x * out[j]
                   - mp.sqrt(mp.mpf(j) / (j + 1)) * out[j - 1])
    return out


def Phi_derivs(z, T0, sigma, J, order):
    """List [Phi, Phi', ..., Phi^(order)] at z (each an mp column vector)."""
    x = (z - T0) / sigma
    vals = psi_list(x, J + order)
    cur = vals
    res = []
    for k in range(order + 1):
        res.append(mp.matrix([cur[j] * sigma ** (-mp.mpf(1) / 2 - k) for j in range(J)]))
        # psi_j' = sqrt(j/2) psi_{j-1} - sqrt((j+1)/2) psi_{j+1}
        nxt = []
        for j in range(len(cur) - 1):
            lo = mp.sqrt(mp.mpf(j) / 2) * cur[j - 1] if j > 0 else 0
            nxt.append(lo - mp.sqrt(mp.mpf(j + 1) / 2) * cur[j + 1])
        cur = nxt
    return res


def F_deriv(z, T0, sigma, J, n):
    """n-th derivative of F = Phi Phi^T at z."""
    d = Phi_derivs(z, T0, sigma, J, n)
    M = mp.zeros(J, J)
    for k in range(n + 1):
        M += mp.binomial(n, k) * d[k] * d[n - k].T
    return M


def P_matrix(gamma, delta, T0, sigma, J):
    f = lambda z: (lambda v: v * v.T)(Phi_derivs(z, T0, sigma, J, 0)[0])
    M = f(mp.mpc(gamma, -delta)) + f(mp.mpc(gamma, delta)) - 2 * f(mp.mpf(gamma))
    return M.apply(mp.re)


def A_matrix(gamma, T0, sigma, J):
    return -F_deriv(mp.mpf(gamma), T0, sigma, J, 2).apply(mp.re)


def eigs(M):
    E = mp.eigsy(M, eigvals_only=True)
    return sorted([E[i] for i in range(len(E))])


def opnorm(M):
    Mr = np.array([[complex(M[i, j]) for j in range(M.cols)] for i in range(M.rows)])
    return float(np.linalg.norm(Mr, 2))


def C_const(gamma, delta0, T0, sigma, J, nsamp=9):
    """(1/12) max_{|s|<=delta0} ||F''''(gamma+is)||_op, sampled."""
    best = 0.0
    for s in np.linspace(0.0, float(delta0), nsamp):
        best = max(best, opnorm(F_deriv(mp.mpc(gamma, s), T0, sigma, J, 4)))
    return best / 12.0


# ----------------------------------------------------------------- prime side
def K_entry(j, k, w):
    """K_jk(w) for numpy array w (exact closed form, j,k >= 0)."""
    if j < k:
        j, k = k, j
    d = j - k
    pref = math.exp(0.5 * (math.lgamma(k + 1) - math.lgamma(j + 1)))
    return (pref * (-1j * w / math.sqrt(2)) ** d * np.exp(-w * w / 4)
            * special.eval_genlaguerre(k, d, w * w / 2))


def p_poly(j, k):
    """Coefficients (ascending, numpy poly1d-free) of p_jk(w) =
    sqrt(k!/j!) (w/sqrt2)^{j-k} L_k^{(j-k)}(-w^2/2), j >= k; non-negative."""
    if j < k:
        j, k = k, j
    d = j - k
    pref = math.exp(0.5 * (math.lgamma(k + 1) - math.lgamma(j + 1)))
    c = np.zeros(j + k + 1)
    for i in range(k + 1):
        c[d + 2 * i] = pref * 2.0 ** (-d / 2.0) * special.comb(k + d, k - i) / math.factorial(i) / 2.0 ** i
    return c


def P_poly(sigma, J):
    """Ascending coefficients in u of P(u) = (1/2pi) sum_{j,k} p_jk(sigma u)."""
    c = np.zeros(2 * J - 1)
    for j in range(J):
        for k in range(J):
            pc = p_poly(j, k)
            c[:len(pc)] += pc * sigma ** np.arange(len(pc))
    return c / (2 * math.pi)


def majorant(sigma, J):
    """Return callables G(u), |G'(u)| for G = P(u) exp(-sigma^2 u^2/4)."""
    c = P_poly(sigma, J)
    dc = c[1:] * np.arange(1, len(c))
    Pf = lambda u: np.polynomial.polynomial.polyval(u, c)
    dPf = lambda u: np.polynomial.polynomial.polyval(u, dc)
    G = lambda u: Pf(u) * np.exp(-sigma ** 2 * u ** 2 / 4)
    absdG = lambda u: np.abs(dPf(u) - sigma ** 2 * u / 2 * Pf(u)) * np.exp(-sigma ** 2 * u ** 2 / 4)
    return G, absdG


def tail_bound(L, sigma, J, alpha=None):
    """2 c0 int_L^inf e^{u/2}(G/2+|G'|) [e^{alpha u^2}] du  (mp quadrature)."""
    c = [mp.mpf(float(v)) for v in P_poly(sigma, J)]
    dc = [c[i] * i for i in range(1, len(c))]
    s2 = mp.mpf(sigma) ** 2
    al = mp.mpf(0) if alpha is None else mp.mpf(alpha)

    def f(u):
        Pu = mp.polyval(c[::-1], u)
        dPu = mp.polyval(dc[::-1], u)
        return mp.exp(u / 2 - s2 * u * u / 4 + al * u * u) * (Pu / 2 + abs(dPu - s2 * u / 2 * Pu))

    L = mp.mpf(L)
    step = 3 / mp.sqrt(s2 / 4 - al)
    pts = [L + k * step for k in range(0, 15)]
    return 2 * C0 * mp.quad(f, pts)


def von_mangoldt_support(N):
    """Arrays (n, Lambda(n)) of prime powers n <= N."""
    sieve = np.ones(N + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(N ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    primes = np.nonzero(sieve)[0]
    ns = [primes.astype(np.float64)]
    ls = [np.log(primes)]
    for p in primes[primes <= int(N ** 0.5) + 1]:
        q = p * p
        while q <= N:
            ns.append(np.array([float(q)]))
            ls.append(np.array([math.log(p)]))
            q *= p
    n = np.concatenate(ns)
    lam = np.concatenate(ls)
    o = np.argsort(n)
    return n[o], lam[o]


def prime_matrices_cumulative(T0, sigma, J, n, lam, cuts):
    """S(X) = sum_{n<=X} Lambda(n) n^{-1/2} (g(log n)+g(-log n)) for X in cuts
    and for X = max(n) (last entry)."""
    u = np.log(n)
    w = sigma * u
    base = lam / np.sqrt(n) / (2 * math.pi)
    ph = np.exp(-1j * T0 * u)
    idx = [np.searchsorted(n, X, side='right') for X in cuts] + [len(n)]
    out = [np.zeros((J, J)) for _ in idx]
    for j in range(J):
        for k in range(j + 1):
            t = 2 * np.real(ph * K_entry(j, k, w)) * base
            cs = np.concatenate([[0.0], np.cumsum(t)])
            for m, i in enumerate(idx):
                out[m][j, k] = out[m][k, j] = cs[i]
    return out


# ------------------------------------------------------------------- sections
def check_kernel(out):
    out.write("# Closed form of K_jk(w) = int psi_j psi_k e^{-iwx} dx against quadrature\n")
    worst = 0.0
    for (j, k) in [(0, 0), (2, 1), (5, 2), (9, 4)]:
        for w in [0.3, 1.7, 4.0]:
            q = mp.quad(lambda x: psi_list(x, j + 1)[j] * psi_list(x, k + 1)[k] * mp.exp(-1j * w * x),
                        mp.linspace(-14, 14, 15))
            c = complex(K_entry(j, k, np.array([w]))[0])
            worst = max(worst, abs(complex(q) - c))
            pj = np.polynomial.polynomial.polyval(w, p_poly(j, k)) * math.exp(-w * w / 4)
            assert abs(c) <= pj * (1 + 1e-12)
    out.write("max |closed form - quadrature| over samples: %.2e\n" % worst)
    out.write("majorant |K_jk(w)| <= p_jk(w) e^{-w^2/4} holds at all samples\n\n")


def check_lemma(out):
    T0, sigma, J, gamma = mp.mpf('46.13'), mp.mpf(1), 8, mp.mpf('46.6')
    A = A_matrix(gamma, T0, sigma, J)
    ev = eigs(A)
    out.write("# Lemma 3.1: spectrum of A(gamma), J=8, sigma=1, T0=46.13, gamma=46.6\n")
    out.write("eigenvalues: " + ", ".join(mp.nstr(e, 6) for e in ev) + "\n")
    d = Phi_derivs(gamma, T0, sigma, J, 1)
    ph, dph = d[0], d[1]
    n2 = lambda v: sum(v[i] ** 2 for i in range(len(v)))
    dot = sum(ph[i] * dph[i] for i in range(J))
    lb = 2 * (n2(dph) - dot ** 2 / n2(ph))
    out.write("a(gamma) = %s ; lower bound 2(|Phi'|^2-(Phi.Phi')^2/|Phi|^2) = %s\n"
              % (mp.nstr(-ev[0], 8), mp.nstr(lb, 8)))
    out.write("rank (eigenvalues above 1e-30 in modulus): %d\n" % sum(1 for e in ev if abs(e) > mp.mpf(10) ** -30))
    out.write("\n# Remark 3.3: a_J(gamma) at gamma-T0=0.47, sigma=1\n")
    for JJ in [2, 3, 4, 6, 8, 10, 12, 16, 20]:
        out.write("J=%2d  a=%s\n" % (JJ, mp.nstr(-eigs(A_matrix(gamma, T0, sigma, JJ))[0], 8)))
    out.write("\n")


def check_expansion(out):
    out.write("# Proposition 3.4: lambda_min(P)/delta^2 against -a(gamma);  gamma = T0+0.47 sigma\n")
    out.write("# rel = |lambda_min(P)+a delta^2|/(a delta^2);  bound = C delta^2/a with C=(1/12)max||F''''||\n")
    out.write("%6s %5s %3s %9s %13s %11s %11s\n" % ("T0", "sigma", "J", "delta", "a(gamma)", "rel", "bound"))
    worst = {}
    ok = True
    for T0s in ['46.13']:
        for sig in ['0.5', '1', '2', '4']:
            for J in [4, 8, 12, 16, 20]:
                T0, sigma = mp.mpf(T0s), mp.mpf(sig)
                gamma = T0 + mp.mpf('0.47') * sigma
                a = -eigs(A_matrix(gamma, T0, sigma, J))[0]
                for dl in ['1e-2', '1e-3', '1e-4', '1e-5']:
                    delta = mp.mpf(dl) * sigma
                    lm = eigs(P_matrix(gamma, delta, T0, sigma, J))[0]
                    rel = abs(lm + a * delta ** 2) / (a * delta ** 2)
                    C = C_const(gamma, delta, T0, sigma, J, nsamp=3)
                    bnd = C * float(delta) ** 2 / float(a)
                    ok = ok and (float(rel) <= bnd * (1 + 1e-9))
                    worst[dl] = max(worst.get(dl, 0.0), float(rel))
                    out.write("%6s %5s %3d %9s %13s %11.3e %11.3e\n"
                              % (T0s, sig, J, mp.nstr(delta, 3), mp.nstr(a, 8), float(rel), bnd))
    out.write("# largest rel per delta/sigma: " + ", ".join("%s: %.3e" % kv for kv in worst.items()) + "\n")
    out.write("# inequality |lambda_min(P)+a delta^2| <= C delta^4 satisfied in all rows: %s\n\n" % ok)

    out.write("# Theorem 3.2(iii): m pairs, sigma=1, T0=46.13, J=8, delta=1e-3\n")
    T0, sigma, J, delta = mp.mpf('46.13'), mp.mpf(1), 8, mp.mpf('1e-3')
    for gam in [['46.6'], ['45.2', '46.6', '47.9'], ['44.1', '45.2', '45.9', '46.6', '47.9']]:
        S = mp.zeros(J, J)
        Pm = mp.zeros(J, J)
        for g in gam:
            S += A_matrix(mp.mpf(g), T0, sigma, J)
            Pm += P_matrix(mp.mpf(g), delta, T0, sigma, J)
        out.write("m=%d  lambda_min(sum A)=%s  lambda_min(P)/delta^2=%s\n"
                  % (len(gam), mp.nstr(eigs(S)[0], 10), mp.nstr(eigs(Pm)[0] / delta ** 2, 10)))
    out.write("\n")


def check_explicit_formula(out, n, lam):
    T0, sigma, J = 46.13, 1.0, 6
    # zero side
    Mz = mp.zeros(J, J)
    for i in range(1, 31):
        g = mp.im(mp.zetazero(i))
        v = Phi_derivs(g, mp.mpf(T0), mp.mpf(sigma), J, 0)[0]
        Mz += v * v.T
    Mz = np.array([[float(Mz[i, j]) for j in range(J)] for i in range(J)])
    # archimedean side: (1/2pi) int phi_j phi_k Omega, trapezoid rule
    r = np.linspace(T0 - 14 * sigma, T0 + 14 * sigma, 5601)
    hstep = r[1] - r[0]
    x = (r - T0) / sigma
    ps = [np.pi ** -0.25 * np.exp(-x * x / 2)]
    ps.append(np.sqrt(2) * x * ps[0])
    for j in range(1, J - 1):
        ps.append(np.sqrt(2.0 / (j + 1)) * x * ps[j] - np.sqrt(j / (j + 1.0)) * ps[j - 1])
    Om = np.real(special.digamma(0.25 + 0.5j * r)) - math.log(math.pi)
    Ma = np.array([[np.sum(ps[j] * ps[k] * Om) * hstep / sigma / (2 * math.pi) for k in range(J)] for j in range(J)])
    S = prime_matrices_cumulative(T0, sigma, J, n, lam, [])[-1]
    Marith = Ma - S  # polar term is below 1e-900 here
    D = Mz - Marith
    out.write("# Remark 2.1: explicit formula on the basis, T0=46.13, sigma=1, J=6\n")
    out.write("# zeros: first 30 ordinates; prime powers up to %d; polar term negligible\n" % int(n[-1]))
    out.write("||M_zeros||_op = %.6f   ||M_arch||_op = %.6f   ||prime sum||_op = %.6f\n"
              % (np.linalg.norm(Mz, 2), np.linalg.norm(Ma, 2), np.linalg.norm(S, 2)))
    out.write("||M_zeros - M_arith||_op = %.3e   |tr difference| = %.3e\n" % (np.linalg.norm(D, 2), abs(np.trace(D))))
    out.write("lambda_min(M_zeros) = %.6e\n\n" % np.linalg.eigvalsh(Mz)[0])


def check_tail(out, n, lam):
    out.write("# Theorem 4.2 / Proposition 4.3: eta(X)=||E_X||_op for zeta against the bound\n")
    out.write("# bound(X) = 2 c0 int_L^inf e^{u/2}(G/2+|G'|) du,  rate = -log(bound)/L^2\n")
    for (T0, sigma, J) in [(46.13, 1.0, 8), (46.13, 1.0, 10), (85.7, 2.0, 10)]:
        cuts = [10.0 ** e for e in ([2, 3, 4, 5, 6] if sigma == 1.0 else [0.5, 1, 1.5, 2, 2.5])]
        S = prime_matrices_cumulative(T0, sigma, J, n, lam, cuts)
        out.write("T0=%g sigma=%g J=%d   (sigma^2/4 = %g)\n" % (T0, sigma, J, sigma ** 2 / 4))
        out.write("%10s %8s %12s %12s %8s\n" % ("X", "L", "eta(X)", "bound(X)", "rate"))
        for X, SX in zip(cuts, S[:-1]):
            eta = np.linalg.norm(S[-1] - SX, 2)
            L = math.log(X)
            b = tail_bound(L, sigma, J)
            out.write("%10.4g %8.3f %12.4e %12.4e %8.4f\n" % (X, L, eta, float(b), float(-mp.log(b)) / L ** 2))
        out.write("\n")
    out.write("# rate of the bound at large L, sigma=1, J=8\n")
    for L in [10, 20, 40, 80, 160]:
        b = tail_bound(L, 1.0, 8)
        out.write("L=%4d  -log(bound)/L^2 = %.4f\n" % (L, float(-mp.log(b)) / L ** 2))
    out.write("\n")


def table_xmin(out):
    kappa = 0.5
    out.write("# Table 1: cutoffs from Theorem 5.1, kappa=1/2, gamma=T0+0.47 sigma, alpha=sigma^2/5\n")
    out.write("# X_int: least X with bound(X) <= kappa a delta^2;  X_min: formula (9) with A_tr(alpha)\n")
    out.write("%6s %5s %3s %7s %11s %11s %11s %11s %11s\n"
              % ("T0", "sigma", "J", "delta", "a(gamma)", "C", "A_tr", "X_int", "X_min"))
    for (T0, sigma, J, dl) in [(46.13, 1.0, 10, 1e-3), (46.13, 1.0, 10, 1e-4), (46.13, 1.0, 10, 1e-5),
                               (85.7, 2.0, 10, 1e-5)]:
        gamma = mp.mpf(str(T0)) + mp.mpf('0.47') * sigma
        a = float(-eigs(A_matrix(gamma, mp.mpf(str(T0)), mp.mpf(sigma), J))[0])
        C = C_const(gamma, dl, mp.mpf(str(T0)), mp.mpf(sigma), J, nsamp=3)
        assert C * dl ** 2 <= 0.5 * (1 - kappa) * a
        target = kappa * a * dl ** 2
        alpha = sigma ** 2 / 5
        Atr = float(tail_bound(0, sigma, J, alpha=alpha))
        Xmin = math.exp(math.sqrt(max(0.0, math.log(Atr / target)) / alpha))
        lo, hi = 0.0, 60.0
        for _ in range(30):
            mid = (lo + hi) / 2
            if tail_bound(mid, sigma, J) <= target:
                hi = mid
            else:
                lo = mid
        out.write("%6g %5g %3d %7.0e %11.5f %11.4e %11.4e %11.4e %11.4e\n"
                  % (T0, sigma, J, dl, a, C, Atr, math.exp(hi), Xmin))
    out.write("\n")


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "zero_side.txt"), "w") as out:
        check_lemma(out)
        check_expansion(out)
    mp.mp.dps = 20
    n, lam = von_mangoldt_support(20_000_000)
    with open(os.path.join(outdir, "prime_side.txt"), "w") as out:
        check_kernel(out)
        check_explicit_formula(out, n, lam)
        check_tail(out, n, lam)
        table_xmin(out)


if __name__ == "__main__":
    main()
