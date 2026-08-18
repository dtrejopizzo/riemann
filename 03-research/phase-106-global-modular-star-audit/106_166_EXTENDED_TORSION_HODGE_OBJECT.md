# 106.166 — The extended torsion Hodge object and its exact support

## 1. Purpose

The reduced Plancherel quotient of the adelic summation map is zero, while
the CCM Schwartz/Meyer cokernel retains distributional resonances.  There
is one standard categorical repair of this mismatch which had not yet
been tested in this phase: retain a dense, nonclosed range as a *torsion
object* rather than replacing it by its closure.

This note constructs that object on the critical Mellin line and gives it
a canonical positive Hodge form.  The construction succeeds as a
torsion-sensitive polarization and is compatible with normalized scaling.
It also has an exact support theorem: it detects only zeros lying on the
critical line.  Hence the comparison from the full analytic CCM cokernel
to this positive object is faithful exactly when there are no off-line
resonances.  The construction therefore supplies the correct positive
target, but not the missing faithful descent.

No zero list and no assumption on zero location is used.

## 2. A concrete extended category

For the present calculation it is enough to use the following elementary
model.  An extended Hilbert object is a closed densely defined operator

\[
 T:\mathcal D(T)\subset H_0\longrightarrow H_1.              \tag{1}
\]

It is called torsion when \(T\) is injective and has dense, nonclosed
range.  Its reduced Hilbert cokernel is zero, but the pair

\[
 \mathbb T_T=(\mathcal D(T)\mathop{\longrightarrow}^{T}H_1)  \tag{2}
\]

is not discarded.  A unitary equivalence of such objects is a pair of
unitaries intertwining the operators and their graph domains.  This is the
two-term part of the usual abelian envelope of Hilbert spaces; no general
categorical result will be needed below.

Let \(T=U|T|\) be the polar decomposition.  On the form domain
\(\mathcal D(|T|^{1/2})\), define

\[
 q_T(f,g)=\langle |T|^{1/2}f,|T|^{1/2}g\rangle.              \tag{3}
\]

It is a closed positive form.  If \(T\) is injective, (3) is definite on
its form domain.  Thus a dense range is not, by itself, an obstruction to
a positive extended Hodge form.

## 3. The critical-line multiplier

Put

\[
 \Xi(z)=2\xi\!\left(\frac12+z\right),
 \qquad m(\gamma)=\Xi(i\gamma),\qquad \gamma\in\mathbb R.    \tag{4}
\]

The functional equation and real structure give

\[
 m(\gamma)\in\mathbb R,qquad m(-\gamma)=m(\gamma).          \tag{5}
\]

On \(H=L^2(\mathbb R,d\gamma)\), let \(M_m\) be the maximal
multiplication operator.  Since \(m\) is a nonzero real-analytic
function, its real zero set is discrete and hence null.  Therefore
\(M_m\) is injective and has dense range.  Its range is nonclosed: in
particular \(m(\gamma)\) tends to zero along the real line because of the
archimedean factor, and every real zero gives an additional finite
singularity.

### Theorem 3.1 — Canonical positive torsion polarization

The extended object

\[
 \mathbb T_\Xi=
 \bigl(\mathcal D(M_m)\mathop{\longrightarrow}^{M_m}H\bigr) \tag{6}
\]

has the canonical positive form

\[
 \boxed{
 q_\Xi(f,g)=
 \int_{\mathbb R}|m(\gamma)|
 f(\gamma)\overline{g(\gamma)}\,d\gamma.}                   \tag{7}
\]

For

\[
 (U_tf)(\gamma)=e^{it\gamma}f(\gamma),                      \tag{8}
\]

one has

\[
 \boxed{q_\Xi(U_tf,U_tg)=q_\Xi(f,g),
 \qquad U_tM_m=M_mU_t.}                                     \tag{9}
\]

After the degree-one Tate twist
\(\vartheta_t=e^{t/2}U_t\), the form has weight one.

#### Proof

The polar decomposition of the real multiplication operator is

\[
 M_m=M_{\operatorname {sgn}m}M_{|m|}.
\]

Equation (7) is exactly (3).  It is positive, closed, and definite because
\(|m|>0\) almost everywhere.  Both \(M_m\) and \(M_{|m|}\) commute with
the phase multiplier (8), proving (9).  Multiplication of both arguments
by \(e^{t/2}\) multiplies (7) by \(e^t\). \(\square\)

