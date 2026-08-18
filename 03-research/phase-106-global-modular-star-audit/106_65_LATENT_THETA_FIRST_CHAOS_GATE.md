# 106.65 — The latent theta lift and the first-chaos gate

## Purpose and verdict

The full theta decomposition of 106.38 keeps the divisible, fractional and
central prime channels, but it is written after the theta indices have been
summed.  This note restores those indices and tests a specific possible
closure: realize the polar gradient as a conditional expectation, or first
chaos, of the complete latent theta gradient.

There are two exact conclusions.

1.  The Gamma, divisible, fractional and central channels have one positive
    latent-variable realization on the integer and rational theta lattices.
    Forgetting the theta marks loses no norm at all, because every marked
    copy over a fixed edge carries the same spatial increment.
2.  No positive conditional-expectation contraction from that lift to the
    polar pair space can satisfy the radical interpolation equations.  The
    equality family forces equality in conditional Jensen for every
    \(K^{(2j)}/K\).  Those functions separate oriented spatial edges.  Hence
    the coupling would have to preserve the edge endpoints.  But the source
    has positive singular mass on every prime-power edge
    \(t-s=\log n\) and \(t+s=\log n\), whereas the polar pair measure is
    absolutely continuous.  This is an exact measure-capacity
    contradiction.  Even after the singular prime part is removed, the
    Gamma endpoint density is too small on remote fixed-displacement
    rectangles.

Thus the theta marks do not produce the missing norm-one map by a Markov,
Palm, Mecke or first-chaos projection.  A surviving contraction must be
globally signed before its norm is estimated.  The result does not prove
the complementary contraction or RH.

## 1. Nonduplication audit

The nearest earlier mechanisms are distinct from the calculation below.

* Documents 104.43, 104.49 and 104.50 use size bias, unit Palm selectors
  and conditional covariance on the abstract independent prime towers.
  Their latent variables are prime exponents; they contain neither the
  spatial theta atoms nor the fractional and central channels.
* Document 104.53 classifies additive polynomial tower identities and shows
  that their connected parts collapse to single-tower cumulants.  The lift
  below is not an additive tower observable.
* Document 106.32 represents an omitted atomwise tail as a conditional
  variance and then proves that every omitted atom is load-bearing.  The
  present lift retains every atom and all the pieces discarded there.
* Document 106.36 rules out lossy canonical paths by radical saturation.
  The obstruction below is sharper for the proposed first-chaos mechanism:
  it identifies the conditional Jensen defect and an incompatible pair of
  endpoint measures.
* Document 106.57 constructs a two-channel Stinespring dilation for the
  intermediate theta defect.  Its radical short is zero.  Here the complete
  four-channel source is lifted, and the failure occurs already at the
  level of a positive source-to-polar coupling.

## 2. Continuous theta atoms and their invariant coordinate

For \(y>0\) and \(x\geq0\), retain the atom of 106.38,

\[
 k_y(x)=\pi y^2e^{5x/2}
 \bigl(2\pi y^2e^{2x}-3\bigr)e^{-\pi y^2e^{2x}}.
 \tag{1}
\]

It is useful to expose its dilation coordinate.  Put

\[
 \phi(t)=\pi t^2(2\pi t^2-3)e^{-\pi t^2}.
\]

Then

\[
 \boxed{k_y(x)=e^{x/2}\phi(ye^x).}                 \tag{2}
\]

Consequently the quantity \(ye^x\) is invariant under

\[
 (y,x)\longmapsto(ny,x-\log n),
\]

and (2) gives the exact scaling

\[
 k_{ny}(x-\log n)=n^{-1/2}k_y(x).                  \tag{3}
\]

For \(x\geq0\),

\[
 K(x)=\sum_{m\geq1}k_m(x).                         \tag{4}
\]

If \(a_n=\log n\) and \(x\geq a_n\), (3) gives

