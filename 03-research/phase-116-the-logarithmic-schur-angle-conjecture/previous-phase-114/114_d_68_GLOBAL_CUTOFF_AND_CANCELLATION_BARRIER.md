# D.68 — Global cutoff growth and the square-root cancellation barrier

## Status

D.55 couples every prime power to the complete Gamma multiplier and proves
that, on each fixed support window, all sufficiently high Fourier modes are
negative.  This note audits whether that argument can give a uniform global
finite-band core.

Two exact conclusions are proved.

1. The coefficient-blind cutoff obtained from `|cos|<=1` is necessarily on
   the scale
   \[
   \log R_T=4e^T+o(e^T).
   \]
   Hence that proof class does not produce a uniform, polynomial, or merely
   exponential-in-`T` dangerous-frequency core.
2. The natural square-root-size improvement of the prime--continuum
   discrepancy at frequency zero is equivalent to RH.  It cannot be
   imported as an unconditional prime-number-theorem estimate in order to
   prove row D.

These are global-in-`T` no-go theorems for two candidate estimates.  They do
not disprove a cancellation argument which first imposes the two Tate jets,
nor do they prove the parity--Feshbach index law.  No paper file is changed.

## 1. Exact mass of the prime-power tower

Put

\[
 X=e^{2T},\qquad
 A(X)=\sum_{n\le X}{\Lambda(n)\over\sqrt n},
 \qquad A_T=A(e^{2T}).                                    \tag{1.1}
\]

Stieltjes partial summation gives

\[
 A(X)={\psi(X)\over\sqrt X}
      +{1\over2}\int_1^X{\psi(t)\over t^{3/2}}dt.          \tag{1.2}
\]

The unconditional prime number theorem `psi(X)~X` therefore implies

\[
 \boxed{A(X)=2\sqrt X+o(\sqrt X),\qquad
        A_T=2e^T+o(e^T).}                                  \tag{1.3}
\]

The harmless additive constant hidden in (1.3) depends on whether the
continuum integral is started at `1` or `1^-`; it has no effect on any
asymptotic below.

## 2. The optimal cutoff within the coefficient-blind envelope

The exact fixed-window multiplier is

\[
 b_T(\tau)=-\mathfrak a(\tau)
 +2\sum_{n\le e^{2T}}{\Lambda(n)\over\sqrt n}
                         \cos(\tau\log n),                 \tag{2.1}
\]

where

\[
 \mathfrak a(\tau)=
 \mathrm{Re}\,\psi\left({1\over4}+{i\tau\over2}\right)
 -\log\pi.                                                 \tag{2.2}
\]

For positive `tau`, `mathfrak a` is strictly increasing and

\[
 \mathfrak a(\tau)=\log{\tau\over2\pi}+O(\tau^{-2}).       \tag{2.3}
\]

If no cancellation among the prime phases is used, the sharp envelope is

\[
 b_T(\tau)\le -\mathfrak a(\tau)+2A_T.                    \tag{2.4}
\]

For a fixed margin `eta>0`, the smallest positive cutoff certified by this
envelope is the unique solution

\[
 \mathfrak a(R_T^{\rm abs})=2A_T+\eta.                     \tag{2.5}
\]

Equations (1.3), (2.3), and (2.5) prove

\[
 \boxed{
 \log R_T^{\rm abs}=2A_T+\eta+\log(2\pi)+o(1)
                    =4e^T+o(e^T).}                         \tag{2.6}
\]

In particular

\[
 R_T^{\rm abs}=\exp\bigl(4e^T+o(e^T)\bigr).               \tag{2.7}
\]

This is the sharp asymptotic **inside the information class (2.4)**.  It is
not asserted to be the first frequency beyond which the actual arithmetic
multiplier is negative; the actual phases can cancel.  It proves that a
global proof which discards those phases cannot see such cancellation.

The prolate trace estimate in D.55 then returns the certified core-size
bound

\[
 d_T^{\rm abs}
 \le {4T R_T^{\rm abs}(m_0+2A_T+\eta)\over\pi\eta},        \tag{2.8}
\]

and hence

\[
\log d_T^{\rm abs}\le4e^T+o(e^T).                        \tag{2.9}
\]

The right side of (2.8) is an upper bound, so (2.9) is not a lower bound on
the true positive index.  Nevertheless the prolate core selected by this
specific construction is not uniformly finite-dimensional.  Indeed, fix
`N` orthonormal smooth functions on `[-1,1]` and transport them unitarily to
`[-T,T]`.  On their span the Fourier mass outside `[-R,R]` is, after
rescaling, the mass outside `[-TR,TR]`.  It tends uniformly to zero on this
fixed finite-dimensional span as `TR` tends to infinity.  The min--max
principle therefore gives at least `N` eigenvalues of `C_(T,R)` larger than
`1/2` for all sufficiently large `TR`.  Since

\[
 T R_T^{\rm abs}\longrightarrow\infty,
 \qquad
 \beta_T={\eta\over2(m_0+2A_T+\eta)}< {1\over2},           \tag{2.10}
\]

the D.55 subspace spanned by concentration eigenvalues greater than
`beta_T` has dimension at least `N` for all sufficiently large `T`.  As `N`
was arbitrary, its dimension tends to infinity.

This still gives no lower bound on the true positive index: most vectors in
the prolate core may be removed by the finite Schur complement.  The
rigorous no-go is about the coefficient-blind *reduction*, not about row D:

> **Theorem 2.1 (absolute-phase cutoff no-go).**  Any D.55 high-frequency
> proof which uses the prime powers only through their total mass `A_T` and
> `|cos(tau log n)|<=1` requires the cutoff (2.5), whose logarithm has the
> double-exponential scale (2.6).  Such a proof does not furnish a
> `T`-uniform finite core—the corresponding prolate core has dimension
> tending to infinity—or a cutoff bounded by `exp(O(T^k))` for any fixed
> `k`.

