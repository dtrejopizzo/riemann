# 114.a.26 — H7-EVAL is a Laurent normal-form theorem

```
+--------------------------------------------------------------------------+
| REDUCTION   Restrict to the scalar subring actually used by P_{m,n}.     |
| SOURCE      Q[x_l^{+-1}: l prime] maps to the two-ruling scalar ring.    |
| THEOREM     Power evaluations descend for every sigma>0 iff this map is  |
|             injective.                                                   |
| GAIN        H7-EVAL is now one explicit normal-form lemma, not an         |
|             unspecified boundary construction.                          |
| STATUS      The equivalence is proved; `114_a_27` reduces injectivity to |
|             differential faithfulness H7-DFLAT.                          |
+--------------------------------------------------------------------------+
```

## 1. The minimal scalar ring

Let `A` be the generic scalar ring of the localized arithmetic plane
`Z tensor_F Z`, equipped with the addition of the first ruling.  Write
`i_1,i_2` for the two multiplicative scalar maps from `Q`.  The mixed
sections of `114_a_25` use only finite first-additive sums of products

\[
 i_1(a)i_2(b),\qquad a,b\in\mathbb Q.                    \tag{1.1}
\]

Consequently it is enough to work in the subring

\[
 A_{12}:=\mathbb Q[\,i_2(b):b\in\mathbb Q^\times\,]
 \subseteq A,                                            \tag{1.2}
\]

where the coefficient field is the first ruling.  No assertion about all
alternating Haran trees is needed for the lower bound.

Let

\[
 L:=\mathbb Q[x_\ell^{\pm1}:\ell\ {\rm prime}]
    \simeq \mathbb Q[\mathbb Q_{>0}^{\times}]            \tag{1.3}
\]

and define the canonical surjection

\[
 \Phi:L\longrightarrow A_{12},\qquad
 x_\ell\longmapsto i_2(\ell).                            \tag{1.4}
\]

It is surjective by the definition of `A_12`: signs belong to the first
coefficient field, and unique factorization writes every positive rational
as a Laurent monomial in the prime variables.  Put

\[
 J_{\rm Har}:=\ker\Phi.                                  \tag{1.5}
\]

Thus `J_Har` is exactly the collection of additional first-additive scalar
relations imposed by Haran's tree relations on the second ruling.

## 2. Power characters separate the Laurent algebra

For every `sigma>0` there is a ring homomorphism

\[
 \chi_\sigma:L\longrightarrow\mathbb R,
 \qquad x_\ell\longmapsto\ell^\sigma.                   \tag{2.1}
\]

### Lemma 2.1

\[
 \bigcap_{\sigma>0}\ker\chi_\sigma=0.                  \tag{2.2}
\]

### Proof

Every Laurent polynomial has a unique finite expression

\[
 f=\sum_{r\in S}a_r[r],\qquad
 S\subset\mathbb Q_{>0}\text{ finite}.                  \tag{2.3}
\]

If all `chi_sigma(f)` vanish, then

\[
 \sum_{r\in S}a_r e^{\sigma\log r}=0
 \quad(\sigma>0).                                       \tag{2.4}
\]

Order the distinct `r`.  Divide by the largest exponential and let
`sigma` tend to infinity; its coefficient vanishes.  Induction removes all
terms.  Hence `f=0`. QED.

## 3. Exact equivalence with H7-EVAL on the needed subring

### Theorem 3.1 (Laurent normal-form criterion)

The following are equivalent.

1. For every `sigma>0`, the character `chi_sigma` descends through `Phi` to
   a ring map
   \[
     E_\sigma:A_{12}\longrightarrow\mathbb R            \tag{3.1}
   \]
   satisfying
   \[
     E_\sigma(i_1(a))=a,\qquad
     E_\sigma(i_2(b))=\mathrm{sgn}(b)|b|^\sigma.   \tag{3.2}
   \]
2. `J_Har=0`.
3. `Phi` is an isomorphism
   \[
     \mathbb Q[x_\ell^{\pm1}:\ell\ {\rm prime}]
       \xrightarrow{\sim} A_{12}.                       \tag{3.3}
   \]

### Proof

For fixed `sigma`, descent is equivalent to
`J_Har subset ker chi_sigma`.  Descent for every positive `sigma` is
therefore equivalent, by Lemma 2.1, to `J_Har=0`.  Since `Phi` is already
surjective, this is equivalent to (3.3).  Formula (3.2) follows from unique
factorization and the treatment of the sign as a coefficient. QED.

### Corollary 3.2

The H7-EVAL hypothesis used in `114_a_25` does not require a morphism on the
whole localized commutative bio.  It is enough, and is equivalent, to prove
the Laurent normal-form statement (3.3) on `A_12`.

This is also a sharp criterion: constructing all the proposed power
evaluations cannot be easier than proving injectivity of `Phi`, because the
characters jointly detect every nonzero Laurent relation.

## 4. What Haran's source does and does not prove

Haran 2017 equations (10.6)--(10.22) give tree representatives, their
relations, and the ordinary ring obtained by choosing one addition.  They
make (1.4) canonical.  Equations (10.23)--(10.25) give the power action on a
boundary rig and its spectrum.  They do not state a confluence theorem for
the tree relations or the injectivity of (1.4).  Therefore the source does
not by itself prove `J_Har=0`.

The algebraic gate isolated here is:

> **H7-LNF.** Prove that no nonzero Laurent polynomial in the second-ruling
> prime scalars becomes zero under the first-ruling addition in the localized
> scalar ring of `Z tensor_F Z`.

By Theorem 3.1, H7-LNF is exactly H7-EVAL on the portion needed for the mixed
lower bound. `114_a_27` proves H7-LNF conditional on the exact
differential-faithfulness statement H7-DFLAT; the source does not establish
that statement. Genuine real-boundary membership and H7-U remain separate
gates.

**Resolution (`a_49`).** The homogeneous-endobio representation proves
H7-TBIO for every positive power parameter. Hence every character used in
Theorem 3.1 factors through Haran's scalar quotient. Their joint separation
therefore proves `J_Har=0` and closes H7-LNF unconditionally. This does not
revive raw H7-U, which `a_31` rules out as the compatible upper gauge.

## 5. Verification scope

`114_a_26_h7_laurent_gate_verify.py` checks unique Laurent encoding, exact
power-character separation on finite supports, and the factor-through
kernel criterion on finite polynomial models.  It does not assert H7-LNF.
The later proof of H7-LNF is Theorem 4.1 and Corollary 4.2 of `a_49`.
