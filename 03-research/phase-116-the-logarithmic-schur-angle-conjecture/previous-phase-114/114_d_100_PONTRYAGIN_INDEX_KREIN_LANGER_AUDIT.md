# D.100 — Pontryagin index and Krein--Langer audit

## Status

A finite negative-index theorem would close row D if it showed that the
completed prime--Gamma colligation has at most the two negative directions
already accounted for by the Tate residues.  This note calculates the
indices available before using the divisor of `Xi`.

The source-defined local and ambient colligations do **not** have index at
most two.  A single prime transfer ratio is expansive on an open boundary
arc and contractive on another; its de Branges--Rovnyak kernel has
infinitely many negative squares.  The exact prime--Gamma feature target
and the preparation colligation likewise have infinite positive and
negative index.  Redheffer coupling may cancel those directions, but no
finite-index bound survives from the factors.

After global analytic continuation and the functional equation, the
completed transfer is generalized inner.  Krein--Langer theory then says
that its negative index is exactly the number of its upper-half-plane
poles, i.e. the number of off-central zero orbits beyond the displaced
line.  This is an exact audit of the divisor, not a source-side bound.  The
two Tate residue channels are prescribed polar terms and do not absorb
these additional blocks.

Thus Pontryagin theory identifies the desired theorem but does not prove
it: reducing infinite ambient index to the two Tate directions is itself
the primitive Hodge inequality.

No RH statement or zero localization is assumed.  The paper is not
modified.

## 1. Negative squares of a transfer kernel

For a scalar transfer function `S` on the upper half-plane, use the Pick
kernel

\[
 K_S(z,w)={1-S(z)\overline{S(w)}\over-i(z-\overline w)}.  \tag{1.1}
\]

The function belongs to the generalized Schur class `S_kappa` when (1.1)
has exactly `kappa` negative squares.  A conservative realization then
lives in a Pontryagin space of negative index `kappa`; `kappa=0` is the
Hilbert/Schur case.

If a continuous boundary value satisfies

\[
 |S(x)|>1                                                 \tag{1.2}
\]

on an open interval, then `K_S` has infinitely many negative squares.
Indeed, choose any number of separated boundary points in that interval
and approach them nontangentially.  After the standard normalization, the
Cauchy kernel

\[
 {1\over-i(z-\overline w)}                                \tag{1.3}
\]

is positive definite, while the diagonal coefficient
`1-|S(x)|^2` is strictly negative.  Localization makes the off-diagonal
variation of `S` arbitrarily small, giving a negative definite Gram matrix
of arbitrary size.  Equivalently, the boundary multiplication operator
has an infinite-dimensional expansive spectral subspace.

Thus finite negative index is much stronger than isolated pointwise
indefiniteness.

## 2. One prime already has infinite local index

The displaced local Euler transfer has, on a boundary circle,

\[
 R_{p,a}(e^{i\theta})
 ={1-r_+e^{i\theta}\over1-r_-e^{i\theta}},
 \qquad0<r_+<r_-<1.                                      \tag{2.1}
\]

At the two real boundary characters,

\[
 |R_{p,a}(1)|={1-r_+\over1-r_-}>1,
 \qquad
 |R_{p,a}(-1)|={1+r_+\over1+r_-}<1.                      \tag{2.2}
\]

Continuity gives an expansive open arc around `1` and a contractive open
arc around `-1`.  By Section 1,

\[
 \mathrm{ind}_-K_{R_{p,a}}=\infty.                 \tag{2.3}
\]

Therefore the prime factors are not finite-index generalized Schur
factors.  No Krein--Langer degree can be added place by place.

The Gamma factor can change the completed product, but it cannot turn
each individual prime realization into a Hilbert or finite-Pontryagin
colligation.  Any global finite index would have to arise through
infinite cancellation among factors.

## 3. Ambient feature and preparation indices

The exact source feature realization of D.32 is

\[
 B_{\rm nuc}(f,g)=\langle Wf,JWg\rangle,
 \qquad J=I_{\mathcal K_S}\oplus(-I_{\mathcal K_B}).       \tag{3.1}
\]

Both feature spaces contain an infinite-dimensional translation/Gamma
sector.  Hence the ambient Krein space has

\[
 \mathrm{ind}_+(J)=\mathrm{ind}_-(J)=\infty. \tag{3.2}
\]

The preparation colligation of D.86 makes this visible one principal angle
at a time.  On every spectral value `0<lambda<1`, its Hermitian block is

\[
 \begin{pmatrix}
 4(1-\lambda)&-2\sqrt{\lambda(1-\lambda)}\\
 -2\sqrt{\lambda(1-\lambda)}&0
 \end{pmatrix},                                          \tag{3.3}
\]

