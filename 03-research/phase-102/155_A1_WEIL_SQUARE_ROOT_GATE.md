# A1 Weil square-root gate

## Purpose

The Mellin and Weil/Herglotz reductions show that A1 can be viewed as a
restricted Weil positivity problem.  This note isolates the missing
``square-root'' theorem: the compact A1 test must be represented as a
positive autocorrelation before the zero-side interpretation is used.

The conclusion is that a contour formula is not enough.  A Weil proof must
construct a positive factorization of the A1 test from Euler--Gamma data.

## Exact Mellin test

For \(n\ge8\) and cutoff \(T\), put
\[
  L_n(u)=L_{n-1}^{(1)}(u),
  \qquad
  P_{n,T}(s)=\int_0^T e^{-su}L_n(u)\,du.
\tag{1}
\]

`113_MELLIN_COBORDER_NORMAL_FORM.md` gives the exact finite identity
\[
\begin{aligned}
 C_n(T)
 &=
 -n+E(e^T)e^{-T}L_n(T)
 +P_{n,T}(0)
 +{3\over4}\lambda_n^{\rm arch}        \\
 &\quad
 -{1\over2\pi i}
  \int_{c-i\infty}^{c+i\infty}
  -{\zeta'\over\zeta}(1+s)P_{n,T}(s)\,ds ,
\end{aligned}
\tag{2}
\]
with \(c>0\).

Thus A1 is the assertion
\[
  C_n(T_n)\ge0.
\tag{3}
\]

## Completed Weil form

Replacing \(-\zeta'/\zeta\) by the completed logarithmic derivative
\(\xi'/\xi\) moves the pole, endpoint, and Gamma terms into an explicit
completed remainder.  Abstractly, there is an exact identity of the form
\[
  C_n(T)
  =
  G_{n,T}^{\rm exp}
  +
  {1\over2\pi i}
  \int_{\Gamma}
  {\xi'\over\xi}(1+s)P_{n,T}(s)\,ds,
\tag{4}
\]
where \(G_{n,T}^{\rm exp}\) is made only of the explicit pole, Gamma and
endpoint residues already present in (2).

Shifting the contour in (4) produces a zero-side expression
\[
  C_n(T)
  =
  G_{n,T}^{\rm exp}
  -
  \sum_\rho P_{n,T}(\rho-1)
  +
  \hbox{paired residue terms}.
\tag{5}
\]

Equation (5) is a Weil-type explicit formula for the A1 test.  It is not a
positivity theorem.

## Square-root theorem needed

A genuine Weil proof of A1 must construct, for each \(n\ge8\), an admissible
test \(g_{n,T_n}\) such that the completed A1 functional is represented as a
positive autocorrelation:
\[
  C_n(T_n)
  =
  Q_\xi(g_{n,T_n},g_{n,T_n})
  +
  H_{n,T_n},
\tag{6}
\]
where:

1. \(Q_\xi(g,g)\) is the completed Weil quadratic form attached to \(\xi\);
2. \(H_{n,T_n}\ge0\) is an explicit harmless residue or archimedean margin;
3. the identity (6) is proved from Euler--Gamma data before assuming any
   zero support statement;
4. the test \(g_{n,T_n}\) reproduces exactly the compact A1 kernel,
   including the cutoff \(T_n\) and the \({3\over4}\lambda_n^{\rm arch}\)
   budget.

Then positivity of \(Q_\xi(g,g)\) would imply A1.

The missing theorem is precisely the construction of this square root.  It
is stronger than writing down the linear Mellin functional (2).

## Why the linear test is not automatically positive

The compact kernel in collapsed form is
\[
  -e^{-u}L_{n-1}^{(2)}(u).
\tag{7}
\]
It changes sign \(n-1\) times on the positive axis.  A positive
autocorrelation may have oscillatory linear representatives, but the
positivity then comes from a hidden square:
\[
  \widehat{k}(\tau)=|\widehat{g}(\tau)|^2
\tag{8}
\]
or from a positive boundary measure.  Neither is supplied by (7).

Therefore the following implication is invalid:
\[
  \hbox{A1 has an explicit formula}
  \quad\Longrightarrow\quad
  \hbox{A1 is positive}.
\]

The valid implication is:
\[
  \hbox{A1 has an explicit formula}
  +
  \hbox{positive square-root factorization}
  \quad\Longrightarrow\quad
  \hbox{A1 is positive}.
\]

## Relation to other gates

The square-root theorem is equivalent in role to the existing positive gates:

- positive boundary measure;
- Hermite--Biehler/de Branges construction;
- infinite Pick/Stieltjes positivity;
- non-tautological bordered-current coercivity;
- symmetrized Mellin boundary positivity.

All of these are ways of proving that the completed A1 test is a positive
quadratic object rather than only a signed linear explicit formula.

## Status

Closed as a gate.  The exact Mellin test is known, but its positive
square-root factorization is open.

A1 remains open until such a factorization, or one of the equivalent global
positivity theorems, is proved from Euler--Gamma data.
