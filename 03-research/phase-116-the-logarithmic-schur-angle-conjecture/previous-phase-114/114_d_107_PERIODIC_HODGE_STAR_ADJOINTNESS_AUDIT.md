# D.107 — Periodic Hodge star and adjointness audit

## Status

Rows A--B--C determine an exact Hodge--Riemann **equation** on the odd
Poisson cohomology `V`:

* the A Kunneth metric supplies the positive tensor convention;
* the B half-density fixes central normalization and the Real reflection;
* the C scaling representation and Real Lefschetz pairing fix the adjoint
  relation and character.

An admissible Hodge star must be an involutive, Real self-adjoint,
scaling-equivariant operator `star` such that `H=Q star` is positive.  The
block equations can be solved completely.  On a nonfixed Real character
pair, the unique equivariant self-adjoint involutions leave `H`
hyperbolic.  The nonequivariant swap makes `H` positive but fails to
commute with scaling.  On a fixed semisimple character block, a positive
star exists but is not uniquely normalized by A--B--C.

Equivalently, a positive scaling-invariant Hermitian form solves a
Lyapunov equation.  It exists only when every centered scaling exponent is
purely imaginary; on the original nonsemisimple Frechet block it also
forces the nilpotent part to vanish.  At character level, existence of the
positive GNS polarization is exactly Weil positivity/row D.  A faithful
Hilbertization of the full Meyer module is potentially stronger because it
also imposes semisimplicity.

Locality and monoidality do not force a solution.  Prime-local transfer
blocks already have infinite negative index, and the Kunneth metric of A
does not descend through the Poisson cokernel by a metric functor.

No RH statement or spectral localization is assumed.  The paper is not
modified.

## 1. The source-defined Real pairing

Let `Q` denote the nondegenerate Real Lefschetz pairing on the algebraic
finite-character blocks of `V`.  The central scaling representation is

\[
 R_t=t^{-1/2}\rho(t).                                     \tag{1.1}
\]

The functional equation gives the `Q`-adjoint relation

\[
 R_t^* Q R_t=Q.                                          \tag{1.2}
\]

This is a Krein-unitary representation.  Its character, together with the
two even Tate classes, is the row-C nuclear character.

Define an admissible periodic Hodge star to be an operator satisfying

\[
 \star^2=I,qquad
 \star^*Q=Q\star,qquad
 [\star,R_t]=0\quad(t>0).                                \tag{1.3}
\]

The Hodge metric would be

\[
 H=Q\star.                                                \tag{1.4}
\]

The middle equation in (1.3) makes `H` Hermitian.  From (1.2) and scaling
equivariance,

\[
 R_t^*HR_t=H.                                             \tag{1.5}
\]

Row D would follow if (1.4) were positive on the primitive odd
cohomology and its trace metric agreed with D.102(4.4).

## 2. Free Real character block

After removing the common unitary phase, a free two-character block has

\[
 Q=J=\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad
 R_t=\begin{pmatrix}t^a&0\\0&t^{-a}\end{pmatrix},
 \quad a\ne0.                                             \tag{2.1}
\]

Equation (1.2) holds exactly.  Since the two characters are distinct, any
operator commuting with all `R_t` is diagonal:

\[
 \star=\begin{pmatrix}\epsilon_1&0\\0&\epsilon_2\end{pmatrix},
 \qquad\epsilon_i\in\{1,-1\}.                            \tag{2.2}
\]

The `Q`-self-adjoint equation in (1.3) forces

\[
 \epsilon_1=\epsilon_2.                                  \tag{2.3}
\]

Therefore

\[
 H=Q\star=\pm J,                                         \tag{2.4}
\]

which has inertia `(1,1)`.  No equivariant Hodge star is positive on a
free block.

There is an algebraically positive choice,

\[
 \star=J,qquad H=J^2=I.                                 \tag{2.5}
\]

But

\[
 JR_t\ne R_tJ\quad(a\ne0).                               \tag{2.6}
\]

Thus (2.5) changes the scaling adjoint and cannot retain the row-C
characters.  This is the precise reason why simply using the ordinary
positive divisor metric does not solve D.

## 3. Lyapunov form of the obstruction

Let `A` be the infinitesimal centered scaling generator.  A positive
Hermitian metric `H` makes scaling unitary exactly when

\[
 A^*H+HA=0.                                               \tag{3.1}
\]

For a scalar eigenvector `Av=lambda v`, positivity gives

\[
 0=\langle v,(A^*H+HA)v\rangle
 =2\mathrm{Re}(\lambda)\langle v,Hv\rangle.         \tag{3.2}
\]

Hence

