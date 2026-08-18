# D.73 — A relative ordered object and the support-compression pivot

## Status

D.72 identifies the missing A--B--C datum as an ordered adelic gluing whose
pullback is the rank-two boundary majorant.  This note constructs the first
half of that datum without assuming a sign:

* the divergent positive and negative feature norms are replaced by a
  support-compressed **relative form**;
* the form stabilizes exactly under prime exhaustion and is compatible with
  zero-extension of support windows;
* its dagger and order are the ordinary `L^2` adjoint and closed-form cone.

Thus the cofinal neutral divergence is removed before asking for
contractivity.  The naive alternative—quotienting an infinite hyperbolic
Krein sum by its neutral diagonal—is proved impossible: the diagonal is not
radical, and its Krein reduction is zero.

The second half, contractivity, is then attacked by support compression.
The raw two-jet inclusion fails by an infinite-rank cross-window theorem.
The surviving datum is a supported trace-exact Poisson lift compatible with
the relative form.  It is specified exactly but not constructed.  No RH,
zeta zero, Weil positivity, screw positivity or spectral polarization is
used.  The paper is not modified.

## 1. The fixed-window form domain

Let

\[
 H_T=L^2([-T,T])                                           \tag{1.1}
\]

and extend its vectors by zero to `L^2(R)`.  Put

\[
 \mathcal D_T=left\{F\in H_T:
 \int_{\mathbb R}\log(2+|\tau|)|\widehat F(\tau)|^2d\tau
 <\infty\right\}.                                         \tag{1.2}
\]

The complete Gamma form is closed on `D_T`; every finite-place translation
is bounded on `H_T`.  Hence all finite-cutoff prime--Gamma forms below have
the same dense form domain.

For a finite set of primes `P`, define

\[
 \begin{aligned}
 R_{P,T}(F,G)
 :={}&\sum_{p\in P}\log p
 \left(\langle A_pF,A_pG\rangle-\langle F,G\rangle\right)\\
 &+m_0\langle F,G\rangle
 -\langle\partial_\infty F,\partial_\infty G\rangle,
 \end{aligned}                                             \tag{1.3}
\]

where

\[
 A_p=\sqrt{1-p^{-1}}(I-p^{-1/2}S_{\log p})^{-1}.           \tag{1.4}
\]

This is defined from the A--B local orbit coefficients and the Gamma
oscillator before taking a sign.  At finite `P`, (1.3) is exactly

\[
 R_{P,T}=\mathbf S_P^*\mathbf S_P-mathbf B_P^*\mathbf B_P
                                                                    \tag{1.5}
\]

as a closed Hermitian form.

## 2. Exact prime stabilization

Functional calculus gives the norm-convergent identity

\[
 A_p^*A_p-I=
 \sum_{k\ne0}p^{-|k|/2}S_{k\log p}.                       \tag{2.1}
\]

If

\[
 \log p>2T,                                                \tag{2.2}
\]

then `[-T,T]` and every nonzero translate by `k log p` are disjoint.
Therefore

\[
 \langle F,S_{k\log p}G\rangle=0
 \quad(F,G\in H_T,\ k\ne0),                              \tag{2.3}
\]

and hence

\[
 \boxed{
 P_T(A_p^*A_p-I)P_T=0.}                                   \tag{2.4}
\]

All powers `p^k` are included in (2.1); their vanishing in (2.4) is a
support theorem, not a truncation.

Let

\[
 \mathcal P_T=\{p:p\le e^{2T}\}.                         \tag{2.5}
\]

Then for every finite `P` containing `P_T`,

\[
 \boxed{R_{P,T}=R_{\mathcal P_T,T}.}                       \tag{2.6}
\]

We may therefore define the cofinal relative object

\[
 \mathfrak R_T:=R_{\mathcal P_T,T}.                        \tag{2.7}
\]

> **Theorem 2.1 (relative prime stabilization).**  The form `R_T` is a
> source-defined, closed, upper-bounded Hermitian form on `D_T`.  It contains
> every prime power capable of meeting the support window and the complete
> Gamma oscillator.  The cofinal prime limit is exactly stationary after
> the finite set (2.5).

The scalar equality with `B_(nuc,T)` is the already proved D.32 comparison;
it is not used to define the ordered object.

## 3. Dagger and cone