\[
 K(x-a_n)=n^{-1/2}\sum_{j\geq1}k_{j/n}(x).        \tag{5}
\]

All the atoms in (5) are positive on this domain: indeed
\((j/n)e^x\geq j\geq1\), and \(2\pi j^2-3>0\).

## 3. The exact marked four-channel edge measure

Let

\[
 g(u)=\frac{e^{-u/2}}{1-e^{-2u}},\qquad u>0,
\]

and extend the integer atoms evenly by

\[
 \kappa_m(x)=k_m(|x|),\qquad
 K(x)=\sum_{m\geq1}\kappa_m(x).                    \tag{6}
\]

Define four positive, sigma-finite marked edge measures.

### Gamma channel

On \((u,x,\ell,m)\in(0,\infty)\times\mathbb R\times
\mathbb N^2\), put

\[
 d\Omega_\Gamma
 =g(u)\kappa_\ell(x)\kappa_m(x-u)\,du\,dx .       \tag{7}
\]

The endpoints are \(x\) and \(x-u\).

### Divisible and fractional tail channels

For \(n\geq2\), \(x\geq a_n\), and
\((\ell,j)\in\mathbb N^2\), put

\[
 d\Omega_{n,\mathrm{tail}}
 =\frac{2\Lambda(n)}n
   k_\ell(x)k_{j/n}(x)\,dx .                       \tag{8}
\]

The endpoints are \(x\) and \(x-a_n\).  Split (8) into

\[
 \Omega_{n,\mathrm{div}}: n\mid j,
 \qquad
 \Omega_{n,\mathrm{frac}}: n\nmid j .             \tag{9}
\]

Thus the divisible marks are exactly the integer sublattice
\(j/n\in\mathbb N\), and the fractional marks are its complement in the
rational lattice \(n^{-1}\mathbb N\).

### Central channel

For \(0<x<a_n\) and \((\ell,m)\in\mathbb N^2\), put

\[
 d\Omega_{n,\mathrm{ctr}}
 =\frac{\Lambda(n)}{\sqrt n}
   k_\ell(x)k_m(a_n-x)\,dx .                       \tag{10}
\]

The endpoints are \(x\) and \(a_n-x\).

Let \(\Omega_\Theta\) be the orthogonal sum of (7)--(10).  Orient each
edge after replacing its endpoints by their absolute values, and write

\[
 (\nabla_\Theta r)(e)=r(t(e))-r(s(e)),
 \qquad t(e)>s(e)\geq0,                            \tag{11}
\]

for an even multiplier \(r\).

### Theorem 1 — Exact latent theta Dirichlet form

For every even multiplier in the full-kernel form domain,

\[
 \boxed{
 \|\nabla_\Theta r\|_{L^2(\Omega_\Theta)}^2
 =\mathscr E_\Gamma(r)
  +\widetilde{\mathscr E}_p(r)
  +\mathscr X_{\mathrm{frac}}(r)
  +\mathscr X_{\mathrm{ctr}}(r)
 =\mathscr E_K(r).}                                \tag{12}
\]

#### Proof

Summing (7) over \((\ell,m)\) gives

\[
 g(u)K(x)K(x-u)\,du\,dx,
\]

the complete Gamma edge measure.  Summing (8) over the marks and using
(5) gives

\[
 \frac{2\Lambda(n)}{\sqrt n}
 K(x)K(x-a_n)\,dx,
\]

the two reflected tails of the \(n\)-th prime-power edge.  Restricting to
\(n\mid j\) gives

\[
 \frac{2\Lambda(n)}nK(x)^2\,dx,
\]

which is the divisor channel; \(n\nmid j\) gives the fractional channel.
Finally, summing (10) gives the central line of 106.38(7).  Multiplication
by the squared increments in (11), followed by monotone convergence,
proves (12).  \(\square\)

Let \(\partial e=(t(e),s(e))\).  Conditional expectation over the theta
marks at fixed \(\partial e\) leaves (11) unchanged:

