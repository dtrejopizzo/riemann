# 114.a.16 — H7-Pic descent criterion: two concrete statements kill the anti-diagonal kernel

> **Typing refinement (`a_63`--`a_66`).** This descent criterion is
> unconditional for abstract unit-torsor pullbacks in `Pic_tor`. Applying it
> to completed Section-11 lattices additionally requires H7-PB-REG.

```
+--------------------------------------------------------------------------+
| INPUT        delta(L)=p_2^*L tensor p_1^*L^{-1} is trivial on X x_S X.  |
| DEFECT       A chosen trivialization fails descent by one global unit on |
|              X x_S X x_S X.                                            |
| CRITERION    Injectivity of partial-diagonal restriction on units plus   |
|              effective line-bundle descent forces L to come from S.     |
| CONSEQUENCE  Since Pic(S)=0, those two statements make delta injective   |
|              and close the anti-diagonal gate of G-7.                    |
+--------------------------------------------------------------------------+
```

## 1. Setting

Let

\[
 S=\mathrm{Spec}\,\mathbb F\{\pm1\},\qquad
 \pi:X=\overline{\mathrm{Spec}\,\mathbb Z}\longrightarrow S,
\]

and write `X^[n]` for the `n`-fold fiber product over `S`.  For
`L in Pic(X)` define the Cech difference

\[
 \delta(L)=p_2^*L\otimes p_1^*L^{-1}\in\mathrm{Pic}(X^{[2]}). \tag{1.1}
\]

This is the anti-diagonal part isolated in `114_a_12`.

## 2. Normalized descent defect

Assume `delta(L)=0`. Choose an isomorphism

\[
 \varphi:p_1^*L\xrightarrow{\sim}p_2^*L.                \tag{2.1}
\]

Its pullback along the diagonal is an automorphism of `L`, hence multiplication
by a global unit `u in Gamma(X,O_X^*)`. Multiplying `varphi` by the inverse
pullback of `u`, we may and do normalize

\[
 \Delta^*\varphi=\mathrm{id}_L.                   \tag{2.2}
\]

On `X^[3]`, let `varphi_ij` denote pullback along the indicated projection and
define

\[
 c(\varphi)=\varphi_{13}^{-1}\varphi_{23}\varphi_{12}
 \in\Gamma(X^{[3]},\mathcal O^*).                       \tag{2.3}
\]

This is exactly the obstruction to the Cech cocycle condition.

### Lemma 2.1

Let `d_12:X^[2]->X^[3]` be the partial diagonal `(x,z)->(x,x,z)`. Then

\[
 d_{12}^*c(\varphi)=1.                                  \tag{2.4}
\]

### Proof

On the partial diagonal, `varphi_12=id` by (2.2), while `varphi_23` and
`varphi_13` become the same isomorphism from the copy at `x` to the copy at
`z`. Their quotient is one. QED.

## 3. Exact anti-diagonal theorem

### Theorem 3.1

Assume:

- **(U3) unit detection:**
  \[
  d_{12}^*:\Gamma(X^{[3]},\mathcal O^*)
       \longrightarrow\Gamma(X^{[2]},\mathcal O^*)
  \quad\text{is injective};                              \tag{3.1}
  \]
- **(LD) line-bundle descent:** every line bundle on `X` equipped with an
  isomorphism (2.1) satisfying the Cech cocycle condition descends effectively
  to a line bundle on `S`.

Then

\[
 \ker\delta=\pi^*\mathrm{Pic}(S).                 \tag{3.2}
\]

In particular, since `Pic(S)=0`, `delta` is injective and the external Picard
map of `114_a_12` has no anti-diagonal kernel.

### Proof

The inclusion `pi^*Pic(S) subset ker(delta)` is functorial. Conversely, take
`L in ker(delta)` and normalize `varphi` as above. Lemma 2.1 and (U3) imply
`c(varphi)=1`, so `varphi` is a descent datum. By (LD), `L` is the pullback of
a line bundle on `S`. This proves (3.2). The absolute affine point has trivial
Picard group because its structure object is already its fraction object, so
the final assertion follows. QED.

### Corollary 3.2 (simple sufficient unit computation)

Condition (U3) follows if both global-unit groups in (3.1) are the base units
`{+-1}` and partial-diagonal restriction is the identity on them. Therefore a
calculation

\[
 \Gamma(X^{[n]},\mathcal O^*)=\{\pm1\},\qquad n=2,3,      \tag{3.3}
\]

together with effective descent would close H7-Pic.

## 4. What the sources do and do not give

Haran computes

\[
 \Gamma(X,\mathcal O_X)=\mathbb F\{\pm1\}
\]

for the compactified arithmetic curve, and constructs all finite fiber
products in the generalized-scheme category.  The read sources do not compute
the global units of `X^[2]` or `X^[3]`, and do not state an fpqc/effective
descent theorem for the completed line bundles of 2017 section 11.

Thus the former single phrase “decide the anti-diagonal kernel” has been
replaced by two explicit tasks:

1. **H7-U3:** compute units on the double and triple square and prove (3.1);
2. **H7-LD:** prove effective descent for Haran's bounded completed line
   bundles along `X->S`.

Either a direct finite-cocycle computation or an absolute-point slice from
`114_a_12` can still bypass these hypotheses.

## 5. Verification scope

`114_a_16_h7_descent_source_verify.py` checks the primary-source anchors and
the finite sign-unit model of Lemma 2.1. It does not mark (U3) or (LD) proved;
those are the two open mathematical statements isolated here.
