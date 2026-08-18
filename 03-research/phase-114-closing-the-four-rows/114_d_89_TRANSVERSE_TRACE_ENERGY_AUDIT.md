# D.89 — Transverse trace energy and its exact extra channel

## Status

**Typing correction (D.91).**  The Künneth tensor
\(f\boxtimes\widetilde g\) enters the Weil pairing through the *linear*
character \(\ell(\mathcal A(f\boxtimes\widetilde g))
=B_{\rm nuc}(f,g)\).  It must not be treated as a new test \(h=\mathcal AF\)
and inserted into \(B_{\rm nuc}(h,h)\).  Sections 5--6 below audit that
latter composite as an analytic map, but it is not the correctly typed
Künneth realization of the Weil quadratic form.  D.91 gives the corrected
polarized comparison.  The transverse trace/coisometry theorems in
Sections 1--4 are unaffected.

D.88 identifies the first global landing problem: mixed periodic Künneth
lands in \(L^2(\mathbb R^2)\), whereas row C requires the addition
pushforward to one logarithmic variable.  This note constructs a canonical
transverse graph domain from the two logarithmic covers and proves the
sharp trace theorem.

The analytic trace is successfully constructed.  For every \(s>1/2\),
weighting the relative coordinate \(u=x-y\) by
\((1+u^2)^s\) makes addition pushforward bounded.  The first integral
choice \(s=1\) gives
\[
 \|\mathcal AF\|_2^2\le{\pi\over2}
 \int_{\mathbb R^2}(1+(x-y)^2)|F(x,y)|^2dxdy.
\]
The constant is sharp and equality occurs on an infinite-dimensional
family.

Two exact obstructions remain.

First, the graph norm is invariant under equal half-translations of the
two rulings, but the A--B--C Dirichlet scalar acts on one scalar factor.
One-sided translation shifts \(u\) and changes the graph norm by an
explicit quadratic cocycle.  Half-translation would repair covariance but
requires a square root of \(U_n\) in each ruling, which is not an arrow of
the integer correspondence semigroup.

Second, the trace defect is a new positive channel.  The preparation Gram
after trace is still exactly \(-4B_{\rm nuc}\), with all \(p^k\) and Gamma,
only if this channel is not inserted.  Inserting it to obtain Hilbert
positivity changes the Gram by the explicitly computed defect.  Adding it
in both parities preserves the Gram but cancels its help.  Because the
sharp defect vanishes on a copy of the entire one-variable primitive
source, it cannot dominate the positive round-trip output without the
original row-D inequality.

No RH or sign of \(B_{\rm nuc}\) is used.  The paper is not modified.

## 1. Geometry of the transverse coordinate

At the nuclear level there is no discontinuity: the natural source is
\[
 \mathcal S(\mathbb R)\widehat\otimes_\pi\mathcal S(\mathbb R)
 \simeq\mathcal S(\mathbb R^2),                           \tag{1.0}
\]
and both diagonal restriction in Fourier coordinates and addition
pushforward are continuous maps to \(\mathcal S(\mathbb R)\).  D.88's
unboundedness concerns the plain \(L^2\) Hilbertization.  The purpose of
this section is to construct the Hilbert graph norm supplied by the
conormal geometry, not to repair the already valid nuclear map.

The two periodic factors have canonical logarithmic covers with origins
fixed by their neutral points.  On the product cover write
\[
 t=x+y,\qquad u=x-y.                                     \tag{1.1}
\]
The addition map is the lift of Künneth multiplication to the row-C
logarithmic variable.  Its pushforward is
\[
 (\mathcal AF)(t)=\int_{\mathbb R}F(x,t-x)\,dx
 ={1\over2}\int_{\mathbb R}
 F\left({t+u\over2},{t-u\over2}\right)du.                \tag{1.2}
\]

In two-variable Fourier coordinates, (1.2) is restriction to the diagonal:
\[
 \widehat{\mathcal AF}(\tau)=\widehat F(\tau,\tau).       \tag{1.3}
\]
Thus regularity in the normal Fourier direction is the correct missing
datum.  Under inverse Fourier transform, one normal derivative is
multiplication by \(u=x-y\).

