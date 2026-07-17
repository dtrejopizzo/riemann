# E72.42 -- Endpoint operator probe

**Date:** 2026-07-08.
**Role:** test whether endpoint tightness is an operator-norm fact or only a scalar/channel fact.

## 0. Endpoint operator

Define the normalized endpoint operator

```text
S_x(z) := sum_{n<=x} (n/x)^z T_{x,n}.
```

The scalar WRL channel is:

```text
<v_{x,s},S_x(z)k_x>.
```

If `||QS_x(z)k_x|| -> 0` strongly, then WCB follows for bounded `v_{x,s}`. If even
`||S_x(z)|| -> 0`, the proof would be easier.

## 1. Numerical probe

Representative unweighted endpoint values:

```text
z=3:
  x=64    ||QS_zk||=5.86e-2,  ||S_z||=3.36e-1
  x=100   ||QS_zk||=1.30e-1,  ||S_z||=3.69e-1
  x=144   ||QS_zk||=6.52e-2,  ||S_z||=4.56e-1

z=10:
  x=64    ||QS_zk||=2.23e-2,  ||S_z||=1.15e-1
  x=100   ||QS_zk||=2.22e-2,  ||S_z||=8.25e-2
  x=144   ||QS_zk||=6.59e-3,  ||S_z||=1.60e-1

z=14:
  x=64    ||QS_zk||=1.63e-2,  ||S_z||=8.64e-2
  x=100   ||QS_zk||=1.39e-2,  ||S_z||=5.32e-2
  x=144   ||QS_zk||=2.88e-3,  ||S_z||=1.10e-1
```

The endpoint operator gets smaller as `Re z` increases, consistent with endpoint taper. But it does not
show a clean monotone decay in `x` at these small finite sizes.

## 2. Interpretation

The proof should not target:

```text
||S_x(z)|| -> 0
```

as an operator norm. That is stronger than needed and not numerically clean.

The viable target remains the scalar matrix element:

```text
<C_x^(-1)Q_x(sI-D_x)^(-1)1_x, S_x(z)k_x> -> 0.
```

This can vanish by:

```text
endpoint taper,
projection by Q_x,
and phase/orthogonality between v_{x,s} and S_x(z)k_x,
```

even when `S_x(z)` is not small in norm.

## 3. Current target

### Endpoint Scalar Orthogonality

For two Cauchy heights and compact `K`,

```text
sup_{z in K}
|<C_x^(-1)Q_x(sI-D_x)^(-1)1_x, S_x(z)k_x>| -> 0.
```

This is the precise weighted endpoint channel estimate from E72.41.

## 4. Status

```text
observed: endpoint operator is damped with Re z but not uniformly small in x;
open:     prove scalar endpoint orthogonality.
```

The next proof attempt must use the relation between `C_x` and `S_x(z)k_x`, not just endpoint operator
norms.
