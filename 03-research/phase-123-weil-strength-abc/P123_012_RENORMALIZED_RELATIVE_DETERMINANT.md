# P123.012 — the renormalized relative determinant at the identity

## Status

`IMPORTED + PROVED APPLICATION` for the trace-class cutoff determinant and
its renormalized limit on compactly supported semilocal tests.

`PROVED-IN-REPOSITORY` for additivity, dagger reality, cyclicity and gauge
(inner/principal) invariance of the limiting determinant character, and for
the induced determinant biextension on the numerical test quotient.

`OPEN` for identifying gauge equivalence with scalar DC Cartier principal
equivalence and for extending the determinant to the entire rapid label
completion.  The latter belongs to the summability gate of row C.

## 1. Exact imported analytic input

For the local theorem, Connes proves that for compactly supported `h` the
cutoff operator

```text
A_(Lambda,v)(h)=R_Lambda U(h)                         (1.1)
```

is trace class and computes its trace asymptotic.  This is Theorem 3 of
*Trace formula in noncommutative geometry and the zeros of the Riemann zeta
function*, arXiv:math/9811068, Section V:
<https://arxiv.org/abs/math/9811068>.

The semilocal version used here is the theorem and normalization audited in
P123.004:

```text
Tr(A_(Lambda,S)(h))
 =2h(1)log Lambda+T_S(h)+o(1).                        (1.2)
```

Only the geometric/local side of this theorem is used.  No spectral sum
over zeros is invoked.

## 2. Finite-cutoff determinant

If `A` is trace class, `exp(A)-1` is trace class and the Fredholm
determinant satisfies

```text
det_F(exp A)=exp(Tr A).                               (2.1)
```

Define the generic-orbit-renormalized determinant scalar

```text
d_(Lambda,S)(h)
 =det_F(exp(A_(Lambda,S)(h)))
  exp(-2h(1)log Lambda).                              (2.2)
```

The second factor is the inverse determinant character of the regular
generic orbit.  It is fixed before evaluating the finite remainder.

### Theorem 2.1 — identity relative determinant

The limit

```text
d_S^rel(h)=lim_(Lambda->infinity)d_(Lambda,S)(h)       (2.3)
```

exists, is nonzero, and equals

```text
d_S^rel(h)=exp(T_S(h)).                               (2.4)
```

### Proof

Apply (2.1) to (2.2), take logarithms, and use (1.2).  The exponent tends
to `T_S(h)`, and the exponential never vanishes.  QED.

Thus the renormalized identity contribution is an actual limit of
Fredholm determinants of trace-class cutoff operators, not a line named
after a previously desired scalar.

## 3. The based relative line

Let `Pic_b(C)` be the Picard groupoid of based one-dimensional complex
lines.  Define

```text
Det_S^rel(h)=(C,s_h),
s_h=d_S^rel(h) in C^times.                            (3.1)
```

The construction carries canonical multiplication isomorphisms

```text
Det_S^rel(h+k) ~=Det_S^rel(h) tensor Det_S^rel(k),     (3.2)
```

because trace is linear and hence
`d_S^rel(h+k)=d_S^rel(h)d_S^rel(k)`.  At finite cutoff this follows from

```text
det_F(exp A exp B)=det_F(exp A)det_F(exp B)            (3.3)
```

for trace-class perturbations, whether or not `A` and `B` commute.  The
generic countercharacters multiply as well.

The source star-reality proved in P123.007 gives

```text
Det_S^rel(h^dagger) ~=conjugate(Det_S^rel(h)).         (3.4)
```

For convolution tests, cyclicity gives

```text
Det_S^rel(f star g) ~=Det_S^rel(g star f).             (3.5)
```

## 4. Determinant biextension of the mixed intersection

For test correspondences `f,g`, set

```text
L_S(f,g)=Det_S^rel(f star g^dagger).                  (4.1)
```

It is additive in `f`, conjugate-additive in `g`, Hermitian under exchange,
and its logarithmic determinant character is

```text
log d(L_S(f,g))=I_A(f,g).                             (4.2)
```

All assertions follow from (3.2)--(3.5).  If `f` lies in the numerical
radical of P123.007, (4.2) vanishes for every `g`; hence (4.1) has the unit
basing and descends to a nondegenerate determinant biextension on the
numerical test quotient.

This line supplies the missing relative determinant at the identity label
and, in fact, applies to every compactly supported test `h`.  P123.009
identifies the geometric excess line underlying each off-identity local
integrand.  The semilocal theorem **adds** those local Lefschetz numbers;
exponentiation in (2.4) then tensors their exponential determinant
characters.  It does not multiply the raw local Jacobians.

## 5. Principal/gauge invariance in the kernel category

The natural principal transformations of an operator-kernel category are
changes of trivialization by an invertible multiplier.  If `a` is such a
multiplier and the commutators remain in the trace domain, put

```text
h^a=a star h star a^(-1).                             (5.1)
```

Cyclicity gives `T_S(h^a)=T_S(h)`, so

```text
Det_S^rel(h^a) ~=Det_S^rel(h).                        (5.2)
```

The isomorphisms compose because conjugations do.  This proves principal
invariance in the chosen noncommutative correspondence category.

It does **not** solve the different scalar-DC problem closed by
107.240: continuous DC potentials do not descend as scalar Cartier lines
on the Scaling quotient.  Equating (5.1) with that nonexistent scalar
principal relation would be false.  The phase-123 route is explicitly the
surviving higher-rank/operator alternative.

## 6. Stabilization and cutoff independence

For a compactly supported test, P123.004 proves stabilization after a
finite set of places.  Therefore the based lines (3.1) have canonical
identifications after support stabilization.  An admissible phase-space
cutoff producing the same normalized asymptotic (1.2) gives the same limit
(2.4).  This is the precise cutoff-independence assertion; arbitrary
counterterms are not allowed.

## 7. What this closes in A.5/A.8

The two singularity types now both have determinant realizations:

```text
q!=1: local perfect inverse excess [1-q^-1]           (P123.009)
all h: relative Fredholm trace determinant            (this note)
q=1:  generic-orbit countercharacter in that determinant.
```

For every finite compactly supported test packet, diagonal trace,
renormalized determinant, dagger, cyclicity and gauge invariance are joined.
This closes the identity gap in A.5 and the finite-packet determinant gap
in A.8.

The full A.8 clause is still not green because:

1. the determinant is not yet proved continuous on the complete rapid
   infinite-label space;
2. comparison with the pre-existing intrinsic periodic cohomology
   determinant is proved only on its hyperbolic Tate/ruling realization,
   not as an equivalence of pro-perfect cohomology objects;
3. effective compatibility after the final numerical completion remains
   open.

These are now completion/comparison questions, not missing local
determinants.
