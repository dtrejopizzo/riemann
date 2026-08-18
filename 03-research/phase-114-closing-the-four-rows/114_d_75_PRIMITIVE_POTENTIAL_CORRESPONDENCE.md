# D.75 — Primitive cancellation as a compact-potential correspondence

## Status

D.74 shows that basiswise smoothing cannot turn the periodic Dirac frame
into a supported multiplicative `L^2` frame.  This note tests the remaining
possibility: impose the two primitive cancellations **before** passing from
distributions to Hilbert vectors.

The result is positive and explicit.  The two-moment kernel is a convolution
`*`-ideal.  Every compactly supported primitive distribution has a canonical
compactly supported potential for `D^2-1/4`; for a finite Dirac combination
the two moment equations cancel its two exponential tails exactly.  The
construction is injective, translation covariant, compatible with support
enlargement, and an exact bimodule map.  The ideal also has a bounded smooth
compactly supported approximate identity, necessarily with expanding
support.

It cannot be made into a nonzero translation-covariant algebra
homomorphism into compactly supported `L^2`: multiplicativity forces an
idempotent Fourier multiplier.  Accordingly the correct object is a
module/correspondence, not a new convolution algebra.

The compact potential supplies the support half of D.73, but its ordinary
Fourier compression does not equal `B_nuc`: it has an absolutely continuous
rational multiplier and contains neither the prime-power atoms nor the full
Gamma phase.  Thus D.75 constructs the rigged primitive-cancellation
functor, but the adelic trace-exact comparison remains a further theorem.
No RH or zeta zero is used.  The paper is not modified.

## 1. The primitive convolution ideal

Let `M_c(R)` be the finite compactly supported complex measures on the
logarithmic line, with convolution and involution

\[
 \mu^*(\varphi)=\overline{\mu(\overline{\varphi(-\cdot)})}.    \tag{1.1}
\]

Put

\[
 \chi_\pm(\mu)=\langle\mu,e^{\pm t/2}\rangle.                 \tag{1.2}
\]

Since exponentials are characters of the additive group,

\[
 \chi_\pm(\mu*\nu)=\chi_\pm(\mu)\chi_\pm(\nu).               \tag{1.3}
\]

Define

\[
 \mathfrak I_{\rm prim}^{\rm meas}
 =\ker\chi_-\cap\ker\chi_+.                                 \tag{1.4}
\]

Equation (1.3) proves immediately that this is a two-sided convolution
ideal in `M_c(R)`.  Its smooth part is its intersection with
`C_c^infinity(R)`.  The involution exchanges the two characters up to
conjugation,

\[
 \chi_\pm(\mu^*)=\overline{\chi_\mp(\mu)},                   \tag{1.5}
\]

so it is a `*`-ideal.

Under the central logarithmic transform of D.32,

\[
 \chi_-(\mu)=M_-(\mu),\qquad \chi_+(\mu)=M_+(\mu).            \tag{1.6}
\]

Thus (1.4) is not a new notion of primitivity: it is exactly the A--B--C
two-jet kernel.

> **Proposition 1.1.**  Primitive tests and primitive finite periodic-frame
> combinations in the measure algebra are closed under convolution and
> Tate involution.  Their
> product actually lies in the square of each character kernel, since its
> Fourier--Laplace transform has at least the sum of the vanishing orders.

## 2. The compact-potential theorem

Put

\[
 L=D^2-\frac14,
 \qquad G(t)=-e^{-|t|/2}.                                    \tag{2.1}
\]

Distributionally,

\[
 LG=\delta_0.                                                \tag{2.2}
\]

For `mu in I_prim^meas`, define

\[
 \boxed{\mathcal W\mu:=G*\mu.}                              \tag{2.3}
\]

Then

\[
 L\mathcal W\mu=\mu.                                       \tag{2.4}
\]

Let `supp(mu) subset [a,b]`.  If `t>b`, then

