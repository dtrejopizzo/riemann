# D.157 — Hierarchical directed Schur certificate

## Verdict

The (168\times168) graph lower matrix of D.155 does not need uniform
(10^{-12})-scale entry radii.  Its spectrum has only five delicate
directions; the sixth selected value is (5.7448\times10^{-2}).  A second,
finite Schur complement separates these obligations:

* enclose the five-dimensional dangerous block at high precision;
* enclose its coupling to the safe block at medium precision;
* certify the 163-dimensional safe block with a coarse positive gap.

This is an exact congruence, not an eigenvalue extrapolation.  It reduces the
expensive singular-kernel integrations of D.156 to five distinguished linear
combinations; the remaining combinations only need enough accuracy to
preserve a gap of order (10^{-2}).

No paper file is modified.

## 1. Two-level Schur theorem

Let the directed graph lower form from D.154 be represented, after an
invertible frozen coordinate change, by

\[
 L=\begin{pmatrix}L_{dd}&L_{ds}\\L_{sd}&L_{ss}\end{pmatrix},
 \qquad \dim L_{dd}=r.                                 \tag{1.1}
\]

If interval arithmetic proves

\[
 L_{ss}\ge\eta I,
 \qquad
 L_{dd}-L_{ds}L_{ss}^{-1}L_{sd}\ge0,                  \tag{1.2}
\]

then (L\ge0), hence the complete primitive operator is nonnegative.
Indeed,

\[
\begin{pmatrix}I&-L_{ds}L_{ss}^{-1}\\0&I\end{pmatrix}
L
\begin{pmatrix}I&0\\-L_{ss}^{-1}L_{sd}&I\end{pmatrix}
=
\begin{pmatrix}
L_{dd}-L_{ds}L_{ss}^{-1}L_{sd}&0\\0&L_{ss}
\end{pmatrix}.                                        \tag{1.3}
\]

All matrices in (1.3) are finite.  The first Feshbach step has already
handled the infinite complement.

## 2. Perturbative radius budget

Suppose a midpoint selector diagonalizes the centre and puts the first
(r=5) directions in the dangerous block.  If the exact safe block differs
from its centre by operator norm at most (\varepsilon_s<\eta_0), where
the centre has lower edge (\eta_0), then

\[
 L_{ss}^{-1}\le(\eta_0-\varepsilon_s)^{-1}I.           \tag{2.1}
\]

If (\|L_{ds}\|\le\varepsilon_c), the entire safe-block correction obeys

\[
 0\le L_{ds}L_{ss}^{-1}L_{sd}
 \le{\varepsilon_c^2\over\eta_0-\varepsilon_s}I.       \tag{2.2}
\]

At the rank-60 selection point,

\[
 \eta_0\simeq5.7448\times10^{-2}.                     \tag{2.3}
\]

Thus a coupling enclosure (\varepsilon_c<10^{-7}) contributes less than
(1.75\times10^{-13}).  Only the (5\times5) Schur block must resolve the
final (3.0\times10^{-12}) margin directly.  Safe-block entry radii can be
many orders of magnitude larger than the dangerous-block radii, provided
their directed operator-norm sum preserves (2.3).

## 3. Frozen, not spectral, coordinates

The coordinate change used in (1.1) is obtained once from the floating
selection audit and rounded to dyadic rationals.  In the proof it is simply
an explicit invertible matrix (U\).  No assertion that its columns are exact
eigenvectors is made.  Directed arithmetic forms

\[
 U^*LU                                                   \tag{3.1}
\]

and checks (1.2).  Therefore rounding the selector cannot invalidate the
certificate; it can only enlarge the off-diagonal intervals and make the
test fail.

## 4. Integration schedule

The data of D.156 should be accumulated after applying the frozen columns
of (U):

1. five dangerous combinations with high-precision tanh--sinh balls;
2. dangerous--safe cross Grams to an operator-norm radius below (10^{-7});
3. the safe block with row-sum radii below a fixed fraction of (2.3);
4. the exact interval solves in D.155 and the final (5\times5) Schur test.

This mixed-precision schedule is mathematically equivalent to a uniform
168-dimensional enclosure but substantially cheaper.

`114_d_157_hierarchical_schur_verify.py` checks (1.3) and the radius bound
(2.2) on a nontrivial example.
