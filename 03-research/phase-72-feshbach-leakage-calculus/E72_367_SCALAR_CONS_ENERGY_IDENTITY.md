# E72.367 - Scalar consistency as a finite energy identity

## 1. Purpose

E72.365 split the simple-window CFIR equation into:

```text
PCFIR + SCALAR-CONS.
```

This note rewrites `SCALAR-CONS` without naming the fitted scalar.  It is a finite quadratic energy
identity for the actual residue vector `k=J_TG_x`.

## 2. Setup

For a simple Xi-zero window, let

```text
k := J_TG_x,
KWin_{ij}:=K_L(a_i,a_j),
t:=J_TTail_T^M,
v:=KWin k - t.
```

The full simple-window CFIR equation is

```text
v = Lambda_L k + O_T(L^B).                            (1)
```

## 3. Projective and scalar parts

The projective gate is

```text
P_k^perp v = O_T(L^B).
```

The scalar recovered from the projective line is

```text
lambda_win = <k,v>/<k,k>.                             (2)
```

Thus `SCALAR-CONS` is equivalent to

```text
<k,v> = Lambda_L <k,k> + O_T(L^B ||k||).              (3)
```

Substituting `v=KWin k-t`, the scalar gate becomes the finite energy identity:

```text
<k,KWin k> - <k,t> - Lambda_L <k,k>
= O_T(L^B ||k||).                                    (4)
```

## 4. Why this is useful

Equation (4) is not a rowspace statement and not a fitted-scalar statement.  It is a scalar quadratic
identity involving:

```text
1. the Cauchy interpolation matrix KWin;
2. the residue vector k=J_TG_x;
3. the signed finite tail t;
4. the independent Feshbach coefficient Lambda_L.
```

It can therefore be attacked by the coupled explicit formula as an energy balance.  In particular,
it is the scalar part that the alternating residue matrix cannot see.

## 5. Relation to full CFIR

Define the full residual

```text
r_L := v - Lambda_L k.
```

Then

```text
||r_L||^2
= ||P_k^perp v||^2
 + |<k,v>/<k,k>-Lambda_L|^2 ||k||^2.                 (5)
```

Thus:

```text
PCFIR controls the first term;
SCALAR-ENERGY controls the second term.
```

Together they are exactly `CFIR-H`.

## 6. Non-circular target

The proof-facing scalar target is:

```text
SCALAR-ENERGY:
<k,KWin k> - <k,t> = Lambda_L ||k||^2 + O_T(L^B||k||).
```

This must be proved using the transformed Feshbach/explicit-formula identity that defines
`Lambda_L`, not by setting `Lambda_L=lambda_win`.

## 7. Status

```text
proved: SCALAR-CONS is equivalent to the finite energy identity (4);
proved: full CFIR residual decomposes as projective defect plus scalar-energy defect;
open: prove SCALAR-ENERGY for Xi-zero windows from the coupled identity.
```
