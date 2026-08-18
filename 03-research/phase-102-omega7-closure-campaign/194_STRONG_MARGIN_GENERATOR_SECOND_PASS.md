# Strong margin generator second pass

## Purpose

`122_STRONG_MARGIN_REDUCTION.md` isolates the strong margin
\[
  \lambda_n\ge {1\over2}\lambda_n^{\rm arch}
  \qquad(n\ge8)
\tag{1}
\]
as a sufficient bridge from A0 to compact A1.  `150` writes the exact
tail/compact generator identity, while `189` and `192` show that global
Toeplitz/Schoenberg positivity gives Li positivity but not the compact A1
budget.

This note records the exact generator for the strong margin and separates
what global Toeplitz/Schoenberg contributes from the extra quantitative
margin still missing.

## Strong-margin generator

Let
\[
  \mathcal L(z)=\sum_{n\ge1}\lambda_nz^n,
  \qquad
  \mathcal A(z)=\sum_{n\ge1}\lambda_n^{\rm arch}z^n.
\]

Define the strong-margin generator
\[
\boxed{
  \mathcal M_{\rm SM}(z)
  =
  \mathcal L(z)-{1\over2}\mathcal A(z).
}
\tag{2}
\]

Then (1) is exactly
\[
\boxed{
  [z^n]\mathcal M_{\rm SM}(z)\ge0
  \qquad(n\ge8).
}
\tag{3}
\]

Using the Euler--Gamma split from `140` and `141`,
\[
  \mathcal L(z)
  =
  \mathcal A(z)
  -
  {z\over(1-z)^2}
  -
  {z\over(1-z)^3}
  \int_0^\infty
  E(e^u)\exp\!\left(-{u\over1-z}\right)\,du,
\tag{4}
\]
so
\[
\boxed{
  \mathcal M_{\rm SM}(z)
  =
  {1\over2}\mathcal A(z)
  -
  {z\over(1-z)^2}
  -
  {z\over(1-z)^3}
  \int_0^\infty
  E(e^u)\exp\!\left(-{u\over1-z}\right)\,du.
}
\tag{5}
\]

Coefficientwise,
\[
\boxed{
  [z^n]\mathcal M_{\rm SM}
  =
  {1\over2}\lambda_n^{\rm arch}
  +
  \lambda_n^{\rm prime}.
}
\tag{6}
\]

Thus the strong margin is the signed prime lower bound
\[
\boxed{
  \lambda_n^{\rm prime}\ge
  -{1\over2}\lambda_n^{\rm arch}
  \qquad(n\ge8),
}
\tag{7}
\]
as in `122`.

## Relation to compact A1

From `150`,
\[
  C_n(T_n)
  =
  \lambda_n
  -
  {1\over4}\lambda_n^{\rm arch}
  -
  R_n(T_n).
\tag{8}
\]

Write
\[
  M_n^{\rm SM}
  =
  \lambda_n-{1\over2}\lambda_n^{\rm arch}
  =
  [z^n]\mathcal M_{\rm SM}.
\tag{9}
\]

Then
\[
\boxed{
  C_n(T_n)
  =
  M_n^{\rm SM}
  +
  \left({1\over4}\lambda_n^{\rm arch}-R_n(T_n)\right).
}
\tag{10}
\]

The A0 upper-tail budget gives
\[
  R_n(T_n)\le {1\over4}\lambda_n^{\rm arch}.
\tag{11}
\]

Therefore
\[
\boxed{
  [z^n]\mathcal M_{\rm SM}\ge0
  \quad+\quad
  R_n(T_n)\le {1\over4}\lambda_n^{\rm arch}
  \Longrightarrow
  C_n(T_n)\ge0.
}
\tag{12}
\]

This is the precise generator bridge from strong margin to A1.

## Toeplitz/Schoenberg contribution

The global Toeplitz/Schoenberg route gives a positive kernel
\[
  K(j,k)=\lambda_j+\lambda_k-\lambda_{|j-k|}
\tag{13}
\]
or equivalently positive-definite second differences.  Taking the diagonal,
\[
  K(n,n)=2\lambda_n\ge0.
\tag{14}
\]

