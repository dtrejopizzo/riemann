# Loewner cone margin-tail decomposition

## Purpose

`195_LOEWNER_SCHUR_TAIL_COMPARISON_GATE.md` and
`199_COMPARATIVE_INNOVATION_MARGIN_GATE.md` formulate the comparative
Loewner--Schur route:
\[
  \mathfrak Q^{\mathcal C,T}
  =
  \mathfrak Q^{\mathcal L}
  -{1\over4}\mathfrak Q^{\mathcal A}
  -\mathfrak Q^{\mathcal R,T}.
\]

This note rewrites that comparative form as a sum of two exact pieces:
the strong-margin form and the tail-surplus form.  The decomposition shows
precisely what a non-circular Loewner proof must add beyond A0.

## The two pieces

Define the strong-margin form
\[
\boxed{
  \mathfrak Q^{\mathcal M}
  =
  \mathfrak Q^{\mathcal L}
  -{1\over2}\mathfrak Q^{\mathcal A}.
}
\tag{1}
\]

Define the tail-surplus form
\[
\boxed{
  \mathfrak Q^{\Delta,T}
  =
  {1\over4}\mathfrak Q^{\mathcal A}
  -
  \mathfrak Q^{\mathcal R,T}.
}
\tag{2}
\]

Then
\[
\boxed{
  \mathfrak Q^{\mathcal C,T}
  =
  \mathfrak Q^{\mathcal M}
  +
  \mathfrak Q^{\Delta,T}.
}
\tag{3}
\]

On the Li test vector \(p_n=1-z^n\), with the normalizations of `195`,
\[
  {1\over2}\mathfrak Q^{\mathcal M}(p_n,p_n)
  =
  \lambda_n-{1\over2}A_n
  =
  M_n,
\tag{4}
\]
and
\[
  {1\over2}\mathfrak Q^{\Delta,T_n}(p_n,p_n)
  =
  {1\over4}A_n-R_n(T_n)
  =
  \delta_n.
\tag{5}
\]

Therefore
\[
\boxed{
  {1\over2}\mathfrak Q^{\mathcal C,T_n}(p_n,p_n)
  =
  M_n+\delta_n
  =
  C_n(T_n).
}
\tag{6}
\]

This is the Loewner-cone version of the compensation identity.

## Cone sufficient conditions

A sufficient Loewner theorem for A1 is:
\[
\boxed{
  \mathfrak Q^{\mathcal M}
  +
  \mathfrak Q^{\Delta,T_n}
  \succeq0
  \quad\hbox{on a space containing }p_n.
}
\tag{7}
\]

Two stronger but simpler sufficient conditions are:
\[
\boxed{
  \mathfrak Q^{\mathcal M}\succeq0
  \quad\hbox{and}\quad
  \mathfrak Q^{\Delta,T_n}\succeq0
}
\tag{8}
\]
on that same space.

However, (8) is much stronger than the scalar information currently
available:

1. \(\mathfrak Q^{\mathcal M}\succeq0\) implies
   \[
     M_n\ge0,
   \]
   hence strong margin on the Li test vectors.
2. \(\mathfrak Q^{\Delta,T_n}\succeq0\) implies
   \[
     \delta_n\ge0,
   \]
   but A0 supplies only this scalar endpoint on \(p_n\), not positivity of
   the whole form on any larger comparison space.

Thus the cone decomposition does not weaken the problem.  It identifies
the exact missing comparison: prove positivity of the sum in (7), or prove
that the tail-surplus cone dominates the negative part of the margin cone
on the chosen comparison space.

## Scalar diagonal reduction

On \(p_n\), (7) reduces to
\[
  M_n+\delta_n\ge0.
\tag{9}
\]

Equivalently,
\[
\boxed{
  \delta_n\ge -M_n.
}
\tag{10}
\]

This is exactly the same condition obtained in `238`, `240`, and `241`.
Therefore a Loewner proof that is checked only on the one-dimensional
space \(\mathbb C p_n\) is not a new mechanism; it is A1 itself.

To become non-circular, the proof must establish a structural statement on
a larger space before reading off the value at \(p_n\).  For example, it
could prove:
\[
\boxed{
  \mathfrak Q^{\Delta,T_n}(u,u)
  \ge
  -\mathfrak Q^{\mathcal M}(u,u)
  \qquad(u\in\mathcal V_n)
}
\tag{11}
\]
for a canonically defined space \(\mathcal V_n\ni p_n\).

Equation (11) is the genuine Loewner order version of the one-sided tail
theorem.  At \(u=p_n\) it is exactly (10).

## Schur complement consequence

Let
\[
  \mathfrak Q^{\mathcal C,T_n}
  =
  \mathfrak Q^{\mathcal M}
  +
  \mathfrak Q^{\Delta,T_n}
\]
on a finite space \(W_n=U_n\oplus\mathbb Cp_n\).  Write its matrix as
\[
  \begin{pmatrix}
    B_n & b_n\\
    b_n^* & d_n
  \end{pmatrix},
  \qquad
  d_n=2C_n(T_n).
\tag{12}
\]

If \(B_n\succeq0\), then a Schur proof requires
\[
\boxed{
  d_n-b_n^*B_n^\dagger b_n\ge0.
}
\tag{13}
\]

Since \(b_n^*B_n^\dagger b_n\ge0\), this implies
\[
  d_n\ge0.
\]
Thus the Schur innovation theorem is stronger than the diagonal scalar
A1 unless \(b_n=0\) after a canonical orthogonalization.  Proving (13)
from Euler--Gamma data would be a valid route; deriving it after assuming
the sign of \(d_n\) would be circular.

## Status

Closed as the Loewner cone margin-tail decomposition.

A1 remains open.  The comparative route now has the precise non-circular
target: prove Loewner domination of the negative strong-margin cone by the
tail-surplus cone, or prove nonnegative Schur innovation for the completed
comparative form before using the diagonal value \(2C_n(T_n)\).
