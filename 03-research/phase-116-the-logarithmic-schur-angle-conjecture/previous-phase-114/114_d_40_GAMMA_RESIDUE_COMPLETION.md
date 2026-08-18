# D.40 — Gamma-residue completion of the Meyer triangle

## 1. Purpose

D.39 shows that the canonical scaling multiplier `A=mathcal FJ` fails as
an endomorphism because its Mellin multiplier has the Gamma divisor

\[
 \operatorname{div}(\gamma)
 =\sum_{n\ge0}[1+2n]-\sum_{n\ge0}[-2n].              \tag{1.1}
\]

Those points are the trivial Gamma zero--pole towers, not nontrivial zeta
zeros.  The correct categorical repair is therefore to retain their
residue objects.  This note constructs that repair and determines exactly
what it does and does not provide for row D.

## 2. Meromorphic line and residue sequences

Let `E` be the Mellin image of Meyer's `H_-`: entire functions which are
Schwartz on every vertical line.  Put

\[
 D_-:=\sum_{n\ge0}[-2n],\qquad
 D_+:=\sum_{n\ge0}[1+2n].                            \tag{2.1}
\]

For a finite subdivisor

\[
 D_-^{(N)}=\sum_{0\le n\le N}[-2n],\qquad
 D_+^{(N)}=\sum_{0\le n\le N}[1+2n],
\]

write `E(D_-^(N))` for meromorphic functions with at most simple poles on
`D_-^(N)` and the same vertical-Schwartz estimates after subtraction of
their principal parts.  Write `E(-D_+^(N))` for the closed subspace of `E`
vanishing on `D_+^(N)`.  At every finite level, residue and evaluation give
the exact sequences

\[
 0\longrightarrow E\longrightarrow E(D_-^{(N)})
 \xrightarrow{\operatorname{res}}
 \mathbb C^{N+1}\longrightarrow0,                  \tag{2.2}
\]

\[
 0\longrightarrow E(-D_+^{(N)})\longrightarrow E
 \xrightarrow{\operatorname{ev}}
 \mathbb C^{N+1}\longrightarrow0.                  \tag{2.3}
\]

Finite surjectivity follows by elementary interpolation with
vertical-Schwartz entire factors.  The finite sequences, with the evident
restriction maps, define exact **pro-sequences**.

Nothing in the topology of `E` controls horizontal growth as `n` tends to
infinity: its seminorms control one vertical line, or one compact
horizontal strip, at a time.  Consequently the inverse-limit coordinate
space is not automatically a rapidly decreasing sequence space.
Identifying the pro-object with one Frechet residue space, and proving
surjectivity onto it, requires a separate topological Mittag--Leffler
theorem.  No such identification is asserted here.

For `t>0`, scaling acts in Mellin coordinates by

\[
 (\lambda_t h)(s)=t^s h(s).                          \tag{2.4}
\]

It preserves every finite-level space and the pro-systems.  On the
residue/value coordinates it acts by the explicit characters

\[
 \operatorname{res}_{-2n}:\ t^{-2n},\qquad
 \operatorname{ev}_{1+2n}:\ t^{1+2n}.               \tag{2.5}
\]

Thus the completion is scaling equivariant and is defined entirely by the
archimedean trivial divisor.

## 3. Gamma becomes a genuine isomorphism of twisted lines

The multiplier

\[
 \gamma(s)=\pi^{1/2-s}
 \frac{\Gamma(s/2)}{\Gamma((1-s)/2)}                 \tag{3.1}
\]

has simple poles exactly on `D_-`, simple zeros exactly on `D_+`, and no
other divisor.  Stirling estimates give polynomial growth on every
vertical line away from its finitely many intersections with a compact
strip.  Define

\[
 E_\gamma:=m_\gamma(E)
\]

with the transported Frechet topology.  Multiplication by `gamma` is then
a continuous scaling-equivariant isomorphism

\[
 \boxed{
 m_\gamma:E\xrightarrow{\sim}E_\gamma.}             \tag{3.2}
\]

As a meromorphic line, `E_gamma` embeds in the sections with at most pole
divisor `D_-` and at least zero divisor `D_+`.  Equality with an
independently topologized space denoted `E(D_-)(-D_+)` is the infinite
residue/topology theorem not proved in Section 2.

