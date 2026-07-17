# E73.130 Results - Vector-Swap Source of CSV

Date: 2026-07-12.

Script:

```text
E73_130_vector_swap_csv_probe.py
```

Purpose:

Separate the CSV cancellation into:

```text
C_zeta(-gamma) = <xi_zeta,k_gamma>,
C_arch(-gamma) = <xi_arch,k_gamma>,
C_delta(-gamma) = <xi_zeta-xi_arch,k_gamma>.
```

Output:

```text
E73.130 vector-swap CSV probe
Compares C_zeta, C_arch, and C_delta= C_zeta-C_arch from vector change.
 lam     L gamma      zetaB    archB   deltaB  z/a angle
  16   5.545   14.13   -19.995   -1.372   -1.372 -18.62 -19.027
  16   5.545   21.02   -19.338   -0.326   -0.326 -19.01 -19.417
  20   5.991   14.13   -18.960   -1.838   -1.838 -17.12 -17.510
  20   5.991   21.02   -19.690   -0.195   -0.195 -19.49 -19.882
  24   6.356   14.13   -17.817   -1.116   -1.116 -16.70 -17.076
  24   6.356   21.02   -21.992   -0.475   -0.475 -21.52 -21.892
  28   6.664   14.13   -20.760    1.215    1.215 -21.97 -22.340
  28   6.664   21.02   -17.254   -0.546   -0.546 -16.71 -17.074
  32   6.931   14.13   -19.617   -2.145   -2.145 -17.47 -17.831
  32   6.931   21.02   -18.831   -0.848   -0.848 -17.98 -18.341
```

## Reading

`C_arch` is not small.  `C_delta` has essentially the same size as
`C_arch`.  The zeta value is small because

```text
C_arch + C_delta
```

cancels to very high order.

The cancellation ratio

```text
|C_zeta|/(|C_arch|+|C_delta|)
```

is typically `L^-17` to `L^-22`.

Therefore CSV is a first-order eigenvector perturbation cancellation:

```text
xi_zeta = xi_arch + delta xi,
<xi_arch,k_gamma> + <delta xi,k_gamma> ~= 0.
```

## Consequence

The next viable identity is not a property of the final vector alone.  It
is a perturbative identity comparing the arch/free ground vector to the
zeta-coupled ground vector:

```text
delta xi
 =
 - (A_arch-mu_arch)^{-1}_{perp}
   (Prime - delta_mu) xi_arch
 + higher orders.
```

CSV becomes the scalar cancellation

```text
<xi_arch,k_gamma>
 =
 <(A_arch-mu_arch)^{-1}_{perp} Prime xi_arch,k_gamma>
 + controlled remainder.
```

This is now a concrete finite Feshbach/resolvent identity, and it is
arithmetically nontrivial because the prime perturbation is absent in the
arch/free model.

