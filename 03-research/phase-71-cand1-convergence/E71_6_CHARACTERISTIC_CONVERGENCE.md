# E71.6 -- characteristic-function convergence probe

**Date:** 2026-07-07.
**Script:** `E71_6_characteristic_convergence_probe.py`.
**Role:** begin testing the Hurwitz closure target from E71.5 at the function level.

## Natural CCM entire function

From the rational model

```text
f_N(s) = sum_k xi_k/(s-d_k),        d_k = 2*pi*k/L,
```

the natural entire function is

```text
Phi_N(s) = (2/sqrt(L)) sin(sL/2) f_N(s).
```

The sine factor cancels the poles at `d_k`. The zeros of `Phi_N` include the finite CCM spectral
roots, and the finite spectral roots are real because the CCM operator is self-adjoint.

E71.5 says that the decisive theorem is:

```text
c_{lambda,N} Phi_{lambda,N}(s) -> Xi(s)
```

locally uniformly, for a canonical nonzero normalization `c_{lambda,N}`.

## Diagnostic only

The script fits a single scalar `c` against `Xi` on a real grid and reports relative errors. This is
not a proof and not an allowed final normalization, because it uses the target function to fit `c`.

It answers only this question:

```text
does zero locking visibly come with function-level convergence?
```

If no, then the Hurwitz theorem remains the right closure theorem, but the natural normalization is
more subtle than a scalar least-squares fit on the real axis.

## Result

The first probe fails for the raw `Phi_N`: after the best scalar least-squares fit on `[0,42]`, the
relative error remains essentially `1`. Results are recorded in `E71_6_RESULTS.md`.

Thus zero locking is not the same as function-level convergence of this raw normalization.

## Closure target after E71.6

The real theorem must supply:

1. a canonical normalization of `Phi_{lambda,N}`;
2. locally uniform bounds on compact subsets of `C`;
3. convergence to `Xi` from the CCM Euler/Gamma construction, not from known zeros.

Then E71.5 closes `Omega_7` by Hurwitz.

After the E71.6 probe, item 1 is the active issue: the correct object is likely a genuine
Fredholm/characteristic determinant or de Branges normalization, not the raw ground-vector numerator.
