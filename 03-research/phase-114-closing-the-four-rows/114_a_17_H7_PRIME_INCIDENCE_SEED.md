# 114.a.17 — H7–I7 prime incidence seed on the literal Haran square

```
+--------------------------------------------------------------------------+
| SPACE       Y = X x_S X is Haran's literal arithmetic square.           |
| CYCLES      The diagonal and both inverse images of every finite prime   |
|             are genuine pro-subschemes, obtained only by fiber products. |
| INCIDENCE   Delta x_Y (x_p x_S X) is canonically x_p = Spec F_p.         |
| MASS        log #F_p = log p, hence the local seed has Lambda(p^k).      |
| LIMIT       This is not yet a Frobenius correspondence or an             |
|             intersection product.                                       |
+--------------------------------------------------------------------------+
```

## 1. Literal objects

Put

\[
 S=\operatorname{Spec}\mathbb F\{\pm1\},\qquad
 X=\overline{\operatorname{Spec}\mathbb Z},\qquad
 Y=X\times_S X.
\]

Haran constructs `X` as a pro-generalized scheme and `Y` as its literal
fiber square.  Ordinary schemes embed fully faithfully in the generalized
category, so for every rational prime `p` the ordinary closed point

\[
 i_p:x_p=\operatorname{Spec}\mathbb F_p\longrightarrow X                 \tag{1.1}
\]

is present in the ordinary dense chart and is compatible with the transition
maps of the compactification.

There are three functorially defined pro-subschemes of `Y`:

\[
 \Delta:X\longrightarrow Y,\qquad
 V_p^{(1)}=x_p\times_S X,\qquad
 V_p^{(2)}=X\times_S x_p.                                                  \tag{1.2}
\]

No divisor group, metric or Frobenius endomorphism is used here.

## 2. Exact incidence theorem

### Theorem 2.1

For every rational prime `p`, there are canonical isomorphisms

\[
 \Delta\times_Y V_p^{(1)}\simeq x_p,
 \qquad
 \Delta\times_Y V_p^{(2)}\simeq x_p.                                     \tag{2.1}
\]

### Proof

This is a formal pullback identity in any category with finite fiber products.
For the first ruling, a point of the pullback is represented by `x in X` and
`(z,x') in x_p x_S X` with

\[
 (x,x)=(i_p(z),x').                                                        \tag{2.2}
\]

Thus `x=i_p(z)` and `x'=x`; the datum is uniquely `z in x_p`.  The construction
and its inverse use only projections and diagonals, so the identification is
an isomorphism of generalized schemes, level by level in the pro-system.  The
second ruling is symmetric. QED.

### Corollary 2.2 (the von Mangoldt mass is already geometric locally)

Define the finite arithmetic mass of a zero-dimensional ordinary incidence by

\[
 \deg_{\rm fin}(\operatorname{Spec}A)=\log\#A.                             \tag{2.3}
\]

Then

\[
 \deg_{\rm fin}(\Delta\times_YV_p^{(i)})=\log p.                           \tag{2.4}
\]

Consequently the labelled incidence family

\[
 C_n=\begin{cases}
       V_p^{(1)},&n=p^k,\ k\ge1,\\
       \varnothing,&n\text{ is not a prime power}
     \end{cases}                                                          \tag{2.5}
\]

has

\[
 \deg_{\rm fin}(\Delta\times_Y C_n)=\Lambda(n).                           \tag{2.6}
\]

Equation (2.6) is an incidence calculation, not yet the value of a global
Picard intersection pairing.

## 3. What this closes and what it does not

This closes one previously missing existence statement:

> the literal Haran square has genuine geometric carriers whose diagonal
> incidence is the ordinary residue field responsible for `log p`.

In particular, the local `Lambda` seed no longer has to be imported from the
cyclotomic quotient or stipulated as a bilinear form.

It does **not** yet supply the required correspondences `Gamma_n`:

1. the cycles `C_n` have labels but no composition law
   `Gamma_m circ Gamma_n=Gamma_{mn}`;
2. `C_{p^k}` is independent of `k`, so it records the von Mangoldt weight but
   not a degree-`p^k` Frobenius graph;
3. no Cartier/Weil divisor group or moving lemma on `Y` has been constructed;
4. (2.3) is the correct local normalization, but no global intersection theory
   has yet been proved to induce it;
5. the archimedean component, proper gauge and Riemann--Roch remain open.

Thus H7-I7 is sharpened from “find any geometric source of `log p`” to the
smaller task:

> extend the prime incidences to a correspondence algebra and prove that a
> global intersection product on the completed square has (2.3) as its finite
> local term.

## 4. Verification scope

`114_a_17_h7_prime_incidence_verify.py` checks the primary-source anchors, the
finite-set model of the categorical pullback identity, and the exact
von-Mangoldt labelling through a finite test range.  It does not certify the
five open structures listed above.
