# E73.254 - Laplace expansion audit for Cramer numerators

## 1. Purpose

E73.253 reduced the hard coordinate statement to Cramer numerator divisibility:

```text
N_j = O_M(L^-M) det(D_J).
```

This note checks whether `N_j` is small because of a large alternating
cancellation in its Laplace expansion.

## 2. Laplace expansion

Let

```text
b = D_Q xi_L.
```

For the Cramer numerator obtained by replacing column `j` of `D_J` by `b`,

```text
N_j = sum_a b_a Cof_{a,j}(D_J).
```

The audit measures:

```text
termAbs = sum_a |b_a Cof_{a,j}|,
altGain = termAbs/|N_j|.
```

Large `altGain` would indicate that the missing theorem is an alternating
four-term cancellation.

## 3. Result

The observed `altGainB` is generally small.  It is often near `0`, and in the
largest observed cases is only around `1.3` in the tested windows.

Thus the Cramer numerator is not mainly produced by a huge cancellation among
four large Laplace terms.  The Laplace terms are already near the numerator
scale.

## 4. Consequence

The next theorem should not imitate the earlier alternating-rank CFIR
certificate from Phase 72.  The quotient Cramer numerator has a different
structure:

```text
N_j small because b_a=D_Q xi_L is small in the quotient packet,
not because large b_a Cof_{a,j} terms cancel dramatically.
```

So the route returns to the bordered vector:

```text
b = D_Q xi_L.
```

The refined target is:

```text
BORDERED-VECTOR-DIV:
D_Q xi_L = O_M(L^-M) det(D_J) / Cof(D_J)
```

or more concretely, using polynomial cofactor bounds from `GRAM-NONDEG`:

```text
D_Q xi_L = O_M(L^-M)
```

in the quotient packet coordinates.

This is equivalent to `CURV-QUOT-DIV`, but now the determinant audit shows
where the numerator smallness must enter: through `b`, not through Laplace
alternation.

## 5. Status

```text
rejected: large four-term Laplace alternation as the main mechanism;
kept:     Cramer numerator divisibility;
next:     prove smallness of the bordered vector b=D_Q xi_L structurally.
```
