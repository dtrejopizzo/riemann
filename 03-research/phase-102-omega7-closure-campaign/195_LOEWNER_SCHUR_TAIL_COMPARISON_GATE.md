# Loewner--Schur tail comparison gate

## Purpose

`192_ONE_SIDED_TAIL_FROM_GLOBAL_POSITIVITY_AUDIT.md` isolated the missing
comparison:
\[
  [z^n]\mathcal R_{T_n}
  \le
  [z^n]\mathcal L
  -
  {1\over4}[z^n]\mathcal A.
\tag{1}
\]

Equivalently,
\[
  C_n(T_n)
  =
  [z^n]\left(\mathcal L-{1\over4}\mathcal A-\mathcal R_{T_n}\right)
  \ge0.
\tag{2}
\]

This note writes the exact Loewner/Schur form that would imply (2) on the
moving diagonal, explains why global Toeplitz positivity does not imply it
formally, and isolates the comparative theorem still needed.

## Three moment forms

Let \(\mathfrak Q^{\mathcal L}\) denote a completed Li Toeplitz/Schoenberg
quadratic form normalized so that
\[
  {1\over2}\mathfrak Q^{\mathcal L}(1-z^n,1-z^n)=\lambda_n.
\tag{3}
\]

Let \(\mathfrak Q^{\mathcal A}\) be the archimedean form normalized by
\[
  {1\over2}\mathfrak Q^{\mathcal A}(1-z^n,1-z^n)=A_n
  =
  \lambda_n^{\rm arch}.
\tag{4}
\]

Finally, for each cutoff \(T\), let \(\mathfrak Q^{\mathcal R,T}\) be the
tail form normalized by
\[
  {1\over2}\mathfrak Q^{\mathcal R,T}(1-z^n,1-z^n)=R_n(T).
\tag{5}
\]

These symbols are not assumed positive.  They are the Hermitian forms whose
diagonal Li-test values reproduce the three coefficient functionals in
`150_A1_TAIL_REMAINDER_GENERATOR_IDENTITY.md`.

Define the comparative form
\[
  \boxed{
  \mathfrak Q^{\mathcal C,T}
  =
  \mathfrak Q^{\mathcal L}
  -
  {1\over4}\mathfrak Q^{\mathcal A}
  -
  \mathfrak Q^{\mathcal R,T}.
  }
\tag{6}
\]

Then
\[
  {1\over2}\mathfrak Q^{\mathcal C,T_n}(1-z^n,1-z^n)
  =
  \lambda_n-{1\over4}A_n-R_n(T_n)
  =
  C_n(T_n).
\tag{7}
\]

Therefore compact A1 is exactly
\[
  \boxed{
  \mathfrak Q^{\mathcal C,T_n}(1-z^n,1-z^n)\ge0
  \qquad(n\ge8).
  }
\tag{8}
\]

## Minimal diagonal Loewner gate

The weakest comparative theorem sufficient for A1 is the moving-diagonal
Loewner condition:
\[
  \boxed{
  \mathfrak Q^{\mathcal L}(p_n,p_n)
  \ge
  {1\over4}\mathfrak Q^{\mathcal A}(p_n,p_n)
  +
  \mathfrak Q^{\mathcal R,T_n}(p_n,p_n),
  \quad
  p_n=1-z^n,\ n\ge8.
  }
\tag{9}
\]

This is exactly (8).  It is a diagonal comparison of forms depending on the
moving cutoff \(T_n\).

A stronger, cleaner theorem would be a Loewner inequality on a finite
subspace:
\[
  \boxed{
  \mathfrak Q^{\mathcal C,T_n}(p,p)\ge0
  \quad
  \hbox{for all }p\in\mathcal V_n,
  }
\tag{10}
\]
where \(\mathcal V_n\) is any subspace containing \(1-z^n\), for example
\[
  \mathcal V_n=\mathrm{span}\,\{1,z,\ldots,z^n\}
\]
or the vanishing-test subspace
\[
  \mathcal V_n=(z-1)\mathbb C_{\le n}[z].
\]

In matrix language, if \(M_N^{\mathcal L}\), \(M_N^{\mathcal A}\), and
\(M_N^{\mathcal R,T}\) are the finite Gram matrices of these forms on
\(\{1,z,\ldots,z^N\}\), then the stronger condition is
\[
  \boxed{
  M_N^{\mathcal L}
  -
  {1\over4}M_N^{\mathcal A}
  -
  M_N^{\mathcal R,T_n}
  \succeq 0
  \quad\hbox{on a subspace containing }1-z^n.
  }
\tag{11}
\]

The diagonal A1 target needs only the quadratic value on \(1-z^n\), but a
Loewner theorem like (11) would provide a non-tautological structural
reason for it.

