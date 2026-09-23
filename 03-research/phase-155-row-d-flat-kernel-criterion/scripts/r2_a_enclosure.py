"""Phase 155 round 2, task (a): rigorous interval enclosure of a beta-uniform
NEGATIVE test-kernel ceiling at T = (1/2)log 3.

For a single explicit pair (tau0, q) Theorem TK (Paper 47 Prop. 8.4) gives, for every
certificate (nu,beta) of value c on the lattice of step d = 2T/M,

    c  <=  Q(tau0,q,beta) = a + b0*beta0 + b1*beta1,
    a  = (P||q||^2)^{-1} int_W sigma_T phi,   b_j = (P||q||^2)^{-1} int_W ghat_j phi,

with W = [tau0, tau0+P], P = 2pi/d, phi(tau) = |sum_k q_k e^{i k d tau}|^2 >= 0, and
int_W phi = P ||q||^2 exactly.  Combined with the a priori bound ||beta||_inf <= B of
task (c) this yields the unconditional bound  c <= a + (|b0|+|b1|) B.

Everything below is enclosed in mpmath interval arithmetic:
  * m(tau) = C0 + sum_{k<K} t_k(tau) + R,  t_k = tau^2/(a_k(tau^2+4a_k^2)), a_k = k+1/4,
    C0 = -gamma - pi/2 - 3 log 2 - log pi  (Gauss digamma at 1/4),
    R = sum_{k>=K} t_k in [ L - E, L ],  L = (1/2) log(1+tau^2/(4A^2)),  A = K - 1/4,
    E = (1/24) |t'(A)| = (1/24) tau^2 (tau^2+12A^2) / (tau^2 A + 4A^3)^2
    (t is positive, decreasing and convex in a, so the midpoint sum underestimates the
     integral by at most (1/24) int |t''| = (1/24)|t'(A)|).
  * composite Simpson with n subintervals and the rigorous remainder
    |E_simpson| <= P h^4 C4 / 180,  h = P/n,  C4 an explicit bound on the 4th derivative
    of the integrand (|m^{(j)}| <= 2^{-j} j! zeta(j+1,1/4); Bernstein for phi).

Usage:  python3 r2_a_enclosure.py [M]        (default M = 8; each run < 60 s)
"""
import sys, json, time
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import numpy as np
from mpmath import iv, mp, mpf
from scipy.linalg import toeplitz
import tk_common as tk
from scipy.optimize import minimize

iv.dps = 25
mp.dps = 30

Tf = 0.5 * np.log(3.0)


# ---------------------------------------------------------------- double precision search
def find_pair(M, n=1 << 17):
    """Double-precision search for tau0 and the minimising q at the beta that maximises
    lambda_min(C_M(tau0,.)) -- purely heuristic; the certificate is verified afterwards."""
    parts = tk.make_S_parts(Tf)[:3]
    P = np.pi * M / Tf
    grid = np.linspace(-2.2 * P, 0.2 * P, 161)
    CS = [tk.coeff_families(Tf, M, t, 1 << 14, parts) for t in grid]
    ceil_b = lambda b: min(tk.lam_min(c, b)[0] for c in CS)
    r = minimize(lambda b: -ceil_b(b), [2.4, -1.3], method='Nelder-Mead',
                 options={'xatol': 1e-10, 'fatol': 1e-14, 'maxiter': 4000})
    vals = [tk.lam_min(c, r.x)[0] for c in CS]
    t0 = round(float(grid[int(np.argmin(vals))]), 3)
    Ms = [toeplitz(np.conj(c), c) for c in tk.coeff_families(Tf, M, t0, n, parts)]
    r2 = minimize(lambda b: -np.linalg.eigvalsh(Ms[0] + b[0] * Ms[1] + b[1] * Ms[2])[0],
                  r.x, method='Nelder-Mead', options={'xatol': 1e-13, 'fatol': 1e-17, 'maxiter': 8000})
    C = Ms[0] + r2.x[0] * Ms[1] + r2.x[1] * Ms[2]
    w, V = np.linalg.eigh(C)
    q = V[:, 0] / np.exp(1j * np.angle(V[0, 0]))
    q = q / np.linalg.norm(q)
    return t0, np.round(q.real, 15), np.round(q.imag, 15), r2.x, -r2.fun


