#!/usr/bin/env python3
"""
108_50 verifier.

Numpy-only checks supporting 108_50_STAGE_5_NO_COMPARISON_MAP_AT_GENERATOR_LEVEL.md.

(i)   Lemma 1.1 mechanism: an eigenfunction defined on [1,2] under a dilation
      character, extended across an unbounded orbit lambda = 2^n, stays
      nonzero at every stage -> its support cannot be compact.
(ii)  Fact 2.1: the Mellin transform of the indicator of [1,2],
      fhat(s) = (1 - 2^{-s})/s, has zeros exactly at s = 2 pi i k / log 2,
      k in Z \\ {0}.  Checked for k = 1..1000.
(iii) fhat(0) = log 2, cross-checked against a direct Riemann-sum quadrature
      of the defining integral.

Exit 0 iff every check passes.
"""

import numpy as np


def fhat(s, a=1.0, b=2.0):
    """Mellin transform of the indicator of [a,b] at (possibly array) s,
    handling the removable singularity at s = 0 by the closed form
    int_a^b x^{-s-1} dx = (a^{-s} - b^{-s})/s  (s != 0),  log(b/a) (s = 0)."""
    s = np.asarray(s, dtype=complex)
    out = np.empty_like(s)
    zero_mask = np.abs(s) < 1e-300
    nz = ~zero_mask
    out[nz] = (a ** (-s[nz]) - b ** (-s[nz])) / s[nz]
    out[zero_mask] = np.log(b / a)
    return out


def check_lemma_mechanism():
    print("=== (i) Lemma 1.1 mechanism: unbounded orbit stays nonzero ===")
    s = 0.3 + 0.5j  # covariance exponent for the toy eigenfunction
    f0 = 1.0 + 0.0j  # f(x) = 1 for x in [1,2] (base value at x=1, say)
    all_nonzero = True
    for n in range(0, 31):
        lam = 2.0 ** n
        # f(lam * x0) = chi(lam) * f(x0), chi(lam) = lam^{-s}
        val = (lam ** (-s)) * f0
        mag = abs(val)
        ok = mag > 0.0
        all_nonzero = all_nonzero and ok
        if n in (0, 5, 10, 20, 30):
            print(f"  n={n:2d}  lambda=2^{n}={lam:.3e}  "
                  f"|f(lambda*x0)|={mag:.6e}  nonzero={ok}")
    print(f"  all 31 extended values nonzero: {all_nonzero}")
    assert all_nonzero, "eigenfunction extension unexpectedly vanished"
    print("  -> the orbit {lambda * x0 : lambda = 2^n, n=0..30} is entirely")
    print("     in the support; since this orbit is unbounded, no compactly")
    print("     supported f can satisfy the eigen-relation (Lemma 1.1).")
    return True


def check_mellin_zeros(kmax=1000):
    print("\n=== (ii) Fact 2.1: zeros of fhat at s = 2 pi i k / log 2 ===")
    ks = np.arange(1, kmax + 1)
    s_vals = 1j * 2.0 * np.pi * ks / np.log(2.0)
    vals = fhat(s_vals)
    max_abs = np.max(np.abs(vals))
    print(f"  tested k = 1..{kmax}")
    print(f"  max |fhat(2 pi i k / log 2)| over all k = {max_abs:.3e}")
    ok = max_abs < 1e-9
    assert ok, "Mellin-transform zero formula failed floating-point check"
    print(f"  all below floating-point tolerance 1e-9: {ok}")
    print("  -> exact zero by the algebraic identity 2^{-s} = e^{-2 pi i k} = 1;")
    print("     since k ranges over an infinite index set, fhat has infinitely")
    print("     many zeros (Theorem 2.2's premise).")
    return True


def check_fhat_at_zero():
    print("\n=== (iii) fhat(0) = log 2, cross-checked by quadrature ===")
    closed_form = fhat(np.array([0.0]))[0]
    log2 = np.log(2.0)
    print(f"  closed form fhat(0)            = {closed_form.real:.10f}")
    print(f"  log 2                          = {log2:.10f}")
    assert abs(closed_form.real - log2) < 1e-12
    assert abs(closed_form.imag) < 1e-12

    # direct Riemann-sum quadrature of int_1^2 x^{-0-1} dx = int_1^2 x^{-1} dx
    n = 2_000_000
    x = np.linspace(1.0, 2.0, n + 1)
    y = 1.0 / x
    quad = np.trapezoid(y, x) if hasattr(np, "trapezoid") else np.trapz(y, x)
    print(f"  Riemann-sum quadrature (n={n}) = {quad:.10f}")
    assert abs(quad - log2) < 1e-6
    print("  closed form, exact log 2, and quadrature agree.")
    return True


def main():
    ok1 = check_lemma_mechanism()
    ok2 = check_mellin_zeros()
    ok3 = check_fhat_at_zero()
    assert ok1 and ok2 and ok3
    print("\nVERDICT: all checks passed -- Lemma 1.1's mechanism and Fact 2.1's "
          "exact zero formula are both confirmed numerically; the written "
          "proofs of Theorem 1.2, Theorem 2.2 and Theorem 3 in "
          "108_50 are unaffected by (and independent of) this script.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
