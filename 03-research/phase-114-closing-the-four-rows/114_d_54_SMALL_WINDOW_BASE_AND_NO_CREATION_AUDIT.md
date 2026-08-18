# D.54 — An unconditional small-window base and audit of no-mode creation

## 1. Purpose

D.53 reduced the continuous route to an oscillation statement for the
explicit kernel `K_g`, but showed that activating prime-power shifts does
not give a monotone spectral flow.  This note establishes a genuine
unconditional base interval.  On sufficiently small windows the complete
continuous Weil kernel is positive on the entire zero-mass space, before
the two Tate moment constraints are imposed.

The threshold is explicit.  The attempted propagation by ordinary total
positivity or variation diminution is then audited.  That propagation does
not follow: the Gamma density has the wrong `TP_2` sign and the
prime-power crossing forms are indefinite.  No assertion that `g` is a
screw function is used; globally that assertion would be equivalent to RH.

## 2. Exact Gamma tail bound

On `I_T=[-T,T]`, before the first prime-power displacement enters, D.52
gives

\[
 B_T=\Gamma_T=m_0I-L_{\infty,T},
 \qquad m_0=\log\pi-\psi(1/4),                              \tag{2.1}
\]

with

\[
 \langle F,L_{\infty,T}F\rangle
 =\int_0^\infty w(r)\|F-S_rF\|_2^2dr,
 \qquad w(r)={e^{-r/2}\over1-e^{-2r}}.                     \tag{2.2}
\]

If `r>=2T`, the supports of `F` and `S_rF` are disjoint up to a null
boundary, hence

\[
 \|F-S_rF\|_2^2=2\|F\|_2^2.                               \tag{2.3}
\]

It follows that

\[
 \Gamma_T(F,F)
 \leq \bigl(m_0-2I(2T)\bigr)\|F\|_2^2,
 \qquad I(R)=\int_R^\infty w(r)dr.                         \tag{2.4}
\]

The tail is elementary.  With `x=e^(-R/2)`,

\[
 I(R)=2\int_0^x{dy\over1-y^4}
 ={1\over2}\log{1+x\over1-x}+\arctan x.                  \tag{2.5}
\]

In particular,

\[
 2I(2T)=\log\coth(T/2)+2\arctan(e^{-T}).                  \tag{2.6}
\]

This estimate uses only the positive Gamma measure.  It does not use a
spectral zero or a positivity property of `g`.

## 3. Control of the polar rank-two block

The exact comparison is

\[
 QW_T(F,F)=\langle M_TF,CM_TF\rangle-B_T(F,F),
 \qquad C=\begin{pmatrix}0&1\\1&0\end{pmatrix}.            \tag{3.1}
\]

Writing `M_TF=(M_-(F),M_+(F))`, Cauchy--Schwarz gives

\[
 \begin{aligned}
 \langle M_TF,CM_TF\rangle
 &=2\mathrm{Re}(M_-(F)\overline{M_+(F)})\\
 &\geq-|M_-(F)|^2-|M_+(F)|^2\\
 &\geq-4\sinh(T)\|F\|_2^2,                               \tag{3.2}
 \end{aligned}
\]

because

\[
 \|e^{t/2}\|_{L^2(I_T)}^2
 =\|e^{-t/2}\|_{L^2(I_T)}^2=2\sinh T.                    \tag{3.3}
\]

Combining (2.4) and (3.2), as long as `2T<log 2` so that no finite-place
hinge is present, yields

\[
 QW_T(F,F)\geq \delta(T)\|F\|_2^2,                        \tag{3.4}
\]

where

\[
 \delta(T)=\log\coth(T/2)+2\arctan(e^{-T})
             -m_0-4\sinh T.                               \tag{3.5}
\]

## 4. The explicit base threshold

The function `delta` is strictly decreasing, since

\[
 \delta'(T)=-{1\over\sinh T}-{1\over\cosh T}-4\cosh T<0. \tag{4.1}
\]

Moreover `delta(T)->+infinity` as `T downarrow 0`, while it is negative
before `T=log(2)/2`.  Therefore there is a unique number

\[
 \boxed{
 T_0:\quad
 \log\coth(T_0/2)+2\arctan(e^{-T_0})
 =\log\pi-\psi(1/4)+4\sinh T_0}                           \tag{4.2}
\]

and numerically

\[
 T_0=0.0371152624450827647\ldots< {\log2\over2}.           \tag{4.3}
\]

### Theorem 4.1 (unconditional base interval)

For every `0<T<T_0`,

\[
 QW_T(F,F)\geq\delta(T)\|F\|_2^2>0                       \tag{4.4}
\]

for every nonzero `F` in the compact-core form domain.  Equivalently, under
the derivative identification of D.52,

\[
 \langle K_{g,T}u,u\rangle>0
 \qquad(0\neq u\in H_T^0).                                \tag{4.5}
\]

Thus the D.53 oscillation index satisfies

