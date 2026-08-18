# 106.200 — The charge-shifted Gamma connection and relative cone map

> **Post-audit status.**  Theorem 8.1 below is a correct conditional
> implication, but its closure hypothesis is not available for the
> Cauchy/Gamma Hilbert target.  Document 106.205 proves that every such
> charged pushout completion has absolutely continuous normalized-scale
> spectrum, whereas CCM degree one has nonzero resonant eigenclasses.
> Hence (24) is false for this concrete Hilbert realization.  The finite
> connection and cone identities remain valid source constructions.

## 1. Purpose

The scalar Gamma-compliance kernel of 106.199 is faithful before quotient,
but its scalar CCM restriction range is dense.  Therefore the arithmetic
charge labels must be retained until after the relative quotient.  Document
106.198 records the required diagonal law

\[
 K_\Gamma(E)_{q,q}
 =\kappa_\infty+m_\Gamma(E-\log q),
\tag{1}
\]

without constructing the corresponding closed connection on the complete
charge module.

This note constructs that connection.  It then packages the finite Euler
row and the complete Gamma row into a single co-diagonal relative
differential.  The quotient universal property gives an actual map of the
primitive CCM restriction cone at every finite prime level.  What remains
after this construction is no longer chain compatibility; it is the
cofinal Hilbert-closure identity.

## 2. The total charge generator

Let \(Q\subset\mathbb Q_+^\times\) be any countable multiplicative charge
set containing all prime powers and stable under the finite charge shifts
under consideration.  Put

\[
 \mathscr K_Q=\ell^2(Q)\widehat\otimes\mathscr K,
\tag{2}
\]

where \((\mathscr K,V_u=e^{iuA})\) is the common Cauchy coefficient
space.  On the algebraic charge core define

\[
 L_Qe_q=(\log q)e_q.
\tag{3}
\]

The operators \(L_Q\otimes I\) and \(I\otimes A\) strongly commute.
Hence

\[
 \boxed{
 A_Q=I\otimes A-L_Q\otimes I,
 \qquad
 W_u=e^{iuA_Q}}
\tag{4}
\]

is a strongly continuous unitary group.  On the \(q\)-fiber,

\[
 (W_uF)_q=e^{-iu\log q}V_uF_q.
\tag{5}
\]

The phase in (5) is the finite/infinite-place coupling.  Removing it would
return to the Euler-blind scalar induction of 106.189.

## 3. The closed charge-shifted Gamma gradient

With

\[
 g_\Gamma(u)={e^{-u/2}\over1-e^{-2u}},
\tag{6}
\]

define on the generator core

\[
 \boxed{
 (\mathcal G_{\Gamma,Q}F)(u)
 =\sqrt{2g_\Gamma(u)}(I-W_u)F.}
\tag{7}
\]

### Theorem 3.1 — Exact total-energy multiplier

The form defined by (7) is closable, and its closure satisfies

\[
 \boxed{
 \mathcal G_{\Gamma,Q}^*\mathcal G_{\Gamma,Q}
 =\mathcal J_{\Gamma,Q}
 =m_\Gamma(A_Q).}
\tag{8}
\]

Equivalently, on the joint spectral fiber \((q,\gamma)\),

\[
 \boxed{
 \mathcal J_{\Gamma,Q}(q,\gamma)
 =m_\Gamma(\gamma-\log q).}
\tag{9}
\]

#### Proof

For a vector in the joint spectral representation,

\[
 \|(I-W_u)F\|^2
 =|1-e^{iu(\gamma-\log q)}|^2\|F\|^2
 =2\bigl(1-\cos(u(\gamma-\log q))\bigr)\|F\|^2.
\tag{10}
\]

Multiplication by \(2g_\Gamma(u)\), integration, and the spectral theorem
give (8)--(9).  Near \(u=0\), the difference in (7) is \(O(u)\) on the
generator core while \(g_\Gamma(u)=1/(2u)+O(1)\); at infinity the density
decays exponentially.  The usual monotone form closure proves
closability. \(\square\)

## 4. The complete charged boundary row

Let \(B_\infty\) be the scalar finite-part row of 106.196, now tensored
with \(\ell^2(Q)\), and define

\[
 \boxed{
 \mathbb B_{\infty,Q}F
 =B_\infty F\oplus\mathcal G_{\Gamma,Q}F.}
\tag{11}
\]

### Theorem 4.1 — Strict charged compliance

\[
 \boxed{
 \mathbb B_{\infty,Q}^*\mathbb B_{\infty,Q}
 =K_{\Gamma,Q}
 :=\kappa_\infty I+m_\Gamma(A_Q)
 \succeq\kappa_\infty I.}
\tag{12}
\]

Thus \(K_{\Gamma,Q}^{-1}\) is bounded, and the minimum-norm right
inverse of \(\mathbb B_{\infty,Q}^*\) is

\[
 \boxed{
 (\mathbb B_{\infty,Q}^*)^\dagger
 =\mathbb B_{\infty,Q}K_{\Gamma,Q}^{-1}.}
\tag{13}
\]

