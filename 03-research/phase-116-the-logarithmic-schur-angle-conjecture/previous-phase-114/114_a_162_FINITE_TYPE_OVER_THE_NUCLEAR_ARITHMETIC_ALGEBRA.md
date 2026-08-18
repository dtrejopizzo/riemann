# Finite type over the nuclear arithmetic algebra

## 1. Why the coefficient ring must carry the prime directions

The matrix `Lambda(mn)` has arbitrarily large prime diagonal blocks.  Hence
no finite-rank abelian group can simultaneously contain all `Gamma_n`, carry
their biadditive composition, and retain exact diagonal contact.  This does
not prevent finite *module* rank if the arithmetic label algebra itself is
the coefficient ring.  The distinction is the same one that separates
finite-dimensional vector spaces from their generally infinite underlying
abelian groups.

Let

`C = {a=(a_n): q_r(a)=sum_n |a_n|n^r < infinity for every r}`

with Dirichlet convolution.  The preceding notes prove that `C` is a
commutative unital nuclear Frechet algebra, that `delta_m*delta_n=delta_mn`,
and that

`ell(a)=sum_n a_n Lambda(n)`

is continuous.

## 2. A finite free bivariant module

Define

`N_nuc = C e_1 direct-sum C e_2 direct-sum C e_Gamma`.

It is free of rank three over `C`.  Put

`V_(p,1)=delta_p e_1`,  `V_(p,2)=delta_p e_2`,

and

`Gamma_n=delta_n e_Gamma`.

The third summand is an algebra object under

`(a e_Gamma) o (b e_Gamma)=(a*b)e_Gamma`.

Consequently `Gamma_m o Gamma_n=Gamma_mn` exactly.  The diagonal contact
functional on this summand is `ell_Gamma(a e_Gamma)=ell(a)` and therefore

`ell_Gamma(Gamma_n)=Lambda(n)`.

This is not a finite-rank abelian Neron--Severi group.  It is a finite free
module over the canonical nuclear arithmetic algebra forced by exact
composition.  Its three generators record the two rulings and the mixed
correspondence direction; all arithmetic labels occur as scalars.

## 3. Continuous external and contact forms

Set

`d(a)=sum_n a_n log(n)`.

The estimate `log(n)<=n` gives `|d(a)|<=q_1(a)`, so `d` is continuous.  On
the two ruling summands define

`B_ext((a,b),(a',b'))=d(a)d(b')+d(b)d(a')`.

It has the required prime values

`B_ext(V_(p,1),V_(q,2))=log(p)log(q)`.

On the mixed summand define

`K_Gamma(a,b)=ell(a*b)`.

It is jointly continuous because convolution is jointly continuous and
`ell` is continuous, and

`K_Gamma(Gamma_m,Gamma_n)=Lambda(mn)`.

The direct-sum form

`B_nuc = B_ext direct-sum K_Gamma`

therefore carries the coefficient-one external Riemann--Roch polarization
and the exact mixed arithmetic contact on one finite-type nuclear module.
The two forms are not identified: their difference is still the Green
comparison datum.

## 4. Internal coefficient sheaf

Let `K_nuc_sheaf` be the algebraic sheaf of nuclear correspondence
coefficients constructed from the actual restricted decorated
correspondences on the regularized Haran carrier.  Form the sheaf of modules

`N_nuc_sheaf = K_nuc_sheaf^3`.

It is locally free of rank three as an algebraic
`K_nuc_sheaf`-module.  The actual sections `[Gamma_n]` occupy its third
summand, and the two copies of the globally labelled prime sector occupy the
first two summands.  Composition and contact are sheaf morphisms on the
globally generated nuclear sector by the construction of
`K_nuc_sheaf`; taking three finite copies preserves descent.

Thus the mixed arithmetic directions and the two ruling directions now
belong to a single internal finite-type coefficient module on the carrier.
This closes the algebraic *finiteness-versus-exact-contact* conflict after
the coefficient ring is changed from `Z` to `K_nuc_sheaf`.

## 5. Exact numerical quotient

The radical of the mixed form is `ker J`, where

`J(a)=(a_1,(sum_(k>=1)a_(p^k))_p)`.

The radical of `B_ext` is `ker d direct-sum ker d`.  Since there are no
cross terms between the external and mixed blocks,

`rad(B_nuc)=(ker d)e_1 direct-sum (ker d)e_2 direct-sum (ker J)e_Gamma`.

Hence the separated numerical space is

`(C/ker d)^2 direct-sum (C/ker J)`.

The first two factors are one-dimensional; the last necessarily retains
one independent direction for every prime.  No numerical information is
silently discarded.

## 6. Scope

This theorem supplies a coherent replacement for the impossible clause
"finite-rank abelian numerical group": finite locally free rank over the
canonical nuclear arithmetic coefficient algebra.  It preserves exact
composition, exact `Lambda` contact, both rulings, and internal sheaf
placement.

It does not turn the elements of `N_nuc_sheaf` into ordinary Cartier
divisors, and it does not construct the missing surface `H^1` or a
determinant of cohomology.  Those are separate requirements.  In
particular, this result cannot candidly be described as the original
finite-rank Weil row; it proves the strongest non-contradictory nuclear
finiteness statement currently available.

