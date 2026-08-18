# Global log-derivative to compact A1 audit

## Purpose

`174_LOG_DERIVATIVE_HALF_PLANE_POSITIVITY_GATE.md` identifies the global
half-plane theorem
\[
  \Re{\xi'\over\xi}(s)\ge0\qquad(\Re s>1/2)
\tag{1}
\]
with the increment Toeplitz gate.  `175_LOG_DERIVATIVE_RH_EQUIVALENCE.md`
then proves that (1) is equivalent to RH.

This note answers the remaining compatibility question:

\[
  \hbox{Does (1) imply compact A1 directly?}
\]

The answer is:

\[
  \boxed{\hbox{No, not through the existing A0/A1 bookkeeping alone.}}
\]

The global theorem would close Omega7 by RH and Li, but compact A1 is a
stronger cutoff-budget statement.  To derive compact A1 from the global
theorem one still needs an archimedean margin, a one-sided tail theorem, or
a direct signed-core proof.

## Exact identities

Write
\[
  A_n=\lambda_n^{\rm arch}>0\qquad(n\ge8)
\]
and let \(R_n(T)\) be the paired tail in
`150_A1_TAIL_REMAINDER_GENERATOR_IDENTITY.md`.  The compact A1 quantity is
\[
  C_n(T_n)
  =
  \lambda_n-R_n(T_n)-{1\over4}A_n.
\tag{2}
\]

Therefore compact A1 is exactly
\[
  C_n(T_n)\ge0
\tag{3}
\]
or equivalently
\[
  \boxed{
  \lambda_n\ge R_n(T_n)+{1\over4}A_n.
  }
\tag{4}
\]

The A0 theorem supplies only the absolute tail budget
\[
  |R_n(T_n)|\le {1\over4}A_n.
\tag{5}
\]

The global log-derivative theorem (1) supplies, through RH and Li,
\[
  \lambda_n\ge0.
\tag{6}
\]

Combining (5) and (6) gives at best
\[
  C_n(T_n)
  =
  \lambda_n-R_n(T_n)-{1\over4}A_n
  \ge
  -{1\over2}A_n.
\tag{7}
\]

This lower bound is not A1.

## Necessary and sufficient bridge

For each \(n\ge8\), the exact bridge from global Li data to compact A1 is
\[
  \boxed{
  R_n(T_n)\le \lambda_n-{1\over4}A_n.
  }
\tag{8}
\]

This is not a consequence of \(\lambda_n\ge0\).  It is precisely the
one-sided tail theorem already isolated by the phase.

Using only A0, a sufficient replacement for (8) is the strong margin
\[
  \lambda_n\ge {1\over2}A_n.
\tag{9}
\]

Indeed, (5) and (9) give
\[
  C_n(T_n)
  \ge
  {1\over2}A_n-{1\over4}A_n-{1\over4}A_n
  =
  0.
\tag{10}
\]

Thus the exact implication chain is:
\[
  \hbox{global log-derivative positivity}
  \Longrightarrow
  \lambda_n\ge0,
\]
but compact A1 requires in addition either (8), (9), or a direct proof of
(3).

## Toeplitz interpretation

The increment Toeplitz theorem of `172` gives a positive-definite
second-difference sequence
\[
  g_0=2\lambda_1,\qquad
  g_m=\lambda_{m+1}-2\lambda_m+\lambda_{m-1}.
\]

Equivalently, the Schoenberg kernel
\[
  K(j,k)=\lambda_j+\lambda_k-\lambda_{|j-k|}
\]
is positive semidefinite.  Its diagonal is
\[
  K(n,n)=2\lambda_n.
\tag{11}
\]

Thus global positivity gives the diagonal statement
\[
  K(n,n)\ge0.
\tag{12}
\]

Compact A1 after A0 asks for the stronger diagonal margin
\[
  K(n,n)\ge A_n
\tag{13}
\]
or, equivalently,
\[
  \lambda_n\ge {1\over2}A_n.
\tag{14}
\]

Positive semidefiniteness alone does not contain the numerical lower bound
(13).  It gives nonnegativity of squared tests; A1 needs the square to
dominate a specific archimedean budget and the signed moving tail.

This is the same gap recorded in `164_A1_TOEPLITZ_SCHUR_MARGIN.md`.

## Algebraic separation

The separation can be seen without changing any analytic object.  Suppose
only the inequalities supplied by the global route and A0 are known:
\[
  \lambda_n\ge0,
  \qquad
  |R_n(T_n)|\le {1\over4}A_n.
\tag{15}
\]

These allow the sign pattern
\[
  \lambda_n=0,\qquad R_n(T_n)={1\over4}A_n.
\tag{16}
\]

Then
\[
  C_n(T_n)
  =
  0-{1\over4}A_n-{1\over4}A_n
  =
  -{1\over2}A_n<0.
\tag{17}
\]

Thus the formal information
\[
  \lambda_n\ge0
  \quad+\quad
  |R_n(T_n)|\le {1\over4}A_n
\]
does not imply A1.  Any derivation of A1 from global positivity must use
additional structure beyond these two inequalities.

This is a logical separation of proof data, not a construction of a zeta
counterexample.  It states exactly which information is absent from the
global implication.

## What would close the gap

There are three valid bridges from the global side to compact A1:

1. **Strong margin**
   \[
     \lambda_n\ge {1\over2}A_n\qquad(n\ge8).
   \]

2. **One-sided tail**
   \[
     R_n(T_n)\le \lambda_n-{1\over4}A_n\qquad(n\ge8),
   \]
   proved from Euler--Gamma data without using A1.

3. **Direct compact signed core**
   \[
     C_n(T_n)\ge0\qquad(n\ge8),
   \]
   by the Laguerre, finite-certificate, recurrence, or moving-diagonal
   mechanisms.

The first two convert the global Li conclusion into the compact A1 budget.
The third bypasses the global route.

## Project-level consequence

If (1) is proved non-circularly, Omega7 is closed:
\[
  (1)\Longrightarrow RH\Longrightarrow\lambda_n\ge0\quad(n\ge1).
\]

But if the internal phase requirement is to close the A0/A1 decomposition
itself, then (1) is not enough unless it is accompanied by one of the bridge
theorems above.

Therefore the correct statement is:
\[
  \boxed{
  \hbox{global log-derivative positivity closes Omega7, but does not by
  itself close compact A1.}
  }
\]

## Status

Closed as an implication audit.  A1 remains open.

The missing compact input is exactly a margin theorem, a one-sided tail
theorem, or a direct signed-core proof.