Thus global positivity contributes exactly
\[
  \lambda_n\ge0.
\tag{15}
\]

In the Toeplitz energy normalization of `164`,
\[
  \lambda_n={1\over2}Q_n(1-z^n),
\tag{16}
\]
so (15) is
\[
  Q_n(1-z^n)\ge0.
\tag{17}
\]

The strong margin asks for the stronger quantitative inequality
\[
\boxed{
  Q_n(1-z^n)\ge \lambda_n^{\rm arch}
  \qquad(n\ge8).
}
\tag{18}
\]

Equivalently,
\[
  K(n,n)\ge \lambda_n^{\rm arch}.
\tag{19}
\]

So the global Toeplitz/Schoenberg theorem supplies the sign of the diagonal
energy, but not its archimedean lower margin.

## Formal no-go: positivity data do not imply margin data

The implication
\[
  K\ge0
  \quad\Longrightarrow\quad
  K(n,n)\ge \lambda_n^{\rm arch}
\tag{20}
\]
is false as a matter of positive-kernel algebra.

Indeed, fix any positive sequence \(A_n>0\).  The zero kernel
\[
  K_0(j,k)=0
\tag{21}
\]
is positive semidefinite, but
\[
  K_0(n,n)=0<A_n.
\tag{22}
\]

More generally, for any \(0<\eta<1\), a positive kernel with
\[
  K_\eta(n,n)=\eta A_n
\tag{23}
\]
at a selected diagonal still fails the margin at that diagonal.  Positive
semidefiniteness controls signs of quadratic forms; it does not set a
numerical scale relative to an external sequence \(A_n\).

Therefore any proof of (18) must import a quantitative normalization or
comparison theorem that ties the Toeplitz energy scale to the archimedean
sequence.  Bare Herglotz positivity, Carathéodory positivity, Schoenberg
positivity, or RH/Li positivity cannot supply this margin by formal
algebra.

This is a no-go for proof data, not a counterexample to zeta.  It says that
the global positivity theorem must be strengthened by an explicit
archimedean margin theorem if it is to close compact A1 through (12).

## Equivalent missing theorems

The strong-margin route can now be stated in any of the following equivalent
forms.

### Coefficient form

\[
  [z^n]\left(\mathcal L-{1\over2}\mathcal A\right)\ge0
  \qquad(n\ge8).
\tag{24}
\]

### Prime-pole form

\[
  \lambda_n^{\rm prime}
  +
  {1\over2}\lambda_n^{\rm arch}
  \ge0
  \qquad(n\ge8).
\tag{25}
\]

### Toeplitz Li-test margin

\[
  Q_n(1-z^n)\ge \lambda_n^{\rm arch}
  \qquad(n\ge8).
\tag{26}
\]

### Schoenberg diagonal margin

\[
  K(n,n)\ge \lambda_n^{\rm arch}
  \qquad(n\ge8).
\tag{27}
\]

### Schur innovation sufficient strengthening

Using `164`, a stronger sufficient theorem is
\[
  \sigma_n\ge \lambda_n^{\rm arch}
  \qquad(n\ge8),
\tag{28}
\]
where \(\sigma_n\) is the Toeplitz prediction-error energy.  Since
\(\sigma_n\le Q_n(1-z^n)\) is not automatic in the direction needed for all
normalizations, the exact implication must be checked in the chosen
Toeplitz model; in the setup of `164`, \(\sigma_n\ge A_n\) implies
\(Q_n(1-z^n)\ge A_n\) because \(q=1\) is an admissible competitor.

## Status

Closed as a second-pass strong-margin generator audit.  A1 remains open.

The generator
\[
  \mathcal M_{\rm SM}=\mathcal L-\frac12\mathcal A
\]
is the exact object whose coefficients must be nonnegative for \(n\ge8\).
Global Toeplitz/Schoenberg positivity supplies \(\lambda_n\ge0\), but the
compact A1 bridge requires the quantitative margin
\(\lambda_n\ge\frac12\lambda_n^{\rm arch}\), or an equivalent Toeplitz,
Schoenberg, prime-pole or Schur innovation margin theorem.