For \(s>1/2\), define the transverse graph space as the completion of
compact smooth Künneth sections for
\[
 \|F\|_{\perp,s}^2
 :=\int_{\mathbb R^2}(1+(x-y)^2)^s|F(x,y)|^2dxdy.        \tag{1.4}
\]
This is source-defined from the two log covers.  In the Bloch description
it is the graph norm of the fractional normal connection
\((1+D_\perp^2)^{s/2}\) on the two-character field.  It acts on the flat
Hilbert coefficient in D.88 and leaves the finite ordered-extremal frame
unchanged.

For \(s=1\), this is the first Dirichlet graph norm on the conormal of the
diagonal in Fourier space:
\[
 \|F\|_{\perp,1}^2
 =\|\widehat F\|_2^2+\|D_\perp\widehat F\|_2^2.          \tag{1.5}
\]
The additive self-dual Fourier coordinate and the two neutral points fix
the scale in (1.5).

The construction is functorial under principal translations and under
exchange of the two rulings, which sends \(u\) to \(-u\).  The choice
\(s=1\) is the first integral graph connection.  The trace theorem works
for every \(s>1/2\); no claim that geometry singles out a unique
fractional exponent is needed.

## 2. Sharp transverse trace theorem

Put
\[
 C_s=\int_{\mathbb R}(1+u^2)^{-s}du
 ={\sqrt\pi\,\Gamma(s-\tfrac12)\over\Gamma(s)}.          \tag{2.1}
\]
By Cauchy--Schwarz in (1.2),
\[
\begin{aligned}
 |\mathcal AF(t)|^2
 \le {1\over4}C_s
 \int_{\mathbb R}(1+u^2)^s
 \left|F\left({t+u\over2},{t-u\over2}\right)\right|^2du.
                                                                  \tag{2.2}
\end{aligned}
\]
The Jacobian is \(dx\,dy=\tfrac12dt\,du\).  Integrating (2.2) gives
\[
 \boxed{
 \|\mathcal AF\|_2^2\le {C_s\over2}\|F\|_{\perp,s}^2.}   \tag{2.3}
\]

The constant is sharp.  For arbitrary \(a\in L^2(\mathbb R)\), define
\[
 F_{a,s}\left({t+u\over2},{t-u\over2}\right)
 ={a(t)\over(1+u^2)^s}.                                  \tag{2.4}
\]
Then
\[
 \mathcal AF_{a,s}={C_s\over2}a,\qquad
 \|F_{a,s}\|_{\perp,s}^2={C_s\over2}\|a\|_2^2,           \tag{2.5}
\]
and equality holds in (2.3).

For \(s=1\), \(C_1=\pi\), so
\[
 \boxed{
 \|\mathcal AF\|_2^2\le{\pi\over2}
 \left(\|F\|_2^2+\|(x-y)F\|_2^2\right).}                \tag{2.6}
\]
Therefore
\[
 T_\perp=\sqrt{2/\pi}\,\mathcal A:
 \mathcal H_{\perp,1}\longrightarrow L^2(\mathbb R)      \tag{2.7}
\]
 is a contraction constructed before any arithmetic sign.

### 2.1 Minimal Poisson extension and coisometry

Give the same vector space the sharply normalized Hilbert norm
\[
 \|F\|_{\mathcal K_s}^2={C_s\over2}\|F\|_{\perp,s}^2.    \tag{2.8}
\]
Then the unscaled geometric pushforward
\[
 \mathcal A:\mathcal K_s\longrightarrow L^2(\mathbb R)  \tag{2.9}
\]
is a coisometry.  Its Hilbert adjoint is the explicit Poisson/minimal
extension
\[
 \boxed{
 (\mathcal A^\dagger a)
 \left({t+u\over2},{t-u\over2}\right)
 ={2\over C_s}{a(t)\over(1+u^2)^s}.}                    \tag{2.10}
\]
Indeed, the Jacobian calculation used in (2.2) gives
\[
 \langle\mathcal AF,a\rangle_{L^2}
 =\langle F,\mathcal A^\dagger a\rangle_{\mathcal K_s},
 \qquad
 \mathcal A\mathcal A^\dagger=I.                        \tag{2.11}
\]
Consequently \(\mathcal A^\dagger\) is an isometry and
\[
 \mathcal K_s=\ker\mathcal A\ \widehat\oplus\
 \mathrm{Ran}\,\mathcal A^\dagger.                  \tag{2.12}
\]
The normalization in (2.8) is forced by the coisometry equation and leaves
the row-C convolution \(\mathcal A\) itself unscaled.

