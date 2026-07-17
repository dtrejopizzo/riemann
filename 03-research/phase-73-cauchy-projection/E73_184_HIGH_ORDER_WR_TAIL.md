# E73.184 - High-order WR tail certificate

Date: 2026-07-14.

## 1. Purpose

E73.183 gives a closed WR tail bound after subtracting the first two Taylor
terms of

```text
F(y)=e^(y/2)B(y)-B(0).
```

The bound is valid but conservative.  This note records the order-`K`
version, which is the right proof-facing certificate.

## 2. Order-`K` acceleration

For `K>=1`, write

```text
F(y)=sum_{m=1}^K F^(m)(0)y^m/m! + R_{K+1}(y).
```

If

```text
M_{K+1} >= sup_{0<=y<=L} |F^(K+1)(y)|,
```

then

```text
|R_{K+1}(y)| <= M_{K+1} y^(K+1)/(K+1)!.
```

Against the omitted odd exponential tail this gives

```text
|Tail_{R,K}|
<= M_{K+1} sum_{r>=R}(2r+1)^(-(K+2)).
```

The sum is explicit:

```text
sum_{r>=R}(2r+1)^(-p)
= (-1)^p psi_{p-1}(R+1/2)/(2^p (p-1)!).
```

## 3. Finite derivative bound

For the finite mode packet

```text
B(y)=sum c_omega e^(i omega y)+y sum l_omega e^(i omega y),
```

all derivatives of `F=e^(y/2)B` are finite mode sums.  A computable
coefficient-absolute bound is:

```text
M_s
<= e^(L/2) sum_{a=0}^s binom(s,a)2^{-(s-a)}
   ||B^(a)||_infty,
```

with

```text
||B^(a)||_infty
<= sum |c_omega||omega|^a
 + sum |l_omega|(a|omega|^(a-1)+L|omega|^a).
```

Thus the WR tail certificate is finite, explicit, and parameterized by
`K,R`.

## 4. Status

```text
proved:   order-K WR tail inequality;
verified: K=2,4,6,8 all bound the observed tail;
open:     optimize K,R and coefficient grouping so the bound is sharp enough
          for final SCRCE residual certification.
```
