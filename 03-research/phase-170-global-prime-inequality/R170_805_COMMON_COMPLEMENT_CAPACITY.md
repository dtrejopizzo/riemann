# R170_805 — A salvageable result from Three Gates

Origin: theorem 6.52 and theorem 6.53 of
[2609.20367v1](https://arxiv.org/abs/2609.20367v1). Here the proof is
reconstructed directly, without using its RH induction or its
certificates. The application to the Paper 47 arithmetic operator is
kept separate.

## Form and statement

On (0,1), we define the nonnegative form

\[
 r[u]=\frac14\iint\left(\frac1{|x-y|}-1\right)|u(x)-u(y)|^2dxdy
 +\int\left[-\frac12\log(x(1-x))-\log2\right]|u(x)|^2dx.
\]

Let Iν=(aν,aν+ε) be disjoint intervals contained in (0,1), all of
length ε. Write fν=u|Iν and fν,0=fν−average(fν). For D≥1,

\[
 d(D)=\log(1+1/D)-1/(D+1)>0,\qquad
 \Delta_\nu=\frac12\sum_{\mu\ne\nu}d(|a_\mu-a_\nu|/\varepsilon).
\]

Then, for every common extension u of the data prescribed on the Iν,

\[
 r[u]\ge\sum_\nu[\log(1/(2\varepsilon))-\Delta_\nu]\|f_{\nu,0}\|^2,
 \qquad\Delta_\nu\le1-\gamma_E.
\]

## Reconstructed proof

Set Vν=||fν,0||². On Iν², replacing the kernel by 1/ε−1 gives a
contribution of at least (1−ε)Vν/2. Against an exterior point y,

    ∫Iν |fν(x)−u(y)|² dx = Vν+ε|average(fν)−u(y)|² ≥ Vν.

The lower bounds of the kernel for y<aν and y>aν+ε are, respectively,
1/(aν+ε−y)−1 and 1/(y−aν)−1. Integrating over the whole complement of
a single interval, the exterior load is at least

    [log((aν+ε)(1−aν)/ε²)−(1−ε)] Vν/2.

The potential is ≥cν on Iν, with
cν=−log((aν+ε)(1−aν))/2−log2. If cν≥0 we use ||fν||²≥Vν; if cν<0 we use
the nonnegativity of the potential. The sum of the three bounds is
log(1/(2ε))Vν.

With several intervals, the coupling Iν×Iμ cannot be counted twice as
if both sides had a free complement. For a pair at distance Dε, its
actual energy is at least

    [1/(D+1)−ε](Vν+Vμ)/2,

while the two free-complement loads would have given

    [log(1+1/D)−ε](Vν+Vμ)/2.

The exact difference between these bounds is d(D)(Vν+Vμ)/2. Subtracting
it once per pair proves the statement with Δν. Only nonnegative terms
from differences of averages and of the complement were discarded.

By separation, Dνμ≥|ν−μ|; d decreases because
d'(D)=−1/[D(D+1)²]. Also

    Σ_{j=1}^N d(j)=1+log(N+1)−H_{N+1} → 1−γ_E.

There is at most one contribution per index distance on each side,
which gives Δν≤1−γ_E. No numerical certificate is needed.

## Simultaneous budget, without spending the complement twice

Let β=log2+1/2 and

    l₀[u]=β||u||²−(1/2)|∫u|²,       b=l₀+r.

If S is the union of M intervals and ℓ=Mε, the minimum of l₀ over the
single free complement, with u|S=f fixed, is exactly

    β||f||² − β/(2log2+ℓ) |∫S f|².

Proof: on S^c only its average can reduce the energy; completing the
square of that single average gives the formula. The zero-average part
of the complement only adds positive energy.

In the basis of normalized indicators of the intervals, the mean block
is

    D₀ = β I_M − [βε/(2log2+Mε)] 11*.

Since the bound on r depends exclusively on the data fixed on S, it is
preserved when taking the same infimum over S^c. We obtain

    short_S(b) ≥ D₀ on the means,
                 β+log(1/(2ε))−Δν on each zero-average sector.

Both budgets come out of l₀+r **before** minimizing. Coupled sources
are not minimized as if they had independent complements.

## Usefulness and pending condition

It is a valid tool for multiple sources with a common complement. It
can replace a step that would lose the interaction between means and
fluctuations. To use it toward D one must prove a congruence or a form
bound from the real archimedean block to b, preserving scale
coefficients, prime couplings, and the polar term. This document does
not prove that identification nor the global induction of Three Gates.

## Independent diagnostics

`python3 verify_common_complement.py` assembles the form b on
normalized cell indicators, integrating the kernel and the potential
analytically, and eliminates a single complementary block. It compares
that matrix Schur complement with the simultaneous bound above, without
minimizing each source separately. Three configurations of 24 and 48
cells, including adjacent windows and windows at the edges, gave
minimum eigenvalues of the difference 1.03988, 1.02223 and 0.89163,
respectively.

These numbers are floating-point diagnostics of finite compressions.
They do not certify the continuous form: the continuous justification
is the proof above. Nor are they margins of the Paper 47 arithmetic
operator.
