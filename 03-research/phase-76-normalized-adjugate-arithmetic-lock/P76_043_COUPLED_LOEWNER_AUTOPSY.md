# P76.043 - Coupled Loewner remainder autopsy

The inhomogeneous nodal identity of P76.042 is exact; its direct nodal error
is `1e-74--1e-66`.  However its off-mesh interpolation residual at `z=i`
is not small:

```text
N       |R_S,h|       |L(C-mu/2)I_h|       |(L/2)I_f|       |E_h|
5       7.36e3         8.02e4                2.22e-6          7.28e4
6       6.21e4         7.11e5                1.06e-6          6.49e5
7       7.20e5         8.55e6                8.72e-7          7.83e6
8       8.13e7         9.92e8                4.29e-6          9.11e8
9       4.25e7         5.31e8                1.38e-7          4.88e8
```

The source term is tiny but the canonical interpolation residual grows by
many orders.  Therefore the source coupling does not repair the contour-
remainder wall found in P76.012.

## Decision

`COUPLED-LOEWNER-REM` is closed as an estimation route.  P76.041 remains a
useful exact algebraic identity, but P76.042 may not be used to infer a small
off-mesh remainder.

The next object must use the real divisor globally rather than estimate the
Loewner interpolation residual.  The concrete next test is whether the core
boundary polynomials at consecutive cutoffs form a Sturm/interlacing chain.
Such a chain would control safe-axis products through signed root motion and
would not invoke the collapsing Schur inverse or the huge contour residual.
