# R170_847 — Two-parameter PC curvature before hermitianization

## 0. Motivation and verdict

R170_846 corrected the undefined symbol `mathfrak P`, but its first
concrete carrier

\[
 \operatorname{Herm}(S_N^{\rm ren}A_M\mathscr F)
\]

falls into the class already computed in R161_062--064: a boundary
Hermitian power after the orientations are recombined. R170_843 proves
that this recombination leaves the support concomitant and does not by
itself transport the Wronskian sign.

The correct order of operations is therefore forced:

1. separate the two scales of the Euler leg and the integer leg;
2. differentiate in the antidiagonal direction;
3. preserve `S_N-C_N` and its jumps;
4. compress with the moving primitive projection;
5. only then take the Hermitian part and the diagonal.

This record defines that object. It does not yet prove its boundary
sign.

## 1. The antidiagonal derivation

Use the dilation of R170_841,

\[
 B(r)=U_r^{-1}BU_r,
 \qquad \dot\tau_a=-a\partial_t\tau_a.
\]

Introduce two independent parameters:

\[
 L_M(r),\qquad Z_N(q)=S_N(q)-C_N(q),
\]

and the derivation

\[
 \partial_-:=\left.(\partial_r-\partial_q)\right|_{r=q=1}.
 \tag{1.1}
\]

Then, by the product rule,

\[
 \boxed{
 \partial_-[L_M(r)Z_N(q)]
 =\dot L_MZ_N-L_M\dot Z_N
 =\mathcal A_{M,N}^{\rm ren}.}
 \tag{1.2}
\]

Its raw part is exactly the Wronskian of R170_843:

\[
 \partial_-[L_M(r)S_N(q)]
 =\mathcal A_{M,N}^{\rm raw}.
 \tag{1.3}
\]

The diagonal direction, in contrast, produces
`dot L Z+L dot Z`, i.e. the synchronized channel. So (1.1) is not a
cosmetic rewriting: it separates the two arithmetic jets that behave
differently.

## 2. Well-defined covariant compression

Let the physical window depend on the Euler leg `r`. For a positive
Hankel observer `G_delta` in its safe domain, first define the
bilinear form

\[
 \mathfrak C_{M,N,T,\delta}(r,q;F,G)
 :=\langle F,
   \Pi_{rT}G_\delta L_M(r)Z_N(q)\Pi_{rT}G\rangle.
 \tag{2.1}
\]

It is not declared that the operator inside (2.1) is symmetric. The
candidate Ward--PC form is its hermitianized antidiagonal derivative:

\[
 \boxed{
 \mathfrak W^-_{M,N,T,\delta}(F,G)
 :={1\over2}\left(
   \partial_-\mathfrak C(F,G)
  +\overline{\partial_-\mathfrak C(G,F)}
 \right).}
 \tag{2.2}
\]

This avoids inventing a symmetric PC operator. All expressions are
understood first in the common core; passing to the form domain
remains a separate analytic task.

The product rule gives the exact identity

\[
\begin{aligned}
 2\mathfrak W^-(F,F)
 =2\operatorname{Re}\{&
 \langle F,\dot\Pi_TG_\delta L_MZ_N\Pi_TF\rangle\\
 &+\langle F,\Pi_TG_\delta\mathcal A_{M,N}^{\rm ren}
                       \Pi_TF\rangle\\
 &+\langle F,\Pi_TG_\delta L_MZ_N\dot\Pi_TF\rangle\}.
 \tag{2.3}
\end{aligned}
\]

If the observer is also transported with `r`, the explicit term
`Pi dot G_delta LZ Pi` is added; it must not be hidden inside the
archimedean part. In (2.1)--(2.3) it is kept fixed in order to first
isolate the arithmetic curvature.

## 3. Arithmetic bulk already signed

Decompose

\[
 \mathcal A_{M,N}^{\rm ren}
 =\mathcal A_{M,N}^{\rm raw}
  -(\dot L_MC_N-L_M\dot C_N).
 \tag{3.1}
\]

For

\[
 M=N\ge\max\{N_0,\lceil e^{2T}\rceil\},
\]

R170_843--844 prove

\[
 \operatorname{Re}\langle F,
  \Pi_TG_\delta\mathcal A_{N,N}^{\rm raw}\Pi_TF\rangle
 =-\mathscr E_{N;T,\delta}^{\beta}(F)<0
 \tag{3.2}
\]

for `F` nonzero in the observed domain. The incomplete tail `k>N` is
included in `E^beta`; it has not been replaced by a complete
convolution.

By (3.1), the central term of (2.3) is exactly

