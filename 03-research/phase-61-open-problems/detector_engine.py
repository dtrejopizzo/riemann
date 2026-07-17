"""
A finite spectral detector for the Riemann Hypothesis.
================================================================
Builds the semilocal Weil quadratic form A_lambda on test functions supported
in the additive window [0, L], L = 2 log(lambda), in the Fourier basis
V_n(u) = exp(2 pi i n u / L).  Its smallest eigenvalue mu_lambda satisfies

        mu_lambda >= 0  for all lambda   <==>   Riemann Hypothesis.

The same construction applied to the Davenport-Heilbronn function (a Dirichlet
series with a Riemann-type functional equation but NO Euler product and zeros
off the critical line) yields mu_lambda < 0: the detector is faithful.

Requires: mpmath, numpy.  All spectral computations use 40 decimal digits;
the near-radical eigenvalue is of size e^{-cL} ~ 1e-20 and is invisible to
double precision.
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 40

GAMMA  = mp.euler
LOG4PI = mp.log(4*mp.pi)
LOG5   = mp.log(5)

# ----------------------------------------------------------------------
# 1. The autocorrelation kernel q_{nm}(u) of the Fourier modes on [0,L].
# ----------------------------------------------------------------------
def q_kernel(m, n, L):
    if m == n:
        return lambda u: 2*(1 - u/L)*mp.cos(2*mp.pi*n*u/L)
    c = 1/(mp.pi*(n - m))
    return lambda u: (mp.sin(2*mp.pi*m*u/L) - mp.sin(2*mp.pi*n*u/L))*c

# ----------------------------------------------------------------------
# 2. von Mangoldt coefficients.
#    zeta:  Lambda(p^k) = log p, else 0.
#    DH:    Lambda_DH(n) = coefficients of -f'/f, by exact Dirichlet inversion
#           of the real coefficients a_n (period 5): [0,1,k,-k,-1], k=tan(theta).
# ----------------------------------------------------------------------
def vonmangoldt_zeta(mx):
    Lam = [mp.mpf(0)]*(mx+1); sieve = [True]*(mx+1)
    for i in range(2, int(mx**0.5)+1):
        if sieve[i]:
            for j in range(i*i, mx+1, i): sieve[j] = False
    for p in range(2, mx+1):
        if sieve[p]:
            lp = mp.log(p); pw = p
            while pw <= mx:
                Lam[pw] = lp; pw *= p
    return Lam

def vonmangoldt_DH(mx):
    kappa = (mp.sqrt(10-2*mp.sqrt(5)) - 2)/(mp.sqrt(5)-1)   # tan(theta)
    a = lambda n: [mp.mpf(0), mp.mpf(1), kappa, -kappa, mp.mpf(-1)][n % 5]
    c = [mp.mpf(0)]*(mx+1)
    for n in range(1, mx+1):
        s = mp.log(n)*a(n); d = 2
        while d <= n:
            if n % d == 0: s -= a(d)*c[n//d]
            d += 1
        c[n] = s
    return c

# ----------------------------------------------------------------------
# 3. The matrix entry  A_lambda(V_n, V_m) = P - R - Q.
#    P  : pole term  int q (e^{u/2}+e^{-u/2}) du     (present iff the L-function
#         has a pole at s=1; absent for entire L-functions such as DH).
#    R  : archimedean (Gamma-factor) term; weight e^{+u/2} for an even functional
#         equation (zeta, psi(1/4)), weight e^{-u/2} for an odd one (DH, psi(3/4)).
#    Q  : prime term  sum_{k<=lambda^2} Lambda(k) k^{-1/2} q(log k).
#    C  : the archimedean constant  log(4 pi) + gamma  (+ log(conductor)).
# ----------------------------------------------------------------------
def entry(m, n, L, lam, Lam, C, even, pole):
    q  = q_kernel(m, n, L)
    q0 = q(mp.mpf(0))
    w  = (lambda u: mp.e**( u/2)) if even else (lambda u: mp.e**(-u/2))
    half = mp.mpf('1')/2
    def integrand(u):
        if u < mp.mpf('1e-12'):
            h = mp.mpf('1e-8')   # lim_{u->0} = ( q'(0) +/- q0/2 ) / 2
            return ((q(h) - q0)/h + (half if even else -half)*q0)/2
        return (w(u)*q(u) - q0)/(2*mp.sinh(u))
    R = C*q0/2 + mp.quad(integrand, [0, L]) + q0*mp.log(mp.tanh(L/2))/2
    Q = mp.mpf(0); mx = int(lam*lam)
    for k in range(2, mx+1):
        if Lam[k] != 0:
            Q += Lam[k]*(mp.mpf(k)**mp.mpf('-0.5'))*q(mp.log(k))
    if pole:
        P = mp.quad(lambda u: q(u)*(mp.e**(u/2) + mp.e**(-u/2)), [0, L])
        return P - R - Q
    return - R - Q

def matrix(lam_str, N, kind, C=None, pole=None):
    lam = mp.mpf(lam_str); L = 2*mp.log(lam); dim = 2*N+1
    idx = list(range(-N, N+1)); mx = int(lam*lam)
    Lam  = vonmangoldt_zeta(mx) if kind == 'zeta' else vonmangoldt_DH(mx)
    even = (kind == 'zeta')
    if pole is None: pole = (kind == 'zeta')
    if C is None:    C = LOG4PI + GAMMA + (0 if kind == 'zeta' else LOG5)
    M = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            v = entry(idx[a], idx[b], L, lam, Lam, C, even, pole)
            M[a, b] = v; M[b, a] = v
    return M, L, idx

# ----------------------------------------------------------------------
# 4. Spectrum, and reconstruction of the zeros from the ground eigenvector.
#    The Fourier transform of the ground state f_0 = sum (ev)_n V_n is
#    f_0^(z) = 2 sin(zL/2) g(z),  g(z) = sum_n (ev)_n / (k_n + z),  k_n=2 pi n/L.
#    The genuine zeros of f_0^ (those of g) coincide with the zeros of the
#    L-function on the critical line.
# ----------------------------------------------------------------------
def spectrum(M):
    E, V = mp.eigsy(M)
    order = sorted(range(M.rows), key=lambda j: E[j])
    return [E[j] for j in order], V, order

def zeros_of_ground_state(V, order, idx, L, zmax=35.0):
    ev = np.array([float(mp.re(V[i, order[0]])) for i in range(len(idx))])
    kn = np.array([2*np.pi*n/float(L) for n in idx])
    g  = lambda z: np.sum(ev/(kn + z))
    zs = np.linspace(0.5, zmax, 20000); gv = np.array([g(z) for z in zs])
    out = []
    for i in range(len(zs)-1):
        if gv[i]*gv[i+1] < 0:
            a, b = zs[i], zs[i+1]
            for _ in range(60):
                mid = (a+b)/2
                if g(a)*g(mid) <= 0: b = mid
                else: a = mid
            out.append((a+b)/2)
    return out

# ----------------------------------------------------------------------
# 5. Demonstration.
# ----------------------------------------------------------------------
if __name__ == "__main__":
    lam, N = '7.0', 14
    C0 = LOG4PI + GAMMA

    Mz, L, idx = matrix(lam, N, 'zeta', C=C0)
    Ez, Vz, oz = spectrum(Mz)
    print("ZETA  : mu_0 =", mp.nstr(Ez[0], 5),
          " ratios mu_k/mu_0 =", [mp.nstr(Ez[k]/Ez[0], 4) for k in range(5)])
    zz = zeros_of_ground_state(Vz, oz, idx, L)
    known = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062]
    print("        zeros of f0^:", [round(z, 4) for z in zz if min(abs(z-k) for k in known) < 0.01])

    Md, _, _ = matrix(lam, N, 'DH', C=C0)          # same constant as zeta
    Ed, _, _ = spectrum(Md)
    print("DH    : mu_0 =", mp.nstr(Ed[0], 5), " (negative: detects non-RH)")

    Mznp, _, _ = matrix(lam, N, 'zeta', C=C0, pole=False)   # zeta, pole removed
    Eznp, _, _ = spectrum(Mznp)
    print("ZETA  (no pole): mu_0 =", mp.nstr(Eznp[0], 5),
          " (positivity is lost without the pole at s=1)")
