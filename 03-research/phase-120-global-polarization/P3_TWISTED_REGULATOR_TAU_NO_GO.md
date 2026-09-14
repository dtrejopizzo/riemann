# Phase 120 — twisted-regulator tau gate

## Verdict

The Mellin local-system variant does not escape
`P3_DERIVED_THETA_TAU_GATE.md`.  In the purely cohomological regulator
pairing, the twist on a self-pair cancels against its dual.  If an analytic
Green operator is added so that the twist survives, the construction becomes
the already built Hurwitz/Quillen Gamma determinant; assembling graph cycles
then gives the same ratio-character kernel as the G-1 linear realization.
The moving-regulator candidate is retired as an independent route.

## 1. Coefficient twist

Let (mathcal L_	au) be the unitary Mellin local system and let
(chi_	au(n)=n^{-i	au}).  Functoriality of the graph correspondence labelled
by (n) gives, on the regulator realization,

\[
 r_	au(Z_n)=\chi_	au(n)r_0(Z_n).                    \tag{1.1}
\]

The Hermitian pairing uses the duality

\[
 mathcal L_	au\otimes\mathcal L_{-	au}
 \longrightarrow\mathbf1.                            \tag{1.2}
\]

Therefore, for one graph cycle,

\[
 \langle r_	au(Z_n),r_	au(Z_n)\rangle
 =|\chi_	au(n)|^2
  \langle r_0(Z_n),r_0(Z_n)\rangle
 =\langle r_0(Z_n),r_0(Z_n)\rangle.                  \tag{1.3}
\]

Thus the proposed one-cycle gate cannot produce a nonconstant Gamma
multiplier from a topological Deligne/regulator cup pairing.

For a linear combination (Z(F)=\sum_mF_mZ_m), put
(H_{mn}=\langle r_0(Z_m),r_0(Z_n)\rangle).  Then

\[
 \langle r_	au Z(F),r_	au Z(F)\rangle
 =\sum_{m,n}F_m\overline{F_n}(m/n)^{-i\tau}H_{mn}.    \tag{1.4}
\]

Equivalently (H_	au=D_	au H D_	au^*), where (D_	au) is diagonal
unitary.  The family has constant inertia; its apparent spectral dependence
is the external Mellin modulation already displayed in equation (7) of
`P3_DERIVED_THETA_TAU_GATE.md`.

## 2. Analytic twist

A nonconstant self-pair can be obtained only by allowing the harmonic
representative or Green operator itself to depend on the twisted differential

\[
 d_	au=d+i\tau\,d\theta.                             \tag{2.1}
\]

The spectrum of the resulting circle/Hardy Laplacian is shifted by (	au).
Its regularized determinant is a Hurwitz/analytic-torsion function and, on the
quarter-twisted half-density carrier, produces

\[
 \log\pi-\operatorname{Re}\psi(1/4+i\tau/2).          \tag{2.2}
\]

But (2.2) is exactly the quarter-Gamma determinant already constructed in
phase 120.  It is forced by the local functional equation and supplies no
global prime coupling or Hodge sign.

When graph cycles are inserted, their coefficient dependence is still (1.4).
Proving that the resulting analytic height equals or dominates the Weil form
requires an additive realization of the complete primitive test module in a
polarized space.  This is amended Gap G-1 and is equivalent in strength to row
(d).  Defining the cycles or Green metric to force that comparison is circular.

## 3. Shifted-pair discrimination

For real (	au), (chi_	au) is unitary.  The shifted pair replaces it
locally by

\[
 n^{a-i\tau}\oplus n^{-a-i\tau},                     \tag{3.1}
\]

which is rank two and nonunitary in each shifted summand.  This correctly
distinguishes (Xi_a) at the coefficient level, but it does not help with the
global comparison: unitarity gives positivity of the coefficient metric, not
negativity of the Weil form.  Dedekind zeta retains unitary rank-one local
systems and its global sign remains GRH.

## 4. Final classification

* topological twisted regulator: (	au) cancels on self-pairs;
* cross-pairs: (	au) is only external unitary conjugation;
* analytic twisted regulator: (	au) survives, but yields the already built
  Hurwitz/Quillen Gamma carrier;
* comparison with the prime side: returns to G-1;
* independent moving-regulator route: **closed negatively**.

