# Log-density increment generator gate

## Purpose

`202_FEJER_DENSITY_SCALE_GATE.md` shows that bounded increment density is
too small for the strong margin, while `203_ATOM_AT_ONE_INCOMPATIBILITY_AUDIT.md`
eliminates an atom at \(\zeta=1\) as too singular for the Euler--Gamma Li
generator.

This note identifies the intermediate scale: logarithmic concentration of
the increment measure near \(1\).  It is exactly the scale compatible with
the one-sided Euler--Gamma increment generator
\[
  \mathcal G_+(z)
  =
  \lambda_1+{(1-z)^2\over z}\mathcal L(z).
\]

The remaining theorem is not only to see a logarithm in the generator; it is
to construct a positive increment measure and prove a lower logarithmic
coefficient large enough for the Fejer margin.

## Increment generator boundary scale

From `172`,
\[
  \mathcal G_+(z)
  =
  g_0+\sum_{m\ge1}g_mz^m
  =
  \lambda_1+{(1-z)^2\over z}\mathcal L(z).
\tag{1}
\]

From `140`,
\[
  \mathcal L(z)
  =
  {z\over(1-z)^2}
  {\xi'\over\xi}\!\left({1\over1-z}\right).
\tag{2}
\]

Therefore
\[
\boxed{
  \mathcal G_+(z)
  =
  \lambda_1+
  {\xi'\over\xi}\!\left({1\over1-z}\right).
}
\tag{3}
\]

Along \(z=r\to1^-\), putting \(s=(1-r)^{-1}\), one has
\[
  {\xi'\over\xi}(s)=O(\log s).
\]
Thus
\[
\boxed{
  \mathcal G_+(r)=O\!\left(\log {1\over1-r}\right)
  \qquad(r\to1^-).
}
\tag{4}
\]

This is exactly between the two scales audited earlier:

- bounded density gives a bounded Abel mean;
- an atom at \(1\) gives \((1-r)^{-1}\);
- the Euler--Gamma increment generator allows logarithmic growth.

## Logarithmic density produces logarithmic Abel growth

Assume, as a model, that near \(\theta=0\),
\[
  d\nu_g(e^{i\theta})
  =
  h(\theta){d\theta\over2\pi},
  \qquad
  h(\theta)\sim a\log {e\over|\theta|}.
\tag{5}
\]

For \(0<r<1\), the Abel boundary pairing is
\[
  \int_{\partial\mathbb D}{1\over1-r\zeta}\,d\nu_g(\zeta).
\tag{6}
\]

Its real singular size is controlled by the Poisson-type denominator
\[
  |1-re^{i\theta}|^2
  =
  (1-r)^2+2r(1-\cos\theta)
  \asymp (1-r)^2+\theta^2
\tag{7}
\]
near \(\theta=0\).  More precisely, the real part has kernel
\[
  \mathrm{Re}{1\over1-re^{i\theta}}
  =
  {1-r\cos\theta\over |1-re^{i\theta}|^2}
  \asymp
  {(1-r)\over(1-r)^2+\theta^2}
  \tag{8}
 \]
on the local scale \(|\theta|<\theta_0\).  Therefore the local real Abel
scale is governed by
\[
  \int_{|\theta|<\theta_0}
  \log(e/|\theta|)
  {(1-r)\over(1-r)^2+\theta^2}
  \,d\theta,
\]
which grows like
\[
  \log {1\over1-r}.
\tag{9}
\]

Thus logarithmic density is compatible with the generator scale (4), unlike
an atom.

## Lower-density theorem sufficient for the margin

Let
\[
  I_n=\{|\theta|\le1/n\}.
\]

If for all small \(|\theta|\)
\[
  h(\theta)\ge a\log {e\over|\theta|},
\tag{10}
\]
then, as shown in `202`,
\[
  \nu_g(I_n)
  \ge
  {a\over\pi n}(\log(en)+1).
\tag{11}
\]

Combining with `200`, the strong margin follows for all large \(n\) if
\[
  {a\over\pi n}(\log(en)+1)
  \ge
  {\pi^2\over4}{\lambda_n^{\rm arch}\over n^2}.
\tag{12}
\]

Equivalently, a sufficient asymptotic condition is
\[
\boxed{
  a\ge { \pi^3\over4}
  \limsup_{n\to\infty}{\lambda_n^{\rm arch}\over n\log n},
}
\tag{13}
\]
with the finite initial range checked separately.

This is a clean log-density gate.

## Why generator logarithmic growth is not enough

The estimate
\[
  \mathcal G_+(r)=O\!\left(\log{1\over1-r}\right)
\]
does not imply the lower-density theorem.  It gives only an upper scale for
the Abel growth.

To close the strong margin, one needs all of the following:

1. Toeplitz positivity of the increment sequence \(g_m\), producing a
   positive measure \(\nu_g\);
2. a non-circular identification of the near-\(1\) boundary component of
   that measure;
3. a lower logarithmic density or equivalent Fejer lower bound, not merely
   an \(O(\log)\) upper estimate;
4. constants large enough to dominate \(\lambda_n^{\rm arch}\).

Thus the generator scale is compatible with the Fejer margin but does not
prove it.

## Exact live theorem

The Fejer strong-margin route now has the following sharp form:

Construct the Euler--Gamma increment measure \(\nu_g\) and prove that its
near-\(1\) component satisfies either
\[
\boxed{
  n\int F_n\,d\nu_g\ge\lambda_n^{\rm arch}
  \qquad(n\ge8),
}
\tag{14}
\]
or the stronger local density condition
\[
\boxed{
  {d\nu_g\over dm}(e^{i\theta})
  \ge
  a\log {e\over|\theta|}
  \quad(|\theta|\hbox{ small}),
}
\tag{15}
\]
with \(a\) satisfying (13).

This theorem is RH-strength if it exists, but it is no longer vague: it is
a boundary lower-density theorem for the increment generator (3).

## Status

Closed as a log-density normal form for the Fejer strong-margin route.

A1 remains open.  The atom shortcut is eliminated; bounded density is too
small; the remaining Fejer route requires a positive increment measure with
a lower logarithmic boundary density, or a direct proof of the exact Fejer
lower bound.
