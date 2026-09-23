"""revlib.py -- phase 155, REVERSE-ENGINEERING track.

Flat-top weights w (Paper 47, Def. 7.1 / class W_T), their Fourier transforms,
the zero-side sum  f^known_w(tau) = sum_{|gamma|<=Gmax} what(tau-gamma),
and the prime/Gamma side of Theorem Z.

Conventions (Paper 47):
  what(t) = int w(u) e^{itu} du ;  rho = 1/2 + i gamma ;  v_n = 2 Lambda(n)/sqrt(n)
  K(u) = (1/2)/sinh(u/2) + (1/2)/cosh(u/2) ;  C0 = psi(1/4) - log pi
  m(tau) = Re psi(1/4 + i tau/2) - log pi
Weight family: w = 1 on [-2T,2T]; for |u|>2T, w(u) = sum_k x_k exp(-s_k(|u|-2T)),
s_k > 1/2 required (finiteness of nu_w).  ALL NUMBERS HERE ARE DIAGNOSTIC.
"""
import numpy as np, os
from scipy.special import digamma

LOG_PI = np.log(np.pi)
C0 = float(np.real(digamma(0.25))) - LOG_PI

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- zeros
def load_zeros(path=None):
    path = path or os.path.join(HERE, "zeros1.txt")
    g = np.loadtxt(path)
    return g                      # positive ordinates, ascending

# ---------------------------------------------------------------- m(tau)
def m_of_tau(tau):
    return np.real(digamma(0.25 + 0.5j * np.asarray(tau, float))) - LOG_PI

# ------------------------------------------------- what : box + columns
def what_box(t, T):
    """FT of 1_{[-2T,2T]} : 2 sin(2Tt)/t."""
    t = np.asarray(t, float)
    out = np.empty_like(t)
    small = np.abs(t) < 1e-12
    out[~small] = 2.0 * np.sin(2 * T * t[~small]) / t[~small]
    out[small] = 4.0 * T
    return out

def what_col(t, T, s):
    """FT of exp(-s(|u|-2T)) 1_{|u|>=2T}, even:  2 Re[e^{2iTt}/(s-it)]."""
    t = np.asarray(t, float)
    d = s * s + t * t
    return 2.0 * (s * np.cos(2 * T * t) - t * np.sin(2 * T * t)) / d

# ------------------------------------------------- zero-side sums
# far-zero trick: what_box(tau-g) = 2 Im[e^{2iT tau} e^{-2iT g}/(tau-g)]
#                 what_col(tau-g) = 2 Re[e^{2iT tau} e^{-2iT g}/(s-i(tau-g))]
# For |tau-g| large the bracket is slowly varying in tau -> coarse grid + spline.
from scipy.interpolate import CubicSpline

def zero_side_matrix(tau, T, svals, gam, near_cut=1200.0, ncoarse=129, JF=14):
    """Return (Bz, Az) with
         Bz[i]   = sum_{|gamma|<=Gmax} what_box(tau_i - gamma)
         Az[k,i] = sum_{|gamma|<=Gmax} what_col(tau_i - gamma ; s_k),
       both gamma and -gamma included.  Near zeros (|gamma|<=near_cut) exactly;
       far zeros through the slowly varying brackets
         P_j(tau) = sum_far [ e^{-2iT g}/(tau-g)^{j+1} + e^{+2iT g}/(tau+g)^{j+1} ]
       (coarse grid + cubic spline), using
         what_box(t) = 2 Im[e^{2iT tau} P_0-term],
         1/(s-i d)   = sum_j (-1)^j i^{j+1} s^j / d^{j+1}.
    """
    tau = np.asarray(tau, float)
    svals = np.asarray(svals, float)
    near = gam[gam <= near_cut]
    far = gam[gam > near_cut]
    nT = len(tau); nS = len(svals)
    Bz = np.zeros(nT); Az = np.zeros((nS, nT))
    # ---- near part, exact, chunked over zeros
    CHZ = 128
    for a in range(0, len(near), CHZ):
        ng = near[a:a + CHZ]
        for d in (tau[None, :] - ng[:, None], tau[None, :] + ng[:, None]):
            c2 = np.cos(2 * T * d); s2 = np.sin(2 * T * d)
            with np.errstate(divide='ignore', invalid='ignore'):
                bb = 2.0 * s2 / d
            bb[np.abs(d) < 1e-12] = 4.0 * T
            Bz += bb.sum(0)
            d2 = d * d
            for k in range(nS):
                s = svals[k]
                Az[k] += ((s * c2 - d * s2) / (s * s + d2)).sum(0) * 2.0
    # ---- far part
    if len(far):
        tc = np.linspace(tau.min(), tau.max(), ncoarse)
        e_m = np.exp(-2j * T * far); e_p = np.conj(e_m)
        P = np.zeros((JF, ncoarse), complex)
        CH = 4096
        for c0 in range(0, len(far), CH):
            c1 = min(c0 + CH, len(far))
            fg = far[c0:c1]
            d1 = tc[None, :] - fg[:, None]; d2 = tc[None, :] + fg[:, None]
            em = e_m[c0:c1][:, None]; ep = e_p[c0:c1][:, None]
            r1 = em / d1; r2 = ep / d2
            for j in range(JF):
                P[j] += r1.sum(0) + r2.sum(0)
                r1 /= d1; r2 /= d2
        ph = np.exp(2j * T * tau)
        def interp(z):
            return CubicSpline(tc, z.real)(tau) + 1j * CubicSpline(tc, z.imag)(tau)
        Pi = np.array([interp(P[j]) for j in range(JF)])
        Bz += 2.0 * np.imag(ph * Pi[0])
        for k in range(nS):
            s = svals[k]
            H = np.zeros(nT, complex)
            for j in range(JF):
                H += ((-1) ** j) * (1j ** (j + 1)) * (s ** j) * Pi[j]
            Az[k] += 2.0 * np.real(ph * H)
    return Bz, Az

