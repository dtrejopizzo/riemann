# 114.a.151 — The strong row-A specification is inconsistent

## Purpose

This note tests the *simultaneous* requirements imposed on a Weil-strength
row (a).  It does not test one particular carrier.  The conclusion is a
finite-rank obstruction that applies before questions of sheaves,
regularization or continuous dimension arise.

## The finite-rank contact theorem

Let `L` be an abelian group and suppose that:

1. `L` has finite rank `rho`;
2. there are classes `Gamma_n in L` for all positive integers `n`;
3. composition of correspondences induces a biadditive operation on `L`
   and `Gamma_m o Gamma_n = Gamma_(mn)`;
4. intersection with the diagonal is an additive functional
   `ell : L -> R` satisfying `ell(Gamma_n)=Lambda(n)`.

Then these four properties are incompatible.

### Proof

Tensor `L` with `R` and quotient torsion.  Left composition by `Gamma_m`
defines a linear endomorphism of the vector space `L_R`, whose dimension is
at most `rho`.  More directly, the matrix

`H_(m,n) = ell(Gamma_m o Gamma_n) = Lambda(mn)`

factors through `L_R`: its `n`-th column is the evaluation of the linear
functional `x |-> ell(x o Gamma_n)` on the vectors `Gamma_m`.  Therefore
every finite submatrix of `H` has rank at most `rho`.

Choose distinct primes `p_1,...,p_r`.  On the rows and columns indexed by
these primes,

`H_(p_i,p_j) = Lambda(p_i p_j)`.

This is zero for `i != j`, while

`H_(p_i,p_i) = Lambda(p_i^2) = log p_i`.

The resulting diagonal matrix has rank `r`.  Since `r` is arbitrary, `H`
has unbounded finite rank, contradicting finite `rho`.  QED.

The proof uses no zero of zeta and no positivity statement.

## Consequences

The following desiderata cannot all be part of one definition:

* a finitely generated integral Neron--Severi group (or any finite-rank
  additive numerical correspondence group);
* a class for every arithmetic Frobenius label;
* bilinear correspondence composition with the multiplicative label law;
* diagonal intersection equal to the exact von Mangoldt mass.

Passing to numerical equivalence does not help if composition and diagonal
intersection descend: the same factorization takes place in the numerical
quotient.  Adding mixed divisors only enlarges the source and cannot lower
the ranks of the displayed prime submatrices.

### Separation does not internalize

Let `N` be a finite-rank external Neron--Severi group and let `C` be a
separate infinite-rank correspondence group.  If a comparison

`j : C -> N`

sends every `Gamma_n` to a numerical divisor class and preserves composition
and diagonal contact, the finite-rank contact theorem applies to `im(j)` and
gives the same contradiction.  If no such `j` exists, the correspondences
are not mixed divisor classes in the numerical theory and their contact is
not its internal intersection product.  Thus using two tiers is coherent,
but it is exactly the already acknowledged external coupling; it does not
meet the strong internalization clause.

Consequently one of the following three requirements must be removed:

1. finite numerical rank;
2. exact composition and von Mangoldt contact;
3. internalization of every `Gamma_n` in one divisor/intersection theory.

This obstruction is independent of the earlier prime-Cartier-rank
obstruction.  Even if all vertical prime classes were replaced by a new
finite presentation, the exact correspondence/contact requirements would
again force infinite rank.

Thus there are only three mathematically coherent specifications:

1. retain exact arithmetic contact and use an infinite-rank/topological or
   nuclear correspondence space;
2. retain a finite-rank lattice and replace `Lambda` by a finite-rank
   approximation;
3. retain both objects but do not claim that the finite-rank lattice carries
   the exact correspondence composition and contact pairing.

Only the first can retain the exact explicit formula, and it is not the
finite-rank row stated in the Weil comparison table.

## Why the proposed internalization technologies do not remove the theorem

### The maximal scalar bridge that is well typed

There is a genuine, but strictly scalar, hyperfield bridge.  Let
`T_p = R union {infinity}` be the min-convention tropical hyperfield and put

`v_p(a)=ord_p(a) log(p)`, `v_p(0)=infinity`.

Then

`v_fin : Q -> product_p T_p`, `a |-> (v_p(a))_p`

is a hyperring morphism.  Multiplicativity is the additivity of `ord_p`.
If `v_p(a) != v_p(b)`, the ultrametric equality gives
`v_p(a+b)=min(v_p(a),v_p(b))`; if the values tie, the ultrametric inequality
puts `v_p(a+b)` in the hyper-sum, which is the interval above their common
value.  These maps extend uniquely across every central localization
`Z -> Z[1/N]` because every finite tropical value is multiplicatively
invertible.  The extensions commute with further localization.  Moreover
the image of a prime `q` has the single nonzero finite-place coordinate
`log(q)` at `q`, so prime labels and their masses are retained.

This proves a first comparison theorem on the ordinary scalar skeleton of
every Haran chart.  It is the strongest immediate hyperfield construction:
the target has multivalued addition and therefore is not a commutative
involutive F-ring target.  The scalar maps do not specify images of the
higher-arity operation sets of the literal square and cannot pull back its
rank-one Haran torsors.  Consequently they glue as valuations of scalar
cores, not as a structure sheaf `O_val` on the generalized pro-square.

### Bend relations and ordered blueprints

Ordered-blueprint tropicalization represents extensions of a valuation from
a *single* ordered additive structure.  The literal Haran square has two
non-interchanging higher-arity additive structures.  Selecting either one
forgets the other ruling; imposing a common semiring addition imposes the
interchange relation whose failure detects the mixed direction.  Therefore
the published bend construction does not provide a well-typed base change
of this literal square.  Even if such an enrichment were constructed, the
finite-rank contact theorem above would still apply to its numerical
correspondence quotient.

### Tropical hyperfields

The tropical hyperfield records cancellation at tied valuations and repairs
the elementary failure of an idempotent semiring morphism.  It does not by
itself define images of all Haran operation sets, a rank-one torsor functor,
or descent for the two non-interchanging rulings.  Most importantly, it does
not change the rank argument, which uses only biadditivity, composition and
exact contact after any proposed internalization.

### Fibred topoi

One may form a disjoint or fibred category carrying the Haran charts and the
periodic Scaling-Site modules as two projections.  Without a comparison
geometric morphism and a pullback identification of structure objects, this
is precisely the already constructed external packet, not an internal
section theory.  Declaring the comparison as part of the objects assumes
the missing theorem rather than proving it.

### Dequantization

Dequantization supplies asymptotic valuations of ordinary sums.  It neither
gives an exact functor on the two Haran operation systems nor turns the
unbounded-rank matrix `Lambda(mn)` into a finite-rank matrix.  Consequently
it can be useful only after the finite-rank condition is removed.

## Exact verdict

The existing carrier plus external valuative packet may still be developed
into an infinite-rank internal geometry.  What cannot be constructed is the
object requested by the *simultaneous* strong row-A clauses.  Hence the
phrase “constructed complete” would be false unless the specification is
changed explicitly.  This is a theorem of incompatibility, not an open
verification gap.
