# 106.105 — The canonical signed transfer and the virial gate

## 1. Purpose

The heat-localized source identity leaves open the possibility that a
globally signed current, rather than a positive path coupling, might close
the physical surplus.  This note computes the signed transfer which is
forced by the interpolation equation before trying to represent it by a
kernel.

The computation has two consequences.

1.  After the constant and the complete Riemann radical have been shorted,
    there is only one exact transfer on the source-gradient range.  Its
    singular values are the inverse square roots of the physical spectrum.
    Contractivity of that transfer is therefore exactly the missing
    threshold, with no additional freedom in a signed realization.
2.  Adding a commutator cannot hide a subthreshold eigenmode.  Its diagonal
    matrix element on that mode vanishes by the virial identity.  Hence an
    exact square-plus-commutator factorization would already prove the
    surplus; it cannot follow from source-independent heat or
    mean-periodic algebra.

All identities below are operator-theoretic consequences of the proved
full ordinary-prime--Gamma form.  No zero-location statement is used.

## 2. The two closed gradients after exact shorting

Work on

\[
 \mathscr C=(\mathbf 1\oplus\mathcal R)^\perp,
 \qquad A=L|_{\mathscr C}.
 \tag{1}
\]

The full Gamma displacement measure is positive at every displacement.
Consequently the only null vectors of the unshorted Dirichlet form are
constants.  In particular,

\[
 \ker A=\{0\}\quad\hbox{on }\mathscr C.
 \tag{2}
\]

Let

\[
 \mathcal G:\mathcal D(A^{1/2})\longrightarrow\mathscr H_{\rm src}
 \tag{3}
\]

be the complete four-channel source gradient of 106.38, with ordinary
von Mangoldt, Gamma, nondivisible-theta and central-crossing fibers.  Its
closed-form normalization is

\[
 \|\mathcal Gf\|^2=\langle A^{1/2}f,A^{1/2}f\rangle.
 \tag{4}
\]

Let

\[
 (D_\mu f)(x,y)=\frac{f(x)-f(y)}2.
 \tag{5}
\]

Every vector of \(\mathscr C\) is centered.  Therefore

\[
 \|D_\mu f\|^2=\frac12\|f\|^2,
 \qquad f\in\mathscr C.
 \tag{6}
\]

Write the polar decompositions

\[
 \mathcal G=U_AA^{1/2},
 \qquad
 D_\mu=2^{-1/2}U_D.
 \tag{7}
\]

By (2), \(U_A\) is an isometry from \(\mathscr C\) onto
\(\overline{\mathrm{ran}\,\mathcal G}\); by (6), \(U_D\) is an
isometry from \(\mathscr C\) onto
\(\overline{\mathrm{ran}\,D_\mu}\).

## 3. Exact formula for the canonical signed transfer

On \(\mathrm{ran}\,\mathcal G\), the coefficient equation fixes a
linear map by

\[
 C_0\mathcal Gf=D_\mu f.
 \tag{8}
\]

It is well defined by (2).  The following formula shows that no choice of
signed paths or currents changes this map.

### Theorem 1 — Unique transfer and exact gain

The operator in (8) is the closed densely defined operator

\[
 \boxed{
 C_0=2^{-1/2}U_DA^{-1/2}U_A^*}
 \tag{9}
\]

on \(\overline{\mathrm{ran}\,\mathcal G}\), with its natural
domain.  If

\[
 \alpha=\inf\sigma(A),
 \tag{10}
\]

then

\[
 \boxed{
 \|C_0\|=(2\alpha)^{-1/2}}
 \tag{11}
\]

with the value \(+\infty\) when \(\alpha=0\).  In particular,

\[
 \boxed{
 C_0\text{ is a contraction}
 \quad\Longleftrightarrow\quad
 A\ge\frac12I.}
 \tag{12}
\]

#### Proof

For \(f\in\mathcal D(A^{1/2})\), equations (7) and (9) give

\[
 C_0\mathcal Gf
 =2^{-1/2}U_DA^{-1/2}U_A^*U_AA^{1/2}f
 =2^{-1/2}U_Df
 =D_\mu f.
 \tag{13}
\]

