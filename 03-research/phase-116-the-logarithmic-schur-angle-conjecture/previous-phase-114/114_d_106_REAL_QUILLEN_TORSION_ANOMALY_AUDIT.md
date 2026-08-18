# D.106 — Real Quillen torsion anomaly audit

## Status

The analytic torsion of the completed mapping cone is already the
determinant whose normal connection produces all prime powers and Gamma in
D.94.  This note tests whether its Real/equivariant anomaly supplies a
second term cancelling the anti-invariant Bochner defect of D.105.

It does not.  Quillen torsion is multiplicative under direct sums.  On a
free Real orbit its anomaly is the sum of two diagonal local anomalies and
reproduces the ordinary Poincare--Lelong divisor current.  Positive changes
of the two fibre metrics act by congruence on the Real swap form and
preserve its negative determinant.  The missing correction `I-J` is an
off-diagonal coupling between the reflected cohomology values; it is not a
torsion anomaly of the direct-sum cone.

Equivariant torsion with insertion of the swapping involution vanishes on a
free orbit and localizes on fixed orbits.  Replacing the Real character by
that fixed-point character deletes the off-line terms rather than proving
their positivity, and changes the A--B--C trace.

Finally, any nonconstant torsion correction capable of producing the
missing square changes the normal determinant connection and therefore
changes at least one `p^k` or Gamma coefficient.  An anomaly preserving the
complete row-C character has zero boundary derivative and cannot repair
the sign.

No RH statement or desired sign is assumed.  The paper is not modified.

## 1. Torsion of the local mapping cone

For an acyclic two-term Hermitian complex

\[
 0\longrightarrow L_0\xrightarrow{d}L_1\longrightarrow0, \tag{1.1}
\]

the finite-dimensional Ray--Singer/Quillen torsion is, up to the fixed
cohomological convention,

\[
 \log T(d)=\log|\det d|.                                  \tag{1.2}
\]

For the completed cone `d=Xi`, zeta regularization gives the same
determinant line used in D.94.  Its normal derivative is

\[
 \partial_\nu\log T(\Xi)
 =\text{all finite }p^k\text{ contacts}+	ext{Gamma}.      \tag{1.3}
\]

The curvature/anomaly is the Poincare--Lelong current

\[
 dd^c\log T(\Xi)
 =\sum_\rho m_\rho\delta_\rho                             \tag{1.4}
\]

with the convention-dependent global sign.  Thus torsion reproduces the
same divisor current as the Bochner superconnection; it is not a second
independent curvature.

## 2. Multiplicativity on a free Real orbit

Let `rho` and `rho^iota` be a free orbit.  Locally the Real cone is the
direct sum

\[
 \mathcal K_\rho\oplus\mathcal K_{\rho^\iota}.            \tag{2.1}
\]

Analytic torsion is multiplicative:

\[
 T(\mathcal K_\rho\oplus\mathcal K_{\rho^\iota})
 =T(\mathcal K_\rho)T(\mathcal K_{\rho^\iota}),           \tag{2.2}
\]

so its logarithmic anomaly is additive.  It changes the two ordinary fibre
norms separately and yields the positive form

\[
 Q_{\rm abs}=m_\rho(|a|^2+|b|^2).                        \tag{2.3}
\]

The exact Real trace remains

\[
 Q_{\mathbb R}=m_\rho(a\overline b+b\overline a),
 \qquad
 J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.                 \tag{2.4}
\]

The missing correction is

\[
 Q_{\rm abs}-Q_{\mathbb R}
 =m_\rho\langle(a,b),(I-J)(a,b)\rangle
 =m_\rho|a-b|^2.                                         \tag{2.5}
\]

The matrix `I-J` couples the two summands.  It cannot arise from the
additive anomaly in (2.2), which is diagonal before applying the Real
trace.

## 3. Metric anomaly preserves inertia

A change of Hermitian metrics on the two local cone fibres is represented
by an invertible positive matrix `H`.  The Real Gram changes by congruence,

\[
 J\longmapsto H^*JH.                                     \tag{3.1}
\]

Therefore

\[
 \det(H^*JH)=|\det H|^2\det J=-|\det H|^2<0.              \tag{3.2}
\]

No Quillen rescaling, Bott--Chern anomaly or positive torsion factor can
turn the free-orbit Real plane into a positive plane.  At most it changes
the relative magnitude of its positive and negative chiral directions.

