# Cofinal subsequence certificate no-go

## Purpose

This note closes a common false shortcut between finite arithmetic
certificates and full compact A1:

\[
\boxed{
  \hbox{certificates on an infinite cofinal subsequence do not prove A1.}
}
\]

They become useful only after a structural propagation theorem converts the
subsequence information into every missing coordinate, or after an effective
threshold theorem leaves a genuinely finite remainder.

## A1 as a coordinatewise conjunction

Compact A1 is the pointwise statement
\[
\boxed{
  C_n(T_n)\ge0\qquad(n\ge8).
}
\tag{1}
\]

Let \(S\subset\{8,9,\ldots\}\) be infinite and cofinal.  A subsequence
certificate proves only
\[
\boxed{
  C_n(T_n)\ge0\qquad(n\in S).
}
\tag{2}
\]

The implication \((2)\Rightarrow(1)\) is not formal.

## Separation

For any proper subset \(S\subsetneq\{8,9,\ldots\}\), choose
\[
  N\in\{8,9,\ldots\}\setminus S.
\]

Define a coordinate functional \(L_N\) on finitely supported nonnegative
test weights by
\[
  L_N(\mu)=\sum_{n\ge8}\mu_n c_n,\qquad
  c_n=
  \begin{cases}
    1,&n\ne N,\\
   -1,&n=N.
  \end{cases}
\]

Then \(L_N(\delta_n)\ge0\) for every \(n\in S\), but
\[
  L_N(\delta_N)=-1<0.
\]

Thus any testing family that omits the coordinate \(N\) cannot certify the
coordinate \(N\).  The same separation is the coordinate version of the
dual-cone gate in `256`.

## Consequence for cofinal computations

Even if \(S\) is cofinal, has density one, contains arbitrarily long
blocks, or is produced by a natural arithmetic progression of parameters,
positivity on \(S\) proves only those indices unless a separate theorem
supplies one of:

1. monotone or recurrent propagation from \(S\) to all omitted indices;
2. positive reconstruction of every missing coordinate mass from the tested
   coordinates;
3. an explicit effective threshold \(N_\infty\) above which all indices are
   covered, plus rigorous finite verification below it.

Without one of these additions, a missed index can still carry the negative
coordinate in the separation above.

## Relation to the finite-certificate gate

`277` rules out threshold-free finite checking.  This note rules out the
parallel infinite-but-subsequential shortcut.  Both express the same A1
principle:

\[
\boxed{
  \hbox{A1 is coordinatewise; every coordinate must be proved or
  positively reconstructed.}
}
\]

Thus certificates from `148`, `190`, `230`, or `261` may be sampled on
finite or cofinal sets for diagnostics, but they close compact A1 only after
they are made uniform, propagated, or paired with an effective threshold
and a complete finite remainder check.

## Status

Closed as a no-go for cofinal/subsequence certificate shortcuts.  A1
remains open until every \(n\ge8\) is covered by a direct proof, a positive
reconstruction, or an effective-threshold plus finite-remainder theorem.
