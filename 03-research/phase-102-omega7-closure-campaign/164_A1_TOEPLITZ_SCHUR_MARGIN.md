# A1 Toeplitz Schur margin

## Purpose

This note connects the Schur--Friedrichs energy form of A1 with the disk
Toeplitz moment gate.

The new point is that Toeplitz positivity has a canonical variational form:
the Schur complement of a Toeplitz moment matrix is the prediction-error
energy
\[
  \inf_{\deg q<N} Q(z^N-q).
\]
This gives an exact hierarchy of possible targets:

1. Toeplitz positivity of the completed disk moments;
2. nonnegativity of the Li square energy \(Q(1-z^n)\);
3. the stronger margin \(Q(1-z^n)\ge A_n\), or the still stronger
   prediction-error margin, which implies A1 after A0.

A1 is not closed here.  The missing theorem is an Euler--Gamma Toeplitz
moment construction with the required margin.

## Toeplitz moments and quadratic energy

Let \((m_k)_{k\in\mathbb Z}\) be a Hermitian moment sequence,
\[
  m_{-k}=\overline{m_k},
\]
and define the Toeplitz matrices
\[
  T_N=[m_{j-k}]_{0\le j,k\le N}.
\]
For a polynomial
\[
  p(z)=\sum_{j=0}^N c_j z^j,
\]
write
\[
  Q_N(p)
  =
  \sum_{j,k=0}^N c_j\overline{c_k}\,m_{j-k}
  =
  c^*T_Nc.
\tag{1}
\]

Toeplitz positivity is exactly
\[
  Q_N(p)\ge0
  \qquad(N\ge0,\ \deg p\le N).
\tag{2}
\]
If the moments come from a positive measure \(\nu\) on \(\partial\mathbb D\),
then
\[
  Q_N(p)=\int_{\partial\mathbb D}|p(\zeta)|^2\,d\nu(\zeta).
\tag{3}
\]

## Li square energy

Assume now that the disk moments are symmetric in the Li sense, so that the
paired Li coefficient is
\[
  \lambda_n=m_0-m_n
\tag{4}
\]
with \(m_n\in\mathbb R\).  Then the test polynomial
\[
  p_n(z)=1-z^n
\]
has Toeplitz energy
\[
\begin{aligned}
  Q_n(p_n)
  &=m_0+m_0-m_n-m_{-n}  \\
  &=2(m_0-m_n).
\end{aligned}
\tag{5}
\]
Therefore
\[
  \boxed{
  \lambda_n={1\over2}Q_n(1-z^n).
  }
\tag{6}
\]

Thus a positive disk moment theorem gives Li positivity by a square:
\[
  Q_n(1-z^n)\ge0
  \Longrightarrow
  \lambda_n\ge0.
\]
This is stronger than coefficientwise Li positivity because it asks for
positivity of every Toeplitz quadratic form, not just of the special tests
\(1-z^n\).

## Schur--Friedrichs prediction error

Suppose \(T_{N-1}>0\).  Split
\[
  T_N=
  \begin{pmatrix}
    T_{N-1}&b_N\\
    b_N^*&m_0
  \end{pmatrix},
\tag{7}
\]
where the ordering is \((1,z,\ldots,z^{N-1},z^N)\), so
\[
  b_N=(m_{0-N},m_{1-N},\ldots,m_{N-1-N})^t.
\]
The Schur complement is
\[
  \sigma_N
  =
  m_0-b_N^*T_{N-1}^{-1}b_N.
\tag{8}
\]

Equivalently,
\[
  \boxed{
  \sigma_N
  =
  \inf_{\deg q<N} Q_N(z^N-q).
  }
\tag{9}
\]
Indeed, writing \(q(z)=\sum_{j=0}^{N-1}a_jz^j\), the energy
\[
  Q_N(z^N-q)
\]
is an affine quadratic function of \(a\).  Completing the square gives
exactly (8).  This is the Toeplitz version of the Schur--Friedrichs minimum
from `142_A1_VARIATIONAL_ENERGY_FORM.md`.

