# E73.205 results - bordered eigenline audit

Command:

```text
python3 E73_205_bordered_eigenline_audit.py
```

Output:

```text
E73.205 bordered eigenline conditioning audit
Uses current double matrix; this is a precision-demand audit, not a proof.
 lam     L  dim    muB    gapB    resB  condB  stepB
  12   4.970   33 -20.52  -22.12  -21.06  23.72   -0.76
  16   5.545   41 -18.67  -20.30  -19.30  21.11   -0.32
  20   5.991   49 -17.46  -19.43  -18.33  20.57   -0.86
  24   6.356   57 -16.85  -18.29  -18.25  19.91   -0.30
```


Reading:

```text
The bordered matrix has condition number roughly reciprocal to the near-radical
gap, about L^20 in these windows.  With the current double matrix residual,
||J^{-1}F|| is enormous, so the bordered certificate cannot be closed from the
existing quadrature/double entries.

This gives a concrete precision requirement: the closed-form matrix-entry
engine must evaluate H and the approximate eigenpair residual at least about
20 powers of L below the desired eigenline radius before Krawczyk can succeed.
The next implementation target is therefore high-precision closed-form matrix
entries, not another eigenvector manipulation on the double matrix.
```
