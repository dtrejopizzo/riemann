# Strip Green pole-defect decomposition

## Purpose

`178_STRIP_POISSON_BOUNDARY_NO_GO.md` shows that favorable boundary signs in
the strip
\[
  {1\over2}<\Re s<1
\]
do not prove positivity of
\[
  u(s)=\Re{\xi'\over\xi}(s)
\]
unless interior poles are already excluded.

This note records the exact local defect created by such an interior pole.
It is the analytic version of the off-line geometric mode: every off-line
zero creates a sign-changing pole kernel inside the strip.

## Local pole defect

Let \(\rho=\beta+i\gamma\) be a zero of \(\xi\) of multiplicity \(m\), with
\[
  {1\over2}<\beta<1.
\]

Near \(\rho\),
\[
  {\xi'\over\xi}(s)
  =
  {m\over s-\rho}+h(s),
\tag{1}
\]
where \(h\) is holomorphic.

The real part of the principal term is
\[
  D_\rho(s)
  :=
  m\,\Re{1\over s-\rho}
  =
  m\,{\sigma-\beta\over(\sigma-\beta)^2+(t-\gamma)^2},
  \qquad s=\sigma+it.
\tag{2}
\]

Thus
\[
  D_\rho(s)<0\quad\hbox{for }\sigma<\beta,
  \qquad
  D_\rho(s)>0\quad\hbox{for }\sigma>\beta.
\tag{3}
\]

The negative lobe lies inside the target half-strip because
\[
  {1\over2}<\sigma<\beta.
\]

Therefore any zero with \(\beta>1/2\) produces an explicit local negative
defect for the desired inequality
\[
  \Re{\xi'\over\xi}(s)\ge0.
\]

## Quartet under the functional equation

The functional equation and conjugation symmetry attach to \(\rho\) the
quartet
\[
  \rho,\quad \overline{\rho},\quad 1-\rho,\quad 1-\overline{\rho}.
\]

The two zeros with real part \(>1/2\) are
\[
  \rho=\beta+i\gamma,\qquad \overline{\rho}=\beta-i\gamma.
\]

Their right-half pole defect is
\[
  D_{\rho,\overline{\rho}}(s)
  =
  m\,\Re{1\over s-\rho}
  +
  m\,\Re{1\over s-\overline{\rho}}.
\tag{4}
\]

For \(s=\sigma+i\gamma\),
\[
  D_{\rho,\overline{\rho}}(\sigma+i\gamma)
  =
  {m\over\sigma-\beta}
  +
  m\,{\sigma-\beta\over(\sigma-\beta)^2+(2\gamma)^2}.
\tag{5}
\]

As \(\sigma\uparrow\beta\) from the left, the first term tends to
\[
  -\infty.
\]

Hence the quartet defect cannot be compensated by bounded boundary data in
a punctured neighborhood.  Positivity in the strip is impossible if such a
zero exists.

This is the local analytic reason that the half-plane positivity theorem is
equivalent to RH.

## Green formula interpretation

On a truncated rectangle
\[
  R_{T,\varepsilon}
  =
  \{1/2+\varepsilon<\sigma<1,\ |t|<T\}
\]
with small disks around interior zeros removed, \(u=\Re(\xi'/\xi)\) is
harmonic.  Green's formula expresses \(u(s)\) as:

1. Poisson contributions from the vertical sides;
2. horizontal-side contributions;
3. small-circle contributions around the removed zeros.

The vertical sides have the favorable signs recorded in `178`.  The
small-circle terms converge exactly to the pole defects (2).  These terms
are sign-changing and have negative blow-up on the left of an off-line zero.

Thus a strip-boundary proof must either:

- prove there are no such small-circle terms; or
- produce a new positive Euler--Gamma mechanism that cancels every negative
  pole defect without already assuming the zero is absent.

The first option is RH.  The second is the still-missing sign theorem.

## Relation to A1 and Li modes

The local pole defect is the analytic half-plane counterpart of the Li disk
exterior mode.  In disk coordinates
\[
  w_\rho=1-{1\over\rho},
\]
a zero with \(\beta>1/2\) corresponds to
\[
  |w_\rho|<1
\]
for the \(s\)-half-plane singularity of \(\xi'/\xi\), and to a non-boundary
singularity for the Carathéodory object.  The pole-defect negativity is the
same obstruction as the negative geometric Li subsequence in zero-side
language.

For compact A1, this means that any proof must neutralize these local pole
defects through the global pole-prime-Gamma pairing before applying
one-sided estimates.

## Exact no-go statement

The following proof pattern is invalid:

1. use boundary signs on \(\Re s=1/2\) and \(\Re s=1\);
2. ignore or remove interior pole disks;
3. conclude \(\Re(\xi'/\xi)\ge0\) in the strip.

The missing terms from step 2 are precisely the pole defects (2), and they
have negative blow-up if an off-line zero exists.

## Status

Closed as a pole-defect normal form.  A1 remains open.

The live strip target is now: prove, from Euler--Gamma data, that no
negative pole defects occur, or construct a global positive mechanism that
dominates them without assuming their absence.
