# 114.a.24 — H7-R: intrinsic binary rank and the canonical mixed map

> **Geometric typing correction (`a_63`).** The scalar/bio map and its entropy
> statements remain valid. Its interpretation as a section of the displayed
> completed bundle on `Y` requires H7-PB-REG/H7-PRIME-REG.

```
+--------------------------------------------------------------------------+
| FIRST AXIS  P=p^m has the exact minimal binary generator count          |
|             r_m=ceil(log_2(P+1))=Theta(m).                              |
| SECOND AXIS Q=q^n supplies the intrinsic l1 radius.                      |
| DOMAIN      I_{r_m}(Q) has log-cardinality Theta(mn).                   |
| MAP         Sum external products f_j box (c_j/Q) in B_{m,n}.           |
| RESOLVED    a_28/a_30 prove boundary boundedness; a_49 proves            |
|             off-diagonal injectivity. Global normalized RR stays open.  |
+--------------------------------------------------------------------------+
```

## 1. The intrinsic rank from the first axis

Put `P=p^m` and

\[
 r_m=\left\lceil\log_2(P+1)\right\rceil.                 \tag{1.1}
\]

The sections of `L_p^m` are `k/P`, `|k|<=P`, by `114_a_20`.  Define

\[
 f_j=2^j/P,\qquad 0\le j<r_m.                            \tag{1.2}
\]

### Proposition 1.1

The signed family `{f_j}` generates every scalar section of `L_p^m` with the
mass constraint

\[
 \frac1P\sum_j|\alpha_j|2^j\le1,
 \qquad \alpha_j\in\{-1,0,1\},                           \tag{1.3}
\]

and no smaller signed family can do so.  Hence `r_m` is intrinsic: it is the
minimal generator dimension of the first-axis interval.

### Proof

Binary expansion represents each `0<=k<=P` as a subset sum of
`1,2,...,2^{r_m-1}` whose total is `k`; use the opposite signs for `-k`.
This proves generation and (1.3).  Conversely the `P+1` nonnegative sections
require distinct subsets of any fixed oriented generating family, so `d`
generators give at most `2^d` such sections. Thus `2^d>=P+1` and
`d>=r_m`. QED.

## 2. The canonical mixed domain

Put `Q=q^n` and use the cross-polytope

\[
 I_{r_m}(Q)=\{c\in\mathbb Z^{r_m}:\|c\|_1\le Q\}.         \tag{2.1}
\]

Its exact cardinality is

\[
 \#I_r(Q)=\sum_{j=0}^{\min(r,Q)}2^j{r\choose j}{Q\choose j}.               \tag{2.2}
\]

Indeed, choose the `j` nonzero coordinates, their signs, and a positive
`j`-tuple with total at most `Q`.

### Theorem 2.1 (quadratic domain entropy)

For fixed distinct primes `p,q`, as `m,n->infinity` with comparable size,

\[
 \log\#I_{r_m}(q^n)
 =\frac{\log p\,\log q}{\log2}\,mn-O(m\log m+n).          \tag{2.3}
\]

In particular the logarithmic cardinality is `Theta(mn)`.

### Proof

Here `r_m=(m log p)/(log2)+O(1)` and `r_m=o(Q)`.  The positive boundary alone
has `{Q+r_m-1 choose r_m-1}` points, while
`#I_{r_m}(Q)<=(2Q+1)^{r_m}`.  Stirling's formula gives

\[
 \log {Q+r_m-1\choose r_m-1}
 =r_m\log Q-O(r_m\log r_m),                               \tag{2.4}
\]

and both bounds have leading term
`(log p log q/log2)mn`. QED.

The same lower/upper squeeze proved in G-1 (whose finite bounds hold for every
integer `r,Q`) gives, on the diagonal `m=n=t`,

\[
 \dim_{r_t}(q^t)
 \sim\frac{\log p\,\log q}{(\log2)^2}t^2.                 \tag{2.5}
\]

Thus both the theta-count and minimal-generator versions have a fixed,
derived quadratic constant.

## 3. The scalar mixed map

For `c=(c_0,...,c_{r_m-1}) in I_{r_m}(Q)`, define at the generic level

\[
 \mathcal K_{m,n}(c)
 =\mathop{+_{(1)}}_{j=0}^{r_m-1}
       p_1^*(2^j/P)\,p_2^*(c_j/Q).                       \tag{3.1}
\]

Each summand is an external product of scalar sections and the outer
`+_(1)` is one of Haran's two scalar additions.  Formula (3.1) has fixed
input/output arity `[1]->[1]`; the rank `r_m` appears as the number of terms,
not as an arbitrarily selected component arity.

### Proposition 3.1 (all collapsed mass tests pass)

After diagonal fold and ordinary real realization,

\[
 \left|\Delta^*\mathcal K_{m,n}(c)\right|
 \le\sum_j\frac{2^j}{P}\frac{|c_j|}{Q}
 \le\frac{\|c\|_1}{Q}\le1.                              \tag{3.2}
\]

### Proof

Every `j<r_m` has `2^j<=P`; apply the triangle inequality and (2.1). QED.

## 4. Exact remaining Künneth statement

The construction passes the intrinsic-rank and collapsed-mass audits.  To
turn Theorem 2.1 into quadratic growth on the literal square one must prove:

> **H7-KI.** The map `K_{m,n}` in (3.1) is injective after Haran's tree
> relations, and its values lie in the genuine bounded pro-section set
> `O_Y(B_{m,n})_1` at every real-boundary chart.

Diagonal restriction cannot prove injectivity: `114_a_20` bounds its image by
`exp(O(m+n))`, whereas the domain has `exp(Theta(mn))` elements.  Thus H7-KI
is precisely an off-diagonal normal-form theorem, not an ordinary rational
linear-independence statement.

If H7-KI holds, (2.3) supplies the H7-K lower bound without variable-arity
inflation.  A matching upper bound on all scalar bounded normal forms remains
H7-U.

**Later resolution.** `a_28` and `a_30` prove genuine boundary membership for
the surviving Laurent family, while `a_49` proves the power-evaluation
factorization and hence injectivity. Thus H7-KI is closed on that family.
`a_31` rules out raw H7-U; the compatible upper gauge is the finite-moment
normalization of `a_33`, whose global promotion remains H7-FMD-ALL/H7-RR0.

## 5. Verification scope

`114_a_24_h7_intrinsic_rank_verify.py` checks the exact binary generator
count, formula (2.2), its asymptotic bounds and (3.2).  It deliberately does
not by itself mark H7-KI or H7-U proved; the later status is as above.
