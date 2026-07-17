# E73.073 results - paired packet probe

## 1. Purpose

E73.073 tests the paired packet

```text
Pair_z^infty(w)=M_z^infty(w)+M_z^infty(-w).
```

The goal is not to prove the final estimate, but to check whether pairing creates a visible
cancellation at critical zero heights.

## 2. Representative output

```text
E73.073 paired packet probe
Verifies Pair_z(w)=M_z(w)+M_z(-w) and reports pairing gain.
 lam     L   zIm    wIm       absErr    |pair|/max(|M|)      |pair|
  16   5.545  14.13   14.13    2.826e-15         1.506e-14   9.678e-15
  16   5.545  14.13   21.02    3.351e-15         3.505e-14   7.819e-16
  16   5.545  14.13   25.01    2.368e-15         4.869e-10   7.350e-12
  20   5.991  14.13   14.13    1.291e-14         4.441e-15   2.722e-14
  20   5.991  21.02   21.02    4.928e-16         3.553e-14   7.679e-15
  24   6.356  14.13   21.02    2.306e-16         5.342e-13   1.170e-15
  24   6.356  21.02   25.01    5.863e-15         9.072e-15   9.233e-16
```

## 3. Diagnosis

The paired packet is much smaller than the individual one-sided Mellin packets at the tested critical
heights:

```text
|Pair|/max(|M(w)|,|M(-w)|) = 1e-9 to 1e-14.
```

The absolute quadrature error is at the same numerical scale, so relative errors are not the right
diagnostic near zero.

## 4. Status

```text
observed: strong paired cancellation at critical heights;
not enough: this alone does not identify the divisor;
next: test Pair_z^infty(w) against the finite Cauchy divisor H_0(w).
```
