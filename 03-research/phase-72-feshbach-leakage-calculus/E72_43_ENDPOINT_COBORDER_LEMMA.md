# E72.43 -- Endpoint coborder lemma for scalar WRL

**Date:** 2026-07-08.
**Role:** formulate the renormalized coborder that would prove scalar endpoint orthogonality.

## 0. Endpoint scalar orthogonality

The current target from E72.42 is:

```text
<C_x^(-1)Q_x(sI-D_x)^(-1)1_x, S_x(z)k_x> -> 0,
S_x(z)=sum (n/x)^zT_{x,n}.
```

Set:

```text
r_{x,s}:=(sI-D_x)^(-1)1_x.
```

Then the target is:

```text
<Q_xr_{x,s}, C_x^(-1)Q_xS_x(z)k_x> -> 0.        (ESO)
```

## 1. Endpoint coborder

### Lemma 72.43

Assume there exist vectors `w_x(z)` and remainders `e_x(z)` in the compressed complement such that:

```text
Q_xS_x(z)k_x = C_x w_x(z)+e_x(z),                (EC)
```

and, on the two Cauchy heights,

```text
<Q_xr_{x,s},w_x(z)> -> 0,                        (W-small)
<Q_xr_{x,s},C_x^(-1)e_x(z)> -> 0.                (E-small)
```

Then endpoint scalar orthogonality `(ESO)` holds.

### Proof

Apply `C_x^(-1)` to `(EC)`:

```text
C_x^(-1)Q_xS_x(z)k_x = w_x(z)+C_x^(-1)e_x(z).
```

Pair with `Q_xr_{x,s}` and use `(W-small)` and `(E-small)`. `QED`

## 2. Why this is different from the old coborder

Earlier global coborders tried to solve:

```text
Q_x(H_x-H_x^0)k_x=C_xw_x+e_x
```

for the whole arithmetic residual. That re-entered the full leakage problem.

Here the source is endpoint-weighted:

```text
Q_xS_x(z)k_x,
```

where `S_x(z)` already contains:

```text
endpoint taper,
normalized Mellin damping,
and scalar Cauchy-current localization.
```

So the primitive only has to be Weyl-small, not norm-small.

## 3. Concrete construction target

The natural candidate primitive is the model Doob primitive for the endpoint force:

```text
w_x(z)=D_x^+ ( S_x(z)k_x/k_x )
```

in the one-dimensional prolate coordinate, with centering by `Q_x`.

By E72.12, this primitive is controlled by the cumulative endpoint force:

```text
G_x^z(theta)=int_{a_x}^theta k_x(t)Q_xS_x(z)k_x(t)dt.
```

Thus a sufficient condition is:

```text
<Q_xr_{x,s}, w_x(z)> -> 0
```

with `w_x` given by the explicit cumulative formula.

## 4. Endpoint force advantage

Because each cell kernel vanishes at `u=x`, the endpoint force has an extra boundary zero. The primitive
therefore has one more factor of endpoint distance than the raw arithmetic force.

This is the mechanism that could supply the missing half-power from E72.40.

## 5. New target

### Endpoint Doob-Weyl Smallness

For the endpoint-weighted source `Q_xS_x(z)k_x`, the explicit Doob primitive `w_x(z)` satisfies:

```text
<Q_x(sI-D_x)^(-1)1_x, w_x(z)> -> 0
```

on two Cauchy heights, with the corresponding error estimate for actual/model replacement.

## 6. Status

```text
proved: endpoint coborder + Weyl-small primitive implies scalar WRL annihilation;
open:   prove Endpoint Doob-Weyl Smallness from the endpoint-tapered cumulative formula.
```

This is the renormalized version of the original Feshbach/Sonin idea, now reduced to the scalar current
needed for the divisor.