#### Proof

The scalar and gradient rows have orthogonal targets.  Equations
106.196(5) and (8) give (12).  Strict positivity and the
Moore--Penrose calculation of 106.198 give (13). \(\square\)

Formula (12) is precisely (1), now as a closed operator identity rather
than a fiberwise prescription.

## 5. The charged shared-boundary pushout

Tensor the finite Tate source of 106.169 with the charge core and retain
its two boundary values

\[
 \partial_{T,S,Q}v=(R_{S,Q}J_Sv,R_{S,Q}v).
\tag{14}
\]

The map \(R_{S,Q}\) is taken before common-valuation collapse; it may mix
charge fibers.  Double the charged Gamma row and define

\[
 \boxed{
 \mathbb P_{S,Q}
 =\ker\left(
   \partial_{T,S,Q}\oplus
   (\mathbb B_{\infty,Q}^{(1)})^*
 \right).}
\tag{15}
\]

### Theorem 5.1 — Charged Schur polarization

After shorting the irrelevant kernel of the archimedean adjoint, the
canonical representative of \(v\) is

\[
 \left(
 v,
 -\mathbb B_{\infty,Q}^{(1)}
  (K_{\Gamma,Q}^{-1}\oplus K_{\Gamma,Q}^{-1})
  \partial_{T,S,Q}v
 \right),
\tag{16}
\]

and its metric is

\[
 \boxed{
 \begin{aligned}
 g_{S,Q}(v,w)
 &=g_S(v,w)\\
 &\quad+\langle K_{\Gamma,Q}^{-1}R_{S,Q}J_Sv,
                       R_{S,Q}J_Sw\rangle\\
 &\quad+\langle K_{\Gamma,Q}^{-1}R_{S,Q}v,
                       R_{S,Q}w\rangle .
 \end{aligned}}
\tag{17}
\]

It is positive definite, Hodge invariant, and preserves the complete
phase \(\gamma-\log q\).

#### Proof

Apply (13) independently to the two boundary components.  The squared
norm of the minimum lift of a boundary value \(b\) is
\(\langle K_{\Gamma,Q}^{-1}b,b\rangle\), which gives (17).  Positivity
is immediate.  The Hodge quarter-turn exchanges the two boundary
components and commutes with \(A_Q\), so it preserves (17). \(\square\)

## 6. A relative cone lemma

The following elementary statement records exactly how the pushout enters
the CCM restriction cone.

### Lemma 6.1 — Co-diagonal annihilation produces a cone map

Let \(\rho:A^\bullet\to B^\bullet\) be a morphism of complexes.  Let
\(L_E:B^\bullet\to E^\bullet\) and
\(L_\infty:B^\bullet\to I^\bullet\) be chain maps.  Suppose there are a
complex \(K^\bullet\), a chain map \(\eta:A^\bullet\to K^\bullet\), and
chain maps \(\Gamma:K^\bullet\to E^\bullet\),
\(B_\Gamma:K^\bullet\to I^\bullet\) such that

\[
 L_E\rho=\Gamma\eta,
 \qquad
 L_\infty\rho=B_\Gamma\eta.
\tag{18}
\]

Let \(P^\bullet=\mathrm{Coker}(\Gamma,B_\Gamma)\), with quotient
map \(\pi:E^\bullet\oplus I^\bullet\to P^\bullet\).  Then

\[
 \boxed{
 D=\pi(L_E,L_\infty):B^\bullet\longrightarrow P^\bullet}
\tag{19}
\]

is a chain map satisfying \(D\rho=0\).  It therefore induces a chain map
from \(\mathrm{Cone}(\rho)\), and in degree one a map from the
algebraic cokernel of \(\rho\).

#### Proof

Every map in (19) is a chain map.  Equations (18) give

\[
 D\rho
 =\pi(\Gamma\eta,B_\Gamma\eta)=0
\tag{20}
\]

by the definition of the cokernel.  The universal properties of the
mapping cone and cokernel give the asserted induced maps. \(\square\)

## 7. Application gate for the primitive CCM coefficient cone

After cyclic orbit trace and the first Eulerian projector, the intended
substitution in Lemma 6.1 is

\[
 \begin{aligned}
 L_E&=\mathcal L_{\rm conn}\mathfrak e_1
       \mathrm{Tr}_{\rm orb},\\
 B_\Gamma&=\mathbb B_{\infty,Q}^{(1)},\\
 \Gamma&=\Gamma_{S,Q}.
 \end{aligned}
\tag{21}
\]

The first identity in (18) is the generic Tate restriction identity
106.169(13b), after the local Fourier descent of 106.173.  For the second
identity, 106.172 proves only the scalar zero-mode row, while 106.176
proves equality of the nonzero Gamma *quadratic form*.  Neither statement
by itself is a chain identity on the complete nuclear restriction cone.

Let \(L_{\infty}^{\rm CCM}\) denote the actual archimedean localization
of that cone and define the chain defect

