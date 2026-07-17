# E73.018 - Mesh rational collapse of the critical divided difference

## 1. Statement

Let

```text
d_n=2 pi n/L.
```

For the critical divided difference

```text
DD_L(u,d)= (exp(-i d L)-exp(-i u L))/(u-d),
```

and `u=-gamma`, one has on the CCM pole mesh:

```text
DD_L(-gamma,d_n)
= (1-exp(i gamma L))/(-gamma-d_n).
```

Thus every local generator used in Phase 73 is a rational Cauchy function on the pole mesh:

```text
DD_L(-gamma,d_n)/(d_n^2+beta^2)^r
= c_gamma / ((d_n+gamma)(d_n^2+beta^2)^r),
```

where

```text
c_gamma = exp(i gamma L)-1.
```

The diagonal confluent case is the same formula by analytic continuation.

## 2. Proof

Since `d_n L=2 pi n`,

```text
exp(-i d_n L)=1.
```

Therefore

```text
DD_L(-gamma,d_n)
= (1-exp(i gamma L))/(-gamma-d_n)
= (exp(i gamma L)-1)/(gamma+d_n).
```

Both sides have the same removable value when `d_n=-gamma`, because

```text
lim_{d->u} DD_L(u,d)= iL exp(-iuL).
```

This proves the identity.

## 3. Consequence for LOCAL-FIN

The primitive space is not transcendental on the mesh.  It is the finite rational module

```text
P_{O,K}
= span{ 1/((d+gamma)(d^2+beta^2)^r) : r=0,1,2 }
  + span{ d^2/(d+gamma) }.
```

The source space is

```text
S_{O,K}^{fin}
= span{ 1/((d+gamma)(d^2+beta^2)^r) : r=0,1,2,3 }
  + span{ d^2/(d+gamma), d^4/(d+gamma) }.
```

Constants depending only on `gamma` are harmless.

Thus FDL-2 from E73.017 is an algebraic statement about rational functions under the finite
Loewner displacement of the CCM cell.  No zeta zero or limiting divisor is used in this reduction.

## 4. Why this matters

Before E73.018, the endpoint exponential in `DD_L` made the local ideal look like a
Paley-Wiener object.  On the actual pole mesh it is simpler: the exponential has already been
quantized to `1`, and the entire critical source is Cauchy-rational.

The remaining analytic proof of `LOCAL-FIN` can therefore be organized as:

```text
finite Loewner displacement
+ rational partial fractions
+ Phase 72 endpoint residuals.
```