Thus (9) agrees with (8) on its defining range.  Conversely, (8) fixes
every value on that range, so its closure is unique.  Since \(U_A,U_D\)
are isometries, spectral calculus gives

\[
 \|C_0\|^2
 =\frac12\|A^{-1}\|
 =\frac1{2\alpha}.
 \tag{14}
\]

Equation (12) follows.  \(\square\)

The exact defect operator on the source-gradient space is consequently

\[
 \boxed{
 I-C_0^*C_0
 =U_AA^{-1/2}\left(A-\frac12I\right)A^{-1/2}U_A^*.}
 \tag{15}
\]

Thus a signed kernel representation of \(C_0\) can clarify the arithmetic
content of the inverse square root, but it cannot improve its norm.  The
norm is already fixed by the bottom of the physical spectrum.

### Corollary 2 — Subthreshold amplification

If \(Aq=\alpha q\), \(\|q\|=1\), and \(0<\alpha<1/2\), then every exact
signed realization of (8) satisfies

\[
 \boxed{
 \frac{\|C_0\mathcal Gq\|}{\|\mathcal Gq\|}
 =\frac1{\sqrt{2\alpha}}>1.}
 \tag{16}
\]

Indeed, the numerator is \(\|D_\mu q\|=2^{-1/2}\), whereas the
denominator is \(\sqrt\alpha\).  This is the sharp stress test for a
proposed globally signed current: cancellation among its coefficients
cannot reduce (16), because the exact interpolation equation fixes the
output.

### Heat-resolvent realization

For every \(\varepsilon>0\), the inverse square root has the norm-convergent
Laplace representation

\[
 (A+\varepsilon I)^{-1/2}
 =\frac1{\sqrt\pi}\int_0^\infty
 t^{-1/2}e^{-t(A+\varepsilon I)}\,dt.
 \tag{16a}
\]

Hence the regularized exact transfer is

\[
 \boxed{
 C_\varepsilon
 =\frac1{\sqrt{2\pi}}U_D
 \int_0^\infty t^{-1/2}e^{-t(A+\varepsilon I)}\,dt\,U_A^*,}
 \qquad
 \|C_\varepsilon\|=\frac1{\sqrt{2(\alpha+\varepsilon)}}.
 \tag{16b}
\]

The strong graph limit as \(\varepsilon\downarrow0\) is \(C_0\).  Formula
(16b) is an explicit globally signed heat realization once the two polar
isometries are expanded in the source and target edge coordinates.  It
also shows that a triangle estimate on the heat integral cannot prove the
target: its exact norm already tends to \((2\alpha)^{-1/2}\).  Any gain
must therefore come from proving, with the literal source, that
\(\alpha\ge1/2\), rather than from cancellation between alternative
representations of the same inverse square root.

## 4. Radical saturation before shorting

Before passing to (1), the complete radical is the \(1/2\)-eigenspace of
the unshorted generator.  Formula (11), restricted to that eigenspace,
has gain one.  Hence (9) recovers the radical-isometry theorem of 106.39
without an auxiliary path argument.

Moreover, after splitting the source-gradient closure into the radical
block and its orthogonal complement, formula (15) shows that shorting
subtracts the same exact isometric square from both sides.  The
complementary transfer has norm

\[
 \left(2\inf\sigma(A|_{\mathscr C})\right)^{-1/2},
 \tag{17}
\]

so radical anti-shorting localizes the unknown channel but creates no
spectral slack.

## 5. Why a harmless commutator cannot supply the missing sign

A natural signed-current ansatz is a factorization

\[
 A-\frac12I=B^*B+i[A,X]+R,
 \qquad R\ge0,
 \tag{18}
\]

where \(X=X^*\) is a current or position observable and the commutator is
expected to disappear after integration or trace.  The next statement is
the exact falsifier for that ansatz.

### Theorem 3 — Virial obstruction on a bound state

Let \(q\) be a normalized eigenvector of \(A\), \(Aq=\alpha q\), in a
common domain on which the quadratic-form commutator in (18) is defined.
Then

\[
 \langle q,i[A,X]q\rangle=0.
 \tag{19}
\]

Consequently, an identity of the form (18) implies

\[
 \alpha-\frac12=\|Bq\|^2+\langle q,Rq\rangle\ge0.
 \tag{20}
\]

