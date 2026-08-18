# One-sided tail from global positivity audit

## Purpose

`189_GLOBAL_LOG_DERIVATIVE_TO_COMPACT_A1_AUDIT.md` showed that global
log-derivative positivity closes Omega7 through RH/Li, but does not by
itself close the compact A1 budget.

This note refines the bridge question:

\[
  \hbox{Can global log-derivative/Toeplitz/Schoenberg positivity force}
  \quad
  R_n(T_n)\le \lambda_n-{1\over4}A_n?
\tag{1}
\]

Here
\[
  A_n=\lambda_n^{\rm arch}>0,\qquad n\ge8,
\]
and \(R_n(T_n)\) is the paired A0 tail.

The conclusion is:

\[
  \boxed{
  \hbox{No, not from global positivity alone.}
  }
\]

The one-sided tail inequality (1) is exactly compact A1 in tail language.
Global positivity supplies \(\lambda_n\ge0\); it does not order the signed
moving tail \(R_n(T_n)\) below \(\lambda_n-A_n/4\).

## Exact equivalence with compact A1

From `150_A1_TAIL_REMAINDER_GENERATOR_IDENTITY.md`,
\[
  C_n(T_n)=\lambda_n-R_n(T_n)-{1\over4}A_n.
\tag{2}
\]

Therefore
\[
  C_n(T_n)\ge0
\]
if and only if
\[
  \boxed{
  R_n(T_n)\le \lambda_n-{1\over4}A_n.
  }
\tag{3}
\]

Thus the proposed one-sided tail theorem is not merely a consequence useful
for A1.  It is A1 itself after the generator identity.

Any proof of (3) must therefore contain the same missing signed information
as compact A1, unless it is replaced by a stronger independent margin.

## What global positivity gives

