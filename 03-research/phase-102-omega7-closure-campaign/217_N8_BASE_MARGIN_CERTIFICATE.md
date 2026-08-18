# n=8 base margin certificate

## Purpose

`215_BASE_CUTOFF_NORMALIZATION_GAMMA_POSITIVITY.md` shows that the terminal
budget coefficient \(\Gamma_{\mathcal B}\) becomes positive once the base
compact condition
\[
  C_8^\ast=C_8(T_8)\ge0
\]
is proved, provided the auxiliary \(T_7\) is chosen small.

This note closes that base condition from a finite Euler--Gamma/Stieltjes
margin at \(n=8\), together with A0.

## Exact finite formula at \(n=8\)

Use the notation of
`RH-MASTER-CONTEXT/fragments/OMEGA7_POINT4_FINITE_CERTIFICATE.md`.  Let
\[
  \log(z\zeta(1+z))=\sum_{k\ge1}p_kz^k,
\]
with
\[
  q_r={(-1)^{r-1}\gamma_{r-1}\over(r-1)!},
  \qquad
  p_r=q_r-{1\over r}\sum_{k=1}^{r-1}kp_kq_{r-k}.
\tag{1}
\]

Then
\[
  \lambda_8^{\rm prime}
  =
  8\sum_{k=1}^{8}{7\choose k-1}p_k,
\tag{2}
\]
and
\[
  \lambda_8^{\rm arch}
  =
  1-4(\gamma+\log(4\pi))
  +
  \sum_{k=2}^{8}
  (-1)^k{8\choose k}(1-2^{-k})\zeta(k).
\tag{3}
\]

Thus the finite strong margin is the rational expression
\[
\boxed{
  \lambda_8-{1\over2}\lambda_8^{\rm arch}
  =
  \lambda_8^{\rm prime}
  +
  {1\over2}\lambda_8^{\rm arch}
}
\tag{4}
\]
in the constants
\[
  \gamma_0,\ldots,\gamma_7,
  \quad
  \log(4\pi),
  \quad
  \zeta(2),\ldots,\zeta(8).
\]

## Global finite margin at \(n=8\)

The rational interval verifier
\[
  \texttt{RH-MASTER-CONTEXT/tools/omega7\_point4\_interval\_verify.py}
\]
has been extended from \(1\le n\le7\) to \(1\le n\le8\) by adding rational
enclosures for \(\gamma_7\) and \(\zeta(8)\):
\[
  \gamma_7\in
  [-0.000527289567057751046074097506,\,
   -0.000527289567057751046074097505],
\tag{5}
\]
and
\[
  \zeta(8)\in
  [1.0040773561979443393786852385,\,
   1.0040773561979443393786852386].
\tag{6}
\]

The enclosure (5) is obtained by the same Euler--Maclaurin Laurent
coefficient method used in the finite certificate, now with \(j=7\).  The
enclosure (6) follows from
\[
  \zeta(8)={\pi^8\over9450}
\]
and the same rational Machin enclosure for \(\pi\).

Interval propagation through (1)--(4) gives, in particular,
\[
\boxed{
  \lambda_8^{\rm arch}
  \in
  [0.02089993302762,\ 0.02089993302764].
}
\tag{7}
\]

For \(n=8\), it proves the interval
\[
\boxed{
  \lambda_8
  \in
  [1.465755677147060632655514,\,
   1.465755677147060632655515].
}
\tag{8}
\]

It also proves the stronger margin
\[
\boxed{
  \lambda_8-{1\over2}\lambda_8^{\rm arch}
  \in
  [1.455305710633246144455217,\,
   1.455305710633246144455218].
}
\tag{9}
\]

In particular,
\[
\boxed{
  \lambda_8\ge {1\over2}\lambda_8^{\rm arch}.
}
\tag{10}
\]

This is a finite zero-free computation from the Laurent expansion at
\(s=1\), the Euler--Gamma factor, and rational interval arithmetic.

## From the finite margin to the compact base \(C_8^\ast\)

From `150_A1_TAIL_REMAINDER_GENERATOR_IDENTITY.md`,
\[
  C_n(T_n)
  =
  \lambda_n
  -{1\over4}\lambda_n^{\rm arch}
  -R_n(T_n).
\tag{11}
\]

A0 gives
\[
  |R_n(T_n)|\le {1\over4}\lambda_n^{\rm arch}
  \qquad(n\ge8).
\tag{12}
\]

At \(n=8\), combining (10)--(12) yields
\[
\begin{aligned}
  C_8^\ast
  &=
  C_8(T_8)\\
  &\ge
  \lambda_8
  -{1\over4}\lambda_8^{\rm arch}
  -{1\over4}\lambda_8^{\rm arch}\\
  &=
  \lambda_8-{1\over2}\lambda_8^{\rm arch}\\
  &>0.
\end{aligned}
\tag{13}
\]

Thus
\[
\boxed{
  C_8^\ast>0.
}
\tag{14}
\]

This closes the base condition required by the moving-diagonal recurrence,
provided A0 is instantiated for \(n=8\) with its declared tail bound.

## Consequence for \(\Gamma_{\mathcal B}\)

With the auxiliary normalization
\[
  0<T_7\le\min(\log2,1/130)
\]
from `215`, (14) implies
\[
  \Gamma_{\mathcal B}>0.
\]

Therefore the terminal large-\(n\) budget coefficient is positive.  By
`208` and `210`, the terminal VK load is absorbed for all sufficiently
large \(n\), after making the constants and threshold explicit.

## What remains open

This note does not close A1.  It closes only the base \(n=8\) compact
condition and the associated terminal budget sign gate.

The remaining absolute-route tasks are:

1. make the terminal threshold and finite range explicit;
2. prove the mixed off-diagonal \(L^1\) domination from `211`;
3. or replace the absolute route by a signed compact proof, strong margin,
   one-sided tail, comparative Loewner--Schur theorem, or global half-plane
   theorem from `196`.

## Status

Closed as a finite \(n=8\) base margin certificate.

A1 remains open.  The base compact condition \(C_8^\ast\ge0\) is closed via
finite interval arithmetic plus A0, but the mixed \(L^1\) loads and the
uniform infinite-range compact proof remain open.
