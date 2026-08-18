# 114.a.128 — H7 correction: finite principalization leaves an archimedean boundary defect

```
+------------------------------------------------------------------------+
| CANDIDATE   h_p=p_2/p_1 cancels the finite local multipliers.           |
| FINITE      On finite overlaps the remaining factors are O-units.       |
| INFINITY    In Haran's real unit ball, 1/p is bounded but not a unit;    |
|             its inverse p is not integral.                              |
| VERDICT     h_p does not trivialize the completed anti-lattice.          |
| REDUCTION   Anti-diagonal faithfulness is entirely an archimedean        |
|             boundary/metric problem.                                    |
+------------------------------------------------------------------------+
```

## 1. The tempting finite-chart calculation

Fix a prime `p`.  On the repaired square `Y^reg`, both ruling scalars are
regular in the Section-11 sense, so the global fraction

\[
 h_p=\frac{p_2}{p_1}\in GL_1(\mathcal K(Y^{\rm reg}))                 \tag{1.1}
\]

exists.  At finite places, represent the inverse-uniformizer lattice `L_p`
by multiplier `p^{-1}` at `p` and `1` away from `p`.  For

\[
 \mathcal A_p=\mathcal L_{p,1}\otimes\mathcal L_{p,2}^{-1},            \tag{1.2}
\]

the formal four-chart quotients after division by (1.1) are

\[
\begin{array}{c|c|c}
\text{finite chart type}&f_1/f_2&(f_1/f_2)/h_p\\ \hline
p\times p       &p_2/p_1&1\\
p\times({\ne}p) &1/p_1&1/p_2\\
({\ne}p)\times p&p_2&p_1\\
({\ne}p)\times({\ne}p)&1&p_1/p_2.
\end{array}                                                            \tag{1.3}
\]

At a finite place different from `p`, both `p` and `1/p` are local units.
Thus (1.3) really does cancel every purely finite valuation.

## 2. Why the calculation does not extend over infinity

The complement of the finite point `p` is not a chart on which `p` is an
arithmetic unit.  Haran's real local object is the Euclidean unit ball
`Z_R`; on scalar coordinates its integral elements satisfy `|x|<=1`, and

\[
 GL_1(\mathbb Z_{\mathbb R})=\{x:|x|=|x^{-1}|=1\}=\{\pm1\}.            \tag{2.1}
\]

For every prime `p`, `1/p` lies in the scalar unit ball but is **not** a
unit of it, because its inverse `p` has norm greater than one.  Conversely,
`p` is not an integral scalar on that chart.  Therefore the mixed entries
`1/p_2` and `p_1` in the last column of (1.3) are not `O`-units when the
corresponding away-factor is the real boundary.

Haran's equivalence (11.4) requires actual local `GL_1(O)` elements, not
merely elements of `O` or units of the fraction object.  Hence (1.3) is not
a completed-bundle trivialization.

### Theorem 2.1 (failure of naive principalization)

The global fraction `p_2/p_1` cancels the finite part of
`L_(p,1)L_(p,2)^(-1)` but does not trivialize it in Haran's completed Picard
category.  The purported proof that the full anti-diagonal is principal is
false because it treats bounded nonunits at infinity as local units.

This is the square analogue of the familiar curve fact that the finite
prime idele `p^{-1}` has degree `log p` although the rational number `p`
exists: the product formula supplies a compensating archimedean component.

## 3. Exact residual boundary class

Let `B_p^infty` denote the residual completed transition datum obtained from
`A_p` after the finite cancellation by `h_p`.  It is represented trivially
at all finite valuation charts and by the nonunit norm ratios on the mixed
real-boundary charts.  In the generically trivialized divisor object,

\[
 \mathcal A_p=\mathrm{div}(h_p)+B_p^\infty,                     \tag{3.1}
\]

where (3.1) is a decomposition of local fraction data, not an assertion
that either summand vanishes.  Passing to completed Picard kills the global
principal term and gives

\[
 [\mathcal A_p]=[B_p^\infty].                                        \tag{3.2}
\]

For a finite family `a=(a_p)`, the possible anti-relation is therefore
equivalent to

\[
 \sum_p a_p[B_p^\infty]=0.                                           \tag{3.3}
\]

### Corollary 3.1 (archimedean boundary reduction)

The prime anti-diagonal is faithful if and only if the boundary classes
`[B_p^infty]` are integrally independent.  All finite valuations are blind
to this question; the missing detector must be an archimedean norm/Green
boundary functor.

Call this exact remaining statement **H7-ARCH-BDRY**.  Proving it would
establish the prime-sector H7-RULING-PF and unlock the descent criteria of
`a116`, `a121`, `a123` and `a124`.  Refuting it would exhibit an actual
anti-diagonal relation.  Neither conclusion is asserted here.

## 4. Scope correction

The presentation-lattice RR form, all-ray section asymptotic, numerical
Green matrix and metrized biextension remain valid.  Their descent to
ordinary completed Picard remains open, now localized precisely at
H7-ARCH-BDRY.  Row A and RH remain open.

## 5. Verification scope

`114_a_128_h7_antidiagonal_principal_verify.py` checks the finite exponent
cancellation and the real-unit obstruction for every sampled prime, plus
the Section-11 and real-ball source anchors.  The theorem is the distinction
between membership in `O`, invertibility in `O`, and invertibility in `K`.
