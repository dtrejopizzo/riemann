# Li Schoenberg vanishing kernel

## Purpose

`168_RENORMALIZED_VANISHING_TEST_KERNEL_TARGET.md` isolates a positive form
on polynomials \(p(1)=0\).  This note writes the corresponding kernel
directly in Li coefficients.

The result is a renormalized exact normal form:
\[
  K(j,k)=\lambda_j+\lambda_k-\lambda_{|j-k|}.
\]

It is not a proof of A1.  It is the first explicit candidate for the
vanishing-test positivity cone.

## Boundary model calculation

On the critical-line model, transformed zeros satisfy
\[
  |w_\rho|=1,\qquad w_\rho=1-{1\over\rho}.
\]

For the Li test vectors
\[
  e_j(z)=1-z^j\qquad(j\ge1),
\]
the critical-line square form is
\[
  \mathfrak Q_{\rm CL}(e_j,e_k)
  =
  \sum_\rho (1-w_\rho^j)(1-\overline{w_\rho}^{\,k}).
\tag{1}
\]

Since \(\overline{w_\rho}=w_\rho^{-1}\) on the boundary,
\[
\begin{aligned}
  (1-w_\rho^j)(1-w_\rho^{-k})
  &=
  1-w_\rho^j-w_\rho^{-k}+w_\rho^{j-k}.
\end{aligned}
\tag{2}
\]

Using the paired Li normalization
\[
  \lambda_n=\sum_\rho(1-w_\rho^n),
  \qquad
  \lambda_{-n}=\lambda_n,
  \qquad
  \lambda_0=0,
\tag{3}
\]
equation (2) gives
\[
  \boxed{
  \mathfrak Q_{\rm CL}(e_j,e_k)
  =
  \lambda_j+\lambda_k-\lambda_{j-k}.
  }
\tag{4}
\]

With the symmetric convention \(\lambda_{-m}=\lambda_m\), this is
\[
  \boxed{
  K(j,k)=\lambda_j+\lambda_k-\lambda_{|j-k|}.
  }
\tag{5}
\]

In particular,
\[
  K(n,n)=2\lambda_n.
\tag{6}
\]

Thus Li positivity is the diagonal part of the positive-kernel statement.

## Kernel positivity theorem needed

Let \(c_1,\ldots,c_N\in\mathbb C\).  The renormalized vanishing-kernel
positivity theorem is
\[
  \boxed{
  \sum_{j,k=1}^{N}c_j\overline{c_k}
  \left(\lambda_j+\lambda_k-\lambda_{|j-k|}\right)\ge0
  \qquad(N\ge1).
  }
\tag{7}
\]

If (7) is proved from completed Euler--Gamma data, then every diagonal entry
is nonnegative:
\[
  2\lambda_n=K(n,n)\ge0.
\]
Therefore Li positivity and Omega7 follow.

For the compact A1 assembly after A0, the stronger diagonal margin
\[
  K(n,n)\ge 2\lambda_n^{\rm arch}
  \qquad(n\ge8)
\tag{8}
\]
is sufficient, because it is exactly
\[
  \lambda_n\ge\lambda_n^{\rm arch}.
\]
That margin is stronger than needed for Li and should be treated as a
sufficient A1 route, not as an equivalent target.

## Relation to negative type

The kernel (5) is the standard Schoenberg transform of the function
\[
  d(j,k)=\lambda_{|j-k|}
\]
on the additive semigroup of nonnegative integers.  Positivity of
\[
  K(j,k)=d(j,0)+d(k,0)-d(j,k)
\]
means that \(d\) is of negative type on this anchored set.

Equivalently, for coefficients \(a_0,\ldots,a_N\) with
\[
  \sum_{j=0}^{N}a_j=0,
\]
the condition is
\[
  \sum_{j,k=0}^{N}a_j\overline{a_k}\lambda_{|j-k|}\le0.
\tag{9}
\]

Thus the Li problem can be embedded into a renormalized negative-type
problem.  This is different from Toeplitz moment positivity: it acts on
differences \(p(1)=0\), not on all moments of a finite measure.

## Why this is stronger than coefficient positivity

The inequalities
\[
  \lambda_n\ge0
\]
are only the diagonal constraints \(K(n,n)\ge0\).  Positive semidefiniteness
of \(K\) also requires all mixed inequalities, for example
\[
  \det
  \begin{pmatrix}
    2\lambda_j&\lambda_j+\lambda_k-\lambda_{|j-k|}\\
    \lambda_j+\lambda_k-\lambda_{|j-k|}&2\lambda_k
  \end{pmatrix}
  \ge0.
\tag{10}
\]

Therefore (7) is not merely Li positivity rewritten.  It is a stronger
Hilbert-space theorem whose diagonal would imply Li.

## Non-circular construction obligation

The derivation (1)--(5) used the boundary identity
\[
  \overline{w_\rho}=w_\rho^{-1}.
\]
That identity is equivalent to \(|w_\rho|=1\), hence to critical-line
support.  It cannot be used as a proof.

The valid theorem must construct the kernel (5), or a completed
Euler--Gamma kernel with the same Li-square values, directly from the
arithmetically completed data and prove (7) without inserting
\(\overline{w_\rho}=w_\rho^{-1}\) as a hypothesis.

This is the exact non-circular content of the vanishing-kernel route.

## Status

Closed as a kernel normal form.  A1 remains open.

The new target is the Schoenberg positivity of
\[
  \left[\lambda_j+\lambda_k-\lambda_{|j-k|}\right]_{1\le j,k\le N}
\]
for every \(N\), or an Euler--Gamma renormalized variant with the A1
archimedean margin.
