# Fejer mass strong-margin gate

## Purpose

`198_STRONG_MARGIN_SECOND_DIFFERENCE_AUDIT.md` rewrites the strong margin as
\[
  n\int_{\partial\mathbb D}F_n(\zeta)\,d\nu_g(\zeta)
  \ge
  \lambda_n^{\rm arch},
\tag{1}
\]
where
\[
  F_n(e^{i\theta})
  =
  {1\over n}
  \left|
    1+e^{i\theta}+\cdots+e^{i(n-1)\theta}
  \right|^2
  =
  {1\over n}
  \left({\sin(n\theta/2)\over\sin(\theta/2)}\right)^2.
\tag{2}
\]

This note converts (1) into quantitative mass conditions near
\(\zeta=1\).  It gives sufficient local-mass theorems and clarifies why
positivity or total mass alone is not enough.

## Local lower bound for Fejer

For \(|x|\le\pi/2\),
\[
  |\sin x|\ge {2\over\pi}|x|.
\tag{3}
\]

For \(|\theta|\le 1/n\), one has \(|n\theta/2|\le1/2<\pi/2\), so
\[
  |\sin(n\theta/2)|
  \ge
  {2\over\pi}{n|\theta|\over2}
  =
  {n|\theta|\over\pi}.
\tag{4}
\]

Also
\[
  |\sin(\theta/2)|\le {|\theta|\over2}.
\tag{5}
\]

Therefore, for \(0<|\theta|\le1/n\),
\[
  \left|
  {\sin(n\theta/2)\over\sin(\theta/2)}
  \right|
  \ge
  {2n\over\pi}.
\]
The same bound holds at \(\theta=0\) by continuity, since \(F_n(1)=n\).
Hence
\[
\boxed{
  F_n(e^{i\theta})\ge {4\over\pi^2}n
  \qquad(|\theta|\le1/n).
}
\tag{6}
\]

## Sufficient local mass theorem

Let
\[
  I_n=\{e^{i\theta}:|\theta|\le1/n\}.
\tag{7}
\]

By (6),
\[
  n\int_{\partial\mathbb D}F_n\,d\nu_g
  \ge
  n\int_{I_n}F_n\,d\nu_g
  \ge
  {4\over\pi^2}n^2\nu_g(I_n).
\tag{8}
\]

Thus the strong margin follows if
\[
\boxed{
  \nu_g(I_n)
  \ge
  {\pi^2\over4}{\lambda_n^{\rm arch}\over n^2}
  \qquad(n\ge8).
}
\tag{9}
\]

This is a concrete sufficient Fejer-mass theorem.

Using the known growth scale
\[
  \lambda_n^{\rm arch}=O(n\log n),
\]
(9) asks, at the level of order of magnitude, for local mass
\[
  \nu_g(I_n)\gtrsim {\log n\over n}.
\tag{10}
\]

The phase does not currently prove such a lower bound for the increment
measure \(\nu_g\).

## More general arcs

For \(0<c\le1\), define
\[
  I_{n,c}=\{e^{i\theta}:|\theta|\le c/n\}.
\tag{11}
\]

The same proof gives
\[
  F_n(e^{i\theta})\ge {4\over\pi^2}n
  \qquad(e^{i\theta}\in I_{n,c}),
\tag{12}
\]
so the sufficient condition may be weakened to
\[
\boxed{
  \nu_g(I_{n,c})
  \ge
  {\pi^2\over4}{\lambda_n^{\rm arch}\over n^2}.
}
\tag{13}
\]

The constant can be improved by using sharper sine bounds depending on
\(c\), but the scale remains \(\lambda_n^{\rm arch}/n^2\).

## Annular complement obstruction

The preceding theorem also shows exactly why total mass is insufficient.
The Fejer kernel is concentrated near \(1\), but it has zeros at nontrivial
\(n\)-th roots of unity:
\[
  F_n(\zeta)=0
  \qquad(\zeta^n=1,\ \zeta\ne1).
\tag{14}
\]

A positive measure can have large total mass while assigning too little
mass to \(I_n\), or even concentrating on the zero set (14).  Then
\[
  \int F_n\,d\nu_g
\]
does not see that mass.  Therefore a strong-margin proof from the increment
measure must control distribution, not merely positivity or total mass.

## Equivalent moving lower-density theorem

The strong-margin route through \(g\)-Toeplitz positivity is closed if the
increment measure satisfies
\[
\boxed{
  \inf_{n\ge8}
  {n^2\nu_g(I_n)\over\lambda_n^{\rm arch}}
  \ge
  {\pi^2\over4}.
}
\tag{15}
\]

This is stronger than necessary, because mass outside \(I_n\) also
contributes positively.  The exact necessary and sufficient condition
remains
\[
\boxed{
  n\int_{\partial\mathbb D}F_n\,d\nu_g
  \ge
  \lambda_n^{\rm arch}
  \qquad(n\ge8).
}
\tag{16}
\]

But (15) is a clean local theorem that would imply (16).

## Relation to Euler--Gamma data

For zeta, the measure \(\nu_g\) is not currently constructed
non-circularly with the needed support and density properties.  A proof
must therefore supply both:

1. the positive increment measure from Euler--Gamma data;
2. the moving lower-density estimate (15), or the exact Fejer lower bound
   (16).

The first item is the global Toeplitz/RH-strength theorem.  The second is
the extra strong-margin scale isolated here.

## Status

Closed as a quantitative Fejer-mass gate for the strong-margin route.

A1 remains open.  The new sufficient target is the moving local mass bound
(15), while the exact target remains the Fejer lower bound (16).