Equip `D_T` with the Gamma graph norm and let `Form_T` be the real vector
space of continuous Hermitian sesquilinear forms on that graph Hilbert
space.  The form `R_T` belongs to this space (and, in its upper-semibounded
orientation, is closed on `H_T`).  The vector space carries

\[
 q^*(F,G)=\overline{q(G,F)},                               \tag{3.1}
\]

and the intrinsic cone

\[
 \mathrm{Form}_{T,+}
 =\{q:q(F,F)\ge0\text{ for every }F\in\mathcal D_T\}.     \tag{3.2}
\]

This is an actual ordered dagger object, not an order placed on a stable
mapping spectrum.  The relative form `R_T` is self-adjoint in this sense.
For the two boundary maps

\[
 M_TF=(M_-(F),M_+(F)),                                     \tag{3.3}
\]

the desired ordered assertion is now well-typed:

\[
 \mathfrak R_T-zI\le M_T^*C_{T,z}M_T.                     \tag{3.4}
\]

Thus D.73 constructs the category in which the D.72 majorant can be stated,
without declaring (3.4) true.

## 4. Compatibility under support enlargement

For `0<T<T'`, let

\[
 E_{T,T'}:H_T\longrightarrow H_{T'}                       \tag{4.1}
\]

be zero extension.  Full-line translation correlations and the Gamma
Fourier multiplier are unchanged by this extension.  A prime power with
displacement greater than `2T` has zero correlation on the extended vector,
even if it belongs to `P_(T')`.  Therefore

