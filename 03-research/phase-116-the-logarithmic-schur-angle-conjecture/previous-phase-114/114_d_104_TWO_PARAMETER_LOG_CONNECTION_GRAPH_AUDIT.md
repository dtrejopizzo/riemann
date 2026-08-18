# D.104 — Two-parameter logarithmic graph connection audit

## Status

The Euler--Gamma determinant gives a positive fibre metric whose normal
connection has first variation exactly equal to the completed contact.
This note tests whether placing that metric in a positive two-parameter
graph, adding the two Tate boundary legs and taking a Schur complement
creates an independent convexity proof of the sign.

It does not.  Three exact alternatives exhaust the natural construction:

1. the unregularized Euler determinant has the exact first variation, but
   its logarithmic curvature changes sign already on one prime Bloch
   circle;
2. a positive coercive graph regularization changes the first variation by
   a frequency-dependent attenuation and loses the `p^k` coefficients;
3. the reflection-symmetric doubled graph has a positive Schur complement,
   but it is even in the normal parameter and its first variation vanishes.

Positivity of a family of metrics never controls the sign of its connection
one-form.  Loewner monotonicity of the Schur complement would control it,
but that monotonicity pulls back exactly to row D.  Joint convexity controls
a second variation, not the oriented first variation `B_nuc`.

The Gamma determinant behaves in the same way: its first normal derivative
is exact, while a reflected double cancels it and a coercive
regularization changes its finite-part connection.

No RH statement or desired sign is assumed.  The paper is not modified.

## 1. Exact local determinant connection

Fix a prime, put `L=log p`, `r=p^(-sigma)` and let `u=e^(i theta)` be a
Bloch character.  The positive determinant metric is

\[
 g_p(\sigma,\theta)=|1-ru|^2
 =1-2r\cos\theta+r^2.                                    \tag{1.1}
\]

Its logarithmic normal connection is

\[
 \begin{aligned}
 c_p(\sigma,\theta)
 &=\partial_\sigma\log g_p(\sigma,\theta)\\
 &=L\bigl(P_r(e^{i\theta})-1\bigr)
 =2L\sum_{k\ge1}r^k\cos(k\theta).                        \tag{1.2}
\end{aligned}
\]

At `sigma=1/2`, (1.2) is exactly every
`Lambda(p^k)/sqrt(p^k)` contribution.  This is the D.94 normal connection.

However its curvature in the normal direction is not sign-definite.  At
the two boundary characters,

\[
 \partial_\sigma c_p(\sigma,0)
 =-{2L^2r\over(1-r)^2}<0,                                \tag{1.3}
\]

whereas

\[
 \partial_\sigma c_p(\sigma,\pi)
 ={2L^2r\over(1+r)^2}>0.                                 \tag{1.4}
\]

Thus neither `log g_p` nor `-log g_p` is convex on all Bloch fibres.

## 2. Coercive graph regularization loses exact contact

To make the graph uniformly positive one may replace (1.1) by

\[
 g_{p,\epsilon}=g_p+\epsilon,
 \qquad\epsilon>0.                                       \tag{2.1}
\]

Its connection is

\[
 \partial_\sigma\log g_{p,\epsilon}
 ={g_p\over g_p+\epsilon}\,c_p.                          \tag{2.2}
\]

The attenuation factor depends on `theta`.  Consequently its Fourier
series is not the Poisson series in (1.2): it mixes all powers and changes
the coefficient of every `p^k`.

The operator version is the same.  If

\[
 D_p(\sigma)=I-p^{-\sigma}U_p,
 \quad G_{p,\epsilon}=D_p^*D_p+\epsilon I,                \tag{2.3}
\]

then

\[
 \nabla_\sigma^{\epsilon}
 =G_{p,\epsilon}^{-1}\partial_\sigma G_{p,\epsilon}       \tag{2.4}
\]

is not the logarithmic derivative of `D_p^*D_p`; its Bloch multiplier is
(2.2).  Taking `epsilon->0` restores exact contact but loses the uniform
closed-range/coercivity which the Hodge graph was meant to supply.

## 3. Reflection double and Schur complement

Let

\[
 g_+(a)=g_p(1/2+a,\theta),
 \qquad g_-(a)=g_p(1/2-a,\theta).                         \tag{3.1}
\]

The positive reflected double is

\[
 g_+(a)|x|^2+g_-(a)|y|^2.                                \tag{3.2}
\]

In diagonal/anti-diagonal boundary coordinates its block matrix has
diagonal entry `(g_++g_-)/2` and off-diagonal entry `(g_+-g_-)/2`.
Eliminating one boundary leg gives the positive Schur complement

\[
 S_p(a)={2g_+(a)g_-(a)\over g_+(a)+g_-(a)}>0.             \tag{3.3}
\]

It is even:

