# 114.a.129 — H7: pre-Picard exact sequence isolates the boundary obstruction

```
+------------------------------------------------------------------------+
| SOURCE      Haran D_1/Bun_1 records completed objects with generic      |
|             trivialization before the global GL_1(K) quotient.          |
| PRINCIPAL   p_2/p_1 removes only the finite part of the anti-divisor.    |
| RESIDUAL    Its Picard class is the mixed archimedean boundary class.    |
| EXACT GATE  Anti-faithfulness is equivalent to independence of those    |
|             boundary classes (H7-ARCH-BDRY).                            |
| LIMIT       The source defines the recipient, not the missing boundary  |
|             degree or Green comparison.                                 |
+------------------------------------------------------------------------+
```

## 1. Haran's canonical pre-Picard object

For a finite pro-level `Z_N`, equation (11.3) defines

\[
 D_1(Z_N)=\Gamma\bigl(Z_N,GL_1(\mathcal K_N)/GL_1(\mathcal O_{Z_N})\bigr).
                                                                        \tag{1.1}
\]

Its objects are completed rank-one data trivialized at the generic points.
Equations (11.11)--(11.15) form bounded completed pro-objects, and (11.16)
lets the global fraction group

\[
 GL_1(\mathcal K(Z))=\varinjlim_NGL_1(\mathcal K_N(Z_N))               \tag{1.2}
\]

act by changing the generic trivialization.  On every tensor-stable sector
where the rank-one operations are defined, this gives the exact pattern

\[
 GL_1(\mathcal O(Z))\longrightarrow GL_1(\mathcal K(Z))
 \xrightarrow{\mathrm{div}}D_1^{\rm cmp}(Z)
 \longrightarrow Pic_{\rm cmp}(Z)\longrightarrow0.                   \tag{1.3}
\]

Thus there is no need to invent a pre-Picard carrier.  What must still be
constructed is the archimedean boundary functional on it.

## 2. Correct decomposition of the anti-class

For `Z=Y^reg`, let

\[
 A_p=D_{p,1}-D_{p,2},\qquad h_p=p_2/p_1.                              \tag{2.1}
\]

The corrected calculation `a128` gives in the completed divisor object

\[
 A_p=\mathrm{div}(h_p)+B_p^\infty.                              \tag{2.2}
\]

Here `div(h_p)` cancels all finite local multipliers.  The residual
`B_p^infty` is supported in the sense of completed norms on the mixed real
boundary; it cannot be deleted by (11.4), because the required factors
`p` and `1/p` are not real `O`-units.

Passing through the last arrow in (1.3) kills only the principal term:

\[
 [A_p]=[B_p^\infty]\quad\text{in }Pic_{\rm cmp}(Y^{\rm reg}).          \tag{2.3}
\]

This corrects the false finite-only conclusion that `[A_p]=0`.

## 3. Exact prime-sector reduction

For a finite vector `a=(a_p)`, tensoring (2.2) gives

\[
 \sum_pa_pA_p=
 \mathrm{div}\,\!\left(\prod_p(p_2/p_1)^{a_p}\right)
 +\sum_pa_pB_p^\infty.                                                \tag{3.1}
\]

The diagonal argument of `a112` already proves that every possible kernel
element has this anti-form.  Therefore:

### Theorem 3.1 (boundary kernel formula)

\[
 \ker\rho=
 \left\{\sum_pa_p(e_{p,1}-e_{p,2}):
       \sum_pa_p[B_p^\infty]=0\right\}.                               \tag{3.2}
\]

In particular, the following are equivalent:

1. the prime presentation map `rho` is injective;
2. the classes `[B_p^infty]` are integrally independent;
3. the archimedean boundary map
   `a -> sum_p a_p[B_p^infty]` has zero kernel.

### Proof

Equation (3.1) and exactness of (1.3) identify the Picard image of every
anti-vector with its residual boundary class.  The kernel containment of
`a112` shows there are no other relations.  QED.

This is H7-ARCH-BDRY.  It is strictly narrower than computing the full
Picard group or all global units.

## 4. What a proof must now construct

A proof of H7-ARCH-BDRY needs a functorial homomorphism

\[
 \deg_\infty^{(1)}-\deg_\infty^{(2)}:
 \langle[B_p^\infty]\rangle\longrightarrow\mathbb R                 \tag{4.1}
\]

with

\[
 (\deg_\infty^{(1)}-\deg_\infty^{(2)})([B_p^\infty])=2\log p
 \quad\text{up to the fixed orientation convention}.                 \tag{4.2}
\]

Then unique factorization would make (3.2) trivial.  Formula (4.2) is the
expected norm computation, but it is not yet a theorem on the reflected
pro-square: one must define the two mixed-boundary restriction/norm maps and
prove invariance under Haran's completed equivalence and pro-transitions.

The numerical Green biextension of `a124` has exactly the required real
values, but using it to prove (4.1) before its geometric descent would be
circular.  H7-ARCH-BDRY, the two-target Deligne comparison, dynamic cycles,
row A and RH remain open.

## 5. Verification scope

`114_a_129_h7_framed_divisor_exact_verify.py` checks the exact anti-kernel
algebra, principal-plus-boundary decomposition and unique-factorization
detector, together with the Section-11 source anchors.  It does not assume
the missing geometric boundary degree (4.1).

**Later geometric reduction (`a130`).**  Pull the two literal mixed
boundaries back to `Y^reg`.  On them the anti-class restricts to the pullback
of `L_p^(-1)` and `L_p` from the remaining arithmetic factor.  Faithfulness
of either mixed-boundary pullback on the prime curve lattice implies
H7-ARCH-BDRY.
