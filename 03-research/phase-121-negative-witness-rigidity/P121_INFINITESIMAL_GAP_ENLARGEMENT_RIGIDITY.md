# Infinitesimal gap enlargement excludes first contact

## 1. Purpose

The phase-116 closure criterion asked a hypothetical zero mode to make the
local co-Poisson observation vanish on the whole physical annulus
`(exp(-T),exp(T))`.  That target is much larger than necessary when `T` is
the first loss of positivity.  The first causal cell contains no arithmetic
translate.  Vanishing on any nonempty initial subcollar therefore shortens
the support of the source; parity shortens the other end, and exact nesting
contradicts minimal first contact.

This note proves that reduction.  It does not claim that the first-contact
equation already supplies the subcollar vanishing.

## 2. The first-cell identity

Put

\[
 I_T=(-T,T),\qquad a=e^{-T},\qquad b=e^T,
\]

and extend `F in L^2(I_T)` by zero.  Its local physical co-Poisson
observation is

\[
 (\mathfrak S_T^{\rm loc}F)(x)
 =\sum_{n\geq1}{1\over n}x^{-1/2}F(\log(x/n)).       \tag{2.1}
\]

### Lemma 2.1 -- arithmetic-free collar

For almost every `a < x < min(2a,b)`,

\[
 \boxed{
 (\mathfrak S_T^{\rm loc}F)(x)=x^{-1/2}F(\log x).} \tag{2.2}
\]

#### Proof

The term `n=1` is the right side of (2.2).  If `n>=2` and `x<2a`, then
`x/n<a`; hence `log(x/n)<-T` and the zero extension kills that term.  The
bound `x<b` keeps the `n=1` argument in the physical window.  QED.

In logarithmic coordinates, whenever

\[
 0<\delta<\min(\log2,T),                             \tag{2.3}
\]

equation (2.2) says

\[
 ({\cal U}\mathfrak S_T^{\rm loc}F)(t)=F(t),
 \qquad -T<t<-T+\delta.                              \tag{2.4}
\]

No global zeta estimate is involved: the sum has literally one term.

## 3. Minimal-window rigidity

Assume positivity is strict on every primitive window of half-length
`T'<T_*`, while at `T_*` there is a parity state

\[
 F_*\in\mathcal P_{T_*},\qquad
 P_{T_*}\mathcal A_\infty F_*=0.                    \tag{3.1}
\]

### Theorem 3.1 -- infinitesimal gap-enlargement rigidity

Let `RF_*=epsilon F_*`.  If for some `delta` satisfying (2.3), with
`T=T_*`,

\[
 \mathfrak S_{T_*}^{\rm loc}F_*=0
 \quad\hbox{a.e. on}\quad
 (e^{-T_*},e^{-T_*+\delta}),                        \tag{3.2}
\]

then `F_*=0`.

#### Proof

Lemma 2.1 turns (3.2) into

\[
 F_*(t)=0\quad\hbox{a.e. for }-T_*<t<-T_*+\delta.  \tag{3.3}
\]

Parity gives the reflected vanishing on
`(T_*-delta,T_*)`.  Consequently

\[
 \operatorname{ess\,supp}F_*
 \subset[-T_*+\delta,T_*-\delta].                  \tag{3.4}
\]

The same function belongs to the smaller primitive window
`\mathcal P_{T_*-\delta}`: its two Tate moments are unchanged.  Exact
nesting of the global form also leaves its zero quadratic value unchanged.
Strict positivity below first contact forces `F_*=0`.  QED.

### Corollary 3.2 -- the missing arrow is only a boundary germ

To exclude first contact it suffices to prove, for one positive `delta`
(which may depend on the hypothetical state),

\[
 \boxed{
 P_T\mathcal A_\infty F=0
 \Longrightarrow
 \mathfrak S_T^{\rm loc}F=0
 \text{ on }(e^{-T},e^{-T+\delta}).}                \tag{3.5}
\]

The former v94 target (441) demanded vanishing on all of
`(e^{-T},e^T)`.  At first contact (3.5) is enough.  No reciprocal Sonin
threshold, global co-Poisson norm or full finite Neumann inversion is then
needed.

## 4. Exact scope

This is a sharper terminal descent, not yet the source law.  In the first
collar the observation is the state itself, so (3.5) says that a zero mode
cannot saturate the left boundary.  The support-saturation theorem of v94
says that every nonzero first-loss state must saturate both endpoints.
Therefore abstract minimality alone cannot prove (3.5); a proof must use
arithmetic information from the oriented Euler--Gamma equality case.

The target has nevertheless changed materially:

* old demand: transport the natural gap through logarithmic width `2T`;
* new demand: advance it by any positive amount below `log 2`;
* terminal mechanism: the `n=1` identity, parity and exact nesting.

Future source candidates need only control this boundary germ.  A candidate
whose output starts after the first prime delay, or controls only a global
norm, cannot supply it.

## 5. Corpus audit

The ingredients existed separately: v94 (436)--(439) gave the causal
observation, v94 Theorem (273) gave support saturation, and phase 121 gave
the first-contact reduction.  A semantic search through phases 1--120 found
no previous statement that an arbitrary positive enlargement of the
natural gap suffices, nor the reduction (3.2)--(3.4).  This does not prove
row (d); it replaces the full-annulus gate by its minimal boundary-germ
version.
