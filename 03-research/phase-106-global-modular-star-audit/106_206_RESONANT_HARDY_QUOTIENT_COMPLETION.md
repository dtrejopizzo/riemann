# 106.206 — The resonant Hardy-quotient completion

## 1. Purpose

Document 106.205 proves that every absolutely continuous Cauchy/Gamma
Hilbert completion loses CCM's discrete resonant degree one.  The repair
must make analytic evaluation and its multiplicity jets continuous before
taking a Hilbert quotient.

This note constructs such a target directly from the completed
arithmetic multiplier.  It uses no list of zeros.  The quotient is
positive by construction, retains every local Artin factor of the CCM
zero scheme, and carries the exact normalized scale action.  Its scale
norm is not automatically invariant; the defect is computed exactly.

## 2. The strip Hardy space and the arithmetic multiplier

Put

\[
 \Sigma=\{z\in\mathbb C:|\operatorname {Re}z|<1/2\},
 \qquad
 \Xi(z)=2\xi(1/2+z).
\tag{1}
\]

Let (H^2(\Sigma)) be the conformally invariant Hardy space of the
vertical strip.  Equivalently, use

\[
 \phi(z)=\tan(\pi z/2):\Sigma\longrightarrow\mathbb D
\tag{2}
\]

and transport (H^2(\mathbb D)) with the standard half-Jacobian factor.
Point evaluation and every derivative evaluation are continuous on
compact sub-strips.

The completed function \(\Xi\) is analytic across the closed strip,
has no zero on its two boundary lines, and decays exponentially in the
vertical direction after a polynomial factor.  Hence it belongs to the
Smirnov class of \(\Sigma\), and multiplication by \(\Xi\) defines a
closed densely defined operator

\[
 M_\Xi:\mathcal D(M_\Xi)\subset H^2(\Sigma)
 \longrightarrow H^2(\Sigma).
\tag{3}
\]

If one uses the bounded outer normalization of \(\Xi\), (3) becomes a
bounded multiplier; the closure of its range is unchanged.

### Definition 2.1 — Resonant Hardy completion

Define

\[
 \boxed{
 \mathscr K_\Xi
 =H^2(\Sigma)/\overline{\operatorname {Ran}M_\Xi}
 \simeq
 \left(\overline{\operatorname {Ran}M_\Xi}\right)^\perp.}
\tag{4}
\]

This definition uses the source function \(\Xi\), not its divisor.

## 3. Exact identification of the retained torsion

Let

\[
 \Xi=B_\Xi O_\Xi
\tag{5}
\]

be its inner--outer factorization in the strip.  Analytic continuation
across the boundary excludes a singular inner factor; (B_\Xi) is the
Blaschke product of the complete zero divisor in \(\Sigma\), counted
with multiplicity.  The unconditional zero-counting estimate implies
the strip Blaschke condition because, under (2), distance to the circle
decays exponentially with vertical height.

### Theorem 3.1 — The Hilbert quotient retains the full analytic divisor

\[
 \boxed{
 \overline{\operatorname {Ran}M_\Xi}
 =B_\Xi H^2(\Sigma),
 \qquad
 \mathscr K_\Xi=H^2(\Sigma)\ominus B_\Xi H^2(\Sigma).}
\tag{6}
\]

For every zero (a\in\Sigma) of order (m_a\), the Riesz vectors of

\[
 f\longmapsto f^{(j)}(a),
 \qquad 0\le j<m_a,
\tag{7}
\]

belong to \(\mathscr K_\Xi\) and are linearly independent.  Conversely,
the closed span of all vectors (7) is \(\mathscr K_\Xi\).

#### Proof

The outer multiplier (O_\Xi) has dense range in (H^2(\Sigma)).
Multiplication by the inner factor is an isometry with closed range.
Therefore the closure of the range of the product is the first identity
in (6).

If (j<m_a\), then every function in (B_\Xi H^2(\Sigma)) has its first
(m_a\) jets zero at (a).  Hence the Riesz vector of (7) is orthogonal
to that range and belongs to the model space.  Hermite interpolation by
polynomials proves linear independence on every finite set of zero jets.
If a vector in the model space is orthogonal to all of them, its analytic
representative is divisible by the complete Blaschke product and also
lies in its orthogonal complement, so it is zero. \(\square\)

Unlike the Cauchy completion, (4) therefore sees isolated resonances and
their nilpotent jets.

## 4. Comparison with the finite CCM analytic quotient

Let (D\Subset\Sigma\) have smooth symmetric boundary disjoint from the
zero divisor and retain

\[
 \mathcal H_D=\mathcal O(\overline D)/\Xi\mathcal O(\overline D)
\tag{8}
\]

from 106.163.

### Theorem 4.1 — Local Artin comparison

Restriction of Hardy functions to (D), followed by their jets at the
finite zero scheme in (D), induces a surjection