Taking the real double and the standard operator
\(J(f,g)=(-g,f)\) turns (7) into a positive alternating polarization in
the same way as in 106.164.  Thus positivity, the complex structure, and
the weight-one law coexist on a torsion-sensitive object.

## 4. What this object remembers

Let \(D\Subset\mathbb C\) be a symmetric finite window as in 106.163 and

\[
 \mathcal H_D=\mathcal O(\overline D)/\Xi\mathcal O(\overline D). \tag{10}
\]

The finite support of (10) is the complete zero divisor of \(\Xi\) in
\(D\).  The finite characteristic support of the multiplier object (6),
by contrast, is its real zero set

\[
 Z_{\mathbb R}(\Xi)=\{\gamma\in\mathbb R:m(\gamma)=0\}.      \tag{11}
\]

This distinction is categorical, not numerical.

### Theorem 4.1 — Exact support of the positive extended object

Under the identification \(z=\rho-1/2\), the finite characteristic
singularities of \(\mathbb T_\Xi\) are precisely the zeros with

\[
 \boxed{\operatorname {Re}\rho=\frac12.}                   \tag{12}
\]

An off-line local Artin factor of (10) has zero image in every
localization of (6) on the real Mellin line.

#### Proof

A finite characteristic singularity of the multiplication operator occurs
at a real \(\gamma_0\) exactly when
\(m(\gamma_0)=\Xi(i\gamma_0)=0\).  This is (12).  The additional decay
at \(|\gamma|=\infty\) is the archimedean torsion end and is not a finite
zero factor.  If \(a\in D\) is a nonreal zero of \(\Xi\), choose a small
disc \(B(a,r)\) disjoint from the imaginary axis.  The corresponding
local Artin factor is supported in that disc, whereas restriction to the
imaginary axis sees a nowhere-zero analytic multiplier in a neighborhood
of every real point.  Multiplication is locally invertible there, so the
localized critical-line torsion object is zero. \(\square\)

The theorem remains true for multiple zeros: the vanishing order can be
read from the small-value spectral density of \(|M_m|\), but only when
the zero lies on the line.

## 5. The comparison theorem

Let

\[
 \mathfrak R_D:\mathcal H_D\longrightarrow \mathbb T_\Xi|_D \tag{13}
\]

denote any functorial comparison induced by restriction of analytic
Mellin data to the critical line.  Here the right side is understood in
the extended sense of (2), not as the zero reduced cokernel.

### Theorem 5.1 — Faithful positive comparison is the missing theorem

The comparison (13) can be faithful on every finite window only if every
zero of \(\Xi\) lies on the imaginary axis.  Conversely, if every zero in
\(D\) lies on the imaginary axis, the complete local support of
\(\mathcal H_D\) occurs in the torsion support (11).

#### Proof

If \(a\) is an off-axis zero in \(D\), its nonzero local Artin factor in
(10) is killed by Theorem 4.1, so (13) is not faithful.  The converse is
the equality of the two supports inside \(D\).  Recovering the full
nilpotent jet requires the corresponding graph-scale filtration, but no
off-support factor remains. \(\square\)

In particular, the positive form (7) cannot simply be transported to the
full CCM degree one.  Transport is faithful precisely after the off-line
local factors have been excluded.

## 6. Consequence for the polarization programme

The torsion category repairs the *dense-range* defect but not the
*analytic-support* defect:

* reduced \(L^2\) kills every isolated resonance;
* extended \(L^2\) retains critical-line singularities of the boundary
  multiplier;
* the CCM nuclear cokernel retains the complete complex zero divisor.

Thus an extended-Hilbert completion is a genuine new object and carries a
canonical positive polarization, but it cannot be the sought global
polarization by itself.  The missing theorem is not merely “do not close
the range.”  It is a source-side intersection map which sends every
analytic local factor to the critical-line torsion support.  By Theorem
4.1 such a faithful map already excludes off-line factors.

## 7. Status

Proved:

* a torsion-sensitive positive Hodge object for the completed arithmetic
  multiplier;
* exact compatibility with normalized scaling and the Tate weight;
* the precise support retained by that object;
* the exact failure of faithfulness for an off-line analytic factor.

Not proved:

* faithful comparison of the full CCM analytic cokernel with the positive
  torsion object.

This closes the possibility that the missing polarization is obtained
solely by replacing reduced Hilbert cohomology with extended Hilbert
cohomology.