\[
 (G*\mu)(t)
 =-e^{-t/2}\langle\mu,e^{s/2}\rangle
 =-e^{-t/2}\chi_+(\mu)=0.                                  \tag{2.5}
\]

If `t<a`, similarly

\[
 (G*\mu)(t)
 =-e^{t/2}\langle\mu,e^{-s/2}\rangle
 =-e^{t/2}\chi_-(\mu)=0.                                   \tag{2.6}
\]

Therefore

\[
 \boxed{\operatorname {supp}(\mathcal W\mu)
 \subseteq\operatorname {conv}(\operatorname {supp}\mu).}   \tag{2.7}
\]

For a finite Dirac combination

\[
 \mu=\sum_{j=1}^Nc_j\delta_{t_j},\qquad
 \sum_jc_je^{t_j/2}=\sum_jc_je^{-t_j/2}=0,                  \tag{2.8}
\]

the potential is the explicit compact `L^2` vector

\[
 \mathcal W\mu(t)=-\sum_{j=1}^Nc_je^{-|t-t_j|/2}.            \tag{2.9}
\]

It is continuous and piecewise smooth; for a smooth primitive test it is
smooth.  Equation (2.4) proves injectivity.

> **Theorem 2.1 (primitive-cancellation lift).**  The map
> \[
> \mathcal W:\mathfrak I_{\rm prim}^{\rm meas}
> \longrightarrow L^2_c(\mathbb R)
>                                                                  \tag{2.10}
> \]
> is canonical, injective, translation covariant and support preserving in
> the sharp sense (2.7).  It sends every primitive finite periodic-frame
> vector to a genuine compactly supported Hilbert vector.  No basis vector
> is smoothed separately; support appears from cancellation of the two
> collective tails.

This is the requested way around the basiswise obstruction of D.74.

For distributions of positive order, (2.3) still makes sense
distributionally but need not be `L^2` (a second derivative of a Dirac can
produce a Dirac term).  The Hilbert-valued assertion is deliberately made
for finite measures.  This class contains the periodic Dirac frames and all
smooth compact tests.

## 3. Exact module law

Associativity and commutativity of convolution give, whenever one factor is
primitive,

\[
 \boxed{
 \mathcal W(\mu*\nu)
 =\mu*(\mathcal W\nu)
 =(\mathcal W\mu)*\nu.}                                    \tag{3.1}
\]

Thus `W` is a morphism from the regular primitive ideal to the convolution
module of compact potentials.  It is compatible with support addition:

\[
 \operatorname {supp}\mathcal W(\mu*\nu)
 \subseteq \operatorname {conv}(\operatorname {supp}\mu)
           +\operatorname {conv}(\operatorname {supp}\nu).   \tag{3.2}
\]

For windows this gives exact directed maps

\[
 \mathcal W_T:\mathfrak I_{\rm prim}^{\rm meas}
                 \cap\mathcal M([-T,T])
 \longrightarrow L^2([-T,T]),                               \tag{3.3}
\]

and zero-extension compatibility