This constructs the requested Gysin/Thom-type Hilbert landing from the
conormal graph energy.  It is a statement about the positive Hilbert
norm.  It is not yet the \(J\)-contractivity of the arithmetic preparation.

## 3. Exact scalar-covariance defect

Let \(S_a^{(1)}=S_a\otimes I\) be the one-sided lift of the row-C
translation.  It satisfies
\[
 \mathcal A S_a^{(1)}=S_a\mathcal A.                     \tag{3.1}
\]
However, changing variables gives
\[
\boxed{
\begin{aligned}
 \|S_a^{(1)}F\|_{\perp,1}^2
 ={}&\|F\|_{\perp,1}^2
 +2a\,\mathrm{Re}\,\langle uF,F\rangle
 +a^2\|F\|_2^2.
\end{aligned}}                                           \tag{3.2}
\]
Thus the trace domain is covariant as a vector space but the constructed
dagger norm is not invariant under the one-sided scalar action.

There is an analytic repair:
\[
 \widetilde S_a=S_{a/2}\otimes S_{a/2}.                  \tag{3.3}
\]
Then
\[
 \mathcal A\widetilde S_a=S_a\mathcal A,\qquad
 \|\widetilde S_aF\|_{\perp,s}=\|F\|_{\perp,s}.          \tag{3.4}
\]
This distributes the central scaling equally between the two rulings.
For \(a=\log n\), it uses \(U_{\sqrt n}\) in each factor.  Rows A--B use
the integer Dirichlet action \(\delta_n\), and their Künneth scalar map is
not equipped with a comultiplication
\[
 \delta_n\longmapsto\delta_{\sqrt n}\otimes\delta_{\sqrt n}.       \tag{3.5}
\]
Hence (3.3) is canonical in the continuous scaling representation but is
not natural for the constructed integer correspondence category.

This is not merely a normalization issue.  If a Hilbert norm on the
relative \(u\)-coordinate made all one-sided translations unitary and made
the nonzero invariant functional \(f\mapsto\int f(u)du\) bounded, its
Riesz vector would be fixed by every translation.  The regular
translation representation has no nonzero fixed vector.  Thus a bounded
trace and unitary one-sided covariance require adding a trivial spectral
summand at normal frequency zero.

## 4. The forced positive trace channel

Define the sharp trace defect
\[
 \boxed{
 \mathcal D_s(F,G)
 ={C_s\over2}\langle F,G\rangle_{\perp,s}
 -\langle\mathcal AF,\mathcal AG\rangle.}                \tag{4.1}
\]
Theorem (2.3) says \(\mathcal D_s\ge0\).  At \(s=1\),
\[
\begin{aligned}
 \mathcal D_1(F,F)
 ={\pi\over2}\left(\|F\|_2^2+\|(x-y)F\|_2^2\right)
 -\|\mathcal AF\|_2^2.                                  \tag{4.2}
\end{aligned}
\]
Equations (2.4)--(2.5) show
\[
 \mathcal D_s(F_{a,s},F_{a,s})=0
 \quad\text{for every }a\in L^2(\mathbb R).              \tag{4.3}
\]

In the coisometric normalization this is exactly the orthogonal kernel
energy:
\[
 \boxed{
 \mathcal D_s(F,F)
 =\|F\|_{\mathcal K_s}^2-\|\mathcal AF\|_2^2
 =\|(I-\mathcal A^\dagger\mathcal A)F\|_{\mathcal K_s}^2.}        \tag{4.4}
\]

