# 114.a.66 — H7 type audit: unit torsors survive; `Pic_qc` and `Tor` do not

```
+-------------------------------------------------------------------------+
| SOURCE  Haran (11.7) is a sheaf of operation sets with a right action. |
| NOT     It is not an abelian O-module of Section 6.                    |
| SURVIVE Its GL_1(O)-transition cocycle defines a unit torsor.          |
| PULLBACK Unit torsors pull back along every generalized-ring map.      |
| LABELS  The prime torsors remain nontrivial and faithfully label n.    |
| RETRACT Pic_qc, short-exact, Tor and derived-normal claims.             |
+-------------------------------------------------------------------------+
```

## 1. The source has two different notions

Haran's Section 6 defines an `A`-module as a functor to **abelian groups**,
with additive multiplication and contraction actions.  Equation (6.3) gives
extension and restriction of scalars in that abelian category.

Completed bundles in Section 11 are different.  A rank-one object is locally
represented by `f_alpha in GL_1(K)`, and (11.7) defines

\[
 \mathcal O(D)_{d'}|_{U_\alpha}
   =f_\alpha\circ\mathcal O_{1,d'}|_{U_\alpha}\subseteq\mathcal K_{1,d'}.
                                                                    \tag{1.1}
\]

The source says that (1.1) is stable under the **right action** of
`O`.  It supplies no abelian-group law on these sets and does not identify
them with the abelian modules of Section 6.  Thus the map

\[
 Pic_{comp}(Z)\longrightarrow Pic_{qc}(Z)                             \tag{1.2}
\]

asserted in `a_65` was not typed by the cited source.  In particular,
extension of scalars (6.3) cannot be applied directly to (11.7).

## 2. The unconditional object is a unit torsor

For a generalized ringed space `Z`, let `Pic_tor(Z)` denote isomorphism
classes of locally trivial torsors under the sheaf of abelian rank-one units
`GL_1(O_Z)`.  Equivalently, on a cover they are Cech cocycles

\[
 u_{\alpha\beta}\in GL_1(\mathcal O_Z)(U_{\alpha\beta}),\qquad
 u_{\alpha\beta}u_{\beta\gamma}=u_{\alpha\gamma},                    \tag{2.1}
\]

modulo coboundaries by local units.  Rank-one multiplication makes this an
abelian group.

Every finite-layer completed line bundle has the cocycle

\[
 u_{\alpha\beta}=f_\alpha^{-1}f_\beta\in GL_1(\mathcal O_Z),          \tag{2.2}
\]

by (11.3)--(11.4).  Hence it has an underlying unit torsor.  Moreover this
forgetful operation detects triviality: if
`u_{alpha beta}=v_alpha^{-1}v_beta` for local `O`-units, then

\[
 h_\alpha=f_\alpha v_\alpha^{-1}
\]

agrees on overlaps.  The sheaf property gives a global
`h in GL_1(K)`, and the global `GL_1(K)` action plus (11.4) makes the
completed Picard class trivial.  Consequently the nonzero-degree prime
class `L_p` has a nontrivial underlying unit torsor `T_p`.

This argument is used only for the eventually finite-layer prime bundles on
the arithmetic curve; no equivalence between arbitrary pro-completed
bundles and torsors is asserted.

## 3. Pullback and the faithful labels

A morphism `f:Y->X` induces a sheaf homomorphism

\[
 f^{-1}GL_1(\mathcal O_X)\longrightarrow GL_1(\mathcal O_Y),          \tag{3.1}
\]

because a generalized-ring homomorphism sends an inverse pair to an inverse
pair.  Extending the structure group in (3.1), or simply mapping the cocycle
(2.1), defines

\[
 f^*:Pic_{tor}(X)\longrightarrow Pic_{tor}(Y)                         \tag{3.2}
\]

without applying `f^#` to any element of `K_X`.  It commutes with tensor
product and composition.

On Haran's literal square `Y=X x_S X`, put

\[
 \mathcal T_n=p_1^*\bigotimes_pT_p^{\otimes v_p(n)}.                  \tag{3.3}
\]

Then

\[
 \mathcal T_m\otimes\mathcal T_n\simeq\mathcal T_{mn}.               \tag{3.4}
\]

If `T_m` and `T_n` were isomorphic on the square, diagonal pullback would
identify their curve torsors.  Their quotient would then be trivial; by the
triviality-detection argument of Section 2, the completed curve bundle
`L_m tensor L_n^{-1}` would be trivial.  Its degree is
`log(m/n)`, hence `m=n`.  The same argument gives the two-prime discrete
bigrade.  Thus the faithful abstract labels survive, but in `Pic_tor`, not
in the unproved `Pic_qc` category of `a_65`.

## 4. Consequence for the Cartier gate

Equation (11.1) still makes H7-PRIME-REG the exact condition for `p` to be
an admissible denominator on the square.  What must be retracted is the
stronger claim in `a_62` that

\[
 p:\mathcal O_Y\longrightarrow\mathcal O_Y                            \tag{4.1}
\]

is a morphism in Haran's abelian module category with a short exact sequence
and a `Tor_1` obstruction.  The structure sheaf values are generalized-ring
operation sets, not abelian modules.  A linearized free module could be
introduced, but the source does not identify its cokernel with the closed
fiber or prove the claimed Cartier comparison.

Therefore the rigorously typed status is:

1. unit-torsor pullbacks and faithful multiplicative labels: **closed**;
2. completed fraction-lattice pullbacks: conditional on H7-PRIME-REG;
3. principal generalized quotient/right act and its ordinary diagonal layers:
   **closed conditional on H7-PRIME-REG** by `a_67`;
4. global cotangent conormal: **constructed** by `a_68`; its derived diagonal
   identification is the open H7-LCI-DELTA gate;
5. contact sheaves on the underlying site and their `Lambda(n)` cardinality:
   unchanged, but not yet derived from Cartier normal layers.

This correction narrows the valid route without assuming RH.

## 5. Verification scope

`114_a_66_h7_type_audit_verify.py` checks the distinct source definitions,
the exact (11.3)--(11.7) anchors, Cech cocycle pullback and the gluing
calculation proving triviality detection.  It does not assert
H7-PRIME-REG or a generalized Cartier theory.

Primary source: [Haran, arXiv:1709.05831](https://arxiv.org/abs/1709.05831).
