# E87.004 - Endpoint boundary layer in the arithmetic deformation

## 1. Finite diagnostic

For the multiprecision `L=2 log 6` section with four outer modes, the
deformation `H_t=H_A-tH_P` gives

```text
t             mu_t          gap_t         critical row    displaced row
0             -3.51         2.26          1.62e-1         1.61e-1
0.9           -3.50e-1      2.32e-1       1.61e-1         1.60e-1
0.99          -3.45e-2      2.31e-2       1.53e-1         1.52e-1
1-1e-4        -2.71e-4      1.65e-4       7.77e-3         8.00e-3
1-1e-8        -1.91e-8      1.20e-8       4.97e-5         6.63e-5
1-1e-12       -1.21e-12     1.06e-12      9.65e-8         8.30e-7
1             3.80e-18      2.91e-15      1.62e-10        9.04e-8.       (1.1)
```

The row values are normalized Cauchy overlaps.  They are diagnostic only; no
zero ordinate enters the deformation theorem.

The table shows that the arithmetic alignment is concentrated in a thin
layer near `t=1`.  Uniform estimates obtained on compact subintervals of
`[0,1)` cannot be extrapolated to the endpoint.

## 2. Exact bulk-layer split

For every `epsilon in (0,1)`, Theorem 3.1 of E87.003 gives

```text
integral_0^1 partial_s K_t dt
 =integral_0^(1-epsilon) partial_s K_t dt
  +integral_(1-epsilon)^1 partial_s K_t dt.            (2.1)
```

The corrected proof program is

```text
BASE-BULK:
calculate the archimedean defect together with the first integral by regular
perturbation and fixed-L convergence;

DEFORM-LAYER:
choose epsilon=epsilon(L)->0 and compute the second integral through the
cluster tangent source without a uniform inverse bound.                (2.2)
```

## 3. Why the layer is load-bearing

The tangent formula contains

```text
M_t^(-1)y_t.                                          (3.1)
```

Both the lowest eigenvalue and the gap collapse inside the layer.  Bounding
`M_t^{-1}` before pairing would lose the cancellation and reproduce the old
inverse wall.  The layer theorem must keep

```text
h_z^T M_t^(-1)y_t/G_t(z)                              (3.2)
```

bilaterally coupled and integrate it in `t` before estimating.

This endpoint term is build-discriminating and is therefore eligible to carry
the arithmetic force absent from the build-neutral convergence clauses.

## 4. Minimal live theorem

```text
DEFORM-LAYER-RDI:
after fixed-L cluster regularization, the bilateral integral of (3.2) over
the shrinking endpoint layer differs from the Euler current layer by a
projectively constant term plus o(1), locally uniformly on Re s>1, with one
s derivative.                                         (4.1)
```

Together with the signed `BASE-BULK` term of E87.005, this is exactly the
combined deformation identity, hence RDI-ANCHOR.

## 5. Status

```text
proved:
  exact bulk-layer decomposition;

observed:
  a sharply localized arithmetic endpoint layer in finite sections;

open:
  BASE-BULK;
  DEFORM-LAYER-RDI.
```
