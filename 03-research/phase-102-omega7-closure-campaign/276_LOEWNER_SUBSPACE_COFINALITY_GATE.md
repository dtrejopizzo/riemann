# Loewner subspace cofinality gate

## Purpose

The comparative Loewner--Schur route proves compact A1 only if it tests the
actual Li direction
\[
  p_n=1-z^n.
\]

This note records the exact cofinality condition.  Positivity of the
comparative form on subspaces or test families that do not contain, or do
not positively reconstruct, \(p_n\) does not imply A1.

## Exact diagonal target

With the normalizations of `195`,
\[
\boxed{
  {1\over2}\mathfrak Q^{\mathcal C,T_n}(p_n,p_n)
  =
  C_n(T_n).
}
\tag{1}
\]

Thus compact A1 is exactly
\[
\boxed{
  \mathfrak Q^{\mathcal C,T_n}(p_n,p_n)\ge0
  \qquad(n\ge8).
}
\tag{2}
\]

## Inclusion criterion

If a finite-dimensional test space \(V_n\) satisfies
\[
  p_n\in V_n
\]
and
\[
  \mathfrak Q^{\mathcal C,T_n}(v,v)\ge0
  \qquad(v\in V_n),
\tag{3}
\]
then (2) follows immediately.

Therefore the simplest valid Loewner cofinality condition is
\[
\boxed{
  p_n\in V_n\qquad(n\ge8).
}
\tag{4}
\]

## Positive reconstruction criterion

More generally, suppose the proof tests a family of vectors
\[
  v_\alpha\in W_n.
\]

Knowing
\[
  H(v_\alpha,v_\alpha)\ge0
\]
for a Hermitian form \(H\) implies \(H(p_n,p_n)\ge0\) for every such \(H\)
only if
\[
\boxed{
  p_np_n^*
  \in
  \overline{\operatorname{cone}}\{v_\alpha v_\alpha^*\}
}
\tag{5}
\]
in the finite-dimensional cone of rank-one Hermitian tests.

Indeed, if (5) holds, \(H(p_n,p_n)\) is a nonnegative limit of known
nonnegative tested values.  If (5) fails, finite-dimensional separation
gives a Hermitian form \(H\) such that
\[
  H(v_\alpha,v_\alpha)\ge0
  \quad\hbox{for every tested }\alpha,
\]
but
\[
  H(p_n,p_n)<0.
\]

Thus unrelated test positivity cannot rule out a negative A1 diagonal.

## Relation with Schur innovation

In a Schur proof one chooses
\[
  W_n=U_n\oplus\mathbb Cp_n.
\]
This automatically satisfies the inclusion condition.  The remaining
obligations are then the genuine Schur obligations of `199`: positivity on
\(U_n\), the range condition, and nonnegative innovation.

If \(p_n\) is not included or positively reconstructed, the Schur or
Loewner theorem has no A1 diagonal content.

## Status

Closed as the cofinality gate for Loewner--Schur tests.  A1 remains open
until the comparative form is proved nonnegative on a space containing
\(p_n\), or until \(p_n\) is positively reconstructed from tested
directions, or until the diagonal A1 inequality is proved directly.
