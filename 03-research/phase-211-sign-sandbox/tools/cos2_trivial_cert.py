"""Certified trivial-bound range for the cos^2 profile (phase 211, ROUND_012_A, Theorem 2.1).

rho(u) = [pi(-u cos(pi u) - 2u + 2cos(pi u) + 4) + 3 sin(pi u)]/(6 pi) on [0,2], 0 beyond (exact autocorrelation of
cos^2(pi x/2) on [-1,1], normalised).  rho is nonincreasing on [0,2], so Sigma(T) = sum_{n<e^{2T}} v_n rho(log n/T) is
nondecreasing in T; m is increasing, so m(Omega_lo(T)) is nondecreasing.  On a grid T_0 < T_1 < ... it suffices to
check  Sigma(T_{j+1}) + kappa <= m(Omega_lo(T_j)).  Sigma is enclosed in interval arithmetic (mpmath.iv); m by mpmath
digamma at 50 digits (error << 1e-40).  Prints the worst slack per grid cell.
"""
import sys, math
from mpmath import mp, iv, mpf, digamma, log, pi as mpi
mp.dps = 50; iv.dps = 50
def m_lo(T, delta):
    tau = 2 * mpi * (1 + delta) * mp.e ** (2 * mpf(T)); return digamma(mpf(1) / 4 + 0.5j * tau).real - log(mpi)
def lam(n):
    for p in range(2, int(math.isqrt(n)) + 1):
        if n % p == 0:
            k = n
            while k % p == 0: k //= p
            return p if k == 1 else 0
    return n
def Sigma(T):
    T = iv.mpf(T); s = iv.mpf(0); n = 2
    while math.log(n) < 2 * float(T.b) + 1e-12:
        p = lam(n)
        if p:
            u = iv.log(n) / T
            if u.a < 2:
                r = (iv.pi * (-u * iv.cos(iv.pi * u) - 2 * u + 2 * iv.cos(iv.pi * u) + 4) + 3 * iv.sin(iv.pi * u)) / (6 * iv.pi)
                r = iv.mpf([max(mpf(0), r.a), max(mpf(0), r.b)]) if u.b >= 2 else r
                s += 2 * iv.log(p) / iv.sqrt(n) * r
        n += 1
    return s
if __name__ == '__main__':
    T0, T1, h, delta = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]) if len(sys.argv) > 4 else 0.1
    worst = None; T = T0
    while T < T1 - 1e-12:
        Tn = min(T + h, T1); sl = m_lo(T, delta) - Sigma(Tn).b
        worst = sl if worst is None or sl < worst else worst
        if sl <= 0: print("FAIL cell", T, Tn, float(sl)); break
        T = Tn
    print("T in [%g,%g], step %g, delta %g: min slack m(Omega_lo(T_j)) - Sigma(T_{j+1}) = %.6f" % (T0, T1, h, delta, float(worst)))