\[
 \boxed{
 \operatorname {Loc}_D:\mathscr K_\Xi
 \longrightarrow\mathcal H_D.}
\tag{9}
\]

Its adjoint embeds the dual local Artin algebra as the span of the kernel
jets (7).  These maps are compatible under nested windows after passing
to the corresponding local factors.

#### Proof

The map is well defined because every vector in the closed multiplier
range has zero class in (8).  A finite collection of prescribed jets is
realized by a polynomial, which belongs to (H^2(\Sigma)) after
multiplication by a fixed zero-free outer damping function.  This proves
surjectivity.  The adjoint statement is the reproducing property, and
compatibility is restriction of jets. \(\square\)

Thus (4) is a genuine Hilbert realization of the complete cofinal family
of finite CCM resonant quotients.  The unresolved global comparison is
topological: the full Meyer/CCM completion and the model-space completion
need not contain the same infinite jet combinations.

## 5. Positive Hodge data

Regard \(\mathscr K_\Xi\) as a real Hilbert space and define

\[
 J_Hf=if,
 \qquad
 g_H(f,g)=\operatorname {Re}\langle f,g\rangle,
 \qquad
 \Omega_H(f,g)=g_H(J_Hf,g).
\tag{10}
\]

### Theorem 5.1 — Canonical positive resonant polarization

The triple \((\Omega_H,J_H,g_H)\) satisfies

\[
 \boxed{
 J_H^2=-I,
 \quad
 \Omega_H\text{ alternating and nondegenerate},
 \quad
 g_H(u,v)=\Omega_H(u,J_Hv),
 \quad
 g_H(u,u)>0\ (u\ne0).}
\tag{11}
\]

It retains all multiplicity jets and uses no sign of the Weil/Rosati
form.

#### Proof

These are the standard identities of a complex Hilbert space viewed over
the reals.  Definiteness is the quotient Hardy norm. \(\square\)

This is an alternative positive form.  It is not asserted to equal the
Rosati trace form of 106.157.

## 6. Exact normalized-scale action and its defect

For (t\in\mathbb R\), the function (e^{tz}) is a bounded invertible
multiplier of the strip, with

\[
 \|e^{tz}\|_{H^\infty(\Sigma)}=e^{|t|/2}.
\tag{12}
\]

Since it commutes with (M_\Xi), it induces a strongly continuous group

\[
 \boxed{U_t[f]=[e^{tz}f]}
\tag{13}
\]

on \(\mathscr K_\Xi\), satisfying

\[
 \|U_t\|\le e^{|t|/2},
 \qquad U_tJ_H=J_HU_t.
\tag{14}
\]

The weight-one action is \(\vartheta_t=e^{t/2}U_t\).

### Theorem 6.1 — Pointwise scale test

Let (k_a\in\mathscr K_\Xi\) be the evaluation vector at a zero (a).
Then

\[
 \boxed{U_t^*k_a=e^{t\bar a}k_a.}
\tag{15}
\]

Consequently, if the positive metric (10), or any equivalent positive
metric, makes (U_t) unitary, then

\[
 \boxed{\operatorname {Re}a=0}
\tag{16}
\]

for every zero represented faithfully in the completion.  Higher jets
form the corresponding upper-triangular Jordan blocks; a unitary action
also forces their nilpotent part to vanish on the separated quotient.

#### Proof

For every class (f),

\[
 \langle f,U_t^*k_a\rangle
 =\langle U_tf,k_a\rangle
 =(U_tf)(a)=e^{ta}f(a),
\tag{17}
\]

which is (15), with the conjugation determined by the Hilbert convention.
If (U_t) is unitary, the norm of the nonzero vector (k_a) is constant;
(15) then gives (e^{t\operatorname {Re}a}=1) for all (t\), proving
(16).  Differentiated evaluation gives the jet statement. \(\square\)

## 7. What this changes

The construction repairs exactly the failure in 106.205:

* it is defined from \(\Xi\), not from a zero list;
* its quotient norm is positive;
* it retains every discrete zero jet rather than an almost-everywhere
  multiplier class;
* every finite CCM analytic quotient is a local factor of it;
* normalized scaling acts by a genuine bounded group for each fixed
  time.

It does not yet finish the global polarization.  Two statements remain:

1. prove that the prime-orbit/Gamma/polar cyclic localization extends
   from the algebraic resonant core to a faithful comparison between
   existing CCM degree one and \(\mathscr K_\Xi\);
2. prove that the induced normalized-scale group is unitary for a
   source-defined positive metric compatible with that comparison.

Theorem 6.1 shows that the second statement carries the complete
critical-line content.  The gain over the absolutely continuous target
is categorical rather than logical: the relevant resonant vectors now
exist in the positive target, so the descent question is well posed and
does not collapse before reaching the arithmetic sign.
