# Exact cumulative forcing representation

## Purpose

`156_A1_LAGUERRE_N_RECURRENCE_GATE.md` gives the recurrence
\[
  nC_{n+1}(T)
  =
  (2n+1)C_n(T)
  -(n+1)C_{n-1}(T)
  +F_n(T).
\]

This note solves that recurrence explicitly in cumulative forcing form.
The result is an exact representation of \(C_n(T)\) at a fixed cutoff.

This sharpens the induction route: positivity of each individual forcing
term is sufficient but not necessary; the exact load is positivity of a
weighted cumulative sum.

## Difference recurrence

Let
\[
  \Delta_n(T)=C_n(T)-C_{n-1}(T).
\]

From `156`,
\[
  {\Delta_{n+1}(T)\over n+1}
  =
  {\Delta_n(T)\over n}
  +
  {F_n(T)\over n(n+1)}.
\tag{1}
\]

For \(n\ge8\), iterating gives
\[
  \boxed{
  {\Delta_n(T)\over n}
  =
  {\Delta_8(T)\over8}
  +
  \sum_{k=8}^{n-1}{F_k(T)\over k(k+1)}
  }
  \qquad(n\ge9).
\tag{2}
\]

Therefore
\[
  \Delta_n(T)
  =
  n\left[
  {\Delta_8(T)\over8}
  +
  \sum_{k=8}^{n-1}{F_k(T)\over k(k+1)}
  \right].
\tag{3}
\]

## Exact formula for \(C_n(T)\)

For \(n\ge8\),
\[
  C_n(T)=C_8(T)+\sum_{j=9}^{n}\Delta_j(T).
\tag{4}
\]

Substituting (3),
\[
\boxed{
  C_n(T)
  =
  C_8(T)
  +
  \left(\sum_{j=9}^{n}j\right){\Delta_8(T)\over8}
  +
  \sum_{j=9}^{n}
  j\sum_{k=8}^{j-1}{F_k(T)\over k(k+1)}.
}
\tag{5}
\]

Switching the order of summation,
\[
  \sum_{j=9}^{n}
  j\sum_{k=8}^{j-1}{F_k(T)\over k(k+1)}
  =
  \sum_{k=8}^{n-1}
  {F_k(T)\over k(k+1)}
  \sum_{j=k+1}^{n}j.
\tag{6}
\]

Since
\[
  \sum_{j=a}^{n}j={n(n+1)-(a-1)a\over2},
\]
we get
\[
  \sum_{j=k+1}^{n}j
  =
  {n(n+1)-k(k+1)\over2}.
\tag{7}
\]

Also
\[
  \sum_{j=9}^{n}j={n(n+1)-72\over2}.
\tag{8}
\]

Thus the closed formula is
\[
\boxed{
  C_n(T)
  =
  C_8(T)
  +
  {n(n+1)-72\over16}\,\Delta_8(T)
  +
  {1\over2}
  \sum_{k=8}^{n-1}
  \left({n(n+1)\over k(k+1)}-1\right)F_k(T).
}
\tag{9}
\]

This is exact for every fixed cutoff \(T\) and every \(n\ge8\).

## Necessary and sufficient fixed-cutoff condition

For a fixed cutoff \(T\), the statement
\[
  C_n(T)\ge0\qquad(n\ge8)
\tag{10}
\]
is equivalent to:

1. \(C_8(T)\ge0\);
2. for every \(n\ge9\),
   \[
   \boxed{
     C_8(T)
     +
     {n(n+1)-72\over16}\,\Delta_8(T)
     +
     {1\over2}
     \sum_{k=8}^{n-1}
     \left({n(n+1)\over k(k+1)}-1\right)F_k(T)
     \ge0.
   }
   \tag{11}
   \]

The stronger condition from `156`,
\[
  {\Delta_8(T)\over8}
  +
  \sum_{k=8}^{n-1}{F_k(T)\over k(k+1)}
  \ge0,
\tag{12}
\]
is only sufficient: it forces \(\Delta_n(T)\ge0\), hence monotonicity of
\(C_n(T)\).  Formula (11) allows controlled negative differences as long as
the accumulated value \(C_n(T)\) stays nonnegative.

## Forcing content

The forcing is
\[
  F_k(T)
  =
  M_k(T)+1+{3\over4}D_k^{\rm arch},
\tag{13}
\]
where
\[
  M_k(T)=
  \int_0^T u\,E(e^u)e^{-u}L_{k-1}^{(2)}(u)\,du.
\tag{14}
\]

Therefore the exact fixed-cutoff A1 induction theorem is a weighted
cumulative signed estimate for
\[
  M_k(T)+1+{3\over4}D_k^{\rm arch}.
\]

Termwise positivity of \(F_k(T)\) is not required.  What is required is the
family of cumulative inequalities (11).

## Moving cutoff

A1 uses \(T=T_n\), not one fixed \(T\).  Hence (9) cannot be applied directly
to the A0 diagonal.

For the moving cutoff define
\[
  \widetilde C_n=C_n(T_n).
\]

Choose a common cutoff \(S\) for a block.  Then
\[
  \widetilde C_n
  =
  C_n(S)
  +
  \bigl[C_n(T_n)-C_n(S)\bigr].
\tag{15}
\]

The first term is controlled by (9).  The second term is exactly the
cutoff-transfer quantity from `153_CUTOFF_COMPARISON_AND_MONOTONICITY_GATE.md`
and `154_CUTOFF_TRANSFER_DUAL_BALANCE.md`.

Thus a moving-diagonal induction proof requires:

1. the fixed-cutoff cumulative forcing inequalities (11);
2. a signed transfer theorem for
   \[
     C_n(T_n)-C_n(S).
   \]

This is the exact Target E load.

## Status

Closed as an exact fixed-cutoff recurrence solution.  A1 remains open.

The live induction target is now the cumulative inequality (11), plus the
moving-cutoff transfer theorem needed to pass to \(T=T_n\).
