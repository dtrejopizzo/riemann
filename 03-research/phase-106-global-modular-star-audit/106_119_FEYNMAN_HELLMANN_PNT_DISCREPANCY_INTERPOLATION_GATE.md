# 106.119 — Feynman--Hellmann PNT-discrepancy interpolation gate

## Purpose and verdict

The compensated identity of 106.66 suggests switching on the actual signed
prime discrepancy continuously.  This is the affine form path

\[
 \mathfrak a_s=\mathfrak a_0+s\mathfrak r_\psi,
 \qquad 0\le s\le1,                                      \tag{1}
\]

where the endpoint \(s=1\) is the complete ordinary-prime--Gamma
generator and the endpoint \(s=0\) already has the critical lower bound
\(1/2\).  This note performs the interpolation after the complete Riemann
radical has been removed.

The calculation gives an exact endpoint criterion, but not an automatic
closure.  The bottom of an affine self-adjoint family is concave, so its
curvature has the wrong sign for transporting a lower bound from \(s=0\)
to \(s=1\).  If a subthreshold state exists at \(s=1\), its
Feynman--Hellmann slope is necessarily strictly negative.  Consequently
the strongest surviving interpolation statement is

\[
 \boxed{
 \sup_{\substack{q\in E_1\\\|q\|=1}}
 \int_0^\infty J_u(q)\,dD(u)\ge0,}                 \tag{2}
\]

where \(E_1\) is the bottom eigenspace of the completed operator whenever
that bottom is below \(1/2\).  Formula (2) would exclude a subthreshold
state, but it is itself a state-dependent signed correlation for the real
von Mangoldt discrepancy.  Neither concavity, the endpoint radical, nor a
moving radical constraint proves it.

Thus the interpolation is useful as a sharp localization of the missing
sign, not as an independent proof of the physical surplus.

## 1. Nonduplication audit

The following earlier deformations were checked before introducing (1).

* `104_41` and `104_47` deform the Cayley/Laguerre parameter and obtain a
  zero-residue flux; their obstruction is the residue sum crossed during
  the deformation.
* `106_21` varies the spatial cutoff.  It is a nested-domain compression,
  not an affine signed perturbation; its bottom can only decrease.
* `106_83` and `106_85` vary a **positive** response block after adaptive
  regression.  Their increasing concave Schur gain is not the bottom of
  the signed PNT-discrepancy family.
* `106_101` varies a positive trace-class boost and uses
  Feynman--Hellmann to compute the relative spectral-shift density.  It
  detects, rather than excludes, a subthreshold state.

The path (1), and especially its endpoint-slope identity after fixed
radical shorting, is therefore not one of those previous flows.

## 2. The exact affine path

Work in the centered complete radical complement

\[
 \mathscr C=(\mathbf1\oplus\mathcal R)^\perp
 \subset L^2_{\rm even}(\mu_K).                    \tag{3}
\]

For \(q\) in the common form core put

\[
 J_u(q)=\int_{\mathbb R}K(x)K(x-u)
             |q(x)-q(x-u)|^2\,dx.                 \tag{4}
\]

Use the locally finite weighted-prime discrepancy

\[
 D(U)=\sum_{\log n\le U}{\Lambda(n)\over\sqrt n}
       -2(e^{U/2}-1)                               \tag{5}
\]

and the positive completed Gamma remainder

\[
 r_\Gamma(u)={e^{-5u/2}\over1-e^{-2u}}.            \tag{6}
\]

The exact compensated-measure identity of 106.66 is

\[
 \mathscr E_K(q)
 ={1\over2}\|q\|^2
 +\int_0^\infty r_\Gamma(u)J_u(q)\,du
 +\int_0^\infty J_u(q)\,dD(u).                    \tag{7}
\]

Accordingly define

\[
\begin{aligned}
 \mathfrak a_0[q]
  &={1\over2}\|q\|^2+
    \int_0^\infty r_\Gamma(u)J_u(q)\,du,\\
 \mathfrak r_\psi[q]
  &=\int_0^\infty J_u(q)\,dD(u),\\
 \mathfrak a_s[q]
  &=\mathfrak a_0[q]+s\mathfrak r_\psi[q].        \tag{8}
\end{aligned}
\]

