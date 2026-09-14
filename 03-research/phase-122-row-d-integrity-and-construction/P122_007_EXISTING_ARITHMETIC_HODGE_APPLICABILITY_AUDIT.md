# P122.007 — applicability of existing arithmetic Hodge-index theorems

## Verdict

The classical arithmetic Hodge-index theorems do not apply to the row-A
spherical square or the row-B decorated correspondences.  Their hypotheses
identify exactly what a new D would have to construct, but they cannot be
imported as the missing sign theorem.

## 1. Standard theorem and hypotheses

In the Faltings--Hriljac--Moriwaki form, and in the adelic extension of
Yuan--Zhang, the input is a regular projective arithmetic variety

\[
 \pi:\mathcal X\longrightarrow\operatorname {Spec}O_K
\]

with geometrically connected generic fibre of relative dimension at least
one, an arithmetically ample or nef Hermitian/adelic line bundle `L`, and an
integrable Hermitian/adelic line bundle `M` whose generic intersection with
`L^(n-1)` vanishes.  The conclusion is

\[
 \overline M^2\,\overline L^{,n-1}\le0,
\]

with a classified equality case.  Gillet--Soule's arithmetic Chow theory
likewise starts with regular quasi-projective arithmetic varieties and
Hermitian geometric data.

## 2. Hypothesis map to the repository

| standard hypothesis | repository object | status |
|---|---|---|
| regular noetherian arithmetic variety | sheafified `S`-algebra/Segal-Gamma carrier `Y_S` | not an object of the theorem's category |
| projective morphism to `Spec O_K` with relative dimension >=1 | noncollapsed Day-smash square | no such morphism or generic algebraic fibre constructed |
| arithmetic Chow group/intersection product | external ruling line tensor law plus nuclear contact | mixed product not constructed |
| Hermitian/adelic line bundle representing every `M_f` | decorated Witt/nuclear object | not constructed |
| ample/nef polarization | ruling degree/effective data on a restricted sector | no positivity notion on completed mixed classes |
| primitive generic intersection condition | two Mellin/Tate evaluations | analytic analogue, not identified with an arithmetic intersection |
| equality classification | phase-121 oriented defect | absent; this is the open theorem |

Every load-bearing geometric hypothesis fails to type-check before one even
asks whether its inequality is sharp enough.

## 3. Why ordinary realization does not repair the mismatch

For ordinary schemes,

\[
 \operatorname {Spec}\mathbb Z
 \times_{\operatorname {Spec}\mathbb Z}
 \operatorname {Spec}\mathbb Z
 \simeq\operatorname {Spec}\mathbb Z.
\]

Thus a realization that simply forgets the spherical structure collapses
the proposed square; it does not produce a relative-dimension-one
arithmetic surface.  Paper 42's infinite-rank contact theorem supplies an
independent obstruction: the mixed nuclear pairing cannot factor through
the two-dimensional ruling quotient left by such a collapse.

Choosing an unrelated arithmetic surface over `Spec Z` would meet the
ambient type but would add an arbitrary generic curve and still require a
construction sending every decorated `Gamma_n` to a line/cycle with the
exact Lambda contact and composition.  No such functor exists in the
repository.

## 4. Consequence for D

The geometric route is genuinely new mathematics.  At minimum it needs
either:

1. a recognition theorem turning the spherical/IDN carrier into a class of
   generalized arithmetic surfaces with Chow groups, products and degree;
   or
2. a new Hodge-index theorem stated directly in the stable
   periodic--Deligne--nuclear category.

In both cases the theorem must cover the infinite-rank mixed sector and
recover the standard surface theorem over function fields.  Merely citing
arithmetic Hodge index after calling `Y_S` a surface is invalid.

## 5. Research decision

`STANDARD-ARAKELOV-IMPORT: NOT APPLICABLE`.

The existing theorems remain a design template for D-Hodge and for its
equality clause.  They do not discharge any current row-D arrow.
