"""R163_402: light-cone / resolution-law numerics (UNCERTIFIED float).
One-sided local model: G(z)=int_{-T}^{T} f(u) e^{izu} du, f Hermitian (G real on R),
basis phi_k(u)= i^k P_k(u/T). Zero set: actual zeta ordinates gamma_n (shifted by gamma0)
plus one artificial off-line pair t = +-i delta at x=0 (i.e. quartet at gamma0).
W(c) = sum_n G(x_n)^2 + 2 Re G(-i delta)^2 ; lambda(T) = min W/||f||^2."""
import numpy as np, mpmath as mp, sys, os
from numpy.polynomial.legendre import leggauss, legval
from scipy.linalg import eigh

cache = os.path.join(os.path.dirname(__file__), 'zeta_zeros_600.npy')
N = 600
if os.path.exists(cache):
    g = np.load(cache)
else:
    mp.mp.dps = 15
    g = np.array([float(mp.zetazero(n).imag) for n in range(1, N + 1)])
    np.save(cache, g)

K = int(os.environ.get('K', 40))
uq, wq = leggauss(80)

from scipy.special import spherical_jn
def Gmat(z, T):
    # exact: int_{-1}^1 P_k(s) e^{ias} ds = 2 i^k j_k(a); with i^k factor -> G_k(z)=2T(-1)^k j_k(Tz)
    z = np.asarray(z, dtype=complex)
    return np.array([2 * T * (-1) ** k * spherical_jn(k, T * z) for k in range(K)]).T

ZEROS = None
def lam(T, gamma0, delta):
    x = (g if ZEROS is None else ZEROS) - gamma0
    A = Gmat(x.astype(complex), T).real
    M = A.T @ A
    v = Gmat(np.array([-1j * delta]), T)[0]
    M += 2 * np.real(np.outer(v, v))
    Gram = np.diag([2 * T / (2 * k + 1) for k in range(K)])
    ev = eigh(M, Gram, eigvals_only=True)
    return ev[0] / ev[-1]  # relative; |.| < ~1e-12 is roundoff

def Tstar(gamma0, delta):
    Ts = np.linspace(0.05, 14, 1400)
    prev = None
    for T in Ts:
        l = lam(T, gamma0, delta)
        if l < -1e-9:
            return T
    return np.nan

def model(gamma0, delta):
    pr = np.log(gamma0 / (2 * np.pi)) / 2  # = pi*rho
    from scipy.optimize import brentq
    S = lambda T: np.sinh(2 * delta * T) / (2 * delta) - T - pr
    return brentq(S, 1e-6, 200), (3 * pr / (2 * delta ** 2)) ** (1 / 3)

if __name__ == '__main__':
    # gamma0 = midpoint of consecutive zeros (no on-line zero removed)
    # control: exact lattice of density rho (Poisson model), offset 1/2
    for gamma0 in [500.0]:
        rho = np.log(gamma0/2/np.pi)/(2*np.pi)
        ZEROS = gamma0 + (np.arange(-400, 400) + 0.5) / rho
        for delta in [0.4, 0.8, 1.2]:
            print('LATTICE', gamma0, delta, Tstar(gamma0, delta), model(gamma0, delta))
    ZEROS = None
    for idx in [100, 300, 500]:
        gamma0 = 0.5 * (g[idx] + g[idx + 1])
        for delta in [0.1, 0.2, 0.4, 0.8, 1.2]:
            ts = Tstar(gamma0, delta)
            m_exact, m_cubic = model(gamma0, delta)
            print(f"gamma0={gamma0:8.3f} delta={delta:5.2f}  T*_num={ts:6.3f}  "
                  f"T*_lattice(sinh)={m_exact:6.3f}  T*_cubic={m_cubic:6.3f}  "
                  f"Landau pi*rho={np.log(gamma0/2/np.pi)/2:5.3f}")
    sys.stdout.flush()
