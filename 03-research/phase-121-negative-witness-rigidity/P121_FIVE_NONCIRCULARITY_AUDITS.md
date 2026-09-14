# P121 -- five radical-only noncircularity audits

## Status

This note audits five attempts to extract an additional law from a
first-contact state without dividing by `zeta`, constructing a positive
lift, or assuming the primitive gap.  None closes F2.  The calculations
below are source-side obstructions and are recorded so that these mechanisms
are not proposed again under different vocabulary.

## 1. Euler/source two-parameter holonomy is flat

Let `E` be the completed determinant and let `K=K_F` be the compact-source
entire function.  The two natural scalar deformations are horizontal
translation of `E` and exponential tilt of the source:

\[
 E_\epsilon(z)=E(z+\epsilon),\qquad
 K_\sigma(z)=K(z-\sigma).
\]

For the scalar product `G(epsilon,sigma;z)=E_epsilon(z)K_sigma(z)`,

\[
 \partial_\epsilon\partial_\sigma\log G=0.             \tag{1.1}
\]

Thus the scalar rectangle has zero holonomy.  For the unlogged product its
mixed derivative is `-E'(z)K'(z)`, not the frozen critical current
`(E'/E)K`.  On the diagonal deformation one obtains

\[
 {\partial_\epsilon(E(z+\epsilon)K(z-\epsilon))|_0\over E(z)}
 ={E'\over E}K-K',                                    \tag{1.2}
\]

but the division by `E` is physically removable at its critical zeros if
and only if `K` vanishes there.  Hence (1.2) is F2, not a derivation of F2.

Replacing the two commuting scalar jets by opposite noncommuting nilpotents
creates curvature proportional to `K(lambda)^2`, but that replacement is
extra source data.  This is the exact collision with the sourced-framing
audit and the older two-parameter logarithmic-connection audit.

## 2. The high Gamma moments do not form a contracting recurrence

For `a_j=2j+1/2` the right and left exterior Gamma states are encoded by

\[
 M_j^+=\langle F,e^{a_jt}\rangle,\qquad
 M_j^-=\langle F,e^{-a_jt}\rangle.                    \tag{2.1}
\]

Vanishing of either complete tail would force `F=0` by polynomial moment
determinacy.  It is tempting to pair the one-way collar equation with the
oppositely decaying exponential, because a prime shift then displays a
factor `n^{-a_j}`.

The physical pairing is over a translated collar, not over the whole
support.  If `C=(u,v)`, then exactly

\[
 \int_C e^{-a t}F(t-\log n)\,dt
 =n^{-a}\int_{C-\log n}e^{-a s}F(s)\,ds.             \tag{2.2}
\]

After the natural normalization of the translated cell, the exponential
change of its endpoints cancels `n^{-a}`.  Equation (2.2) therefore couples
cell moments of comparable size; it is not a contraction on the global
moments (2.1).  Eliminating the auxiliary cell moments by divisor/Mobius
triangularity leaves the depth-zero block unchanged, namely the observed
transport equation (445).  This is the root-diagonal persistence no-go of
the CMO source matrix in moment coordinates.

## 3. Modulus contraction stops at the Tate projection

Let `L_T` be the positive prime--Gamma jump form and let
`q_T(F)=<F,(L_T-m_T)F>` on the two-Tate primitive space.  The Markov and
phase inequalities give

\[
 \mathcal E_T(|F|)\leq\mathcal E_T(F).               \tag{3.1}
\]

For a nonzero sign-changing radical the inequality is strict on a connected
jump graph.  Thus `|F|` has Rayleigh quotient below `m_T`.  This only
recovers the low positive mode which the two Tate constraints are supposed
to remove.  The function `|F|` is not primitive, since both of its Tate
moments are positive.

Projecting it back gives `P_T|F|`, but an estimate

\[
 q_T(P_T|F|)\leq q_T(F)                               \tag{3.2}
\]

is a constrained Markov property.  By the projection/Finsler lemma, the
existence of the required rank-two correction is equivalent to positivity
of the primitive compression.  Hence (3.2) is the matrix-Picone/Tate
majorant of D.99, not a consequence of (3.1).  Equality rigidity of the
ordinary modulus cannot cross the Tate projection for free.

## 4. The normalized radial Euler energy has no fixed monotonicity

In the safe half-plane the exact normalized energy satisfies

\[
 \partial_\sigma\mathscr W(\sigma;F)
 ={2\over\zeta(2\sigma)}
 \langle(c_\sigma I-\operatorname {Re}B_\sigma)h_\sigma,
 h_\sigma\rangle,                                    \tag{4.1}
\]

where

\[
 c_\sigma=-{\zeta'\over\zeta}(2\sigma),\qquad
 B_\sigma=\sum_{n\ge2}{\Lambda(n)\over n^\sigma}S_{\log n}.
\]

The generator in (4.1) is indefinite.  On long almost-constant profiles,
`Re<B_sigma h,h>/||h||^2` approaches
`-zeta'/zeta(sigma)>c_sigma`; modulated profiles can reverse the sign.
Consequently neither monotonicity nor complete monotonicity follows from
`Lambda>=0` after common-divisor normalization.

Moreover first contact is a source variation statement at the critical
line.  Transporting it to (4.1), which is initially proved for
`sigma>1`, requires the same oriented continuation across the critical
divisor that F2 asks for.  The radial flow therefore gives an exact domain
coordinate, but not an independent equality-state law.

## 5. Minimal support supplies no sign by itself

Translation invariance and the Tate moments imply that positivity below a
first length holds for every translated interval of smaller length.  A
first-contact vector is therefore a minimal-span null state.  This extra
fact does not exclude it: local Sturm operators and finite connected Markov
graphs have ordinary first critical lengths with nonzero threshold states.

Partitioning a radical and correcting the pieces back into the two-moment
kernel produces the nonlocal IMS cross term.  Its sign depends on the phase
of the pieces.  Signing that term for the literal Euler--Gamma kernel is a
new arithmetic inequality; without such a law, minimality merely restates
the one-sided shape derivative and does not annihilate the state.

## 6. Consequence

These audits remove four apparent ways of making F2 noncircular:

1. scalar two-parameter curvature;
2. large-quarter-shift moment contraction;
3. radical modulus rigidity;
4. radial complete monotonicity;
5. abstract minimal-support localization.

A surviving proof must contribute a genuinely new **oriented source law**
which is absent for a general rank-two functional-equation model.  It must
act on the equality state before scalar supertrace and must not be obtained
by inverting the primitive operator or by dividing by the completed
determinant.
