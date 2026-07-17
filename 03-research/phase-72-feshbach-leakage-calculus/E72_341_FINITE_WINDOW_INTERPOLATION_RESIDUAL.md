# E72.341 -- Finite-window interpolation residual

**Purpose.** Write the balanced Feshbach-Weil remainder of E72.340 as an explicit Cauchy
interpolation residual plus the finite signed packet tail.  This is the analytic form in which the
maximal-real-part block of E72.324 acts.

## 1. Complete-mesh pair kernel

For the complete mesh, E72.320--E72.321 give the paired factor formula

```text
Pair_z^infty(w)
= K_L(z,w)G_x(w),
```

where

```text
K_L(z,w)
:= [ w(1+e^(zL))(1-e^(-wL))
     + z(1-e^(zL))(1+e^(-wL)) ]
   /(w^2-z^2),                                      (1)
```

with the removable Hermite value at `w=+-z`.  The `G_x(z)` coefficient has already cancelled by the
`w ~ -w` pairing.

For the actual finite packet,

```text
F_z^M(w)=Pair_z^infty(w)-TailPair_z^M(w).             (2)
```

The tail is not estimated pointwise; it is kept as the signed finite packet contribution from
E72.333--E72.334.

## 2. Window residual identity

Insert (2) into E72.340(7).  For any finite zero-pair window `W_T`,

```text
Rem_T^M(z)
= Lambda_LG_x(z)
 - sum_{w in W_T/+-} K_L(z,w)G_x(w)
 + sum_{w in W_T/+-} TailPair_z^M(w).                 (3)
```

Define the finite interpolation operator

```text
(I_TG)(z):=sum_{w in W_T/+-} K_L(z,w)G(w).
```

Then

```text
Rem_T^M(z)=Lambda_LG_x(z)-(I_TG_x)(z)+Tail_T^M(z).    (4)
```

This is the corrected finite-window object.  The first two terms are a Cauchy interpolation residual;
the last term is a finite signed tail, not an incoherent Fourier tail.

## 3. Nodal equations

Evaluate (4) at a zero node `z=a in W_T`.  The removable value of `K_L(a,a)` gives the diagonal
coefficient of E72.322, while `K_L(a,w)` for `w != a` gives the off-diagonal Cauchy coupling.

Thus the nodal system is

```text
[Lambda_L - K_L(a,a)]G_x(a)
 - sum_{w in W_T, w != a} K_L(a,w)G_x(w)
= Rem_T^M(a)-Tail_T^M(a).                            (5)
```

For a maximal positive-real-part cluster `A={a_1,...,a_N}`, the leading exponential part of the
matrix in (5) is

```text
-diag(e^(a_jL)) C_A,       C_A(j,k)=1/(a_j+a_k),
```

exactly as in E72.324.  Hence, if the right side of (5) is polynomial, then

```text
G_x(a_j)=O(e^(-Re(a_j)L)L^B)
```

for every node in the cluster.

## 4. What must be proved, now sharply

The transformed route no longer needs a global smoothness estimate.  It needs the following two
analytic statements:

```text
TAIL-WIN:
sup_{z in K} |Tail_T^M(z)| <= C_{K,T}L^B.

RIGHT-WIN:
sup_{a in W_T} |Rem_T^M(a)-Tail_T^M(a)| <= C_TL^B.
```

But by (3), `RIGHT-WIN` is exactly the statement that the coupled Feshbach interpolation residual is
polynomial at the finite nodes.  It must be proved from the finite eigenvector equation before any
zero-tail estimate is invoked.

Equivalently, the non-circular theorem is:

```text
CFIR:
At every fixed finite zero window, the transformed Feshbach equation makes
Lambda_LG_x-I_TG_x polynomial at the window nodes, with the signed tail retained.
```

Then E72.324--E72.327 propagate this nodal control to the shifted compact strip.

## 5. Why this avoids the old walls

The forbidden estimates were:

```text
sum |Lambda(n)n^(-1/2)B(log n)|,
sum |TailPair(w)|,
int |(B_z^M)''|.
```

Equation (4) uses none of them.  It keeps the Cauchy interpolation structure and lets the maximal
cluster matrix absorb the exponential factors.

## 6. Status

```text
proved: Rem_T^M is the finite Cauchy interpolation residual (4);
proved: nodal evaluation recovers the maximal Cauchy block of E72.324;
reduced: the proof obligation to CFIR plus signed finite-window tail control.
```