To obtain `I` from `J` one must **add** the positive rank-one form `I-J`,
not congruently rescale `J`.  Such an addition changes the bilinear
character rather than its metric presentation.

## 4. Equivariant torsion deletes free orbits

Let `R` be the involution exchanging the two isomorphic cone fibres.  The
ordinary heat operator is diagonal on the orbit:

\[
 e^{-t\Delta}=\begin{pmatrix}K_t&0\\0&K_t\end{pmatrix},
 \qquad
 R=\begin{pmatrix}0&I\\I&0\end{pmatrix}.                  \tag{4.1}
\]

Hence

\[
 \operatorname{Tr}(R e^{-t\Delta})=0                     \tag{4.2}
\]

on every free orbit.  Equivariant analytic torsion therefore localizes on
the fixed locus of the involution.

This is a valid Lefschetz fixed-point character, but it is not the Real
pairing (2.4).  Replacing row C by (4.2) would simply omit every free orbit
from the spectral trace.  On the arithmetic side it would remove the
corresponding part of the completed normal connection.  It does not prove
that the omitted orbit is absent.

## 5. Character-preservation obstruction

Let `A` be an additional scalar torsion anomaly.  It changes the determinant
connection by

\[
 \nabla_\nu\log\|\lambda\|_Q^2
 \longmapsto
 \nabla_\nu\log\|\lambda\|_Q^2+\partial_\nu A.           \tag{5.1}
\]

The row-C coefficients are already termwise exact:

\[
 \partial_\nu\log\|\lambda\|_Q^2
 \rightsquigarrow
 \{\Lambda(p^k)/\sqrt{p^k}\}_{p,k}
 \quad\text{and}\quad m_0-\ell_\infty.                  \tag{5.2}
\]

To preserve every finite coefficient and the Gamma finite part, an
admissible anomaly must satisfy

\[
 \partial_\nu A=0                                        \tag{5.3}
\]

as a boundary distribution on the full A--B--C test category.  Such an
anomaly cannot contribute the nonzero quadratic defect (2.5).

Conversely, an anomaly engineered so that its source Hessian is
`m|a-b|^2` necessarily has nonzero boundary variation and changes the
character.  If it is defined orbit by orbit it also uses the nontrivial
divisor explicitly.

## 6. Compatibility with multiplication

The determinant/torsion functor is multiplicative for direct sums and
distinguished triangles.  This multiplicativity is what gives the
logarithmic Euler derivative and the correct prime-power idempotence after
D.94.  A cross-orbit correction `I-J` is not additive over the two cone
summands; it requires the Real involution as an extra correspondence.

Inserting that correspondence in the torsion trace gives the equivariant
trace (4.2), which kills rather than squares a free orbit.  Inserting the
positive projector `(I-R)/2` gives the defect (2.5), but adds a new
projector-dependent character not present in rows A--B--C.  Its choice is
equivalent to selecting the anti-invariant divisor subspace.

Thus there is no torsion correction which is simultaneously:

1. multiplicative and source-defined before the divisor;
2. exact for every `p^k` and Gamma;
3. trace-preserving for row C;
4. positive on every free Real orbit.

## 7. Outcome and periodic Hodge--Riemann gate

Quillen torsion closes no additional sign gap.  It gives the same normal
connection and the same divisor current already present in D.94--D.105.

The remaining geometric statement can be phrased as a periodic
Hodge--Riemann/fixed-point theorem.  One must construct on the nontrivial
periodic cohomology `V` a positive Hermitian form `H` such that:

\[
 \langle\rho(h)v,w\rangle_H
 =\langle v,\rho(h^\vee)w\rangle_H,                       \tag{7.1}
\]

the two Tate residues form the polar boundary, and the Lefschetz trace of
the A--B correspondences remains the row-C character.  Then the scaling
generator is skew-adjoint in central normalization, forcing its spectral
characters onto the fixed line and giving D.

Existence of `H` is not supplied by torsion.  On each free Real orbit it is
equivalent to replacing the hyperbolic trace by a positive `star`-metric,
which is impossible while retaining off-line scaling eigencharacters.
The next audit formulates this periodic polarization as a source-side
adjointness equation and tests whether the A-row Kunneth metric and B-row
torsor determine it uniquely or whether solvability is exactly the Weil
positivity condition.