Its inverse is multiplication by `gamma(1-s)`.  Equation
`gamma(s)gamma(1-s)=1` pairs the two divisor towers under

\[
 -2n\longleftrightarrow1+2n.                         \tag{3.3}
\]

On actual residue/value coordinates the induced map contains the nonzero
leading Laurent coefficient of `gamma` at each point; it is not the
identity of unnormalized coordinate sequences.  Under reflection the two
scaling characters are related by the weight-one Tate twist.

This proves that the failure in D.39 is a type defect at the transported
line and finite/pro-divisor levels: `A` is a morphism to the Gamma twist,
though not an endomorphism of the untwisted numerator.  It does not identify
that twist with an independently completed residue Frechet space.

## 4. Compatibility with the zeta functional equation

Since

\[
 \zeta(1-s)=\gamma(s)\zeta(s),                       \tag{4.1}
\]

the square

\[
\begin{array}{ccc}
 E & \xrightarrow{\ \zeta(s)\ } & E(D_{\zeta})\\
 \downarrow m_\gamma && \downarrow m_\gamma\\
 E_\gamma & \xrightarrow{\ \zeta(s)\ } &
 E_\gamma(D_{\zeta})
\end{array}                                         \tag{4.2}
\]

is the same meromorphic correspondence as multiplication by
`zeta(1-s)` in the opposite orientation.  The only extra divisor in
changing orientation is (2.1).  After adjoining the finite-level/pro
residue complexes (2.2)--(2.3), Fourier--Tate duality is therefore a
well-typed morphism of
the corresponding **meromorphic line diagram**.  Promoting this diagram to
Meyer's topological range--cokernel triangle still requires a comparison
of the stripwise Schwartz conditions; it is not implied by the divisor
calculation alone.

This completion is precisely the place where the two polar/ruling
characters and the Gamma oscillator must live.  It explains why deleting
the poles by hand in D.39 was wrong: their residue representations are
geometric boundary objects, not errors.

## 5. The nontrivial characteristic after residue cancellation

Let

\[
 \Xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).                \tag{5.1}
\]

At the algebraic-divisor level, residue completion removes the Gamma
towers and the two polar characters, leaving the entire characteristic
morphism `m_Xi`.  Its divisor cokernel has generalized evaluation
functionals at exactly the nontrivial zeros, with the same algebraic
multiplicities as the transpose spectrum of row C.  Reflection

\[
 s\longmapsto1-s                                    \tag{5.2}
\]

gives the functional-equation duality on this divisor cokernel.  No
location of a nontrivial zero was used to obtain (5.1)--(5.2).

This equality of algebraic spectral divisors is not yet a topological
isomorphism with `H_-^0`.  Meyer's relation space is defined by two
stripwise divisibility and Schwartz conditions, whereas a naive quotient
`E/Xi E` carries a different topology and different Gamma weights.  A
complete residue construction must prove the comparison rather than infer
it from equality of spectra.

The Gamma-residue completion therefore solves one typing obligation and
isolates another:

1. it extends `mathcal FJ` across its full trivial divisor;
2. it reduces topological descent to comparison of that line diagram with
   the two-strip Meyer triangle.

It does **not** yet produce a positive Weil operator.  On a generalized
eigenfunctional at `rho`, the normalized scale character is
`t^(rho-1/2)`.  A faithful positive metric invariant under all `t` can
exist only if `Re(rho)=1/2`.  Thus positivity of the descended duality is
still the Hodge statement, not a formal consequence of residue
completion.

## 6. New exact target

After D.38--D.40, the remaining construction is no longer obscured by
local Crofoot covariance or Gamma poles.  It has two ordered parts:

1. prove a topological comparison between the residue-completed
   meromorphic diagram and Meyer's two-strip range--cokernel triangle;
2. construct, from the periodic section pairing before taking the
   characteristic cokernel, a positive Hermitian metric on the resulting
   cokernel for which reflection (5.2) is the adjoint Tate duality and the
   integrated scaling trace agrees with row C.

The local trace of this metric is already forced by D.32: every `p^k` is
the Crofoot defect and the full archimedean term is the residue-completed
Gamma oscillator.  D.40 places these pieces in one correctly typed
meromorphic diagram.  What remains is its topological comparison and
positivity on the nontrivial characteristic cokernel; neither may be
obtained by selecting zero eigenspaces or assuming bounded normalized
scaling.
