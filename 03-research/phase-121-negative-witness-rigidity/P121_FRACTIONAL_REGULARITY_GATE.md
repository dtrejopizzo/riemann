# P121 -- fractional regularity gate for a first-loss state

## Status

This note proves a strictly weaker regularity threshold than the
translation-jet criterion of phase 116. It also identifies exactly why the
optimal scalar boundary profile of the logarithmic Laplacian is not, by
itself, the obstruction to the nuclear graph domain.

The required fractional regularity is now proved in
`P121_DYADIC_RADICAL_BOOTSTRAP.md`.  The present note originally claimed
that this would by itself exclude first loss.  The post-bootstrap audit
found that claim to be too strong: v94 still requires annular gap transport
(358)/(441) after the global co-Poisson observation has been defined.
Consequently fractional regularity closes the domain gate, but not the
global square.

## 1. A quarter derivative is enough

Let `F` be supported in a bounded interval and extended by zero. Use the
Sobolev convention

\[
 \|F\|_{H^s}^2=\int_{\mathbb R}(1+\tau^2)^s
                    |\widehat F(\tau)|^2\,d\tau .       \tag{1.1}
\]

### Theorem 1.1 -- Sobolev-to-nuclear inclusion

For every `s>1/4`,

\[
 H^s(\mathbb R)\cap\{\operatorname{supp}F\text{ compact}\}
 \subset
 \operatorname{Dom}S^{\max},                         \tag{1.2}
\]

where

\[
 \operatorname{Dom}S^{\max}
 =\{F:\zeta(1/2+i\tau)\widehat F(\tau)\in L^2(d\tau)\}.
\]

#### Proof

The classical convexity estimate gives, for every `eta>0`,

\[
 |\zeta(1/2+i\tau)|
 \ll_\eta (1+|\tau|)^{1/4+\eta}.                    \tag{1.3}
\]

Choose `eta>0` with `1/4+eta<s`. Squaring (1.3) gives

\[
 |\zeta(1/2+i\tau)|^2
 \ll_\eta (1+\tau^2)^{1/4+\eta}.
\]

The right side is bounded by a constant times `(1+tau^2)^s`.
Multiplication by `|Fhat|^2` and integration prove (1.2). QED.

### Corollary 1.2 -- corrected first-loss domain alternative

For a compact-window vector, membership in any `H^s`, `s>1/4`, implies
membership in `Dom S^max`.  This is a domain conclusion only.  Contrary to
the first version of this note, v94 does not prove that every nonzero
first-loss vector lies outside `Dom S^max`; it proves that exclusion follows
after the additional annular gap-transport identity (358)/(441).

The dyadic radical bootstrap now proves that a first-loss vector is in every
`H^s`, `s<1/2`, and hence in `Dom S^max`.  Thus the regularity escape is
closed, while the annular transport step remains.

## 2. The optimal scalar boundary profile crosses the threshold

Let, for small `x>0`,

\[
 b(x)=\frac1{\sqrt{\log(1/x)}},                     \tag{2.1}
\]

and multiply it by a compactly supported cutoff which is one near zero;
extend the result by zero to the negative half-line.

### Theorem 2.1 -- the logarithmic boundary profile is sub-half-Sobolev

The resulting compactly supported function satisfies

\[
 \boxed{b\in BV(\mathbb R)\subset H^s(\mathbb R)
        \quad(0<s<1/2).}                            \tag{2.2}
\]

#### Proof

Near zero,

\[
 b'(x)=\frac1{2x(\log(1/x))^{3/2}}.
\]

The substitution `u=log(1/x)` gives

\[
 \int_0^\delta |b'(x)|\,dx
 =\frac12\int_{\log(1/\delta)}^\infty u^{-3/2}\,du<\infty.
\]

The cutoff contributes finite variation, and the zero extension has no
jump at the origin because `b(x)->0`. Hence `b` is compactly supported and
of bounded variation. Its distributional derivative is a finite measure,
so

\[
 |\widehat b(\tau)|\le {\operatorname{Var}(b)\over |\tau|}
 \qquad(|\tau|\ge1).
\]

Therefore

\[
 \int_{|\tau|\ge1}(1+\tau^2)^s|\widehat b(\tau)|^2d\tau
 \ll\int_1^\infty \tau^{2s-2}d\tau<\infty
\]

exactly when `s<1/2`. QED.