Then

\[
 \boxed{\mathfrak a_0\ge\tfrac12 I,
 \qquad \mathfrak a_1=\mathscr E_K|_{\mathscr C}.} \tag{9}
\]

For every finite heat Galerkin space \(V\subset\mathscr C\) all forms in
(8) are finite matrices.  Let

\[
 \alpha_V(s)=\min_{\substack{q\in V\\\|q\|=1}}
                    \mathfrak a_s[q].              \tag{10}
\]

The same formulas hold for an isolated full-space branch.  Stating the
finite theorem first avoids any unproved relative-form-boundedness claim
at \(s=0\).

## 3. Exact Feynman--Hellmann and curvature formulas

### Theorem 1 — Concavity and endpoint slopes

The function \(\alpha_V\) is concave and locally Lipschitz.  If \(E_s\)
is its ground eigenspace, then

\[
\boxed{
 \alpha'_{V,+}(s)=
 \min_{\substack{q\in E_s\\\|q\|=1}}\mathfrak r_\psi[q],
 \qquad
 \alpha'_{V,-}(s)=
 \max_{\substack{q\in E_s\\\|q\|=1}}\mathfrak r_\psi[q].} \tag{11}
\]

On a simple branch, with normalized eigenvector \(q_s\),

\[
 \boxed{\alpha_V'(s)=\mathfrak r_\psi[q_s].}       \tag{12}
\]

If \(\lambda_k(s)>\alpha_V(s)\) and \(q_k(s)\) are the remaining
eigenpairs, then

\[
\boxed{
 \alpha_V''(s)
 =-2\sum_{k>0}
 { |\mathfrak r_\psi(q_k(s),q_s)|^2
   \over \lambda_k(s)-\alpha_V(s)}\le0.}          \tag{13}
\]

#### Proof

Equation (10) is the infimum of affine functions of \(s\), hence is
concave.  The one-sided derivative formula for a minimum of finitely many
active Rayleigh branches gives (11).  Differentiating the eigenvalue
equation in the simple case gives (12).  Resolving \(q_s'\) in the
orthogonal eigenbasis gives (13).  \(\square\)

At crossings, (11) is the complete replacement for (12)--(13); no choice
of branch can improve its sign.

### Corollary 2 — The tangent points in the wrong direction

Concavity gives

\[
 \alpha_V(1)\le\alpha_V(0)+\alpha'_{V,+}(0),
 \qquad
 \alpha_V(1)\ge\alpha_V(0)+\alpha'_{V,-}(1).      \tag{14}
\]

The first inequality is an upper bound.  The only endpoint lower bound
available from the interpolation is the second one, and therefore it
requires a lower bound for the **final** signed slope.

## 4. The exact final-slope exclusion criterion

### Theorem 3 — A subthreshold endpoint forces negative signed work

Assume that the completed endpoint has

\[
 \alpha_V(1)<\frac12.                              \tag{15}
\]

Then every normalized \(q\in E_1\) satisfies

\[
\boxed{
 \mathfrak r_\psi[q]
 =\alpha_V(1)-\mathfrak a_0[q]
 \le\alpha_V(1)-\frac12<0.}                       \tag{16}
\]

Consequently

\[
 \boxed{\alpha'_{V,-}(1)<0.}                      \tag{17}
\]

Conversely, either of

\[
 \alpha'_{V,-}(1)\ge0,
 \qquad
 \exists q\in E_1,\ \|q\|=1:\
       \mathfrak r_\psi[q]\ge0                   \tag{18}
\]

excludes (15).

#### Proof

For \(q\in E_1\), (8) gives

\[
 \alpha_V(1)=\mathfrak a_0[q]+\mathfrak r_\psi[q].
\]

Use \(\mathfrak a_0[q]\ge1/2\) and then (11).  \(\square\)

The same result holds for the full operator.  By the essential-threshold
theorem, a bottom below \(1/2\) is an isolated finite-multiplicity
eigenvalue.  Heat-core Rayleigh--Ritz exhaustion approximates its
eigenspace in form norm, so (16) passes to that cluster.  Hence the exact
full-space survivor is (2).

There is also an integrated form.  Along any absolutely continuous ground
branch,

\[
 \boxed{
 \alpha(1)-\alpha(s_*)
 =\int_{s_*}^1\mathfrak r_\psi[q_s],ds.}          \tag{19}
\]

If a branch enters below \(1/2\) at \(s_*\), the right side is negative.
Thus proving its nonnegativity would close the floor, but that is exactly
the signed PNT/profile correlation along the self-consistent ground state.

## 5. The radical constraint adds no favorable derivative

The correct endpoint constraint is the fixed space (3).  The complete
radical is an exact threshold reducing eigenspace for \(\mathfrak a_1\),
so compression to \(\mathscr C\) is exact at the endpoint even though the
separate terms in (8) need not preserve \(\mathscr C\).

For completeness, suppose one instead postulates a differentiable moving
projection \(Q_s\) and transports \(Q_sA_sQ_s\) unitarily to a fixed
space.  If \(\Omega_s\) is the skew connection of that transport,
Feynman--Hellmann gives

\[
 \alpha'(s)
 =\langle q_s,R_\psi q_s\rangle
  +\langle q_s,[A_s,\Omega_s]q_s\rangle.           \tag{20}
\]

If \(Q_s\) is genuinely self-consistent, meaning that it reduces \(A_s\),
then \(A_sq_s=\alpha(s)q_s\) and the commutator expectation in (20)
vanishes exactly.  Formula (12) returns.  If \(Q_s\) is not reducing, the
extra term has no sign and is not a radical identity.

Likewise, differentiating a hypothetical moving threshold vector
\(A_sr_s=\frac12r_s\) gives

\[
 (A_s-\tfrac12)\dot r_s=-R_\psi r_s.              \tag{21}
\]

Solving (21) requires the reduced resolvent at the threshold; it is
singular at the essential edge and its Schur correction is negative, not
a positive surplus.  Thus moving the radical cannot reverse (13).

## 6. Finite exact obstruction

The failure is not caused by domains or crossings.  On
\(\mathbb C r\oplus\mathbb C e_-\oplus\mathbb C e_+\), let

\[
 A_0=\mathrm{diag}
 \left(\frac12,\frac12+\delta,\frac12+M\right),
 \qquad
 R=\mathrm{diag}
 \left(0,-\delta-\varepsilon,\delta+\varepsilon\right),       \tag{22}
\]

with \(\delta,\varepsilon,M>0\).  The vector \(r\) is an exact threshold
radical for every \(s\), the complement is reducing, \(A_0\ge1/2\), and
the perturbation is trace neutral.  Nevertheless

\[
 \alpha_{r^\perp}(s)
 =\frac12+\delta-s(\delta+\varepsilon)
 \quad\hbox{near }s=1,                             \tag{23}
\]

so

\[
 \alpha_{r^\perp}(1)=\frac12-\varepsilon<\frac12. \tag{24}
\]

This model satisfies the endpoint radical, exact affine interpolation,
Feynman--Hellmann, concavity and a compensated signed perturbation.  It
proves that no implication from those structural facts alone can establish
the desired endpoint floor.

## 7. Final gate

The interpolation reduces the physical-surplus problem to the following
strictly state-adapted statement:

> For every isolated bottom cluster of the completed ordinary-prime--Gamma
> operator on \((\mathbf1\oplus\mathcal R)^\perp\), at least one normalized
> bottom state satisfies
> \[
> \int_0^\infty J_u(q)\,dD(u)\ge0.
> \]

This statement uses the signs of all real \(\Lambda(n)\) jumps and all
continuous PNT intervals simultaneously.  It is not supplied by
Feynman--Hellmann: it is the endpoint input that Feynman--Hellmann exposes.
The affine path therefore closes as an exact obstruction/localization, not
as a proof of the physical surplus.

