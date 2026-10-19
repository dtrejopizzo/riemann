"""R155 round 4b, (b): an explicit upper bound on n_-(A_inf|P_T).

On P_T, A_inf(F) = (1/2pi) int m |Fhat|^2.  Fix tau1 > tau0 (the zero of m).  Since m >= C0 on
|tau|<tau1 and m >= m(tau1) > 0 outside,
     A_inf(F) >= m(tau1) - (m(tau1)-C0) * ||B_{tau1} F||^2      (||F||=1)
so A_inf(F) < 0 forces ||B_{tau1}F||^2 > theta(tau1) := m(tau1)/(m(tau1)-C0).
By min-max, n_-(A_inf on L^2(-T,T)) <= #{ n : lambda_n(S_{T,tau1}) > theta(tau1) }, where
S = Q_T B_{tau1} Q_T is the Slepian time-band-limiting operator, eigenvalues lambda_n(c),
c = T*tau1.   Two bounds:
   (A) trace/Markov  #{lambda_n>theta} < trace(S)/theta = 2 T tau1 / (pi theta)   [PROVED, explicit]
   (B) the actual prolate count (DIAGNOSTIC: numerical eigenvalues of the sinc kernel).
"""
import numpy as np
from scipy.special import digamma
from scipy.optimize import brentq

C0 = float(np.real(digamma(0.25)) - np.log(np.pi))
m = lambda t: np.real(digamma(0.25 + 0.5j * np.asarray(t, dtype=complex))) - np.log(np.pi)
tau0 = brentq(lambda t: m(t), 1.0, 50.0, xtol=1e-13)

def theta(t1):
    v = m(t1)
    return v / (v - C0)

def trace_bound(T, t1):
    return 2.0 * T * t1 / (np.pi * theta(t1))

def prolate_eigs(T, t1, N=1400):
    """eigenvalues of (S f)(x) = int_{-T}^{T} sin(t1(x-y))/(pi(x-y)) f(y) dy, Gauss-Legendre Nystrom."""
    x, w = np.polynomial.legendre.leggauss(N)
    x = T * x; w = T * w
    D = x[:, None] - x[None, :]
    K = np.where(np.abs(D) < 1e-12, t1 / np.pi, np.sin(t1 * D) / (np.pi * np.where(D == 0, 1, D)))
    sw = np.sqrt(w)
    A = sw[:, None] * K * sw[None, :]
    return np.sort(np.linalg.eigvalsh(A))[::-1]

if __name__ == '__main__':
    print(f"tau0 = {tau0:.8f}   C0 = {C0:.7f}")
    for name, T in [("halflog3", 0.5*np.log(3.0)), ("log2", np.log(2.0)), ("0.80", 0.80)]:
        grid = np.linspace(tau0*1.02, 200.0, 4000)
        vals = np.array([trace_bound(T, t) for t in grid])
        i = int(np.argmin(vals))
        t1s = grid[i]
        print(f"\nT={name}: trace bound min = {vals[i]:.3f} at tau1={t1s:.3f} "
              f"(theta={theta(t1s):.4f}, c=T*tau1={T*t1s:.3f})  -> n_- <= {int(np.floor(vals[i]))}")
        best = None
        for t1 in np.linspace(tau0*1.005, 60.0, 150):
            ev = prolate_eigs(T, t1, N=500)
            cnt = int((ev > theta(t1)).sum())
            if best is None or cnt < best[0]:
                best = (cnt, t1, theta(t1), ev[:6])
        print(f"   prolate count (DIAGNOSTIC): n_- <= {best[0]} at tau1={best[1]:.3f}, "
              f"theta={best[2]:.4f}; top eigs {np.array2string(best[3], precision=4)}")
