# 107.25 -- Paper C, Part XIII: first polarization intersection identities on the candidate model

## 1. Purpose

`107_24` reduces the degree-zero audit A3 to finitely many visible
generator-vs-polarization intersections, but it still leaves open the
first concrete geometric question:

\[
 H_T^{(1)}\cdot H_T^{(1)}\neq 0\ ?
 \tag{1.1}
\]

The present note derives the first nonformal intersection identities on
the candidate model \(\mathcal X_T^{(1)}\) from the underlying
two-ruling geometry of the compactified square.  The point is not yet to
numerically compute every degree.  The point is to isolate:

1. the mandatory geometric contribution coming from the corner
   \(C_\infty\);
2. the possible correction terms created by the regularizing blow-ups;
3. the minimal hypothesis under which one gets the desired nonvanishing
   of \(H_T^{(1)}\cdot H_T^{(1)}\).

This is the first genuinely geometric step beyond the formal reduction
of `107_24`.

## 2. Inputs

This note uses five previous components.

1. `107_15` gives the candidate model \(\mathcal X_T^{(1)}\) as a
   regularized closure in the compactified square.
2. `107_16` gives the two ruling boundary divisors \(B_{\rm v}\),
   \(B_{\rm h}\), and the common corner \(C_\infty=B_{\rm v}\cap B_{\rm h}\).
3. `107_17` gives local corner charts with normal-crossings parameters.
4. `107_22` and `107_24` fix the candidate polarization
   \(H_T^{(1)}=F_{{\rm v},T}^{(1)}+F_{{\rm h},T}^{(1)}\).
5. `107_23` isolates the same corner as the only remaining nontrivial
   singular receiver for the adelic metric.

## 3. Ambient intersection skeleton before regularization

Before normalization and blow-up, the compactified square
\(\overline{\mathfrak S}\) already dictates the basic incidence pattern.

### Definition 3.1: ambient ruling divisors

Let

\[
 B_{\rm v},\qquad B_{\rm h}\subset\overline{\mathfrak S}
 \tag{3.1}
\]

be the vertical and horizontal boundary divisors of `107_16`, and let

\[
 C_\infty:=B_{\rm v}\cap B_{\rm h}
 \tag{3.2}
\]

be their common corner.

### Proposition 3.2: ambient rulings meet through the corner

The only geometrically forced ambient mixed intersection between the two
ruling divisors is the corner cycle \(C_\infty\).

Proof.  `107_16` defines \(B_{\rm v}\) and \(B_{\rm h}\) as the two
distinct ruling boundary families and identifies their common
intersection exactly with the codimension-two corner \(C_\infty\).
\(\square\)

### Proposition 3.3: ambient self-intersections carry no generic mixed corner contribution

The divisors \(B_{\rm v}\) and \(B_{\rm h}\) do not acquire a new mixed
corner contribution from intersecting with themselves; any such term can
only arise through later exceptional corrections.

Proof.  In the ambient square, the corner is defined by the simultaneous
presence of the two distinct boundary equations, one from each factor.
A single ruling divisor does not generically meet itself through that
codimension-two corner.  Thus the corner contributes naturally to the
mixed product \(B_{\rm v}\cdot B_{\rm h}\), not to the self-products.
\(\square\)

This is the ambient intersection skeleton that later descends to the
candidate surface.

## 4. Transfer to the regularized model

The candidate model \(\mathcal X_T^{(1)}\) is produced by normalization
and blow-ups supported over special strata.  Therefore one must separate
the corner contribution from the exceptional corrections.

### Definition 4.1: strict-transform ruling classes

Let

\[
 F_{{\rm v},T}^{(1)},\qquad F_{{\rm h},T}^{(1)}
 \tag{4.1}
\]

be the strict transforms on \(\mathcal X_T^{(1)}\) of the ambient ruling
divisors \(B_{\rm v}\), \(B_{\rm h}\).

### Definition 4.2: exceptional correction symbols

Write

\[
 \varepsilon_{\rm vv}(T),\qquad
 \varepsilon_{\rm hh}(T),\qquad
 \varepsilon_{\rm vh}(T)
 \tag{4.2}
\]

for the correction terms introduced in the self- and mixed intersections
of the strict transforms by the normalization/blow-up process.

