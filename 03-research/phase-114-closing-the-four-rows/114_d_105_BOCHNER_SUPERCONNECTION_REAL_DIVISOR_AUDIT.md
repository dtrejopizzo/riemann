# D.105 — Bochner superconnection and the Real divisor defect

## Status

The mapping cone of the completed Euler--Gamma determinant carries a
canonical Koszul/Dolbeault superconnection.  Its square is positive and its
Quillen boundary connection is the exact prime--Gamma form of D.94.  The
Bochner--Weitzenbock calculation, however, distinguishes two curvature
pairings.

The ordinary Hermitian divisor curvature is positive: on a free Real orbit
it gives the sum of two squares.  The Green form which pulls back to the
Weil form uses the functional-equation Real trace and gives the crossed
pairing.  Their exact difference is the square of the anti-invariant
component.  Equivalently, every free orbit decomposes into one positive and
one negative chirality.  A fixed orbit contributes only the positive line.

No canonical grading removes the negative chirality.  Unitary changes of
Clifford convention preserve inertia; restricting to the positive
chirality would impose equality of the two reflected test values and would
change the source test category.  Thus the Bochner identity is positive
for the ordinary divisor metric but has the wrong boundary character, or
is trace-exact for `B_nuc` but contains exactly the off-line hyperbolic
defect.

The zero-order term is source-defined by the mapping cone of `Xi`, but its
Real positivity is equivalent to localization of the divisor on the fixed
line.  Bochner curvature therefore restates rather than proves D.

No RH statement or zero localization is assumed.  The paper is not
modified.

## 1. The determinant mapping cone

Let `Xi` be the entire completed determinant section and consider its
two-term Koszul complex

\[
 \mathcal K_\Xi=[\mathcal O\xrightarrow{\Xi}\mathcal O].  \tag{1.1}
\]

On the smooth locus equip the two terms with the determinant metric of
D.94.  With exterior multiplication `epsilon` and contraction `iota`, the
standard Witten--Koszul superconnection is

\[
 \mathbb A_t
 =\bar\partial+\bar\partial^*
  +t(\Xi\,\epsilon+\overline\Xi\,\iota).                  \tag{1.2}
\]

It is odd and self-adjoint.  Hence

\[
 \mathbb A_t^2\ge0.                                      \tag{1.3}
\]

Expansion gives the Weitzenbock form

\[
 \mathbb A_t^2
 =\Delta_{\bar\partial}+t^2|\Xi|^2
  +t\,c(d\Xi,d\overline\Xi),                             \tag{1.4}
\]

where the last term is the Clifford Hessian/zero-order block.  The full
square is positive; the Clifford zero-order block is not separately
positive.  In the local model `Xi(z)=z`, it is the Pauli off-diagonal block
and has both chiral signs.

The cohomology of (1.1) is the divisor sheaf of `Xi`.  Poincare--Lelong
gives, with the standard normalization,

\[
 dd^c\log|\Xi|
 =\sum_\rho m_\rho\,\delta_\rho.                          \tag{1.5}
\]

Thus the ordinary Chern curvature is a positive divisor current.  This
statement uses the determinant section but no location theorem for its
zeros.

## 2. Boundary Green term

Apply Green's formula on a functional-equation half-domain with small
circles removed around the divisor.  The outer central boundary term is
the normal connection

\[
 -\nabla_\nu\log\|\lambda_{\rm comp}\|_Q^2,              \tag{2.1}
\]

whose pullback is `B_nuc` by D.94.  The two rational punctures give the
crossed Tate term.  The small divisor circles give the residue trace.
After passing to a test transform `F`, the exact identity is

\[
 \langle M(F),CM(F)\rangle-B_{\rm nuc}(F,F)
 =Q_{\rm div}^{\mathbb R}(F),                             \tag{2.2}
\]

where `Q_div^R` is the Real divisor pairing.  On primitive tests this is

\[
 -B_{\rm nuc}(F,F)=Q_{\rm div}^{\mathbb R}(F).            \tag{2.3}
\]

All prime powers and Gamma are present in the outer boundary connection;
all nontrivial spectral information is present in the inner divisor
residues.  Equation (2.2) is the Bochner/Green form of the explicit
formula.

## 3. Ordinary versus Real divisor curvature

Let `rho^iota=1-conj(rho)`.  For a fixed orbit `rho=rho^iota`, both the
ordinary and Real trace give

\[
 m_\rho|F(\rho)|^2.                                      \tag{3.1}
\]

For a free orbit put

\[
 a=F(\rho),\qquad b=F(\rho^\iota).                        \tag{3.2}
\]

The ordinary positive curvature gives

\[
 Q_{\rm abs}(a,b)=m_\rho(|a|^2+|b|^2),                   \tag{3.3}
\]

whereas the functional-equation Real trace gives

\[
 Q_{\mathbb R}(a,b)
 =m_\rho(a\overline b+b\overline a).                     \tag{3.4}
\]

