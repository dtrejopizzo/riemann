# 106.171 — Bott--cyclic comparison for the phase-thickened CCM cone

## 1. Purpose

The phase Toeplitz class of 106.170 produces the correct local sign. This
note proves that the same phase is globally compatible with the relative
cyclic construction of CCM. The proof is formal at the level where it
should be formal: smooth cyclic Bott periodicity.

Tensoring the complete CCM relative mixed complex with
\(C^\infty(\mathbb S^1)\) creates an even and an odd de Rham summand.
External product with the normalized phase class identifies the original
CCM complex with the odd summand, and phase integration is its inverse.
The Toeplitz boundary realizes minus this inverse. Hence adding the Tate
phase does not change or postulate the zero-carrying cohomology; it gives
that cohomology its required odd geometric orientation.

This closes the Bott/cyclic clause left in 106.170. It does not yet prove
that Tate-orbit localization is faithful or that the CCM Rosati form is
positive.

## 2. Periodic mixed complexes

Let \(\mathfrak C_{\rm CCM}\) denote the nuclear relative mixed complex

\[
 \mathrm{Cone}\,\!\left(
 \mathscr S(\mathcal G_{\mathbb Q})^\natural_0
 \xrightarrow{\rho^\natural}
 \mathbf S^\natural(C_{\mathbb Q},
                    \mathcal L^1(\mathcal H_x))
 \right).                                                    \tag{1}
\]

Write \(CC^{\rm per}(\mathfrak C_{\rm CCM})\) for its
\(\mathbb Z/2\)-graded periodic total complex with differential \(b+B\).
All tensor products below are completed projective tensor products on the
common nuclear core.

For the phase circle put

\[
 \eta=\frac{d\theta}{2\pi}\in\Omega^1(\mathbb S^1),\qquad
 \int_{\mathbb S^1}\eta=1.                                  \tag{2}
\]

The smooth Hochschild--Kostant--Rosenberg map and the cyclic
Eilenberg--Zilber shuffle identify the periodic mixed complex of
\(C^\infty(\mathbb S^1)\) with

\[
 H_{\rm dR}^{\rm ev}(\mathbb S^1)
 \oplus H_{\rm dR}^{\rm odd}(\mathbb S^1)
 =\mathbb C[1]\oplus\mathbb C[\eta].                         \tag{3}
\]

Nuclearity makes the completed Künneth map exact here; the circle factor
is finite-dimensional after the de Rham contraction.

## 3. External phase product and phase integration

Let

\[
 \mathrm{Bott}_\eta:
 CC^{\rm per}(\mathfrak C_{\rm CCM})
 \longrightarrow
 CC^{\rm per}(
   \mathfrak C_{\rm CCM}\widehat\otimes C^\infty(\mathbb S^1))
                                                                    \tag{4}
\]

be the cyclic shuffle product with the class \(\eta\). Let

\[
 \int_{\mathbb S^1}:
 CC^{\rm per}(
   \mathfrak C_{\rm CCM}\widehat\otimes C^\infty(\mathbb S^1))
 \longrightarrow
 CC^{\rm per}(\mathfrak C_{\rm CCM})                         \tag{5}
\]

be the chain map induced, after the de Rham contraction, by integration
of the phase one-form component.

### Theorem 3.1 — Exact odd-summand comparison

On periodic cyclic homology,

\[
 \boxed{
 \int_{\mathbb S^1}\circ\mathrm{Bott}_\eta=I.}        \tag{6}
\]

Moreover

\[
 \boxed{
 HP_\epsilon(
   \mathfrak C_{\rm CCM}\widehat\otimes C^\infty(\mathbb S^1))
 \cong
 HP_\epsilon(\mathfrak C_{\rm CCM})
 \oplus
 HP_{\epsilon-1}(\mathfrak C_{\rm CCM}),}                    \tag{7}
\]

and \(\mathrm{Bott}_\eta\) is an isomorphism from
\(HP_{\epsilon-1}(\mathfrak C_{\rm CCM})\) onto the second summand.

#### Proof

Under the cyclic Eilenberg--Zilber map and the de Rham contraction (3),
the phase-thickened total complex is homotopy equivalent to

\[
 CC^{\rm per}(\mathfrak C_{\rm CCM})
 \widehat\otimes(\mathbb C[1]\oplus\mathbb C[\eta]).
\]

The map (4) is \(c\mapsto c\otimes\eta\). The map (5) kills the
\(1\)-summand and sends \(c\otimes\eta\) to
\((\int\eta)c=c\). This proves (6) at chain-homotopy level and gives the
direct sum (7). \(\square\)

Because tensor product, shuffle, and phase integration are applied to
both terms of the mapping cone, (6) is a statement about the complete CCM
relative differential, not only about a local prime page.

## 4. The Toeplitz boundary is the same comparison

Let

\[
 0\longrightarrow\mathcal K
 \longrightarrow\mathcal T
 \longrightarrow C^\infty(\mathbb S^1)
 \longrightarrow0                                           \tag{8}
\]

be the smooth Toeplitz extension, oriented by the symbol \(z=e^{i\theta}\).
Its odd boundary class is represented by the unilateral shift \(T_z\),
whose index is \(-1\).

Tensor (8) with the CCM relative complex. The connecting morphism in
periodic cyclic homology is

