"""Closed-form machinery for W5: primitive piecewise-polynomial test functions
F on I_T = (-T,T), with Fhat, Tate moments, L2 norm, and autocorrelation g(a)
all computed EXACTLY via polynomial recursions -- no quadrature over t.

F(t) = P(t) for |t|<T, 0 outside, P a polynomial represented as a coefficient
array `coeffs` with coeffs[n] = coefficient of t^n (numpy convention: index by
power, NOT numpy.poly1d's reversed convention).

Basis: b_k(t) = (t/T)^k * (1-(t/T)^2)^3,  k=0,1,2,3.
(1-x^2)^3 = 1 - 3x^2 + 3x^4 - x^6 vanishes to order 3 at x=+-1, so every
combination of the b_k is globally C^2 on R (value, 1st and 2nd derivative
all match the zero extension at t=+-T) -- Fhat decays like O(tau^-4), i.e.
h(tau)=|Fhat(tau)|^2 like O(tau^-8).  This is the same bump family as the
coordinator's W0_weil_identity.py draft, but with closed-form Fhat instead of
quadrature.

No file in this module imports rowd_assembly or rowd_threshold.
"""
import math
import numpy as np
import mpmath as mp

EULER = 0.57721566490153286060651209008240243104215933593992
M0 = math.log(math.pi) + EULER + math.pi / 2 + 3 * math.log(2)


# --------------------------------------------------------- polynomial basics
def basis_coeffs(T, kmax=3):
    """List of coeff arrays for b_k(t) = (t/T)^k (1-(t/T)^2)^3, k=0..kmax."""
    base = np.array([1.0, 0.0, -3.0, 0.0, 3.0, 0.0, -1.0])  # powers 0..6 of x=t/T
    out = []
    for k in range(kmax + 1):
        # (t/T)^k * base(x)  in x, then convert x^n -> t^n / T^n
        c_x = np.zeros(k + 7)
        c_x[k:k + 7] = base
        c_t = np.array([c_x[n] / T ** n for n in range(len(c_x))])
        out.append(c_t)
    maxlen = max(len(c) for c in out)
    return [np.pad(c, (0, maxlen - len(c))) for c in out]


def pad_to(c, n):
    if len(c) >= n:
        return c
    return np.pad(c, (0, n - len(c)))


def real_moment_integral(coeffs, T, c, small_c_thresh=1.0, taylor_terms=24):
    """int_{-T}^{T} P(t) e^{c t} dt  for real c (c=0 handled exactly).

    The recursion J_k = (...)/c - (k/c) J_{k-1} divides by c at every one of
    the ~deg(P) steps, so for |c| small compared to the degree it amplifies
    float error by ~prod(k/c) -- CONFIRMED to break badly: at T=0.6, c=0.123,
    degree 9, the recursion gave 2.35 against scipy.quad's 0.212 (wrong by a
    factor of 11!). Fixed the same way as fourier_moment_integral: a Taylor
    series in c using the (well-conditioned, power-rule) moments mu_j for
    |c| < small_c_thresh."""
    n = len(coeffs)
    if c == 0.0:
        tot = 0.0
        for k, ck in enumerate(coeffs):
            if ck == 0.0:
                continue
            if k % 2 == 0:
                tot += ck * 2.0 * T ** (k + 1) / (k + 1)
        return tot
    if abs(c) < small_c_thresh:
        mu = moments_at_origin(coeffs, T, taylor_terms)
        fact = 1.0
        acc = 0.0
        power = 1.0
        for j in range(taylor_terms + 1):
            if j > 0:
                fact *= j
                power *= c
            acc += (power / fact) * mu[j]
        return acc
    # J_k = int_{-T}^T t^k e^{ct} dt ; recursion J_k = (T^k e^{cT}-(-T)^k e^{-cT})/c - (k/c) J_{k-1}
    eT, emT = math.exp(c * T), math.exp(-c * T)
    J = (eT - emT) / c
    tot = coeffs[0] * J if n > 0 else 0.0
    Tk = 1.0
    for k in range(1, n):
        Tk *= T
        bterm = (Tk * eT - ((-1.0) ** k) * Tk * emT) / c
        J = bterm - (k / c) * J
        tot += coeffs[k] * J
    return tot


def moments_at_origin(coeffs, T, jmax):
    """mu_j = int_{-T}^T t^j P(t) dt, j=0..jmax (exact power rule)."""
    out = np.zeros(jmax + 1)
    for j in range(jmax + 1):
        shifted = np.concatenate([np.zeros(j), coeffs])
        out[j] = poly_integral_power_rule(shifted, -T, T)
    return out