The global half-plane theorem
\[
  \Re{\xi'\over\xi}(s)\ge0\qquad(\Re s>1/2)
\tag{4}
\]
is equivalent to the increment Toeplitz/Schoenberg positivity:
\[
  [g_{|j-k|}]_{1\le j,k\le N}\ge0,
\qquad
  [\lambda_j+\lambda_k-\lambda_{|j-k|}]_{1\le j,k\le N}\ge0.
\tag{5}
\]

In particular, taking the diagonal in the Schoenberg kernel gives
\[
  2\lambda_n\ge0
  \qquad(n\ge1).
\tag{6}
\]

This is Li positivity.  It is enough to close Omega7.  But the one-sided
tail inequality (3) asks for
\[
  \lambda_n-R_n(T_n)-{1\over4}A_n\ge0,
\tag{7}
\]
which compares the global coefficient \(\lambda_n\) with a separate moving
tail coefficient \(R_n(T_n)\) and a fixed archimedean quarter.

The matrices in (5) contain the Li coefficients and their second-difference
positive-definite structure.  They do not contain an order relation between
the full Li generator \(\mathcal L\) and the moving tail generators
\(\mathcal R_{T_n}\).

## Generator separation

The exact moving-diagonal identity is
\[
  [z^n]\mathcal C_{T_n}
  =
  [z^n]\mathcal L
  -
  {1\over4}[z^n]\mathcal A
  -
  [z^n]\mathcal R_{T_n}.
\tag{8}
\]

Global Toeplitz positivity is a positivity statement for the completed Li
or increment object.  A one-sided tail theorem would require the coefficient
inequality
\[
  [z^n]\mathcal R_{T_n}
  \le
  [z^n]\mathcal L
  -
  {1\over4}[z^n]\mathcal A.
\tag{9}
\]

This is not a formal consequence of positivity of \(\mathcal L\), of the
Schoenberg kernel, or of the increment Toeplitz matrices.  It is a
comparison theorem between two different signed coefficient functionals,
one of them depending on the moving cutoff \(T_n\).

Equivalently, (9) is a Loewner/order statement missing from the global
theorem.  The global theorem gives a positive form; it does not say that
subtracting the archimedean quarter and the moving tail leaves a positive
diagonal coefficient.

## Margin decomposition

Define the Li margin
\[
  M_n=\lambda_n-{1\over2}A_n.
\tag{10}
\]

Using (2),
\[
\begin{aligned}
  C_n(T_n)
  &=
  \lambda_n-R_n(T_n)-{1\over4}A_n\\
  &=
  M_n+\left({1\over4}A_n-R_n(T_n)\right).
\end{aligned}
\tag{11}
\]

A0 gives
\[
  R_n(T_n)\le {1\over4}A_n,
\tag{12}
\]
so the second term in (11) is nonnegative.  Therefore the strong margin
\[
  M_n\ge0
\tag{13}
\]
is sufficient for A1.

But global positivity gives only
\[
  \lambda_n\ge0,
\]
or
\[
  M_n\ge -{1\over2}A_n.
\tag{14}
\]

Thus the precise missing margin is
\[
  \boxed{
  \lambda_n\ge {1\over2}A_n
  }
\tag{15}
\]
unless one proves a sharper one-sided tail bound than A0.

More generally, write
\[
  R_n(T_n)={1\over4}A_n-\delta_n.
\tag{16}
\]
A0 says only
\[
  \delta_n\ge0
\]
for the upper side of the tail.  Compact A1 is
\[
  M_n+\delta_n\ge0.
\tag{17}
\]

Global positivity gives \(M_n\ge-A_n/2\).  It gives no lower bound for
\(\delta_n\) strong enough to compensate a negative \(M_n\).  The missing
theorem is exactly either \(M_n\ge0\), a quantitative lower bound for
\(\delta_n\), or a direct proof of their sum.

## Formal separation of available data

Suppose the only data imported from the global theorem and A0 are
\[
  \lambda_n\ge0,
  \qquad
  -{1\over4}A_n\le R_n(T_n)\le {1\over4}A_n.
\tag{18}
\]

These inequalities allow, as proof data, the pattern
\[
  \lambda_n=0,
  \qquad
  R_n(T_n)={1\over4}A_n.
\tag{19}
\]

Then the proposed one-sided inequality becomes
\[
  {1\over4}A_n
  \le
  -{1\over4}A_n,
\]
which is false, and
\[
  C_n(T_n)=-{1\over2}A_n<0.
\]

This does not claim that (19) occurs for zeta.  It proves that the formal
information supplied by global positivity plus the A0 absolute tail does
not logically contain the one-sided tail theorem.

## Valid ways to obtain the one-sided tail

A proof of (3) must add one of the following non-formal inputs:

1. **Strong margin.**
   \[
     \lambda_n\ge {1\over2}A_n.
   \]
   Together with A0, this gives (3).

2. **Quantitative tail gain.**
   Prove
   \[
     R_n(T_n)\le {1\over4}A_n-\delta_n,
   \]
   with
   \[
     \delta_n\ge {1\over2}A_n-\lambda_n
   \]
   whenever the Li margin is below \(A_n/2\).  This is a signed
   tail--margin correlation theorem, not a consequence of absolute A0.

3. **Direct compact core.**
   Prove \(C_n(T_n)\ge0\) in the Laguerre/core variables.  This proves the
   one-sided tail inequality by (2), but does not derive it from global
   positivity.

4. **Loewner/Schur comparison.**
   Construct a positive Euler--Gamma form in which the operator
   corresponding to
   \[
     \mathcal L-{1\over4}\mathcal A-\mathcal R_{T_n}
   \]
   is positive on the moving Li diagonal.  This would be a new margin
   theorem, stronger than bare Toeplitz positivity.

## Status

Closed as an implication audit.  A1 remains open.

Global log-derivative, Toeplitz, or Schoenberg positivity can close Omega7
through RH/Li, but it does not by itself impose the one-sided tail
inequality.  The missing compact theorem is exactly a strong margin,
tail--margin correlation, Loewner/Schur comparison, or direct signed-core
proof.
