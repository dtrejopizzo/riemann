# E72.56 -- Endpoint rank-one expansion of the CCM overlap cells

**Date:** 2026-07-08.
**Role:** extract the boundary Taylor structure behind the Loewner cancellation observed in E72.55.

## 0. Endpoint coordinate

Set:

```text
y=L-r,       r>=0.
```

Since:

```text
d_nL=2*pi*n,
```

the endpoint expansion of the cell matrix is an expansion in powers of `rD`.

## 1. First-order expansion

For `m=n`:

```text
q_nn(L-r)=2(r/L)cos(d_nr)
        =2r/L+O(r^3d_n^2/L).
```

For `m != n`:

```text
q_mn(L-r)
 = [sin(d_m(L-r))-sin(d_n(L-r))]/[pi(n-m)]
 = [-sin(d_mr)+sin(d_nr)]/[pi(n-m)].
```

Using:

```text
sin(d_nr)-sin(d_mr)=(d_n-d_m)r+O(r^3(d_m^3+d_n^3)),
```

and:

```text
d_n-d_m=2*pi(n-m)/L,
```

gives:

```text
q_mn(L-r)=2r/L+O(r^3(|m|^3+|n|^3)/(L|n-m|)).
```

Thus, to first order:

```text
Q_x(L-r)= (2r/L) J + higher endpoint terms,       (R1)
```

where `J=11^T`.

## 2. Consequence for scalar channel

The scalar endpoint channel becomes:

```text
a_{x,s}(L-r)
 = (2r/L)<v_{x,s},1><1,k_x> + higher terms.      (A1)
```

Therefore the leading endpoint contribution is rank one.

If either:

```text
<v_{x,s},1> = small
```

or:

```text
<1,k_x> = small
```

in the relevant normalization, the leading endpoint layer is suppressed and the next terms carry extra
endpoint powers/frequency factors.

## 3. Why this matters

E72.55 observed strong cancellation between the `2cos` and Loewner pieces. E72.56 explains it:

```text
their combination collapses to the rank-one overlap J at leading endpoint order.
```

Estimating the pieces separately misses this collapse.

## 4. New target

### Rank-One Endpoint Suppression

Prove:

```text
<C_x^(-1)Q_x(sI-D_x)^(-1)1, 1> <1,k_x>
```

is small enough to supply the half-power channel gain, and control the higher endpoint Taylor terms by
the overlap bound.

Equivalently:

```text
<v_{x,s},1>
```

must be small in the finite CCM/prolate normalization.

## 5. Status

```text
proved: endpoint overlap has first-order rank-one expansion Q(L-r)=(2r/L)J+higher;
open:   prove Rank-One Endpoint Suppression for the compressed Cauchy vector.
```

The next diagnostic is to measure `<v_{x,s},1>` and compare the rank-one leading approximation to the
actual scalar endpoint channel.