The last assertion follows because `e^T/T^k` tends to infinity.

## 3. The centered arithmetic remainder

The most direct repair of (2.4) is to subtract the continuum main term
before estimating.  At frequency zero define

\[
 \mathcal R(X)=A(X)-2(\sqrt X-1).                          \tag{3.1}
\]

This is exactly the mass of the Stieltjes discrepancy

\[
 x^{-1/2}d(\psi(x)-x)                                     \tag{3.2}
\]

on `[1,X]`.  The following theorem identifies the forbidden cancellation
threshold.

> **Theorem 3.1 (square-root cancellation barrier).**  The family of
> estimates
> \[
> \mathcal R(X)=O_\varepsilon(X^\varepsilon)
> \quad\hbox{for every }\varepsilon>0                      \tag{3.3}
> \]
> is equivalent to the Riemann hypothesis.

### Proof: (3.3) implies RH

Since `dA(t)=t^(-1/2)dpsi(t)`, Stieltjes inversion gives

\[
 \psi(X)=\sqrt X A(X)-{1\over2}\int_1^X{A(t)\over\sqrt t}dt.
                                                                    \tag{3.4}
\]

Insert

\[
 A(t)=2(\sqrt t-1)+\mathcal R(t).                          \tag{3.5}
\]

The main terms in (3.4) equal `X+O(1)`.  Under (3.3), the two error terms
are bounded by

\[
 \sqrt X\,|\mathcal R(X)|
 +{1\over2}\int_1^X{|\mathcal R(t)|\over\sqrt t}dt
 =O_\varepsilon(X^{1/2+\varepsilon}).                     \tag{3.6}
\]

Thus

\[
 \psi(X)=X+O_\varepsilon(X^{1/2+\varepsilon})              \tag{3.7}
\]

for every positive `epsilon`.  Mellin integration of `psi(X)-X` makes
`-zeta'(s)/zeta(s)-1/(s-1)` holomorphic in `Re(s)>1/2`.  Therefore zeta has
no nontrivial zero in that half-plane.  The functional equation reflects
nontrivial zeros across `Re(s)=1/2`, so every nontrivial zero lies on the
critical line.

### Proof: RH implies (3.3)

Under RH, the classical von Koch estimate is

\[
 \psi(X)=X+O(\sqrt X\log^2X).                              \tag{3.8}
\]

Substitution in (1.2) gives

\[
 \mathcal R(X)=O(\log^3X),                                 \tag{3.9}
\]

which implies (3.3) for every positive `epsilon`.  This proves the
equivalence.

## 4. Why the barrier applies to a pointwise finite-band proof

At `tau=0`, a pointwise estimate of the continuum-subtracted Dirichlet
polynomial necessarily contains `mathcal R(e^(2T))`.  Therefore a proposed
uniform estimate of the form

\[
 \left|\sum_{n\le X}{\Lambda(n)\over\sqrt n}n^{i\tau}
       -\int_1^Xx^{-1/2+i\tau}dx\right|
 \le C_\varepsilon X^\varepsilon                         \tag{4.1}
\]

for all real `tau` includes (3.3) as the special case `tau=0`.  Invoking
(4.1) to establish the D.56 finite-band index would therefore assume an
RH-equivalent estimate.

This does **not** show that every useful phase estimate is circular.  A
valid estimate may exploit all three structures absent from (4.1):

1. the two Tate moment constraints;
2. the negative Gamma multiplier before taking absolute values;
3. the operator compression to a finite support window.

It does show that plain pointwise cancellation of the centered prime
Dirichlet polynomial at square-root scale is not an available
unconditional shortcut.

## 5. Mean-square cancellation does not by itself give finite index

For completeness, let

\[
 D_X(\tau)=\sum_{n\le X}{\Lambda(n)\over\sqrt n}n^{i\tau}. \tag{5.1}
\]

The mean-value theorem for Dirichlet polynomials gives, for `R>0`,

\[
 \int_0^R|D_X(\tau)|^2d\tau
 \le (R+C X)\sum_{n\le X}{\Lambda(n)^2\over n},            \tag{5.2}
\]

with an absolute constant `C`; and

\[
 \sum_{n\le X}{\Lambda(n)^2\over n}=O(\log^2X).            \tag{5.3}
\]

Chebyshev's inequality can therefore bound the measure of frequencies
where the prime polynomial exceeds the Gamma logarithm.  But an exceptional
set of small *relative* measure at height `R` can still have measure of
order `R`, and its time--band concentration trace is proportional to
`T` times that absolute measure.  Thus (5.2), without a geometric
localization or higher structured cancellation, does not bound the number
of dangerous prolate directions uniformly in `T`.

This is not a claim that no strengthened mean-value theorem can help.  It
records the precise missing passage: a density estimate must be converted
into a trace or singular-value estimate after the two-jet compression.

## 6. Circularity audit and surviving theorem

Sections 1--2 use only the unconditional prime number theorem, monotonicity
and asymptotics of the digamma function, and the exact D.55 multiplier.
Section 3 proves rather than assumes the connection between the stronger
remainder and RH.  No zero location is used in the no-go theorem.

The global alternatives are now sharply separated:

* coefficient-blind prime--Gamma coupling gives a rigorous but
  double-exponential cutoff;
* square-root pointwise cancellation would give a small cutoff but is
  RH-equivalent already at frequency zero;
* ordinary mean-square cancellation does not control the time--band rank;
* a noncircular closure must use the *compressed*, two-jet prime--Gamma
  operator and prove its parity--Feshbach inertia directly.

No index-one law is proved here.  Accordingly row D remains open after this
audit.
