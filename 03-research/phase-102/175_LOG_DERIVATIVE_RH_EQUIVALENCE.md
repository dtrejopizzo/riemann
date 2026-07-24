# Log-derivative RH equivalence audit

## Purpose

`174_LOG_DERIVATIVE_HALF_PLANE_POSITIVITY_GATE.md` states the compact
half-plane gate
\[
  \Re{\xi'\over\xi}(s)\ge0\qquad(\Re s>1/2).
\tag{1}
\]

This note audits the exact logical status of that gate.

The conclusion is:
\[
  [g_{|j-k|}]_{1\le j,k\le N}\ge0\quad(\forall N)
  \Longleftrightarrow
  \Re{\xi'\over\xi}(s)\ge0\quad(\Re s>1/2)
  \Longleftrightarrow
  {\rm RH}.
\tag{2}
\]

Thus `174` is not merely a sufficient route.  Its positivity theorem is an
RH-equivalent theorem.  This does not close A1; it identifies the exact
global theorem still missing.

## Toeplitz to Carathéodory, with the boundedness condition made explicit

Define
\[
  g_0=2\lambda_1,\qquad
  g_m=\lambda_{m+1}-2\lambda_m+\lambda_{m-1}\quad(m\ge1),
\]
and set \(g_{-m}=g_m\).  The finite Toeplitz condition is
\[
  \sum_{j,k=1}^{N}c_j\overline{c_k}\,g_{j-k}\ge0
  \qquad(N\ge1,\ c\in\mathbb C^N).
\tag{3}
\]

By Herglotz, (3) for every \(N\) is equivalent to the existence of a finite
positive measure \(\nu\) on \(\partial\mathbb D\) such that
\[
  g_m=\int_{\partial\mathbb D}\zeta^m\,d\nu(\zeta)
  \qquad(m\in\mathbb Z).
\tag{4}
\]

In particular,
\[
  |g_m|\le g_0.
\tag{5}
\]

The associated Carathéodory function is
\[
  H_g(z)
  =
  g_0+2\sum_{m\ge1}g_mz^m
  =
  \int_{\partial\mathbb D}{\zeta+z\over \zeta-z}\,d\nu(\zeta),
\tag{6}
\]
so
\[
  \Re H_g(z)\ge0\qquad(|z|<1).
\tag{7}
\]

Conversely, if a holomorphic function \(H(z)=g_0+2\sum_{m\ge1}g_mz^m\) has
\(\Re H\ge0\) in \(\mathbb D\), then Herglotz gives (4), hence all Toeplitz
blocks are positive.

Thus the Toeplitz statement is a full infinite moment theorem.  Finite
checks, coefficientwise inequalities, or positivity only on selected
trigonometric tests do not imply it.

## Identification of the Carathéodory function

Let
\[
  s={1\over1-z},\qquad q(s)={\xi'\over\xi}(s).
\]

From the Li generator,
\[
  \mathcal L(z)
  =
  {z\over(1-z)^2}\,q\!\left({1\over1-z}\right).
\tag{8}
\]

From the second-difference generator in `172`,
\[
  \mathcal G_+(z)
  =
  g_0+\sum_{m\ge1}g_mz^m
  =
  \lambda_1+{(1-z)^2\over z}\mathcal L(z).
\tag{9}
\]

Therefore
\[
  \mathcal G_+(z)
  =
  \lambda_1+q\!\left({1\over1-z}\right).
\tag{10}
\]

Since \(\lambda_1=q(1)\), the Carathéodory function attached to the Hermitian
sequence \(g_{-m}=g_m\) is
\[
\begin{aligned}
  H_g(z)
  &=
  g_0+2\sum_{m\ge1}g_mz^m\\
  &=
  2\mathcal G_+(z)-g_0\\
  &=
  2q\!\left({1\over1-z}\right).
\end{aligned}
\tag{11}
\]

The disk coordinate satisfies
\[
  |z|<1
  \Longleftrightarrow
  \Re {1\over1-z}>{1\over2}.
\tag{12}
\]

Hence, once the function is holomorphic in the disk, Toeplitz positivity of
\(g\) is equivalent to
\[
  \Re q(s)\ge0\qquad(\Re s>1/2).
\tag{13}
\]

The holomorphy clause is not cosmetic.  If \(q\) had a pole in the half-plane
\(\Re s>1/2\), then \(2q(1/(1-z))\) could not be the Herglotz transform of a
finite positive boundary measure.  Thus Toeplitz positivity itself rules out
such poles by analytic continuation from the Taylor expansion at \(z=0\).

## Positivity implies RH

Assume
\[
  \Re q(s)\ge0\qquad(\Re s>1/2).
\tag{14}
\]

A pole of \(q=\xi'/\xi\) inside the half-plane is a zero of \(\xi\) there.
Near a non-removable pole, the leading principal part has real part of both
signs on sufficiently small circles.  Therefore (14) excludes every zero of
\(\xi\) with
\[
  \Re\rho>{1\over2}.
\tag{15}
\]

The functional equation
\[
  \xi(s)=\xi(1-s)
\tag{16}
\]
reflects zeros by \(\rho\mapsto1-\rho\).  Thus a zero with
\(\Re\rho<1/2\) would reflect to a zero with \(\Re(1-\rho)>1/2\), impossible
by (15).  Hence all nontrivial zeros lie on the critical line.  This is RH.

So (13) is sufficient for RH.

## RH implies positivity

Conversely assume RH.  Use the paired Hadamard product for the completed
function \(\xi\):
\[
  {\xi'\over\xi}(s)
  =
  \lim_{T\to\infty}
  \sum_{|\Im\rho|\le T}{1\over s-\rho},
\tag{17}
\]
with the zeros counted with multiplicity and the standard symmetric limiting
order.  The convergence is locally uniform away from the zeros.

Under RH each zero has
\[
  \rho={1\over2}+i\gamma.
\]

For \(s=\sigma+it\) with \(\sigma>1/2\),
\[
  \Re {1\over s-\rho}
  =
  {\sigma-1/2\over(\sigma-1/2)^2+(t-\gamma)^2}
  >0.
\tag{18}
\]

Taking the symmetric locally uniform limit in (17) gives
\[
  \Re{\xi'\over\xi}(s)\ge0
  \qquad(\Re s>1/2).
\tag{19}
\]

Thus RH implies the half-plane positivity gate.

## Exact status of `174`

The algebra in `174` is correct:
\[
  H_g(z)=2{\xi'\over\xi}\!\left({1\over1-z}\right).
\]

The logical status should be read as the equivalence (2), not as a weaker
one-way sufficient condition.

Therefore the current global target is:

**Log-derivative positivity theorem.**  Prove directly from the completed
Euler--Gamma data, without assuming RH or zero support, that
\[
  \Re{\xi'\over\xi}(s)\ge0\qquad(\Re s>1/2).
\]

This theorem would close Omega7 through RH and Li.

It does not by itself close the compact A1 budget
\[
  C_n(T_n)\ge0\qquad(n\ge8),
\]
unless one additionally proves the archimedean-margin bridge from the
Toeplitz/Schoenberg form to the A0/A1 cutoff decomposition.

## Status

Closed as an audit and correction of logical strength.

A1 remains open.  Omega7 remains open until either the log-derivative
positivity theorem is proved non-circularly, or the compact A1 signed core is
proved directly.
