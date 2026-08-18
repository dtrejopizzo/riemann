# 107.213 -- Published arithmetic Lefschetz--RR does not cover the nonunitary prime character

## 1. The character that must be treated

The finite-place class of 107_212 is evaluated at

\[
 q_{p,s}=p^{-s},\qquad \Re s>0.
 \tag{1.1}
\]

Hence

\[
 0<|q_{p,s}|=p^{-\Re s}<1.
 \tag{1.2}
\]

The required arithmetic direct-image theorem must therefore treat a
nonunitary element of the complexified scaling torus.

## 2. Tang's theorem: exact finite-cyclic obstruction

Tang, Arithmetic Lefschetz--Riemann--Roch theorem
(arXiv:1503.07751), assumes an action of

\[
 \mu_n=\mathrm{Spec}\,\mathbb Z[\mathbb Z/n\mathbb Z]
 \]

and works over

\[
 R(\mu_n)=\mathbb Z[T]/(1-T^n).
 \tag{2.1}
\]

Any complex evaluation \(T\mapsto z\) must satisfy \(z^n=1\).  But

\[
 |q_{p,s}^n|=p^{-n\Re s}<1,
 \]

so \(q_{p,s}^n\ne1\) for every \(n\ge1\).  Therefore there is no
coefficient-ring morphism from (2.1) that sends \(T\) to the Phase 107
character.

Finite-cyclic approximation does not repair this.  Every root of unity
has modulus one, and

\[
 |\zeta-q_{p,s}|\ge1-|q_{p,s}|>0
 \tag{2.2}
\]

for every root of unity \(\zeta\).  Thus no sequence of finite-cyclic
characters converges to \(q_{p,s}\).

### Proposition 2.1

Tang's published arithmetic Lefschetz--RR theorem cannot be specialized
or obtained by a limit of character evaluations to certify the classes
of 107_212.

## 3. Koehler--Roessler: what does apply

Koehler--Roessler, A fixed point formula of Lefschetz type in Arakelov
geometry II (arXiv:math/0105098), treats arithmetic varieties with an
action of the one-dimensional diagonalizable torus.  Their residue
formula applies to torus-equivariant arithmetic Chern numbers and
fixed-scheme normal bundles.  This validates the algebraic
torus-localization shape used in 107_211.

Their proof first restricts to finite subgroups and unitary elements

\[
 g_t=e^{2\pi it}\in S^1.
 \tag{3.1}
\]

Lemma 2.3 identifies, on a pointed real neighborhood and then away from
finitely many unitary values, a combination of equivariant analytic
torsion and fixed-point characteristic terms with a rational function
\(Q(g_t)\).  The rational function itself can of course be evaluated at
\(q_{p,s}\in\mathbb C^\times\), but the published analytic identity is
proved only for (3.1).

Consequently the implication

\[
 Q(q_{p,s})
 \stackrel{?}{=}
 \text{nonunitary equivariant analytic torsion/direct image}
 \tag{3.2}
\]

is not a theorem in that paper.  The final infinitesimal residue formula
computes arithmetic Chern numbers using the torus vector field; it does
not construct the meromorphic \(s\)-family (3.2).

## 4. Applicability theorem

### Theorem 4.1

The published arithmetic fixed-point results establish the following
strictly separated statements for Phase 107:

1. proper algebraic torus localization and arithmetic residue classes
   are available for the finite-support geometry of 107_211--107_212;
2. Tang's finite-cyclic direct-image theorem is inapplicable to
   \(p^{-s}\);
3. Koehler--Roessler do not prove the nonunitary torsion/direct-image
   continuation required to identify their arithmetic pushforward with
   the nuclear \(s\)-family of 107_210.

Therefore no published arithmetic Lefschetz--RR theorem currently
closes the global pushforward of Phase 107.  A new nonunitary or
holomorphic-family extension, with its anomaly term, is required.

This is not a no-go for such an extension.  It is a no-go for claiming
that the existing theorems already provide it.

## 5. Consequence for row (d)

The evaluated sign calibration of 107_181 remains valid, but it cannot
be promoted to a Hodge theorem through Tang or Koehler--Roessler alone.
Before row (d) can use an arithmetic index theorem, Phase 107 must prove:

1. holomorphic continuation of the equivariant torsion/direct image
   from \(S^1\) to \(0<|\chi|<1\);
2. equality of that continuation with the Meyer nuclear character;
3. compatibility of the resulting class with a primitive bilinear
   arithmetic intersection form.

## 6. Falsifier

107_213_published_arithmetic_lrr_nonunitary_applicability_no_go.py tests
five actual prime characters, real and complex spectral parameters,
finite cyclic orders through 64, and the positive radial separation
from every root of unity.  A unitary mutation must be accepted by the
finite-cyclic gate, proving that the program can return NO if the
character lies in the published domain.

