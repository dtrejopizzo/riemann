# 114.a.27 — H7-LNF: the differential-faithfulness criterion

```
+--------------------------------------------------------------------------+
| SOURCE      Haran 2017, Section 6 (modules/differentials) and            |
|             (7.13)--(7.16) (the prime differential module).              |
| BASE CHANGE Relative differentials of the coproduct are induced from     |
|             the second copy.                                             |
| CRITERION   Faithfulness of the induced prime module implies that        |
|             Q[x_l^{+-1}: l prime] -> A_12 is injective.                  |
| SOURCE GAP  Scalar freeness is proved before generalized base change;   |
|             the required faithfulness afterward is not stated.           |
| NOT CLOSED  H7-DFLAT, genuine boundary membership and H7-U.              |
+--------------------------------------------------------------------------+
```

## 1. Set-up and the source differential

Put

\[
 B=\mathbb Z_1\underset{\mathbb F\{\pm1\}}\otimes\mathbb Z_2.
                                                               \tag{1.1}
\]

Let `R` be the scalar ring of `B` with the addition selected by the first
copy. Localize both rulings at the nonzero integers, obtaining `R_Q` and
scalar maps `i_1,i_2`.

Haran 2017 Section 6 constructs modules, extension of scalars, universal
differentials and square-zero extensions. In (7.13)--(7.16), after the
quotient (7.12) and rationalizing the factor `1/2`, he obtains a derivation

\[
 \partial(n)=\sum_\ell v_\ell(n)\frac n\ell\,\partial\ell,
                                                               \tag{1.2}
\]

whose scalar target `Omega_pr` is free abelian on `partial l`, one symbol
for each prime. Signs extend because `-1` belongs to the base and has zero
relative differential. Localization gives the usual inverse rule.

Only this quotient derivation is used. We do not assert that the full
unquotiented cotangent module is free.

## 2. Base change and the exact faithfulness gate

### Lemma 2.1 (relative coproduct base change)

For every `B`-module `M`, restriction to the second coproduct factor gives

\[
 \operatorname{Der}_{\mathbb Z_1}(B,M)
 \simeq
 \operatorname{Der}_{\mathbb F\{\pm1\}}(\mathbb Z_2,M). \tag{2.1}
\]

Thus the induced prime-differential module is

\[
 M_{\rm pr}=B\underset{\mathbb Z_2}{\otimes}\Omega_{\rm pr}.
                                                               \tag{2.2}
\]

### Proof

A relative derivation is, by Haran (6.6), a lift to the square-zero
extension `B pi M`. A map from the pushout (1.1) to `B pi M` under `Z_1`
is, by the pushout universal property, exactly a map from `Z_2` under the
common base, with prescribed reduction to `B`. This proves (2.1); its
representing-object form is (2.2). QED.

After localization there is a natural coefficient-action map

\[
 \tau:\bigoplus_\ell R_Qe_\ell
 \longrightarrow(M_{\rm pr})_{[1]}.                     \tag{2.3}
\]

The source proves that the scalar group of `Omega_pr` before base change is
free abelian on the `partial l`. It does not identify (2.3) as an
isomorphism or state that it is injective. In the generalized module
category this does not follow merely because extension of scalars preserves
coproducts: a generalized ring is a set-valued operadic object, not
automatically its own regular module.

We isolate the exact missing statement:

> **H7-DFLAT.** The map `tau` in (2.3) is injective on every finite sum of
> prime directions occurring in a Laurent polynomial.

The induced relative derivation is ordinary-additive for first addition and
satisfies Leibniz. Formula (1.2) gives

\[
 D(i_2(n))=\sum_\ell v_\ell(n)i_2(n/\ell)e_\ell,
 \qquad D(i_2(\ell))=e_\ell.                            \tag{2.4}
\]

## 3. Conditional Laurent normal form

Recall the surjection of `114_a_26`

\[
 \Phi:L=\mathbb Q[x_\ell^{\pm1}:\ell\ \text{ prime}]
 \longrightarrow A_{12}\subseteq R_Q,
 \qquad x_\ell\longmapsto i_2(\ell).                   \tag{3.1}
\]

### Theorem 3.1 (differential criterion for H7-LNF)

If H7-DFLAT holds, `Phi` is injective.

### Proof

Assume its kernel is nonzero. Multiplying a Laurent relation by a monomial
gives a nonzero polynomial relation. Choose

\[
 0\ne F\in\mathbb Q[x_{\ell_1},\ldots,x_{\ell_s}]
 \cap\ker\Phi                                             \tag{3.2}
\]

of minimal total degree. A nonzero constant cannot lie in the kernel: the
fold `B -> Z`, followed by localization, retracts the first coefficient
field.

Apply `D` to `F(Phi(x))=0`. The chain rule gives

\[
 0=\tau\left(\sum_{j=1}^s
   \Phi\!\left(\frac{\partial F}{\partial x_{\ell_j}}\right)
   e_{\ell_j}\right).                                    \tag{3.3}
\]

H7-DFLAT implies that every coefficient in (3.3) vanishes. In
characteristic zero a nonconstant polynomial has a nonzero partial
derivative. Such a derivative is a nonzero kernel element of smaller total
degree, a contradiction. Hence `ker Phi=0`. QED.

### Corollary 3.2 (conditional H7-EVAL)

Under H7-DFLAT, every `sigma>0` defines

\[
 E_\sigma:A_{12}\longrightarrow\mathbb R,
 \quad E_\sigma(i_1(a)i_2(b))
      =a\,\operatorname{sgn}(b)|b|^\sigma,               \tag{3.4}
\]

extended first-additively. Then `114_a_25` makes

\[
 \mathcal P_{m,n}:I_{m+1}(q^n)\longrightarrow A_{12}     \tag{3.5}
\]

injective, with

\[
 \log\#I_{m+1}(q^n)=mn\log q-O(m\log m+n).              \tag{3.6}
\]

Thus H7-DFLAT is sufficient to close algebraic lower-bound injectivity. Even
then, global boundedness at every real chart (H7-B) and the upper normal-form
bound (H7-U) remain.

## 4. Verification boundary

The conditional implication uses the coproduct universal property, Haran's
module adjunction, the prime differential, localization and the
characteristic-zero degree argument. It does not promote scalar freeness
before base change to H7-DFLAT. No zero of `xi`, explicit formula or
positivity statement is used.

`114_a_27_h7_differential_injectivity_verify.py` checks the prime
differential, inverse rule, chain rule and degree descent. It does not assert
H7-DFLAT.
