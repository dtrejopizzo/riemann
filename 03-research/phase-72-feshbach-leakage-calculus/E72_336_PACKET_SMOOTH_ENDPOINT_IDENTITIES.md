# E72.336 -- Packet smoothness endpoint identities

**Purpose.** Start the proof of `PACK-SMOOTH` from E72.335. Crude finite-sum bounds are not acceptable
because the coefficients contain `1-e^(zL)`. The endpoint derivatives of the overlap kernel have exact
cancellations and must be used first.

## 1. Finite packet

The actual finite packet is

```text
B_z^M(y)=sum_{m,n in active} a_m(z) xi_n Q_y(m,n),
a_m(z):=(1-e^(zL))/(iz-d_m).
```

The endpoint values are

```text
B_z^M(0)=2G_x(z),
B_z^M(L)=0.
```

## 2. First derivative at zero

For `m != n`,

```text
Q_y(m,n)= [sin(d_m y)-sin(d_n y)]/[pi(n-m)].
```

Thus

```text
Q'_0(m,n)= (d_m-d_n)/[pi(n-m)] = -2/L.
```

For `m=n`,

```text
Q_y(m,m)=2(1-y/L)cos(d_m y),
```

so

```text
Q'_0(m,m)=-2/L.
```

Therefore the identity is global:

```text
Q'_0(m,n)=-2/L                 for all active m,n.       (1)
```

Consequently,

```text
(B_z^M)'(0)
= -2/L [sum_m a_m(z)] [sum_n xi_n].                    (2)
```

This is a rank-one endpoint identity.

## 3. First derivative at L

For `m != n`, using `d_jL=2pi j`,

```text
Q'_L(m,n)= (d_m-d_n)/[pi(n-m)] = -2/L.
```

For `m=n`,

```text
Q'_L(m,m)= -2/L
```

as well, since the sine term again vanishes and `cos(d_mL)=1`.

Hence

```text
(B_z^M)'(L)
= -2/L [sum_m a_m(z)] [sum_n xi_n].                    (3)
```

The two endpoint derivatives are equal.

## 4. Meaning for PACK-SMOOTH

`PACK-SMOOTH` requires polynomial control of endpoint derivatives and the integral of the second
derivative. Equations (2)--(3) show that endpoint derivative control reduces to:

```text
S_a(z):=sum_m (1-e^(zL))/(iz-d_m),
S_xi:=sum_n xi_n.
```

The product `S_a(z)S_xi` is much smaller than the incoherent coefficient ceiling if either:

```text
1. S_a(z) has the finite sine-product cancellation; or
2. S_xi is small by the pole-even ground equation/parity normalization; or
3. their product is absorbed into the left coefficient through the same endpoint gauge as B_z(0).
```

Thus the endpoint part of `PACK-SMOOTH` is now a rank-one scalar gate, not a full matrix estimate.

## 5. Second derivative structure

For `m != n`,

```text
Q''_y(m,n)= [-d_m^2 sin(d_m y)+d_n^2 sin(d_n y)]/[pi(n-m)].
```

At both endpoints this vanishes:

```text
Q''_0(m,n)=Q''_L(m,n)=0.
```

For `m=n`,

```text
Q''_y(m,m)
= 4d_m/L sin(d_my) - 2(1-y/L)d_m^2 cos(d_my),
```

so endpoint diagonal terms are explicit. The bulk second derivative carries an additional sine factor,
hence one more oscillation than the original kernel.

The next PACK-SMOOTH target is therefore:

```text
BULK-SMOOTH:
int_0^L |sum_{m,n}a_m(z)xi_n Q''_y(m,n)|dy <= C_KL^B,
```

using the oscillatory sine structure before absolute values are taken over `m`.

## 6. Status

```text
proved: endpoint derivatives collapse to the rank-one identity (2)--(3);
reduced: PACK-SMOOTH to endpoint rank-one control plus BULK-SMOOTH;
refined: E72.337 rewrites BULK-SMOOTH as Dirichlet-Cauchy packet bounds.
```

This is progress toward `UREM-POLY` without taking the forbidden incoherent tail bound.