## Schur-complement version

If the comparative matrix in (11) is written as
\[
  M_N^{\mathcal C,T}
  =
  M_N^{\mathcal L}
  -
  {1\over4}M_N^{\mathcal A}
  -
  M_N^{\mathcal R,T},
\tag{12}
\]
then a Schur route can be stated as follows.

Let \(W_n\) be the finite-dimensional space in which \(p_n=1-z^n\) is
represented, and split
\[
  W_n=U_n\oplus \mathbb C p_n
\]
after choosing a complement \(U_n\).  A sufficient Schur theorem is:

1. \(M_N^{\mathcal C,T_n}\) is nonnegative on \(U_n\);
2. the Schur complement in the \(p_n\)-direction is nonnegative:
   \[
     \boxed{
     \mathfrak Q^{\mathcal C,T_n}(p_n,p_n)
     -
     b_n^*B_n^{\dagger}b_n
     \ge0,
     }
   \tag{13}
   \]
   where \(B_n\) is the block on \(U_n\), \(b_n\) is the coupling vector,
   and \(B_n^{\dagger}\) is the Moore--Penrose inverse when needed.

Since
\[
  b_n^*B_n^{\dagger}b_n\ge0
\]
whenever \(B_n\ge0\), (13) is stronger than the diagonal A1 inequality
\[
  \mathfrak Q^{\mathcal C,T_n}(p_n,p_n)\ge0.
\]

Thus a Schur proof cannot stop at a formal block identity.  It must prove
positivity of the comparative form before identifying the Schur complement
with the A1 scalar.  This is the same non-tautological constraint already
encountered in the bordered-current and Schur--Friedrichs gates.

## Why global Toeplitz positivity is insufficient

Global Toeplitz/Schoenberg positivity says
\[
  \mathfrak Q^{\mathcal L}(p,p)\ge0
\tag{14}
\]
for the appropriate completed Li form, or equivalently positivity of its
increment/Schoenberg reductions.

But (14) does not imply
\[
  \mathfrak Q^{\mathcal L}(p,p)
  \ge
  {1\over4}\mathfrak Q^{\mathcal A}(p,p)
  +
  \mathfrak Q^{\mathcal R,T_n}(p,p).
\tag{15}
\]

Positivity of one form is not an order comparison with two other signed
forms.  In Loewner language,
\[
  M^{\mathcal L}\succeq0
\]
does not imply
\[
  M^{\mathcal L}
  -
  {1\over4}M^{\mathcal A}
  -
  M^{\mathcal R,T_n}
  \succeq0.
\tag{16}
\]

The missing input is an upper bound on the moving tail form plus the
archimedean quarter in the same quadratic geometry as the Li form.  Neither
Li positivity, increment Toeplitz positivity, nor Schoenberg positivity
contains that comparison as formal algebra.

On the Li test \(p_n=1-z^n\), this failure reduces to the scalar separation
from `192`:
\[
  \lambda_n\ge0
  \quad\not\Longrightarrow\quad
  \lambda_n-{1\over4}A_n-R_n(T_n)\ge0.
\tag{17}
\]

## Exact comparative theorem needed

The surviving Loewner--Schur route is therefore:

**Comparative tail theorem.**  Construct the completed Euler--Gamma forms
\(\mathfrak Q^{\mathcal L}\), \(\mathfrak Q^{\mathcal A}\), and
\(\mathfrak Q^{\mathcal R,T}\), with the normalizations (3)--(5), and prove
for every \(n\ge8\) that
\[
  \mathfrak Q^{\mathcal L}(1-z^n,1-z^n)
  -
  {1\over4}\mathfrak Q^{\mathcal A}(1-z^n,1-z^n)
  -
  \mathfrak Q^{\mathcal R,T_n}(1-z^n,1-z^n)
  \ge0.
\tag{18}
\]

Equivalently, prove a stronger subspace Loewner inequality
\[
  \mathfrak Q^{\mathcal L}
  -
  {1\over4}\mathfrak Q^{\mathcal A}
  -
  \mathfrak Q^{\mathcal R,T_n}
  \succeq0
\tag{19}
\]
on a finite space containing \(1-z^n\).

This theorem is exactly a non-tautological comparison between the full
Euler--Gamma Li form and the moving tail form.  It is stronger than bare
global positivity and equivalent to, or stronger than, compact A1 depending
on whether (18) or (19) is proved.

## Status

Closed as a gate formulation.  A1 remains open.

The required new theorem is a comparative Loewner/Schur inequality for
\[
  \mathcal L-{1\over4}\mathcal A-\mathcal R_{T_n},
\]
not merely positivity of the global Li/Toeplitz/Schoenberg form.
