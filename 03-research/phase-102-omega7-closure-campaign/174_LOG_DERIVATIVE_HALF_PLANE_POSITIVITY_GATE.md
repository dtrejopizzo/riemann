# Log-derivative half-plane positivity gate

## Purpose

`172_SCHOENBERG_INCREMENT_TOEPLITZ_GATE.md` introduced the second-difference
sequence
\[
  g_0=2\lambda_1,\qquad
  g_m=\lambda_{m+1}-2\lambda_m+\lambda_{m-1}.
\]

This note records the key simplification:

\[
  [g_{|j-k|}]\ge0\ \hbox{for all finite Toeplitz blocks}
  \quad\Longleftrightarrow\quad
  \Re{\xi'\over\xi}(s)\ge0\quad(\Re s>1/2).
\]

Thus the weighted-divisor route is exactly a half-plane Carathéodory
positivity theorem for the completed logarithmic derivative.

This is not a proof of A1.  It is a sharper equivalent global target.

## Disk-to-half-plane coordinate

The Li disk coordinate is
\[
  s={1\over1-z},
  \qquad
  z=1-{1\over s}.
\]

Then
\[
  |z|<1
  \Longleftrightarrow
  |s-1|<|s|
  \Longleftrightarrow
  \Re s>{1\over2}.
\tag{1}
\]

Thus the unit disk is exactly the right half of the critical strip in the
\(s\)-coordinate.

## Increment generator cancellation

From `140_EULER_GAMMA_LI_GENERATOR.md`,
\[
  \mathcal L(z)
  =
  {z\over(1-z)^2}
  {\xi'\over\xi}\!\left({1\over1-z}\right).
\tag{2}
\]

From `172`,
\[
  \mathcal G_+(z)
  =
  g_0+\sum_{m\ge1}g_m z^m
  =
  \lambda_1+{(1-z)^2\over z}\mathcal L(z).
\tag{3}
\]

Combining (2) and (3),
\[
  \boxed{
  \mathcal G_+(z)
  =
  \lambda_1+
  {\xi'\over\xi}\!\left({1\over1-z}\right).
  }
\tag{4}
\]

Since
\[
  \lambda_1={\xi'\over\xi}(1),
\tag{5}
\]
the constant term is
\[
  \mathcal G_+(0)=2\lambda_1=g_0.
\]

The Carathéodory function attached to the Hermitian Toeplitz sequence
\((g_{|m|})\) is
\[
\begin{aligned}
  H_g(z)
  &=
  g_0+2\sum_{m\ge1}g_m z^m\\
  &=
  2\mathcal G_+(z)-g_0\\
  &=
  2{\xi'\over\xi}\!\left({1\over1-z}\right).
\end{aligned}
\tag{6}
\]

Therefore Toeplitz positivity of \(g\) is equivalent to
\[
  \boxed{
  \Re{\xi'\over\xi}\!\left({1\over1-z}\right)\ge0
  \qquad(|z|<1).
  }
\tag{7}
\]

By (1), this is
\[
  \boxed{
  \Re{\xi'\over\xi}(s)\ge0
  \qquad(\Re s>1/2).
  }
\tag{8}
\]

## Support consequence

If (8) holds, then \(\xi'/\xi\) is a Carathéodory/Herglotz function in the
half-plane \(\Re s>1/2\).  A function with nonnegative real part cannot have
a non-removable pole in the domain: near a pole, the leading principal part
has real part of both signs on small circles.

Therefore (8) rules out zeros of \(\xi\) in
\[
  \Re s>{1\over2}.
\]

The functional equation for \(\xi\) then rules out zeros in
\[
  \Re s<{1\over2}.
\]

Thus (8) implies RH and hence Omega7 by Li.

Conversely, on the critical-line model, `173` shows that the same
logarithmic derivative has a positive weighted boundary-measure
interpretation.  In that model, (8) is exactly the Poisson positivity of the
finite weighted zero-divisor measure.

## Relation to A1

The half-plane positivity theorem closes Omega7 globally through RH/Li.  It
does not by itself supply the compact A1 budget
\[
  C_n(T_n)\ge0
\]
unless one also proves the stronger archimedean margin in the A0/A1
decomposition.

Thus there are two routes:

1. prove (8), then close Omega7 by RH and Li;
2. prove a stronger margin version of the Schoenberg or Toeplitz kernel,
   then close compact A1 after A0.

Route (1) is enough for the project goal.  Route (2) is a stricter
compatibility with the existing compact-core split.

## Why this is not automatic

Using the product expansion of \(\xi\), the logarithmic derivative has poles
at the zeros of \(\xi\).  If any zero lies in \(\Re s>1/2\), then (8) fails
locally by the pole sign argument.

Therefore (8) is not a soft consequence of the Euler product in
\(\Re s>1\).  It is an RH-strength positivity-preserving continuation from
the Euler--Gamma data to the full half-plane.

Equivalently, coefficientwise positivity of the second differences \(g_m\)
is not enough; the theorem is real-part positivity of the completed
logarithmic derivative throughout the half-plane.

## Status

Closed as an exact equivalence and global positivity target.  A1 remains
open.

The currently sharpest global theorem is:
\[
  \Re{\xi'\over\xi}(s)\ge0\qquad(\Re s>1/2),
\]
proved from Euler--Gamma data without assuming the zero-free half-plane.

## Audit update

`175_LOG_DERIVATIVE_RH_EQUIVALENCE.md` records the full logical status of
this gate.  The half-plane positivity theorem is not merely sufficient:
together with the paired Hadamard product for \(\xi\), it is equivalent to
RH.  Therefore it is a legitimate global closure route for Omega7, but it is
still an open RH-strength theorem until proved non-circularly from the
Euler--Gamma data.
