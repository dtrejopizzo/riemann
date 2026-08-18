# 114.a.65 — H7 abstract pullback, corrected by the type audit `a_66`

> **Retraction/refinement (`a_66`).** The original version identified
> Haran's Section-11 right-action lattices with the abelian quasi-coherent
> modules of Section 6.  Equation (11.7) does not make that identification.
> Consequently every occurrence of `Pic_qc` and the claimed forgetful map
> into it is retracted.  The valid unconditional replacement is the
> `GL_1(O)`-torsor category `Pic_tor` constructed in `a_66`.

```
+-------------------------------------------------------------------------+
| TORSORS    GL_1(O)-transition cocycles pull back unconditionally.       |
| LABELS     Prime torsors and the multiplicative family remain faithful. |
| MODULES    No Pic_qc realization follows from Sections 6 and 11.        |
| COMPLETED  Rational lattices inside K still require H7-PRIME-REG.       |
+-------------------------------------------------------------------------+
```

## 1. What survives from the original argument

A completed curve line bundle represented by local multipliers
`f_alpha in GL_1(K)` has transition functions

\[
 u_{\alpha\beta}=f_\alpha^{-1}f_\beta
   \in GL_1(\mathcal O)(U_{\alpha\beta}).                              \tag{1.1}
\]

They define a unit torsor `T(L)` in `Pic_tor`.  If this torsor were trivial,
write `u_{alpha beta}=v_alpha^{-1}v_beta`.  Then
`f_alpha v_alpha^{-1}` glue to one global element of `GL_1(K)`, so the
completed Picard class is trivial.  Thus `T(L_p)` is nontrivial because
`deg L_p=log p`.

Every morphism `f:Y->X` maps units to units and therefore maps the cocycle
(1.1).  This gives unconditional pullback

\[
 f^*:Pic_{tor}(X)\longrightarrow Pic_{tor}(Y),                         \tag{1.2}
\]

compatible with tensor products and composition.  It does not use a map of
fraction sheaves.

## 2. Faithful abstract labels on the square

Let `Y=X x_S X` and define

\[
 \mathcal T_n=p_1^*T\!\left(\bigotimes_pL_p^{\otimes v_p(n)}\right)
 \in Pic_{tor}(Y).                                                     \tag{2.1}
\]

Then

\[
 \mathcal T_m\otimes\mathcal T_n\simeq\mathcal T_{mn}.                \tag{2.2}
\]

If `T_m~=T_n`, diagonal pullback trivializes the torsor underlying
`L_m tensor L_n^{-1}`.  The gluing argument of Section 1 trivializes that
completed curve bundle, and its degree `log(m/n)` forces `m=n`.  Hence the
abstract labels and the two-prime bigrade remain unconditional in
`Pic_tor`.

## 3. What remains conditional or open

To realize (2.1) by pulled rational generators such as `1/p` inside
Haran's Section-11 `K_Y`, the projection must preserve the universally
regular denominators.  This is H7-PRIME-REG from `a_63`--`a_64`.

The additional claims that the prime ruling is an effective Cartier divisor,
that its normal layers are abelian quotient modules, or that derived
diagonal pullback is computed by `Tor` are not consequences of the cited
source.  They are retracted by `a_66` pending a typed generalized Cartier
formalism.

## 4. Verification scope

The former verifier is retained as historical arithmetic/base-change
evidence but its `Pic_qc` verdict is superseded.  The authoritative verifier
for this correction is `114_a_66_h7_type_audit_verify.py`.

Primary source: [Haran, arXiv:1709.05831](https://arxiv.org/abs/1709.05831).