They satisfy the exact defect identity

\[
 \boxed{
 Q_{\rm abs}(a,b)-Q_{\mathbb R}(a,b)
 =m_\rho|a-b|^2\ge0.}                                    \tag{3.5}
\]

Therefore ordinary Bochner positivity yields

\[
 Q_{\mathbb R}(a,b)
 =Q_{\rm abs}(a,b)-m_\rho|a-b|^2,                        \tag{3.6}
\]

not `Q_R>=0`.  The lost square is precisely the anti-invariant mismatch
between the two members of a free Real orbit.

## 4. Chirality and inertia

Use normalized chiral coordinates

\[
 a_+={a+b\over\sqrt2},\qquad
 a_-={a-b\over\sqrt2}.                                   \tag{4.1}
\]

Then

\[
 Q_{\rm abs}=m_\rho(|a_+|^2+|a_-|^2),
 \qquad
 Q_{\mathbb R}=m_\rho(|a_+|^2-|a_-|^2).                 \tag{4.2}
\]

Thus the superconnection grading diagonalizes the problem but does not
remove the negative chirality.  The free-orbit Gram has determinant
`-m_rho^2`; under any invertible change of Clifford frame `T`,

\[
 \det(T^*G_\rho T)=|\det T|^2\det G_\rho<0.               \tag{4.3}
\]

No unitary phase, chirality convention or metric rescaling can make it
positive.

Restricting to `a_-=0` would make (3.4) a square, but it imposes

\[
 F(\rho)=F(\rho^\iota)                                   \tag{4.4}
\]

for every free orbit.  The additive Fourier involution decomposes the
source into both parities and does not imply (4.4).  Discarding the odd
parity changes the primitive test space and the nuclear character.

## 5. Source positivity of the zero-order term

The positive object available before Real trace is the full square
`A_t^2` and its ordinary divisor curvature.  The zero-order Clifford term
in (1.4) has, at a simple zero, the local model

\[
 \begin{pmatrix}0&\overline{d\Xi}\\d\Xi&0\end{pmatrix},   \tag{5.1}
\]

with eigenvalues `plus-or-minus |d Xi|`.  Its supertrace localizes the
divisor, but it is not a positive potential.

Taking the ordinary trace replaces (5.1) by its squared norm and yields
(3.3).  Taking the Real supertrace retains the crossed orientation and
yields (3.4).  Hence there is no source-positive zero-order term with the
exact Real character unless every divisor orbit is fixed.

At the local Euler--Gamma level, before analytic continuation, the Chern
connection is flat off its local determinant zeros.  The global curvature
which remains after completion is exactly (1.5).  There is no additional
positive Ricci term hidden in the local factors.

## 6. Bochner identity in orbit form

After cancelling the contractible bulk range pair of D.102, the completed
Bochner identity can be organized as

\[
 \begin{aligned}
 \|\mathbb A_tu\|^2
 ={}&\|\nabla u\|^2+t^2\|\Xi u\|^2\\
 &+Q_{\rm abs}(u)
 +\mathcal B_{\rm outer}(u),                              \tag{6.1}
 \end{aligned}
\]

with a convention-dependent relocation of the positive divisor term
between the two sides.  Replacing ordinary curvature by the Real trace
changes

\[
 Q_{\rm abs}\longmapsto Q_{\mathbb R}
 =Q_{\rm abs}-\sum_{\rm free\ orbits}m_\rho|a-b|^2.       \tag{6.2}
\]

equivalently by (3.5)--(4.2).  The outer Real boundary term is (2.2).

The schematic notation in (6.2) means exactly
`Q_abs-Q_R=sum m|a-b|^2`; no sign is inferred from rearranging (6.1).
Thus a positive bulk square plus ordinary curvature proves an identity for
the wrong trace, while the trace-exact Real identity contains the negative
anti-invariant defect.

## 7. Outcome and next possible construction

The superconnection route derives the completed contact and exhibits a
positive bulk.  Its failure is completely localized:

\[
 \boxed{
 \text{Bochner defect}
 =\sum_{\{\rho,\rho^\iota\}\ \mathrm{free}}
 m_\rho|F(\rho)-F(\rho^\iota)|^2.}                       \tag{7.1}
\]

This defect vanishes for all tests exactly when there are no free orbits.
It cannot be controlled by the two Tate moments, since finite Mellin
interpolation realizes both chiral values independently.

A further non-spectral route would need a source-side symmetry forcing the
anti-invariant divisor cohomology to be exact before evaluation at zeros.
The additive Fourier involution does not do this by D.102.  The remaining
candidate is a **Real torsion pairing** or analytic-torsion anomaly whose
square is (7.1) and whose sign enters the outer boundary with the opposite
orientation.  It must arise from A--B--C duality without choosing the
nontrivial divisor.  The next audit tests whether Quillen torsion of the
mapping cone supplies such a cancellation or merely reproduces the same
Poincare--Lelong current.