\[
 \mathrm{Re}\,\lambda=0.                             \tag{3.3}
\]

On the free block `A=diag(a+i gamma,-a+i gamma)`, (3.1) forces the
positive diagonal entries of `H` to vanish when `a` is nonzero, a direct
contradiction.

If a fixed character has a generalized block

\[
 A=i\gamma I+N,qquad N\text{ nilpotent},                  \tag{3.4}
\]

then (3.1) reduces to

\[
 N^*H+HN=0.                                               \tag{3.5}
\]

A nilpotent operator which is skew-adjoint for a positive metric is zero.
Thus a faithful positive Hilbert realization of the full generalized
module also requires `N=0`.

This semisimplicity requirement is stronger than the character-level Weil
criterion, which records algebraic multiplicity but can realize it as a
positive multiplicity space.  Therefore the correct row-D target is first
the positive semisimplified/GNS character; a faithful metric on all of `V`
needs an additional theorem about Jordan blocks.

## 4. Fixed semisimple blocks and nonuniqueness

On a fixed centered character, `A=i gamma I` and the Real trace form can be
chosen positive.  Equation (3.1) then holds for every positive Hermitian
form on the multiplicity space.  The Hodge metric is therefore not unique:

\[
 H_\gamma>0\quad\text{arbitrary up to the imposed Real symmetry}.   \tag{4.1}
\]

The row-C character fixes only `Tr(H_gamma)` after normalization by
multiplicity, not its full matrix.  The A determinant metric fixes
effective periodic frames place by place, but no constructed metric
functor identifies those frames with the spectral multiplicity fibre of
`V`.  The B torsor fixes the half-density scale, not a basis in (4.1).

Thus A--B--C determine the adjointness equation and central scale, but not a
unique positive polarization even after solvability.

## 5. Character-level GNS equivalence

Let `I_0` be the involutive convolution ideal of primitive tests and put

\[
 \Phi(f\star g^\vee)
 :=\mathrm{Tr}_V\rho_-^0(f\star g^\vee)
 =-B_{\rm nuc}(f,g).                                      \tag{5.1}
\]

The statement

\[
 \Phi(f\star f^\vee)\ge0\quad(f\in I_0)                 \tag{5.2}
\]

is exactly row D.  If (5.2) holds, the GNS construction gives a positive
Hilbert space `H_GNS`, a `star`-representation of the centered scaling
algebra and a cyclic map from primitive tests whose Gram is (5.1).
Conversely, any such positive realization implies (5.2).

Therefore

\[
 \boxed{
 \text{positive periodic polarization with exact character}
 \quad\Longleftrightarrow\quad\text{row-D Weil positivity}.}        \tag{5.3}
\]

Invoking GNS after assuming (5.2) constructs the polarization but does not
prove it.

## 6. Locality and monoidality audit

One might hope that a monoidal star is forced from local Hodge stars.  This
fails for two independent reasons.

First, the local prime transfer ratio is expansive on one boundary arc and
contractive on another.  Its Pick space has infinite negative index by
D.100, so there is no positive local star whose tensor product can be
taken.

Second, the exact contact is a logarithmic derivative.  Prime powers of
one prime survive idempotently while mixed primes cancel.  A tensor product
of positive local metrics produces positive mixed Gram terms, as in D.103,
and cannot realize this support without a signed global relation.

The Kunneth metric of A is monoidal on effective periodic sections.  Row C
only carries its scalar nuclear action to the Poisson quotient; it does not
construct a strong monoidal metric functor

\[
 \mathrm{Coh}_{\rm per}(A)\longrightarrow\mathrm{Hilb}(V).
                                                                    \tag{6.1}
\]

Postulating (6.1) with the adjointness properties (1.3)--(1.5) would force
(5.2), so it is another exact formulation of the missing theorem.

## 7. Outcome and next source constraint

The block calculation proves that the periodic Hodge star cannot be chosen
by linear algebra while retaining scaling.  Positivity and equivariance
are compatible precisely on fixed centered characters.

A genuinely new source theorem must force (5.2) before forming the GNS
space.  The remaining categorical possibility is a Hodge--Riemann
**primitive decomposition** in the intrinsic periodic category of A, with
a functor to C which is conservative for the contact character.  Such a
theorem would make positivity occur before the Meyer quotient rather than
choose a star after it.

The next audit tests the only available primitive operator in A--B: the
Lefschetz raising map defined by external divisor degree and its formal
adjoint from the determinant metric.  One must prove a hard-Lefschetz
isomorphism and a positive primitive form whose C-realization is (5.1).
If the adjoint is defined using `B_nuc`, the construction is circular.