\[
 \boxed{
 \mathbb E_{\Omega_\Theta}
 [\nabla_\Theta r\mid\partial]
 =\nabla_\Theta r.}                                 \tag{13}
\]

Therefore the integer/rational theta marks are an exact orthogonal
refinement of the source edge measure.  They do not by themselves create
a smaller first chaos.

## 4. The polar edge law and the first-chaos ansatz

The law of (|X|) for (X\sim\mu_K) is

\[
 d\bar\mu(t)=4h(t)K(t)\,dt,
 \qquad h(t)=\cosh(t/2),\quad t>0.                  \tag{14}
\]

On the oriented pair space

\[
 \mathsf S=\{(t,s):t>s>0\},
\]

define

\[
 \boxed{
 d\rho(t,s)=8h(t)h(s)K(t)K(s)\,dt\,ds.}           \tag{15}
\]

Then, with

\[
 (\nabla_0r)(t,s)=r(t)-r(s),
\]

one has

\[
 \|\nabla_0r\|_{L^2(\rho)}^2
 =\frac12\mathrm{Var}_{\mu_K}(r).           \tag{16}
\]

The most general positive conditional-expectation construction relevant
to this lift can be written as follows.  Let \(Q\) be a positive measure on
(\mathsf S\times\mathsf E_\Theta) such that

\[
 Q_{\mathsf S}=\rho,
 \qquad Q_{\mathsf E_\Theta}\leq\Omega_\Theta.     \tag{17}
\]

Disintegrate (Q(de\mid z)\) over (z\in\mathsf S), and put

\[
 (C_Qv)(z)=\int v(e)Q(de\mid z).                    \tag{18}
\]

Conditional Jensen and (17) give

\[
 \|C_Qv\|_{L^2(\rho)}^2
 \leq\int|v|^2\,dQ_{\mathsf E_\Theta}
 \leq\|v\|_{L^2(\Omega_\Theta)}^2.                \tag{19}
\]

Thus (18) includes conditional expectations, randomized positive paths
after they have been compressed to one source edge, and substochastic
first-chaos selections.  Allowing the second marginal to be smaller than
(\Omega_\Theta) permits the construction to discard unused source mass;
the class is therefore larger than a measure-preserving coupling.

The desired coefficient equation in this class is

\[
 \boxed{C_Q\nabla_\Theta r=\nabla_0r}               \tag{20}
\]

for every multiplier in the form core.

## 5. The exact conditional-covariance defect

For \(Q\) as above and \(v\in L^2(Q_{\mathsf E_\Theta})\), the loss in the
first inequality of (19) is exactly

\[
 \boxed{
 \mathfrak d_Q(v)
 :=\int_{\mathsf S}
 \mathrm{Var}_Q(v(E)\mid Z=z)\,d\rho(z)
 =\int|v|^2\,dQ_{\mathsf E_\Theta}-\|C_Qv\|^2.}    \tag{21}
\]

This is the conditional covariance term which a first-chaos proof would
have to control.  It has a fixed nonnegative sign.

Let

\[
 r_j=K^{(2j)}/K,\qquad j\geq0.                      \tag{22}
\]

The exact radical identity gives

\[
 \|\nabla_\Theta r_j\|_{L^2(\Omega_\Theta)}
 =\|\nabla_0r_j\|_{L^2(\rho)}.                     \tag{23}
\]

If (20) holds, (19) and (23) force equality at both inequalities in
(19).  Hence

\[
 \boxed{
 \mathfrak d_Q(\nabla_\Theta r_j)=0,
 \qquad
 \nabla_\Theta r_j(E)=\nabla_0r_j(Z)quad Q\text{-a.s.}}
 \tag{24}
\]

for every (j\).  They also force

\[
 \int|\nabla_\Theta r_j|^2
 \,d(\Omega_\Theta-Q_{\mathsf E_\Theta})=0.        \tag{25}
\]

