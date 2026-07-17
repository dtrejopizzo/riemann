# E73.132 Results - Critical Evaluation Penalty Kernel Probe

Date: 2026-07-12.

Script:

```text
E73_132_eval_penalty_kernel_probe.py
```

Purpose:

Test whether the zeta-coupled ground vector already lies close to the
kernel of the critical evaluation rows.  Define the normalized Cauchy row

```text
k_gamma(d_n)=1/(-gamma-d_n),
K_gamma = k_gamma / ||k_gamma||.
```

Let `K` contain the first three critical rows.  The probe compares the
ground vector of `H` to the ground vector of

```text
H_rho = H + rho K^T K.
```

If `xi_zeta` already lies near `ker K`, then adding this penalty should
produce a tiny energy shift and small evaluation leak.

Output:

```text
E73.132 critical evaluation penalty kernel probe
Adds rho*K^T K for normalized critical Cauchy rows K.
Small shift/overlap loss means xi_zeta already lies near ker K.
 lam     L rho      leakXiB leakEtaB  shiftB overlapLossB
  16   5.545 1.0e-06  -13.639  -13.589 -20.328       -1.649
  16   5.545 1.0e-03  -13.639  -13.598 -20.574       -1.544
  16   5.545 1.0e+00  -13.639  -15.303 -20.278       -1.564
  20   5.991 1.0e-06  -18.888  -19.612 -19.261       -0.961
  20   5.991 1.0e-03  -18.888  -19.416 -19.410       -0.971
  20   5.991 1.0e+00  -18.888  -19.571 -19.457       -0.972
  24   6.356 1.0e-06  -18.567  -18.906 -19.898       -0.284
  24   6.356 1.0e-03  -18.567  -18.467 -18.648       -1.111
  24   6.356 1.0e+00  -18.567  -18.555 -18.441       -1.730
  28   6.664 1.0e-06  -17.976  -17.980 -18.560       -2.838
  28   6.664 1.0e-03  -17.976  -18.006 -18.309       -3.161
  28   6.664 1.0e+00  -17.976  -18.297 -17.499       -1.010
```

## Reading

For `lambda>=20`, the normalized critical evaluation leak is already

```text
||K xi_zeta|| ~= L^-18.
```

Adding a penalty as large as `rho=1` does not reveal a hidden large
evaluation component.  The penalized vector remains in the same tiny
evaluation channel.

`lambda=16` is weaker:

```text
||K xi_zeta|| ~= L^-13.6,
```

which is consistent with treating `lambda=16` as a finite base case rather
than part of the asymptotic theorem.

## Consequence

This supports the variational form of Characteristic CSV:

```text
Critical Evaluation Kernel Theorem:
For all sufficiently large L,
the zeta-coupled ground vector xi_L satisfies

||K_L xi_L|| <= C L^-18
```

for the normalized critical evaluation matrix `K_L`.

Since

```text
|C_x(-gamma)| <= ||k_gamma|| * ||K_L xi_L||,
```

this gives CSV once the row norm `||k_gamma||` is controlled by an
elementary mesh bound.

