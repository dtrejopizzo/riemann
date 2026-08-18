# Fejer density scale gate

## Purpose

`200_FEJER_MASS_STRONG_MARGIN_GATE.md` reduces the strong-margin route to
the Fejer lower bound
\[
  n\int_{\partial\mathbb D}F_n\,d\nu_g
  \ge
  \lambda_n^{\rm arch}
  \qquad(n\ge8).
\tag{1}
\]

This note records what scale of mass near \(\zeta=1\) is needed.  The main
conclusion is:

\[
  \boxed{
  \hbox{bounded absolutely continuous density is too small for the strong
  margin.}
  }
\]

To reach the archimedean scale \(n\log n\), the increment measure must have
either a sufficiently strong concentration near \(1\), for example a
logarithmic density, or an atom/singular component seen by the Fejer
kernels.

## Normalization

Write \(\zeta=e^{i\theta}\), and let
\[
  dm(\theta)={d\theta\over 2\pi}
\]
be normalized Lebesgue measure on \(\partial\mathbb D\).  The normalized
Fejer kernel satisfies
\[
  F_n(e^{i\theta})
  =
  {1\over n}
  \left|
    \sum_{j=0}^{n-1}e^{ij\theta}
  \right|^2,
  \qquad
  \int_{\partial\mathbb D}F_n\,dm=1.
\tag{2}
\]

The strong margin is
\[
  n\int F_n\,d\nu_g\ge \lambda_n^{\rm arch}.
\tag{3}
\]

## Archimedean scale

`151_EXPLICIT_ARCHIMEDEAN_POSITIVE_LOWER_BOUND.md` gives, for all large
\(n\), a lower bound of the form
\[
  \lambda_n^{\rm arch}\ge c_0 n\log n
\tag{4}
\]
with some explicit \(c_0>0\).  For example, (9) of `151` implies such a
bound after a finite threshold.

Thus any Fejer-margin proof must produce
\[
  \int F_n\,d\nu_g\gtrsim \log n.
\tag{5}
\]

This is stronger than mere positivity and stronger than a bounded
Lebesgue-density contribution.

## Bounded density no-go

Assume that
\[
  d\nu_g=h\,dm
\]
and
\[
  0\le h(\zeta)\le M
  \qquad\hbox{for }m\hbox{-a.e. }\zeta.
\tag{6}
\]

Then by (2),
\[
  \int F_n\,d\nu_g
  =
  \int F_n h\,dm
  \le
  M\int F_n\,dm
  =
  M.
\tag{7}
\]

Therefore
\[
  n\int F_n\,d\nu_g\le Mn.
\tag{8}
\]

Combining (4) and (8), the strong margin
\[
  n\int F_n\,d\nu_g\ge\lambda_n^{\rm arch}
\]
fails for all sufficiently large \(n\), because
\[
  Mn<c_0n\log n
\]
eventually.

Thus:
\[
\boxed{
  \hbox{a bounded absolutely continuous increment density cannot prove the
  strong margin.}
}
\tag{9}
\]

This is a formal scale no-go for that regularity class.  It does not claim
that the zeta increment object has such a density.

## Logarithmic density scale

The local mass condition from `200` is
\[
  \nu_g(|\theta|\le1/n)
  \ge
  {\pi^2\over4}{\lambda_n^{\rm arch}\over n^2}.
\tag{10}
\]

Since \(\lambda_n^{\rm arch}\asymp n\log n\) at the level of scale, (10)
asks for
\[
  \nu_g(|\theta|\le1/n)\gtrsim {\log n\over n}.
\tag{11}
\]

A bounded density gives only \(O(1/n)\) mass on that arc.  A logarithmic
density has the right scale.  Indeed, if for sufficiently small
\(|\theta|\)
\[
  h(e^{i\theta})\ge a\log {e\over|\theta|}
\tag{12}
\]
with respect to \(dm=d\theta/(2\pi)\), then
\[
\begin{aligned}
  \nu_g(|\theta|\le1/n)
  &\ge
  {a\over 2\pi}
  \int_{-1/n}^{1/n}\log {e\over|\theta|}\,d\theta\\
  &=
  {a\over\pi n}\left(\log(en)+1\right).
\end{aligned}
\tag{13}
\]

Therefore (10) follows for all large \(n\) if
\[
  {a\over\pi n}(\log(en)+1)
  \ge
  {\pi^2\over4}{\lambda_n^{\rm arch}\over n^2}.
\tag{14}
\]

Using a concrete upper comparison
\[
  \lambda_n^{\rm arch}\le C_1 n\log n
\tag{15}
\]
for large \(n\), it would be enough to have
\[
  a\ge {\pi^3\over4}C_1
\tag{16}
\]
after enlarging the finite threshold.

Thus a logarithmic singularity at \(1\) is the natural absolutely
continuous scale for the strong margin.

## Atom at \(1\)

If \(\nu_g\) has an atom of mass \(a_0>0\) at \(1\), then
\[
  \int F_n\,d\nu_g\ge a_0F_n(1)=a_0n.
\tag{17}
\]

Hence
\[
  n\int F_n\,d\nu_g\ge a_0n^2.
\tag{18}
\]

Since
\[
  \lambda_n^{\rm arch}=O(n\log n),
\]
any fixed atom \(a_0>0\) would dominate the archimedean margin for all
sufficiently large \(n\), leaving only a finite initial range to check.

This is a sufficient singular mechanism.  The phase does not currently
construct such an atom from Euler--Gamma data, and inserting it by hand
would be circular unless it is derived from the completed arithmetic
object.

## Exact remaining theorem

The strong-margin route now splits into precise alternatives:

1. construct \(\nu_g\) non-circularly and prove the exact Fejer bound
   \[
     n\int F_n\,d\nu_g\ge\lambda_n^{\rm arch};
   \]
2. prove a local mass lower bound of order
   \[
     \nu_g(|\theta|\le1/n)\gtrsim{\log n\over n};
   \]
3. prove a logarithmic-density lower bound near \(1\);
4. prove an atom or singular concentration near \(1\) strong enough to
   dominate \(n\log n\).

Bounded density, positivity, or finite total mass alone is insufficient.

## Status

Closed as a density-scale audit for the Fejer strong-margin gate.

A1 remains open.  The new information is that any regular absolutely
continuous increment measure with bounded density cannot provide the
strong-margin scale; a successful Fejer route needs logarithmic or stronger
concentration near \(\zeta=1\), or a different signed compact proof.
