# 114.a.117 — H7: calibrated selective quotient on the saturated rays

```
+------------------------------------------------------------------------+
| BLOCK       a55 maps bounded sections onto F_p^m at linear bidegrees.  |
| SELECT      Keep k_m=floor[(log 2)/(2 log 3) m] ordered odd moments.   |
| EXACT       The selected bounded image is all F_p^(k_m).               |
| RR          k_m log p=d_1 d_2/(2 log 3)+o(m^2).                        |
| LIMIT       Per-block/ray result; denominator transitions and exactness |
|             remain open.                                               |
+------------------------------------------------------------------------+
```

## 1. The saturated bounded block

Use the block of `a55`.  Thus `m=2r`, the odd moment exponents are ordered

\[
 1,3,\ldots,2m-1,                                                       \tag{1.1}
\]

and the controlled prime satisfies `p>2^(2m)` and `log p=Theta(m)`.  Put

\[
 A=m(p-1),\qquad
 d_1=\log A,\qquad d_2=m\log2.                                         \tag{1.2}
\]

Theorem 2.1 of `a55` constructs, for every `y in F_p^m`, a genuine bounded
cross-contraction section of bidegree `(d_1,d_2)` whose moment vector is
exactly `y`.

## 2. Canonical calibrated projection

Set

\[
 \alpha=\frac{\log2}{2\log3},\qquad
 k_m=\lfloor\alpha m\rfloor.                                           \tag{2.1}
\]

Let

\[
 \pi_m:\mathbb F_p^m\longrightarrow\mathbb F_p^{k_m}                  \tag{2.2}
\]

retain the first `k_m` coordinates in the intrinsic increasing order (1.1).
It is a unital ring quotient and therefore respects the selected addition
and multiplication.

Define the per-block selective scalar dimension by

\[
 h_{\rm cal}(D_{m,p})
 =\log\#\pi_m\mathcal E_{m,p}igl(H^0_{\rm bd}(D_{m,p})\bigr).         \tag{2.3}
\]

### Theorem 2.1 (exact selected image)

\[
 \pi_m\mathcal E_{m,p}igl(H^0_{\rm bd}(D_{m,p})\bigr)
 =\mathbb F_p^{k_m},
 \qquad h_{\rm cal}(D_{m,p})=k_m\log p.                               \tag{2.4}
\]

### Proof

The full bounded image is `F_p^m` by `a55`.  A coordinate projection of a
full product is the full selected product.  Its cardinality is `p^(k_m)`.
QED.

This quotient removes the explicit saturation excess rather than attempting
to prove that it was absent.

## 3. Sharp RR coefficient on the saturated ray

The degree-product target from `a53`/`a116` is

\[
 \frac{d_1d_2}{2\log3}
 =\alpha m\log(m(p-1)).                                                 \tag{3.1}
\]

Using `k_m=alpha m+O(1)` and

\[
 \log(m(p-1))=\log p+\log m+O(1/p),                                   \tag{3.2}
\]

we obtain

\[
 \begin{aligned}
 h_{\rm cal}(D_{m,p})-\frac{d_1d_2}{2\log3}
 &= (k_m-\alpha m)\log p
    -\alpha m\log m+O(m/p)\\
 &=O(m\log m)=o(m^2),                                                   \tag{3.3}
 \end{aligned}
\]

because `log p=Theta(m)`.  Hence

\[
 \boxed{
 h_{\rm cal}(D_{m,p})
 =\frac{d_1d_2}{2\log3}+o(m^2).
 }                                                                      \tag{3.4}
\]

Both the upper and lower bounds are exact before taking the asymptotic: the
selected target itself has `p^(k_m)` points and bounded interpolation hits
all of them.

## 4. Relation to H7-SEL-MOM

The construction does not require the fixed balanced code `I_r(Q)` to remain
injective after projection.  Clause 2 of the `a32` acceptance test permits
instead a normalized dimension with the required quadratic growth.  Here
the retained bounded interpolation family supplies that lower bound and the
finite target supplies the matching upper bound.

Thus the numerical/multiplicative **per-block** part of H7-SEL is closed on
the saturated cofinal rays.  What remains is no longer selection of the
correct coefficient, but globalization:

1. choose compatible residue targets when divisors later contain the old
   residue characteristics (H7-DEN-TRANS);
2. prove independence of divisor presentation and principal changes;
3. make the selected coordinates compatible with restriction maps and exact
   sequences;
4. identify the resulting global leading term with the geometric
   excess/Green intersection from H7-REG-EXCESS-RR.

The first-`k_m` rule is canonical inside a given ordered block, but no claim
is made that blocks for different primes or divisor presentations glue.
Consequently this does not close H7-SEL-RR/EXACT, row A or RH.

## 5. Verification scope

`114_a_117_h7_calibrated_selective_quotient_verify.py` checks exact coordinate
surjectivity on finite products, the floor error, the degree formula and the
`o(m^2)` estimate along exponentially sized controlled primes.  Bounded
realization of every full-block vector is the theorem of `a55`.