### Corollary 2.2 -- finite conormal expansions are graph-admissible

Suppose a compact-window source has a decomposition

\[
 F=V+\sum_{j=1}^M c_j\,b_j,                         \tag{2.3}
\]

where `V in H^s` for some `s>1/4` and every `b_j` is a translate,
reflection or smooth multiple of the profile (2.1). Then `F` belongs to
the maximal nuclear domain.  This does not exclude a first-loss state; it
shows that such a state, if it has (2.3), is not escaping the graph domain.

This is the useful correction to the boundary-layer audit in v94. The
optimal profile is not `H^1`, but `H^1` is not the relevant threshold. The
profile already lies comfortably above the quarter threshold needed for
the zeta graph.

## 3. What a counterexample must look like

The scalar estimate

\[
 |F(t)|\lesssim(\log(1/d(t)))^{-1/2},
 \qquad d(t)=\operatorname{dist}(t,\partial I_T),    \tag{3.1}
\]

does not imply (2.3): a function may obey the pointwise envelope while
oscillating arbitrarily fast. Therefore Theorem 2.1 does not permit one to
quote the existing logarithmic boundary estimate as a proof.

The dyadic bootstrap later shows that this oscillatory possibility is not
needed either: every zero mode is sub-half-Sobolev.  Thus boundary roughness
is not the terminal obstruction.  The obstruction is the failure, still
possible for a regular graph vector, of equality-state annular transport.

The pure regularity target was

\[
 \boxed{
 F\in\ker H_T\quad\Longrightarrow\quad
 F\in H^s(\mathbb R)\text{ for some }s>1/4.}        \tag{3.2}
\]

It is proved in `P121_DYADIC_RADICAL_BOOTSTRAP.md`.  The conclusion is that
the co-Poisson observation exists globally.  To close the square one must
still prove that the equality equation transports its natural origin gap
through the physical annulus, i.e. (358)/(441) of v94.

## 4. Why the two-thirds theorem does not prove (3.2)

The 2026 rank--trace theorem proves that at least two thirds of the zeros,
counted with multiplicity, are simple and on the critical line. This is
enough for the Cartwright uniqueness step after the critical samples of
`Fhat` have been shown to vanish. It does not show that they vanish.

More decisively, the theorem is unchanged by finitely many, or even
`o(N(T))`, off-line orbits. A single off-line orbit already contributes a
negative residue fibre and is enough to violate global Weil positivity.
Hence no argument which uses only the asymptotic proportion `2/3` can
annihilate the negative port. A weighted local sampling domination would
be new information beyond the rank--trace theorem and is not inferred from
its count.

## 5. Relation with the Abel-slope note

The normal-slope identity in `P121_WHITE_LIGHT_NORMAL_SLOPE.md` remains
correct, but v94 already identifies the same maximal graph domain and a
strictly weaker local Clark-residue criterion. The slope formulation is
therefore a coordinate on the gap, not the preferred closing mechanism.

The fractional gate (3.2) is more concrete: it asks for a fixed positive
amount of ordinary regularity of a kernel vector. It also explains exactly
why generic logarithmic form regularity is insufficient and exactly why the
known optimal boundary profile is nevertheless not an obstruction.

### Corpus audit

A semantic search over phases 1--120 found the phase-116 statements that
logarithmic ellipticity does not give the full translation jet and that the
optimal profile is not `H^1`.  It did not find the quarter-Sobolev inclusion
(1.2), the observation (2.2), or their combination into the first-loss
criterion (3.2).  The nearest neighbours are v94 (335)--(345) and its
boundary-profile audit (418); the present point is precisely that their
`H^1` target overshoots the nuclear-domain threshold.

## 6. Status

Proved:

* `H^s`, `s>1/4`, implies nuclear graph membership;
* the optimal logarithmic boundary profile belongs to every `H^s`,
  `s<1/2`;
* a finite conormal boundary expansion is nuclear-graph admissible;
* the two-thirds density theorem cannot by itself remove even one negative
  residue orbit.

Closed after the dyadic bootstrap:

* the coupled Gamma--Euler regularity statement (3.2);
* membership of every hypothetical first-loss vector in the maximal
  co-Poisson graph domain.

Open:

* equality-state annular gap transport (358)/(441) of v94.

The global square remains open at that transport statement, not at
fractional regularity.