Consequently, for a nested Toeplitz sequence with all leading blocks
invertible,
\[
  T_N\ge0\quad\hbox{for every }N
\]
is equivalent to
\[
  m_0\ge0,\qquad \sigma_N\ge0\quad(N\ge1),
\tag{10}
\]
with the usual limiting interpretation when a block is singular.

## Relation to compact A1

Let
\[
  A_n=\lambda_n^{\rm arch}>0\qquad(n\ge8),
\]
and write the prime tail after the A0 cutoff as
\[
  R_n(T_n)
  =
  \lambda_n^{\rm prime}
  -
  \left[
    -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy
  \right].
\tag{11}
\]
Then
\[
  \lambda_n
  =
  A_n
  -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy
  +R_n(T_n).
\tag{12}
\]
The compact A1 quantity is
\[
  C_n(T_n)
  =
  -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy
  +{3\over4}A_n.
\tag{13}
\]
Therefore
\[
  \boxed{
  C_n(T_n)=\lambda_n-R_n(T_n)-{1\over4}A_n.
  }
\tag{14}
\]

Using the Li square energy (6), this becomes
\[
  C_n(T_n)
  =
  {1\over2}Q_n(1-z^n)-R_n(T_n)-{1\over4}A_n.
\tag{15}
\]
A0 gives
\[
  |R_n(T_n)|\le {1\over4}A_n.
\tag{16}
\]
Hence A1 follows from the Toeplitz Li-test margin
\[
  \boxed{
  {1\over2}Q_n(1-z^n)\ge {1\over2}A_n
  \qquad(n\ge8).
  }
\tag{17}
\]
Equivalently,
\[
  Q_n(1-z^n)\ge A_n.
\tag{18}
\]

This is exactly the strong-margin route in Toeplitz energy language:
\[
  \lambda_n\ge {1\over2}A_n.
\]

## Prediction-error margin as a stronger sufficient theorem

Since \(q=1\) is one of the competitors in
\[
  \sigma_n=\inf_{\deg q<n}Q_n(z^n-q),
\]
the prediction-error margin
\[
  \boxed{
  \sigma_n\ge A_n\qquad(n\ge8)
  }
\tag{19}
\]
implies
\[
  Q_n(z^n-1)\ge A_n,
\]
and therefore implies A1 by (15)--(16).

Thus the Toeplitz Schur--Friedrichs path has a precise sufficient target:

1. construct the completed Euler--Gamma disk moments \(m_k\) non-circularly;
2. prove the infinite Toeplitz positivity needed for the moment problem;
3. prove the stronger innovation margin \(\sigma_n\ge A_n\) for \(n\ge8\),
   or at least the Li-test margin \(Q_n(1-z^n)\ge A_n\).

The margin is essential for compact A1.  Bare Toeplitz positivity gives
\[
  Q_n(1-z^n)\ge0,
\]
which yields Li positivity, but by itself it does not imply the compact
cutoff inequality (13), because the signed tail \(R_n(T_n)\) can consume the
A0 budget.

## Missing theorem

The exact live theorem isolated by this note is:

**Toeplitz Schur margin theorem.**  The completed Euler--Gamma data define a
Hermitian disk moment sequence \((m_k)\), with the same paired normalization
as the Li coefficients, such that:

1. the Toeplitz matrices \([m_{j-k}]_{0\le j,k\le N}\) are positive
   semidefinite for every \(N\);
2. the associated Carathéodory singularities are the transformed nontrivial
   zero divisor, without assuming boundary support;
3. for every \(n\ge8\), either
   \[
     Q_n(1-z^n)\ge A_n
   \]
   or the stronger Schur--Friedrichs innovation bound
   \[
     \sigma_n\ge A_n
   \]
   holds.

Then A1 follows from A0 by (15)--(16), and Omega7 follows by the existing
assembly.

The theorem is not proved here.  It is stronger than the Toeplitz moment gate
of `161_LI_TOEPLITZ_MOMENT_GATE.md`, because it includes an archimedean
margin rather than only nonnegativity.

## Status

Closed as a reduction.  A1 remains open.

The Schur--Friedrichs Toeplitz minimum gives a clean variational target, but
the required Euler--Gamma moment construction and margin estimate are still
missing.
