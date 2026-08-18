# RDI Li-coefficient extraction gate

## Purpose

`102_RDI_TO_LI_MINIMAL_BRIDGE.md` says that the RDI route can re-enter the
Omega7 proof only if it proves either Li positivity or real-rootedness of
the completed divisor.  This note writes the exact coefficient-extraction
gate in the Li \(z\)-coordinate.

The goal is to remove ambiguity from the phrase "RDI implies Li": the
bridge must produce the Li generating function with enough local uniform
control to pass to coefficients.

## Li coordinate

Set
\[
  s=s(z)={1\over1-z}.
\]

For
\[
  F(z)=\log\xi(s(z)),
\]
the Li generator is
\[
\boxed{
  \mathcal L(z)
  =
  zF'(z)
  =
  {z\over(1-z)^2}{\xi'\over\xi}\!\left({1\over1-z}\right)
  =
  \sum_{n\ge1}\lambda_n z^n.
}
\tag{1}
\]

Thus coefficient positivity is exactly
\[
\boxed{
  [z^n]\mathcal L(z)\ge0
  \qquad(n\ge1).
}
\tag{2}
\]

Any RDI bridge to Li must therefore identify \(\mathcal L\), not merely a
real-axis normalization of \(\Xi\).

## Acceptable coefficient bridge

Let \(\Theta_N\) denote the RDI approximants after all phase-specific
normalizations and limiting orders have been fixed.  An acceptable direct
bridge is a family of analytic functions
\[
  F_N(z)
\]
on a disk \(|z|<r\) with some \(r>0\), satisfying:

1. **Correct target identification**
   \[
     F_N(z)\longrightarrow F(z)=\log\xi\!\left({1\over1-z}\right)
   \]
   locally uniformly on \(|z|<r\), with the same additive normalization for
   all \(N\).
2. **Coefficient-positive logarithmic derivatives**
   \[
     zF_N'(z)=\sum_{n\ge1}\lambda_{n,N}z^n,
     \qquad
     \lambda_{n,N}\ge0
   \]
   for every \(n\) in the range visible to the approximant.
3. **Stable coefficient passage**
   for every fixed \(n\),
   \[
     \lambda_{n,N}\longrightarrow\lambda_n.
   \]

The third item follows from the first by Cauchy's formula:
\[
\boxed{
  \lambda_n
  =
  {1\over2\pi i}\int_{|z|=\rho}
    {\mathcal L(z)\over z^{n+1}}\,dz
  =
  \lim_{N\to\infty}
  {1\over2\pi i}\int_{|z|=\rho}
    {zF_N'(z)\over z^{n+1}}\,dz
}
\tag{3}
\]
for any \(0<\rho<r\).

Consequently, if the RDI approximants have nonnegative Li coefficients and
converge locally uniformly in this coordinate, then
\[
\boxed{
  \lambda_n\ge0\qquad(n\ge1).
}
\tag{4}
\]

By Li's criterion, (4) proves RH and closes Omega7 through the global route.

## Real-rooted bridge

A second acceptable bridge is stronger but often more natural for LP/RDI:
prove that the approximants are real-rooted in the completed \(\Xi\)-line
and converge locally uniformly to \(\Xi\) as entire functions.

If the convergence is locally uniform and the limit is not identically
zero, Hurwitz gives that every nonreal zero of the limit would be
approximated by nonreal zeros of the approximants.  Hence the limit is also
real-rooted.  Then the zeros of \(\xi\) lie on the critical line, and Li
positivity follows from the standard paired zero formula.

This bridge must still identify the actual Euler--Gamma \(\Xi\), not a
renormalized proxy chosen after the fact.

## Insufficient RDI data

The following are not enough to infer Li positivity:

1. pointwise convergence of normalized logarithms on a real ray;
2. convergence of values without local uniform control in a complex
   neighborhood of \(z=0\);
3. real-rootedness of finite approximants without locally uniform
   convergence to the true \(\Xi\);
4. coefficient positivity for a proxy generator not proved equal to
   \(z\,d/dz\log\xi(1/(1-z))\);
5. any limiting argument that chooses the Euler--Gamma normalization using
   the desired Li coefficients.

All five failures lose either target identification or coefficient
continuity.

## Minimal theorem

The RDI route can re-enter the main Omega7 attack only after proving one of
the following:

\[
\boxed{
  zF_N'(z)\to
  {z\over(1-z)^2}{\xi'\over\xi}\!\left({1\over1-z}\right)
  \quad\hbox{locally uniformly near }0,
}
\tag{5}
\]
with nonnegative approximating coefficients, or
\[
\boxed{
  \Theta_N\to\Xi
  \quad\hbox{locally uniformly as entire functions, with all }\Theta_N
  \hbox{ real-rooted}.
}
\tag{6}
\]

Either theorem is RH-strength.  Without one of them, BTG, GAP-Z, and the
other RDI modules remain infrastructure and do not close A1 or Omega7.

## Status

Closed as the RDI Li-coefficient extraction gate.

A1 remains open.  Omega7 remains open unless RDI supplies one of the two
bridges (5)--(6), or unless the compact A1 route is proved directly.
