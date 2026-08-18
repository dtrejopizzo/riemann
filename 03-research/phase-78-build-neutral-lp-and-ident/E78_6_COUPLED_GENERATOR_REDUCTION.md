# E78.6 - Coupled-generator reduction of the IDENT comparison object

**Run:** 2026-07-18.
**Scope:** IDENT (`FIXED-L-WEYL`, `SAFE-GAMMA-IDENT`, `OUTER-LIMIT`).

## 1. Purpose

E78.5 reduced `OUTER-LIMIT` to the exact comparison problem

```text
CELL-SMOOTHED-EULER-COMPARISON:
G_L(sigma)  versus  H_L(1/2+sigma).
```

This note shows that the finite/fixed-L side already factors through a single
coupled holomorphic package.  The live fixed-L object is therefore smaller than
the full log-derivative symbol.

## 2. Exact finite package

From P76.041 `(TG-4)`--`(TG-8)`:

```text
T_b(z)=F_{L,N}(z)/(z-d_b),                                      (CG-1)

F_{L,N}(z)=1+W_{L,N}(z),                                        (CG-2)

W_{L,N}(z)=a_{L,N}[U_{L,N}(z)+U_{b,L,N}]
          +b_{L,N}[V_{L,N}(z)+V_{b,L,N}],                      (CG-3)
```

and

```text
F'_{L,N}(z)=W'_{L,N}(z)
=a_{L,N} U'_{L,N}(z)+b_{L,N} V'_{L,N}(z).                      (CG-4)
```

Hence the exact cell-smoothed finite symbol is

```text
J_{L,N}(sigma)
=L coth(sigma L/2)
  +2 Re( i W'_{L,N}(i sigma)/(1+W_{L,N}(i sigma))
        -i/(i sigma-d_b) )
  -B_ext,L,N(sigma).                                           (CG-5)
```

No further Schur object remains hidden: the full finite arithmetic content of
`J_{L,N}` sits in the coupled pair `(W_{L,N}, W'_{L,N})`.

## 3. Reduced fixed-L target

Fix `L` and a safe compact `K subset (1/2,infinity)`.  Define

```text
K_i = { i sigma : sigma in K }.
```

Suppose there exist holomorphic limits `W_L, W_L'` on a neighborhood of `K_i`
such that:

```text
(A) sup_{z in K_i} |W_{L,N}(z)-W_L(z)| -> 0,
(B) sup_{z in K_i} |W'_{L,N}(z)-W_L'(z)| -> 0,                 (CG-6)
```

and suppose also that

```text
(C) inf_{z in K_i} |1+W_L(z)| > 0,                             (CG-7)
```

with the finite denominators eventually nonvanishing on `K_i`.

Then

```text
J_{L,N}(sigma) -> J_L(sigma)                                   (CG-8)
```

locally uniformly on `K`, where

```text
J_L(sigma)
=L coth(sigma L/2)
  +2 Re( i W_L'(i sigma)/(1+W_L(i sigma))
        -i/(i sigma-d_b) )
  -B_ext,L(sigma).                                             (CG-9)
```

Here `B_ext,L,N -> B_ext,L` uniformly on `K` by the explicit formula
`(EM-2)`.

### Proof

By `(CG-6)` and `(CG-7)`, the quotients

```text
W'_{L,N}/(1+W_{L,N})
```

converge uniformly on `K_i` to

```text
W_L'/(1+W_L),
```

because inversion is continuous on functions bounded away from zero.  The terms

```text
L coth(sigma L/2),
-i/(i sigma-d_b),
```

are independent of `N`, and `B_ext,L,N -> B_ext,L` uniformly on `K` by the
explicit mesh tail.  Substituting into `(CG-5)` yields `(CG-8)`--`(CG-9)`.
QED.

## 4. Consequence

The full fixed-L side of IDENT reduces to a smaller coupled holomorphic target:

```text
COUPLED-GENERATOR-LIMIT:
prove uniform convergence of W_{L,N}, W'_{L,N} and a zero-free bound for
1+W_{L,N} on safe compacta.
```

This strictly sharpens the earlier formulation:

```text
full J_{L,N} convergence
```

is no longer the primitive object.

## 5. Relation to the existing fronts

This reduction does not close IDENT by itself, because it still leaves two
candid tasks:

```text
1. identify the limit pair (W_L, W_L') from the coupled cell/Gamma-prime
   equations (SAFE-GAMMA-IDENT side);
2. compare the resulting J_L with the safe Euler truncation H_L
   as L->infinity (OUTER-LIMIT side).
```

But it removes one layer of opacity: the finite/fixed-L part no longer needs to
be attacked through the whole log-derivative symbol.

## 6. Minimal new live object

Combining E78.5 and Section 3:

```text
COUPLED-GENERATOR-LIMIT
+ limit identification of (W_L, W_L')
+ CELL-SMOOTHED-EULER-COMPARISON
=> FIXED-L-WEYL + SAFE-GAMMA-IDENT + OUTER-LIMIT.              (CG-10)
```

So the smallest new fixed-L object is:

```text
COUPLED-GENERATOR-LIMIT.
```

## 7. Status

```text
proved:
  the finite cell-smoothed symbol J_{L,N} factors exactly through the coupled
  holomorphic pair (W_{L,N}, W'_{L,N});

proved:
  convergence of that pair plus a zero-free denominator bound implies the
  fixed-L symbol limit;

reduced:
  FIXED-L-WEYL / SAFE-GAMMA-IDENT on the finite side to
  COUPLED-GENERATOR-LIMIT;

live:
  identify and control the coupled pair
  a_b(U+U_b)+b_b(V+V_b), a_b U'+b_b V';

next:
  inspect whether MR-1 / the two-generator algebra already supplies a finite
  recurrence or shell update for W_{L,N}, and autopsy that route if it again
  turns into a detector.
```