# ---------------------------------------------------------------- interval machinery
def ivf(x):
    return iv.mpf(repr(float(x)))


def make_env(M, K=100):
    T = iv.log(iv.mpf(3)) / 2
    d = 2 * T / M
    P = 2 * iv.pi / d
    a2T = 2 * T
    C0 = -iv.euler - iv.pi / 2 - 3 * iv.log(iv.mpf(2)) - iv.log(iv.pi)
    v2 = iv.sqrt(iv.mpf(2)) * iv.log(iv.mpf(2))
    log2 = iv.log(iv.mpf(2))
    A = iv.mpf(K) - iv.mpf(1) / 4
    ak = [iv.mpf(k) + iv.mpf(1) / 4 for k in range(K)]
    ak4 = [4 * a * a for a in ak]
    ehalf = iv.exp(a2T / 2)          # e^{(1/2)(2T)}
    emhalf = 1 / ehalf

    def m(t):
        t2 = t * t
        s = C0
        for a, a4 in zip(ak, ak4):
            s = s + t2 / (a * (t2 + a4))
        L = iv.log(1 + t2 / (4 * A * A)) / 2
        E = t2 * (t2 + 12 * A * A) / ((t2 * A + 4 * A ** 3) ** 2) / 24
        return s + iv.mpf([(L - E).a, L.b])

    def sigma(t):
        return m(t) - v2 * iv.cos(t * log2)

    def gs(t):
        c = iv.cos(t * a2T); s = iv.sin(t * a2T); t2 = t * t
        out = []
        for sg, E in ((iv.mpf(1) / 2, ehalf), (-iv.mpf(1) / 2, emhalf)):
            D = sg * sg + t2
            I = (E * (sg * c + t * s) - sg) / D
            num = a2T * E * (sg * c + t * s) + E * c - 1
            dI = num / D - 2 * sg * (E * (sg * c + t * s) - sg) / D ** 2
            out.append((I, dI))
        return out[0][0] + out[1][0], out[0][1] - out[1][1]

    return dict(T=T, d=d, P=P, m=m, sigma=sigma, gs=gs, C0=C0, v2=v2, a2T=a2T, K=K, A=A)


def phi_maker(env, qr, qi, M):
    d = env['d']
    QR = [ivf(x) for x in qr]; QI = [ivf(x) for x in qi]

    def phi(t):
        re = iv.mpf(0); im = iv.mpf(0)
        for k in range(M):
            c = iv.cos(iv.mpf(k) * d * t); s = iv.sin(iv.mpf(k) * d * t)
            re = re + QR[k] * c - QI[k] * s
            im = im + QR[k] * s + QI[k] * c
        return re * re + im * im
    return phi


def simpson_multi(fs, lo, P, n):
    """composite Simpson applied simultaneously to a tuple-valued integrand"""
    h = P / n
    acc = list(fs(lo))
    end = fs(lo + P)
    for i in range(len(acc)):
        acc[i] = acc[i] + end[i]
    for j in range(1, n):
        w = 4 if j % 2 else 2
        v = fs(lo + iv.mpf(j) * h)
        for i in range(len(acc)):
            acc[i] = acc[i] + w * v[i]
    return [x * h / 3 for x in acc]


# ---------------------------------------------------------------- rigorous derivative bounds
def zeta_hurwitz_quarter_ub(p):
    """upper bound for zeta(p,1/4) = sum_{n>=0}(n+1/4)^{-p}, p >= 2 integer."""
    from mpmath import zeta
    return float(4 ** p) + float(zeta(p))


