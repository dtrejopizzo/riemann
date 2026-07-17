# E72.371 Results - Full-row ladder consistency

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_371_full_row_ladder_probe.py
```

## Output

```text
E72.371 full-row ladder probe
Uses h_actual as coupled operator and mu as scalar proxy.
 lam   N roots node     fullDef     redDef      couplingErr  opRowAmp
  6.0  10     2  root  2.3647e-15  1.7883e-15   1.7078e-16  3.301e-17
  6.0  10     2 shift  3.5010e+00  3.5010e+00   7.3277e-16  2.484e-16
  8.0  12     3  root  1.3728e-11  1.3728e-11   4.1309e-16  3.224e-17
  8.0  12     3 shift  2.3125e+01  2.3125e+01   2.2849e-15  1.160e-16
 10.0  14     3  root  1.3408e-11  1.3406e-11   5.1785e-16  4.491e-17
 10.0  14     3 shift  2.3773e+01  2.3773e+01   2.6224e-15  3.523e-16
 12.0  16     3  root  8.6768e-14  8.8040e-14   2.8889e-15  3.024e-15
 12.0  16     3 shift  2.0958e+01  2.0958e+01   1.4125e-14  1.323e-14
```

## Reading

The ladder identity passes:

```text
fullDef = reducedDef + roundoff,
couplingErr = roundoff.
```

The check uses the coupled finite operator `h_actual` and its lowest eigenvalue `mu` as a scalar
proxy.  Therefore

```text
R_full xi - R_reduced xi
= k_z (h_actual-mu I) xi,
```

and the observed `opRowAmp` is machine-scale.

For Weyl-root windows the defect is machine-scale or truncation-scale.  For shifted controls the
defect is large, while the coupling error remains roundoff.  Thus the build distinguishes the
structural eigen-equation identity from the actual CFIR/divisor obstruction.

## Status

```text
validated: coupled-vs-reduced row pipeline has the correct algebraic normalization;
validated: shifted windows still fail after the coupled row is used;
not yet proved: primitive split into W02/WR/Prime/kappa/e_pole rows;
not yet proved: finite Xi-specific CFIR identity from the primitive Feshbach-Weil formula.
```

This result removes a normalization/sign failure from the list of possible obstructions.  It does
not close FINITE-CFIR, because the probe still uses `h_actual` as a combined operator rather than
building the primitive rows separately.
