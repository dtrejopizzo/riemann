# 106.197 — Derived injectivity of the CCM localization into the pushout

## 1. Purpose

Document 106.196 constructs the positive Gamma--Euler--polar pushout but
leaves its comparison with CCM degree one open.  This note constructs the
nuclear localization morphism and proves its derived injectivity.

The decisive point is that the pushout is a graph over the complete Tate
coefficient space.  It does not apply the middle projection and therefore
does not discard the primitive orbit labels.  One fixed nonzero orbit
coefficient, followed through all scale translates and infinitesimal
jets, recovers the exact Schwartz topology by 106.175.

The result closes the kernel part of the comparison.  The equality of the
positive pushout metric with the CCM Rosati/Green form remains separate.

## 2. Primitive coefficient localization

Work first in one compact-character sector of the scalar CCM target and
write it as \(\mathcal S(\mathbb R)\) in logarithmic coordinate.  Let

\[
 G=\log\mathbb Q_+^\times,
 \qquad
 D=\frac d{dt},
 \qquad
 (T_gF)(t)=F(t+g).                                         \tag{1}
\]

Let \(\mathrm{Tr}_{\rm orb}\) be the CCM cyclic diagonal orbit
trace, \(\mathfrak e_1\) the primitive Eulerian projector of 106.174, and
\(\mathcal L_{\rm conn}\) its connected Tate localization.  The
primitive coefficient identity 106.174(17) says that the \((p,k)\) row
of the resulting coefficient vector is

\[
 \boxed{
 E_{p,k}\mathcal L_{\rm conn}\mathfrak e_1
 \mathrm{Tr}_{\rm orb}F
 =p^{-k/2}F(k\log p).}                                     \tag{2}
\]

Let \(\iota_{\rm po}\) denote the graph embedding (15) of 106.196.  It
retains its Tate argument as its first coordinate, so there are continuous
coefficient extractions, still denoted \(E_{p,k}\), satisfying

\[
 E_{p,k}\iota_{\rm po}=E_{p,k}.                            \tag{3}
\]

For the injectivity argument no separate Gamma coordinate is needed: the
canonical archimedean boundary lift is already part of
\(\iota_{\rm po}\), and the primitive Tate coordinate is its graph base.
Define the base localization

\[
 \boxed{
 \mathfrak L
 =\iota_{\rm po}\mathcal L_{\rm conn}\mathfrak e_1
     \mathrm{Tr}_{\rm orb}.}                        \tag{4}
\]

All factors in (4) were constructed before taking the CCM quotient and
use only local Fourier transform, the Euler product, and the canonical
primitive--Gamma boundary lift.  The positive Gamma spin interior and
the polar determinant page are attached when comparing forms; they are
not required to prove that the finite-place coefficient observation is
faithful.

## 3. Jet-prolonged localization

Let \(\mathscr P\) denote the algebraic/nuclear target of (4).  Give
\(\mathscr P^{G\times\mathbb N_0}\) the projective product topology on
the image below and define

\[
 \boxed{
 \mathfrak L_\infty F
 =\bigl(\mathfrak L(D^nT_gF)\bigr)_{g\in G,\ n\ge0}.}       \tag{5}
\]

The derivatives are the infinitesimal descendants of the CCM scaling
action, not additional arithmetic data.

### Theorem 3.1 — A single primitive orbit reconstructs every jet

For all \(g\in G\) and \(n\ge0\),

\[
 \boxed{
 \sqrt2\,E_{2,1}\mathfrak L(D^nT_gF)
 =F^{(n)}(g+\log2).}                                      \tag{6}
\]

Consequently the complete jet observation

\[
 \mathcal O_\infty F=(F^{(n)}(g))_{g\in G,n\ge0}          \tag{7}
\]

factors through \(\mathfrak L_\infty\) by a continuous coordinate
permutation and scalar multiplication.

#### Proof

Equations (2)--(3), with \(p=2,k=1\), give

\[
 E_{2,1}\mathfrak L(D^nT_gF)
 =2^{-1/2}(D^nT_gF)(\log2)
 =2^{-1/2}F^{(n)}(g+\log2),                                \tag{8}
\]

which is (6).  Since \(G+\log2=G\), the right sides in (6) are exactly
all coordinates in (7). \(\square\)

