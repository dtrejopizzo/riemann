# 114.a.31 — H7 no-go: Laurent faithfulness versus the upper bound

> **Geometric typing correction (`a_63`).** The scalar counting no-go remains
> valid. Any assertion that its scalar family is a completed bundle section
> on `Y` is conditional on H7-PB-REG/H7-PRIME-REG.

```
+--------------------------------------------------------------------------+
| FAMILY      Use every positive second-axis leaf k/q^d in the bounded     |
|             dyadic tree of a_30.                                         |
| COUNT       N=2^d leaves give binomial(N+q^d-1,N) multisets.             |
| IF LNF      Distinct multisets are distinct bounded scalar sections.     |
| GROWTH      log h0 >= (2^d-1)log 2 at bidegree (2d,d).                  |
| NO-GO       H7-LNF and H7-U cannot both hold for raw scalar cardinality. |
| CONSEQUENCE The full-Laurent route fails; a selective quotient, a        |
|             normalized dimension, or a different gauge is required.     |
+--------------------------------------------------------------------------+
```

## 1. The full leaf-multiset family

Fix a prime `q>=3`, put

\[
 N=2^d,\qquad Q=q^d.                                    \tag{1.1}
\]

Use the complete dyadic tree `A_d` of `114_a_30`. Every one of the `Q`
positive scalars

\[
 i_2(k/Q),\qquad 1\le k\le Q,                           \tag{1.2}
\]

is a section of `L_q^d`. For a multiplicity vector

\[
 \nu=(\nu_1,\ldots,\nu_Q)\in\mathbb Z_{\ge0}^Q,
 \qquad\sum_{k=1}^Q\nu_k=N,                             \tag{1.3}
\]

fill exactly `nu_k` leaves by `i_2(k/Q)`. Commutativity and associativity of
the first addition make the resulting scalar depend only on `nu`:

\[
 S_{d}(\nu)=4^{-d}\sum_{k=1}^{Q}\nu_k i_2(k/Q).          \tag{1.4}
\]

### Proposition 1.1 (unconditional boundedness)

Every `S_d(nu)` is a genuine scalar pro-section of

\[
 p_1^*L_2^{2d}\otimes p_2^*L_q^d.                       \tag{1.5}
\]

### Proof

This is Theorem 3.1 of `114_a_30`: every internal row and column is
`(1/2,1/2)`, a strict Euclidean contraction, and every leaf lies in the
second real unit interval. The finite denominators are exactly `2^{2d}` and
`q^d`. The proof is uniform in the leaf values, so it applies to all
multisets (1.3). QED.

The number of multiplicity vectors is the stars-and-bars count

\[
 \#\{\nu\}= {N+Q-1\choose N}.                            \tag{1.6}
\]

## 2. Faithfulness makes the count superquadratic

### Theorem 2.1

Assume H7-LNF, equivalently injectivity of

\[
 \Phi:\mathbb Q[\mathbb Q_{>0}^{\times}]\longrightarrow A_{12}.
                                                               \tag{2.1}
\]

Then all sections (1.4) are distinct and

\[
 \log\#\{S_d(\nu)\}
 \ge(2^d-1)\log2.                                      \tag{2.2}
\]

### Proof

The positive rationals `k/Q`, `1<=k<=Q`, are distinct basis elements of the
group algebra in (2.1). Hence two sums (1.4) agree only if every coefficient
`nu_k` agrees.

Since `q>=3`, `Q=q^d>=2^d=N`. Therefore

\[
 {N+Q-1\choose N}\ge {2N-1\choose N}\ge2^{N-1}.        \tag{2.3}
\]

The last inequality follows, for example, by the elementary injection from
binary words of length `N-1` into `N`-subsets of a `2N-1` element set, or
from the central-binomial bound. Substitute `N=2^d`. QED.

## 3. Incompatibility theorem

The bidegree in (1.5) is `(m,n)=(2d,d)`. A surface-type upper bound H7-U
would require

\[
 \log\#\mathcal O_Y
  (p_1^*L_2^{2d}\otimes p_2^*L_q^d)_{[1],[1]}
 \le Cmn+O(m+n)=O(d^2).                                 \tag{3.1}
\]

But (2.2) is `Omega(2^d)`. Thus:

### Theorem 3.1 (H7-LNF/H7-U no-go)

For the raw cardinality of all bounded scalar sections on Haran's literal
square,

\[
 \boxed{\mathrm{H7\!\!-LNF}\quad\Longrightarrow\quad
        \neg\mathrm{H7\!\!-U}.}                         \tag{3.2}
\]

In particular H7-DFLAT, which implies H7-LNF by `114_a_27`, cannot complete
the desired lower-and-upper quadratic package. If H7-DFLAT is true, the raw
bounded scalar set is far too large for H7-U; if it is false, that full
Laurent normal-form proof of the lower bound fails.

This does not rule out a more selective quotient of Haran trees that is
injective on the balanced code of `a_30` but collapses most leaf multisets.
It rules out using **full** Laurent faithfulness to prove the lower bound
while retaining the desired upper bound.

## 4. Meaning for G-7

This is not a failure of real boundedness. Every section counted above is
genuinely local at the real boundary. The failure is that the operadic
closure of a bounded binary node creates exponentially many internal leaves
at only linear divisor cost.

It is the fixed-scalar counterpart of the variable-arity warning in
`114_a_23`: hiding the arity inside a scalar tree does not remove arity
inflation from raw cardinality.

Therefore the surviving G-7 program must define and prove one of:

1. **H7-SEL:** a selective normal-form theorem that separates the balanced
   `exp(Theta(mn))` code but leaves only `exp(O(mn))` bounded scalar classes;
2. an intrinsic minimal-generator/continuous dimension that quotients this
   operadic closure and has quadratic Hilbert--Samuel growth;
3. a geometric complexity truncation canonically determined by the divisor,
   together with a proof that it is compatible with multiplication and RR;
4. a different gauge whose local unit ball excludes the dyadic iteration
   while retaining the required mixed quadratic family.

No such datum is supplied by Haran's current bounded-bundle definition
(11.11)--(11.16). Hence the full-Laurent raw-cardinality route is closed
negatively. Selective-cardinality and normalized-dimension routes remain
open as new constructions.

## 5. Verification scope

`114_a_31_h7_lnf_upper_nogo_verify.py` checks bounded-node parameters,
stars-and-bars counts, the binomial lower bound and the exponential versus
quadratic separation. It treats H7-LNF as the explicit hypothesis of
Theorem 2.1 and does not assert it.
