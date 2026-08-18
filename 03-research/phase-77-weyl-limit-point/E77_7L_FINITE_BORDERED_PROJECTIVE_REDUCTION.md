# E77.7l - Finite bordered projective reduction

**Run:** 2026-07-18.

## 1. Purpose

After E77.7i--k, the open LP interface is

```text
BORDERED-WEYL-COMPLETENESS.
```

Before attacking the infinite theorem, it is useful to isolate what the
Phase 76 ledger already proves at the **finite, nonsingular** level.  This
note records that content precisely.

## 2. Finite bordered scalar already reduced to a normalized pair

Fix a safe reference `z_0`.  P76.052 and P76.054 define

```text
G=B(z_0)^(-1),
g=G e_last,
w=G[:,D] R_0^(-1) (G e_last)_C,
```

with `D` the two deleted rows and `C` the two deleted columns.  The key
exact identities are:

```text
r(z_0)g = 1,
r(z_0)w = 0,                                    (L-1)

theta_N(z) = r(z)w / r(z)g.                     (L-2)
```

Here `g` is the canonical normalized bordered solution and `w` is the
canonical shell-forced directional correction.  No ambient inverse norm is
used in `(L-1)`--`(L-2)`.

Thus the finite shell ratio is already a projective scalar attached to one
normalized pair.

## 3. Finite transfer increment is a 2x2 minor ratio

P76.051 and P76.052 also give the exact complementary-minor reading

```text
[T_{N+1}(z)/T_N(z)] / [T_{N+1}(z_0)/T_N(z_0)]
 = det R_N(z_0) / det R_N(z),                   (L-3)
```

where `R_N(z)` is the `2x2` deleted-row/deleted-column block of
`B_{N+1}(z)^(-1)`.

So the finite shell increment is controlled by a normalized `2x2`
projective quantity, not by full determinants or ambient inverse norms.

## 4. What this proves toward the LP interface

At every finite section for which `B(z_0)` is invertible, the ledger already
proves:

```text
1. existence of a canonical normalized bordered solution g;
2. existence of a canonical directional partner w with zero normalization;
3. the safe scalar theta_N is their projective ratio;
4. the finite transfer quotient is encoded by a 2x2 complementary minor.
```

This is exactly the finite algebraic core needed for any bordered Weyl
interpretation.

## 5. What it does not yet prove

The following are still open and are not supplied by P76.051--P76.054:

```text
1. nested/nonempty disks for one fixed infinite realization;
2. treatment of singular finite sections;
3. identification of the finite projective objects with the full class of
   normalized l2 solutions of the infinite equation;
4. local-uniform transfer from the mu_L pencil to the mu=0 P76.065 family;
5. simplicity and nonvanishing at the ground eigenspace.
```

So P76.051--P76.054 prove the **finite projective reduction**, but not
`BORDERED-WEYL-COMPLETENESS`.

## 6. Candid partial chain

The safe interface now decomposes as:

```text
finite bordered projective reduction
 + singular-section regularization
 + infinite realization / nesting / intersection theorem
 + mu_L <-> mu=0 pencil compatibility
 + ground-space simplicity/nonvanishing
=> BORDERED-WEYL-COMPLETENESS.
```

This is smaller and more accurate than treating the entire interface gap as
one undifferentiated theorem.

## 7. Next live object

The smallest next interface theorem is:

```text
FINITE-TO-INFINITE-BORDERED-COMPATIBILITY:
the finite projective scalar theta_N, defined by the canonical pair
(g,w), is exactly the boundary-relation coordinate of one fixed infinite
bordered realization, including the regularized singular sections.
```

Then:

```text
FINITE-TO-INFINITE-BORDERED-COMPATIBILITY
 + BTG-DIV-L
 + ground-space simplicity/nonvanishing
=> BORDERED-WEYL-COMPLETENESS.
```
