# Inductive forcing generator

## Purpose

`159_INDUCTIVE_FORCING_CERTIFICATE_SCHEMA.md` gives pointwise finite
certificates for the recurrence forcing.  This note writes the same forcing
in generating-function form.

The key point is that the prime moment \(M_n(T)\) is obtained by applying
the Euler operator \(w\partial_w\) to the compact integral generator, where
\[
  w={z\over1-z}.
\]

## Compact integral generator

For fixed \(T\), define
\[
  I_n(T)=\int_0^T E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
\]

The generating function is
\[
  \mathcal I_T(z)
  =
  \sum_{n\ge1}I_n(T)z^n
  =
  {z\over(1-z)^3}
  \int_0^T E(e^u)\exp\!\left(-{u\over1-z}\right)\,du.
\tag{1}
\]

Equivalently, with \(w=z/(1-z)\),
\[
  \mathcal I_T(z)
  =
  {z\over(1-z)^3}
  \int_0^T E(e^u)e^{-u}e^{-uw}\,du.
\tag{2}
\]

## Moment generator

The recurrence forcing contains
\[
  M_n(T)=\int_0^T u\,E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
\tag{3}
\]

Using
\[
  w\partial_w e^{-uw}=-uwe^{-uw},
\]
equation (2) gives
\[
\boxed{
  \sum_{n\ge1}M_n(T)z^n
  =
  -{z\over(1-z)^3}
  \left(w\partial_w\right)
  \int_0^T E(e^u)e^{-u}e^{-uw}\,du.
}
\tag{4}
\]

Since \(w=z/(1-z)\), this can also be written as
\[
\boxed{
  \mathcal M_T(z)
  :=
  \sum_{n\ge1}M_n(T)z^n
  =
  {z\over(1-z)^3}
  \int_0^T u\,E(e^u)e^{-u/(1-z)}\,du.
}
\tag{5}
\]

Thus the moment is a differentiated compact generator.  It is not a new
kind of arithmetic object.

## Archimedean forcing generator

Let
\[
  \mathcal A(z)=\sum_{n\ge1}A_n z^n,
  \qquad A_n=\lambda_n^{\rm arch}.
\]

Define
\[
  D_n^{\rm arch}
  =
  nA_{n+1}-(2n+1)A_n+(n+1)A_{n-1}.
\tag{6}
\]

The ordinary generating function of \(D_n^{\rm arch}\) is obtained by
index shifting.  For \(n\ge2\),
\[
\boxed{
  \mathcal D(z)
  :=
  \sum_{n\ge2}D_n^{\rm arch}z^n
  =
  (1-z)^2\mathcal A'(z)
  +
  \left(2z-1-{1\over z}\right)\mathcal A(z)
  -
  D_1^{\rm edge}z,
}
\tag{7}
\]
where \(D_1^{\rm edge}\) is the harmless edge correction required by the
chosen starting convention.  For the induction range \(n\ge8\), this edge
term is irrelevant.

Indeed,
\[
  \sum_{n\ge1}nA_{n+1}z^n=\mathcal A'(z)-{\mathcal A(z)\over z},
\]
\[
  \sum_{n\ge1}(2n+1)A_nz^n=2z\mathcal A'(z)+\mathcal A(z),
\]
and
\[
  \sum_{n\ge1}(n+1)A_{n-1}z^n
  =
  z^2\mathcal A'(z)+2z\mathcal A(z)
\]
if \(A_0=0\).

Equivalently, one may use the explicit coefficient formula from
`157_ARCHIMEDEAN_FORCING_AUDIT.md`.

## Forcing generator

The forcing is
\[
  F_n(T)=M_n(T)+1+{3\over4}D_n^{\rm arch}.
\tag{8}
\]

Therefore, for \(n\ge8\), its generating function is the tail of
\[
\boxed{
  \mathcal F_T(z)
  =
  \mathcal M_T(z)
  +
  {z\over1-z}
  +
  {3\over4}\mathcal D(z),
}
\tag{9}
\]
after discarding the finite edge coefficients \(n<8\).

The first-difference induction formula
\[
  {\Delta_{n+1}(T)\over n+1}
  =
  {\Delta_n(T)\over n}
  +
  {F_n(T)\over n(n+1)}
\tag{10}
\]
is therefore controlled by weighted partial sums of the coefficients of
\(\mathcal F_T\).

## Induction target in generator form

A fixed-cutoff induction proof must show
\[
  {\Delta_8(T)\over8}
  +
  \sum_{k=8}^{n-1}{[z^k]\mathcal F_T(z)\over k(k+1)}
  \ge0
  \qquad(n\ge9).
\tag{11}
\]

This is a coefficient-sum positivity theorem for \(\mathcal F_T\).

On the A0 diagonal, one must again combine it with the cutoff-transfer
theorem, because \(\mathcal F_T\) is a fixed-cutoff generator.

## Status

Closed as a forcing-generator normal form.  A1 remains open.

The induction route is now a coefficient-sum positivity problem for
\(\mathcal F_T\), plus moving-cutoff transfer.
