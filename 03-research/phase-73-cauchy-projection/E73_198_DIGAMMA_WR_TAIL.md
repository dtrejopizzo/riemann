# E73.198 - Digamma form of the signed WR tail

Date: 2026-07-14.

## 1. Purpose

E73.197 derives the signed grouped WR tail.  This note removes the long tail
sum by expressing the non-exponential part through digamma/polygamma.

## 2. Paired convergent tail

Let

```text
a_r(omega)=2r+1/2-iomega,
b_r=2r+1.
```

The convergent paired term is

```text
D_1(R,omega)=sum_{r>=R} [1/a_r(omega)-1/b_r].
```

Since

```text
a_r=2(r+1/4-iomega/2),
b_r=2(r+1/2),
```

we have

```text
D_1(R,omega)
= 1/2 [ psi(R+1/2)-psi(R+1/4-iomega/2) ].       (1)
```

The square tail is

```text
D_2(R,omega)=sum_{r>=R} 1/a_r(omega)^2
= 1/4 psi_1(R+1/4-iomega/2).                    (2)
```

## 3. Exponential correction

The full tail pieces are

```text
S_1(R,omega)-S_0(R)
= D_1(R,omega)
 -sum_{r>=R} e^{-a_rL}/a_r
 +sum_{r>=R} e^{-b_rL}/b_r,

S_2(R,omega)
= D_2(R,omega)
 -sum_{r>=R} e^{-a_rL}(1+a_rL)/a_r^2.
```

The exponential tails are bounded by elementary geometric estimates:

```text
sum_{r>=R} |e^{-a_rL}/a_r|
<= e^{-(2R+1/2)L}/|a_R| * 1/(1-e^{-2L}),

sum_{r>=R} |e^{-b_rL}/b_r|
<= e^{-(2R+1)L}/b_R * 1/(1-e^{-2L}),

sum_{r>=R} |e^{-a_rL}(1+a_rL)/a_r^2|
<= e^{-(2R+1/2)L}(1+|a_R|L)/|a_R|^2 * 1/(1-e^{-2L}).
```

For the ranges used in E73.195 these exponentials are far below the target
scale once `R` is even moderately large.

## 4. Certificate form

The signed WR tail is

```text
T_R(B)
=sum_omega c_omega D_1(R,omega)
 +sum_omega l_omega D_2(R,omega)
 + exponential correction,
```

with `D_1,D_2` given by (1)--(2).

This is the desired special-function form for interval arithmetic.

## 5. Status

```text
derived: digamma/polygamma signed tail formula;
verified: numerical agreement with direct grouped tail;
open: interval implementation of complex psi/psi_1 enclosures.
```
