# Strong-A audit after the internal periodic Kunneth construction

## 1. Closed statements

The following statements now have constructions and proofs.

| Obligation | Construction | Verdict |
|---|---|---|
| Canonical arithmetic carrier for periodic pairs | `Y_per -> X_abs x X_abs`, obtained from the 2026 arithmetic pullback | proved |
| One coefficient geometry rather than a label dictionary | enriched periodic section category and its presheaf topos | constructed |
| Actual invertible divisor objects | Yoneda representables under Day convolution | proved |
| Principal descent | objects use periodic divisor classes; translations give representable isomorphisms | proved |
| Internal global sections | `Map(y(0),y(x))` | proved by enriched Yoneda |
| Kunneth | enriched Hom is the reduced periodic external tensor | proved, natural and multiplicative |
| Coefficient-one continuous dimension | finite-depth extremal product plus the two published Frobenius limits | proved |
| Perfect finite-depth cohomology realization | real linearization of canonical extremal rays | constructed |
| Determinant of that cohomology | ordinary determinant of the perfect extremal complex, followed by the based Frobenius limit | proved |
| Finite contact determinant | determinant of `[Z --p--> Z]` on the diagonal components | proved |
| Green comparison | determinant quotient in based normed lines | proved |
| Exact arithmetic composition/contact | nuclear Dirichlet coefficient sheaf, free rank three over its nuclear algebra | proved |

The raw spherical Kunneth route is no longer an open item.  It is false:
the assembly quotient gives the lower bound

`dim_S(H_m smash_S H_n)>=2^(s(n))-1`,

which is exponential on Arakelov rays.  The periodic coefficient topos is
therefore a necessary separated replacement, not a second unverified
candidate for the same raw functor.

## 2. Two notions that must not be conflated

There are now two precise carriers.

1. The absolute spherical square has the literal product structure sheaf
   and genuine external divisor modules, but its raw section dimension is
   too large.
2. The periodic coefficient topos lies canonically over the arithmetic
   pair pullback and has the correct internal Kunneth cohomology and
   determinant.

There is a canonical comparison at the level of the pair pullback and at
the level of the negabinary mixed block.  There cannot be an equivalence
which identifies the full raw spherical section functor with periodic
cohomology, because their dimensions have different growth orders.  Any
statement of equivalence would contradict the exponential lower bound.

Thus the correct unified object is the pair

`(absolute carrier, separated periodic coefficient topos over it)`,

analogous to a space equipped with a selected cohomology theory.  It is not
the claim that all raw bounded functions are cohomological sections.

## 3. The finite-rank clause

The finite-rank contact theorem proves that no additive numerical group of
finite rank can simultaneously contain all `Gamma_n`, satisfy

`Gamma_m o Gamma_n=Gamma_(mn)`,

and have diagonal contact `Lambda(n)`.  The prime submatrices

`Lambda(p_i p_j)=delta_(ij)log p_i`

have arbitrary rank.

Consequently the literal Weil-column demand for a finitely generated
Neron--Severi group cannot be appended to the closed package.  This is not
a remaining construction gap.  It is inconsistent with the already
required exact arithmetic contact.  The coherent replacement is finite
type over the nuclear arithmetic algebra, which has been constructed and
retains every prime direction.

## 4. Exact verdict

The nuclear/periodic strong replacement is complete for the obligations in
Section 1: carrier, invertible coefficient lines, internal Kunneth,
quadratic continuous dimension, perfect extremal determinant, finite
contact and Green comparison.

The original finite-rank Weil row is not constructible with exact
von-Mangoldt contact.  Therefore the unqualified sentence “the original
strong row A is constructed complete” would be false.  The strongest true
sentence is:

> The canonical nuclear-periodic row A is constructed complete; its exact
> arithmetic correspondence module is finite free over the nuclear
> Dirichlet algebra, while no finite-rank abelian numerical replacement can
> preserve the same composition and contact.

No assertion in this verdict is conditional on a future Kunneth or
determinant theorem.

