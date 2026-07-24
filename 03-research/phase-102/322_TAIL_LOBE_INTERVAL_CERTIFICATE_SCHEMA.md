# Tail-lobe interval certificate schema

## Purpose

`320_TAIL_LOBE_ONE_SIDED_ENVELOPE_CRITERION.md` gives a sufficient
pointwise theorem for compact A1 using one-sided envelopes on Laguerre tail
lobes.  This note turns that theorem into an interval-certificate schema.

It is a verification format, not a proof of A1.  Its role is to make the
tail-lobe route falsifiable and auditable: every numerical or analytic
certificate must provide the exact lobe roots, oriented envelope bounds,
and final margin comparison recorded below.

## Tail lobe partition

Fix \(n\ge8\).  Put
\[
  K_n(u)=e^{-u}L_{n-1}^{(2)}(u),
  \qquad
  E(e^u)=\psi(e^u)-e^u.
\]
Let
\[
  T_n=\xi_{n,0}<\xi_{n,1}<\cdots<\xi_{n,J_n}<\xi_{n,J_n+1}=\infty
\]
be the ordered tail partition obtained by inserting exactly those positive
zeros of \(L_{n-1}^{(2)}\) that are \(>T_n\).  On each lobe
\[
  J_{n,j}=[\xi_{n,j},\xi_{n,j+1}]
\]
the sign
\[
  \sigma_{n,j}=\operatorname{sgn}K_n(u)
\]
is constant in the interior.

The compact tail functional is
\[
\boxed{
  I_n(T_n)=
  \sum_j
  \sigma_{n,j}
  \int_{J_{n,j}}E(e^u)|K_n(u)|\,du .
}
\tag{1}
\]

## Certificate data

A rigorous one-index lobe certificate consists of the following data.

1. Root intervals
   \[
     \xi_{n,j}\in[\xi_{n,j}^-,\xi_{n,j}^+]
   \]
   isolating every zero of \(L_{n-1}^{(2)}\) in \([T_n,\infty)\), with a
   proof that no zero is omitted.

2. Lobe weights
   \[
   \boxed{
     W_{n,j}^- \le
     \int_{J_{n,j}}|K_n(u)|\,du
     \le W_{n,j}^+ .
   }
   \tag{2}
   \]

3. One-sided Chebyshev-error envelopes with the correct orientation:
   \[
   \boxed{
     E(e^u)\ge L_{n,j}^-
     \qquad(u\in J_{n,j},\ \sigma_{n,j}=+1),
   }
   \tag{3}
   \]
   and
   \[
   \boxed{
     E(e^u)\le U_{n,j}^+
     \qquad(u\in J_{n,j},\ \sigma_{n,j}=-1).
   }
   \tag{4}
   \]
   The bounds may be functions instead of constants.  In that case replace
   the constant products below by rigorous interval enclosures of the
   corresponding weighted integrals.

4. Rigorous intervals for the margin data
   \[
     A_n\in[A_n^-,A_n^+],
     \qquad
     d_n\in[d_n^-,d_n^+].
   \]

## Certified lower bound

For constant lobe envelopes, define
\[
\boxed{
  \mathcal L_n^-
  =
  \sum_{\sigma_{n,j}=+1} L_{n,j}^-\,W_{n,j}^{\epsilon(L_{n,j}^-)}
  -
  \sum_{\sigma_{n,j}=-1} U_{n,j}^+\,W_{n,j}^{\epsilon(U_{n,j}^+)},
}
\tag{5}
\]
where
\[
  W_{n,j}^{\epsilon(c)}
  =
  \begin{cases}
    W_{n,j}^-,&c\ge0,\\
    W_{n,j}^+,&c<0.
  \end{cases}
\]
This sign convention is the interval-safe way to multiply a possibly
signed constant by a positive weight.

Then (1)--(4) imply
\[
\boxed{
  I_n(T_n)\ge \mathcal L_n^-.
}
\tag{6}
\]

Indeed, on positive lobes the lower envelope gives a lower bound directly.
On negative lobes,
\[
  -\int_{J_{n,j}}E(e^u)|K_n(u)|\,du
  \ge
  -U_{n,j}^+\int_{J_{n,j}}|K_n(u)|\,du,
\]
and the interval-safe choice of \(W^\epsilon\) preserves the lower
direction.

## A1 comparison

The certificate closes compact A1 at the index \(n\) if
\[
\boxed{
  \mathcal L_n^-
  \ge
  \left(d_n^+-{1\over4}\right)A_n^{\epsilon(d_n^+-1/4)},
}
\tag{7}
\]
where
\[
  A_n^{\epsilon(c)}
  =
  \begin{cases}
    A_n^+,&c\ge0,\\
    A_n^-,&c<0.
  \end{cases}
\]
Since \(A_n>0\), this is again just interval-safe multiplication.

By `320`, (7) proves
\[
  I_n(T_n)\ge\left(d_n-\frac14\right)A_n,
\]
which is the tail-margin form of compact A1 at \(n\).

## Infinite range use

To close all \(n\ge8\) by this route, one must provide either:

1. certificates of the form above for every \(n\ge8\); or
2. an effective threshold \(N_\infty\) and an analytic theorem proving
   (3)--(7) for all \(n\ge N_\infty\), plus interval certificates for
   every \(8\le n<N_\infty\).

By `277` and `278`, finite samples, cofinal samples, or averaged lobe
certificates do not prove the omitted indices.

## Status

Closed as the interval-certificate schema for the oriented tail-lobe
route.  A1 remains open until such certificates are produced for every
index, or until an effective threshold theorem plus finite remainder is
proved.
