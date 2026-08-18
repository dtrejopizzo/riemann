# A1 Laguerre n-recurrence gate

## Purpose

Most A1 normal forms are coefficientwise.  This note records an exact
recurrence in the Li index \(n\), obtained from the three-term recurrence of
Laguerre polynomials.

The point is to isolate a possible induction route.  The route is not closed
because the forcing term contains a new signed moment.  But the induction
load becomes completely explicit.

## Compact integral and moment

For fixed cutoff \(T\), define
\[
  I_n(T)=\int_0^T E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
\tag{1}
\]
and
\[
  M_n(T)=\int_0^T u\,E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
\tag{2}
\]

The A1 compact quantity is
\[
  C_n(T)
  =
  -n-I_n(T)+{3\over4}\lambda_n^{\rm arch}.
\tag{3}
\]

Thus A1 is \(C_n(T_n)\ge0\) for every \(n\ge8\).

## Laguerre recurrence

The standard recurrence
\[
  (m+1)L_{m+1}^{(\alpha)}(u)
  =
  (2m+\alpha+1-u)L_m^{(\alpha)}(u)
  -(m+\alpha)L_{m-1}^{(\alpha)}(u)
\tag{4}
\]
with \(m=n-1\) and \(\alpha=2\) gives
\[
  nL_n^{(2)}(u)
  =
  (2n+1-u)L_{n-1}^{(2)}(u)
  -(n+1)L_{n-2}^{(2)}(u).
\tag{5}
\]

Multiplying by \(E(e^u)e^{-u}\) and integrating over \([0,T]\),
\[
  \boxed{
  nI_{n+1}(T)
  =
  (2n+1)I_n(T)-M_n(T)-(n+1)I_{n-1}(T).
  }
\tag{6}
\]

This identity is exact for \(n\ge2\).

## Recurrence for the A1 quantities

Put
\[
  A_n=\lambda_n^{\rm arch}.
\]
Since
\[
  I_n(T)=-n+{3\over4}A_n-C_n(T),
\tag{7}
\]
substituting (7) into (6) gives
\[
  \boxed{
  nC_{n+1}(T)
  =
  (2n+1)C_n(T)
  -(n+1)C_{n-1}(T)
  +F_n(T),
  }
\tag{8}
\]
where the forcing term is
\[
  \boxed{
  F_n(T)
  =
  M_n(T)
  +1
  +{3\over4}
  \left[
    nA_{n+1}-(2n+1)A_n+(n+1)A_{n-1}
  \right].
  }
\tag{9}
\]

Equivalently, with
\[
  \Delta_n(T)=C_n(T)-C_{n-1}(T),
\]
one has
\[
  \boxed{
  n\Delta_{n+1}(T)
  =
  (n+1)\Delta_n(T)+F_n(T).
  }
\tag{10}
\]

Dividing by \(n(n+1)\),
\[
  \boxed{
  {\Delta_{n+1}(T)\over n+1}
  =
  {\Delta_n(T)\over n}
  +
  {F_n(T)\over n(n+1)}.
  }
\tag{11}
\]

Therefore, for \(n\ge8\),
\[
  {\Delta_n(T)\over n}
  =
  {\Delta_8(T)\over 8}
  +
  \sum_{k=8}^{n-1}{F_k(T)\over k(k+1)}.
\tag{12}
\]

This is the exact first-difference induction formula.

## Induction gate for fixed cutoff

For a fixed cutoff \(T\), coefficient positivity
\[
  C_n(T)\ge0\qquad(n\ge8)
\]
would follow from:

1. a finite base certificate \(C_8(T)\ge0\);
2. a lower bound on the cumulative normalized forcing
   \[
     {\Delta_8(T)\over 8}
     +
     \sum_{k=8}^{n-1}{F_k(T)\over k(k+1)}
     \ge0
     \qquad(n\ge9).
   \tag{13}
   \]

Indeed, (13) implies \(\Delta_n(T)\ge0\) for \(n\ge9\), and then
\[
  C_n(T)\ge C_8(T)\ge0.
\]

This is a sufficient theorem, not an equivalence.  More general induction
schemes may allow controlled negative differences, but every such scheme
must control the same forcing \(F_n(T)\).

## Moving-cutoff form

A1 uses \(T=T_n\), so (8)--(12) do not directly form a recurrence along the
A0 diagonal.  Along the moving diagonal one must compare
\[
  C_{n+1}(T_{n+1}),\quad C_n(T_n),\quad C_{n-1}(T_{n-1}),
\]
whereas (8) holds at one common cutoff \(T\).

Thus an induction proof of A1 must combine:

1. the fixed-cutoff recurrence above;
2. the cutoff-transfer theorem of
   `153_CUTOFF_COMPARISON_AND_MONOTONICITY_GATE.md` or its dual version
   `154_CUTOFF_TRANSFER_DUAL_BALANCE.md`.

Equivalently, choose a common auxiliary cutoff \(S_n\) for a block of indices,
prove the recurrence at that cutoff, and then transfer to \(T_n\) with a
signed bound.

## Why the recurrence is not automatically positive

The recurrence (8) is not positivity-preserving by itself because of the
negative term
\[
  -(n+1)C_{n-1}(T).
\]
In first-difference form, all positivity is carried by the forcing \(F_n(T)\).

The forcing contains the signed moment
\[
  M_n(T)=\int_0^T u\,E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du,
\]
which has the same prime-Laguerre phase problem as A1.  Ordinary PNT bounds
control \(|M_n(T)|\), not the sign or cumulative lower bound required in
(13).

The archimedean part of \(F_n\) is audited in
`157_ARCHIMEDEAN_FORCING_AUDIT.md`.  It is explicit, but not a free positive
margin.  Thus the live signed forcing problem is the full combination
\(M_n(T)+1+\frac34D_n^{\rm arch}\).

## Status

Closed as an exact recurrence normal form.  A1 remains open.

The new live theorem is a signed lower bound for the normalized cumulative
forcing in (13), together with a moving-cutoff transfer if the proof is to
apply on the A0 diagonal \(T=T_n\).
