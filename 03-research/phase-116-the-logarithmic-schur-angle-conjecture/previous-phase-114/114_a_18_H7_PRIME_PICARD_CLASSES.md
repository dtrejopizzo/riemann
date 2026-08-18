# 114.a.18 — H7 prime Picard classes: the `log p` carrier is nonprincipal

> **Refinement (`a_63`--`a_66`).** The curve bundle and its abstract square
> underlying unit-torsor pullback is unconditional. H7-PRIME-REG is needed
> only for the stronger completed-lattice realization inside Haran's fraction
> sheaf.

```
+--------------------------------------------------------------------------+
| CURVE       Pic(X) is the idelic quotient and equals R_+.                |
| PRIME       The inverse p-uniformizer idele defines L_p of degree log p. |
| SQUARE      p_1^*L_p and p_2^*L_p are nontrivial abstract line bundles.  |
| DETECTOR    Pullback by the diagonal recovers L_p.                       |
| LIMIT       O(V_p)=p_i^*L_p and its intersection still require a         |
|             Cartier/intersection theory on the generalized square.       |
+--------------------------------------------------------------------------+
```

## 1. The prime class on the compactified arithmetic curve

Let `X=overline{Spec Z}`.  Haran's equation (11.19) gives

\[
 \operatorname{Pic}(X)
 =\mathbb Q^*\backslash\mathbb A_{\mathbb Q}^*/
       \prod_v\widehat{\mathbb Z}_v^*
 \simeq\mathbb R_+.                                                       \tag{1.1}
\]

For a rational prime `p`, let `a^(p)` be the idele whose `p`-component is the
inverse uniformizer `p^{-1}` and whose other finite and real components are
one.  Let

\[
 L_p=[a^{(p)}]\in\operatorname{Pic}(X).                                   \tag{1.2}
\]

Use normalized absolute values and define the additive arithmetic degree

\[
 \widehat\deg[a]= \log\!\left(|a_\infty|
              \prod_\ell |a_\ell|_\ell\right).                            \tag{1.3}
\]

The product formula makes (1.3) invariant under the left action of `Q^*`, and
local units have absolute value one, so it descends to (1.1).

### Proposition 1.1

\[
 \widehat\deg L_p=\log p,
 \qquad L_p\ne\mathcal O_X.                                                \tag{1.4}
\]

### Proof

The only nonunit component of `a^(p)` is at `p`, where
`|p^{-1}|_p=p`.  Hence its idelic modulus is `p` and (1.3) is `log p`.
The trivial class has degree zero, so `L_p` is nontrivial. QED.

This inverse-uniformizer orientation is the effective one for Haran's section
lattice: scalar sections of `L_p^m` lie in `p^{-m}Z_p` at `p`.  It is the
completed-line-bundle class of the ordinary finite prime in the adelic
description (11.17)--(11.19).  No zeta value or RH input occurs.

## 2. Nonprincipal prime classes on the literal square

Let `S=Spec F{+-1}`, `Y=X x_S X`, and let `p_1,p_2:Y->X` be the projections.
The unconditional unit-torsor pullbacks of `a_66` give

\[
 \mathcal V_p^{(1)}=p_1^*L_p,
 \qquad
 \mathcal V_p^{(2)}=p_2^*L_p.                                              \tag{2.1}
\]

### Theorem 2.1 (unconditional in `Pic_tor`)

Both classes in (2.1), interpreted as the unit torsors of `a_66`, are
nontrivial in `Pic_tor(Y)`. Their completed Section-11 realizations require
H7-PRIME-REG.

### Proof

For the diagonal `Delta:X->Y`, functoriality gives

\[
 \Delta^*p_i^*L_p=L_p.                                                     \tag{2.2}
\]

If `p_i^*L_p` were trivial, its diagonal pullback would be trivial, contrary
to Proposition 1.1. QED.

### Corollary 2.2

The prime carriers in `114_a_17` have nonprincipal abstract line-bundle lifts,
detected by the curve normalization `log p`. Their completed-bundle lifts are
conditional on H7-PRIME-REG.

The wording “lift” is deliberate.  A theorem identifying

\[
 \mathcal O_Y(V_p^{(i)})\overset?=p_i^*L_p                                \tag{2.3}
\]

requires a definition of effective Cartier divisors and their associated
completed line bundles on Haran's pro-square.  The source defines the right
side of (2.3), while `114_a_17` defines the left-hand closed pro-subscheme;
it does not state the comparison theorem.

## 3. Updated surviving gate

The finite-prime part now has three literal pieces:

1. a closed prime ruling `V_p^(i)`;
2. exact incidence `Delta x_Y V_p^(i)=Spec F_p`;
3. conditionally on H7-PRIME-REG, a nontrivial completed Picard lift
   `p_i^*L_p` of degree `log p`.

What remains at this gate is no longer “find a nonprincipal `log p` carrier.”
It is:

1. prove the Cartier comparison (2.3);
2. construct a correspondence algebra extending these prime carriers;
3. construct a global intersection product inducing the finite degree above;
4. add the archimedean term and the proper section gauge.

`a_61` later globalizes the completed-bundle labels faithfully to every
integer `n` under H7-PRIME-REG, as corrected by `a_63`. It also shows that
comparison (2.3), strengthened to regular Cartier incidence, identifies their
graded normal layers with the geometric contacts `M_n`.

## 4. Verification scope

`114_a_18_h7_prime_picard_verify.py` checks the source equations, the product
formula on rational samples, the inverse-uniformizer degree, and the diagonal
left-inverse calculation.  It does not assert (2.3).
