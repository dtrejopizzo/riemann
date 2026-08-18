# A1 tail remainder generator identity

## Purpose

`149_MOVING_DIAGONAL_A1_GENERATOR.md` gives the fixed-cutoff compact A1
generator.  This note relates that generator to the full Li generator and
the A0 tail generator.

The result is an exact sign bookkeeping identity:
\[
  C_n(T)=\lambda_n-{1\over4}\lambda_n^{\rm arch}-R_n(T),
\]
where \(R_n(T)\) is the paired tail.  This is the generator version of the
strong-margin and one-sided-tail gates.

## Definitions

Let
\[
  \mathcal L(z)=\sum_{n\ge1}\lambda_n z^n
\]
be the full Euler--Gamma Li generator, and let
\[
  \mathcal A(z)=\sum_{n\ge1}\lambda_n^{\rm arch}z^n.
\]

For fixed \(T\), define the compact A1 generator
\[
  \mathcal C_T(z)
  =
  -{z\over(1-z)^2}
  +{3\over4}\mathcal A(z)
  -
  {z\over(1-z)^3}
  \int_0^T
  E(e^u)\exp\!\left(-{u\over1-z}\right)\,du.
\tag{1}
\]

Thus
\[
  [z^n]\mathcal C_T(z)=C_n(T)
  =
  -n-\int_0^T E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  +{3\over4}\lambda_n^{\rm arch}.
\tag{2}
\]

The full Li generator from `140` and `141` is
\[
  \mathcal L(z)
  =
  \mathcal A(z)
  -
  {z\over(1-z)^2}
  -
  {z\over(1-z)^3}
  \int_0^\infty
  E(e^u)\exp\!\left(-{u\over1-z}\right)\,du.
\tag{3}
\]

## Tail generator

Define the signed tail generator
\[
  \mathcal R_T(z)
  =
  -{z\over(1-z)^3}
  \int_T^\infty
  E(e^u)\exp\!\left(-{u\over1-z}\right)\,du.
\tag{4}
\]

Its coefficients are the paired tails:
\[
  [z^n]\mathcal R_T(z)
  =
  R_n(T)
  =
  -\int_T^\infty
  E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
\tag{5}
\]

This sign convention matches the phase convention
\[
  \lambda_n^{\rm prime}=K_n(T)+R_n(T),
\]
with
\[
  K_n(T)=-n-\int_0^T E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du.
\]

## Exact generator identity

Subtracting (3) from (1) gives
\[
\begin{aligned}
  \mathcal C_T(z)
  &=
  \mathcal L(z)-{1\over4}\mathcal A(z)-\mathcal R_T(z).
\end{aligned}
\tag{6}
\]

Equivalently,
\[
  \boxed{
  \mathcal C_T
  =
  \mathcal L
  -
  {1\over4}\mathcal A
  -
  \mathcal R_T .
  }
\tag{7}
\]

Coefficientwise,
\[
  \boxed{
  C_n(T)
  =
  \lambda_n
  -
  {1\over4}\lambda_n^{\rm arch}
  -
  R_n(T).
  }
\tag{8}
\]

This is the exact algebra behind the A1 margin gate.

## Consequences

A1 for the A0 cutoff \(T_n\) is
\[
  C_n(T_n)\ge0.
\]
By (8), this is equivalent to
\[
  \lambda_n\ge R_n(T_n)+{1\over4}\lambda_n^{\rm arch}.
\tag{9}
\]

The A0 theorem gives only
\[
  |R_n(T_n)|\le {1\over4}\lambda_n^{\rm arch}.
\tag{10}
\]

Therefore A0 alone gives the sufficient implication
\[
  \lambda_n\ge {1\over2}\lambda_n^{\rm arch}
  \quad\Longrightarrow\quad
  C_n(T_n)\ge0,
\tag{11}
\]
which is the strong-margin gate.

Alternatively, A1 follows from the one-sided tail theorem
\[
  R_n(T_n)\le \lambda_n-{1\over4}\lambda_n^{\rm arch}.
\tag{12}
\]

The latter is tautological unless the right side is controlled by an
independent Euler--Gamma sign theorem.  The generator identity makes clear
where that theorem must enter: it must compare the Li generator with the
tail generator without assuming coefficient positivity of \(\mathcal L\).

## Moving diagonal form

For the actual A0 cutoffs,
\[
  [z^n]\mathcal C_{T_n}(z)
  =
  [z^n]\left(
  \mathcal L(z)
  -{1\over4}\mathcal A(z)
  -\mathcal R_{T_n}(z)
  \right).
\tag{13}
\]

Thus every moving-diagonal proof must establish
\[
  [z^n]\mathcal L
  \ge
  {1\over4}[z^n]\mathcal A
  +
  [z^n]\mathcal R_{T_n}
  \qquad(n\ge8).
\tag{14}
\]

This is not a simplification of A1; it is the exact generator-level split
between the full Li coefficient and the signed A0 tail.

## Status

Closed as a sign bookkeeping identity.  It confirms that:

1. A0 alone cannot close A1;
2. the strong-margin theorem closes A1;
3. a genuinely one-sided tail theorem closes A1;
4. the moving-diagonal generator of `149` is exactly the Li generator minus
   the archimedean quarter and the signed tail generator.

A1 remains open until one of those signed theorems is proved.