Adding the minimal trivial transverse summand makes the trace bounded
tautologically:
\[
 F\longmapsto(F,\mathcal AF),\qquad
 \|F\|_{\rm ext}^2=\|F\|_{\rm reg}^2+c\|\mathcal AF\|^2. \tag{4.5}
\]
The new summand is an entire copy of the longitudinal row-C Hilbert space,
fixed by relative translations.  It is exactly a positive trace channel,
not a consequence of the original periodic norm.

## 5. Pullback of the arithmetic preparation

For \(F\in\mathcal H_{\perp,s}\), put \(f=\mathcal AF\), apply the two Tate
conditions to \(f\), and use the D.86 state
\[
 f\longmapsto(p(f),z(f))
 \xrightarrow{\mathcal Q}
 (r_0(f),C^{1/2}z(f)).                                   \tag{5.1}
\]
Nothing in the transverse graph completion changes the row-C local
operators.  Therefore
\[
\boxed{
 \langle\mathcal Qf,J\mathcal Qg\rangle
 =-4B_{\rm nuc}(f,g),\qquad f=\mathcal AF,\ g=\mathcal AG.}       \tag{5.2}
\]
Explicitly,
\[
\begin{aligned}
 B_{\rm nuc}(f,g)
 ={}&\sum_p(\log p)\sum_{k\ne0}p^{-|k|/2}
      \langle f,S_{k\log p}g\rangle\\
 &+m_0\langle f,g\rangle
 -\langle\partial_\infty f,\partial_\infty g\rangle.     \tag{5.3}
\end{aligned}
\]
Thus every \(p^k\) and the complete Gamma term remain exact.

The transverse energy is absent from (5.2).  If its positive defect is
inserted as an extra negative preparation channel, the Gram becomes
\[
 -4B_{\rm nuc}(\mathcal AF,\mathcal AF)+\mathcal D_s(F,F).
                                                                  \tag{5.4}
\]
This is positive in one additional direction but is no longer the row-D
form.  If a copy of \(\mathcal D_s\) is inserted in the opposite parity to
restore (5.2), the two copies cancel in the supermetric and supply no
inequality.

## 6. Why the trace defect cannot absorb the Schur channel

The desired round-trip inequality after trace is
\[
 \|C^{1/2}z(\mathcal AF)\|^2
 \le\|r_0(\mathcal AF)\|^2.                              \tag{6.1}
\]
One might try to prove the weaker augmented inequality
\[
 \|C^{1/2}z(\mathcal AF)\|^2
 \le\|r_0(\mathcal AF)\|^2+\mathcal D_s(F,F).            \tag{6.2}
\]
Even if (6.2) were proved, it would establish positivity of the modified
form (5.4), not row D.

More decisively, (4.3) shows that the trace defect supplies no uniform
margin.  Given any one-variable primitive test \(a\), scale it so that
\[
 \mathcal AF_{a,s}=a.                                    \tag{6.3}
\]
Then
\[
 \mathcal D_s(F_{a,s},F_{a,s})=0.                        \tag{6.4}
\]
On this embedded copy of the entire primitive source, (6.2) reduces
exactly to (6.1).  Therefore no argument based solely on the positive
trace defect can absorb the Schur channel; it would still have to prove
row D on the sharp subspace.

The Gamma oscillator does not change this conclusion.  It acts on the
longitudinal output \(a(t)\) and supplies no normal derivative in \(u\).
For the sharp lifts (2.4), every Gamma value is retained in (5.3) while
the transverse defect remains zero.

## 7. Conclusion

The requested transverse trace operator has been constructed, with a
sharp norm, a source-geometric normal connection, and an explicit
minimal-extension adjoint.  It is a coisometry after the forced
normalization (2.8).  Its composition with the round-trip state preserves
the exact prime-power--Gamma Gram.

It does not produce the dagger theorem.  Its norm is incompatible with
the one-sided integer scalar action; equal half-translations repair the
metric only after adjoining square-root correspondences.  The positive
trace defect forced by boundedness either changes the arithmetic Gram or
cancels in the supermetric.  Since that defect vanishes on a copy of every
one-variable primitive test, it cannot absorb the positive round-trip
channel without the original row-D inequality.