with determinant

\[
 -4\lambda(1-\lambda)<0.                                 \tag{3.4}
\]

Thus each nontrivial angle contributes one positive and one negative
direction.  The cofinal prolate/round-trip operator has infinitely many
nontrivial angles, so its ambient index is `(infinity,infinity)`.

Restricting (3.1) or (3.3) to the actual primitive image could in principle
remove all negative directions.  But proving exactly that restriction is
negative/positive as required is the contraction theorem of D.86, hence
row D.  Ambient index alone gives no codimension-two bound.

## 4. Redheffer products do not provide the missing cancellation

For finite Pontryagin colligations, a regular cascade or Redheffer product
has a negative-index bound by the sum of the factor indices; equality
requires minimality and absence of pole-zero cancellation.  Here every
prime factor already has infinite index by (2.3), so this bound is
vacuous:

\[
 \kappa_{\rm product}\le\sum_p\kappa_p=\infty.            \tag{4.1}
\]

Feedback can cancel positive and negative channels.  To prove that only
two survive one must construct an explicit maximal neutral subspace and
show that its orthogonal quotient has index two.  The local determinant
identities and the functional equation identify algebraic cancellations,
but they do not give a positive norm on that quotient.

In particular, finite rank over the nuclear Dirichlet algebra does not
bound Hilbert/Pontryagin index.  The coefficient algebra contains
infinitely many independent prime translations; evaluation in its regular
representation produces the infinite feature spaces in (3.1).

## 5. Global Krein--Langer index after analytic continuation

For

\[
 \Theta_a(z)={\Xi(1/2-a-iz)\over\Xi(1/2+a-iz)},           \tag{5.1}
\]

the functional equation gives unimodular boundary values.  On any finite
height truncation, cancel common factors and apply the Krein--Langer
factorization

\[
 \Theta_a=B_a^{-1}S_a,                                    \tag{5.2}
\]

where `S_a` is Schur and `B_a` is the Blaschke product of the poles in the
upper half-plane.  Therefore

\[
 \boxed{
 \kappa_a(T)=\deg B_a
 =\sum_{\substack{|\mathrm{Im}\,\rho|\le T\\
                   \mathrm{Re}\,\rho>1/2+a}}
   m_\rho,}                                               \tag{5.3}
\]

with the evident correction at truncation boundaries.  If the count is
infinite as `T->infinity`, the global realization is Krein rather than
Pontryagin.

Formula (5.3) is the index version of the free Real orbit block in D.95.
It uses the divisor to **calculate** the index.  It does not bound the
index from prime--Gamma source data.

## 6. The two Tate residues

The meromorphic completed factor before entire normalization has the two
prescribed polar channels at `s=0,1`.  In the explicit formula their
pullback is

\[
 \langle M(f),CM(g)\rangle,
 \qquad C=\begin{pmatrix}0&1\\1&0\end{pmatrix}.            \tag{6.1}
\]

Passing to `Xi(s)=s(s-1)\Lambda(s)` removes those poles from the
nontrivial divisor.  The nontrivial pole count (5.3) is additional to the
known Tate channels.  Equivalently, on primitive tests (6.1) vanishes but
every free nontrivial zero orbit remains as a hyperbolic block.

Thus a source theorem

\[
 \mathrm{ind}_-(\text{completed colligation})\le2  \tag{6.2}
\]

together with exact identification of the two Tate directions would imply
that (5.3) vanishes for every `a>0`.  It would prove RH.  Neither local
index addition, nuclear module rank, nor the ambient preparation space
proves (6.2); all give infinite index before the primitive quotient.

## 7. Outcome

Krein--Langer theory provides an exact dictionary:

\[
 \begin{array}{c|c}
 \text{geometric datum}&\text{negative-index datum}\\ \hline
 \text{Tate poles}&\text{two prescribed residue channels}\\
 \text{fixed nontrivial zero}&\text{positive fixed Real line}\\
 \text{free off-line zero orbit}&\text{one hyperbolic/negative block}\\
 \text{prime--Gamma ambient features}&\text{infinite index}
 \end{array}                                               \tag{7.1}
\]

The hoped-for index-two theorem is not a formal consequence of the
colligation product.  A further viable route must construct a **source-side
maximal neutral relation** pairing the infinite prime and Gamma channels,
then prove that its quotient leaves only the two Tate residues.  This is
more specific than asking for positivity directly.  The relation must be
defined by A--B--C duality or the Euler--Gamma functional equation before
using the zero divisor; choosing it as the negative spectral subspace of
`B_nuc` would be circular.

