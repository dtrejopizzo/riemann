# A1 fixed-cutoff generating function

## Purpose

This document packages the compact A1 core for all \(n\) into one analytic
function when the cutoff is fixed.  It also records the obstruction: the A1
cutoff supplied by A0 is \(T_n\), depending on \(n\), so ordinary coefficient
positivity of a single fixed-cutoff function does not by itself prove A1.

## Laguerre series

For \(|z|<1\),
\[
  \sum_{n\ge1}L_{n-1}^{(1)}(u)z^n
  =
  {z\over(1-z)^2}
  \exp\!\left(-{uz\over1-z}\right).
\tag{1}
\]

Let
\[
  H(z,u)=
  {z\over(1-z)^2}
  \exp\!\left(-{uz\over1-z}\right).
\]

Since
\[
  f_{n,0}(e^u)=e^{-u}L_{n-1}^{(1)}(u),
\]
one has
\[
  f'_{n,0}(e^u)e^u
  =
  e^{-u}
  \left({d\over du}L_{n-1}^{(1)}(u)-L_{n-1}^{(1)}(u)\right).
\]

Differentiating (1) in \(u\) gives
\[
  \sum_{n\ge1}
  \left({d\over du}L_{n-1}^{(1)}(u)-L_{n-1}^{(1)}(u)\right)z^n
  =
  -{z\over(1-z)^3}
  \exp\!\left(-{uz\over1-z}\right).
\tag{2}
\]

## Fixed-cutoff compact core

For a fixed \(T>0\), define
\[
  K_n(T)
  =
  -n+\int_1^{e^T}(\psi(y)-y)f'_{n,0}(y)\,dy.
\]

Using \(y=e^u\), (2), and
\[
  \sum_{n\ge1}nz^n={z\over(1-z)^2},
\]
one obtains the exact coefficient normal form
\[
  \boxed{
  \sum_{n\ge1}K_n(T)z^n
  =
  -{z\over(1-z)^2}
  -
  {z\over(1-z)^3}
  \int_0^T
  (\psi(e^u)-e^u)e^{-u}
  \exp\!\left(-{uz\over1-z}\right)\,du.
  }
\tag{3}
\]

This is an ordinary holomorphic function in the unit disk for each fixed
finite \(T\).

## Archimedean generating function

Let
\[
  A_n=\lambda_n^{\rm arch}.
\]
With
\[
  c=\gamma+\log(4\pi)
\]
and the phase-102 archimedean split
\[
  A_n
  =
  1-{n\over2}c+
  \sum_{\substack{r\ge1\\ r\ {\rm odd}}}
  \left[
    \left(1-{1\over r}\right)^n-1+{n\over r}
  \right],
\]
the generating function is
\[
\begin{aligned}
  \mathcal A(z)
  &:=
  \sum_{n\ge1}A_n z^n                                      \\
  &=
  {z\over1-z}
  -{c\over2}{z\over(1-z)^2}                                  \\
  &\quad+
  \sum_{\substack{r\ge1\\ r\ {\rm odd}}}
  \left[
    { (1-1/r)z\over 1-(1-1/r)z}
    -{z\over1-z}
    +{1\over r}{z\over(1-z)^2}
  \right].
\end{aligned}
\tag{4}
\]

For \(|z|<1\), the sum over odd \(r\) converges locally normally.  Thus
\(\mathcal A\) is holomorphic in the unit disk.

## Fixed-cutoff A1 coefficient statement

Define
\[
  \mathcal C_T(z)
  =
  \sum_{n\ge1}
  \left(K_n(T)+{3\over4}A_n\right)z^n.
\]

Combining (3) and (4),
\[
  \mathcal C_T(z)
  =
  -{z\over(1-z)^2}
  -
  {z\over(1-z)^3}
  \int_0^T
  (\psi(e^u)-e^u)e^{-u}
  \exp\!\left(-{uz\over1-z}\right)\,du
  +{3\over4}\mathcal A(z).
\tag{5}
\]

For a fixed cutoff \(T\), positivity of the coefficients of
\(\mathcal C_T\) would assert
\[
  K_n(T)+{3\over4}A_n\ge0
  \qquad(n\ge1).
\tag{6}
\]

This is stronger and different from the phase-102 A1 statement unless the
same \(T\) is admissible for the required tail budget for all \(n\ge8\).
A0 does not provide such a universal finite cutoff; it provides \(T_n\) after
\(n\) is fixed.

## Moving-cutoff obstruction

The actual A1 coefficients are
\[
  K_n(T_n)+{3\over4}A_n.
\]

Because \(T_n\) depends on \(n\), these numbers are not the Taylor
coefficients of one fixed function \(\mathcal C_T\).  Therefore a proof of
ordinary coefficient positivity for a fixed \(T\) does not close A1 unless it
also proves one of the following:

1. there is a universal admissible cutoff \(T\) for all \(n\ge8\);
2. coefficient positivity is uniform for all \(T\) in the admissible range;
3. the moving cutoff sequence \(T_n\) is encoded by a new positive transform;
4. the tail is handled by a separate one-sided theorem.

The first item is unavailable from the current A0 theorem because the
Laguerre degree grows with \(n\).  The second and third items are new
positivity theorems.  The fourth is exactly the one-sided tail gate.

## Relation to Pick/Stieltjes positivity

The full Li generating function
\[
  {d\over dz}\log\xi\!\left({1\over1-z}\right)
  =
  \sum_{n\ge1}\lambda_n z^{n-1}
\]
has nonnegative coefficients exactly when Omega7 holds.  A Pick/Stieltjes
proof would construct this positivity before reading off the zeros.

The fixed-cutoff function (5) is a compact analogue of that transform, but
the moving cutoff prevents direct replacement of the full Li positivity
problem by a single fixed compact coefficient problem.

## Status

The fixed-cutoff generating function is closed.  It gives a useful analytic
normal form for discovery, but it does not prove A1.  To become a closure
route it must be paired with uniform fixed-cutoff positivity, a positive
moving-cutoff transform, or the one-sided tail theorem.
