# A nuclear numerical correspondence envelope

## Purpose

Finite numerical rank is incompatible with exact multiplicative
correspondences and von Mangoldt contact.  This note constructs a canonical
replacement which keeps both exact structures and has a genuine finiteness
property: it is a nuclear Frechet algebra.

This is a research artifact.  It is not inserted into paper 42 and it does
not yet construct the internal section functor on the Haran square.

## 1. The rapidly decreasing Dirichlet algebra

Let `C` be the vector space of complex sequences `a=(a_n)_(n>=1)` for which

`q_r(a) = sum_(n>=1) |a_n| n^r < infinity`

for every nonnegative integer `r`.  Give `C` the Frechet topology defined by
the increasing family `(q_r)`.

For Dirichlet convolution

`(a star b)_k = sum_(mn=k) a_m b_n`

one has the exact estimate

`q_r(a star b) <= q_r(a) q_r(b)`.

Indeed, absolute convergence and `(mn)^r=m^r n^r` give

`sum_k |sum_(mn=k)a_m b_n| k^r
 <= sum_(m,n)|a_m||b_n|m^r n^r`.

Thus `C` is a commutative unital Frechet algebra.  The point masses
`delta_n` belong to `C`, their finite span is dense, and

`delta_m star delta_n = delta_(mn)`.

Consequently the assignment `Gamma_n -> delta_n` preserves the exact
correspondence composition law.

## 2. Nuclearity

Write `C_r=l^1(N,n^r)`.  Then

`C = projective_limit_r C_r`.

The bonding map `C_(r+2) -> C_r`, after conjugating both weighted `l^1`
spaces to ordinary `l^1`, is the diagonal operator with entries `n^-2`.
It is nuclear because

`sum_(n>=1) n^-2 < infinity`.

The standard Grothendieck--Pietsch criterion for countably normed Köthe
spaces therefore shows that `C` is nuclear.  This replaces algebraic finite
rank by a topological finiteness property stable under the completion needed
for the explicit formula.

## 3. Exact contact

Define

`ell(a) = sum_(n>=1) a_n Lambda(n)`.

Since `Lambda(n)<=log n<=n` for `n>=2`,

`|ell(a)| <= q_1(a)`,

so `ell` is continuous.  The symmetric continuous contact form is

`K(a,b)=ell(a star b)`.

It satisfies, without approximation,

`K(delta_m,delta_n)=Lambda(mn)`

and in particular `ell(delta_n)=Lambda(n)`.

The prime-rank obstruction is now absorbed rather than contradicted: the
quotient by the radical of `K` has infinitely many prime coordinates, but
it is the quotient of a nuclear Frechet algebra by a closed kernel whenever
the coordinate map below is given its image topology.

## 4. Explicit numerical coordinates

For `a in C`, put

`A_p(a)=sum_(k>=1) a_(p^k)`.

The series converges absolutely.  Terms whose indices contain two distinct
primes never contribute to `Lambda(mn)`.  Direct summation gives

`K(a,b)=sum_p log(p) [a_1 A_p(b)+b_1 A_p(a)+A_p(a)A_p(b)]`.

The sum converges absolutely: for every `r>1`, rapid decay gives
`|A_p(a)|=O(p^-r)`, and the same for `b`.

Therefore `K` factors through the continuous coordinate map

`J(a)=(a_1,(A_p(a))_p)`.

Conversely, if `J(a)=0`, the displayed formula gives `K(a,b)=0` for all
`b`.  If `K(a,b)=0` for every `b`, testing against `delta_(p^k)` gives

`log(p)(a_1+A_p(a))=0`

for every `p`, while testing against `delta_1` gives

`sum_p log(p) A_p(a)=0`.

The first identities say `A_p(a)=-a_1`.  Rapid decay forces
`A_p(a)->0` as `p->infinity`, hence `a_1=0` and all `A_p(a)=0`.
Thus

`rad K = ker J`.

The numerical correspondence space is the infinite-dimensional image
`J(C)`, with its quotient nuclear topology and the displayed nondegenerate
form.  Every prime supplies a necessary independent direction, exactly as
the rank theorem predicts.

## 5. What this solves and what remains

This construction gives, canonically and without zeta zeros:

1. a complete nuclear topological algebra generated densely by the actual
   multiplicative labels;
2. exact composition `Gamma_m Gamma_n=Gamma_mn`;
3. a continuous diagonal-contact functional with value `Lambda(n)`;
4. an explicit radical and a separated numerical quotient;
5. a rigorous replacement for finite algebraic rank.

It does not yet give:

1. a valued structure sheaf on the Haran pro-square;
2. mixed Cartier divisor objects rather than completed numerical
   correspondence classes;
3. internal `R Gamma`, effectivity or surface Riemann--Roch;
4. a comparison between its nuclear topology and the periodic continuous
   section dimension.

The next construction must realize `C` as the completed Grothendieck group
or trace-class envelope of an actual category of mixed correspondence
objects on the carrier.  Only after that realization can the section and
Riemann--Roch problem be attacked internally.