## 4. Topological and quotient faithfulness

### Theorem 4.1 — Nuclear localization is a topological embedding

The map

\[
 \mathfrak L_\infty:\mathcal S(\mathbb R)\longrightarrow
 \mathscr P^{G\times\mathbb N_0}                           \tag{9}
\]

is injective and is a homeomorphism onto its image when that image is
equipped with the natural rapid jet seminorms.

#### Proof

Every component of (5) is continuous on the Schwartz space.  Theorem
3.1 supplies a continuous recovery map from \(\mathrm{Ran}
\mathfrak L_\infty\) to \(\mathrm{Ran}\,\mathcal O_\infty\).
Theorem 3.1 of 106.175 gives the exact seminorm identity

\[
 \sup_{g\in G}(1+|g|)^m|F^{(n)}(g)|
 =\sup_{t\in\mathbb R}(1+|t|)^m|F^{(n)}(t)|.                \tag{10}
\]

Thus the inverse on the image is continuous, and injectivity follows
already from the zeroth jets. \(\square\)

Let \(\mathcal V\) be the closed CCM restriction range in the strong
Schwartz/Meyer topology.

### Corollary 4.2 — Derived kernel identity

\[
 \boxed{
 \mathfrak L_\infty^{-1}
 \left(\overline{\mathfrak L_\infty(\mathcal V)}\right)
 =\mathcal V.}                                             \tag{11}
\]

Hence \(\mathfrak L_\infty\) induces an injective topological map

\[
 \boxed{
 \mathbf S(C_\mathbb Q)/\mathcal V
 \hookrightarrow
 \mathrm{Ran}\,\mathfrak L_\infty/
 \overline{\mathfrak L_\infty(\mathcal V)}.}              \tag{12}
\]

After cyclic Morita reduction, (12) applies to the complete scalar
diagonal degree-one CCM target.

#### Proof

Theorem 4.1 is a homeomorphism onto its image, so it preserves closures.
This proves (11), and the quotient universal property gives (12).  The
matrix-field statement follows from the cyclic trace and rank-one chain
section used in 106.175(5). \(\square\)

## 5. Equivariance and why the pushout matters

Translation of the index \(g\) in (5) gives the full real CCM scaling
action by continuity from the dense subgroup \(G\).  The base pushout
already has a unitary normalized real flow by Theorem 5.1 of 106.196, and
the coefficient extraction (6) intertwines the two actions.

Had the ordinary middle projection \(P_S^{\rm mid}\) been applied before
the archimedean attachment, the generic Hodge plane containing (6) could
have been removed.  In the shared-boundary pushout it is instead stored
in the canonical archimedean lift

\[
 -\kappa_\infty^{-1}(B_\infty\oplus B_\infty)
 \partial_{T,S}v,                                          \tag{13}
\]

so the primitive coefficient remains recoverable.  This is the exact
role of the non-free gluing in the injectivity proof.

## 6. Remaining metric comparison

Corollary 4.2 proves that no separated CCM class is lost by the complete
derived localization.  It does not yet prove that the positive metric of
106.196 is the desired intersection metric.  The remaining identity is

\[
 \boxed{
 \Omega_{\rm Ros}(u,v)
 =\Omega_{\rm po}(\mathfrak L_\infty u,
                  \mathfrak L_\infty v),}                  \tag{14}
\]

with the right side interpreted through the compatible nuclear sum of
jet descendants rather than an arbitrary new norm.  Equation (14) is a
chain-level Green/Lefschetz identity.  Its local prime coefficients, its
Gamma determinant, its polar term, its normalization, and its kernel are
now fixed; only the global equality of the two alternating pairings
remains.

## 7. Status

Proved without RH or zero input:

* construction of the complete jet-prolonged localization into the
  shared-boundary pushout;
* explicit recovery of every translated jet from the literal \((2,1)\)
  primitive orbit;
* topological embedding in every compact-character sector;
* preservation of the closed CCM restriction range;
* derived injectivity on the separated CCM quotient;
* compatibility with the normalized scaling action.

Still required:

* the global alternating Green identity (14);
* a compatible Hilbert completion of its nuclear right-hand side;
* application of 106.191--106.190 to obtain the final polarization.
