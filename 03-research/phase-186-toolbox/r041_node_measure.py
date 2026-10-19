#!/usr/bin/env python3
"""R186_041 — Gauss nodal measure of the minimizer h*_T and its coupling with Λ.   (self-contained; imports r034_det.py)

Usage: python3 r041_node_measure.py [M=70] [X=120]

For T in {1/2 log 3, log 2, 1/2 log 5}:
  (1) h*_T (Legendre Galerkin on P_T), G = ĥ* (real: even) or -i ĥ* (odd); nodes X_T = {x : G(x)=0} in (0, X];
  (2) divided functions H_x = h* * (1/(tau-x))^v, H_x(t) = -i e^{-ixt} int_{-T}^t h* e^{ixs} ds  (support in I_T because G(x)=0);
      check of R165_202 2.1 on P_T: (a_T - λ)(H_y, H_x) = 0 (x≠y) and weights w_x = (a_T-λ)(H_x)/|G'(x)|² ≥ 0;
  (3) quadrature identity (Lemma 1):  a_T(F) - λ||F||² = Σ_x w_x |F̂(x)|²  for F ∈ P_T smooth (F̂ = O(τ^-4));
  (4) "the nodes know the primes of the window": the nodal function μ̌_X(u) = Σ w_x cos(xu), smoothed with a Gaussian
      of width eps, compared with -K(u)/2 - Σ_{n∈N_T}(v_n/2) φ_eps(u - log n) + a cosh(u/2) + b u sinh(u/2) on 0<u<2T;
  (5) alignment cos(x log n) of the present nodes with the future prime powers (log n > 2T), and the smoothed
      nodal function in the strip (2T, 2T+1.2) evaluated at the future log n (= the only place where Λ outside the
      window touches the nodes, Lemma 2).
"""
import sys, numpy as np
from numpy.polynomial import legendre as NL
from scipy.special import spherical_jn
import r034_det as R

C0 = R.C0 if hasattr(R, 'C0') else None

def hstar(T, M, nu=400):
    A, A0, ta, tb = R.build_x(T, M, nu)
    Z = R.null_basis([ta, tb]); AP = Z.T @ A @ Z
    lam, V = np.linalg.eigh(AP); c = Z @ V[:, 0]
    return A, Z, lam[0], c / np.linalg.norm(c)

def Ghat(T, M, c, tau):
    """ĥ(τ) = Σ c_k φ̂_k, φ̂_k(τ) = sqrt((2k+1)2T) i^k j_k(τT)."""
    tau = np.atleast_1d(np.asarray(tau, float)); k = np.arange(M)
    J = np.array([spherical_jn(kk, tau * T) for kk in k])
    return np.einsum('k,kt->t', c * np.sqrt((2 * k + 1) * 2 * T) * (1j ** k), J)

def parity(c):
    return 'even' if np.linalg.norm(c[1::2]) < np.linalg.norm(c[0::2]) else 'odd'

def nodes(T, M, c, X, h=2e-3):
    par = parity(c); g = np.arange(h, X, h)
    G = Ghat(T, M, c, g); G = G.real if par == 'even' else G.imag
    xs = []
    for i in range(len(g) - 1):
        if G[i] * G[i + 1] < 0:
            a, b = g[i], g[i + 1]
            for _ in range(50):
                m = (a + b) / 2; Gm = Ghat(T, M, c, [m]); Gm = Gm.real[0] if par == 'even' else Gm.imag[0]
                if G[i] * Gm < 0: b = m
                else: a = m
            xs.append((a + b) / 2)
    return np.array(xs), par

def legcoords(T, M, f_vals, y, w):
    F = R.legbasis(T, M, y); return (F * w) @ f_vals

def divided(T, M, c, x, nq=400, Z=None):
    """Legendre coordinates (complex) of H_x(t) = -i e^{-ixt} int_{-T}^t h*(s) e^{ixs} ds."""
    yq, wq = NL.leggauss(nq); y = T * yq; w = T * wq
    h = (R.legbasis(T, M, y).T @ c)                       # h*(y_j)
    # cumulative integral by inner quadrature at each y_j
    out = np.zeros(len(y), complex)
    yi, wi = NL.leggauss(200)
    for j, t in enumerate(y):
        s = (t + T) / 2 * yi + (t - T) / 2; ws = (t + T) / 2 * wi
        hs = R.legbasis(T, M, s).T @ c
        out[j] = -1j * np.exp(-1j * x * t) * np.sum(hs * np.exp(1j * x * s) * ws)
    cH = legcoords(T, M, out.real, y, w) + 1j * legcoords(T, M, out.imag, y, w)
    return cH if Z is None else Z @ (Z.T @ cH)        # exact reprojection onto P_T (the polar leak has a_T ~ -10^12)

def Gprime(T, M, c, x, par, d=1e-5):
    g = Ghat(T, M, c, [x - d, x + d]); g = g.real if par == 'even' else g.imag
    return (g[1] - g[0]) / (2 * d)

def smooth_test(T, M, Z, seed=0):
    """F = (T²-t²)^4 · random polynomial, projected onto P_T; F̂ = O(τ^-5)."""
    rng = np.random.default_rng(seed); yq, wq = NL.leggauss(300); y = T * yq; w = T * wq
    p = np.polyval(rng.standard_normal(4), y / T); f = (1 - (y / T) ** 2) ** 4 * p
    c = legcoords(T, M, f, y, w); c = Z @ (Z.T @ c); return c / np.linalg.norm(c)

