# 114.a.11 — G-1 closed: the exact higher-rank CC constant is binary

```
+--------------------------------------------------------------------------+
| RESULT       For r=m k+1 and n=floor(exp(m a)), k,a>0,                  |
|                                                                          |
|                 dim_r(n)/(k a m^2)  --->  1/log 2.                      |
|                                                                          |
| MECHANISM    On the positive l1 boundary, the mass constraint forbids   |
|              cancellation.  Signs are fixed, so d generators give at   |
|              most 2^d subset sums, while the boundary has               |
|              binomial(n+r-1,r-1) points.                                |
| STATUS       G-1 CLOSED.  This is elementary and independent of RH.     |
+--------------------------------------------------------------------------+
```

## 1. Setting

Use exactly the Connes--Consani dimension recalled in `107_146`.  Put

\[
 I_r(n)=\{v\in\mathbb Z^r:\|v\|_1\le n\}.
\]

A finite set `F` linearly generates `I_r(n)` if every `v` has a
representation

\[
 v=\sum_{f\in F}\alpha_f f,\qquad \alpha_f\in\{-1,0,1\},\qquad
 \sum_{f\in F}|\alpha_f|\,\|f\|_1\le n.                 \tag{1.1}
\]

Let `dim_r(n)` be the minimum cardinality of such an `F`.

The previously proved coordinate-binary construction gives

\[
 \dim_r(n)\le r\lceil\log_2(n+1)\rceil.                 \tag{1.2}
\]

The missing part was a lower bound with the same leading constant when both
`r` and `log n` grow linearly.

## 2. Positive-orthant boundary theorem

### Theorem 2.1

For every `r>=2` and `n>=1`,

\[
 \boxed{\quad
 \dim_r(n)\ge
 \left\lceil\log_2 {n+r-1\choose r-1}\right\rceil .
 \quad}                                                   \tag{2.1}
\]

### Proof

Let `F` be a generating family and consider

\[
 S^+_{r,n}=\{v\in\mathbb Z_{\ge0}^r:v_1+\cdots+v_r=n\}.
\]

Stars and bars gives

\[
 |S^+_{r,n}|={n+r-1\choose r-1}.                         \tag{2.2}
\]

Fix `v` in this set and a representation (1.1).  Write
`w_f=alpha_f f` for its nonzero summands.  Since `||v||_1=n`,

\[
 n=\left\|\sum_f w_f\right\|_1
 \le\sum_f\|w_f\|_1\le n.
\]

Both inequalities are equalities.  Equality in the `l1` triangle inequality
is coordinatewise, so the summands have one weak sign in every coordinate.
Their sum is nonnegative.  If a coordinate of `v` is positive, that common
sign must be positive; if it is zero, every summand vanishes in that
coordinate.  Hence

\[
 w_f\in\mathbb Z_{\ge0}^r\quad\hbox{for every used }f.    \tag{2.3}
\]

For a fixed nonzero `f`, at most one of `f` and `-f` belongs to the positive
orthant.  Thus its allowable sign in (2.3) is determined by `f`, independently
of `v`.  Discarding the irrelevant zero generator, every `v` is consequently
the sum of a subset of one fixed oriented subfamily of `F`.

Different `v` require different subsets because a subset has a unique sum.
There are at most `2^|F|` subsets, whence

\[
 {n+r-1\choose r-1}\le2^{|F|}.
\]

Taking base-two logarithms, ceilings, and then the minimum over `F` proves
(2.1).  QED.

### Remark 2.2

This strengthens the one-dimensional-segment lower bound in `107_146` from
`log_2(n+1)` to the entropy of the entire positive boundary.  It also explains
why the global `3^d` counting bound is not sharp: on a saturated orthant the
alphabet `{0,+1,-1}` collapses to `{0,1}`.

## 3. Coupled-rank asymptotic

### Theorem 3.1 (exact G-1 constant)

Fix `k,a>0`, with `k` integral, and put

\[
 r_m=mk+1,\qquad n_m=\lfloor e^{ma}\rfloor.
\]

Then

\[
 \boxed{\quad
 \lim_{m\to\infty}
 \frac{\dim_{r_m}(n_m)}{ka m^2}=\frac1{\log2}.
 \quad}                                                   \tag{3.1}
\]

### Proof

Theorem 2.1 gives

\[
 \dim_{r_m}(n_m)\ge
 \frac1{\log2}\log {n_m+mk\choose mk}.                  \tag{3.2}
\]

Since `mk=o(n_m)`, the elementary product expansion of the binomial
coefficient gives

\[
 \log {n_m+mk\choose mk}
 =mk\log n_m-\log((mk)!)+O(m^2/n_m).
\]

Stirling's formula and `log n_m=ma+o(1)` therefore yield

\[
 \log {n_m+mk\choose mk}
 =ka m^2-km\log m+O(m).                                  \tag{3.3}
\]

On the other hand, the coordinate-binary construction (1.2) gives

\[
 \dim_{r_m}(n_m)
 \le(mk+1)\lceil\log_2(n_m+1)\rceil
 =\frac{ka}{\log2}m^2+O(m).                              \tag{3.4}
\]

Divide (3.2)--(3.4) by `ka m^2` and squeeze.  QED.

## 4. Consequences for phase 114

1. Gap G-1 is closed with exact constant `1/log 2`.
2. The binary constant predicted in `107_146` is correct in the coupled
   surface regime, without proving its stronger finite-rank conjecture
   `dim_2(n)=2 ceil(log_2(n+1))`.
3. G-1 remains independent of the toric theta gauge: both have quadratic
   growth, but their normalisations are different invariants.
4. No zero of `xi`, Weil form, Li coefficient, or RH-equivalent positivity is
   used anywhere in the proof.

## 5. Verification

`114_a_11_g1_binary_constant_verify.py` checks the boundary cardinality by
enumeration, the exact lower/upper squeeze numerically, and convergence to
`1/log 2`.  These checks support the finite identities; the proof above
establishes the general theorem.

