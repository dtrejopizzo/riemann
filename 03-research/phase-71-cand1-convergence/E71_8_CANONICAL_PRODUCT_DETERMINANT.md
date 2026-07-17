# E71.8 -- canonical-product determinant probe

**Date:** 2026-07-07.
**Script:** `E71_8_canonical_product_probe.py`.
**Role:** test the next determinant candidate after the raw sine-comb normalization failed in E71.6.

## Candidate

For a finite self-adjoint CCM operator, the most natural real-rooted characteristic object is the
finite canonical product

```text
D_N(t) = product_{r>0, r in sp(H_N)} (1 - t^2/r^2).
```

It is normalized by

```text
D_N(0)=1,
```

matching the standard even product normalization

```text
Xi(t)/Xi(0) = product_gamma (1 - t^2/gamma^2).
```

## Why this is better than E71.6

E71.6 used the raw entire numerator

```text
(2/sqrt(L)) sin(sL/2) sum_k xi_k/(s-d_k),
```

which carries the pole-cancelling sine comb and did not converge to `Xi` under a scalar fit.

The canonical product strips the problem down to the finite real spectrum itself.

## Diagnostic split

The script compares two products:

1. **all-roots product:** uses every positive finite CCM root up to a cutoff. This is canonical but
   includes finite-section background roots.
2. **locked-roots product:** uses only roots lying in `1e-3` windows around known zeta zeros. This is
   not allowed in a proof; it is only a diagnostic control.

If all-roots fails while locked-roots behaves better, then the missing object is not ordinary spectral
product convergence. It is a **relative determinant** that cancels the finite-section background
spectrum without using known zero locations.

## Result

The all-roots product fails because finite CCM spectra contain background roots below the first zeta
zero. Results are recorded in `E71_8_RESULTS.md`.

Thus the next object must be a relative determinant

```text
D_N^{rel}(t) = D_N^{all}(t) / B_N(t),
```

where `B_N` is a canonical background factor native to the CCM pole mesh/window.

## Closure interpretation

The final CAND-1 theorem must produce a determinant-like function

```text
D_{lambda,N}^{rel}(t)
```

such that:

1. its zeros are real because it is built from finite self-adjoint CCM data;
2. it is normalized canonically, not by fitting to `Xi`;
3. it cancels background roots/poles as part of the CCM construction;
4. it converges locally uniformly to `Xi(t)/Xi(0)`.

Then E71.5 Hurwitz closes `Omega_7`.

## Risk from the NO-GO list

The cancellation of background roots must not be:

- Cholesky/spectral factorization of a positive form (MW-1);
- a boundary condition fitted from zeta zeros (Phase 53 / Berry-Keating);
- a KMS partition normalization by `zeta` (MW-5);
- an `epsilon_0>0` renormalization (Phase 60 tribunal: RH-circular).

It must be a relative determinant native to the finite CCM construction.
