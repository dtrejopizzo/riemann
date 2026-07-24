# Mellin coborder normal form for A1

## Purpose

This document writes the A1 core as an exact Mellin object. The goal is to
test the surviving Mellin-coborder route without changing the target.

The output is a normal form, not a proof of A1.

## Compact core

For \(n\ge8\), let \(T=T_n\) be a cutoff satisfying A0, put
\[
  L_n(u)=L_{n-1}^{(1)}(u),
  \qquad
  X=e^T,
\]
and define
\[
  C_n(T)
  =
  -n+\int_1^X(\psi(y)-y)f'_{n,0}(y)\,dy
  +{3\over4}\lambda_n^{\rm arch}.
\]

Integration by parts gives the finite identity
\[
\begin{aligned}
 C_n(T)
 &=
 -n+(\psi(X)-X)X^{-1}L_n(T)        \\
 &\quad
 -\sum_{m\le X}{\Lambda(m)\over m}L_n(\log m)
 +\int_0^T L_n(u)\,du
 +{3\over4}\lambda_n^{\rm arch}.
\end{aligned}
\tag{1}
\]

Thus every term is finite. No polar or prime divergence remains.

## Truncated Mellin kernel

Define the entire kernel
\[
  P_{n,T}(s)
  =
  \int_0^T e^{-su}L_n(u)\,du .
\]

Since
\[
  L_n(u)
  =
  \sum_{j=0}^{n-1}
  (-1)^j {n\choose j+1}{u^j\over j!},
\]
one has the explicit finite formula
\[
  P_{n,T}(s)
  =
  \sum_{j=0}^{n-1}
  (-1)^j {n\choose j+1}{1\over j!}
  \int_0^T e^{-su}u^j\,du .
\]

For \(s\ne0\),
\[
  \int_0^T e^{-su}u^j\,du
  =
  {j!\over s^{j+1}}
  \left[
    1-e^{-sT}\sum_{a=0}^j{(sT)^a\over a!}
  \right],
\]
and at \(s=0\) the value is \(T^{j+1}/(j+1)\).

## Perron form of the prime block

Let \(c>0\). In the usual symmetric Perron sense, with the endpoint convention
chosen consistently with the Stieltjes integral,
\[
  \sum_{m\le X}{\Lambda(m)\over m}L_n(\log m)
  =
  {1\over2\pi i}
  \int_{c-i\infty}^{c+i\infty}
  -{\zeta'\over\zeta}(1+s)\,P_{n,T}(s)\,ds .
\tag{2}
\]

The proof is immediate from
\[
  -{\zeta'\over\zeta}(1+s)
  =
  \sum_{m\ge2}{\Lambda(m)\over m}e^{-s\log m}
  \qquad(\Re s>0)
\]
and Mellin inversion of the truncated kernel.

Combining (1) and (2) gives an exact Mellin normal form for A1:
\[
\begin{aligned}
 C_n(T)
 &=
 -n+(\psi(X)-X)X^{-1}L_n(T)
 +P_{n,T}(0)
 +{3\over4}\lambda_n^{\rm arch}        \\
 &\quad
 -{1\over2\pi i}
  \int_{c-i\infty}^{c+i\infty}
  -{\zeta'\over\zeta}(1+s)\,P_{n,T}(s)\,ds .
\end{aligned}
\tag{3}
\]

Therefore A1 is equivalent to the nonnegativity of the right hand side of
(3) for all \(n\ge8\).

## Symmetrized completed form

To use the functional equation one replaces
\[
  -{\zeta'\over\zeta}(1+s)
\]
by the logarithmic derivative of the completed function. The relation
\[
  {\xi'\over\xi}(1+s)
  =
  {1\over 1+s}+{1\over s}
  -{1\over2}\log\pi
  +{1\over2}\psi\!\left({1+s\over2}\right)
  +{\zeta'\over\zeta}(1+s)
\]
shows that the prime block, the polar block and the Gamma block can be
recombined exactly.

After this recombination, a contour shift crosses the residues of
\[
  {\xi'\over\xi}(1+s),
\]
namely the zeros of \(\xi\) written in the shifted coordinate \(s=\rho-1\).
The contribution has the schematic form
\[
  \sum_\rho P_{n,T}(\rho-1)
\]
plus explicitly computable endpoint and Gamma residues.

## Obstruction found

The Mellin normal form is exact, but it is not yet a positivity theorem.
The expected symmetry \(s\mapsto -s\), inherited from
\(\xi(s)=\xi(1-s)\), sends zero residues to their paired partners. It produces
a nonnegative form immediately if the corresponding Li variables have modulus
one. That is precisely the zero-line condition.

Thus the Mellin route cannot close A1 merely by contour shifting. It must
prove an additional arithmetic positivity statement for the symmetrized
completed kernel before interpreting the residues as lying on the line.

## Live theorem left by the Mellin route

The exact live theorem is:

For every \(n\ge8\), the completed Mellin normal form (3), after Gamma-pole
recombination and functional-equation symmetrization, is nonnegative:
\[
  C_n(T_n)\ge0.
\]

The proof must obtain this sign from the Euler product, Gamma factor and
functional equation before using the zero-side interpretation.

## Status

The Mellin-coborder route is reduced to a single positivity theorem for the
symmetrized completed kernel. The contour identity itself is closed; the sign
is open and is exactly A1.
