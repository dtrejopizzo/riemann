# E71.3 -- convergence-rate/PNT diagnostic results

**Date:** 2026-07-07.
**Script:** `E71_3_convergence_rate_pnt.py`.

## Fixed `lambda=5` scan

For true zeta, the first five target zeros repeatedly lock to the CCM roots at approximately
`1e-7` accuracy, but the lock is not monotone in `N`.

```text
N=10: maxerr(first5) = 1.880034e+01
N=14: maxerr(first5) = 7.924204e+00
N=18: maxerr(first5) = 4.198547e-07
N=20: maxerr(first5) = 2.510186e+00
N=24: maxerr(first5) = 2.510186e+00
N=30: maxerr(first5) = 5.414018e+00
N=36: maxerr(first5) = 4.059887e+00
N=40: maxerr(first5) = 4.198545e-07
```

Reading: fixed-`lambda` finite sections alias. The right convergence statement is not monotone
eigenvalue error in `N`, but finite-section resolvent convergence plus stable Riesz projections.

## Planted off-line scan

With a planted off-line zero at `g0=25`, `b=0.30`, the same scan stabilizes at a nonzero floor:

```text
N=18: maxerr(first5) = 5.785449e-01
N=20: maxerr(first5) = 4.119736e-01
N=24: maxerr(first5) = 3.403309e-01
N=30: maxerr(first5) = 3.133984e-01
N=36: maxerr(first5) = 3.095154e-01
N=40: maxerr(first5) = 3.085805e-01
```

This confirms E71.2 at finer resolution: the off-line perturbation does not become a complex
eigenvalue, but it creates a stable convergence floor.

## Small `lambda` horizon scan

Using a crude automatic `N` choice to cover the first five zeros:

```text
lambda=3.00: consecutive<1e-5 = 0, maxerr = 6.057072e+00
lambda=3.70: consecutive<1e-5 = 0, maxerr = 4.577067e+00
lambda=5.00: consecutive<1e-5 = 5, maxerr = 4.198543e-07
lambda=7.00: consecutive<1e-5 = 3, maxerr = 2.510186e+00
```

This scan is not yet a clean monotone horizon law. It is sensitive to the pole mesh, the matching rule,
and the chosen finite section. Therefore it should be read only as a diagnostic.

## Conclusion

E71.3 supports three points:

1. The zeta case has real finite-section locks to the target zeros.
2. The planted off-line case preserves a nonzero error floor.
3. A proof cannot be a naive PNT-counting estimate; it must be a resolvent/Riesz-projection theorem
   that controls finite-section aliasing.

The exact remaining theorem is the one stated in `E71_3_RESOLVENT_CONVERGENCE_RATE.md`:

```text
zero-independent CCM resolvent convergence
  => sp(H_lambda) converges to zeta zeros
  => RH, because H_lambda is self-adjoint.
```
