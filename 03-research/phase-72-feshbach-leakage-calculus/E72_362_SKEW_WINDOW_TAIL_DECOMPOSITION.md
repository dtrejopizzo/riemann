# E72.362 - Skew window-tail decomposition

## 1. Purpose

E72.361 says that, on simple Xi-zero windows, `CFIR-DIV` is equivalent to the vanishing of the
alternating residue matrix for

```text
Delta(z,w)=S(z)K(w)-S(w)K(z).
```

This note expands `S` and identifies which terms can actually contribute.  The scalar left
coefficient never enters the skew form; only the interpolation window and the signed finite tail
remain.

## 2. Exact affine residual

For a simple window `W_T`, write

```text
R_z^{Xi}(Lambda)=Lambda k_z + S_z,
```

where

```text
S_z = - I_T^H k_z + Tail_z^M.                         (1)
```

For simple nodes this is

```text
(I_T^H k_z) = sum_{b in W_T} K_L(z,b) k_b,
Tail_z^M   = sum_{b in W_T} TailBasis_z^M(b).
```

Apply the reduced adjugate or, in the rank-one channel, evaluate against `xi`.  Put

```text
K(z):=k_z xi = G_x(z),
S(z):=S_z xi.
```

Then

```text
S(z)=S_win(z)+S_tail(z),
```

with

```text
S_win(z):=-sum_{b in W_T} K_L(z,b)K(b),
S_tail(z):=Tail_z^M xi.                              (2)
```

## 3. Scalar term disappears

The Lambda-elimination minor for the full residual is

```text
[S(z)+Lambda K(z)]K(w)-[S(w)+Lambda K(w)]K(z).
```

The scalar part is

```text
Lambda K(z)K(w)-Lambda K(w)K(z)=0.
```

Thus `SCALAR-CONS` is separate from `CFIR-DIV`: the divisor-block skew condition does not see the
value of `Lambda_L`.

## 4. Skew decomposition

The alternating minor is

```text
Delta(z,w)
= Delta_win(z,w)+Delta_tail(z,w),
```

where

```text
Delta_win(z,w)
= S_win(z)K(w)-S_win(w)K(z),

Delta_tail(z,w)
= S_tail(z)K(w)-S_tail(w)K(z).                       (3)
```

Substituting (2):

```text
Delta_win(z,w)
= -sum_{b in W_T}
   [ K_L(z,b)K(b)K(w) - K_L(w,b)K(b)K(z) ].           (4)
```

The signed finite-tail part is

```text
Delta_tail(z,w)
= [Tail_z^M xi]K(w)-[Tail_w^M xi]K(z).               (5)
```

## 5. Window nodes

If `z,w` themselves are in the same simple window, then (4) is the skew of the finite matrix

```text
K_L(a_i,a_b)K(a_b)K(a_j).
```

The diagonal terms `b=i` and `b=j` are not singular: they use the removable value

```text
K_L(a,a)=L+sinh(aL)/a.
```

Thus the simple-window `CFIR-DIV` block is the finite condition

```text
sum_b K(b)[K_L(a_i,b)K(a_j)-K_L(a_j,b)K(a_i)]
= Tail_{a_i}^M xi K(a_j)-Tail_{a_j}^M xi K(a_i)
```

up to polynomial error.

## 6. Meaning

The skew condition is not a bound for the prime tail alone.  It says that the antisymmetric part of
the interpolation window is exactly balanced by the antisymmetric part of the signed finite tail.

This is sharper than `R_T xi=0` because:

```text
1. Lambda has been eliminated;
2. rowspace additions are invisible by E72.352;
3. the target is a finite skew identity in K_L, K, and TailBasis.
```

## 7. Status

```text
proved: scalar Lambda drops out of the skew divisor block;
proved: CFIR-DIV splits into window skew plus signed-tail skew;
open: prove the finite skew identity (4)+(5)=O(L^B) on Xi-zero windows.
```
