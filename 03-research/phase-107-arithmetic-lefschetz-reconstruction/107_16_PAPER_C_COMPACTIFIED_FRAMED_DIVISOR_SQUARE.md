# 107.16 -- Paper C, Part IV: a compactified framed-divisor square and boundary metric protocol

## 1. Purpose

This note refines the candidate construction of `107_15` by specifying a
first compactification candidate

\[
 \overline{\mathfrak S}
 \supset
 \mathfrak S
 =
 \widetilde{\mathrm{Pic}}_{\rm fr}\times
 \widetilde{\mathrm{Pic}}_{\rm fr}
 \tag{1.1}
\]

and by describing the boundary geometry on which the Gamma--polar metric
should descend.

The point is not to claim a finished compactification theorem.  The
point is to replace the placeholder phrase "choose a compactification"
from `107_15` with a concrete protocol that respects the actual source
data:

1. framed arithmetic divisors \((L,\xi,\tau)\);
2. the two ruling directions;
3. the common archimedean phase boundary;
4. the need for a diagonal and a codimension-two corner.

## 2. Input from Connes--Consani

The Phase 39 source inventory isolates the following verified facts.

1. The Riemann sector is identified with a monoid of framed arithmetic
   divisors \((L,\xi,\tau)\).
2. The framing data \(\xi\) records the finite arithmetic part.
3. The seminorm \(\tau\) on \(L\otimes\mathbb R\) is allowed to
   degenerate.
4. Boundary and singular phenomena are not bugs but part of the intended
   geometry.

This means that the most natural compactification datum is not an added
point at infinity in the classical projective sense.  It is the locus
where the archimedean seminorm becomes degenerate while the framed
finite part remains meaningful.

## 3. Boundary parameters

### Definition 3.1: archimedean size coordinate

For a framed arithmetic divisor \(x=(L,\xi,\tau)\), write

\[
 r(x)\in[0,+\infty]
 \tag{3.1}
\]

for the scale parameter of the archimedean seminorm \(\tau\), normalized
so that:

1. \(r(x)\in(0,\infty)\) on the interior Riemann sector;
2. \(r(x)=0\) corresponds to collapse of the archimedean seminorm;
3. \(r(x)=+\infty\) corresponds to the opposite scaling boundary.

The exact normalization is not yet theorematically fixed, but the two
extremal regimes are determined by the source moduli description.

### Definition 3.2: phase coordinate

Retain the common phase variable

\[
 \theta\in\mathbb S^1
 \tag{3.2}
\]

already isolated in `107_08` and `106.169`.

The compactification must remember \(\theta\) at the boundary, because
that is where the prime towers glue and where the Gamma--polar page
lives.

## 4. Compactified one-factor framed-divisor space

### Definition 4.1: compactified framed-divisor factor

Define the first compactified factor

\[
 \overline{\mathfrak P}_{\rm fr}
 \tag{4.1}
\]

to be the framed-divisor moduli enlarged by allowing the boundary values
\(r=0\) and \(r=\infty\), with the phase variable retained at those
limits.

Informally:

\[
 \overline{\mathfrak P}_{\rm fr}
 =
 \widetilde{\mathrm{Pic}}_{\rm fr}
 \sqcup
 \partial_0\widetilde{\mathrm{Pic}}_{\rm fr}
 \sqcup
 \partial_\infty\widetilde{\mathrm{Pic}}_{\rm fr},
 \tag{4.2}
\]

where each boundary component still carries the phase coordinate and the
finite framing data.

This is the minimum enlargement compatible with the source statement
that degenerating seminorms are intrinsic to the monoid geometry.

## 5. The compactified square

### Definition 5.1: compactified framed-divisor square

Set

\[
 \overline{\mathfrak S}
 :=
 \overline{\mathfrak P}_{\rm fr}\times
 \overline{\mathfrak P}_{\rm fr}.
 \tag{5.1}
\]

Its boundary decomposes into four primary divisors:

\[
 B_{{\rm v},0},\ B_{{\rm v},\infty},\ 
 B_{{\rm h},0},\ B_{{\rm h},\infty},
 \tag{5.2}
\]

according to which factor hits which archimedean scale boundary.

For the Phase 107 realization, the load-bearing pair is the common
middle boundary obtained by identifying the two scale extremes through
the scaling action, leaving one vertical and one horizontal boundary
family:

\[
 B_{\rm v},\qquad B_{\rm h}.
 \tag{5.3}
\]

The codimension-two corner

\[
 C_\infty:=B_{\rm v}\cap B_{\rm h}
 \tag{5.4}
\]

is the first candidate for the common phase/Gamma corner.

## 6. Why the corner matters

### Proposition 6.1: the common phase boundary is necessarily a corner phenomenon

The Gamma--polar page cannot live on only one boundary divisor of
\(\overline{\mathfrak S}\); it must be attached to the common corner
\(C_\infty\).

Proof.  The source geometry distinguishes the vertical and horizontal
rulings, so neither boundary divisor may be collapsed into the other.
At the same time, `107_08` shows that the prime towers are glued through
one common phase boundary.  Therefore the boundary page carrying the
joint prime/Gamma/polar interaction must be where the two ruling
boundaries meet, namely at a codimension-two corner.  \(\square\)