\[
 r_T=n_-(K_{g,T}|_{H_T^0})=0,
 \qquad 0<T<T_0.                                           \tag{4.6}
\]

In particular the row-D primitive inequality holds on these windows, even
without imposing the two additional exponential moments.  This is a local
support statement, not the global completion of row D.

### Proof

Equations (2.4), (3.2) and the absence of prime powers imply (4.4).
Differentiation identifies compactly supported `F` with zero-mass `u=F'`;
density passes the nonnegative form to the closure.  The strict lower bound
on `F` rules out a nonzero zero mode.  This proves (4.5)--(4.6).

The theorem proves only local-in-support positivity from the displayed
estimates.  It does not call `g` a screw function.

## 5. Prime-free archimedean base and the stronger Sonin subclass

The elementary estimate above is deliberately internal to the explicit
Gamma--polar formula, but it is not the largest known unconditional base.
The archimedean Weil positivity recalled and analyzed by Connes--Consani,
*Weil positivity and Trace formula, the archimedean place*,
arXiv:2006.13771, applies to positive-type multiplicative tests supported in

\[
 [2^{-1/2},2^{1/2}]                                       \tag{5.1}
\]

and satisfying the Tate primitive conditions at the two polar characters.
It gives

\[
 W_\infty(g*g^*)\geq0.                                   \tag{5.2}
\]

Their stronger Sonin trace inequality (Theorem 1, refined by Theorem 6.11)
assumes, in addition to the polar vanishing, an extra zero at the central
Fourier value.  On that smaller, extra-central subclass it gives

\[
 W_\infty(g*g^*)
 \geq \mathrm{Tr}
 \bigl(\vartheta(g)\mathfrak S\vartheta(g)^*\bigr)\geq0,  \tag{5.3}
\]

where `mathfrak S` is the orthogonal projection onto Sonin's space.  The
second inequality is by construction:

\[
 \mathrm{Tr}
 \bigl(\vartheta(g)\mathfrak S\vartheta(g)^*\bigr)
 =\|\vartheta(g)\mathfrak S\|_{HS}^2.                     \tag{5.4}
\]

Under the Mellin/logarithmic dictionary fixed in D.32 and D.52, the polar
vanishing conditions are precisely the two Tate primitive conditions.
The extra central zero in the Sonin trace theorem is a third condition; it
must not be identified with the second Tate ruling.  The support (5.1) is
`[-T,T]` with

\[
 T\leq T_{\rm pf}:={\log2\over2}.                          \tag{5.5}
\]

On such a window the convolution square is supported in `[1/2,2]`.  No
prime-power term contributes in its interior; at the endpoint `2` a smooth
compactly supported test vanishes to all orders.  Hence the complete
quadratic form equals its archimedean part:

\[
 QW_T(g,g)=W_\infty(g*g^*).                                \tag{5.6}
\]

It follows that

\[
 \boxed{QW_T\geq0\text{ on the primitive space for every }
        0<T\leq {\log2\over2}.}                            \tag{5.7}
\]

This enlarges the elementary interval `(0,T_0)` by almost an order of
magnitude.  The elementary theorem remains useful because it proves
positivity on the entire zero-mass space and gives the explicit coercive
constant `delta(T)`; archimedean Weil positivity supplies the complete
prime-free primitive window.

### Strictness audit on the extra-central subclass

The cited theorem states nonnegativity, but (5.3) also gives strictness for
a nonzero test.  If its trace is zero, then

\[
 \vartheta(g)\mathfrak S=0.                               \tag{5.8}
\]

Choose a nonzero vector `xi` in Sonin's space.  In the Mellin spectral
representation the scaling convolution `vartheta(g)` is multiplication by
the entire Mellin transform `hat g`.  The transform of `xi` is nonzero on a
set of positive measure.  Equation (5.8) therefore forces `hat g` to vanish
on a set with an accumulation point.  Entire analyticity gives
`hat g identically 0`, hence `g=0`.  Consequently, for nonzero tests in
the extra-central subclass,

\[
 QW_T(g,g)>0,
 \qquad 0<T\leq {\log2\over2}.                             \tag{5.9}
\]

This strictness argument uses only the positive Sonin projection and the
Paley--Wiener analyticity of a compactly supported multiplicative test.  It
does not use any zeta zero.  It does **not** prove strictness on the full
two-condition primitive space; there the certified conclusion is (5.7).

## 6. First-exit formulation

Transport `L^2([-T,T])` unitarily to `L^2([-1,1])`.  Ignoring the harmless
positive scalar arising from the Jacobian, the transported centered kernel
is

\[
 \widetilde K_T(x,y)=K_g(Tx,Ty).                            \tag{6.1}
\]

On the zero-mass space the separated centering terms vanish.  At regular
values of `T`, the derivative quadratic form is consequently represented
by

\[
 \dot k_T(x,y)=(x-y)g'(T(x-y)).                            \tag{6.2}
\]

If a negative mode were first created at `T_*`, a normalized null vector
`u_*` would have crossing form