\[
 \boxed{
 \Delta_{\Gamma,S}
 :=L_{\infty}^{\rm CCM}\rho_S^\natural
   -\mathbb B_{\infty,Q}^{(1)}\eta_S.}
\tag{22}
\]

### Proposition 7.1 — Exact finite cone-map criterion

For a finite prime set \(S\), the charged localization induces a
complex-linear Hodge-equivariant map

\[
 D_{S,Q}:H^1\!\left(\mathrm{Cone}(\rho_S^\natural)\right)
 \longrightarrow\mathbb P_{S,Q}
\tag{23}
\]

if and only if the image of \(\Delta_{\Gamma,S}\) vanishes in the
co-diagonal cokernel.  In particular, the stronger identity
\(\Delta_{\Gamma,S}=0\) is sufficient.  When these identities are
compatible under adjoining primes, the maps (23) are cofinally
compatible and intertwine normalized real scaling.

#### Proof

The finite Euler component already satisfies the first equality in (18).
After applying the cokernel quotient, the only remaining value of
\(D\rho\) is the class of \(\Delta_{\Gamma,S}\).  Hence the map descends
exactly when that class is zero.  Lemma 6.1 proves sufficiency of the
stronger identity.  Cofinal and scaling compatibility then follow from
the corresponding identities of every row. \(\square\)

This proposition prevents a quadratic-form identity from being silently
promoted to a chain map.  The charged connection is now explicit, but its
comparison with the actual archimedean CCM differential remains a
well-defined calculation, namely (22).

## 8. The remaining cofinal theorem

Assume first that the defects (22) vanish compatibly, and let \(D_Q\) be
the algebraic direct limit of (23).  Let
\(\mathcal V\) be the closed CCM restriction range in the nuclear
Schwartz/Meyer topology.  The remaining statement is

\[
 \boxed{
 D_Q^{-1}\!\left(
   \overline{D_Q(\mathcal V)}^{\,\mathbb P_{\infty,Q}}
 \right)=\mathcal V.}
\tag{24}
\]

Unlike the scalar collapse excluded by Theorem 5.1 of 106.199, (24)
retains the full charge-dependent multiplier (9) and the charge-mixing
Tate boundary.  It is therefore the first closure gate not already reduced
to a nonzero scalar multiplier almost everywhere.

If (24) holds, the quotient norm is faithful and normalized scaling is
unitary.

### Theorem 8.1 — Closure faithfulness completes the alternative polarization

Assume (24), cofinal compatibility of the maps (23), and their already
proved complex and normalized-scale equivariance.  Let

\[
 \mathscr H_Q
 =\overline{D_Q(\mathscr D_c)}^{\,\mathbb P_{\infty,Q}}
  \big/
  \overline{D_Q(\mathcal V)}^{\,\mathbb P_{\infty,Q}}.
\tag{25}
\]

Then the induced map

\[
 \overline D_Q:H^1_{\rm CCM}\longrightarrow\mathscr H_Q
\tag{26}
\]

is injective.  Pullback of the quotient Hilbert metric, complex structure,
and alternating form gives on the existing CCM degree one

\[
 \boxed{
 \begin{aligned}
 g_Q(u,v)&=langle\overline D_Qu,\overline D_Qv\rangle,\\
 J_Qu&=iu,\\
 \Omega_Q(u,v)&=g_Q(J_Qu,v).
 \end{aligned}}
\tag{27}
\]

The form \(g_Q\) is positive definite, \(J_Q^2=-I\),
\(\Omega_Q\) is alternating and nondegenerate, and normalized scaling is
unitary.  Hence (24) alone, after the finite chain identities, completes
the alternative global polarization; no equality with the Rosati metric
is additionally required.

#### Proof

The kernel of the map induced by \(D_Q\) in (25) is exactly the left side
of (24), modulo \(\mathcal V\).  Equation (24) therefore makes (26)
injective.  The restriction range and its closure are invariant under the
finite-level complex structure and normalized flow, so both descend to
the Hilbert quotient.  Pullback along the injective complex-linear map
(26) gives (27).  Positivity and nondegeneracy follow from injectivity;
the remaining polarization identities and unitary scaling are inherited
from the charged pushout. \(\square\)

This is the alternative-polarization branch of 106.184 in its final
source-defined form.  The fixed-Rosati branch would require the stronger
symplectic comparison of 106.199, but it is not needed once (24) is proved.

## 9. Status

Proved without RH or zero input:

* the self-adjoint total charge generator \(A_Q=A-L_Q\);
* the closed charge-shifted Gamma connection;
* the exact multiplier \(m_\Gamma(\gamma-\log q)\);
* the strictly positive charged compliance and its right inverse;
* the charged Schur polarization retaining all prime phases;
* the co-diagonal cone lemma;
* the exact chain defect (22) whose vanishing is necessary and sufficient
  for the finite relative map.

Still required:

* vanishing of the Gamma chain defect (22) on the complete nuclear cone;
* the cofinal Hilbert-closure identity (24).
