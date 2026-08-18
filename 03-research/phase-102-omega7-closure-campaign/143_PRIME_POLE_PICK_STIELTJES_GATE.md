# Prime-pole Pick/Stieltjes gate

## Purpose

The prime-pole generator is now known exactly:
\[
  \mathcal P(z)
  =
  {z\over(1-z)^2}
  \left[
    {1\over s(z)-1}+{\zeta'\over\zeta}(s(z))
  \right],
  \qquad
  s(z)={1\over1-z}.
\tag{1}
\]

This note tests whether the remaining A1/Omega7 sign can be closed by
showing that the prime-pole generator is a Pick, Herglotz, Stieltjes, or
Schur/Carathéodory object with a positive representing measure.

The conclusion is exact:

- the Euler-product half-plane gives a positive Stieltjes measure before
  continuation;
- the Li boundary generator after pole pairing is a signed Stieltjes
  current;
- a positive Pick/Stieltjes certificate for the continued Li generator would
  force the transformed zero divisor to lie on the admissible boundary;
- that support statement is the missing RH/A1 theorem.

Thus there is no local prime-pole Pick/Stieltjes proof from
\(\Lambda(m)\ge0\).  The viable theorem is a global completed
Euler--Gamma positive-boundary-measure theorem.

## The half-plane Stieltjes object

For \(\Re s>1\),
\[
  -{\zeta'\over\zeta}(s)
  =
  \sum_{m\ge2}{\Lambda(m)\over m^s}
  =
  \int_{1^-}^{\infty} y^{-s}\,d\psi(y).
\tag{2}
\]

With \(x=s-1>0\), this is the Laplace transform
\[
  -{\zeta'\over\zeta}(1+x)
  =
  \int_{0^-}^{\infty} e^{-xu} e^{-u}\,d\psi(e^u).
\tag{3}
\]

Therefore the raw Euler-product logarithmic derivative is completely
monotone in the half-plane variable \(x\).  This is the only unconditional
positive-measure statement supplied by the Euler product.

The paired prime-pole term is different:
\[
  H(s):={1\over s-1}+{\zeta'\over\zeta}(s).
\tag{4}
\]

In the same variable \(x=s-1\),
\[
  H(1+x)
  =
  {1\over x}
  -
  \int_{0^-}^{\infty}e^{-xu}e^{-u}\,d\psi(e^u).
\tag{5}
\]

Equation (5) is not a positive Stieltjes/Laplace transform.  The pole is a
renormalizing term with the opposite sign from the prime measure.  After
Stieltjes integration by parts, as in the prime-pole integral generator,
\[
  H(s)
  =
  -1
  -
  s\int_1^\infty(\psi(y)-y)y^{-s-1}\,dy,
\tag{6}
\]
and the integrand uses the signed error \(E(y)=\psi(y)-y\), not a positive
measure.

Thus the first possible proof pattern is eliminated:
\[
  \Lambda(m)\ge0
  \quad\Longrightarrow\quad
  \mathcal P(z)\hbox{ is Pick/Stieltjes-positive}.
\]

The implication fails at the pole-pairing and boundary-continuation step.

## Exact singular structure in Li coordinates

Let
\[
  z_\rho=1-{1\over\rho}.
\tag{7}
\]

If \(\rho\) is a zero of \(\zeta\), then \(\zeta'/\zeta\) has a simple pole
at \(s=\rho\) with residue equal to the multiplicity \(m_\rho\).  Since
\[
  s'(z)={1\over(1-z)^2}=s(z)^2,
\]
and
\[
  {z\over(1-z)^2}=z\,s(z)^2,
\]
the generator \(\mathcal P\) has, at \(z=z_\rho\),
\[
  \mathcal P(z)
  =
  {m_\rho z_\rho\over z-z_\rho}
  +O(1).
\tag{8}
\]

The prefactor and the pole pairing at \(s=1\) do not remove these poles.

The trivial zeros \(s=-2k\) give poles at
\[
  z_{-2k}=1+{1\over 2k}>1.
\tag{9}
\]
These are outside the unit disk.  The nontrivial zeros determine the possible
Li-disk obstruction.

For a nontrivial zero \(\rho=\beta+i\gamma\),
\[
  |z_\rho|^2
  =
  \left|1-{1\over\rho}\right|^2
  =
  {(\beta-1)^2+\gamma^2\over \beta^2+\gamma^2}.
\tag{10}
\]

Hence
\[
  |z_\rho|<1 \iff \beta>{1\over2},
  \qquad
  |z_\rho|=1 \iff \beta={1\over2},
  \qquad
  |z_\rho|>1 \iff \beta<{1\over2}.
\tag{11}
\]

By the functional equation, any off-line zero produces a paired zero on the
other side of the critical line.  Therefore an off-line zero produces at
least one prime-pole singularity strictly inside the Li disk.

## Disk Pick/Schur no-go

A disk Schur, Carathéodory, or Pick certificate strong enough to imply
coefficient positivity must first give an analytic function on the unit disk,
possibly after explicitly subtracting harmless analytic terms.  But
\(\mathcal P\) has the poles (8).  Therefore:

**Proposition.** If the unmodified prime-pole generator \(\mathcal P\), or
\(\mathcal P\) plus an explicitly analytic harmless correction, belongs to a
disk Pick/Schur/Carathéodory class on \(\mathbb D\), then \(\zeta\) has no
zeros with \(\Re\rho>1/2\).  By the functional equation, all nontrivial zeros
lie on \(\Re s=1/2\).

**Proof.** Membership in any of these disk classes implies analyticity in
\(\mathbb D\).  By (8), every zero with \(\Re\rho>1/2\) gives a non-removable
pole of \(\mathcal P\) at \(z_\rho\), and (11) puts this pole inside
\(\mathbb D\).  An explicitly analytic correction cannot cancel a pole.
Thus no such zero exists.  The functional equation reflects zeros across the
critical line, so no zero with \(\Re\rho<1/2\) exists either.  This is RH.
\(\square\)

This is not a contradiction; it is the exact force-RH content of the gate.
It shows that proving such a disk Pick/Schur theorem from Euler--Gamma data
would close Omega7.  It also shows why the theorem cannot be replaced by a
formal assertion that the transformed divisor is a boundary measure: that
assertion is already RH in Li coordinates.

## Line-coordinate Herglotz/Stieltjes no-go

The same obstruction appears in line coordinates.  Put
\[
  s={1\over2}+i\tau.
\tag{12}
\]

Zeros on the critical line correspond to real \(\tau\).  A Herglotz or
Stieltjes representation with positive measure on the boundary would have
singular measure supported on real \(\tau\).  But a zero off the critical line
gives a pole at a non-real \(\tau\).  Therefore any positive
line-coordinate representing measure for the continued completed logarithmic
derivative must first prove the support collapse
\[
  \mathrm{supp}\,\Delta
  \log\left|\xi\left({1\over2}+z\right)\right|
  \subset i\mathbb R.
\tag{13}
\]

For the prime-pole part alone the situation is even less favorable: the
Gamma factor has not yet cancelled the trivial-zero poles of
\(\zeta'/\zeta\).  A natural positive boundary theorem must therefore be a
theorem for the completed Euler--Gamma object, not for the raw prime-pole
piece in isolation.

## Relation to the A1 integral

The prime-pole integral generator gives
\[
  [z^n]\mathcal P(z)
  =
  -n+\int_1^\infty(\psi(y)-y)f'_{n,0}(y)\,dy.
\tag{14}
\]

After A0, A1 asks for
\[
  -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy
  +{3\over4}\lambda_n^{\rm arch}\ge0
  \qquad(n\ge8).
\tag{15}
\]

A Pick/Stieltjes representation of the positive-measure type would imply
kernel positivity for all Li tests at once, hence would imply (15) after the
A0 tail budget.  But (14) is a signed pairing of the pole with \(E(y)\).  It
does not exhibit a positive measure against a positive kernel.

Thus the Pick/Stieltjes route is not a new finite estimate for the compact
core.  It is an infinite support theorem for the continued Euler--Gamma
object.

## Minimal theorem that would close the gate

The viable theorem is the following.

**Completed Pick/Stieltjes support theorem.** Construct, using only the
Euler product, the Gamma factor, the functional equation and the paired
boundary prescription, a positive Herglotz/Stieltjes representation for the
completed Li logarithmic derivative
\[
  \mathcal L(z)
  =
  {z\over(1-z)^2}
  {\xi'\over\xi}\!\left({1\over1-z}\right)
\tag{16}
\]
whose representing measure is supported on the admissible Li boundary
\(\partial\mathbb D\) in disk coordinates, equivalently on the critical line
in \(s\)-coordinates.

Equivalently, prove a positive boundary-measure formula of the form
\[
  {\xi'\over\xi}\left({1\over2}+w\right)
  =
  A(w)
  +
  \int_{\mathbb R}
  \left({1\over w-it}+{1\over w+it}\right)d\mu(t),
  \qquad
  \mu\ge0,
\tag{17}
\]
with all polynomial and archimedean terms explicitly harmless for the Li
tests.

This theorem would imply that the singularities of the completed object are
on the critical line, hence would imply RH and Omega7.  Conversely, under RH
the divisor side supplies the expected positive square formulas for the Li
coefficients.  Therefore the theorem is equivalent in strength to the
positive boundary measure target already isolated in the phase.

## Eliminated proof patterns

The following patterns do not close A1:

1. use \(\Lambda(m)\ge0\) in \(\Re s>1\) and ignore the pole-pairing term;
2. write the signed error \(E(y)=\psi(y)-y\) as if it were a positive
   measure;
3. construct the Riesz measure of \(\log|\xi|\) and call it a boundary
   measure without proving support on the critical line;
4. define a disk boundary measure from the transformed zeros before proving
   \(|1-1/\rho|=1\);
5. cancel nontrivial-zero poles by a correction that is not explicitly
   analytic and harmless for the Li coefficients.

Each pattern assumes, or hides, the support statement that the gate must
prove.

## Status

Closed as a no-go plus live theorem.

The prime-pole generator has an exact Stieltjes/Laplace representation only
in the Euler-product half-plane.  After pole pairing and Li continuation it
is a signed current whose singularities are the transformed zero divisor.
A Pick/Stieltjes proof strong enough to imply A1 must prove that this divisor
has collapsed to the admissible boundary.  That support-collapse theorem is
the minimal missing theorem; it is not supplied by the prime-pole generator
alone.
