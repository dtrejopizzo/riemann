# Poisson Carathéodory positivity gate

## Purpose

`162_LI_FEJER_TRIGONOMETRIC_MOMENT_GATE.md` gives the Cesaro/Fejer version
of the disk moment problem.  This note records the equivalent Abel/Poisson
version:
\[
  \Re H(re^{i\theta})\ge0
  \qquad(0\le r<1,\ \theta\in\mathbb R).
\]

This is the most compact analytic form of the global positive-measure route.
It does not close A1 unless the completed Euler--Gamma function \(H\) is
constructed and the above real-part inequality is proved without assuming
critical-line support.

## Moment and Carathéodory notation

Let \((m_k)_{k\in\mathbb Z}\) be Hermitian:
\[
  m_{-k}=\overline{m_k}.
\]

Define the formal Carathéodory series
\[
  H_m(z)=m_0+2\sum_{k\ge1}m_k z^k.
\tag{1}
\]

For \(z=re^{-i\theta}\),
\[
\begin{aligned}
  \Re H_m(re^{-i\theta})
  &=
  m_0+\sum_{k\ge1}\left(m_k r^k e^{-ik\theta}
  +m_{-k}r^k e^{ik\theta}\right)\\
  &=
  \sum_{k\in\mathbb Z}m_k r^{|k|}e^{-ik\theta}.
\end{aligned}
\tag{2}
\]

Thus the real part of \(H_m\) is exactly the Abel/Poisson mean of the
trigonometric moment distribution.

## Equivalence theorem

For a Hermitian sequence with finite \(m_0\), the following are equivalent:

1. all Toeplitz matrices
   \[
     [m_{j-k}]_{0\le j,k\le N}
   \]
   are positive semidefinite;
2. there exists a positive finite measure \(\nu\) on \(\partial\mathbb D\)
   with moments
   \[
     m_k=\int_{\partial\mathbb D}\zeta^k\,d\nu(\zeta);
   \]
3. the Carathéodory series has nonnegative real part:
   \[
     \Re H_m(z)\ge0\qquad(|z|<1);
   \tag{3}
   \]
4. all Poisson means are nonnegative:
   \[
     \sum_{k\in\mathbb Z}m_k r^{|k|}e^{-ik\theta}\ge0
     \qquad(0\le r<1,\ \theta\in\mathbb R).
   \tag{4}
   \]

The equivalence of (1) and (2) is the trigonometric moment theorem.  If (2)
holds, then
\[
  \Re H_m(z)
  =
  \int_{\partial\mathbb D}
  \Re {1+\overline{\zeta}z\over1-\overline{\zeta}z}\,d\nu(\zeta)
  =
  \int_{\partial\mathbb D}P_z(\zeta)\,d\nu(\zeta)\ge0,
\tag{5}
\]
where \(P_z\) is the Poisson kernel.  Conversely, if (3) holds, the Herglotz
theorem gives the representing positive measure and hence (2).

Therefore the Poisson gate, the Fejer gate and the Toeplitz gate are the
same infinite positivity theorem in three summability languages:
\[
  \hbox{Toeplitz}
  \Longleftrightarrow
  \hbox{Fejer/Cesaro}
  \Longleftrightarrow
  \hbox{Poisson/Abel}
  \Longleftrightarrow
  \hbox{Carathéodory}.
\tag{6}
\]

## Euler--Gamma version

The required theorem for Omega7 is:

**Completed Poisson positivity theorem.**  Construct \(H_{\rm EG}\) from the
completed Euler--Gamma Li data such that:

1. \(H_{\rm EG}\) has the moment expansion
   \[
     H_{\rm EG}(z)=m_0^{\rm EG}+2\sum_{k\ge1}m_k^{\rm EG}z^k
   \]
   in the disk, with Hermitian moments in the paired Li normalization;
2. for every \(|z|<1\),
   \[
     \Re H_{\rm EG}(z)\ge0;
   \tag{7}
   \]
3. the singularities of the analytic continuation of \(H_{\rm EG}\) are
   exactly the transformed nontrivial zero divisor
   \[
     w_\rho=1-{1\over\rho},
   \]
   up to explicitly harmless analytic terms;
4. the construction and the proof of (7) do not use
   \(|w_\rho|=1\).

Then Herglotz gives a positive boundary measure.  The singularity condition
forces every \(w_\rho\) to lie on \(\partial\mathbb D\), hence RH and Omega7
follow.

## Why this is not automatic from \(\xi\)

The function
\[
  z{d\over dz}\log\xi\!\left({1\over1-z}\right)
\]
has the Li coefficients, but coefficient positivity and real-part positivity
are different assertions.

The condition
\[
  \lambda_n\ge0\qquad(n\ge1)
\]
tests only the special square \(1-z^n\) after a moment normalization.  The
condition
\[
  \Re H_{\rm EG}(z)\ge0
\]
tests every direction in every Toeplitz block simultaneously.  It is a
positive-measure theorem, not a restatement of a one-dimensional coefficient
inequality.

Nor is (7) a consequence of Euler-product positivity in \(\Re s>1\).  The
Li disk map sends the boundary problem to a completed object involving the
pole-prime pairing and the Gamma factor.  Positivity must survive that
completion and continuation.

## Relation to A1 and the Schur margin

Bare Poisson/Carathéodory positivity implies Li positivity globally.  It
would therefore close Omega7 through the zero-side Li criterion.  The compact
A1 route asks for a sharper local statement after the A0 cutoff:
\[
  C_n(T_n)\ge0.
\]

As recorded in `164_A1_TOEPLITZ_SCHUR_MARGIN.md`, A1 after A0 follows from
the stronger margin
\[
  Q_n(1-z^n)\ge \lambda_n^{\rm arch}\qquad(n\ge8),
\tag{8}
\]
or from the still stronger Toeplitz innovation margin.  Thus there are two
distinct global positivity targets:

1. prove \(\Re H_{\rm EG}\ge0\), which closes Omega7 directly;
2. prove the stronger archimedean margin, which closes the compact A1
   decomposition after A0.

The first route is enough for Omega7.  The second route is aligned with the
existing A0/A1 budget.

## Status

Closed as an equivalent analytic gate.  A1 remains open.

The exact missing analytic theorem is the completed Euler--Gamma
Carathéodory inequality
\[
  \Re H_{\rm EG}(z)\ge0\qquad(|z|<1),
\]
with non-circular singularity identification.