This is the square-level analogue of the common phase circle in the
flow picture.

## 7. Diagonal extension

### Definition 7.1: compactified diagonal

Let

\[
 \overline{\Delta}_{\rm fr}\subset\overline{\mathfrak S}
 \tag{7.1}
\]

be the closure of the interior diagonal.

The compactified diagonal meets the corner \(C_\infty\) along the locus
where both framed divisors have the same finite data and the same phase,
while their archimedean scale degenerates simultaneously.

This is the exact place where the diagonal self-intersection must absorb
the Gamma--polar correction in any later regularized model.

## 8. Closure of finite-support graphs

The graphs \(\Gamma_n^{\rm fr}\) from `107_15` must also extend to the
boundary.

### Definition 8.1: compactified graph closure

For \(n\in N_T\), let

\[
 \overline{\Gamma}_n^{\rm fr}
 \subset
 \overline{\mathfrak S}
 \tag{8.1}
\]

be the closure of \(\Gamma_n^{\rm fr}\).

Because multiplication by \(n\) scales the finite framing data but
preserves the common phase variable, the boundary part of
\(\overline{\Gamma}_n^{\rm fr}\) meets the same corner \(C_\infty\).

This gives a common boundary receiver for:

1. the diagonal;
2. the prime-power graphs;
3. the eventual archimedean divisor \(Z_\infty\).

That is exactly the structural convergence demanded by `107_05` and
`107_09`.

## 9. Boundary metric protocol

The compactification is only useful if one can say what metric data
should live on its boundary.

### Definition 9.1: boundary metric line

Let \(\mathcal L_\infty\) denote the line bundle on a neighborhood of
the corner \(C_\infty\) generated by the normal crossing pair
\((B_{\rm v},B_{\rm h})\) and the compactified diagonal
\(\overline{\Delta}_{\rm fr}\).

The Gamma--polar metric protocol is:

1. equip \(\mathcal L_\infty\) with the relative determinant norm
   already fixed in `107_05` and `106.195`;
2. require that its logarithmic variation along the compactified
   diagonal reproduce the Gamma--polar distribution;
3. require that its restriction away from the diagonal agree with the
   off-diagonal finite determinant lines after gluing.

This does not yet prove existence of a smooth or adelic metric.  It does
identify the precise line on which such a metric must be placed.

### Proposition 9.1: one boundary metric, not three unrelated corrections

The Phase 107 boundary metric must be assigned once on
\(\mathcal L_\infty\), not separately on prime, Gamma, and polar sectors.

Proof.  `107_05` already closed the diagonal and off-diagonal pairings by
one metrized determinant theory, while `107_09` derives the
prime--Gamma--polar Lefschetz side from one joint fixed-point
calculation.  Splitting the boundary metric into independent corrections
would destroy exactly that coherence.  \(\square\)

## 10. Regularization protocol for \(\mathcal X_T^{(1)}\)

With \(\overline{\mathfrak S}\) fixed, the regularization protocol of
`107_15` becomes more precise.

### Protocol 10.1

To build \(\mathcal X_T^{(1)}\):

1. take the closure of
   \[
    \mathfrak U_T=
    \overline{\Delta}_{\rm fr}
    \cup
    \bigcup_{n\in N_T}\overline{\Gamma}_n^{\rm fr}
    \cup
    B_{\rm v}\cup B_{\rm h}
   \]
   inside \(\overline{\mathfrak S}\);
2. normalize;
3. blow up the loci where:
   the compactified diagonal meets the corner nontransversely,
   different \(\overline{\Gamma}_n^{\rm fr}\) meet each other or the
   corner with excess tangency,
   and the ruling boundaries fail to be normal crossings;
4. pull back the boundary metric line \(\mathcal L_\infty\) to the
   regularized model.

The resulting regularized object is the sharpened version of the
candidate \(\mathcal X_T^{(1)}\).

## 11. New concrete checks enabled by this compactification

The compactified square reduces the next tasks to explicit checks.

1. Verify that the corner \(C_\infty\) is nonempty and phase-carrying.
2. Verify that the closures \(\overline{\Gamma}_n^{\rm fr}\) meet
   \(C_\infty\) in a way compatible with the return lengths \(k\log p\).
3. Verify that the pullback of \(\mathcal L_\infty\) can be interpreted
   as a Green metric on the regularized model.
4. Verify that the degree-one classes remain visible after blowing up.

These are now model-specific questions rather than abstract desiderata.

## 12. Status

The current Phase 107 state is now stronger than in `107_15`.

1. `107_15` proposed a first candidate \(\mathcal X_T^{(1)}\) from a
   compactified framed-divisor square.
2. The present note identifies a first explicit compactification
   candidate \(\overline{\mathfrak S}\), its ruling boundaries, its
   common corner \(C_\infty\), and the line \(\mathcal L_\infty\) on
   which the Gamma--polar metric should descend.
3. The compactification and metric descent problems of Part III are now
   reduced to concrete boundary/corner checks.

What remains open is still substantial:
actual construction of \(\overline{\mathfrak P}_{\rm fr}\),
proof that the graph closures are finite type,
existence of the regularization with the desired comparison properties,
and proof that the pulled-back boundary metric is admissible in the
sense required by Part IV.
