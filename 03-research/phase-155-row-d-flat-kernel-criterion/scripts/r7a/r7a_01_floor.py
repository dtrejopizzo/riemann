"""R155 round 7a: the prolate concentration floor (Theorem P) and the proved bound on n_-.

S_{T,s} = Q_T B_s Q_T on L^2(-T,T), c = T s, tr S = 2c/pi, 0 <= S <= I.
Legendre basis P_j(t/T): FT on I_T is 2T i^j j_j(tau T) (spherical Bessel), so the diagonal of S is
   R_j(c) = (2j+1)(2/pi) int_0^c j_j(x)^2 dx,      sum_j R_j(c) = 2c/pi = tr S   (completeness).
Ky Fan (sum_{j<k} lambda_j >= sum_{j<k} R_j) + positivity (lambda_k <= sum_{n>=k} lambda_n) give

   THEOREM P:  lambda_k(c) <= Lam_k(c) := (2/pi) int_0^c (1 - G_k(x)) dx,
               G_k(x) = sum_{j<k} (2j+1) j_j(x)^2 in [0,1],  1 - G_k(x) = O(x^{2k}).

With Prop NC (R155_033): n_-(A_inf|P_T) <= n_-(Gamma_T on L^2) <= #{n : lambda_n(T tau1) > theta(tau1)},
theta(tau1) = m(tau1)/(m(tau1)-C0), hence
   n_- <= min_{tau1 > tau0} min{ k : Lam_k(T tau1) <= theta(tau1) }.
Runtime < 60 s.  Outputs scripts/r7a/r7a_01.json.
"""
import json
import numpy as np
from scipy.special import digamma, spherical_jn
from scipy.optimize import brentq
from scipy.integrate import cumulative_trapezoid

C0 = float(np.real(digamma(0.25)) - np.log(np.pi))
m = lambda t: float(np.real(digamma(0.25 + 0.5j * complex(t)))) - np.log(np.pi)
tau0 = brentq(m, 1.0, 50.0, xtol=1e-14)
theta = lambda t1: m(t1) / (m(t1) - C0)

KMAX, NG, XMAX = 45, 200001, 200.0
_xg = np.linspace(0.0, XMAX, NG)
_G = np.zeros(NG)
_I = []
for _k in range(KMAX + 1):
    _I.append(np.concatenate([[0.0], cumulative_trapezoid(1.0 - _G, _xg)]))
    _G = _G + (2 * _k + 1) * spherical_jn(_k, _xg) ** 2
_I = np.array(_I)
Lam = lambda k, c: (2 / np.pi) * max(float(np.interp(c, _xg, _I[k])), 0.0)

def prolate_eigs(T, s, N=300):
    x, w = np.polynomial.legendre.leggauss(N); x, w = T * x, T * w
    D = x[:, None] - x[None, :]
    K = np.where(np.abs(D) < 1e-13, s / np.pi, np.sin(s * D) / (np.pi * np.where(D == 0, 1, D)))
    sw = np.sqrt(w)
    return np.sort(np.linalg.eigvalsh(sw[:, None] * K * sw[None, :]))[::-1]

if __name__ == '__main__':
    out = {"tau0": tau0, "C0": C0, "windows": {}}
    print(f"tau0 = {tau0:.9f}   C0 = {C0:.7f}")
    for name, T in [("halflog3", 0.5 * np.log(3.0)), ("log2", np.log(2.0)), ("0.80", 0.80)]:
        best = None
        for t1 in np.linspace(tau0 * 1.0005, 200.0, 3000):
            th, c = theta(t1), T * t1
            for k in range(KMAX + 1):
                if Lam(k, c) <= th:
                    if best is None or k < best[0]:
                        best = (k, t1, th, c, Lam(k, c))
                    break
        k, t1, th, c, lk = best
        ev = prolate_eigs(T, t1)
        J = int(np.ceil(2 * T * tau0 / np.pi)) - 1
        print(f"\nT = {name} ({T:.7f}): PROVED  n_- <= {k}   (tau1 = {t1:.4f}, theta = {th:.6f}, "
              f"c = {c:.4f}, Lam_{k} = {lk:.3e});  Theorem J lower bound {J}")
        print("   Lam_k(c):", ["%.3e" % Lam(j, c) for j in range(k + 2)])
        print(f"   true lambda_n(c) (DIAGNOSTIC): {np.array2string(ev[:8], precision=5)};  "
              f"count > theta = {int((ev > th).sum())}")
        out["windows"][name] = {"T": T, "proved_upper_n_minus": k, "tau1": t1, "theta": th, "c": c,
                                "Lam": [Lam(j, c) for j in range(k + 2)],
                                "theoremJ_lower": J, "true_eigs": ev[:8].tolist(),
                                "true_count_above_theta": int((ev > th).sum())}
    json.dump(out, open("scripts/r7a/r7a_01.json", "w"), indent=1)
    print("\nwrote scripts/r7a/r7a_01.json")