\[
 \dot\lambda(T_*)=
 \int_{-1}^1\!\int_{-1}^1
 (x-y)g'(T_*(x-y))u_*(y)\overline{u_*(x)}\,dy\,dx,         \tag{6.3}
\]

 plus the standard constraint-transport correction if one works directly
on the moving two-moment kernel.  A no-creation theorem must prove the
appropriate sign of (6.3) on every nullspace.  Continuity and compactness
alone do not provide it.

For a prime-power hinge `g_a(t)=c_a(|t|-a)_+`, (5.2) contains

\[
 c_a|x-y|\,\mathbf1_{\{T|x-y|>a\}},                        \tag{6.4}
\]

and D.53 gives smooth test vectors with both signs for the equivalent
translated-correlation form.  Thus the source terms are not ordered in the
operator cone required by a standard no-creation argument.

At each finite Galerkin level `N`, the relevant first-exit point can now be
taken after the full prime-free interval:

\[
 T_{*,N}:=\inf\left\{T>{\log2\over2}:
 QW_{T,N}\text{ has a nonpositive primitive direction}\right\}. \tag{6.5}
\]

If this set is nonempty, finite-dimensional continuity together with the
nonnegativity (5.7) forces a primitive zero mode at `T_(\*,N)` (after the
standard form-domain transport).  A propagation theorem must show that its
crossing form cannot enter the negative cone, uniformly in `N`.

There is an essential infinite-dimensional caveat.  The continuous-kernel
operator is compact, so zero belongs to its spectral accumulation even when
the form is pointwise strictly positive.  Even the subclass strictness in
(5.9) does **not** supply a uniform `L^2` spectral gap on the full primitive
space.  Negative eigenvalues could in principle be born
from the zero accumulation while `T_(\*,N)` drifts with `N`, without a
nonzero kernel vector at a limiting `T_*`.  Therefore a valid no-creation
theorem must include a uniform Galerkin/compactness estimate; tracking only
each fixed eigenvalue branch is insufficient.

## 7. Ordinary variation diminution does not propagate the base

One possible propagation mechanism would factor the evolution into
`TP_2`, variation-diminishing local kernels.  The exact Gamma density in
(2.2) already has the opposite local curvature:

\[
 {d^2\over dr^2}\log w(r)
 ={4e^{-2r}\over(1-e^{-2r})^2}>0.                          \tag{7.1}
\]

Equivalently, for `r>h>0`,

\[
 w(r)^2-w(r-h)w(r+h)<0,                                   \tag{7.2}
\]

whereas a translation kernel of order `TP_2` requires the reverse sign.
Indeed, after putting `q=e^{-2r}` the product denominator is

\[
 1-2q\cosh(2h)+q^2<(1-q)^2,                               \tag{7.3}
\]

which proves (7.2) exactly.

At the finite places, the unsigned crossing calculation of D.53 supplies a
second independent obstruction: even a positive hinge coefficient admits
both crossing orientations.  Hence neither the Gamma factors nor the
prime-power factors satisfy the hypotheses of the ordinary
variation-diminishing composition theorem that would preserve (4.6).

This does not prove that the complete arithmetic kernel lacks some new,
global oscillation property produced by cancellation among its terms.  It
proves that such a property cannot be obtained by multiplying the standard
local `TP_2` certificates or by operator-monotone threshold activation.

## 8. What remains after the base theorem

The unconditional conclusion is now anchored on the complete prime-free
interval:

\[
 QW_T\geq0\text{ on primitive tests},
 \qquad 0<T\leq {\log2\over2}.                             \tag{8.1}
\]

To continue it to all windows one needs one of the following genuinely new
source-side statements:

1. the null-crossing inequality `dot lambda>=0` at every first exit from
   the nonnegative cone, including moving-constraint terms;
2. the D.53 bound `r_T<=2` and equality
   `n_-(mathcal G_T)=r_T` through every singular window;
3. a nonstandard global sign-regularity theorem for the full Gamma--Lerch
   plus prime-power kernel, whose hypotheses can be verified despite
   (7.2) and the indefinite hinge crossings.

Invoking that `g` is a screw function would assert that `r_T=0` for every
`T`, which is Weil positivity and therefore RH.  It cannot serve as the
propagation theorem.

## 9. Verdict

There are now two certified starting statements.  The elementary
Gamma-tail estimate proves that the complete centered kernel has no
negative modes on the whole zero-mass space for
`T<T_0=0.0371152624...`.  Archimedean Weil positivity proves the
nonnegative primitive inequality throughout the optimal prime-free window
`T<=(log2)/2`; the stronger Sonin trace gives strictness only after imposing
its additional central-zero condition.

Ordinary variation diminution cannot propagate this result: its `TP_2`
hypothesis fails exactly for the Gamma density, and prime-power hinges have
unsigned crossing forms.  The remaining step is therefore a new global
oscillation or first-exit theorem, not an application of the classical
variation-diminishing machinery.
