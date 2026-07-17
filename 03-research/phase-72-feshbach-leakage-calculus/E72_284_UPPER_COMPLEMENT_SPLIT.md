# E72.284 -- Upper complement split

**Purpose.** Reduce the upper complement bound needed by E72.283 to two explicit size estimates.

The corrected pole-even complement is

```text
C_actual = B_even^T(H_actual-e_pole I)B_even.
```

Since

```text
H_actual = H_model - prime part,
```

we have the exact split

```text
C_actual = C_model + Delta_arith,
Delta_arith = C_actual-C_model.
```

Therefore

```text
||C_actual||
<= ||C_model|| + lambda_max(Delta_arith)_+.                  (UCS)
```

This is better than bounding `||Delta_arith||`: the negative arithmetic directions lower the operator
ceiling and are harmless for the upper complement estimate.

## Sufficient upper-complement theorem

The upper complement bound

```text
||C_actual|| = O(L^2)
```

follows from:

```text
MUCB:  ||C_model|| = O(L^2),
APCB:  lambda_max(Delta_arith)_+ = O(L^2).
```

`MUCB` is a model/archimedean size theorem.  `APCB` is an arithmetic positive-part ceiling.  This is not
the same as `RFBD`, which controls the negative part of the model-normalized arithmetic perturbation.
It is also not the too-strong absolute bound `||Delta_arith||` in the model norm.

## Probe

Run:

```text
python3 E72_284_upper_complement_split_probe.py
```

Output:

```text
E72.284 upper-complement split probe
C_actual=C_model+Delta_arith in the corrected pole-even complement.
op(C_actual) <= op(C_model)+lambda_max(Delta_arith)_+.
lam L dim opA/L2 opM/L2 posDelta/L2 absDelta/L2 minA/L2 minM/L2 dMin/L2 dMax/L2
 16 5.545177  41 6.122293e-01 9.865376e-01 1.617975e-01 5.841092e-01 4.008406e-01 3.371033e-01 -5.841092e-01 1.617975e-01
 20 5.991465  49 6.451008e-01 1.069877e+00 1.530683e-01 6.240223e-01 4.446259e-01 3.855733e-01 -6.240223e-01 1.530683e-01
 24 6.356108  57 6.730699e-01 1.150110e+00 1.428683e-01 6.624494e-01 4.865207e-01 4.308218e-01 -6.624494e-01 1.428683e-01
 28 6.664409  65 7.008396e-01 1.227395e+00 1.406409e-01 6.999850e-01 5.266809e-01 4.735465e-01 -6.999850e-01 1.406409e-01
 32 6.931472  73 7.391787e-01 1.302030e+00 1.327397e-01 7.356424e-01 5.653143e-01 5.142315e-01 -7.356424e-01 1.327397e-01
```

## Reading

The observed split is favorable:

```text
||C_model||/L^2          ~ 1.0--1.3,
lambda_max(Delta)_+/L^2 ~ 0.13--0.16,
||C_actual||/L^2        ~ 0.61--0.74.
```

The negative arithmetic part is larger in absolute value, but it lowers the top of `C_actual`; it should
not be charged against the upper complement bound.

Thus E72.283's remaining upper-complement input is reduced to the two concrete estimates `MUCB` and
`APCB`.  The next proof-facing target is `APCB`, the positive-part arithmetic ceiling.
