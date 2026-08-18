# 114.a.63 — H7 correction: completed fraction-lattice pullback is the prime-regularity gate

> **Refinement (`a_65`).** This correction concerns Haran's completed
> Section-11 lattices inside `K`. By the type audit `a_66`, the unconditional
> replacement is pullback of `GL_1(O)`-torsors, not an asserted `Pic_qc`
> module. Thus abstract torsor labels and the discrete bigrade survive.

```
+-------------------------------------------------------------------------+
| SOURCE      K_N is obtained by inverting universally regular elements.  |
| ISSUE       A map O_X -> O_Y need not send those elements into S_Y.     |
| CONSEQUENCE Pullback as a completed K-lattice is not automatic.         |
| EXACT GATE  p_i^#(S_X) subset S_Y; for L_p this is H7-PRIME-REG.         |
| RETRACTION  Their completed-lattice claims are conditional.             |
| SURVIVES    Abstract Picard labels, incidences and formal results.       |
+-------------------------------------------------------------------------+
```

## 1. What Section 11 actually localizes

For a pro-generalized scheme `X={X_N}`, Haran (11.1) defines `S_X(U)` to
consist of symmetric scalars whose action remains injective on **all**
arities, all smaller opens and all later pro-levels.  The fraction sheaf is

\[
 \mathcal K_{X,N}=\mathrm{sh}
   \bigl(S_X(-)^{-1}\mathcal O_{X_N}(-)\bigr).                         \tag{1.1}
\]

Bundle trivializers in (11.3) live in `GL_d(K_X)`, not merely in
`GL_d(O_X)`.  Therefore a morphism `f:Y->X` induces pullback of these
trivializers only after proving

\[
 f^\#\bigl(S_X(U)\bigr)\subseteq S_Y(f^{-1}U).                         \tag{1.2}
\]

The source explicitly constructs pullback in (11.10) for the transition maps
of the chosen pro-system.  It does not state (1.2), or arbitrary functorial
pullback of the completed bundle category, for every morphism of generalized
pro-schemes.

## 2. A section of the projection does not repair the issue

Regular denominators are not preserved by an arbitrary split ring map.  For
example, for any prime `p`, let

\[
 A=\mathbb Z,\qquad B=\mathbb Z\times\mathbb F_p,
 \qquad A\longrightarrow B,quad a\longmapsto(a,\bar a).               \tag{2.1}
\]

Projection to the first factor retracts (2.1).  Multiplication by `p` is
injective on `A`, while

\[
 p(0,1)=(0,0)\quad\text{in }B.                                        \tag{2.2}
\]

Thus even `Delta^*p_i^*=id`, at the structure-sheaf level, cannot prove that
`p_i^#` extends to fraction sheaves.  A flatness or regularity theorem is
still required.

## 3. Correction to the completed external Picard construction

The local formula from `a_12`,

\[
 h_{\alpha\beta}=p_1^\#f_\alpha\,p_2^\#g_\beta,                       \tag{3.1}
\]

is valid provided the following admissibility condition holds:

> **H7-PB-REG.** Each projection `p_i:Y=X x_S X -> X` sends the regular
> denominator sheaf `S_X` into `S_Y`, levelwise and on every relevant open.

Under H7-PB-REG, (3.1) constructs the external map in `Pic_comp` and all
completed-lattice arguments apply unchanged. Without it, `p_i^*L` is not
typed as a general Section-11 completed bundle. Its transition cocycle is
nevertheless typed in `Pic_tor` by `a_66`.

For the inverse-uniformizer bundle `L_p`, the only nonunit denominator is
`p`.  Hence the needed instance of H7-PB-REG is precisely

\[
 p:p_i^*\mathcal O_X\longrightarrow p_i^*\mathcal O_X
 \quad\text{injective in every local arity and later level}.           \tag{3.2}
\]

This is H7-PRIME-REG of `a_62`, with the full Section-11 quantifiers restored.

### Theorem 3.1 (corrected completed-Picard implication)

Assume H7-PRIME-REG for every prime dividing `n`.  Then `p_1^*L_n` exists as
a completed line bundle on `Y`.  The family

\[
 \mathcal G_n=p_1^*\bigotimes_pL_p^{\otimes v_p(n)}                    \tag{3.3}
\]

is faithful and satisfies `G_m tensor G_n ~= G_mn`. If H7-PRIME-REG is not
known, their existence in `Pic_comp` remains conditional; their abstract
`Pic_tor` versions are unconditional by `a_66`.

### Proof

Condition (3.2) lets the projection map extend through every localization
used by the finite product of prime bundles.  Formula (3.3) is therefore
typed.  The valuation-additive tensor law and diagonal-degree proof of `a_61`
then apply verbatim.  QED.

## 4. Corrected status

The following remain unconditional:

1. `L_p` and its degree `log p` on the curve `X`;
2. the literal ruling `V_p=x_p x_S X` and `Delta x_Y V_p=x_p`;
3. the contact sheaves `M_n` on the underlying site;
4. all algebraic implications proved after explicitly assuming the Picard
   pullback or H7-CART-NORMAL.
5. the abstract `Pic_tor` pullbacks, faithful labels and discrete bigrade of
   `a_66`.

The following earlier labels are retracted only as unconditional
**completed-lattice** statements:

1. the `Pic_comp` external homomorphism of `a_12`;
2. the completed square-side prime lift of `a_18`;
3. the completed realization of the `a_19` bigrade and `a_20` grid;
4. the completed-lattice existence claim for `G_n` in `a_61`.

They become theorems under H7-PB-REG/H7-PRIME-REG.  This is not a new
independent obstruction: it identifies the previously hidden circular use of
the same regularity gate isolated in `a_62`.

## 5. Verification scope

`114_a_63_h7_fraction_pullback_admissibility_verify.py` checks the exact
Section-11 anchors and the split-map counterexample.  It does not prove
H7-PRIME-REG.

**Later resolution (`a108`).**  For the actual signed square, the image of
`2` kills the nonzero scalar `kappa`.  Hence H7-PB-REG/H7-PRIME-REG fails
for `L_2`, and the conditional completed fraction-lattice pullback in
Theorem 3.1 is unavailable for all integers divisible by `2`.
