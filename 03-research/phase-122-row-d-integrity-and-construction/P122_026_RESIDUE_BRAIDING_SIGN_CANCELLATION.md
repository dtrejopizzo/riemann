# P122 -- the quadratic-reciprocity-looking residue sign cancels

## Status

`PROVED-IN-REPOSITORY`.  Iterated affine residue decomposition produces a
tensor-flip sign which, for odd primes, has the quadratic reciprocity
exponent.  The arithmetic mixed-radix relabellings on the two sides have
the same sign, so the canonical coherence map has sign `+1`.  No new
oriented `mu_2` anomaly survives.

## 1. The apparent sign

Take positive integers `p,q`.  Transposing a `p` by `q` array changes the
top exterior power by

\[
 \operatorname {sgn}(\mathrm{flip}_{p,q})
 =(-1)^{\binom p2\binom q2}.                       \tag{1.1}
\]

Indeed an inversion is determined by two different rows and two different
columns.  If `p,q` are odd primes, (1.1) becomes

\[
 (-1)^{(p-1)(q-1)/4},                              \tag{1.2}
\]

the sign occurring in quadratic reciprocity.  Taken alone, this looks like
an orientation anomaly between “decompose by `p` then `q`” and the reverse
order.

## 2. Arithmetic residue labelling carries the same sign

In the affine carrier, the first iterated decomposition labels residues
modulo `pq` by

\[
 f(r,s)=r+ps,qquad 0\leq r<p,quad0\leq s<q,       \tag{2.1}
\]

with lexicographic order `(r,s)`.  The second labels them by

\[
 g(s,r)=s+qr,qquad 0\leq s<q,quad0\leq r<p,       \tag{2.2}
\]

with lexicographic order `(s,r)`.

### Proposition 2.1

Relative to the increasing order `0,...,pq-1`,

\[
 \operatorname {sgn}(f)=operatorname {sgn}(g)
 =(-1)^{\binom p2\binom q2}.                       \tag{2.3}
\]

#### Proof

For (2.1), two lexicographically ordered pairs with `r<r'` form an
inversion exactly when `s>s'`: then
`p(s-s')>r'-r`.  There are independently `binom(p,2)` choices of rows and
`binom(q,2)` choices of columns.  Pairs in a common row create no
inversion.  This proves the first equality.  Interchanging `p,r` with
`q,s` proves the second.  QED.

### Corollary 2.2 -- canonical determinant coherence is even

The determinant sign comparing the two arithmetic decompositions inside
the common ordered residue basis is

\[
 \boxed{
 \operatorname {sgn}(f)\operatorname {sgn}(g)^{-1}=+1.} \tag{2.4}
\]

Thus the apparent flip sign (1.1) is exactly compensated by the residue
relabelling required to map both tensor orders back to the same integer
basis.

## 3. Consequence for D

There is no canonical cross-prime `mu_2` anomaly in the affine determinant
line at this level.  Keeping (1.1) while omitting either `f` or `g` forgets
part of the arithmetic coherence and creates a convention-dependent sign.

This does not say that quadratic reciprocity is absent from richer tame
symbols or metaplectic extensions.  It says precisely that the elementary
top-exterior-power braiding of the P122.024 residue decomposition cannot
provide the missing port orientation or Gate S.

```text
tensor flip sign                              reciprocity exponent
first mixed-radix relabelling sign            same exponent
second mixed-radix relabelling sign           same exponent
canonical p--q residue coherence sign          +1
new cross-prime determinant anomaly            NONE
```
