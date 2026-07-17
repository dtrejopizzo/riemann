# E72.369 results - energy operator audit

Command:

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_369_energy_operator_probe.py
```

The probe expands

```text
E_CFIR=||A k+t||^2,       A=Lambda I-KWin,
```

using `mu` as scalar proxy.  It compares the actual residual energy with the incoherent bound

```text
(||Ak||+||t||)^2.
```

## Table

```text
lam   N roots node    ||A||      smin(A)    ||Ak||     ||t||      energy     incohBd    ratio
 6.0  10     2 root   3.62e+00  3.20e+00  4.81e-16  1.10e-15  2.420e-30  2.492e-30 9.71e-01
 6.0  10     2 shift  3.49e+00  2.61e+00  3.50e+00  5.53e-03  1.226e+01  1.230e+01 9.96e-01

 8.0  12     3 root   5.49e+00  3.57e+00  1.37e-11  3.76e-15  1.884e-22  1.884e-22 1.00e+00
 8.0  12     3 shift  8.14e+00  3.53e+00  2.31e+01  2.53e-02  5.348e+02  5.363e+02 9.97e-01

10.0  14     3 root   6.20e+00  3.35e+00  1.34e-11  1.80e-14  1.797e-22  1.806e-22 9.95e-01
10.0  14     3 shift  9.02e+00  2.72e+00  2.38e+01  5.11e-02  5.652e+02  5.683e+02 9.94e-01

12.0  16     3 root   5.72e+00  4.22e+00  8.99e-14  2.33e-15  7.732e-27  8.510e-27 9.09e-01
12.0  16     3 shift  9.23e+00  4.11e+00  2.10e+01  4.49e-02  4.392e+02  4.408e+02 9.96e-01
```

## Reading

The incoherent bound is essentially sharp in shifted controls:

```text
energy / incohBd ~= 0.99.
```

That means no useful cancellation is visible after separating `Ak` and `t`.  The signed tail is much
smaller than `Ak`, so it cannot repair generic shifted windows.

Thus an analytic proof cannot proceed by:

```text
bound ||A||, bound ||k||, bound ||t||.
```

It must prove the coupled residual identity before norming:

```text
A_L k+t=O_T(L^B).
```

## Consequence

`ENERGY-CFIR` is a clean certificate, but not a source of cancellation.  The next theorem must expose
why the actual Xi-window vector `k=J_TG_x` satisfies the coupled residual equation.  This returns the
load-bearing work to the finite explicit-formula/Feshbach identity, not to spectral positivity of
`A_L^*A_L`.
