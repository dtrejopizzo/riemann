# E73.253 - Cramer numerator divisibility

## 1. Purpose

E73.251--E73.252 isolated the hard coordinate statement:

```text
MAXMIN-PIV-DIV:
z_{J_*}=O_M(L^-M).
```

Rather than search blindly for a second-layer coborder, this note rewrites the
coordinate statement as four explicit bordered determinant numerators.

## 2. Cramer identity

Let

```text
D_J = D_Q[:,J_*],
b   = D_Q xi_L.
```

Then:

```text
z = D_J^{-1}b.
```

For `j=1,...,4`, let `N_j` be the determinant obtained from `D_J` by replacing
its `j`-th column by `b`:

```text
N_j = det(D_J with column j replaced by b).
```

Cramer's rule gives the exact identity:

```text
z_j = N_j / det(D_J).
```

Therefore, assuming `MAXMIN-NONDEG`, the coordinate divisibility is equivalent
to:

```text
CRAMER-NUM-DIV:
N_j = O_M(L^-M) det(D_J),       j=1,...,4.
```

## 3. Why this is the right finite identity

This removes the need to guess a primitive `Y_j` directly.  The second-layer
coborder becomes a determinant divisibility problem:

```text
the bordered numerator minors vanish super-polynomially relative to the
maximal quotient denominator.
```

The denominator is handled separately by:

```text
QROW-INDEP => GRAM-NONDEG => MAXMIN-NONDEG.
```

The numerator is the remaining spectral Mellin divisibility.

## 4. Relation to earlier minor/cofactor routes

This is not the old adjugate tautology.  The old cofactor routes tried to prove
row membership in the full finite operator rowspace.  Here:

```text
1. D_Q has already quotient-removed the fixed DD-local image;
2. J_* is chosen by the maximal quotient minor;
3. N_j is a bordered minor inside this quotient coordinate system.
```

Thus the target is a quotient-coordinate numerator identity, not a full
rowspace certificate.

## 5. Current route

```text
QROW-INDEP
  => GRAM-NONDEG
  => MAXMIN-NONDEG

CRAMER-NUM-DIV
  + MAXMIN-NONDEG
  => MAXMIN-PIV-DIV
  => CURV-QUOT-DIV
  => scalar WRL.
```

## 6. Status

```text
proved: Cramer identity z_j=N_j/det(D_J);
open:   prove CRAMER-NUM-DIV for the quotient bordered numerators.
```
