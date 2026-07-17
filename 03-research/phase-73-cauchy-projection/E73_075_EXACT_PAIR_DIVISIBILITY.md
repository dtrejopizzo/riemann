# E73.075 - Exact pair divisibility

## 1. Purpose

E73.073--E73.074 show that the paired complete-mesh packet

```text
Pair_z^infty(w)=M_z^infty(w)+M_z^infty(-w)
```

is tiny when the finite Cauchy divisor is tiny at `w`.  This note proves the algebraic reason.

## 2. Cauchy packet notation

Let

```text
H_0(u):=sum_n xi_n/(u+i d_n).
```

E73.070 wrote

```text
M_z^infty(w)
= i(e^(wL)-e^(zL))H_0(z)/(w-z)
 - i(e^((w+z)L)-1)H_0(z)/(w+z)

 - i(e^(wL)-1)R_+(z,w)
 + i e^(zL)(e^(wL)-1)R_-(z,w),
```

where

```text
R_+(z,w):=sum_n xi_n/((z+i d_n)(w+i d_n)),
R_-(z,w):=sum_n xi_n/((z+i d_n)(w-i d_n)).
```

## 3. Partial fractions

The two double Cauchy packets satisfy the exact identities

```text
R_+(z,w)= (H_0(z)-H_0(w))/(w-z),                      (1)
```

and

```text
R_-(z,w)= (H_0(z)-H_0(-w))/(z+w).                     (2)
```

Proof.  For (1),

```text
1/(z+i d_n)-1/(w+i d_n)=(w-z)/((z+i d_n)(w+i d_n)).
```

For (2),

```text
1/(z+i d_n)-1/(-w+i d_n)=-(z+w)/((z+i d_n)(-w+i d_n)),
```

and `(w-i d_n)=-(-w+i d_n)`.

## 4. One-sided factorization

Substituting (1)--(2) into `M_z^infty(w)` gives

```text
M_z^infty(w)
= i(1-e^(zL)) 2w H_0(z)/(w^2-z^2)
 + i(e^(wL)-1)H_0(w)/(w-z)
 - i e^(zL)(e^(wL)-1)H_0(-w)/(w+z).                  (3)
```

The first term is the only term involving `H_0(z)`.

## 5. Paired cancellation

Replace `w` by `-w` in (3) and add.  The `H_0(z)` term is odd in `w`, hence cancels exactly.

Therefore:

```text
Pair_z^infty(w)
= A_L(z,w)H_0(w)+B_L(z,w)H_0(-w),                    (4)
```

where

```text
A_L(z,w)
= i[(e^(wL)-1)+e^(zL)(e^(-wL)-1)]/(w-z),
```

and

```text
B_L(z,w)
= -i[e^(zL)(e^(wL)-1)+(e^(-wL)-1)]/(w+z).
```

Equation (4) is the exact pair divisibility identity.

## 6. Consequence for zero windows

At a finite spectral root of the Cauchy transform,

```text
H_0(w)=0.
```

If the root set is symmetric, the partner also gives

```text
H_0(-w)=0.
```

Then

```text
Pair_z^infty(w)=0.
```

For approximate Xi-zero heights, the paired packet is controlled by the two Cauchy defects:

```text
|Pair_z^infty(w)|
<= |A_L(z,w)||H_0(w)|+|B_L(z,w)||H_0(-w)|.
```

This is exactly the Mellin spectral divisibility mechanism required by the packet route.

## 7. Updated endpoint

The complete-mesh part of `BALANCED-PACKET-ROW-5` is now reduced to:

```text
PAIR-DIV:
control H_0(w) and H_0(-w) on the finite zero window, with the explicit coefficients A_L,B_L.
```

The remaining non-complete part is the finite mesh tail:

```text
Pair_z^M(w)=Pair_z^infty(w)-Pair_z^tail(w).
```

Thus the next analytic target is:

```text
TAIL-PAIR-DIV:
the finite mesh tail has the same Cauchy-divisor smallness, or is small enough in the weighted
FAR3 budget.
```

## 8. Status

```text
proved: Pair_z^infty(w) belongs to the ideal (H_0(w),H_0(-w));
proved: complete-mesh zero-window packet vanishes at finite symmetric Cauchy roots;
open: prove the finite mesh tail version needed for the actual packet B_z^M.
```
