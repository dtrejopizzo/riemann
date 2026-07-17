# E73.022 - Scalar dual formula

## 1. Source pairing

The source vector is

```text
S_b(d_n)=sum_{k in K_L} Pi(b,k) DD_L(-gamma_k,d_n).
```

Scalar WRL only sees

```text
<xi,S_b>.
```

By E73.018, on the pole mesh:

```text
DD_L(-gamma,d_n)=(exp(i gamma L)-1)/(gamma+d_n).
```

Therefore

```text
<xi,S_b>
= sum_{k in K_L} Pi(b,k)(exp(i gamma_k L)-1)
  sum_n conjugate(xi_n)/(gamma_k+d_n).                 (1)
```

This is the scalar dual formula.

## 2. Finite Cauchy transform

Define the finite Cauchy transform of the eigenpacket:

```text
F_x(gamma):=sum_n conjugate(xi_n)/(gamma+d_n).
```

Then (1) becomes:

```text
<xi,S_b>
= sum_{k in K_L} Pi(b,k)(exp(i gamma_k L)-1)F_x(gamma_k).       (2)
```

The natural-height source gate is:

```text
e^(Re b L)
|sum_{k in K_L} Pi(b,k)(exp(i gamma_k L)-1)F_x(gamma_k)|
<= L^B.                                                        (3)
```

## 3. Why this is the right endpoint

Earlier formulations involved:

```text
vector image membership,
full residual norm,
large cokernel directions.
```

Those are stronger than scalar WRL.  Formula (3) is exactly the one-dimensional obstruction.

It contains:

```text
Pi(b,k)                  finite off-line Cauchy-Schur projection kernel;
exp(i gamma_k L)-1       mesh quantization residue;
F_x(gamma_k)             finite Cauchy transform of the eigenpacket.
```

No vector projection or unstable coefficient law remains.

## 4. Relation to Phase 72

Phase 72 reduced the problem to natural-height Cauchy projection.  E73.022 rewrites the surviving
projection as the scalar rational identity (3).  Thus the remaining statement is:

```text
RATIONAL-DUAL:
The weighted rational Cauchy residue sum (3) is polynomially bounded through natural height.
```

Together with the already isolated Phase 72 tail absorptions, `RATIONAL-DUAL` implies:

```text
NAT-SRC => NAT-PROJ => scalar WRL => Omega_7.
```

## 5. Status

```text
proved: direct mesh pairing equals scalar rational formula (1);
validated: E73.022 numerical equality to floating precision;
open: prove the natural-height bound (3) analytically.
```

This is now the explicit finite identity to attack.
