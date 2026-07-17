# E74.23 - Planted off-line nodal falsifier

Date: 2026-07-16.

## Test

`E74_023_planted_nodal_falsifier.py` imports the Phase 71 explicit-formula
perturbation

```text
(g0,b,c)=(25,0.30,5)
```

and evaluates the same normalized Cauchy values and local finite roots used by
`CAUCHY-EIG-LOC`.

## Result

```text
zeta:
||Q_gamma xi|| = 4e-16 to 2e-15,
root shifts      = O(1e-15),
mu               = -2.1e-14.

planted off-line:
||Q_gamma xi|| = 9e-3 to 6e-2,
root shifts      = 9e-3 to 2.3e-1,
mu               = -5.0.
```

The planted control fails decisively.  Hence critical nodal cancellation is
not a universal consequence of self-adjoint finite matrices, Cauchy geometry,
or the functional-equation cell.  It is sensitive to the off-line part of the
explicit formula.

## Meaning

This is the required anti-circularity discriminator: any proposed proof of
`CCM-ROOT-LOCK` must use an arithmetic property absent from the planted
deformation.  Conversely, a proof based only on generic gap, smoothness, or
finite Cauchy algebra cannot work because those structures survive planting.

