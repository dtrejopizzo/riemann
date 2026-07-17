# E73.019 - Source image certificate

## 1. The load-bearing equation

The natural-height Schur gate is reduced to the source pairing

```text
<xi,S_b>.
```

The useful way to annihilate it is not to bound `S_b` by size.  The useful way is to show that
`S_b` is an image vector for the finite eigen-operator:

```text
S_b = (C_E-mu I)Y_b + R_b.          (1)
```

Then, since

```text
(C_E-mu I)xi=0,
```

one gets

```text
<xi,S_b>=<xi,R_b>.
```

Thus the whole problem is moved into a residual class.

## 2. Primitive class

By E73.018, the critical divided differences collapse on the CCM pole mesh to rational Cauchy
functions.  Therefore we test (1) with

```text
Y_b in P_{O,K}
= span{ DD_gamma(d)/(d^2+beta^2)^r : r=0,1,2 }
  + span{ d^2 DD_gamma(d) }.
```

This is the same primitive class used by E73.016.

## 3. Finite certificate

For each off-line node `b`, define the finite source

```text
S_b(d)=sum_{k in K_L} pi_b(k) DD_L(-gamma_k,d),
```

where `pi_b(k)` is the rational Cauchy projection coefficient from E73.003.

The finite certificate is:

```text
SRC-IMG:
dist(S_b, Image((C_E-mu I)P_{O,K})) <= residual_72(b,L).
```

If the residual obeys

```text
e^(Re b L)|<xi,R_b>| <= L^B,
```

then `NAT-SRC` follows.

## 4. Numeric evidence

E73.019 tests exactly `SRC-IMG`, using the SVD-truncated effective image to avoid over-reading the
ill-conditioned columns.  The relative source residual is in the range:

```text
1e-6 to 2.6e-4
```

and the exponentially weighted eigenvector pairing is:

```text
<= 2.2e-8
```

on the tested finite windows.

This is the correct quantity.  Raw source size is not small; image membership is the mechanism.

## 5. Analytic target

The analytic theorem to prove is now:

```text
SRC-IMG theorem:
For every compact off-line window O and critical window K, the Cauchy-Schur source vector S_b
belongs to Image((C_E-mu I)P_{O,K}) modulo the Phase 72 residual class, uniformly through natural
height.
```

Together with E73.017 and E73.018 this reduces the remaining problem to a finite rational
displacement identity:

```text
finite Loewner displacement
+ rational Cauchy module
+ endpoint residual absorption
=> SRC-IMG.
```

No positivity or zero input is used in this formulation.