\[
 S_p(-a)=S_p(a),
 \qquad S_p'(0)=0.                                       \tag{3.4}
\]

Therefore the reflection-positive graph cancels the oriented connection
`c_p`; it cannot have first variation (1.2).  Keeping one oriented leg
retains (1.2), but then the reflected positive Schur argument is absent.

Adding a fixed positive Tate boundary block does not change (3.4).  Adding
the crossed Tate metric `C` creates a nonzero oriented first variation, but
the boundary metric has inertia `(1,1)` and returns to the Krein system of
D.95--D.101.

## 4. General positive-family obstruction

Let `S(a)>0` be any differentiable family of Hilbert metrics.  At `a=0`
its connection is

\[
 A=S(0)^{-1/2}S'(0)S(0)^{-1/2}.                           \tag{4.1}
\]

There is no sign restriction on `A`: for every bounded self-adjoint
operator `A`,

\[
 S(a)=e^{aA}>0                                            \tag{4.2}
\]

has `S(0)=I` and `S'(0)=A`.  Positivity of a metric family is therefore
logically insufficient to sign its normal connection.

If one proves the Loewner monotonicity

\[
 S'(0)\ge0\quad\text{or}\quad S'(0)\le0,                 \tag{4.3}
\]

then (4.1) has the corresponding sign.  For a source map `J` whose
connection pullback is exact,

\[
 J^*S'(0)J=B_{\rm nuc}                                   \tag{4.4}
\]

up to the fixed convention.  Thus the needed direction of (4.3) on the
primitive source is row D itself.

Joint geodesic convexity of `log S(a)` controls
`partial_a^2 log S`; it gives monotonicity of the connection only after a
one-sided boundary value is known.  Functional-equation reflection gives
an even value and zero derivative for the completed regular determinant,
not the sign of the arithmetic boundary distribution.

## 5. Gamma determinant

The positive archimedean determinant metric is

\[
 g_\infty(s)=|\pi^{-s/2}\Gamma(s/2)|^2.                   \tag{5.1}
\]

Its exact normal connection is

\[
 \partial_\sigma\log g_\infty(s)
 =-\log\pi+\operatorname{Re}\psi(s/2).                   \tag{5.2}
\]

With the orientation used for the completed contact, its negative is

\[
 m_\infty(\tau)
 =\log\pi-\operatorname{Re}\psi(1/4+i\tau/2)
 =m_0-\ell_\infty(\tau).                                 \tag{5.3}
\]

Thus the unregularized determinant gives the entire Gamma block and its
finite-part mass.  A reflected product
`g_infinity(1/2+a+i tau)g_infinity(1/2-a+i tau)` is even in `a`, so its
first derivative vanishes.  Adding `epsilon` to the oscillator Gram
changes (5.2) by the analogue of (2.2), including the finite-part constant.

Consequently the prime and Gamma components respond identically to the
three choices: exact oriented connection, coercive but inexact
regularization, or positive reflected cancellation.

## 6. Two-parameter mixed variation

One can retain two independent parameters and consider

\[
 \mathcal G(a,b)=g_p(1/2+a,\theta)\,
                  g_p(1/2-b,\theta).                     \tag{6.1}
\]

Since `log G` is a sum of a function of `a` and a function of `b`,

\[
 \partial_a\partial_b\log\mathcal G=0.                   \tag{6.2}
\]

Replacing the product by a positive sum produces a nonzero mixed Hessian,
but it is a covariance term depending quadratically on the two local
connections.  It does not equal the linear contact (1.2).  This is the
same typing obstruction found for the softmax/Ronkin Hessian in D.93.

The formal mixed derivative of the Kunneth unit expansion does equal
`B_nuc` (D.92), but no positive determinant potential constructed here has
that expansion as its Hessian.

## 7. Outcome and Bochner boundary gate

The logarithmic graph route proves the exact first-variation comparison
but supplies no independent sign.  Its failure is not caused by a missing
normalization: it is the distinction between a connection and curvature.

A remaining geometric mechanism would be a Bochner identity

\[
 \|\mathcal Df\|^2
 =\|\nabla f\|^2+\langle\mathcal Rf,f\rangle
  +\mathcal B_{\partial}(f,f),                             \tag{7.1}
\]

where the bulk terms on the right are independently nonnegative, the two
Tate moments are the elliptic boundary data, and

\[
 \mathcal B_{\partial}(f,f)=-B_{\rm nuc}(f,f)              \tag{7.2}
\]

is derived by the determinant connection.  D.94--D.95 show that the naive
curvature is flat off the completed divisor and has divisor sources on it.
The next audit must determine whether a source-defined superconnection on
the Euler--Gamma complex has a positive Weitzenbock curvature before
spectral localization, or whether its curvature term is exactly the Real
divisor current and hence again equivalent to RH.

