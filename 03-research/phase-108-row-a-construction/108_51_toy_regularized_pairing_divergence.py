#!/usr/bin/env python3
"""
108_51 verifier.

Numpy-only checks supporting 108_51's Proposition 3.1: the toy regularized
pairing Q(T) = lambda1*P(T;s1) + lambda2*P(T;s2), with s1=0.3, s2=0.7,
lambda1=1, lambda2=-1 (mass zero), diverges to -infinity as T -> infinity,
with leading exponent s2 = 0.7.

This is a MODEL computation illustrating that a naive cutoff-and-limit
comparison does not converge for free; it is explicitly not a claim about
Stage 0's actual corner pairing I_partial, whose definition is outside the
read scope of this note (see 108_50 Scope, 108_51 Scope).
"""

import numpy as np


def P(T, a):
    """Closed form of int_{1/T}^{T} x^{a-1} dx."""
    T = np.asarray(T, dtype=float)
    if abs(a) < 1e-300:
        return 2.0 * np.log(T)
    return (T ** a - T ** (-a)) / a


def P_quadrature(T, a, n=2_000_000):
    """Direct Riemann-sum quadrature of int_{1/T}^{T} x^{a-1} dx, for
    cross-checking the closed form at moderate T."""
    x = np.linspace(1.0 / T, T, n + 1)
    y = x ** (a - 1.0)
    return np.trapezoid(y, x) if hasattr(np, "trapezoid") else np.trapz(y, x)


def check_closed_form_vs_quadrature():
    print("=== closed form vs direct quadrature, moderate T ===")
    ok = True
    for T in (10.0, 100.0, 1000.0):
        for a in (0.3, 0.7):
            cf = P(T, a)
            q = P_quadrature(T, a)
            rel = abs(cf - q) / abs(cf)
            print(f"  T={T:8.1f} a={a}  closed_form={cf:.6f}  "
                  f"quadrature={q:.6f}  rel.err={rel:.2e}")
            ok = ok and (rel < 1e-3)
    assert ok, "closed form does not match direct quadrature"
    print(f"  closed form confirmed against quadrature: {ok}")
    return ok


def check_divergence():
    print("\n=== Q(T) = P(T;0.3) - P(T;0.7), mass-zero pair, T -> infinity ===")
    s1, s2 = 0.3, 0.7
    lam1, lam2 = 1.0, -1.0
    assert abs(lam1 + lam2) < 1e-15, "mass-zero condition must hold"

    Ts = np.array([10.0, 1e2, 1e3, 1e4, 1e6, 1e8, 1e10, 1e12])
    Qs = lam1 * P(Ts, s1) + lam2 * P(Ts, s2)
    for T, Q in zip(Ts, Qs):
        print(f"  T={T:.1e}   Q(T)={Q:.6e}")

    # Q(T) should be strictly decreasing (more negative) as T grows, and
    # unbounded below on the tested range -- the actual property claimed
    # by Proposition 3.1, not an arbitrary threshold.
    strictly_decreasing = np.all(np.diff(Qs) < 0)
    unbounded_below = Qs[-1] < 10 * Qs[0]  # grows in magnitude, not just sign
    print(f"  strictly decreasing over the scan: {strictly_decreasing}")
    print(f"  |Q(T_max)| >> |Q(T_min)|:          {unbounded_below}  "
          f"(Q(T_min)={Qs[0]:.3e}, Q(T_max)={Qs[-1]:.3e})")
    assert strictly_decreasing
    assert unbounded_below

    # leading exponent should match s2 = 0.7: for large T,
    # Q(T) ~ -(1/s2) T^{s2}, so log(-Q(T)) ~ s2 * log(T) - log(s2).
    logT = np.log(Ts[-4:])  # use the large-T tail only
    logmQ = np.log(-Qs[-4:])
    slope = np.polyfit(logT, logmQ, 1)[0]
    print(f"  log-log slope of -Q(T) vs T (large-T tail): {slope:.6f}  "
          f"(expected s2 = {s2})")
    assert abs(slope - s2) < 1e-3
    return True


def main():
    ok1 = check_closed_form_vs_quadrature()
    ok2 = check_divergence()
    assert ok1 and ok2
    print("\nVERDICT: the toy regularized pairing Q(T) on a mass-zero pair "
          "diverges as T -> infinity with leading exponent s2, confirming "
          "Proposition 3.1; this is a model computation, not a statement "
          "about Stage 0's actual I_partial.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