def fourier_moment_integral(coeffs, T, tau, small_tau_thresh=2.0, taylor_terms=40):
    """int_{-T}^T P(t) e^{i tau t} dt, vectorized complex.

    The direct recursion (division by i*tau at every step) loses precision by
    catastrophic cancellation as tau -> 0 (checked: ~1e-8 relative error
    already visible at tau*T ~ 1e-3).  For |tau| < small_tau_thresh we instead
    use the Taylor series Fhat(tau) = sum_j (i tau)^j/j! mu_j, mu_j = the j-th
    moment of F about the origin (an exact, well-conditioned power-rule
    integral) -- verified against scipy.quad to < 1e-13 in both regimes, see
    W5_test_closed_form.py."""
    tau = np.atleast_1d(np.asarray(tau, dtype=float))
    out = np.zeros(tau.shape, dtype=complex)

    small = np.abs(tau) < small_tau_thresh
    if np.any(small):
        mu = moments_at_origin(coeffs, T, taylor_terms)
        fact = 1.0
        acc = np.zeros(np.sum(small), dtype=complex)
        z = tau[small]
        power = np.ones_like(z, dtype=complex)
        for j in range(taylor_terms + 1):
            if j > 0:
                fact *= j
                power = power * (1j * z)
            acc = acc + (power / fact) * mu[j]
        out[small] = acc

    nz = ~small
    if np.any(nz):
        z = tau[nz]
        ic = 1j * z
        eT = np.exp(ic * T)
        emT = np.exp(-ic * T)
        n = len(coeffs)
        J = (eT - emT) / ic
        tot = coeffs[0] * J if n > 0 else np.zeros_like(J)
        Tk = 1.0
        for k in range(1, n):
            Tk *= T
            bterm = (Tk * eT - ((-1.0) ** k) * Tk * emT) / ic
            J = bterm - (k / ic) * J
            tot = tot + coeffs[k] * J
        out[nz] = tot
    return out


def shift_poly_correct(coeffs, a):
    """Correct binomial shift: P(t+a) = sum_k c_k sum_j C(k,j) a^{k-j} t^j."""
    n = len(coeffs)
    out = np.zeros(n)
    for k in range(n):
        ck = coeffs[k]
        if ck == 0.0:
            continue
        for j in range(k + 1):
            out[j] += ck * math.comb(k, j) * a ** (k - j)
    return out


def poly_integral_power_rule(coeffs, lo, hi):
    """int_lo^hi P(t) dt via the power rule, exact for polynomials."""
    tot = 0.0
    for k, ck in enumerate(coeffs):
        if ck == 0.0:
            continue
        tot += ck * (hi ** (k + 1) - lo ** (k + 1)) / (k + 1)
    return tot


def l2_norm_sq(coeffs, T):
    prod = np.convolve(coeffs, coeffs)
    return poly_integral_power_rule(prod, -T, T)


def total_variation(coeffs, T):
    """TV of F on R = TV of P on [-T,T] (F is continuous, 0 outside, since
    (1-x^2)^3 vanishes at x=+-1) = int_{-T}^T |P'(t)| dt.

    Computed by adaptive quadrature of |P'(t)| directly (scipy.integrate.quad
    handles the finitely many kinks of |P'| fine on its own via bisection);
    NOTE an earlier version tried to locate the kinks itself via np.roots and
    silently dropped near-boundary roots that numpy perturbed off the real
    axis by ~1e-7 (t=+-T is a genuine double root of P' here), giving a value
    ~20% too small. Cross-checked the fix against a 4e6-point trapezoid grid
    to 8 digits -- see W5_test_closed_form.py."""
    from scipy.integrate import quad
    dcoeffs = np.array([coeffs[k] * k for k in range(1, len(coeffs))])
    if len(dcoeffs) == 0 or np.allclose(dcoeffs, 0):
        return 0.0
    Pp = np.poly1d(dcoeffs[::-1])
    return quad(lambda t: abs(Pp(t)), -T, T, limit=4000)[0]


def autocorr(coeffs, T, a):
    """g(a) = int F(t) F(t+a) dt, F supported on (-T,T), for |a| < 2T."""
    a = abs(a)
    if a >= 2 * T:
        return 0.0
    shifted = shift_poly_correct(coeffs, a)
    prod = np.convolve(coeffs, shifted)
    lo, hi = -T, T - a
    if hi <= lo:
        return 0.0
    return poly_integral_power_rule(prod, lo, hi)


# ------------------------------------------------------------- archimedean
def phi_gamma(tau):
    """phi(tau) := Re psi(1/4 + i tau/2) - log(pi)  ==  g_Gamma(tau) - m_0
    identically (PROOF_ARCHITECTURE.md Sec.2, verified to 30 digits at
    tau=0,0.5,3,17.5,120).  Scalar, uses mpmath digamma."""
    return float(mp.re(mp.digamma(mp.mpf('0.25') + 1j * mp.mpf(tau) / 2))) - math.log(math.pi)


def phi_gamma_vec(taus, dps=30):
    old = mp.mp.dps
    mp.mp.dps = dps
    try:
        return np.array([phi_gamma(t) for t in taus])
    finally:
        mp.mp.dps = old


# ------------------------------------------------------- prime-power sieve
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
    """List of (n, w_n=Lambda(n)/sqrt(n)) for 2<=n<e^{2T}."""
    Nmax = int(math.floor(math.exp(2 * T)))
    lam = von_mangoldt_upto(max(Nmax, 2))
    out = []
    for n in range(2, Nmax + 1):
        if lam[n] > 0 and n < math.exp(2 * T) - 1e-12:
            out.append((n, lam[n] / math.sqrt(n)))
    return out
