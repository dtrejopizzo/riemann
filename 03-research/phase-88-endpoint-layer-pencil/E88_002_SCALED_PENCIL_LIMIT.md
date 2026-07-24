# E88.002 - Abstract scaled-pencil limit theorem

## 1. Scaling hypotheses

Let `rho_N->0` and set

```text
t_N(tau)=1-rho_N tau.                                 (1.1)
```

On every compact `tau` interval, assume in a fixed finite-dimensional cluster
coordinate space that

```text
rho_N^(-1)F_{N,t_N(tau)} -> K+tau B,                  (1.2)

a_N^(-1)b_{N,t_N(tau)}^eff -> b,                      (1.3)

h_{N,t_N(tau),z}^eff -> h_z,                          (1.4)
```

locally uniformly in the safe variable `z`.  Assume also

```text
rho_N a_N^(-1)G_{N,t_N(tau),z}^reg -> g_z^reg,        (1.5)
```

and that `K+tau B` is invertible on the compact parameter set.

## 2. Limit theorem

### Theorem 2.1

Under (1.2)--(1.5),

```text
(rho_N/a_N)G_{N,t_N(tau)}(z)
 ->g_tau(z),                                          (2.1)

g_tau(z)=g_z^reg-h_z(K+tau B)^(-1)b.                  (2.2)
```

The convergence is locally uniform in `z` and `tau`.  If `g_tau` is zero-free
on a compact set, then the normalized ratios and logarithmic derivatives also
converge there.

### Proof

From (1.2), finite-dimensional inverse continuity gives

```text
rho_N F_{N,t_N(tau)}^(-1)->(K+tau B)^(-1).             (2.3)
```

Multiply the exact identity E88.001, equation (2.2), by `rho_N/a_N` and use
(1.3)--(1.5).  This proves (2.1)--(2.2).  Zero-free ratio and derivative
convergence follow from uniform convergence, Hurwitz and Cauchy's formula.
`QED`

## 3. Growing clusters

For a growing cluster, the same conclusion requires strong-resolvent
convergence of the pencils together with convergence of the two specified
source and bordered matrix elements.  Ambient norm convergence of the inverse
is unnecessary.  The finite-dimensional theorem identifies the exact data
that the growing-cluster version must preserve.

## 4. Status

```text
proved:
  scaled effective-pencil theorem for fixed cluster dimension;

open:
  verification of (1.2)--(1.5) for the CCM endpoint layer;
  the growing-cluster extension required by the cascade.
```