These are bookkeeping symbols for the unresolved regularization
contribution; they are not assumed to vanish identically a priori.

### Proposition 4.3: intersection decomposition on \(\mathcal X_T^{(1)}\)

On the candidate model, the first ruling intersections decompose as

\[
 F_{{\rm v},T}^{(1)}\cdot F_{{\rm v},T}^{(1)}
 =
 \varepsilon_{\rm vv}(T),
 \tag{4.3}
\]

\[
 F_{{\rm h},T}^{(1)}\cdot F_{{\rm h},T}^{(1)}
 =
 \varepsilon_{\rm hh}(T),
 \tag{4.4}
\]

\[
 F_{{\rm v},T}^{(1)}\cdot F_{{\rm h},T}^{(1)}
 =
 c_T+\varepsilon_{\rm vh}(T),
 \tag{4.5}
\]

where \(c_T\) is the contribution of the strict transform of the corner
cycle \(C_\infty\).

Proof.  Proposition 3.2 identifies the ambient mixed intersection
receiver as \(C_\infty\), while Proposition 3.3 shows that the ambient
self-intersection sector has no analogous generic corner term.  Passing
to the regularized model can therefore only add correction terms coming
from the exceptional locus, yielding the decomposition above.
\(\square\)

This is the precise separation needed for the degree-zero audit.

## 5. The polarization self-intersection

Recall from `107_24` that

\[
 H_T^{(1)}
 =
 F_{{\rm v},T}^{(1)}+F_{{\rm h},T}^{(1)}.
 \tag{5.1}
\]

### Theorem 5.1: first polarization intersection identity

The polarization self-intersection decomposes as

\[
 H_T^{(1)}\cdot H_T^{(1)}
 =
 2c_T
 +\varepsilon_{\rm vv}(T)
 +\varepsilon_{\rm hh}(T)
 +2\varepsilon_{\rm vh}(T).
 \tag{5.2}
\]

Proof.  Expand \((F_{{\rm v},T}^{(1)}+F_{{\rm h},T}^{(1)})^2\) and use
the decomposition of Proposition 4.3.  \(\square\)

This is the first concrete formula for the denominator \(h_T\) of
`107_24`.

### Corollary 5.2: minimal nonvanishing criterion for \(h_T\)

If the exceptional correction satisfies

\[
 \varepsilon_{\rm vv}(T)
 +\varepsilon_{\rm hh}(T)
 +2\varepsilon_{\rm vh}(T)
 \neq
 -2c_T,
 \tag{5.3}
\]

then

\[
 h_T=H_T^{(1)}\cdot H_T^{(1)}\neq 0.
 \tag{5.4}
\]

Proof.  Immediate from Theorem 5.1.  \(\square\)

### Corollary 5.3: minimal-regularization case

If the chosen regularization is corner-preserving and introduces no net
correction to the ruling intersections, namely

\[
 \varepsilon_{\rm vv}(T)
 =
 \varepsilon_{\rm hh}(T)
 =
 \varepsilon_{\rm vh}(T)
 =
 0,
 \tag{5.5}
\]

then

\[
 h_T=2c_T.
 \tag{5.6}
\]

In particular, if \(c_T\neq0\), then \(h_T\neq0\).

This gives the first candid route from the square geometry to the
primitive degree-zero denominator.

## 6. Why \(c_T\) is expected to be nonzero

The corner term is not an arbitrary symbol: it is the codimension-two
receiver already singled out repeatedly in Part III.

### Proposition 6.1: the corner contribution is load-bearing across the whole Part III package

The cycle \(C_\infty\) is simultaneously the receiver for:

1. the mixed ruling boundary intersection of `107_16`;
2. the diagonal boundary closure of `107_16`;
3. the Gamma--polar metric descent of `107_16` and `107_23`;
4. the common visible boundary support of graph closures from `107_15`.

Proof.  Each of these roles is stated explicitly in `107_15`, `107_16`,
and `107_23`.  Therefore setting \(c_T=0\) would collapse the very
corner geometry that all later completions use.  \(\square\)

### Consequence 6.2: \(c_T=0\) is a genuine failure mode, not a neutral option

If the eventual construction forced \(c_T=0\), then the candidate
surface would fail not only the degree-zero normalization route, but
also the intended common boundary receiver for the Gamma--polar
completion.

