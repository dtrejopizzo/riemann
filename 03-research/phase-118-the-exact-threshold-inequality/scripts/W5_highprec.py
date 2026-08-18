"""High-precision (mpmath) re-verification of the identity for the cases where
W5_identity_check.py's float64 pipeline shows a residual gap larger than the
target 8 significant digits.

Diagnosis (see W5_WEIL_IDENTITY.md): for the specific "null_vec" test
functions used there, gamma_term and 2*prime_sum are O(1e-2) numbers whose
difference (=LHS) shrinks to O(1e-8..1e-9) as T grows -- a real, large
cancellation intrinsic to those test functions (not a bug). float64 has only
~15-16 significant digits total, so once ~7-8 digits are eaten by
cancellation, only 7-8 digits of LHS survive: exactly the pattern observed
(relative error ~1e-5 to 1e-4 at T=2,3 vs ~1e-10 at T=0.6).

This script redoes the SAME computation -- same closed-form formulas, same
test functions, same cached zeros -- in mpmath at dps=40, where the
cancellation costs digits but 40 - 8 = 32 remain, more than enough for the
target 8 significant digits. If the gap does not shrink accordingly, that
would indicate a genuine formula error rather than float64 round-off.

run:  python3 W5_highprec.py
"""
import json
import math
import os
import time

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
mp.mp.dps = 40

EULER = mp.mpf('0.57721566490153286060651209008240243104215933593992')


def basis_coeffs_mp(T, kmax=3):
    base = [mp.mpf(1), mp.mpf(0), mp.mpf(-3), mp.mpf(0), mp.mpf(3), mp.mpf(0), mp.mpf(-1)]
    out = []
    for k in range(kmax + 1):
        c_x = [mp.mpf(0)] * k + list(base)
        c_t = [c_x[n] / T ** n for n in range(len(c_x))]
        out.append(c_t)
    maxlen = max(len(c) for c in out)
    return [c + [mp.mpf(0)] * (maxlen - len(c)) for c in out]


def poly_integral_power_rule_mp(coeffs, lo, hi):
    tot = mp.mpf(0)
    for k, ck in enumerate(coeffs):
        if ck == 0:
            continue
        tot += ck * (hi ** (k + 1) - lo ** (k + 1)) / (k + 1)
    return tot


def real_moment_integral_mp(coeffs, T, c):
    n = len(coeffs)
    if c == 0:
        return poly_integral_power_rule_mp(coeffs, -T, T)
    eT, emT = mp.e ** (c * T), mp.e ** (-c * T)
    J = (eT - emT) / c
    tot = coeffs[0] * J
    Tk = mp.mpf(1)
    for k in range(1, n):
        Tk *= T
        bterm = (Tk * eT - ((-1) ** k) * Tk * emT) / c
        J = bterm - (k / c) * J
        tot += coeffs[k] * J
    return tot


def moments_at_origin_mp(coeffs, T, jmax):
    out = []
    for j in range(jmax + 1):
        shifted = [mp.mpf(0)] * j + list(coeffs)
        out.append(poly_integral_power_rule_mp(shifted, -T, T))
    return out


def fourier_moment_integral_mp(coeffs, T, tau, small_tau_thresh=2.0, taylor_terms=50):
    """Single complex tau (mpmath mpf/mpc), returns mpc.

    Same catastrophic-cancellation issue as the float64 version's naive
    recursion (division by i*tau at every one of ~deg(P) steps) -- ONLY
    worse here because mp.quad's tanh-sinh substitution probes tau as small
    as ~1e-30 near the t=0 endpoint of the outer [0,5] segment; the
    recursion's cancellation there overwhelmed even 40 mpmath digits and
    produced a ~1e566 garbage value (caught by comparing segment-by-segment
    quad output against direct pointwise evaluation, which looked fine).
    Fixed the same way: Taylor series in tau using the origin moments for
    |tau| < small_tau_thresh."""
    if tau == 0:
        return mp.mpc(poly_integral_power_rule_mp(coeffs, -T, T))
    if abs(tau) < small_tau_thresh:
        mu = moments_at_origin_mp(coeffs, T, taylor_terms)
        fact = mp.mpf(1)
        acc = mp.mpc(0)
        power = mp.mpc(1)
        for j in range(taylor_terms + 1):
            if j > 0:
                fact *= j
                power *= 1j * tau
            acc += (power / fact) * mu[j]
        return acc
    n = len(coeffs)
    ic = 1j * tau
    eT, emT = mp.e ** (ic * T), mp.e ** (-ic * T)
    J = (eT - emT) / ic
    tot = coeffs[0] * J
    Tk = mp.mpf(1)
    for k in range(1, n):
        Tk *= T
        bterm = (Tk * eT - ((-1) ** k) * Tk * emT) / ic
        J = bterm - (k / ic) * J
        tot += coeffs[k] * J
    return tot


