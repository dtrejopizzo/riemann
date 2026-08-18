# D.69 — Stieltjes and de Branges audit of the two-jet compression

## Status

This note attacks the coupled prime--Gamma operator after the two Tate jets.
It proves two results.

1. The most direct scalar Stieltjes representation is impossible for the
   actual source multiplier.  It already fails in the first prime cell,
   where only the complete Gamma term and the `n=2` contact occur.
2. After reflection and one jet per parity channel, there is an exact
   Schur--Stieltjes representation.  Its measure is supported on the
   required half-line if and only if the compressed operator has the
   desired sign, modulo an explicitly stated cyclicity/persistent-mode
   condition.  Thus declaring this measure positive with the right support,
   or declaring the associated de Branges function to have the required
   half-line property, would assume the missing Hodge theorem unless that
   support is proved independently.

No zeta zero, Weil positivity, screw positivity or RH assumption is used.
The paper is not modified.

## 1. The scalar prime--Gamma multiplier in the first cell

Let

\[
 {\log2\over2}<T<{\log3\over2}.                            \tag{1.1}
\]

Then the only prime-power displacement not killed by the support window is
`log 2`.  With

\[
 a=\log2,\qquad c={\log2\over\sqrt2},                      \tag{1.2}
\]

the exact D.55 multiplier is

\[
 b_T(\tau)=-\mathfrak a(\tau)+2c\cos(a\tau),               \tag{1.3}
\]

where

\[
 \mathfrak a(\tau)=
 \mathrm{Re}\,\psi\left({1\over4}+{i\tau\over2}\right)
 -\log\pi.                                                 \tag{1.4}
\]

For positive `tau`, termwise differentiation of the trigamma series gives

\[
 \mathfrak a'(\tau)
 ={\tau\over2}\sum_{j=0}^\infty
 {j+1/4\over((j+1/4)^2+\tau^2/4)^2}>0.                    \tag{1.5}
\]

Set

\[
 \tau_0={3\pi\over2a},\qquad \beta={\tau_0\over2}
 ={3\pi\over4\log2}>3.                                   \tag{1.6}
\]

For

\[
 f_\beta(y)={y\over(y^2+\beta^2)^2},                      \tag{1.7}
\]

an elementary upper-rectangle estimate for a nonnegative unimodal function
gives

\[
 \sum_{j=0}^\infty f_\beta(j+1/4)
 \le \int_0^\infty f_\beta(y)dy+2\sup_{y\ge0}f_\beta(y).
                                                                    \tag{1.8}
\]

The two terms are explicit:

\[
 \int_0^\infty f_\beta(y)dy={1\over2\beta^2},\qquad
 \sup f_\beta={9\over16\sqrt3\,\beta^3}.                 \tag{1.9}
\]

Consequently

\[
 \mathfrak a'(\tau_0)
 \le {1\over2\beta}+{9\over8\sqrt3\,\beta^2}
 <{1\over6}+{1\over8\sqrt3}.                             \tag{1.10}
\]

On the other hand, `sin(a tau_0)=-1`, and therefore

\[
 \begin{aligned}
 b_T'(\tau_0)
 &=-\mathfrak a'(\tau_0)-2ca\sin(a\tau_0)\\
 &=-\mathfrak a'(\tau_0)+\sqrt2(\log2)^2>0.               \tag{1.11}
 \end{aligned}
\]

For a wholly rational check of the last strict sign, use
`log 2>2/3`, `sqrt 2>7/5`, and `1/sqrt 3<3/5`:

\[
 \sqrt2(\log2)^2>{28\over45},\qquad
 {1\over6}+{1\over8\sqrt3}<{29\over120},                 \tag{1.12}
\]

and `28/45>29/120`.

## 2. Scalar Stieltjes and total-variation no-go

A scalar Green/Stieltjes candidate with positive measure has the form

\[
 q(\tau)=q(0)-\int_{[0,\infty)}
                {\tau^2\over\lambda+\tau^2}\,d\mu(\lambda),
 \qquad \mu\ge0.                                          \tag{2.1}
\]

Whenever differentiation is justified, and otherwise by monotone
comparison of the integrands,

\[
 q(\tau_2)\le q(\tau_1)qquad(0\le\tau_1\le\tau_2).        \tag{2.2}
\]

Equivalently, mixtures of the corresponding exponential Green kernels
have a fixed variation orientation.  Equation (1.11) contradicts (2.2).

> **Theorem 2.1 (scalar Stieltjes no-go).**  In every first-prime window
> (1.1), the complete prime--Gamma multiplier `b_T` has no representation
> of the form (2.1) with a positive measure.  In particular it is not a
> complete-Bernstein function of `tau^2` with the sign required to force the
> Hodge inequality, and the associated translation kernel is not a positive
> total-variation mixture of scalar Green kernels.

The theorem concerns the exact multiplier, including Gamma; it is not a
local-term counterexample.  It does not rule out a *matrix-valued* or
jet-compressed Stieltjes representation.

## 3. One jet in each parity channel

Reflection splits the fixed-window Hilbert space as

\[
 H_T=H_e\oplus H_o.                                       \tag{3.1}
\]

The two primitive equations likewise split into one equation per channel,
represented by

\[
 u_e(t)=2\cosh(t/2),\qquad u_o(t)=2\sinh(t/2).             \tag{3.2}
\]

