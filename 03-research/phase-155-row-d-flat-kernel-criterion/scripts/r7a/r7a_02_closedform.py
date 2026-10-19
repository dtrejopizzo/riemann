"""Corollary P1: the fully explicit closed-form version of Theorem P, with no quadrature.
|j_n(x)| <= x^n/(2n+1)!!  =>  Lam_k(c) <= (2/pi) sum_{j>=k} c^{2j+1}/((2j+1)!!)^2 =: Lam*_k(c).
Gives the n_- bound with every number a convergent series of rationals times powers of c."""
import numpy as np, json
from scipy.special import digamma
from scipy.optimize import brentq
C0 = float(np.real(digamma(0.25)) - np.log(np.pi))
m = lambda t: float(np.real(digamma(0.25 + 0.5j * complex(t)))) - np.log(np.pi)
tau0 = brentq(m, 1.0, 50.0, xtol=1e-14); theta = lambda t: m(t)/(m(t)-C0)
def dfact(n):
    r = 1.0
    for i in range(n, 0, -2): r *= i
    return r
def Lstar(k, c, J=80):
    return (2/np.pi)*sum(c**(2*j+1)/dfact(2*j+1)**2 for j in range(k, J))
res = {}
for nm, T in [("halflog3", .5*np.log(3)), ("log2", np.log(2)), ("0.80", .8)]:
    best = None
    for t1 in np.linspace(tau0*1.0005, 200., 3000):
        th, c = theta(t1), T*t1
        for k in range(50):
            if Lstar(k, c) <= th:
                if best is None or k < best[0]: best = (k, t1, th, c, Lstar(k, c))
                break
    print(f"{nm}: closed-form PROVED n_- <= {best[0]}  (tau1={best[1]:.4f}, theta={best[2]:.6f}, "
          f"c={best[3]:.4f}, Lam*={best[4]:.3e})")
    res[nm] = {"k": best[0], "tau1": best[1], "theta": best[2], "c": best[3], "Lamstar": best[4]}
json.dump(res, open("scripts/r7a/r7a_02.json", "w"), indent=1)
