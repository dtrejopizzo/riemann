# E72.352 - Rowspace invariance of the CFIR defect

## 1. Purpose

E72.350 and E72.351 showed that the finite TailBasis correction and a scalar `Lambda_L`
do not close the shifted CFIR row defect.  A tempting next move is to add the full
transformed eigen-equation row to the incomplete residual row.

This note proves that this cannot repair the row-ideal defect.  Any row which is already
in the rowspace of the singular finite operator is invisible to the defect detector.

## 2. Setting

Let

```text
E = C_E - mu I
```

be the finite Hermitian singular operator and let `xi` be a normalized null vector:

```text
E xi = 0.
```

For a candidate residual row `R`, the row-ideal defect is the null component

```text
def_E(R) = R xi.
```

Because `E` is Hermitian with one-dimensional kernel, this is also the orthogonal
distance from `R` to `Row(E)`, up to the normalization `||xi||=1`:

```text
dist(R, Row(E)) = |R xi|.
```

## 3. The invariance lemma

**Lemma.**  For every row or matrix multiplier `A`,

```text
def_E(R + A E) = def_E(R).
```

Equivalently,

```text
dist(R + A E, Row(E)) = dist(R, Row(E)).
```

**Proof.**

Since `E xi=0`,

```text
(R + A E)xi = R xi + A(E xi) = R xi.
```

This proves the first identity.  For the distance statement, `A E` is itself in
`Row(E)`, so adding it translates `R` along the affine rowspace coset

```text
R + Row(E).
```

The orthogonal projection onto the one-dimensional null direction is unchanged, hence
the rowspace distance is unchanged.  This proves the lemma.

## 4. Consequence for CFIR

The transformed eigen-equation row

```text
k_z E
```

is load-bearing for deriving identities, but it cannot repair a nonzero CFIR residual
after the residual row has already been formed.  It is a rowspace row.  Therefore

```text
R_T  ->  R_T + k_z E
```

leaves `R_T xi` unchanged.

Thus the remaining CFIR closure cannot be:

```text
take the current incomplete interpolation row and add full operator rows.
```

The closure must instead prove that the exact residual row itself is in the row ideal,
or else change the construction of the residual row before testing membership.  The
possible missing pieces are therefore:

```text
exact Hermite interpolation normalization,
exact finite-window node set,
exact TailBasis sign/normalization,
exact balanced kernel used in R_T,
or an additional non-rowspace compatibility identity.
```

But any additive correction of the form `A(C_E-mu I)` is inert for the CFIR defect.

## 5. Numerical certificate

The companion probe adds explicit rows `k_a E` to the defective `window_tail` rows.
The null amplitude is unchanged to roundoff:

```text
base defect:   |R xi|
added defect:  |(R+k_aE)xi|
delta:         |(R+k_aE)xi - R xi| ~ roundoff.
```

This is not a heuristic.  It is the finite numerical shadow of the lemma above.

## 6. Updated endpoint

The next analytic target is now sharper:

```text
prove  R_T(L) in Row(C_E-mu I)
```

for the exact CFIR residual row `R_T`, not for an incomplete row modulo later operator
additions.  The determinant certificate remains the right finite formulation:

```text
R_T adj(C_E-mu I)=0,
det ReplaceRow(C_E-mu I; i, R_T)=0.
```

But E72.352 removes a false escape route: rowspace additions cannot change these
conditions.
