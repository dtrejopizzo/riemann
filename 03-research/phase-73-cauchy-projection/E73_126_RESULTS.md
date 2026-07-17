# E73.126 Results - Displacement Source Probe and Its Tautology

Date: 2026-07-12.

Script:

```text
E73_126_csv_displacement_source_probe.py
```

Purpose:

Test whether the CSV channel can be explained by a source identity

```text
k_gamma = (C_E-mu I)Y_gamma + R_gamma
```

by projecting `k_gamma` onto `(C_E-mu I)` applied to rational source
vectors and measuring only the scalar channel

```text
<xi,residual>.
```

Output:

```text
E73.126 CSV displacement source probe
Projects k_gamma onto (C_E-mu) applied to rational source vectors.
Success channel is scalar residual <xi,resid>, not ambient norm.
 lam     L gamma    beforeB   afterB ambientB nsrc status
  16   5.545   14.13   -19.996  -20.399  -10.301   18 PASS
  16   5.545   21.02   -19.339  -19.324   -8.344   18 PASS
  16   5.545   25.01   -13.864  -13.868   -1.138   18 FAIL
  20   5.991   14.13   -18.954  -19.349   -7.531   18 PASS
  20   5.991   21.02   -19.679  -18.332   -6.643   18 PASS
  20   5.991   25.01   -17.872  -17.665   -5.824   18 PASS
  24   6.356   14.13   -17.818  -17.769   -7.400   18 PASS
  24   6.356   21.02   -20.239  -17.264   -6.786   18 PASS
  24   6.356   25.01   -19.743  -18.706   -4.873   18 PASS
  28   6.664   14.13   -20.099  -17.472   -6.083   18 PASS
  28   6.664   21.02   -17.250  -17.265   -5.922   18 PASS
  28   6.664   25.01   -18.104  -17.886   -5.770   18 PASS
```

## Diagnosis

This test is not a valid mechanism for CSV.

Reason:

```text
(C_E-mu I)xi=0
```

and `C_E` is symmetric.  Hence for every source vector `Y`,

```text
<xi,(C_E-mu I)Y> = <(C_E-mu I)xi,Y> = 0.
```

Therefore replacing

```text
k_gamma
```

by

```text
k_gamma - (C_E-mu I)Y
```

cannot change the scalar channel:

```text
<xi,k_gamma-(C_E-mu I)Y> = <xi,k_gamma>.
```

The observed `beforeB` and `afterB` are essentially the same because this
is forced algebraically.  The ambient residual can improve, but the scalar
CSV value is invariant under adding anything in the range of `(C_E-mu I)`.

## Consequence

The E73.125 formulation must be corrected:

```text
k_gamma = (C_E-mu I)Y_gamma + R_gamma
```

does not prove CSV unless the residual estimate is obtained independently;
the range component is invisible to `xi` by construction.

Thus CSV is not a displacement-image problem.  It is a direct statement
that the Cauchy row is almost orthogonal to the finite ground vector:

```text
<xi,k_gamma> = C_x(-gamma) is small.
```

The correct reformulation is via the finite characteristic function:

```text
Phi_N(s) = (2/sqrt(L)) sin(sL/2) C_x(s),
```

so CSV at `s=-gamma` is equivalent to a finite interpolation statement:

```text
Phi_N(-gamma) is small at the critical ordinates.
```

That is the next target.