# ------------------------------------------------- prime / Gamma side
NIK = 40   # terms of K(u) = 2 sum_{i>=0} e^{-(2i+1/2)u}

def Ktail_box(tau, T):
    """int_{2T}^inf K(u) cos(tau u) du   (the '1' part of 1-w)."""
    tau = np.asarray(tau, float); z = 2 * T
    out = np.zeros_like(tau)
    ph = np.exp(2j * T * tau)
    for i in range(NIK):
        a = 2 * i + 0.5
        out += 2 * np.exp(-a * z) * np.real(ph / (a - 1j * tau))
    return out

def Ktail_col(tau, T, s):
    """int_{2T}^inf e^{-s(u-2T)} K(u) cos(tau u) du."""
    tau = np.asarray(tau, float); z = 2 * T
    out = np.zeros_like(tau); ph = np.exp(2j * T * tau)
    for i in range(NIK):
        a = 2 * i + 0.5
        out += 2 * np.exp(-a * z) * np.real(ph / (s + a - 1j * tau))
    return out

def cosh_box(tau, T):
    """2 int_{-2T}^{2T} cosh(u/2) cos(tau u) du."""
    tau = np.asarray(tau, float)
    return 4 * (0.5 * np.sinh(T) * np.cos(2 * T * tau)
                + tau * np.cosh(T) * np.sin(2 * T * tau)) / (0.25 + tau ** 2)

def cosh_col(tau, T, s):
    """2 int_{|u|>=2T} e^{-s(|u|-2T)} cosh(u/2) cos(tau u) du."""
    tau = np.asarray(tau, float); ph = np.exp(2j * T * tau)
    return 2 * np.real(ph * (np.exp(T) / (s - 0.5 - 1j * tau)
                             + np.exp(-T) / (s + 0.5 - 1j * tau)))

# prime data
def vonmangoldt_table(N):
    sieve = np.zeros(N + 1, dtype=np.int64)
    is_c = np.zeros(N + 1, dtype=bool)
    for p in range(2, int(N ** .5) + 1):
        if not is_c[p]:
            is_c[p * p::p] = True
    primes = np.nonzero(~is_c[2:])[0] + 2
    ns, lg = [], []
    for p in primes:
        q = int(p)
        while q <= N:
            ns.append(q); lg.append(np.log(p)); q *= p
    ns = np.array(ns, float); lg = np.array(lg, float)
    o = np.argsort(ns)
    return ns[o], lg[o]

def prime_side(tau, T, svals, x, ns, lam, dzz=None):
    """- sum_n v_n w(log n) cos(tau log n), with v_n = 2 Lambda(n)/sqrt(n).
       ns, lam : prime powers <= N and their Lambda.  dzz : optional dict
       s -> array of  D(1/2+s+i tau) = sum_n Lambda(n) n^{-1/2-s-i tau} (exact,
       from -zeta'/zeta) used to replace the tail n > N for small s."""
    tau = np.asarray(tau, float)
    L2T = 2 * T
    logn = np.log(ns)
    wn = np.where(logn <= L2T, 1.0,
                  sum(x[k] * np.exp(-svals[k] * np.maximum(logn - L2T, 0.0))
                      for k in range(len(svals))))
    coef = 2 * lam / np.sqrt(ns) * wn
    out = np.zeros_like(tau)
    CH = 20000
    for a in range(0, len(ns), CH):
        b = min(a + CH, len(ns))
        out += coef[a:b] @ np.cos(np.outer(logn[a:b], tau))
    return -out

def f_prime_side(tau, T, svals, x, ns, lam):
    """Theorem Z (i):  f_w(tau) = m(tau) + int_{2T}^inf (1-w) K cos
                        - sum v_n w(log n) cos + 2 int w cosh(u/2) cos."""
    tau = np.asarray(tau, float)
    Kt = Ktail_box(tau, T) - sum(x[k] * Ktail_col(tau, T, svals[k])
                                 for k in range(len(svals)))
    ch = cosh_box(tau, T) + sum(x[k] * cosh_col(tau, T, svals[k])
                                for k in range(len(svals)))
    return m_of_tau(tau) + Kt + prime_side(tau, T, svals, x, ns, lam) + ch

# ------------------------------------------------- misc
def basis(K=48, smin=1.5, smax=60.0):
    return np.exp(np.linspace(np.log(smin), np.log(smax), K))

def A_const(T):
    """A_T = sup of the prime comb = sum_{n < e^{2T}} v_n."""
    tot = 0.0
    n = 2
    ns, lam = vonmangoldt_table(int(np.exp(2 * T)) + 2)
    for nn, ll in zip(ns, lam):
        if np.log(nn) < 2 * T - 1e-12:
            tot += 2 * ll / np.sqrt(nn)
    return tot