def main(M=70, X=120.0):
    for T in [0.5 * np.log(3), np.log(2), 0.5 * np.log(5)]:
        A, Z, lam, c = hstar(T, M)
        xs, par = nodes(T, M, c, X)
        print(f"\n===== T = {T:.4f}  (2T = {2*T:.4f})  M = {M}  λ_A = {lam:.4e}  h* {par}  #nodes in (0,{X:.0f}] = {len(xs)} =====")
        print("first nodes:", np.round(xs[:12], 3))
        print("mean spacing of last 10:", np.round(np.mean(np.diff(xs[-10:])), 4), " vs π/T =", round(np.pi / T, 4))
        Q = A - lam * np.eye(M)
        # (2) weights and orthogonality of the divided functions (first nodes, expensive)
        nd = len(xs); Hs = [divided(T, M, c, x, Z=Z) for x in xs[:nd]]
        Gp = np.array([Gprime(T, M, c, x, par) for x in xs[:nd]])
        Qm = np.array([[np.conj(Hs[i]) @ Q @ Hs[j] for j in range(nd)] for i in range(nd)])
        dg = np.real(np.diag(Qm)); off = np.max(np.abs(Qm - np.diag(np.diag(Qm)))) / np.max(np.abs(dg))
        print(f"(2) max |(a-λ)(H_y,H_x)|/max diag (x≠y) = {off:.2e};  min diag = {dg.min():.3e}")
        w_first = dg / Gp ** 2
        # weights for all nodes via the cheap route: w_x ≈ (σ_T(x)-λ)·(local spacing)/(2π)·2 ? NO: the exact ones
        # are used for the first nd and, for the rest, the Riemann approximation w_x ≈ (σ_T(x)-λ)·Δx/π (Δx = half the spacing
        # on each side); the quality of the approximation is checked against the exact nd.
        dx = np.gradient(xs); w_riem = (R.sigma_T(T, xs) - lam) * dx / (2 * np.pi)   # mass of (σ-λ)dτ/2π in the cell of node x>0
        print("(2) exact w    :", np.round(w_first[:8], 4))
        print("    Riemann w  :", np.round(w_riem[:8], 4), "  (exact/Riemann ratio:", np.round(w_first[:8] / w_riem[:8], 3), ")")
        w = w_riem.copy(); w[:nd] = w_first
        # (3) quadrature on smooth F in P_T
        for seed in range(3):
            f = smooth_test(T, M, Z, seed); lhs = f @ Q @ f
            Fx = np.abs(Ghat(T, M, f, xs)) ** 2
            rhs_ex = 2 * (np.sum(w_first * Fx[:nd]) + np.sum(w_riem[nd:] * Fx[nd:]))   # symmetric X: ±x
            rhs_first = 2 * np.sum(w_first * Fx[:nd])
            print(f"(3) F#{seed}: (a-λ)(F) = {lhs:.5e}   Σ_x w_x|F̂(x)|² = {rhs_ex:.5e}  (only {nd} exact: {rhs_first:.5e})  ratio = {rhs_ex/lhs:.4f}")
        # (4) nodal function smoothed inside the window
        eps = 0.06; u = np.linspace(0.25, 2 * T + 1.2, 600)
        mu = np.array([np.sum(w * np.exp(-eps ** 2 * xs ** 2 / 2) * np.cos(xs * uu)) for uu in u]) * 2   # ±x
        Kh = -0.5 * R.K(u)                                                                               # Lévy
        phi = lambda v: np.exp(-v ** 2 / (2 * eps ** 2)) / (np.sqrt(2 * np.pi) * eps)
        comb = np.zeros_like(u)
        for n, lp in R.contacts(T): comb -= lp / np.sqrt(n) * (phi(u - np.log(n)) + phi(u + np.log(n)))
        inside = u < 2 * T - 0.1
        # fit of a, b (Tate) by least squares inside the window
        B = np.vstack([np.cosh(u / 2), u * np.sinh(u / 2)]).T
        resid = mu - Kh - comb; ab, *_ = np.linalg.lstsq(B[inside], resid[inside], rcond=None)
        model = Kh + comb + B @ ab; err_in = np.max(np.abs(mu - model)[inside]) / np.max(np.abs(mu[inside]))
        print(f"(4) a,b (Tate) = {ab.round(4)};  max relative error of μ̌_X vs [-K/2 - atoms v_n/2 + Tate] on (0.25, 2T-0.1): {err_in:.3f}")
        for n, lp in R.contacts(T):
            i = np.argmin(np.abs(u - np.log(n))); print(f"    atom log {n}={np.log(n):.3f}: μ̌_X smoothed = {mu[i]:+.3f}, model = {model[i]:+.3f}, without atom = {(Kh + B @ ab)[i]:+.3f}")
        # (5) future primes
        fut = [(n, lp) for n, lp in R.contacts(T + 0.7) if np.log(n) >= 2 * T][:5]
        print("(5) alignment cos(x log n) at the first 8 nodes for FUTURE prime powers:")
        for n, lp in fut:
            cs = np.cos(xs[:8] * np.log(n)); print(f"    n={n:2d} log n={np.log(n):.3f}: " + " ".join(f"{v:+.2f}" for v in cs) + f"   Σ_x w_x cos(x log n) (smoothed) = {2*np.sum(w*np.exp(-eps**2*xs**2/2)*np.cos(xs*np.log(n))):+.3f}")
        strip = u > 2 * T + 0.05
        eta = mu - Kh - B @ ab
        print("    strip (2T, 2T+1.2): η̌_T = μ̌_X + K/2 - Tate  at u = 2T+0.1 … 2T+1.1:",
              np.round([eta[np.argmin(np.abs(u - (2 * T + d)))] for d in (0.1, 0.3, 0.5, 0.7, 0.9, 1.1)], 3))

if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 70
    X = float(sys.argv[2]) if len(sys.argv) > 2 else 120.0
    main(M, X)
