# D.259 — Pointwise prime primitivity is stronger than the two Tate equations

## Verdict

The finite-prime contraction of D.244--D.247 holds on the pointwise
prime-coefficient kernel

\[
 \sum_p\sqrt{\log p}\,z_p=0.
\]

The row-D primitive space instead imposes two global moments on the source
function.  These conditions do not force the coherent prime port to vanish
pointwise, or even on any positive-measure set.  Consequently the finite
source Hodge inequality cannot be applied fibrewise after Tate compression.

The unpaid coherent \(L^2\) port identified in D.258 is real and
infinite-dimensional.  Gamma transport and old-core shorting must control
it; declaring it primitive would be a false closure.

## 1. The two notions of primitivity

The finite prime coefficient condition is

\[
 \mathcal K_S
 =\left\{z\in\mathbb C^S:
   \ell_S(z):=\sum_{p\in S}\sqrt{\log p}\,z_p=0
  \right\}.                                        \tag{1.1}
\]

It is a codimension-one condition in each prime-index fibre.

On a support window \(I_T\), row-D primitivity is

\[
 \mathcal P_T
 =\left\{F\in L^2(I_T):
   M_-(F)=M_+(F)=0\right\},                         \tag{1.2}
\]

where

\[
 M_\pm(F)=\int_{I_T}e^{\pm t/2}F(t)\,dt.
\]

This is a codimension-two condition on the whole support function.  It is
not a pointwise condition in the Fourier variable or in prime-index space.

## 2. Infinite-dimensional mismatch

Let

\[
 \mathcal C_{S,T}F=M_{\eta_S}\mathcal FJ_TF
\]

be the coherent dual-central feature from D.258.  The multiplier
\(\eta_S\) is nonzero almost everywhere, so \(\mathcal C_{S,T}\) is
injective.  Hence

\[
 F\in\mathcal P_T\setminus\{0\}
 \quad\Longrightarrow\quad
 \mathcal C_{S,T}F\ne0.                            \tag{2.1}
\]

In particular Tate primitivity does not annihilate the coherent port.
Since \(\mathcal P_T\) is infinite-dimensional, the collection of such
nonzero coherent outputs is infinite-dimensional.

This is compatible with D.175.  The two Tate moments kill the continuous
Chebyshev synthesis \(M_N\), which lies in the two prescribed polar
channels.  They do not kill the centered coherent discrepancy

\[
 E_N(\tau)=\sum_{n\le N}{\Lambda(n)\over\sqrt n}
 e^{-i\tau\log n}
 -{N^{1/2-i\tau}-1\over1/2-i\tau}.
\]

It is this residual coherent channel, together with its endpoint Volterra
terms, that enters the cross \(q_N\) of D.175.

More generally, let \(m(\tau)\) be any nonzero almost-everywhere coherent
prime multiplier and put

\[
 z_p(\tau)=a_p(\tau)\widehat{J_TF}(\tau),qquad
 m(\tau)=\sum_p\sqrt{\log p}\,a_p(\tau).
\]

Then the pointwise condition (1.1) for this source is

\[
 m(\tau)\widehat{J_TF}(\tau)=0\quad\text{a.e.}     \tag{2.2}
\]

If \(m\ne0\) almost everywhere, (2.2) forces \(F=0\) by Fourier
injectivity.  Thus the intersection between the pointwise primitive fibre
and the realized support source can be trivial even though
\(\mathcal P_T\) is infinite-dimensional.

## 3. What D.244 actually proves after realization

D.244 proves a contraction on \(\mathcal K_S\) before the support source
is inserted.  After tensoring with a spectral Hilbert space, it proves the
fibrewise inequality on

\[
 \mathcal K_S\widehat\otimes L^2.
\]

The realized Tate-primitive image need not lie in this subspace.  Its
coherent component is exactly the infinite-rank channel of D.258.

Therefore the implication

\[
 F\in\mathcal P_T
 \quad\Longrightarrow\quad
 z(F,\tau)\in\mathcal K_S\text{ a.e.}              \tag{3.1}
\]

is false for the natural dual-central realization.

## 4. Correct decomposition of the realized source

For every realized source vector, split the prime-index feature as

\[
 z(F)=z_{\rm prim}(F)+z_{\rm coh}(F).              \tag{4.1}
\]

D.244--D.247 control \(z_{\rm prim}\) with the exact positive contact
defect.  The remaining term is the coherent \(L^2\) output
\(z_{\rm coh}\), not a scalar.  The carrying theorem must show that after
Gamma is adjoined and the old reference is shorted,

\[
 \text{capacity of }z_{\rm coh}
 \le
 \text{remaining old output defect},               \tag{4.2}
\]

with sharp constant one.  Equation (4.2) is the source-typed content still
missing from D.190.

More explicitly, D.256(2.4) shows that the realized coherent direction
carries the Lorentzian surplus

\[
 \left(1-{1\over|S|}\right)\|d(F)\|_{L^2}^2.       \tag{4.3}
\]

Pointwise prime primitivity would set (4.3) to zero.  Tate primitivity does
not.  The Gamma/support/Green part must therefore pay (4.3), together with
the centered endpoint discrepancy, rather than merely transport a neutral
scalar port.

## 5. Equality

The finite-prime equality theorem says that a pointwise primitive contact
vector has zero defect only when it is zero.  For row D, equality can also
involve the coherent channel.  Hence the global equality case cannot be
deduced from D.244 alone; it requires equality in (4.2) and subsequent
removal of the two Tate/radical modes.

## 6. Classification

* Distinction between (1.1) and (1.2): **PROVED BY TYPE**.
* Infinite-rank coherent output on \(\mathcal P_T\): **PROVED**.
* Fibrewise application of D.244 to every Tate-primitive source:
  **FALSE**.
* Primitive-contact component: **CONTROLLED BY D.244--D.247**.
* Coherent-channel capacity estimate (4.2): **OPEN AND EQUIVALENT TO THE
  REMAINING TRANSPORT GATE**.
* Row D: **OPEN**.
