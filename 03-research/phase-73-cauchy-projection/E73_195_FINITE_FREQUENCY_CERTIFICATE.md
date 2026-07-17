# E73.195 - Finite-frequency certificate for the balanced endpoint

Date: 2026-07-14.

## 1. Purpose

E73.194 gives the proof-facing identity

```text
F_L[B_a^bal]=int_0^L K_L(t)(B_a^bal)''(t)dt.
```

Direct nested quadrature is not stable enough at the true residual scale.  This
note records the finite-frequency certificate that should replace quadrature.

## 2. Finite expansion

The transverse packet has the exact form

```text
B_a(y)=sum_omega c_omega e^(i omega y)
      + y sum_omega l_omega e^(i omega y).
```

The coefficients are finite sums over the active mesh.  The balanced packet is

```text
B_a^bal(y)=B_a(y)-B_a'(0)r_*(y),
```

where

```text
F_L[r_*]=0.
```

Therefore

```text
F_L[B_a^bal]=F_L[B_a].
```

The value can be certified without nested quadrature by:

```text
F_L[B_a]
= A_L^closed[{c_omega,l_omega}]
 - sum_{p^k<=e^L}(log p)p^(-k/2)
   [sum_omega c_omega e^(i omega klogp)
    + klogp sum_omega l_omega e^(i omega klogp)].
```

The archimedean closed term is the accelerated WR series of E73.182, with a
separate rigorous tail bound from E73.183--E73.185.

## 3. Why this is the right certificate

The second-Abel kernel is analytically clean, but numerically ill-conditioned
when paired with highly oscillatory `B''`.  The frequency certificate keeps the
same theorem but evaluates the finite packet in its native basis.

For a proof, one should combine:

```text
1. finite coefficients c_omega,l_omega;
2. closed exponential primitives for A_L;
3. exact prime-power samples;
4. WR tail bounds from E73.183--E73.185;
5. the balanced-ramp fact F_L[r_*]=0.
```

This is a finite explicit certificate, suitable for interval arithmetic.

## 4. Current theorem

The endpoint is:

```text
FF-SECOND-ABEL:
The finite-frequency expression above satisfies O_R(L^-R)
for the Cauchy-balanced transverse coefficients.
```

Equivalently:

```text
FF-SECOND-ABEL <=> SECOND-ABEL <=> BAL-DOUBLE-ZERO <=> TRANS-CELL.
```

## 5. Status

```text
proved: finite-frequency expression for F_L[B_a^bal];
verified: closed-series evaluation matches the matrix residual to the
          available WR-series precision;
open: prove the finite-frequency expression has rapid decay uniformly.
```
