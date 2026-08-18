# Fejer mass localization necessary gate

## Purpose

`271_POSITIVE_INCREMENT_FEJER_MASS_SEPARATION.md` shows that a positive
increment measure gives Li positivity but not the compact A1 strong margin.
This note records the corresponding necessary localization theorem.

If a positive measure \(\nu\) is to satisfy the Fejer lower bound
\[
  \int_{\partial\mathbb D}F_n\,d\nu
  \ge c\log n-O(1),
\tag{1}
\]
then \(\nu\) must have a logarithmically large Fejer-localized mass near
\(\zeta=1\).  Positivity, finite mass, a bounded absolutely continuous
density by itself, or support away from \(1\) cannot supply (1).

This is a necessary gate, not a proof of A1.

## Fejer envelope

Write \(\zeta=e^{i\theta}\), \(-\pi\le\theta\le\pi\), and
\[
  F_n(e^{i\theta})
  =
  {1\over n}
  \left({\sin(n\theta/2)\over\sin(\theta/2)}\right)^2.
\tag{2}
\]

Using
\[
  |\sin(n\theta/2)|\le \min\{n|\theta|/2,1\},
  \qquad
  |\sin(\theta/2)|\ge {|\theta|\over\pi}
  \quad(|\theta|\le\pi),
\]
we get the pointwise bound
\[
\boxed{
  F_n(e^{i\theta})
  \le
  \min\left\{n,\ {\pi^2\over n\theta^2}\right\}
  \qquad(0<|\theta|\le\pi).
}
\tag{3}
\]
At \(\theta=0\), \(F_n(1)=n\), consistent with the first branch.

## Localization upper bound

Let
\[
  I_n=\{e^{i\theta}:|\theta|\le 1/n\}.
\]
For any finite positive measure \(\nu\) on \(\partial\mathbb D\), (3)
implies
\[
\boxed{
  \int F_n\,d\nu
  \le
  n\,\nu(I_n)
  +
  {\pi^2\over n}
  \int_{\{|\theta|>1/n\}}{d\nu(e^{i\theta})\over \theta^2}.
}
\tag{4}
\]

Equivalently, with dyadic annuli
\[
  A_{n,j}=
  \left\{
    e^{i\theta}:
    {2^j\over n}<|\theta|\le {2^{j+1}\over n}
  \right\},
  \qquad
  0\le j\le \lfloor\log_2(\pi n)\rfloor,
\tag{5}
\]
one has
\[
\boxed{
  \int F_n\,d\nu
  \le
  n\nu(I_n)
  +
  \pi^2 n
  \sum_{0\le j\le\lfloor\log_2(\pi n)\rfloor}
    4^{-j}\nu(A_{n,j}).
}
\tag{6}
\]

Thus any lower bound of size \(c\log n\) forces the localized quantity on
the right of (4), or equivalently (6), to have logarithmic size.

## Necessary condition for the compact Fejer route

For the Euler--Gamma increment route, compact strong margin requires
\[
  \int F_n\,d\nu_g
  \ge {A_n\over n}
  \qquad(n\ge8),
\tag{7}
\]
where \(A_n=\lambda_n^{arch}\).  Since
\[
  A_n={1\over2}n\log n+O(n),
\tag{8}
\]
(7) implies
\[
  \int F_n\,d\nu_g
  \ge {1\over2}\log n-O(1).
\tag{9}
\]

Combining (4) with (9), any positive increment measure capable of closing
the compact Fejer margin must satisfy
\[
\boxed{
  n\,\nu_g(I_n)
  +
  {\pi^2\over n}
  \int_{\{|\theta|>1/n\}}{d\nu_g(e^{i\theta})\over \theta^2}
  \ge
  {1\over2}\log n-O(1).
}
\tag{10}
\]

This is a necessary localization condition.  It is weaker than the local
log-density theorem of `263`--`264`, but it is strong enough to rule out
several false shortcuts.

## Consequences

### Support away from \(1\)

If \(\mathrm{supp}\,\nu\subset\{|\theta|\ge\theta_0\}\) for some
\(\theta_0>0\), then (3) gives
\[
  \int F_n\,d\nu
  \le
  {\pi^2\over n\theta_0^2}\nu(\partial\mathbb D)
  =
  O(1/n).
\tag{11}
\]
So support away from \(1\) is incompatible with the compact Fejer margin.

### Bounded density

If an absolutely continuous component has density \(0\le h\le M\), then
that component contributes only \(O(1)\):
\[
  \int F_n h\,dm
  \le M\int F_n\,dm
  =
  M.
\tag{12}
\]
Thus bounded density cannot produce the required \((1/2)\log n\) growth.
A singular component could still contribute, but it would have to satisfy
the same localization condition (10).  This recovers the scale obstruction
of `202` in localization form.

### Logarithmic density is the correct scale

For
\[
  L(\theta)=-\log|2\sin(\theta/2)|,
\]
`260` proves the exact identity
\[
  \int F_nL\,dm
  =
  H_{n-1}-{n-1\over n}
  =
  \log n+O(1).
\tag{13}
\]
Therefore a lower density \(h\ge aL-B\) gives precisely the logarithmic
scale.  By `259`--`264`, the compact route needs \(a>1/2\); by `265`, the
Euler--Gamma Abel budget forces \(a\le1\).

Hence the live window remains
\[
\boxed{
  {1\over2}<a\le1,
}
\tag{14}
\]
and (10) is the necessary localization shadow of that window.

## Relation to Abel and anti-concentration gates

The Abel/Poisson kernel \(P_{1-1/n}\) sees radial mass near \(1\) but has no
moving zeros.  The Fejer kernel \(F_n\) is localized near \(1\) and also
vanishes at the nontrivial \(n\)-th roots of unity.  Therefore:

- `266` records the exact defect term needed to transfer Abel mass to Fejer
  mass;
- `270` proves that no positive inverse from Poisson kernels to Fejer
  kernels exists;
- this note proves that a direct Fejer proof must create the logarithmic
  growth through the localized quantity (10).

Together these gates leave no hidden shortcut:
\[
  \hbox{Abel growth or positivity}
  \not\Rightarrow
  \hbox{compact Fejer margin}
\]
without local logarithmic density, direct Fejer lower bounds, or equivalent
anti-concentration.

## Status

Closed as a necessary localization theorem for the Fejer strong-margin
route.  A1 remains open until the Euler--Gamma increment measure is
constructed non-circularly and shown to satisfy a sufficient lower
log-density, direct Fejer, or anti-concentration theorem, plus the finite
certificate of `261`.