Equations (24)--(25) are the simultaneous radical saturation conditions
for a positive first-chaos construction.

## 6. The radical signatures separate edges

The next lemma turns (24) into a geometric constraint.

### Lemma 2 — Edge separation

For \(a,b,c,d\geq0\), \(a\ne b\), and \(c\ne d\), suppose

\[
 r_j(a)-r_j(b)=r_j(c)-r_j(d)
 \qquad\text{for every }j\geq0.                    \tag{26}
\]

Then \(a=c\) and \(b=d\).

#### Proof

For \(a\geq0\), Taylor's formula gives the even analytic germ

\[
 A_a(z)
 :=\sum_{j\geq0}\frac{r_j(a)z^{2j}}{(2j)!}
 =\frac{K(a+z)+K(a-z)}{2K(a)}.                     \tag{27}
\]

The theta series is analytic in the connected strip
\(|\mathrm{Im}\,z|<\pi/4\).  Thus equality of the Taylor germs in
(27) continues throughout that strip, in particular along the entire real
axis.  The family \(\{A_a:a\geq0\}\) is finitely linearly independent.
To see this, take distinct \(0\leq a_1<\cdots<a_m\) and let
\(z\to+\infty\).  The first theta atom gives, uniformly for fixed \(a\),

\[
 K(z-a)
 =C\,e^{9(z-a)/2}e^{-\pi e^{2(z-a)}}(1+o(1)),       \tag{28}
\]

with \(C>0\); the \(K(z+a)\) term is smaller.  Therefore

\[
 \frac{A_{a_k}(z)}{A_{a_m}(z)}\longrightarrow0
 \qquad(k<m).                                      \tag{29}
\]

In a finite linear relation the coefficient of \(A_{a_m}\) must vanish.
Descending induction proves the claimed independence.

Summing (26) with the weights in (27) gives

\[
 A_a-A_b-A_c+A_d=0.
\]

Linear independence says that the signed atomic measures satisfy

\[
 \delta_a-\delta_b=\delta_c-\delta_d.
\]

Since both edges are nondegenerate and oriented, this implies
\(a=c\) and \(b=d\).  \(\square\)

Apply Lemma 2 simultaneously to the countable family in (24).  It follows
that any \(Q\) satisfying (20) and the radical equalities must be supported
on the endpoint diagonal:

\[
 \boxed{\partial E=Z\qquad Q\text{-a.s.}}           \tag{30}
\]

In other words, radical saturation forbids the conditional expectation
from moving a source edge to a different polar edge.

## 7. Singular prime mass gives an exact contradiction

Let

\[
 J=\partial_\#\Omega_\Theta                         \tag{31}
\]

be the unmarked source endpoint measure on \(\mathsf S\).  Its prime part
is supported on the countable union

\[
 \mathcal L_p
 =\bigcup_{n\geq2:\,\Lambda(n)>0}
 \bigl\{t-s=\log n\bigr\}
 \cup
 \bigl\{t+s=\log n\bigr\}.                        \tag{32}
\]

The first family contains the two reflected tails; the second contains
the central crossing channel.  Every component has positive mass.  For
example, on \(t-s=\log n\), its density includes

\[
 \frac{2\Lambda(n)}{\sqrt n}K(t)K(s)\,ds>0.         \tag{33}
\]

By contrast, the polar measure (15) is absolutely continuous, so

\[
 \rho(\mathcal L_p)=0.                              \tag{34}
\]

### Theorem 3 — No positive theta first-chaos contraction

There is no positive measure \(Q\) satisfying (17) and (20) while
preserving the radical equalities (23).  Equivalently, the complete latent
theta gradient does not admit the polar gradient as a positive
conditional-expectation or first-chaos factor.

#### Proof

By (24) and Lemma 2, \(Q\) is endpoint preserving.  Therefore

