# E72.367 results - scalar consistency energy

Command:

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_367_scalar_energy_probe.py
```

The probe evaluates the finite energy identity

```text
<k,KWin k> - <k,t> = Lambda_L ||k||^2
```

using `mu` as a visible scalar proxy.  The theorem uses

```text
Lambda_L=mu+e_pole-2kappa_*.
```

So this is not the final scalar-consistency test; it validates the energy decomposition and relative
sizes.

## Table

```text
lam   N roots node     ||k||       |<k,Kk>|    |<k,t>|     |lambda_win|  |def_mu|    scalarNorm tail/win
 6.0  10     2 root        nan          nan        nan          nan        nan        nan      nan
 6.0  10     2 shift  1.257e+00    4.362e+00  2.465e-03    2.761e+00  4.360e+00  3.470e+00 5.65e-04

 8.0  12     3 root   3.098e-12    4.212e-23  9.909e-27    4.391e+00  4.213e-23  1.360e-11 2.35e-04
 8.0  12     3 shift  5.023e+00    1.137e+02  6.082e-02    4.504e+00  1.137e+02  2.263e+01 5.35e-04

10.0  14     3 root   2.978e-12    3.970e-23  4.829e-26    4.469e+00  3.965e-23  1.331e-11 1.22e-03
10.0  14     3 shift  4.927e+00    1.138e+02  1.277e-01    4.684e+00  1.137e+02  2.308e+01 1.12e-03

12.0  16     3 root   1.832e-14    1.634e-27  3.568e-29    4.766e+00  1.599e-27  8.729e-14 2.18e-02
12.0  16     3 shift  4.349e+00    8.214e+01  9.038e-02    4.345e+00  8.217e+01  1.890e+01 1.10e-03
```

## Reading

For shifted controls, the scalar energy is dominated by the window kernel:

```text
|<k,t>| / |<k,KWin k>| ~= 1e-3.
```

Thus `SCALAR-CONS` cannot be explained by the signed finite tail alone.  It must be an energy identity
for the actual Xi-window residue vector against `KWin`, with the Feshbach left coefficient
`Lambda_L`.

The root rows are not load-bearing because `||k||` is tiny by finite Weyl-root construction.

## Consequence

The remaining scalar gate is now the explicit quadratic identity:

```text
<J_TG_x, KWin J_TG_x>
- <J_TG_x, J_TTail_T^M>
- Lambda_L ||J_TG_x||^2
= O_T(L^B||J_TG_x||).
```

Together with the projective gate, this is exactly the finite Hermite CFIR equation.
