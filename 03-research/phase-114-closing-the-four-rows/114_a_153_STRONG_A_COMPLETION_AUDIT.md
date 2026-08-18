# Strong row A: requirement-by-requirement completion audit

## Objective under audit

The requested object must simultaneously internalize the valuative section
theory on the regularized Haran square, contain external and mixed divisor
classes, carry internal sections and Riemann--Roch, preserve exact
correspondence composition and diagonal contact, and have the integral
finite-rank numerical quotient required by the Weil row.

## Audit matrix

| Requirement | Evidence | Status |
|---|---|---|
| Literal non-additive square | The supportwise regular pro-square and its nonzero cross defect are proved in paper 42 | proved |
| Regular reflection, localization, gluing and pro-compatibility | Small congruence reflector, localization comparison and bounded monotone pro-bundles | proved for the carrier |
| Prime-generated metrized Cartier sector | Boundary norm and anti-diagonal detection | proved |
| Reduced prime contact | The torsion complex `[Z --p--> Z]` has determinant mass `log p` | proved |
| External periodic section packet | Pairwise periodic tensors and continuous dimension `d1 d2` | proved externally |
| Intrinsic valued structure sheaf on the Haran square | No operation-preserving valued target carrying both non-interchanging ruling sums has been constructed | missing |
| Internal `R Gamma` | The existing packet is indexed by prime pairs and is not obtained by descent from the four Haran charts | missing |
| Local--global principal formula for mixed fractions | Projection along `Div = Prin direct-sum D_pr` gives sectorial descent, not local mixed valuations | missing |
| Mixed correspondences as divisor classes | They presently live in the cohomological/contact category, not in the internal Cartier group | missing |
| Internal surface Riemann--Roch and determinant | The coefficient-one formula belongs to the external periodic category | missing |
| Internal intersection containing composition and exact contact | Impossible together with finite numerical rank by the finite-rank contact theorem | contradicted |
| Finite-rank integral numerical quotient | The faithful prime lattice already has zero integral radical; exact mixed contact gives a second independent unbounded-rank obstruction | contradicted |

## Carrier technology cannot remove the contradiction

Assume, for the sake of the audit, that a new bi-operadic valued target has
been constructed and that all sheaf, descent, tensor and cohomological
problems have been solved.  Let `L` be the resulting integral numerical
correspondence group.  If it has finite rank, contains the internal mixed
classes `Gamma_n`, and transports composition and diagonal contact, then

`H_(m,n) = Delta . (Gamma_m o Gamma_n) = Lambda(mn)`

factors through `L tensor R`.  On distinct primes `p_1,...,p_r`, its
prime-by-prime submatrix is

`diag(log p_1,...,log p_r)`,

which has rank `r`.  Since `r` is arbitrary, `L` cannot have finite rank.
This contradiction is independent of the chosen sheaf language, valuation,
topos, hyperfield, blueprint or bi-operad.

Separating a finite external Neron--Severi group from an infinite
correspondence space does not satisfy the objective.  If a comparison map
internalizes every correspondence and preserves the two operations, the
same rank contradiction applies to its image.  Without that map, the two
objects remain externally coupled and the requested single divisor and
intersection theory has not been constructed.

## Terminal verdict

The exact objective is not merely unfinished: two of its required clauses
are mutually inconsistent.  Therefore no mathematical construction can
satisfy all of them simultaneously.  A coherent new objective must change
at least one of:

1. finite integral numerical rank;
2. exact multiplicative composition and von Mangoldt contact;
3. internalization of all mixed correspondences in one numerical divisor
   theory.

Retaining the exact explicit-formula arithmetic forces the first change: the
mixed numerical correspondence space must be infinite-rank/topological or
nuclear.  That revised programme would still require a new internal valued
section theory, but it would no longer be logically contradictory.