\[
 \boxed{
 E_{T,T'}^*\mathfrak R_{T'}E_{T,T'}=\mathfrak R_T.}        \tag{4.2}
\]

The Tate moments are also unchanged:

\[
 M_{T'}E_{T,T'}=M_T.                                      \tag{4.3}
\]

> **Theorem 4.1 (directed relative system).**  The triples
> \[
> (\mathcal D_T,\mathfrak R_T,M_T)                         \tag{4.4}
> \]
> form a directed system of ordered form objects under zero extension.
> Reflection commutes with every transition and splits (4.4) into the even
> and odd one-jet systems.

This is the requested cofinal compatibility.  It is exact, not an interval
or asymptotic statement.

## 5. Why the neutral Krein quotient fails

One might instead retain the two divergent feature spaces in

\[
 \mathcal K=H\oplus H,qquad
 [(x,y),(x',y')]=\langle x,x'\rangle-\langle y,y'\rangle,   \tag{5.1}
\]

and quotient by the neutral diagonal

\[
 \mathcal N=\{(h,h):h\in H\}.                              \tag{5.2}
\]

This does not define a quotient form.  A Hermitian form descends to
`K/N` only if `N` lies in its radical.  But

\[
 [(h,h),(h,0)]=\|h\|^2\ne0.                               \tag{5.3}
\]

Moreover

\[
 \mathcal N^{[\perp]}=\mathcal N,                          \tag{5.4}
\]

so the standard Krein reduction is

\[
 \mathcal N^{[\perp]}/\mathcal N=0.                       \tag{5.5}
\]

> **Proposition 5.1 (neutral-quotient no-go).**  The common prime norm
> cannot be cancelled by quotienting the hyperbolic direct sum by its
> diagonal.  The ordinary quotient has no induced form, while the canonical
> coisotropic reduction kills the entire block.

This justifies taking the operator/form difference before the cofinal
limit, as in Sections 1--4.

## 6. The support-compression sign mechanism

Let `H` be a Hilbert space, `P` an orthogonal support projection and `U` a
unitary Fourier--Poisson transform.  For every map `mathcal M` satisfying

\[
 P\mathcal M=\mathcal M,                                   \tag{6.1}
\]

one has the source identity

\[
 \boxed{
 \mathcal M^*(U^*PU-P)\mathcal M
 =-(QU\mathcal M)^*(QU\mathcal M)\le0,
 \qquad Q=I-P.}                                           \tag{6.2}
\]

This is independent of any arithmetic trace or zeta spectrum.  Therefore a
supported lift

\[
 \mathcal M_T:\mathcal D_T\longrightarrow PH              \tag{6.3}
\]

with the trace-exact pullback

\[
 \boxed{
 \mathfrak R_T-M_T^*C_TM_T
 =\mathcal M_T^*(U^*PU-P)\mathcal M_T}                    \tag{6.4}
\]

would prove the boundary majorant and close the fixed-window sign.

Because `mathfrak R_T` is already a directed relative object, the required
lift must additionally satisfy

\[
 \mathcal M_{T'}E_{T,T'}=J_{T,T'}\mathcal M_T             \tag{6.5}
\]

for the semilocal support inclusions `J_(T,T')`.

## 7. The raw primitive inclusion is not supported

The obvious candidate takes the primitive test vector itself in the
ambient Fourier--Poisson space.  Two scalar jets cannot force the support
condition (6.1).

Indeed decompose `H=PH direct-sum QH` and consider the cross-window block

\[
 b=PUQ:QH\longrightarrow PH.                              \tag{7.1}
\]

Let

\[
 \mathcal P_0=\ker M_+\cap\ker M_-                        \tag{7.2}
\]

have codimension at most two.  If `b` vanished on
`QH intersect P_0`, it would factor through the quotient

\[
 QH/(QH\cap\mathcal P_0),                                 \tag{7.3}
\]

whose dimension is at most two.  Thus

\[
 \mathrm{rank}\,b>2                                 \tag{7.4}
\]

forces a primitive `y in QH` with `PUy!=0`.

For the archimedean Fourier transform between a nonempty interval and its
exterior, `b` has infinite rank: the kernel functions

\[
 x\longmapsto e^{-2\pi ixy_j}                              \tag{7.5}
\]

for distinct exterior points `y_j` are linearly independent on every
interval.  The same continuous archimedean block is present in the
semilocal Fourier--Poisson transform.  Hence the raw two-jet source is not
triangular under `P` and `U`.

> **Theorem 7.1 (raw support no-go).**  Imposing the two Tate jets does not
> put the analytic test realization in the supported range required by
> (6.1).  The raw phase operator remains indefinite on the primitive
> source.  A new lift, not the identity inclusion or primitive projection,
> is necessary.

## 8. Attempted minimal-norm supported lift

A natural pivot is to prescribe the two-chart Poisson relation `A h=F` and
choose

\[
 \mathcal M_T(F)=
 \mathop{\mathrm{argmin}}_{h\in PH,\ Ah=F}\|h\|.            \tag{8.1}
\]

When it exists, this is the Moore--Penrose formula

\[
 \mathcal M_T=P A^*(APA^*)^\dagger.                        \tag{8.2}
\]

It is automatically supported.  However three independent statements are
needed before (8.1) becomes the desired construction:

1. every primitive periodic test lies in `Ran(AP)`;
2. the range is closed and (8.2) is compatible with semilocal enlargement;
3. its phase pullback is exactly (6.4), including every `p^k` and Gamma.

Neither enriched Yoneda nor the Witt determinant proves item 1: they
construct sections and scalar contacts, not surjectivity of the adelic
summation/support map.  Item 3 is a new operator comparison, not a formal
property of Moore--Penrose inversion.  Defining `A` from a square root or
spectral polarization of the already known form `mathfrak R_T` would make
(6.4) tautological and is excluded.

Thus (8.1) is a well-typed candidate but not yet a constructed functor on
the full primitive source.

## 9. Minimal independent support theorem

The remaining datum can now be stated without the divergent-norm ambiguity
of D.72.

> **Support theorem required for D.**  Construct from periodic Yoneda
> multiplication, Witt dynamics and additive Poisson duality a family
> `mathcal M_T` such that:
>
> 1. `P mathcal M_T=mathcal M_T`;
> 2. the exact relative pullback (6.4) holds before taking a sign;
> 3. `mathcal M_T` separates nonzero primitive tests;
> 4. the directed compatibility (6.5) holds.

Then (6.2) gives

\[
 \mathfrak R_T(F,F)\le\langle M_TF,C_TM_TF\rangle,         \tag{9.1}
\]

and hence nonpositivity on the primitive space.  Conversely, constructing
the lift by polar decomposition of `mathfrak R_T` would use precisely the
sign being proved and is not an independent support theorem.

## 10. Verdict

The cofinal ordered object itself is now constructed: it is the stabilized
relative form `mathfrak R_T`, with exact prime and window compatibility.
The hyperbolic neutral quotient is not a substitute.

Contractivity has not been obtained.  The raw two-jet inclusion fails the
support condition by infinite rank, and the minimal-norm supported lift
requires a new range theorem and the trace-exact comparison (6.4).  These
are precisely the remaining source statements; no global sign or row-D
closure is claimed.
