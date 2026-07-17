# E71.8 -- canonical-product determinant probe results

**Date:** 2026-07-07.
**Script:** `E71_8_canonical_product_probe.py`.

## Output

The test compared the canonical all-root product with a cheating locked-root product on `[0,12]`,
below the first zeta zero.

```text
grid: [0,12.0] below first zero, hmax=55
   N  #roots #locked     all_relL2    all_relSup    lock_relL2   lock_relSup
  18      11       5  9.062859e+00  2.551887e+01  2.980388e-01  2.541996e-01
  40      20       5  1.318981e+00  1.304684e+00  2.980388e-01  2.541996e-01
```

At `N=18`, the positive roots begin with

```text
1.3303, 3.6690, 6.3097, 8.1575, 11.1139, 14.1347, ...
```

At `N=40`, they begin with

```text
2.1756, 4.5757, 10.4222, 12.8360, 14.1347, ...
```

Thus the finite CCM spectrum contains background roots below the first zeta zero. These roots dominate
the all-root canonical product and prevent direct convergence to `Xi(t)/Xi(0)`.

## Reading

The raw spectral product

```text
product_{r in sp_+(H_N)} (1 - t^2/r^2)
```

is not the desired determinant.

The cheating locked-root product, using only roots within `1e-3` of the first five known zeta zeros,
is much closer but still not exact because it omits the remaining zeta zeros above the cutoff. More
importantly, it is forbidden as a proof object because it uses the target zeros.

## Consequence

The determinant needed for E71.5 must be relative:

```text
D_N^{rel}(t) = D_N^{all}(t) / B_N(t),
```

where `B_N` is a canonical background determinant built from the CCM pole mesh/window and not from zeta
zeros.

The next task is to identify `B_N`.

## Audit status

This result is consistent with the NO-GO audit:

- not a positivity wall;
- not a Stone/unitarity claim;
- not a proof;
- a sharper localization of the convergence problem.

The CAND-1 path now lives or dies on the existence of a **zero-independent background determinant**
for CCM finite sections.
