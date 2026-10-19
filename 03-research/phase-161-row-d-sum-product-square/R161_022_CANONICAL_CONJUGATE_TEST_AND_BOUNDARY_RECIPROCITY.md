# R161_022 — Canonical conjugate test and the exact boundary reciprocity remainder

## 0. Verdict

The conjugate test requested in `R161_021` need not be guessed and need not use an inverse of the primitive Weil
operator.  On the common product graph it is canonically

```
H_F=Pi_T P_T Z* g,                                               (0.1)
```

where `Z` is the causal zeta synthesis, `g` is the corrected right product port, and `Pi_T` is the orthogonal
projection onto the two-Tate primitive space.  This test is primitive, so first-contact radicality annihilates its
pairing with `F`.

The price is an explicit boundary remainder. The desired extremal correlation is exactly the sum of one interior
Tate term and two exterior pairings. The crossed polar correction fixes the first term uniquely, but does not by
itself cancel it. The remaining mathematical identity would have to be an exterior Green reciprocity between the
Weil leakage and the exterior part of the functional-equation defect.

This note proves the decomposition.  It does not assert the exterior reciprocity.

## 1. Abstract first-contact decomposition

Let `P=P_T`, let `Pi=Pi_T` be the primitive projection inside `PL2`, and let `A=A_infinity` be the completed Weil
operator on the common graph.  For a first-contact vector `F=PF`, write

```
AF=r+ell,
r=PAF in Tate_T,
ell=(I-P)AF.                                                     (1.1)
```

Let

```
w=(W_epsilon^0)^vee.                                            (1.2)
```

By `R161_017`, the canonical exterior corrections do not alter the restriction to the physical window, and hence

```
Pw=r.                                                            (1.3)
```

It follows that

```
d:=w-AF                                                         (1.4)
```

is exterior-supported:

```
Pd=0.                                                            (1.5)
```

This is the exact place where first contact enters the scattering defect.

## 2. The canonical pullback test

Let `g` be the corrected right product port, with Mellin transform `G_+^0`, and put

```
y=Z* g.                                                          (2.1)
```

All formulas below are first identities on the common smooth graph; the asserted boundary pairings require their
usual graph limits.  Define

```
H_F=Pi P y.                                                      (2.2)
```

Then `H_F` is supported in `I_T` and primitive.  Since `F` is in the radical of the nonnegative primitive
compression,

```
a_T(F,H_F)=<AF,Pi P y>=0.                                       (2.3)
```

Thus (2.2) is a source-defined conjugate test, not a solution of an equation involving `A^(-1)`.

## 3. Exact boundary-reciprocity formula

The cross defect of `R161_021` is

```
X_T(F)=Re<G_+^0,zeta W_epsilon^0>
      =Re<g,Zw>
      =Re<Z*g,w>
      =Re<y,w>.                                                  (3.1)
```

Let `Tau=I-Pi` on `PL2`; its range is the two-dimensional Tate space.  Decompose

```
y=Pi P y+Tau P y+(I-P)y                                         (3.2)
```

and use `w=AF+d`, (1.1), and (1.5).  The primitive interior term vanishes by (2.3), while the other support
pairings separate.  Therefore:

**Theorem 3.1 (canonical boundary decomposition; PROVED on the common graph).**

```
X_T(F)=Re[
    <r,Tau P y>
   +<ell,(I-P)y>
   +<d,y>
].                                                               (3.3)
```

*Proof.* Starting from (3.1),

```
<y,w>=<y,AF>+<y,d>.
```

Insert (3.2).  The pairing of `Pi P y` with `AF` is zero by (2.3).  The pairing of `Tau P y` with `AF` equals its
pairing with `r`, because it is interior-supported.  The pairing of `(I-P)y` with `AF` equals its pairing with
`ell`, because it is exterior-supported.  Finally `d` is exterior-supported, so retaining `<d,y>` is exact.
Taking real parts proves (3.3). ∎

No positivity, division by zeta, or physical scattering was used.

## 4. What the polar/Tate match actually does

The first term in (3.3) is finite-dimensional:

```
B_T^Tate(F):=Re<r,Tau P Z*g>.                                   (4.1)
```

The coefficients of `r` are the first-contact multipliers `(alpha,beta)`. `R161_009` proves that the polar
coefficients of `g` are the same crossed Tate collar currents and fixes them uniquely. Thus (4.1) is not a new
unknown. However, the crossed Tate matrix is not the positive Gram matrix of the orthogonal projection; phase 121
explicitly distinguishes the two matrices. No cancellation may be inferred merely by inserting that matrix.

The possible remaining assertion is the scalar exterior reciprocity

```
Re[<ell,(I-P)Z*g>+<d,Z*g>]=0.                                  (4.2)
```

Equation (4.2) is strictly typed:

- `ell=(I-P)AF` is the exterior Weil leakage isolated in `R161_005`;
- `d=W_epsilon^0^vee-AF` is the exterior functional-equation defect;
- `Z*g` is the adjoint pullback of the right product port.

It is not an abstract consequence of support, since all three entries have exterior pieces.  It is the exact
Green-type identity which finite `(PC-ren)` must prove if this route closes.

## 5. Finite admissible approximation

The formal pullback `Z*g` has a canonical finite version.  Let `g_(M,N)` be the right-oriented port obtained before
the two Poisson orientations are recombined and put

```
y_(M,N)=(S_N^ren)* g_(M,N),
H_(M,N,T)F=Pi_T P_T y_(M,N).                                    (5.1)
```

Then `H_(M,N,T)F` is primitive for every finite `M,N`, so

```
a_T(F,H_(M,N,T)F)=0                                             (5.2)
```

on a first-contact radical.  The remaining analytic task is not to prove (5.2), which is automatic, but to prove
that the finite analogue of the right side of (3.3), with the explicit continuum counterterm retained, converges
to `X_T(F)` and that `(PC-ren)` cancels its boundary remainder.  This is exactly L161.5 in a now canonical gauge.

The definition of `g_(M,N)` must be taken from the separated finite `(PC-ren)` expansion.  Defining it by projecting
the limiting `g` backward would merely assume the required graph convergence.

## 6. Closure if reciprocity is proved

If an independent finite boundary law cancels the complete right side of (3.3), then `X_T(F)=0`. The chain is then
entirely proved:

```
X_T(F)=0
 -> (I+epsilon C_log)g=0                 by R161_021
 -> F=0                                 by R161_019
 -> no first contact
 -> row D                               by nesting and the cofinal theorem.
```

## 7. Status

- canonical primitive conjugate test `Pi P Z*g`: **PROVED on the common graph**;
- exterior support of `d=w-AF`: **PROVED**;
- exact three-term boundary decomposition (3.3): **PROVED**;
- finite admissible gauge (5.1): **DEFINED, graph convergence OPEN**;
- crossed Tate coefficients in (3.3): **FIXED, BUT NO STANDALONE CANCELLATION**;
- exterior Green reciprocity (4.2) from finite `(PC-ren)`: **OPEN / TERMINAL**;
- row D: **OPEN**.
