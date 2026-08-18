# D.95 — Functional-equation Real double and divisor blocks

## Status

The canonical double of the completed determinant line under

\[
 \iota(s)=1-\overline s                                      \tag{0.1}
\]

has an explicit reflection form.  A divisor point fixed by `iota` gives a
positive square.  A free two-point orbit gives a hyperbolic swap block of
determinant negative.  The pullback by a primitive test function is exactly
the spectral side of the completed Weil form.

The bulk Dolbeault/Dirac operator before insertion of the divisor has the
standard positive Dirichlet-to-Neumann operator and Hardy Calderon
projector.  It does not contain the arithmetic divisor blocks.  Inserting
the Real divisor adds the positive fixed blocks and the hyperbolic free
blocks.  Therefore reflection positivity of the completed divisor module
is equivalent to all nontrivial divisor orbits being fixed by `iota`, i.e.
to localization on the central line.

The orientation and central torsor of A--B implement the involution and
the half-density, but they do not select the positive eigenline inside a
free orbit.  Both parity eigenspaces occur in the primitive test category.
Discarding the negative eigenline would impose the desired localization
rather than derive it.

This gives an exact categorical form of the remaining row-D statement,
not a proof of RH.  No sign or zero localization is assumed.  The paper is
not modified.

## 1. The Real determinant line

Let `lambda_comp` denote the completed local determinant line of D.94.
The functional equation and complex conjugation give a Real isomorphism

\[
 c:\iota^*\overline{\lambda_{\rm comp}}
      \longrightarrow\lambda_{\rm comp},
 \qquad c\,\iota^*\overline c=1.                           \tag{1.1}
\]

The fixed locus of `iota` is `Re(s)=1/2`.  In the centered coordinate
`z=s-1/2`, the involution is

\[
 z\longmapsto-\overline z.                                \tag{1.2}
\]

Before using the divisor, take the right half-plane `x=Re(z)>=0` and the
flat Dolbeault double

\[
 \mathscr D=
 \begin{pmatrix}0&-\partial_x+i\partial_y\\
                 \partial_x+i\partial_y&0
 \end{pmatrix}.                                           \tag{1.3}
\]

On a boundary Fourier mode `e^(i tau y)`, the decaying Cauchy data select
one chirality according to the sign of `tau`.  Thus the Calderon projector
is the Hardy projection

\[
 C_0(\tau)=1_{(-\infty,0)}(\tau)                           \tag{1.4}
\]

for the displayed Dolbeault convention (the complementary chirality has
the opposite projector), and the scalar Dirichlet-to-Neumann operator is

\[
 N_0(\tau)=|\tau|\ge0.                                    \tag{1.5}
\]

Equations (1.4)--(1.5) are fixed before the arithmetic divisor is
inserted.  Tensoring with the flat Real line (1.1) does not alter them away
from its divisor.

## 2. Mapping cone of the divisor

Let `Xi(s)` be any entire normalization of the completed zeta determinant,
so that its nontrivial divisor is the zero divisor and

\[
 \Xi(s)=\Xi(1-s),\qquad
 \overline{\Xi(\overline s)}=\Xi(s).                       \tag{2.1}
\]

The divisor object is represented locally by the mapping cone

\[
 \mathcal K_\Xi=\mathrm{Cone}
   [\mathcal O\xrightarrow{\Xi}\mathcal O].               \tag{2.2}
\]

At a zero `rho` of multiplicity `m_rho`, its length is `m_rho`; hence the
divisor fibre is the corresponding jet space.  The Real structure pairs
the fibre at `rho` with the fibre at `iota(rho)`.

For the sign audit it suffices to display one scalar in each jet; higher
multiplicity repeats the same block after choosing the derivative jet
frame.  If `rho=iota(rho)`, the Real trace pairing is

\[
 q_\rho(a)=m_\rho|a|^2.                                   \tag{2.3}
\]

If `rho` and `rho^iota=iota(rho)` are distinct, the orbit fibre is
`C e_rho direct-sum C e_(rho^iota)` and its trace pairing is

\[
 q_{\{\rho,\rho^\iota\}}(a,b)
 =m_\rho(a\overline b+b\overline a),
 \qquad
 G_\rho=m_\rho\begin{pmatrix}0&1\\1&0\end{pmatrix}.       \tag{2.4}
\]

Consequently

\[
 \det G_\rho=-m_\rho^2<0,
 \qquad\mathrm{inertia}(G_\rho)=(1,1).              \tag{2.5}
\]

This is the local Real/Witt decomposition: fixed divisor points give
definite lines and free involution orbits give hyperbolic planes.

## 3. Pullback by the primitive test transform

For a logarithmic Schwartz test `f`, let `F(s)` denote its Mellin--Laplace
transform in the normalization of D.32.  The involutive convolution
`h=f star f^vee` satisfies

