# P121 -- active Euler-ideal overdensity

## Status

This note proves a strictly finite terminal rigidity lemma.  No inactive
prime is needed.  If the compact transform of a first-contact candidate
preserves the local Euler ideals for the primes which are already active in
its window, the union of the corresponding local divisor lattices has density
larger than the exponential type of the transform.  The candidate is
therefore zero.

**Logical warning.**  The equality-state lift from the compressed
first-contact equation to active local-ideal preservation is not an
intermediate gate.  Combined with Theorem 2.1 and the proved first-contact
reduction, it has the full force of the global square.  This note must not be
used to insert another milestone before that square.

## 1. Local ideals and their tangent derivation

Let `F` be supported in `[-T,T]` and put

\[
 G_F(w)=\int_{-T}^T e^{t/2}F(t)e^{-iwt}\,dt .       \tag{1.1}
\]

Then `G_F` is a Cartwright entire function of exponential type at most `T`.
For a prime `p`, write

\[
 e_p(w)=1-e^{-iw\log p},\qquad I_p=(e_p)\subset\mathcal O(\mathbb C),
 \tag{1.2}
\]

and define the witness-dependent derivation

\[
 \delta_F=G_F(w){d\over dw}.                        \tag{1.3}
\]

### Lemma 1.1 -- local ideal dictionary

The following are equivalent:

\[
 \delta_F(I_p)\subset I_p,
 \qquad
 G_F\left({2\pi k\over\log p}\right)=0
 \quad(k\in\mathbb Z).                              \tag{1.4}
\]

#### Proof

The ideal is principal, so it is enough that `delta_F(e_p)` be divisible by
`e_p`.  Every zero `2 pi k/log p` of `e_p` is simple and

\[
 \delta_F(e_p)(w)=i(\log p)e^{-iw\log p}G_F(w).
\]

Divisibility is therefore equivalent to the displayed vanishing.  QED.

### Lemma 1.2 -- compact coboundary dictionary

Put `g(t)=e^(t/2)F(t)` and let `U_a h(t)=h(t-a)`.  For `a=log p`, the
conditions of Lemma 1.1 are also equivalent to the existence of a compactly
supported function `h_p` such that

\[
                    g=(I-U_a)h_p.                  \tag{1.5}
\]

#### Proof

Fourier transformation turns `I-U_a` into multiplication by `e_p`, so
(1.5) implies (1.4).  There is also a direct support proof of the converse.
Define the locally finite causal sum

\[
 h_p(t)=\sum_{j\ge0}g(t-ja).                        \tag{1.6}
\]

It satisfies `(I-U_a)h_p=g`.  It vanishes sufficiently far to the left by
compact support of `g`.  Write `t=r+ka`, with `0<=r<a`.  For sufficiently
large `k`, (1.6) stabilizes to

\[
 \sum_{\ell\in\mathbb Z}g(r+\ell a),               \tag{1.7}
\]

the periodic seam.  Poisson/Fourier series and (1.4) say that every Fourier
coefficient of (1.7) is zero.  Hence (1.7) is zero, so `h_p` also vanishes
sufficiently far to the right and is compactly supported.  QED.

### Proposition 1.3 -- one active-product tangency

Let `S` be a finite set of primes and put

\[
 E_S(w)=\prod_{p\in S}e_p(w).                       \tag{1.8}
\]

If the positive Tate condition `G_F(0)=0` holds, then

\[
 \delta_F(E_S)\in(E_S)                              \tag{1.9}
\]

is equivalent to `delta_F(I_p) subset I_p` for every `p in S`.

#### Proof

Every nonzero zero of `E_S` belongs to exactly one factor and is simple,
because the nonzero lattices of distinct primes are disjoint.  At such a
zero `lambda`,

\[
 \delta_F(E_S)(\lambda)=G_F(\lambda)E_S'(\lambda),
 \qquad E_S'(\lambda)\ne0.
\]

Thus (1.9) is equivalent to the local vanishing in Lemma 1.1 away from the
origin.  At the origin `E_S` has order `|S|` and `E_S'` has order
`|S|-1`; the Tate zero of `G_F` supplies the remaining order.  Hence no
extra condition is present at zero.  QED.

Equivalently, AEIF can be formulated without a post-trace separation of
prime labels: the witness vector field is tangent to the divisor of the one
finite active Euler product.

## 2. The active-prime overdensity theorem

Let

\[
 \mathcal P_T=\{p:\ p<e^{2T}\},\qquad
 \vartheta(e^{2T})=\sum_{p<e^{2T}}\log p .          \tag{2.1}
\]

### Theorem 2.1

Assume `T>log 2`.  If

\[
 \delta_F(I_p)\subset I_p\qquad(p\in\mathcal P_T), \tag{2.2}
\]

then `F=0`.