\[
 Q_{\mathsf E_\Theta}
 \bigl(\partial^{-1}\mathcal L_p\bigr)
 =Q_{\mathsf S}(\mathcal L_p)
 =\rho(\mathcal L_p)=0.                              \tag{35}
\]

On the other hand, (25) with \(j=1\) says that no source mass on which
\(\nabla_\Theta r_1\ne0\) may be omitted.  On a prime line the equality

\[
 r_1(t)=r_1(s)
\]

can hold only on a discrete set unless \(r_1\) is periodic with period
\(\log n\) (or satisfies the corresponding reflected identity on an
interval).  The latter is impossible because \(r_1=K''/K\) is analytic
and unbounded at \(+\infty\).  Hence

\[
 \int_{\partial^{-1}\mathcal L_p}
 |\nabla_\Theta r_1|^2\,d\Omega_\Theta>0.           \tag{36}
\]

Equations (25), (35) and (36) contradict one another.  \(\square\)

This argument uses the literal von Mangoldt atoms.  It is not a generic
failure caused by deleting the arithmetic: every prime line is precisely
the positive source mass which radical equality says cannot be discarded.

## 8. A second capacity obstruction in the Gamma channel

The singularity mismatch already proves Theorem 3.  There is an
independent obstruction showing that smoothing the prime atoms would not
repair an endpoint-preserving first chaos.

The absolutely continuous Gamma part of (31) has density

\[
 \boxed{
 dJ_\Gamma(t,s)
 =2K(t)K(s)
 \{g(t-s)+g(t+s)\}\,dt\,ds,\qquad t>s>0.}          \tag{37}
\]

Indeed, the two same-sign preimages contribute \(g(t-s)\), and the two
opposite-sign preimages contribute \(g(t+s)\).  Comparing (37) with (15)
gives

\[
 \frac{d\rho}{dJ_\Gamma}(t,s)
 =\frac{4h(t)h(s)}{g(t-s)+g(t+s)}.                  \tag{38}
\]

Fix \(u>0\) and take \(t=R+u\), \(s=R\).  Then

\[
 g(t-s)+g(t+s)\longrightarrow g(u),
 \qquad 4h(t)h(s)\asymp e^{2R+u}.                  \tag{39}
\]

Thus the ratio in (38) tends to infinity.  Choose a small rectangle about
\((R+u,R)\) and delete the countable prime lines (32).  The deletion has
zero \(\rho\)- and \(J_\Gamma\)-Lebesgue measure and removes all prime
singular mass.  For large \(R\), pointwise comparison on the remaining
set gives

\[
 \boxed{\rho(B_R)>J(B_R).}                           \tag{40}
\]

An endpoint-preserving substochastic coupling would require
\(\rho\leq J\), contradicting (40).

At finite level, (40) is a two-cell Hall obstruction.  Compress the pair
space into \(B_R\) and its complement.  Radical separation makes every
off-diagonal entry of a Jensen-saturated transport matrix vanish, whereas
the demand in the first cell is \(\rho(B_R)\) and its available source
capacity is only \(J(B_R)\).  The missing amount is positive by (40).  If
one inserts an off-diagonal entry to repair the capacity, the exact loss is
the strictly positive conditional variance (21) for at least one radical
signature.

## 9. Consequence

The complete theta-index lift (12) is exact and retains all four source
channels with their literal coefficients.  Its marks are ancillary for
spatial gradients, and a positive first-chaos projection cannot turn it
into the polar gradient:

\[
 \text{radical saturation}
 \Longrightarrow\text{endpoint preservation}
 \Longrightarrow\text{measure-capacity contradiction}.              \tag{41}
\]

Therefore a successor to 106.38 cannot be a conditional expectation,
Palm selector, positive Markov transport or randomized positive path whose
norm is proved by Jensen.  The only surviving class is a genuinely signed
global operator in which prime-line, Gamma and polar contributions cancel
before a norm estimate is taken.  Constructing that signed complementary
operator remains the unresolved contraction problem.
