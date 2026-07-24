# Laguerre lobe block-compensation gate

## Purpose

`313_DIRECT_A1_TERMWISE_SIGN_OBSTRUCTION.md` shows that the direct A1
prime-power certificate is not coefficientwise positive.  This note
records the next viable unit: compensation by signed Laguerre lobes.

It converts the phrase "signed global compensation" into an exact block
criterion over the sign intervals of the high-block coefficient
\[
  \Omega_n(m)=G_{n-1}(T_n)-G_{n-1}(\log m),
  \qquad
  G_N(u)=e^{-u}L_N^{(1)}(u).
\]

## Direct high-block certificate

For \(n\ge9\), the direct certificate of `226` has the schematic form
\[
\boxed{
  \mathcal A_n-P_n+\sum_{m\le e^{T_n}}\Lambda(m)\Omega_n(m)\ge0.
}
\tag{1}
\]

The low block below \(T_8\), endpoint terms, pole term, and archimedean
terms are collected into a fixed remainder
\[
  B_n^{\rm base}.
\]

The moving high block is
\[
\boxed{
  H_n=
  \sum_{T_8\le\log m\le T_n}
  \Lambda(m)\left(G_{n-1}(T_n)-G_{n-1}(\log m)\right).
}
\tag{2}
\]

Then the direct A1 certificate is equivalent to
\[
\boxed{
  B_n^{\rm base}+H_n\ge0.
}
\tag{3}
\]

## Lobe partition

Let
\[
  \omega_n(u)=G_{n-1}(T_n)-G_{n-1}(u).
\]

Let
\[
  T_8=a_{n,0}<a_{n,1}<\cdots<a_{n,J_n}=T_n
\]
be any finite partition such that \(\omega_n\) has a fixed sign on each
open interval \((a_{n,j},a_{n,j+1})\).  The coarsest such partition is
obtained by inserting the zeros of \(\omega_n\), equivalently the
solutions of
\[
  G_{n-1}(u)=G_{n-1}(T_n).
\]

Define block contributions
\[
\boxed{
  H_{n,j}
  =
  \sum_{a_{n,j}\le\log m<a_{n,j+1}}
  \Lambda(m)\omega_n(\log m).
}
\tag{4}
\]

Then
\[
  H_n=\sum_{j=0}^{J_n-1}H_{n,j}.
\]

## Exact block-compensation criterion

Let
\[
  \mathcal P_n=\{j:\omega_n\ge0\hbox{ on }(a_{n,j},a_{n,j+1})\},
  \qquad
  \mathcal N_n=\{j:\omega_n\le0\hbox{ on }(a_{n,j},a_{n,j+1})\}.
\]

Set
\[
  H_n^+=\sum_{j\in\mathcal P_n}H_{n,j},
  \qquad
  H_n^-=-\sum_{j\in\mathcal N_n}H_{n,j}\ge0.
\]

Then the direct A1 certificate (3) is exactly
\[
\boxed{
  H_n^+-H_n^-+B_n^{\rm base}\ge0.
}
\tag{5}
\]

Equivalently, the positive lobe mass must dominate the negative lobe mass
by the base deficit:
\[
\boxed{
  H_n^+\ge H_n^- - B_n^{\rm base}.
}
\tag{6}
\]

Thus a block proof cannot merely bound \(|H_{n,j}|\).  It must prove the
oriented inequality (5) or (6).

## Why absolute lobe bounds are insufficient

Suppose one proves only
\[
  H_n^++H_n^-\le L_n.
\]

This controls total lobe load but not the signed difference
\[
  H_n^+-H_n^-.
\]

For any fixed \(L_n\), the two configurations
\[
  (H_n^+,H_n^-)=(L_n,0),
  \qquad
  (H_n^+,H_n^-)=(0,L_n)
\]
have the same absolute load and opposite sign.  Hence absolute lobe
control cannot imply A1 unless supplemented by an orientation theorem.

This is the direct-prime analogue of the phase-lobe separation in `280`.

## Sufficient block theorem

A non-circular direct proof of A1 may proceed by proving, for every
\(n\ge9\),
\[
\boxed{
  \sum_{j=0}^{J_n-1}
  \sum_{a_{n,j}\le\log m<a_{n,j+1}}
  \Lambda(m)\omega_n(\log m)
  \ge
  -B_n^{\rm base}.
}
\tag{7}
\]

Equivalently, after partial summation on each lobe, it may prove an
oriented Chebyshev-error theorem for the signed weight \(\omega_n\).  The
essential point is that the theorem must keep the signs of the lobes until
after summation; replacing \(\omega_n\) by \(|\omega_n|\) returns to the
discarded absolute route.

## Relation to A1

The block criterion is not weaker or stronger than the direct certificate;
it is the same certificate with the minimal sign partition exposed.  It is
useful because it identifies the next admissible proof unit after the
termwise positivity no-go of `313`:

\[
\boxed{
  \hbox{A1 direct route requires lobe-oriented prime-power compensation.}
}
\]

## Status

Closed as the direct-route lobe-block compensation gate.  A1 remains open
until the oriented block inequality (7), the equivalent tail-margin gate
\(s_n\ge d_n\), or another surviving Fejer/Herglotz/RDI route is proved.