\[
 E_{T,T'}\mathcal W_T=\mathcal W_{T'}\qquad(T<T')             \tag{3.4}
\]

on the smaller source.

The image product is different:

\[
 (\mathcal W\mu)*(\mathcal W\nu)
 =(G*G)*(\mu*\nu),                                          \tag{3.5}
\]

whereas `W(mu*nu)=G*(mu*nu)`.  The natural structure is therefore a
correspondence with the unbounded inverse `L`, not an algebra of smoothed
frames.

## 4. A primitive compact approximate identity

There is an unexpectedly simple approximate identity inside the primitive
ideal.  For `R>0`, put

\[
 \epsilon_R
 =\delta_0-\frac{\delta_R+\delta_{-R}}{2\cosh(R/2)}.          \tag{4.1}
\]

Direct calculation gives

\[
 \chi_+(\epsilon_R)=\chi_-(\epsilon_R)=0.                    \tag{4.2}
\]

For every translation-unitary Hilbert representation,

\[
 \|\epsilon_R*f-f\|_2
 \le {1\over\cosh(R/2)}\|f\|_2\xrightarrow[R\to\infty]{}0. \tag{4.3}
\]

Let `phi_delta` be a standard smooth compactly supported approximate
identity and choose `delta(R)->0`.  Then

\[
 \eta_R=\epsilon_R*\phi_{\delta(R)}                           \tag{4.4}
\]

is smooth, compactly supported and primitive, because the two characters
are multiplicative.  Equations (4.3)--(4.4) give

\[
 \eta_R*f\longrightarrow f                                   \tag{4.5}
\]

in `L^2`, in every fixed Sobolev topology on smooth inputs, and in the
Schwartz topology after the usual diagonal choice of `delta(R)`.  It does
not converge in the strict LF topology of `C_c^infinity`, because the
supports escape.  The `L^1` norms of the kernels are uniformly bounded.

The support expansion is necessary.  Suppose a bounded approximate identity
`eta_alpha in I_prim^meas` had supports in one fixed interval.  Its
Fourier--Laplace transforms would form a locally bounded normal family of
entire functions of uniformly bounded exponential type.  For every real
`xi`, choose a primitive test whose Fourier transform does not vanish at
`xi`; then the approximate-identity property forces

\[
 \widehat\eta_\alpha(\xi)\longrightarrow1.                   \tag{4.6}
\]

Montel compactness and the identity theorem make every subsequential entire
limit equal to `1`.  But

\[
 \widehat\eta_\alpha(i/2)
 =\widehat\eta_\alpha(-i/2)=0,                               \tag{4.7}
\]

a contradiction.

> **Theorem 4.1.**  The primitive ideal has a uniformly bounded smooth
> compactly supported approximate identity for its `L^2`/Sobolev/Schwartz
> actions.  Its supports must escape every fixed window.  Consequently it is
> compatible with the directed window system, but not with a single fixed
> support projection or with the strict LF topology.

## 5. No algebra homomorphism even after restricting to the ideal

The removal of the unit from the primitive ideal does not evade the
multiplicativity obstruction.  Let a continuous translation-covariant
linear realization have the convolution-multiplier form

\[
 T_\kappa\mu=\kappa*\mu.                                     \tag{5.1}
\]

Suppose it were multiplicative only on `I_prim^meas`:

\[
 T_\kappa(\mu*\nu)
 =(T_\kappa\mu)*(T_\kappa\nu)qquad(\mu,\nu\in\mathfrak I_{\rm prim}).
                                                                  \tag{5.2}
\]

Taking Fourier transforms gives

\[
 \widehat\mu(\xi)\widehat\nu(\xi)
 \widehat\kappa(\xi)
 \bigl(1-\widehat\kappa(\xi)\bigr)=0.                       \tag{5.3}
\]

For every real `xi` there is a primitive smooth compact test with nonzero
Fourier value there.  One construction is to smooth (4.1): on the real axis

\[
 \widehat\epsilon_R(\xi)
 =1-\frac{\cos(R\xi)}{\cosh(R/2)}>0.                          \tag{5.4}
\]

Thus (5.3) forces

\[
 \widehat\kappa(\xi)\in\{0,1\}\quad(\xi\in\mathbb R).       \tag{5.5}
\]

Continuity and connectedness make it constant.  If `kappa` is compactly
supported `L^2`, it is `L^1`; Riemann--Lebesgue excludes the constant `1`,
and the constant `0` gives the zero map.

> **Theorem 5.1 (ideal-algebra no-go).**  Every translation-covariant
> algebra homomorphism from the primitive ideal to compactly supported
> `L^2` convolution vectors is zero.  The module identity (3.1) is the
> strongest exact multiplicative structure available to a nonzero compact
> potential lift.

## 6. Compression pullback of the compact potential

Let `P_T` be the projection onto `[-T,T]` and `U` a unitary transform.  In
this section take smooth primitive `mu,nu`, so every form below is an
ordinary `L^2` form.  By (2.7), for `mu` supported in the window,

\[
 P_T\mathcal W_T\mu=\mathcal W_T\mu.                          \tag{6.1}
\]

Therefore the universal compression identity gives

\[
 \boxed{
 \mathcal W_T^*(U^*P_TU-P_T)\mathcal W_T
 =-((I-P_T)U\mathcal W_T)^*((I-P_T)U\mathcal W_T)\le0.}      \tag{6.2}
\]

This is a genuine source-defined negative square.  It has not been defined
from `B_nuc`.

For the ordinary real Fourier transform its value can be computed.  With
the convention `widehat(Du)(xi)=i xi widehat u(xi)`, (2.4) gives

\[
 \widehat{\mathcal W\mu}(\xi)
 =-{\widehat\mu(\xi)\over \xi^2+1/4}.                        \tag{6.3}
\]

If the target support projection is a frequency window `Omega_T`, then

\[
 q_{\mathcal W,T}(\mu,\nu)
 =-\int_{\mathbb R\setminus\Omega_T}
 {\widehat\mu(\xi)\overline{\widehat\nu(\xi)}
  \over(\xi^2+1/4)^2}\,d\xi.                                \tag{6.4}
\]

This multiplier is absolutely continuous and rational apart from the sharp
window.  By contrast, the exact A--B--C form is

\[
 \begin{aligned}
 B_{\rm nuc}(\mu,\nu)={}&
 \sum_p\log p\sum_{k\ne0}p^{-|k|/2}
       \langle\mu,S_{k\log p}\nu\rangle\\
 &+m_0\langle\mu,\nu\rangle
 -\langle\partial_\infty\mu,\partial_\infty\nu\rangle.
 \end{aligned}                                               \tag{6.5}
\]

Its convolution kernel has the full prime-power point masses and the Gamma
digamma multiplier.  Hence

\[
 \boxed{q_{\mathcal W,T}\ne B_{{\rm nuc},T}}                 \tag{6.6}
\]

for the archimedean Fourier compression.  Equality cannot be restored by a
two-dimensional jet term: the difference contains infinitely many
prime-power atoms.

Equation (6.6) does not exclude a genuinely adelic transform carrying
finite-place components.  It proves that the compact-potential functor alone
is the support module, not yet the trace-exact A--B--C comparison functor.

## 7. The correspondence pivot

The constructed data form a directed rigged correspondence

\[
 \mathfrak I_{\rm prim,T}^{\rm meas}
 \xrightarrow{\ \mathcal W_T\ }
 H^1_0([-T,T])
 \xrightarrow{\ L\ }
 \mathfrak I_{\rm prim,T}^{\rm meas},                       \tag{7.1}
\]

with

\[
 L\mathcal W_T=I,\qquad
 \mathcal W_T(a*b)=a*\mathcal W_T(b).                        \tag{7.2}
\]

The next construction should tensor this archimedean potential
correspondence with the periodic local-contact module before applying the
semilocal additive Fourier transform.  It must prove that the paired local
phase defects pull back to (6.5), rather than replacing (6.5) by the
archimedean tail (6.4).  This is now a module-intertwining problem; Theorem
5.1 rules out returning to an algebra embedding.

## 8. Verdict

Primitive cancellation does solve the support problem at the vector level.
The exact functor is the compact Green potential (2.3), and the primitive
ideal has the explicit approximate identity (4.1)--(4.4).  What fails is
algebra multiplication after Hilbert realization; the exact surviving law
is the bimodule identity (3.1).

The ordinary compression pullback is a negative square but is not `B_nuc`.
Therefore D.75 advances the D.73 contract by constructing a faithful,
supported, directed primitive module.  The remaining comparison is to
couple it to the finite periodic contact correspondence so that the adelic
phase pullback, not merely the real Fourier tail, equals all of (6.5).