So the nonvanishing of \(c_T\) is part of the real geometric audit.

## 7. First degrees against the polarization

The same decomposition idea gives the first structure of the visible
degrees introduced in `107_24`.

### Definition 7.1: corner degrees of diagonal and graph closures

Write

\[
 \delta_T:=\Delta_T^{(1)}\cdot C_\infty^{(1)},
 \qquad
 \gamma_{p,k}(T):=\Gamma_{p,k,T}^{(1)}\cdot C_\infty^{(1)},
 \tag{7.1}
\]

where \(C_\infty^{(1)}\) is the strict transform of the corner receiver
on \(\mathcal X_T^{(1)}\).

### Proposition 7.2: first degree skeleton for the diagonal

The diagonal degree admits a decomposition

\[
 d_\Delta(T)
 =
 2\delta_T+\varepsilon_\Delta(T),
 \tag{7.2}
\]

where \(\varepsilon_\Delta(T)\) records only exceptional corrections
from the regularization.

Proof.  The diagonal meets both ruling directions symmetrically, and in
the compactified square both meetings are funneled through the same
corner/diagonal receiver.  The only extra contribution comes from the
exceptional loci introduced while regularizing those incidences.
\(\square\)

### Proposition 7.3: first degree skeleton for prime-power graphs

For every visible \((p,k)\in S_T\),

\[
 d_{p,k}(T)
 =
 2\gamma_{p,k}(T)+\varepsilon_{p,k}(T),
 \tag{7.3}
\]

where \(\varepsilon_{p,k}(T)\) is the exceptional correction attached to
the regularization of the graph/ruling incidences.

Proof.  `107_16` states that each compactified graph closure meets the
same corner receiver \(C_\infty\).  Since the polarization is the sum of
the two ruling directions, the graph degree is the sum of its two ruling
intersections, both funneled through the same corner receiver up to
regularization corrections.  \(\square\)

These are not final numerical formulas, but they are the first concrete
geometric expressions for the degree data of `107_24`.

## 8. What the degree-zero audit now needs

Combining `107_24` with the present note, A3 is reduced further.

### Checklist 8.1: remaining concrete A3 inputs

To fully discharge the degree-zero audit, it now remains to prove:

1. \(c_T\neq0\);
2. the exceptional correction pattern
   \(\varepsilon_{\rm vv}(T),\varepsilon_{\rm hh}(T),
   \varepsilon_{\rm vh}(T)\);
3. the corner multiplicities \(\delta_T,\gamma_{p,k}(T)\);
4. the diagonal and graph correction terms
   \(\varepsilon_\Delta(T),\varepsilon_{p,k}(T)\).

That is a much tighter finite list than before.

### Proposition 8.2: the first indispensable denominator is now geometrically localized

The only new ingredient needed to make the primitive correction of
`107_24` concrete is the nonvanishing of the corner-driven denominator
\(h_T\).

Proof.  `107_24` already reduces degree zero to visible intersections
once \(h_T\neq0\).  Theorem 5.1 localizes \(h_T\) to the corner
contribution and its exceptional corrections.  \(\square\)

## 9. What is now closed

This note closes the next gap after `107_24`.

1. the polarization self-intersection now has a concrete geometric
   decomposition;
2. the nonvanishing of \(h_T\) is reduced to a corner contribution plus
   explicit regularization corrections;
3. the diagonal and graph degrees now have first geometric skeleton
   formulas against the polarization;
4. the remaining A3 work is no longer abstract and has a finite list of
   concrete geometric quantities to determine.

## 10. What remains open

This note still does not prove the full degree-zero audit.

1. It does not yet compute \(c_T,\delta_T,\gamma_{p,k}(T)\) numerically.
2. It does not yet prove the exceptional corrections vanish or have the
   required sign.
3. It does not prove the realized metrized Picard class exactly matches
   the divisor-level skeleton.
4. It does not prove the exact-kernel identity of `107_11`.
5. It does not prove the terminal identity of `107_13`.

## 11. Next technical front

The next proof-bearing move is now to analyze the regularization
exceptional loci themselves and show that, for the chosen blow-up
protocol of `107_15`, the corner contribution survives with the needed
nonzero coefficient and the ruling correction terms are controlled.
