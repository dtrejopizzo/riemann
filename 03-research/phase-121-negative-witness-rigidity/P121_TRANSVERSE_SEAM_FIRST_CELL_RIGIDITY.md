# A single transverse prime seam excludes first contact

## 1. Result

Phase 120 constructed, before any global-square claim, the literal prime
cell outputs

\[
 E_{p,T}\mathfrak h=
 \left(
  \sqrt{1-p^{-1}}\,\mathbf1_{[-T,T-\log p]}B_p\mathfrak h,
  \mathbf1_{[T-\log p,T]}B_p\mathfrak h
 \right),                                          \tag{1.1}
\]

where

\[
 \mathfrak h_F(t,\ell)=e^{-\ell/2}F(t-\ell),
 \qquad
 B_p\mathfrak h_F(t)=\sum_{j\geq0}p^{-j/2}
 F(t-j\log p).                                     \tag{1.2}
\]

The pairwise transverse channel is `E_(p,T)-E_(q,T)`.  This note proves
that vanishing of **one** such channel on a first-contact state already
excludes that state.  The proof uses only the unequal Frobenius
normalizations in the first causal cell.

## 2. First-cell separation

### Lemma 2.1

Let `p != q` be active primes (`log p,log q<2T`) and choose

\[
 0<\delta<\min\{T,\log2,2T-\log p,2T-\log q\}.     \tag{2.1}
\]

Then, for almost every `-T<t<-T+delta`,

\[
 E_{p,T}\mathfrak h_F(t)
   =\bigl(\sqrt{1-p^{-1}}F(t),0\bigr),             \tag{2.2}
\]

and similarly with `q`.

#### Proof

For `j>=1`,

\[
 t-j\log p<-T+\delta-\log2<-T,
\]

so every delayed term in (1.2) vanishes and `B_p h_F(t)=F(t)`.  The last
two inequalities in (2.1) put the collar inside the first component of
(1.1) and outside its terminal component.  QED.

### Theorem 2.2 -- one-seam radical rigidity

Assume `T_*` is a first-contact parameter and `F_*` is a parity
first-contact state.  If two distinct active primes satisfy

\[
 (E_{p,T_*}-E_{q,T_*})\mathfrak h_{F_*}=0,          \tag{2.3}
\]

then `F_*=0`.

#### Proof

Since `p!=q`,

\[
 \sqrt{1-p^{-1}}\ne\sqrt{1-q^{-1}}.                \tag{2.4}
\]

Equations (2.2)--(2.4) imply `F_*=0` on the initial collar of any width
satisfying (2.1).  The infinitesimal gap-enlargement theorem then uses
parity and exact nesting to force `F_*=0` globally.  QED.

### Corollary 2.3 -- transverse variance is strictly detecting

For the phase-120 seam operator

\[
 \theta_T\|\mathcal K_T^{\rm seam}\mathfrak h\|^2
 ={1\over2\theta_T}\sum_{p,q}a_pa_q
 \|(E_{p,T}-E_{q,T})\mathfrak h\|^2,               \tag{2.5}
\]

one has, at first contact,

\[
 \boxed{
 \mathcal K_{T_*}^{\rm seam}\mathfrak h_{F_*}=0
 \Longrightarrow F_*=0.}                          \tag{2.6}
\]

There are at least two active primes: the previously certified interval
gives `T_*>log 2`, hence `log2,log3<2T_*`.

More precisely, for every `delta` satisfying (2.1),

\[
 \|(E_{p,T_*}-E_{q,T_*})\mathfrak h_{F_*}\|^2
 \geq
 \left|\sqrt{1-p^{-1}}-\sqrt{1-q^{-1}}\right|^2
 \|F_*\|^2_{L^2(-T_*,-T_*+\delta)}.                \tag{2.7}
\]

The support-saturation theorem makes the last norm strictly positive for
every admissible `delta` when `F_*` is nonzero.  Thus every pair of distinct
active primes has a strictly nonzero seam on a hypothetical nonzero
first-contact state; this is not merely injectivity of the full ANOVA bank.

## 3. Why this is stronger than the former seam discussion

Phase 120 proved that the seam is a positive variance and identified it as
the remaining transverse leakage.  It did not use the unequal factors
`sqrt(1-p^(-1))` on the arithmetic-free first cell to prove that its kernel
contains no first-contact state.

Thus the global-square problem has a second, very small equality-state
target:

\[
 P_T\mathcal A_\infty F=0
 \quad\Longrightarrow\quad
 \mathcal K_T^{\rm seam}\mathfrak h_F=0.           \tag{3.1}
\]

One does **not** need the full operator identity (phase-120 (5.3)) to use
(3.1).  A source-level equality law which kills only the transverse seam
on the radical already closes first contact.

This is a sufficient law, not a consequence of the proposed phase-120
square.  In (5.3) the seam occurs on both sides of the rearranged signed
balance and is cancelled before the final remainder `Q_T` is squared.
Therefore even the completed global square would force `Q_TG=0` at
equality, not seam vanishing.  Any proof of (3.1) must be genuinely
additional and cannot cite (5.3).

## 4. Noncircularity boundary

Equation (2.6) is proved independently of the Weil sign.  Equation (3.1)
is not yet proved.  It must not be obtained by asserting that the entire
signed Green balance is a sum of squares, because that is the retired
global-square architecture.

The admissible remaining construction is narrower: derive seam vanishing
as an equality condition of the unsupertraced Euler source.  It is enough
to derive it for one pair of distinct active primes.  The first-cell
calculation then supplies the contradiction with no estimate and no
cofinal limiting argument.

## 5. Corpus audit

A semantic search through phases 1--120 found the ingredients (the cell
outputs, ANOVA seam square and Frobenius factors) but no first-cell theorem
(2.2)--(2.6).  The result is not row (d); it is an exact kernel theorem for
the already constructed transverse channel and isolates the remaining
source identity (3.1).