def shift_poly_mp(coeffs, a):
    n = len(coeffs)
    out = [mp.mpf(0)] * n
    for k in range(n):
        ck = coeffs[k]
        if ck == 0:
            continue
        for j in range(k + 1):
            out[j] += ck * mp.binomial(k, j) * a ** (k - j)
    return out


def polymul_mp(a, b):
    out = [mp.mpf(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            if bj == 0:
                continue
            out[i + j] += ai * bj
    return out


def autocorr_mp(coeffs, T, a):
    a = abs(a)
    if a >= 2 * T:
        return mp.mpf(0)
    shifted = shift_poly_mp(coeffs, a)
    prod = polymul_mp(coeffs, shifted)
    lo, hi = -T, T - a
    if hi <= lo:
        return mp.mpf(0)
    return poly_integral_power_rule_mp(prod, lo, hi)


def phi_gamma_mp(tau):
    return mp.re(mp.digamma(mp.mpf('0.25') + 1j * mp.mpf(tau) / 2)) - mp.log(mp.pi)


def von_mangoldt_upto(N):
    lam = [0.0] * (N + 1)
    sieve = [True] * (N + 1)
    for p in range(2, N + 1):
        if sieve[p]:
            for m in range(p * p, N + 1, p):
                sieve[m] = False
            q, lp = p, math.log(p)
            while q <= N:
                lam[q] = lp
                q *= p
    return lam


def prime_power_terms(T):
    Nmax = int(math.floor(math.exp(2 * float(T))))
    lam = von_mangoldt_upto(max(Nmax, 2))
    out = []
    for n in range(2, Nmax + 1):
        if lam[n] > 0 and n < math.exp(2 * float(T)) - 1e-9:
            out.append((n, mp.mpf(lam[n]) / mp.sqrt(n)))
    return out


def _row_reduce_2xN(row0, row1):
    """Gauss-Jordan on a 2 x nb matrix with partial pivoting (mpmath mpf).
    Returns (pivot_cols, free_cols, R) with R the reduced 2 x nb matrix."""
    nb = len(row0)
    R = [list(row0), list(row1)]
    pivots = []
    r = 0
    for c in range(nb):
        # find pivot in column c among rows r..1
        best = max(range(r, 2), key=lambda i: abs(R[i][c])) if r < 2 else None
        if best is None or abs(R[best][c]) < mp.mpf('1e-20'):
            continue
        R[r], R[best] = R[best], R[r]
        piv = R[r][c]
        R[r] = [x / piv for x in R[r]]
        for i in range(2):
            if i != r:
                f = R[i][c]
                R[i] = [R[i][j] - f * R[r][j] for j in range(nb)]
        pivots.append(c)
        r += 1
        if r == 2:
            break
    free = [c for c in range(nb) if c not in pivots]
    return pivots, free, R


def null_basis_2xN(row0, row1):
    """Basis of the null space of the 2 x nb matrix [row0;row1] (nb-2 vectors,
    normalized to unit L2 norm and Gram-Schmidt orthogonalized -- purely for
    readability of the printed coefficients, any basis works)."""
    nb = len(row0)
    pivots, free, R = _row_reduce_2xN(row0, row1)
    basis = []
    for fc in free:
        v = [mp.mpf(0)] * nb
        v[fc] = mp.mpf(1)
        for i, pc in enumerate(pivots):
            v[pc] = -R[i][fc]
        basis.append(v)
    # Gram-Schmidt orthonormalize
    ortho = []
    for v in basis:
        w = list(v)
        for u in ortho:
            proj = sum(w[i] * u[i] for i in range(nb))
            w = [w[i] - proj * u[i] for i in range(nb)]
        norm = mp.sqrt(sum(x * x for x in w))
        ortho.append([x / norm for x in w])
    return ortho


def null_vec(T, kmax, which):
    """Primitive test functions: coefficients in the null space of the Tate
    moment map, built via exact (mpmath) Gauss-Jordan elimination -- an
    independent linear-algebra path from W5_identity_check.py's numpy SVD.
    The resulting functions need not be numerically identical to the
    float64 script's, only primitive; `which` selects among the null_dim
    orthonormal basis vectors returned."""
    basis = basis_coeffs_mp(T, kmax)
    nb = len(basis)
    Mm = [real_moment_integral_mp(b, T, mp.mpf('-0.5')) for b in basis]
    Mp = [real_moment_integral_mp(b, T, mp.mpf('0.5')) for b in basis]
    null_vecs = null_basis_2xN(Mm, Mp)
    vec = null_vecs[which]
    coeffs = [mp.mpf(0)] * len(basis[0])
    for j in range(nb):
        for i in range(len(basis[0])):
            coeffs[i] += vec[j] * basis[j][i]
    return coeffs, vec, Mm, Mp


def lhs_mp(coeffs, T, tau_cutoff=600.0, verbose=False):
    def integrand(tau):
        phi = phi_gamma_mp(tau)
        z = fourier_moment_integral_mp(coeffs, T, mp.mpf(tau))
        return phi * (mp.fabs(z) ** 2)

    gamma_part = mp.quad(integrand, [0, 5, 20, 50, 150, tau_cutoff])
    gamma_term = gamma_part / mp.pi

    terms = prime_power_terms(T)
    prime_sum = mp.mpf(0)
    for n, w in terms:
        g = autocorr_mp(coeffs, T, mp.log(n))
        prime_sum += w * g
    lhs = gamma_term - 2 * prime_sum
    if verbose:
        print("    gamma_term=%s" % mp.nstr(gamma_term, 20))
        print("    2*prime_sum=%s" % mp.nstr(2 * prime_sum, 20))
    return lhs, gamma_term, prime_sum


def load_zeros():
    with open(os.path.join(HERE, "W5_zeros_cache.json")) as f:
        d = json.load(f)
    return [mp.mpf(g) for g in d["gammas"]], d["dps"]


def rhs_mp(coeffs, T, gammas, kmax_zeros=200):
    tot = mp.mpf(0)
    partials = []
    for i, g in enumerate(gammas[:kmax_zeros], start=1):
        z = fourier_moment_integral_mp(coeffs, T, g)
        tot += 2 * (mp.fabs(z) ** 2)
        if i in (10, 20, 40, 80, 120, 160, 200) or i == kmax_zeros:
            partials.append((i, tot))
    return tot, partials


def main():
    gammas, dps_cache = load_zeros()
    print("cached zeros: %d at dps=%s\n" % (len(gammas), dps_cache))

    cases = [(0.6, 0), (1.2, 0), (1.2, 1), (2.0, 0), (2.0, 1), (3.0, 0), (3.0, 1)]
    for T, which in cases:
        T_mp = mp.mpf(T)
        coeffs, vec, Mm, Mp = null_vec(T_mp, 3, which)
        mm_val = sum(vec[j] * Mm[j] for j in range(len(vec)))
        mp_val = sum(vec[j] * Mp[j] for j in range(len(vec)))
        print("=" * 70)
        print("T=%s  null_vec_%d   M-=%s  M+=%s" %
              (T, which, mp.nstr(mm_val, 5), mp.nstr(mp_val, 5)))
        t0 = time.time()
        L, gt, ps = lhs_mp(coeffs, T_mp, verbose=True)
        t1 = time.time()
        R, partials = rhs_mp(coeffs, T_mp, gammas, kmax_zeros=min(200, len(gammas)))
        for k, s in partials:
            print("    RHS k=%3d  %s" % (k, mp.nstr(s, 18)))
        diff = L - R
        rel = diff / abs(L) if L != 0 else mp.mpf('nan')
        print("  LHS       = %s" % mp.nstr(L, 18))
        print("  RHS(%3d)  = %s" % (min(200, len(gammas)), mp.nstr(R, 18)))
        print("  LHS-RHS   = %s   relative = %s   (lhs_time=%.1fs)" %
              (mp.nstr(diff, 6), mp.nstr(rel, 6), t1 - t0))
        print()


if __name__ == "__main__":
    main()
