# Archimedean forcing audit

## Purpose

`156_A1_LAGUERRE_N_RECURRENCE_GATE.md` derives an exact recurrence
\[
  nC_{n+1}(T)
  =
  (2n+1)C_n(T)
  -(n+1)C_{n-1}(T)
  +F_n(T),
\]
where
\[
  F_n(T)
  =
  M_n(T)
  +1
  +{3\over4}
  \left[
    nA_{n+1}-(2n+1)A_n+(n+1)A_{n-1}
  \right],
\]
and \(A_n=\lambda_n^{\rm arch}\).

This note simplifies the archimedean second-order combination.  The correct
formula is explicit but not positive.  Therefore the induction route does
not receive a free archimedean margin; it must control the full signed
forcing.

## Archimedean second-order combination

The phase archimedean term is
\[
  A_n
  =
  1-{n\over2}(\gamma+\log(4\pi))
  +
  \sum_{\substack{r\ge1\\ r\ {\rm odd}}}
  q_n\!\left({1\over r}\right),
\tag{1}
\]
where
\[
  q_n(x)=(1-x)^n-1+nx.
\tag{2}
\]

Define
\[
  D_n^{\rm arch}
  =
  nA_{n+1}-(2n+1)A_n+(n+1)A_{n-1}.
\tag{3}
\]

The constant term in (1) cancels in (3), and the explicit linear term
\[
  -{n\over2}(\gamma+\log(4\pi))
\]
also cancels.  Hence
\[
  D_n^{\rm arch}
  =
  \sum_{\substack{r\ge1\\ r\ {\rm odd}}}
  \left[
    nq_{n+1}\!\left({1\over r}\right)
    -(2n+1)q_n\!\left({1\over r}\right)
    +(n+1)q_{n-1}\!\left({1\over r}\right)
  \right].
\tag{4}
\]

Let \(a=1-x\).  The exponential part contributes
\[
  na^{n+1}-(2n+1)a^n+(n+1)a^{n-1}.
\]
Factoring \(a^{n-1}\),
\[
\begin{aligned}
  na^{n+1}-(2n+1)a^n+(n+1)a^{n-1}
  &=
  a^{n-1}\left[na^2-(2n+1)a+n+1\right]  \\
  &=
  a^{n-1}\left[x+nx^2\right].
\end{aligned}
\tag{5}
\]

The linear part \(nx\) inside \(q_n(x)\) contributes
\[
  n(n+1)x-(2n+1)nx+(n+1)(n-1)x=-x.
\tag{6}
\]

Therefore the exact summand is
\[
  a^{n-1}(x+nx^2)-x.
\tag{7}
\]

With \(x=1/r\), this gives
\[
  \boxed{
  D_n^{\rm arch}
  =
  \sum_{\substack{r\ge1\\ r\ {\rm odd}}}
  \left[
  \left(1-{1\over r}\right)^{n-1}
  \left({1\over r}+{n\over r^2}\right)
  -{1\over r}
  \right].
  }
\tag{8}
\]

The \(r=1\) summand is \(-1\).  For fixed \(r\ge3\), the summand tends to
\(-1/r\) as \(n\to\infty\).  Thus \(D_n^{\rm arch}\) is not termwise
positive and cannot be used as an automatic positive margin.

## Forcing decomposition

The recurrence forcing from `156` is
\[
  \boxed{
  F_n(T)
  =
  M_n(T)+1+{3\over4}D_n^{\rm arch},
  }
\tag{9}
\]
with
\[
  M_n(T)=
  \int_0^T
  u\,E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
\tag{10}
\]

Hence the induction theorem must control the full signed forcing
\[
  M_n(T)+1+{3\over4}D_n^{\rm arch}.
\tag{11}
\]

The corrected first-difference condition is
\[
  {\Delta_8(T)\over8}
  +
  \sum_{k=8}^{n-1}
  {M_k(T)+1+{3\over4}D_k^{\rm arch}\over k(k+1)}
  \ge0
  \qquad(n\ge9).
\tag{12}
\]

This is the exact induction gate.  The archimedean correction is explicit,
but not sign-free.

## Consequence

The induction route remains valid as a possible proof architecture, but the
load is sharper:

1. prove a base certificate at a common cutoff;
2. prove the cumulative lower bound (12);
3. transfer from the common cutoff to the A0 diagonal \(T_n\).

The term \(D_n^{\rm arch}\) is no longer an unknown, but it does not remove
the signed prime-moment problem.

## Status

Closed as a corrected audit.  A1 remains open.

The previous apparent positivity of the archimedean forcing is false; the
correct formula is (8).  The live induction target is the full signed
forcing bound (12), plus moving-cutoff transfer.