In particular, no square-plus-harmless-commutator identity valid in a
subthreshold heat/mean-periodic model can prove the physical surplus.

#### Proof

On the stated common domain,

\[
 \begin{aligned}
 \langle q,i[A,X]q\rangle
 &=i\{\langle Aq,Xq\rangle-\langle Xq,Aq\rangle\}\
 &=i\alpha\{\langle q,Xq\rangle-\langle Xq,q\rangle\}=0,
 \end{aligned}
 \tag{21}
\]

because \(X\) is symmetric.  Taking the \(q\)-matrix element of (18)
gives (20).  The standard bounded-commutator regularization gives the same
conclusion when (19) is initially available only as a form identity.
\(\square\)

The full marked-current formulas of 106.51--106.53 are therefore useful
only if their boundary or rate-variation term is retained as a genuinely
signed arithmetic term.  If it is converted into a vanishing commutator
plus nonnegative squares, (20) shows that the conversion itself is already
a proof that no subthreshold eigenstate exists.

## 6. Heat-row form of the same obstruction

For the faithful heat state of 106.103,

\[
 \Gamma_t=e^{-t(A+1/2)/2}Ve^{-t(A+1/2)/2},
 \tag{22}
\]

the literal source identity is

\[
 \mathrm{Tr}\,\{(A-\tfrac12I)\Gamma_t\}
 =\int_0^\infty\mathcal J_u[\Gamma_t],d\sigma(u).
 \tag{23}
\]

If \(\alpha<1/2\), heat concentration and injectivity of \(V\) give

\[
 \frac{\mathrm{Tr}\,\{(A-\tfrac12I)\Gamma_t\}}
      {\mathrm{Tr}\,\Gamma_t}
 \longrightarrow\alpha-\frac12<0.
 \tag{24}
\]

Suppose a current decomposition of the numerator has the form

\[
 \mathrm{Tr}\,\{(A-\tfrac12I)\Gamma_t\}
 =\|B\Gamma_t^{1/2}\|_{\mathfrak S_2}^2
  +\mathrm{Tr}\,\{i[A,X]\Gamma_t\}
  +\mathrm{Tr}(R\Gamma_t),
 \tag{25}
\]

with \(R\ge0\).  The heat state concentrates on the ground eigenspace,
and the normalized commutator term tends to zero by (19), provided the
commutator is uniformly form-integrable along the heat row.  The other
two normalized terms are nonnegative.  This contradicts (24).

Thus a successful heat/hybrid proof cannot discard the signed current as
a harmless commutator.  It must prove, from the literal placements
\(\log p^k\) together with Gamma and the pole, that the subthreshold
spectral mass in (24) is absent.  Equivalently, it must bound the concrete
inverse-square-root transfer (9), not an algebraically freer surrogate.

## 7. Exact remaining target

The globally signed-current route has now been reduced to one operator
estimate with no representation ambiguity:

\[
 \boxed{
 \left\|2^{-1/2}U_DA^{-1/2}U_A^*\right\|\le1.}
 \tag{26}
\]

In the literal source coordinate this is the cofinal estimate of 106.102,

\[
 \int_0^\infty\mathcal J_u[\Gamma_{t_k}]\,d\sigma(u)
 \ge-o(\mathrm{Tr}\,\Gamma_{t_k}),
 \tag{27}
\]

for an unbounded sequence \(t_k\).  A new arithmetic argument may still
prove (26) by constructing and estimating the kernel of \(A^{-1/2}\).
What (9)--(25) rule out is a proof obtained by changing the exact transfer,
or by placing the entire signed defect into a commutator which vanishes on
the state that must be excluded.

## 8. Status

Proved here:

* the unique exact signed transfer (9);
* its exact norm and defect formulas (11), (15);
* the subthreshold amplification factor (16);
* the radical saturation interpretation;
* the virial obstruction for square-plus-commutator closures;
* the heat-row version of that obstruction.

Not proved here:

\[
 \|C_0\|\le1.
\]

By (12), this is exactly the physical surplus.  The remaining proof must
use a source-specific estimate for the literal ordinary-prime--Gamma
inverse square root; it cannot arise from an alternative exact signed
transfer or a harmless commutator.