\[
 -\mathscr E_{N;T,\delta}^{\beta}(F)
 -\operatorname{Re}\langle F,
  \Pi_TG_\delta(\dot L_NC_N-L_N\dot C_N)\Pi_TF\rangle.
 \tag{3.3}

This is an identity proved under the domain gate of R170_844, not a
sign conjecture.

## 4. Exact PC extension off the diagonal

The PC identity does admit an exact extension to `(r,q)`, but it is
not obtained by moving only `L` and `S`. Define

\[
 X_r=U_r^{-1}XU_r=rX,
 \quad \mathscr F_r=U_r^{-1}\mathscr FU_r,
 \quad \mathcal M_r=U_r^{-1}\mathcal MU_r,
 \tag{4.1}
\]

so that

\[
 X_r+\mathscr F_rX_r\mathscr F_r=\mathcal M_r.
 \tag{4.2}
\]

Set

\[
\begin{aligned}
 S_N(q)&=\sum_{n\le N}n^{-1/2}\tau_{\log n/q},\\
 L_M(r)&=\sum_{d\le M}{\Lambda(d)\over\sqrt d}
                       \tau_{\log d/r},\\
 K_N(r,q)&={r\over q}\sum_{n\le N}{\log n\over\sqrt n}
                       \tau_{\log n/q},\\
 A_M(r)&=\mathcal M_r-(L_M(r)+L_M(r)^*),\\
 E_N(r,q)&=S_N(q)\mathscr F_r-JS_N(q),\\
 H_{M,N}(r,q)&=L_M(r)S_N(q)-K_N(r,q).
\end{aligned}
 \tag{4.3}
\]

The factor `r/q` is not optional. It gives exactly

\[
 [X_r,S_N(q)]=-K_N(r,q).                                    \tag{4.4}
\]

**Theorem 4.1 (two-scale PC).** On the Schwartz core, for all
`r,q>0`,

\[
\boxed{
 S_N(q)A_M(r)\mathscr F_r
 =\{X_r,E_N(r,q)\}-L_M(r)^*E_N(r,q)
  -JH_{M,N}(r,q)-H_{M,N}(r,q)\mathscr F_r.}
 \tag{4.5}
\]

**Proof.** The proof of Paper 47 Theorem `PCfinite` uses only (4.2),
(4.4), `JL(r)=L(r)^*J`, commutation of the translation sums, and the
definition of `H`. All of these hold for `(r,q)` separately. Repeating
those steps gives (4.5). QED.

In particular, applying `partial_-` to (4.5) produces an exact
operator identity, not the transversal derivative of an equality
defined only on `r=q`.

The Chebyshev jet that must be preserved is also explicit. If

\[
 K_N^{(2,\partial)}
 :=\sum_{n\le N}{(\log n)^2\over\sqrt n}
       \partial_t\tau_{\log n},
\]

then

\[
 \partial_-K_N(r,q)|_{1,1}=2K_N+K_N^{(2,\partial)}.
 \tag{4.6}
\]

This piece is necessary so that the synchronized terms and the
terminal jumps are not lost when extracting the Wronskian.

## 5. Why this is still not VIR--LB

Form (2.2) correctly contains the Wronskian and the moving connection,
but still does not automatically contain

\[
 {1\over2\pi}\int \tau m'(\tau)|\widehat F(\tau)|^2d\tau.
 \]

That term arises from differentiating `A_M(r) mathscr F_r` in (4.5),
not only `L_M(r)Z_N(q)`. The correct coupling is, by Theorem 4.1, the
antidiagonal derivative of the full side

\[
 S_N(q)A_M(r)\mathscr F_r=\operatorname{PC}_{M,N}(r,q).
 \tag{5.1}
\]

and showing that, on expanding (4.5), the terms `dot mathscr F` and
`dot mathcal M` produce the archimedean virial, while the part
`dot L Z-L dot Z` is (2.3). The differentiated identity is already
proved; what remains is its compression, polarization and reduction
by first contact.

## 6. Corpus collisions avoided by (2.2), and remaining gate

* It is not the PC square of R161_002.
* It is not a linear limit of PC as in R161_018.
* It does not vary coefficients exteriorly, a route voided by
  R162_305.
* It does not use the cross Tate Gram as a projection, the error of
  R161_063.
* It does not hermitianize before separating the legs, the collision
  of R170_843.
* It preserves the polar continuum and the hyperbola `k>N`.

The next load-bearing identity is now formulated with existing
objects:

> **PC--curvature.** Differentiate (4.5) by `partial_-` at finite
> cutoffs, transport the window on leg `r`, expand both sides before
> recombining, and prove that its Hermitian diagonal on a
> first-contact vector is the sum of: minus the full virial, minus
> `E^beta`, minus the synchronized tail energy, and a single explicit
> polar residue that cancels against the `dot Pi` terms.

This identity remains open. Its advantage over R170_844 is that it no
longer uses `mathfrak P` and its central arithmetic block is literally
(1.2).

## 7. Status

```text
antidiagonal derivation of two legs                           DEFINED
identity partial_-(LZ)=A_ren                                   PROVED
later compressed/hermitianized form                             DEFINED
Wronskian bulk inside the form                                   PROVED
polar continuum preserved                                       PROVED
exact two-scale PC identity                                     PROVED
antidiagonal jet of K_N                                          COMPUTED
coupling with full PC and the archimedean virial                 OPEN
dotPi/Tate cancellation against the polar residue                 OPEN
PC--curvature / VIR--LB / D                                       OPEN
```