\[
 \widehat h(s)=F(s)\overline{F(1-\overline s)}.             \tag{3.1}
\]

The two polar jets are

\[
 F(0)=M_-(f),\qquad F(1)=M_+(f).                           \tag{3.2}
\]

Thus primitivity removes exactly the two polar divisor terms.  Pulling the
nontrivial divisor trace (2.3)--(2.4) back along evaluation of `F` gives

\[
 \begin{aligned}
 Q_{\rm div}(f)={}&
 \sum_{\rho=\iota\rho}m_\rho|F(\rho)|^2\\
 &+\sum_{\{\rho,\iota\rho\},\ \rho\ne\iota\rho}
 2m_\rho\mathrm{Re}
   \bigl(F(\rho)\overline{F(\iota\rho)}\bigr).           \tag{3.3}
 \end{aligned}
\]

This is the zero side of the Weil explicit form.  With the conventions of
D.49,

\[
 Q_{\rm div}(f)=QW(f,f)=-B_{\rm nuc}(f,f)
 \quad\text{on }\ker M_-\cap\ker M_+.                      \tag{3.4}
\]

Equation (3.4) is the divisor version of the normal-connection pullback in
D.94.  The arithmetic side contains all prime powers and Gamma; the Real
divisor side decomposes them into the fixed and free orbit blocks above.

## 4. Reflection positivity is divisor localization

If every nontrivial zero is fixed by `iota`, then every summand in (3.3)
is a positive square and

\[
 Q_{\rm div}(f)\ge0,
 \qquad B_{\rm nuc}(f,f)\le0                              \tag{4.1}
\]

for every primitive test.

Conversely, a free orbit contains the negative vector `(1,-1)` of (2.4).
The evaluation map from compactly supported smooth tests to any finite set
of distinct Mellin values, together with the two polar moments, is
surjective.  Indeed, a linear relation among these evaluation functionals
would be a linear relation among distinct exponentials on an interval,
which is impossible.  Hence the negative parity of an individual finite
orbit is visible to the local divisor module while preserving the two
primitive constraints.

At the global completed level the standard Weil criterion supplies the
corresponding density/approximation statement for the nuclear test space.
Therefore

\[
 \boxed{
 \text{reflection positivity of the completed Real divisor trace}
 \quad\Longleftrightarrow\quad
 \mathrm{supp}(\mathrm{Div}_{\rm nt}\Xi)
 \subset\mathrm{Fix}(\iota).}                       \tag{4.2}
\]

The right side is precisely `Re(rho)=1/2` for every nontrivial zero.
Equation (4.2) is a geometric equivalence, not a new proof of its right
side.

## 5. Audit of the A--B orientation and central torsor

The central half-density of A--B supplies the involution on test sections

\[
 (\Theta f)(t)=\overline{f(-t)},                            \tag{5.1}
\]

which exchanges the two fibres in every free orbit.  On the orbit block,
the induced linear swap is

\[
 J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.                  \tag{5.2}
\]

Its spectral projections are

\[
 P_+={I+J\over2},\qquad P_-={I-J\over2}.                  \tag{5.3}
\]

The torsor normalization fixes the common scale and makes `J` isometric;
it does not eliminate either `P_+` or `P_-`.  Both parity subspaces are
nonzero in the periodic/Witt coefficient category, and both occur among
primitive tests.  Orientation reversal exchanges the orbit labels but
commutes with the decomposition (5.3).

Selecting `P_+` alone would impose

\[
 F(\rho)=F(\iota\rho)                                     \tag{5.4}
\]

at every free zero orbit.  This is not a consequence of the two Tate
moments, Witt multiplicativity, the central torsor, or the functional
equation of `Xi`: the latter constrains the determinant section, not every
test transform `F`.  Selecting the right-half-plane member alone instead
changes the swap trace (2.4) into `|F(rho)|^2` and therefore no longer
pulls back to `B_nuc`.

Thus A--B constructs the Real double but does not canonically choose the
positive Lagrangian needed to remove the free-orbit negative direction.

## 6. Consequence for the next step

The canonical double has now exhausted the data supplied by the functional
equation:

* its divisor-free bulk has a positive universal DtN operator `|D_y|`;
* fixed divisor points add positive boundary squares;
* free divisor orbits add hyperbolic swap blocks;
* the A--B torsor provides the reflection but no positive-orbit selection.

A proof of D must therefore add a theorem forcing the completed divisor
module to have no free `iota`-orbits.  A polarization chosen after reading
the locations of the zeros is circular.  A viable further pivot must act
before spectral decomposition and force fixedness from the arithmetic
operator itself--for example, a self-adjoint realization whose
characteristic determinant is `Xi` and whose construction uses only the
prime--Gamma correspondences of A--B--C.  Constructing that realization,
rather than postulating it, is the remaining gate.