\[
 \partial_{\mathcal T}:
 HP_\epsilon(
  \mathfrak C_{\rm CCM}\widehat\otimes C^\infty(\mathbb S^1))
 \longrightarrow HP_{\epsilon-1}(\mathfrak C_{\rm CCM}).     \tag{9}
\]

### Theorem 4.1 — Toeplitz realization of phase integration

On the odd Bott summand,

\[
 \boxed{
 \partial_{\mathcal T}\circ\mathrm{Bott}_\eta=-I.}    \tag{10}
\]

Equivalently,

\[
 \partial_{\mathcal T}
 =-\int_{\mathbb S^1}                                       \tag{11}
\]

on that summand.

#### Proof

Both sides are natural with respect to the coefficient mixed complex, so
it is enough to evaluate them for the scalar coefficient \(1\). The
pairing of the Toeplitz extension with the generator
\([z]\in K_1(C(\mathbb S^1))\) is

\[
 \mathrm{Ind}\,T_z=-1.
\]

The normalized de Rham class \(\eta\) pairs with the same generator by
\(\int_{\mathbb S^1}\eta=1\). Naturality of the external product then
gives (10) for every CCM class. \(\square\)

This theorem identifies the parity in 106.170 with the parity of the
actual CCM cyclic cone. No spectral symbol or zero divisor enters.

## 5. Compatibility with sharp, scaling, and the Tate middle boundary

Complex conjugation and phase reversal send

\[
 z\longmapsto z^{-1},\qquad \eta\longmapsto-\eta.            \tag{12}
\]

The CCM sharp involution reverses scaling and is conjugate-linear.
Therefore the product involution on the phase-thickened cone preserves the
real odd Bott summand after the usual degree-one sign. The normalized
scaling action is trivial on the phase coordinate and hence commutes with
(4)--(5).

At every finite set of primes, restriction of the phase factor to the Tate
fibres sends \(\eta\) to the common harmonic class \(b_p\). Its Hodge
conjugate is \(c_p^{-1}\)-normalized \(a_p\), exactly as in (5) of
106.169. Consequently the two middle boundary maps

\[
 R,\qquad RJ                                                  \tag{13}
\]

are the harmonic phase restriction and its Hodge conjugate inside the
same Bott-thickened complex.

Thus the following square is defined and commutes on the smooth finite
orbit core:

\[
\begin{CD}
 CC^{\rm per}(\mathfrak C_{\rm CCM})
   @>{\mathrm{Bott}_\eta}>>
 CC^{\rm per}(\mathfrak C_{\rm CCM}\widehat\otimes C^\infty(S^1))\\
 @V{\mathrm{Loc}_{\rm orb}}VV
 @VV{(R,RJ)\circ\mathrm{Loc}_{\rm Tate}}V\\
 \mathfrak C_{\rm orb}
   @>>{\mathrm{phase}}>
 \mathscr K\oplus\mathscr K .
\end{CD}                                                     \tag{14}
\]

Here \(\mathrm{Loc}_{\rm orb}\) denotes the existing fixed-orbit
localization functional underlying the CCM trace formula. The top arrow
and the right phase boundary are now constructed. Extending the bottom
and left arrows to a quasi-isomorphism of nonreduced nuclear complexes is
the remaining arithmetic clause.

## 6. What this closes and what it does not

The phase factor no longer contributes an open logical step:

* it is a genuine geometric circle supplied by the absolute curve;
* its odd class is represented by an unconditional Fredholm operator;
* cyclic Bott periodicity identifies its odd summand with the original CCM
  relative complex;
* the Toeplitz boundary gives exactly the minus sign used by the prime
  Lefschetz index.

What remains cannot be called a parity or Bott problem. It is the
faithfulness of fixed-orbit localization after the identity sector,
Gamma page, polar plane, and generic subtraction are joined in the
nonreduced topology.

## 7. Exact remaining comparison

Let \(\mathfrak C_{\rm Tate}^{\rm mid}\) be the LF inductive limit of the
finite middle complexes of 106.169 and let
\(\mathfrak C_{\Gamma,0,2}\) be the archimedean/polar page of 106.160.
The remaining map is

\[
 \mathrm{Loc}^{\rm mid}:
 \mathfrak C_{\rm CCM}
 \longrightarrow
 \mathfrak C_{\rm Tate}^{\rm mid}
 \mathop{\widehat\oplus}_{\partial}
 \mathfrak C_{\Gamma,0,2}.                                  \tag{15}
\]

The phase/Bott component of (15) is fixed by Theorems 3.1 and 4.1. The
unproved assertions are:

\[
 \boxed{
 H^1(\mathrm{Loc}^{\rm mid})\text{ is injective},
 \qquad
 \mathfrak h_{\rm Ros}(u,v)
 =\langle\mathrm{Loc}^{\rm mid}u,
          \mathrm{Loc}^{\rm mid}v\rangle_{\rm mid}.}  \tag{16}
\]

The second equality would transfer the positive middle metric to the CCM
Rosati form. It is the arithmetic Hodge-index identity, now stripped of
the already solved phase and finite-prime parity components.

## 8. Status

Proved without RH or zero input:

* cyclic Bott splitting for the full CCM relative cone;
* an explicit inverse on the odd phase summand;
* identification of that inverse with the Toeplitz index boundary;
* compatibility with scaling, real structure, and the Tate phase class;
* elimination of phase parity as an independent gap.

Still required:

* nuclear extension and injectivity of fixed-orbit localization;
* Gamma/polar gluing in the identity sector;
* the metric identity in (16).
