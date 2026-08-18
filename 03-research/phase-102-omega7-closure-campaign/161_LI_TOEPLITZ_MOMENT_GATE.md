# Li Toeplitz moment gate

## Purpose

The disk Schur/Carathéodory route can be stated as a moment problem.  This
note records the exact Toeplitz positivity gate for the Li transform.

The point is that coefficientwise Li positivity is not the same as
Toeplitz moment positivity.  Toeplitz positivity would be a stronger
boundary-measure theorem and would close Omega7.

## Disk moments

Let
\[
  F(z)=\log\xi\!\left({1\over1-z}\right),
  \qquad
  \mathcal L(z)=zF'(z)=\sum_{n\ge1}\lambda_n z^n.
\]

In zero-side disk coordinates,
\[
  w_\rho=1-{1\over\rho}.
\]

Formally, the Li coefficients are paired power sums of the transformed
divisor:
\[
  \lambda_n
  =
  \sum_\rho \left(1-w_\rho^n\right)
\tag{1}
\]
in the usual paired sense.

If a positive boundary measure \(\nu\) on \(\partial\mathbb D\) represented
the transformed divisor, its moments would be
\[
  m_n=\int_{\partial\mathbb D}\zeta^n\,d\nu(\zeta).
\tag{2}
\]

The Carathéodory function
\[
  H(z)=\int_{\partial\mathbb D}{1+\zeta z\over1-\zeta z}\,d\nu(\zeta)
\tag{3}
\]
has positive real part in the disk and expansion
\[
  H(z)=\nu(\partial\mathbb D)+2\sum_{n\ge1}m_n z^n.
\tag{4}
\]

Thus a disk positive-measure theorem is equivalent to positivity of all
Toeplitz moment matrices
\[
  \boxed{
  \left[m_{j-k}\right]_{0\le j,k\le N}\ge0
  \qquad(N\ge0),
  }
\tag{5}
\]
with \(m_{-n}=\overline{m_n}\).

## Relation to Li coefficients

Li positivity asks for
\[
  \lambda_n\ge0\qquad(n\ge1).
\tag{6}
\]

Toeplitz positivity is different.  It asks for positivity of all quadratic
forms
\[
  \sum_{j,k=0}^N c_j\overline{c_k}\,m_{j-k}\ge0.
\tag{7}
\]

Coefficient positivity of a single sequence does not imply (7).  Therefore
the following implication is invalid:
\[
  \lambda_n\ge0\hbox{ termwise}
  \quad\Longrightarrow\quad
  \hbox{Carathéodory/Schur representation}.
\]

Conversely, a Carathéodory representation whose measure is the completed
boundary divisor would imply the support statement and hence Omega7.

## Completed Euler--Gamma gate

A non-tautological Toeplitz theorem for phase 102 would be:

Construct moments \(m_n\) from the completed Euler--Gamma data, with the
same paired normalization as the Li coefficients, such that:

1. the Toeplitz matrices \([m_{j-k}]\) are positive semidefinite for every
   \(N\);
2. the singularities of the associated Carathéodory function are exactly the
   transformed nontrivial zero divisor;
3. the construction is made before assuming the transformed divisor lies on
   \(\partial\mathbb D\).

Then the Herglotz representation theorem on the disk gives a positive
boundary measure \(\nu\) supported on \(\partial\mathbb D\).  The singularity
condition forces
\[
  |1-1/\rho|=1
\]
for every nontrivial zero \(\rho\), which is RH.  Li positivity follows.

## Why finite Toeplitz checks do not close A1

For each fixed \(N\), positivity of
\[
  [m_{j-k}]_{0\le j,k\le N}
\]
is only a finite condition.  A1/Omega7 requires the infinite moment problem:
all \(N\), with a cofinal identification of the moments with the completed
Euler--Gamma boundary data.

Thus finite Toeplitz positivity is like finite Jensen positivity: useful as
reconnaissance, not a proof.

## Relation to A1

If the Toeplitz gate is proved, then the positive boundary measure gate of
`116_POSITIVE_BOUNDARY_MEASURE_TARGET.md` is proved.  Consequently:

1. all nontrivial zeros lie on the critical line;
2. \(\lambda_n\ge0\) for every \(n\);
3. the finite range and A0/A1 assembly close Omega7.

If the gate is not proved, the Toeplitz language is only another
representation of the missing support theorem.

## Status

Closed as a gate.  A1 remains open.

The live theorem is infinite Toeplitz moment positivity for the completed
Euler--Gamma boundary data, with non-circular identification of the
transformed zero divisor.
