"""Unit checks for W5_closed_form.py against scipy.integrate.quad (ground
truth via direct numerical quadrature over t, independent implementation).
Not part of the identity check itself -- just validates the closed-form
machinery before it is trusted in W5_identity_check.py.

run:  python3 W5_test_closed_form.py
"""
import math
import numpy as np
from scipy.integrate import quad
import W5_closed_form as W5


def P_eval(coeffs, t):
    return sum(c * t ** k for k, c in enumerate(coeffs))


def run(seed, T, kmax=3):
    rng = np.random.default_rng(seed)
    basis = W5.basis_coeffs(T, kmax=kmax)
    coeffs = sum(rng.standard_normal() * b for b in basis)
    P = lambda t: P_eval(coeffs, t)
    print(f"--- T={T}  seed={seed} ---")

    worst = 0.0
    for c in [0.5, -0.5, 0.123, -1.9]:
        exact = W5.real_moment_integral(coeffs, T, c)
        numint = quad(lambda t: P(t) * math.exp(c * t), -T, T, limit=800)[0]
        worst = max(worst, abs(exact - numint))
    print(f"  real_moment_integral max|diff| over 4 c values: {worst:.3e}")

    worst = 0.0
    for tau in [1e-6, 1e-3, 1e-2, 0.049, 0.05, 0.051, 0.3, 1.3, 5.7, 23.4, 137.0]:
        z = W5.fourier_moment_integral(coeffs, T, np.array([tau]))[0]
        re = quad(lambda t: P(t) * math.cos(tau * t), -T, T, limit=1200)[0]
        im = quad(lambda t: P(t) * math.sin(tau * t), -T, T, limit=1200)[0]
        worst = max(worst, abs(z - complex(re, im)))
    print(f"  fourier_moment_integral max|diff| over tau incl. small: {worst:.3e}")

    worst = 0.0
    for a in [0.0, 0.11, 0.3, 1.5, 2 * T - 0.01, 2 * T, 2 * T + 1.0]:
        exact = W5.autocorr(coeffs, T, a)

        def integrand(t, a=a):
            if -T < t < T and -T < t + a < T:
                return P(t) * P(t + a)
            return 0.0

        numint = quad(integrand, -T, T, limit=1200)[0]
        worst = max(worst, abs(exact - numint))
    print(f"  autocorr max|diff| over several a (incl. a>=2T): {worst:.3e}")

    exact = W5.l2_norm_sq(coeffs, T)
    numint = quad(lambda t: P(t) ** 2, -T, T, limit=800)[0]
    print(f"  l2_norm_sq diff: {abs(exact - numint):.3e}")

    tv_quad = W5.total_variation(coeffs, T)
    ts = np.linspace(-T, T, 4_000_001)
    Pvec = np.polyval(coeffs[::-1], ts)
    tv_grid = np.sum(np.abs(np.diff(Pvec)))
    print(f"  total_variation: closed(quad)={tv_quad:.8f}  fine-grid={tv_grid:.8f}  "
          f"diff={abs(tv_quad-tv_grid):.3e}")

    # smoothness check: F and F' vanish at +-T (continuity of value+slope
    # with the zero extension), F'' need not.
    eps = 1e-6
    for k, lbl in [(0, "F"), (1, "F'")]:
        dc = coeffs.copy()
        for _ in range(k):
            dc = np.array([dc[j] * j for j in range(1, len(dc))]) if len(dc) > 1 else np.array([0.0])
        val = P_eval(dc, T - eps) if len(dc) else 0.0
        print(f"  {lbl}(T-eps) = {val:.3e}  (should be ~0 for k<=1: C^2 bump)")


if __name__ == "__main__":
    for T in (0.6, 1.2, 2.0, 3.0):
        run(seed=1, T=T)
    print("\nAll checks above should show diffs at the 1e-9..1e-13 level "
          "(limited by scipy.quad's own tolerance / float64), confirming the "
          "closed-form formulas in W5_closed_form.py.")
