# E73.197 - Signed closed form for the WR tail

Date: 2026-07-14.

## 1. Purpose

E73.196 shows that the existing absolute WR tail bound is rigorous but too
conservative for `FF-SECOND-ABEL`.  The required replacement is a signed tail
formula.

## 2. Tail per frequency

For a finite packet

```text
B(y)=sum_omega c_omega e^(i omega y)
    +y sum_omega l_omega e^(i omega y),
```

the WR tail after `R` terms is

```text
T_R(B)=sum_{r>=R}
 [ int_0^L e^{-(2r+1/2)y}B(y)dy
  -B(0)int_0^L e^{-(2r+1)y}dy ].
```

For each frequency put

```text
a_r(omega)=2r+1/2-iomega.
```

Then

```text
int_0^L e^{-a_r y}dy
=(1-e^{-a_rL})/a_r,

int_0^L y e^{-a_r y}dy
=(1-e^{-a_rL}(1+a_rL))/a_r^2.
```

Thus

```text
T_R(B)
=sum_omega c_omega S_1(R,omega)
 +sum_omega l_omega S_2(R,omega)
 -B(0)S_0(R),
```

where

```text
S_1(R,omega)=sum_{r>=R}(1-e^{-a_rL})/a_r,
S_2(R,omega)=sum_{r>=R}(1-e^{-a_rL}(1+a_rL))/a_r^2,
S_0(R)=sum_{r>=R}(1-e^{-(2r+1)L})/(2r+1).
```

## 3. Closed special-function form

The non-exponential parts are shifted polygamma/digamma tails:

```text
sum_{r>=R} 1/(2r+1/2-iomega)
= 1/2 * divergent_digamma_tail,

sum_{r>=R} 1/(2r+1/2-iomega)^2
= 1/4 psi_1(R+1/4-iomega/2).
```

The `S_1-S_0` combination is convergent because the original WR summand has
the zero-order subtraction.  Therefore one should evaluate it in the
renormalized paired form

```text
sum_omega c_omega[S_1(R,omega)-S_0(R)]
```

using `sum_omega c_omega=B(0)`.

Equivalently:

```text
T_R(B)
=sum_omega c_omega [S_1(R,omega)-S_0(R)]
 +sum_omega l_omega S_2(R,omega).
```

This expression is finite and signed.

## 4. Certification route

The final interval certificate should:

```text
1. enclose each finite coefficient c_omega,l_omega;
2. evaluate S_1-S_0 and S_2 with complex interval arithmetic;
3. sum signed intervals over omega;
4. add the exact finite partial WR sum and the exact prime-power sample sum.
```

This avoids the 7--12 powers of `L` lost in the coefficient-absolute bound of
E73.196.

## 5. Status

```text
derived: signed closed WR tail form;
open: implement complex interval/special-function evaluation.
```
