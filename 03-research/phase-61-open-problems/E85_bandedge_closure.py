"""
CONSTRUCTIVE STEP TOWARD CLOSING 2.3.F-Loc (RH-neutral by R1: G_lambda >= 0 unconditional).

Thesis: the (k+1)^2 ladder is the BAND EDGE of the intrinsic PERIOD-2 Jacobi of G_lambda,
and depends ONLY on the AVERAGED (Cesaro) coefficients, not on their fluctuations. If, upon
smoothing the Lanczos coefficients, the ladder SURVIVES => Cesaro/PNT convergence suffices =>
2.3.F-Loc proved (unconditional), the arithmetic fluctuation is irrelevant by construction.

Three tests:
  (T1) exact Lanczos on A reproduces the (k+1)^2 ladder [N1 confirmation].
  (T2) SMOOTH the coefficients (separate parities, average) and recompute the spectrum:
       if the ratios still go ~ (k+1)^2 => the ladder lives in the AVERAGE.
  (T3) LIMIT period-2 Jacobi (alpha_even_inf, alpha_odd_inf, beta_inf bulk constants)
       on a finite chain with Dirichlet ends: band edge => (k+1)^2 ratios predicted
       from the AVERAGED symbol alone.
"""
import sys, numpy as np, mpmath as mp
from engine_cache import get_matrices

mp.mp.dps = 40


def lanczos(A, q0, m):
    n = A.rows
    Q = [q0 / mp.sqrt((q0.T * q0)[0])]
    alpha = []; beta = []; qprev = mp.zeros(n, 1); b = mp.mpf(0)
    for j in range(m):
        Aq = A * Q[j]
        a = (Q[j].T * Aq)[0]; alpha.append(a)
        r = Aq - a * Q[j] - (b * qprev if j > 0 else mp.zeros(n, 1))
        for qi in Q:
            r = r - (qi.T * r)[0] * qi
        b = mp.sqrt((r.T * r)[0])
        if b < mp.mpf(10) ** (-mp.mp.dps + 5) or j == m - 1:
            break
        beta.append(b); qprev = Q[j]; Q.append(r / b)
    return [float(x) for x in alpha], [float(x) for x in beta]


def jac_eigs(alpha, beta):
    m = len(alpha); T = mp.zeros(m)
    for i in range(m):
        T[i, i] = alpha[i]
        if i < len(beta):
            T[i, i + 1] = beta[i]; T[i + 1, i] = beta[i]
    E, _ = mp.eigsy(T)
    return sorted(float(E[i]) for i in range(m))


def ratios6(ev):
    """ABSOLUTE ratio ev_k/ev_0 (= (k+1)^2 only if ev_0 is the band bottom ~0)."""
    return [ev[k] / ev[0] for k in range(min(6, len(ev)))]


def shifted_ratios6(ev):
    """Doob SHIFTED ratio (ev_k-ev_0)/(ev_1-ev_0) -> k(k+2): the band-edge SHAPE,
    RH-neutral (R1), independent of where the band bottom lies. target [0,1,2.667,5,8,11.667]."""
    g = ev[1] - ev[0]
    return [(ev[k] - ev[0]) / g for k in range(min(6, len(ev)))]


def parity_smooth(seq):
    """separates even/odd subsequences, smooths them (running mean 3) and reinterleaves = Cesaro period-2."""
    s = np.array(seq, dtype=float)
    out = s.copy()
    for par in (0, 1):
        idx = np.arange(par, len(s), 2)
        sub = s[idx]
        if len(sub) >= 3:
            sm = sub.copy()
            for i in range(len(sub)):
                lo = max(0, i - 1); hi = min(len(sub), i + 2)
                sm[i] = np.mean(sub[lo:hi])
            out[idx] = sm
    return out.tolist()


def period2_limit_ladder(alpha, beta, M):
    """LIMIT period-2 Jacobi: bulk averages of the two parities, chain of length M, Dirichlet."""
    a = np.array(alpha); b = np.array(beta)
    # bulk: discard edges (first/last 2)
    ae = np.mean(a[2:-2:2]) if len(a) > 6 else np.mean(a[0::2])
    ao = np.mean(a[3:-2:2]) if len(a) > 6 else np.mean(a[1::2])
    bb = np.mean(b[2:-2]) if len(b) > 6 else np.mean(b)
    al = [ae if i % 2 == 0 else ao for i in range(M)]
    be = [bb for _ in range(M - 1)]
    ev = jac_eigs(al, be)
    return ratios6(ev), (ae, ao, bb)


def run(lam, N):
    Larch, Lpr, A, L, idx = get_matrices(lam, N, 'zeta', dps=40)
    n = A.rows
    q0 = mp.matrix([[mp.mpf(1) + mp.mpf('0.7') * (2 * i - (n - 1))] for i in range(n)])
    alpha, beta = lanczos(A, q0, n)
    print(f"\n{'='*72}\nlam={lam} N={N} (dim={n}, {len(alpha)} coef)")
    TGT = [0, 1, 2.667, 5, 8, 11.667]
    # uniform BOUNDEDNESS in lambda (critical link of RH-neutrality):
    maxA = max(abs(float(A[i, j])) for i in range(n) for j in range(n))
    print(f"  (B0) max|alpha|={max(abs(x) for x in alpha):.3f}  max|beta|={max(abs(x) for x in beta):.3f}  "
          f"max|A_ij|={maxA:.3f}  (must stay O(1), NOT grow with lambda)")
    ev = jac_eigs(alpha, beta)
    print(f"  shifted k(k+2) target:           [0, 1, 2.667, 5, 8, 11.667]")
    print(f"  (T1) exact Lanczos    SHIFT = {[round(r,3) for r in shifted_ratios6(ev)]}")
    # T2: period-2 Cesaro smoothing
    a_s = parity_smooth(alpha); b_s = parity_smooth(beta)
    ev_s = jac_eigs(a_s, b_s)
    sr = shifted_ratios6(ev_s)
    print(f"  (T2) SMOOTHED Jacobi   SHIFT = {[round(r,3) for r in sr]}  "
          f"=> {'SHAPE SURVIVES' if abs(sr[2]-2.667)<0.6 and abs(sr[3]-5)<1.2 else 'breaks'}")
    # T3: limit period-2 (band-edge shape from AVERAGED coefficients only)
    a = np.array(alpha); b = np.array(beta)
    ae = np.mean(a[2:-2:2]); ao = np.mean(a[3:-2:2]); bb = np.mean(b[2:-2])
    al = [ae if i % 2 == 0 else ao for i in range(n)]; be = [bb] * (n - 1)
    ev3 = jac_eigs(al, be); sr3 = shifted_ratios6(ev3)
    print(f"  (T3) LIMIT period-2    SHIFT = {[round(r,3) for r in sr3]}  "
          f"(a_even={ae:.3f} a_odd={ao:.3f} b={bb:.3f}) "
          f"=> {'band-edge SHAPE' if abs(sr3[2]-2.667)<0.7 else 'collapses'}")
    return shifted_ratios6(ev), sr, sr3


if __name__ == '__main__':
    lams = [(9.0, 16), (13.0, 18), (17.0, 20)]
    if len(sys.argv) > 1:
        lams = eval(sys.argv[1])
    print("E85 — the (k+1)^2 ladder as the BAND EDGE of the averaged Jacobi (Cesaro/PNT)")
    for lam, N in lams:
        run(lam, N)
