# Inductive forcing certificate schema

## Purpose

`156_A1_LAGUERRE_N_RECURRENCE_GATE.md` reduces an induction route to lower
bounds for the forcing
\[
  F_n(T)=M_n(T)+1+{3\over4}D_n^{\rm arch}.
\]
`157_ARCHIMEDEAN_FORCING_AUDIT.md` gives the corrected explicit formula for
\(D_n^{\rm arch}\).  This note writes \(F_n(T)\) as an explicit finite
arithmetic certificate for fixed \(n,T\).

This is the induction analogue of
`148_A1_FINITE_ARITHMETIC_CERTIFICATE_SCHEMA.md`.

## Prime moment

The signed prime moment is
\[
  M_n(T)=
  \int_0^T u\,E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
\tag{1}
\]

Write
\[
  L_{n-1}^{(2)}(u)=\sum_{k=0}^{n-1}c_{n,k}u^k,
  \qquad
  c_{n,k}=(-1)^k{1\over k!}\binom{n+1}{n-1-k}.
\tag{2}
\]

Since
\[
  E(e^u)=\psi(e^u)-e^u,
\]
the moment splits as
\[
  M_n(T)=M_n^{\rm pp}(T)+M_n^{\rm pole}(T),
\tag{3}
\]
where
\[
  M_n^{\rm pole}(T)
  =
  -\int_0^T u L_{n-1}^{(2)}(u)\,du
  =
  -\sum_{k=0}^{n-1}c_{n,k}{T^{k+2}\over k+2}.
\tag{4}
\]

For the prime-power part, finite Fubini gives
\[
\begin{aligned}
  M_n^{\rm pp}(T)
  &=
  \int_0^T u e^{-u}L_{n-1}^{(2)}(u)\psi(e^u)\,du\\
  &=
  \sum_{m\le e^T}{\Lambda(m)\over m}
  \int_0^{T-\log m}
  (t+\log m)
  L_{n-1}^{(2)}(t+\log m)e^{-t}\,dt.
\end{aligned}
\tag{5}
\]

Let
\[
  M_q(A)=\int_0^A e^{-t}t^q\,dt
  =
  q!\left(1-e^{-A}\sum_{\ell=0}^q{A^\ell\over\ell!}\right).
\tag{6}
\]

Expanding the polynomial,
\[
\boxed{
\begin{aligned}
  M_n^{\rm pp}(T)
  &=
  \sum_{m\le e^T}{\Lambda(m)\over m}
  \sum_{k=0}^{n-1}c_{n,k}
  \sum_{b=0}^{k}
  \binom{k}{b}(\log m)^{k-b}
  \left[
    M_{b+1}(T-\log m)
    +(\log m)M_b(T-\log m)
  \right].
\end{aligned}
}
\tag{7}
\]

Thus \(M_n(T)\) is a finite explicit prime-power sum plus the elementary
pole polynomial (4).

## Archimedean forcing correction

From `157_ARCHIMEDEAN_FORCING_AUDIT.md`,
\[
  D_n^{\rm arch}
  =
  \sum_{\substack{r\ge1\\ r\ {\rm odd}}}
  \left[
  \left(1-{1\over r}\right)^{n-1}
  \left({1\over r}+{n\over r^2}\right)
  -{1\over r}
  \right].
\tag{8}
\]

This series is explicit and independent of \(T\).  For certificates, one may
split it at an odd \(R\):
\[
  D_n^{\rm arch}=D_{n,\le R}^{\rm arch}+D_{n,>R}^{\rm arch}.
\tag{9}
\]

The finite part is rational:
\[
  D_{n,\le R}^{\rm arch}
  =
  \sum_{\substack{1\le r\le R\\ r\ {\rm odd}}}
  \left[
  \left(1-{1\over r}\right)^{n-1}
  \left({1\over r}+{n\over r^2}\right)
  -{1\over r}
  \right].
\tag{10}
\]

The tail must be bounded with ordinary one-variable estimates.  This is not
an A1 difficulty; it contains no primes and no zeros.

## Forcing certificate

Combining (3), (4), (7), and (8),
\[
\boxed{
  F_n(T)
  =
  M_n^{\rm pp}(T)
  +M_n^{\rm pole}(T)
  +1
  +{3\over4}D_n^{\rm arch}.
}
\tag{11}
\]

The induction gate of `156` requires, for a common cutoff \(T\),
\[
  {\Delta_8(T)\over8}
  +
  \sum_{k=8}^{n-1}{F_k(T)\over k(k+1)}
  \ge0.
\tag{12}
\]

Using (11), this is a finite prime-power certificate plus explicit
archimedean tails.

## Moving diagonal caveat

The certificate (11) is fixed-cutoff.  A1 uses \(T_n\), so an induction proof
must still combine (12) with the cutoff-transfer gates `153` and `154`.

No finite forcing certificate by itself proves A1 on the moving A0 diagonal.

## Status

Closed as a finite forcing certificate schema.  A1 remains open.

The induction route is now reduced to proving a uniform signed lower bound
for the explicit forcing certificates (11), together with signed
cutoff-transfer control.