For either parity `epsilon`, normalize the corresponding jet vector `u`
and decompose

\[
 H_\epsilon=\mathbb C u\oplus u^\perp,qquad
 B_\epsilon=
 \begin{pmatrix}a&b^*\\b&D\end{pmatrix}.                 \tag{3.3}
\]

Here

\[
 D=P_{u^\perp}B_\epsilon P_{u^\perp}                     \tag{3.4}
\]

is exactly the form restricted by that parity jet.  Thus the primitive
Hodge assertion in this channel is `D<=0`.

For `z` outside the spectrum of `D`, Gaussian elimination gives the scalar
Schur function

\[
 s(z)=a-z-\langle b,(D-z)^{-1}b\rangle.                   \tag{3.5}
\]

At finite Galerkin level,

\[
 \det(B_\epsilon-z)=\det(D-z)s(z),                         \tag{3.6}
\]

and the same identity holds as a relative Fredholm formula whenever the
relative determinant is defined.

## 4. Exact Schur--Stieltjes theorem

Assume first that `D<=0`.  Let `E_D` be its spectral measure and put

\[
 d\mu(t)=d\langle b,E_D(-t)b\rangle,qquad t\ge0.          \tag{4.1}
\]

Then for `z>0`,

\[
 \boxed{
 s(z)=a-z+\int_{[0,\infty)}{d\mu(t)\over t+z}.}           \tag{4.2}
\]

In particular

\[
 s'(z)=-1-\int_{[0,\infty)}{d\mu(t)\over(t+z)^2}<0.       \tag{4.3}
\]

Conversely, suppose the measure in the actual resolvent matrix coefficient

\[
 \langle b,(D-z)^{-1}b\rangle                             \tag{4.4}
\]

is supported on `(-infinity,0]`, and suppose `b` is cyclic for `D`.  The
spectral theorem then gives `sigma(D) subset (-infinity,0]`, hence `D<=0`.
If cyclicity is absent, the same conclusion follows provided every
eigenmode of `D` orthogonal to the cyclic subspace generated by `b` is
independently proved nonpositive.

We have therefore proved:

> **Theorem 4.1 (Schur--Stieltjes equivalence).**  In each parity channel,
> the jet-compressed Hodge inequality is equivalent to a Stieltjes
> representation (4.2) whose spectral measure is supported on the
> nonnegative `t`-axis, together with exclusion of positive persistent modes.
> If the compression is strict and invertible, the sign of
> \[
> s(0)=a-\langle b,D^{-1}b\rangle                          \tag{4.5}
> \]
> supplies the remaining one-dimensional inertia exactly as in the D.56
> Feshbach certificate.

Thus the Stieltjes transform is a useful coordinate for the finite core,
but the required support of its measure is not automatic from
self-adjointness.

## 5. The persistent-mode obstruction

Cyclicity cannot be silently omitted.  Consider

\[
 B=\mathrm{diag}(2,1,-1),\qquad u=e_1.              \tag{5.1}
\]

Then relative to `C u direct-sum u^perp`, one has

\[
 a=2,\qquad b=0,qquad D=\mathrm{diag}(1,-1),
 \qquad s(z)=2-z.                                          \tag{5.2}
\]

The Schur function has the apparently acceptable representation (4.2)
with zero measure, but `D` has a positive persistent mode invisible to
`b`.  This exact example shows why a scalar characteristic or de Branges
function cannot by itself certify the primitive sign without cyclicity or a
separate persistent-spectrum bound.

For the arithmetic operator, D.50 already found the same issue: rank-one
secular equations omit eigenvectors orthogonal to the ruling vector.

## 6. de Branges interpretation and circularity boundary

At finite Galerkin level the scalar resolvent matrix coefficient is a
Nevanlinna function because `D` is self-adjoint.  Writing it as a quotient
of two real entire characteristic functions and forming the usual
combination `E=A-iB` produces a de Branges/Hermite--Biehler object after the
standard normalization.  That generic Nevanlinna property only gives
interlacing of poles and zeros on the whole real axis.

Row D needs the stronger half-line assertion:

\[
 \text{all poles belonging to }D\text{ lie in }(-\infty,0],          \tag{6.1}
\]

plus the persistent-mode condition.  By Theorem 4.1, (6.1) is precisely
the primitive Hodge sign.  Therefore any proposed de Branges proof must
derive (6.1) from a source-side property established before the explicit
formula.  Building the characteristic function from completed zeta data
and invoking its Hermite--Biehler property would be equivalent to RH;
building it from the Galerkin operator is noncircular, but merely calling
the resulting function Hermite--Biehler does not locate its poles on the
required half-line.

## 7. Surviving finite-core target

The scalar multiplier cannot be a positive Stieltjes mixture, while the
parity Schur transform is Stieltjes on the correct half-line exactly when
the desired compressed sign holds.  A noncircular continuation must
therefore prove, for every support window and uniformly under Galerkin
exhaustion,

1. cyclicity of the effective jet vector or negativity of every persistent
   mode;
2. support of the actual Schur spectral measure on `(-infinity,0]`;
3. the even/odd signs of `s_e(0)` and `s_o(0)` required by D.56.

The prime coefficients, Gamma monotonicity and reflection alone do not
prove item 2: Theorem 2.1 shows that they do not even yield a scalar
Stieltjes orientation before compression.  No global index-one law is
proved here, so row D remains open.