More generally, it is enough that (2.2) hold on a subset `S` of active
primes satisfying

\[
 \sum_{p\in S}\log p>2T.                            \tag{2.3}
\]

#### Proof

For different primes the nonzero lattices

\[
 {2\pi\over\log p}\mathbb Z
\]

are disjoint.  Indeed, an equality
`k/log p=l/log q`, with nonzero integers `k,l`, would give `p^l=q^k`, hence
`p=q` by unique factorization.

By Lemma 1.1, the number `N_G(R)` of zeros of `G_F` in `|w|<=R`, counted
with multiplicity, therefore satisfies

\[
 \begin{aligned}
 N_G(R)
 &\ge \sum_{p\in S}2\left\lfloor{R\log p\over2\pi}\right\rfloor\\
 &= {R\over\pi}\sum_{p\in S}\log p+O_S(1).         \tag{2.4}
 \end{aligned}
\]

If `G_F` is nonzero, the Cartwright zero-density bound for a Fourier--Laplace
transform supported in `[-T,T]` gives

\[
 \limsup_{R\to\infty}{N_G(R)\over R}\le {2T\over\pi}. \tag{2.5}
\]

Equations (2.3)--(2.5) are incompatible.  Thus `G_F` is identically zero,
and Fourier--Laplace injectivity gives `F=0`.

It remains to verify (2.3) for all active primes.  Put `x=e^{2T}>4`.
For `4<x<=5`,

\[
 \prod_{p<x}p=6>x.
\]

For `x>5`, let `q` be the largest prime below `x` and `r` the next prime.
Bertrand's postulate gives `r<2q`, while

\[
 \prod_{p<x}p\ge 2\cdot3\cdot q=6q>r>x
\]

when `x<r`; at a prime endpoint use the preceding prime in the same
argument.  Consequently

\[
 \vartheta(x)=\log\prod_{p<x}p>\log x=2T.           \tag{2.6}
\]

Taking `S=mathcal P_T` proves the theorem.  QED.

## 3. Consequence for first contact

The certified initial interval gives `T_*>log 2` for any hypothetical first
contact.  Hence the following equality-state statement would exclude first
contact and prove the global square:

\[
 \boxed{
 P_{T_*}\mathscr A_{T_*}F=0
 \quad\Longrightarrow\quad
 \delta_F(I_p)\subset I_p
 \quad(p<e^{2T_*}).}
 \tag{AEIF}
\]

Unlike the cofinal first-harmonic target, AEIF asks only about primes which
occur in the localized operator.  Unlike global flat descent, it is asserted
only on a first-contact radical.  Theorem 2.1 proves that AEIF is sufficient.
Since first-contact reduction and nesting are already proved, AEIF has the
full force of the global square; naming it does not reduce the open problem.
By Lemma 1.2 it can equivalently be written as simultaneous compact Euler
coboundary:

\[
 e^{t/2}F(t)=(I-U_{\log p})h_p(t),
 \qquad \operatorname{supp}h_p\Subset\mathbb R,
 \qquad p<e^{2T_*}.                                \tag{3.1}
\]

This identifies the missing datum with the periodic seam, rather than with
an abstract ideal-theoretic condition.

By Proposition 1.3 the same target is the single multiplicative law

\[
 \delta_F(E_{\mathcal P_{T_*}})
 \in(E_{\mathcal P_{T_*}}).                         \tag{3.2}
\]

The logarithmic quotient
`delta_F(E_mathcal P)/E_mathcal P=G_F E_mathcal P'/E_mathcal P`
is exactly the full active Euler logarithmic response.  Therefore (3.2)
says that this response has removable local-Euler poles.  The compressed
first-contact equation contains the corresponding truncated logarithmic
response only on `(-T,T)`.  Promoting that local equality to the global
removability assertion (3.2) is precisely the exterior-history/annular
transport problem; formal Leibniz manipulation does not perform the
promotion.

It does not prove AEIF.  A proof must be performed in the labelled row-(b)
source before the row-(c) scalar trace.  Deriving (AEIF) from a positive norm,
a contraction, or the assertion that the full Euler ideal is stable under the
degree derivation would respectively repeat the phase-120 positive-lift
theorem or the phase-91 derivation defect.

## 4. Corpus audit

`P121_ALL_PRIME_SEAM_DIVERGENCE_THEOREM.md` proves that one harmonic on
cofinally many primes is faithful by accumulation at the Tate character.
The present theorem is different: it uses all harmonics of finitely many
active primes and Cartwright overdensity.  No phase-1--120 statement of this
active density budget was found.

Phase 91 proves that global Euler-ideal stability on arbitrary physical
vectors leaves the defect `(I-Z^{-1})delta v`; AEIF does not remove that
defect formally.  It specifies the strictly weaker equality-locus assertion
which a new source law would have to prove.