def bounds(M, qr, qi, env, tau_max_abs):
    Sq = sum(abs(complex(a, b)) for a, b in zip(qr, qi))
    Gam = Sq * Sq                       # >= sum_l |gamma_l|
    dd = float(2 * Tf / M); n = M - 1
    Phi = [Gam * (dd * n) ** j for j in range(5)]
    mb = [0.0] + [2.0 ** (-j) * float(__import__('math').factorial(j)) * zeta_hurwitz_quarter_ub(j + 1)
                  for j in range(1, 5)]
    v2 = np.sqrt(2) * np.log(2); l2 = np.log(2)
    mb[0] = abs(float(-5.3721834)) + np.log(max(tau_max_abs, 7.0) / (2 * np.pi)) + 1.0
    sig = [mb[j] + v2 * l2 ** j for j in range(5)]
    a = 2 * Tf; chT = np.cosh(Tf); shT = np.sinh(Tf)
    g0 = [2 * chT * a ** (j + 1) / (j + 1) for j in range(5)]
    g1 = [2 * shT * a ** (j + 2) / (j + 2) for j in range(5)]
    from math import comb
    C4 = lambda X: sum(comb(4, j) * X[4 - j] * Phi[j] for j in range(5))
    return C4(sig), C4(g0), C4(g1), Gam


# ---------------------------------------------------------------- main
def run(M, na=4096, nb=12288, K=100):
    t0f, qr, qi, beta, lam = find_pair(M)
    env = make_env(M, K)
    phi = phi_maker(env, qr, qi, M)
    P = env['P']; lo = ivf(t0f)
    tau_max = abs(t0f) + float(P.b) + 1
    C4s, C4g0, C4g1, Gam = bounds(M, qr, qi, env, tau_max)
    Pf = float(P.b)
    err = lambda C4, n: Pf * (Pf / n) ** 4 * C4 / 180
    nrm2 = sum(x * x + y * y for x, y in zip(qr, qi))
    den = P * ivf(nrm2)

    t_start = time.time()
    (Ia,) = simpson_multi(lambda t: (env['sigma'](t) * phi(t),), lo, P, na)
    Ia = Ia + iv.mpf([-err(C4s, na), err(C4s, na)])

    def gpair(t):
        p = phi(t); a, b = env['gs'](t)
        return (a * p, b * p)
    g0i, g1i = simpson_multi(gpair, lo, P, nb)
    g0i = g0i + iv.mpf([-err(C4g0, nb), err(C4g0, nb)])
    g1i = g1i + iv.mpf([-err(C4g1, nb), err(C4g1, nb)])
    aI, b0I, b1I = Ia / den, g0i / den, g1i / den
    el = time.time() - t_start

    B = 5.0e4                      # task (c): ||beta||_inf <= 45169.4 < 5e4 when c >= 0
    bnd = aI + (abs(b0I) + abs(b1I)) * iv.mpf(B)
    out = dict(M=M, tau0=t0f, q_re=list(map(float, qr)), q_im=list(map(float, qi)),
               beta_search=list(map(float, beta)), lam_double=float(lam),
               n_sigma=na, n_g=nb, K=K,
               C4_sigma=C4s, C4_g0=C4g0, C4_g1=C4g1,
               err_sigma=err(C4s, na), err_g0=err(C4g0, nb), err_g1=err(C4g1, nb),
               a=[float(aI.a), float(aI.b)], b0=[float(b0I.a), float(b0I.b)],
               b1=[float(b1I.a), float(b1I.b)], B=B,
               ceiling_upper_bound=float(bnd.b), seconds=el)
    print(json.dumps(out, indent=1))
    return out


if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    na = int(sys.argv[2]) if len(sys.argv) > 2 else 4096
    nb = int(sys.argv[3]) if len(sys.argv) > 3 else 12288
    r = run(M, na, nb)
    json.dump(r, open(f'r2_a_enclosure_M{M}.json', 'w'), indent=1)
