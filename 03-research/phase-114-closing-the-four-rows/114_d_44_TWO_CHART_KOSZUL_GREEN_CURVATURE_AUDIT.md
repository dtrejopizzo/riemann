# D.44 — Two-chart Koszul, determinant and Green-curvature audit

## 1. Question

Let

\[
 C_\zeta=
 [\mathcal L_\gamma^0\xrightarrow{\,\sigma_\zeta\,}\mathcal E]
                                                               \tag{1.1}
\]

be the exact Frechet two-chart presentation of D.42, placed in degrees
`-1,0`.  Here `sigma_zeta` is a closed embedding and

\[
 H^{-1}(C_\zeta)=0,
 \qquad H^0(C_\zeta)=V.                                      \tag{1.2}
\]

The purpose of this note is to determine whether mixed/Koszul cohomology,
its determinant and a Green/Riemann--Roch identity construct the missing
row-D positivity without using the zero divisor or assuming the sign of the
Weil form.

## 2. The mixed complex exists, but is virtual

In the derived category of complete locally convex spaces for which the
completed tensor products below are defined, form

\[
 \mathcal K_\zeta
   =C_\zeta^\vee\widehat\otimes^{\mathbf L}C_\zeta.             \tag{2.1}
\]

Before contraction, (2.1) is the total complex of

\[
 \begin{matrix}
 (\mathcal L_\gamma^0)^\vee\widehat\otimes\mathcal L_\gamma^0
 &\longrightarrow&
 (\mathcal L_\gamma^0)^\vee\widehat\otimes\mathcal E
 \\[1mm]
 \downarrow &&\downarrow
 \\[1mm]
 \mathcal E^\vee\widehat\otimes\mathcal L_\gamma^0
 &\longrightarrow&
 \mathcal E^\vee\widehat\otimes\mathcal E .
 \end{matrix}                                                  \tag{2.2}
\]

Strict exactness of (1.1) identifies it, whenever the stated derived tensor
is exact on the factors under consideration, with

\[
 \mathcal K_\zeta\simeq V^\vee\widehat\otimes^{\mathbf L}V.    \tag{2.3}
\]

The Tate--Paugam contraction and the row-C nuclear trace give a map from
(2.3) to the Tate line.  For compactly supported tests `f,g`, its Euler
character is the polarization of the nuclear Weil form:

\[
 \chi_{\rm nuc}\bigl(\mathcal K_\zeta;f,g\bigr)
     =B_{\rm nuc}(f,g),                                        \tag{2.4}
\]

with the sign convention fixed in D.32 and D.37.  Thus (2.1) is a valid
cohomological packaging of the already proved A--B--C character.

It does not supply effectivity.  In the relative nuclear `K_0` group used
by row C,

\[
 [C_\zeta]=[\mathcal E]-[\mathcal L_\gamma^0]=[V],             \tag{2.5}
\]

and a relative/nuclear determinant functor records the same alternating
difference:

\[
 \det C_\zeta
   =\det\mathcal E\otimes(\det\mathcal L_\gamma^0)^{-1}.       \tag{2.6}
\]

The qualification is essential: the Frechet spaces in (1.1) are not
finite-dimensional perfect complexes, so their ordinary Knudsen--Mumford
determinant lines do not exist.  Row C supplies determinants of nuclear
integrated endomorphisms, or equivalently a relative determinant after the
two-chart comparison; no absolute determinant line is silently asserted.

Neither relative `K_0` nor the nuclear determinant orders this virtual
class.  A quadratic Euler trace can be extracted after (2.1), but its sign
is not a formal consequence of exactness or determinant multiplicativity.

## 3. Exact source-side virtual metric

D.32 constructs, without zeros, source operators `S` and `B` such that on
the primitive test space

\[
 \mathcal P=\{F:M_+(F)=M_-(F)=0\}
\]

one has

\[
 B_{\rm nuc}(F,G)
   =\langle \mathbf SF,\mathbf SG\rangle
    -\langle \mathbf BF,\mathbf BG\rangle.                    \tag{3.1}
\]

Consequently the hermitian determinant of the mixed complex has the exact
virtual curvature operator

\[
 \mathscr R_{\rm vir}=\mathbf S^*\mathbf S-\mathbf B^*\mathbf B,
 \qquad
 B_{\rm nuc}(F,G)=\langle F,\mathscr R_{\rm vir}G\rangle.       \tag{3.2}
\]

Equivalently, the would-be effective Hodge defect is

\[
 \boxed{
 \Delta_H=\mathbf B^*\mathbf B-\mathbf S^*\mathbf S.}         \tag{3.3}
\]

This is the exact curvature/effectivity defect.  The desired primitive
sign is precisely

\[
 \Delta_H\ge0\quad\hbox{on }\mathcal P.                        \tag{3.4}
\]

If (3.4) holds, the Douglas factorization lemma gives a contraction `A`
(on the closures of the appropriate ranges) such that

\[
 \mathbf S=A\mathbf B,
 \qquad \|A\|\le1,                                             \tag{3.5}
\]

and conversely (3.5) implies (3.4).  Therefore an effective Koszul model
for the virtual determinant is equivalent to constructing the contraction
(3.5).  Exactness of the two-chart complex does not construct `A`.

This gives a sharp, source-defined formulation of the missing theorem:

\[
 \boxed{
 \text{effectivity of the mixed determinant}
 \Longleftrightarrow
 \Delta_H\ge0
 \Longleftrightarrow
 B_{\rm nuc}|_{\mathcal P}\le0.}                      \tag{3.6}
\]

The last condition is Weil's criterion.  Hence declaring the virtual
determinant effective would assume row D rather than prove it.

## 4. The Green/scattering identity and its exact limitation

For a finite set `P` of primes, D.33 constructs the source-defined unitary
scattering transition

\[
 \Theta_P(\tau)=u_\infty(\tau)
   \prod_{p\in P}\frac{b_{p^{-1/2}}(e^{i\tau\log p})}
                         {e^{i\tau\log p}}.                     \tag{4.1}
\]

Its logarithmic phase derivative is

\[
 \begin{aligned}
 \kappa_P(\tau)
 &:={1\over i}{d\over d\tau}\log\Theta_P(\tau)\\
 &=m_\infty(\tau)+
   \sum_{p\in P}\log p
   \left(P_{p^{-1/2}}(e^{i\tau\log p})-1\right),               \tag{4.2}
 \end{aligned}
\]

and the exact finite Green/RR identity is

\[
 B_P(F,F)={1\over2\pi}\int_{\mathbb R}
       \kappa_P(\tau)|\widehat F(\tau)|^2\,d\tau.              \tag{4.3}
\]

After the paired stabilization, (4.3) is (3.1).  Thus the desired
Green/RR **identity** exists.

There are two independent reasons why it is not a positivity theorem.

### 4.1 Phase derivative is not Chern curvature

On the real boundary `|Theta_P|=1`.  Therefore the hermitian line with
unitary transition (4.1) is flat there: its Chern norm curvature is zero.
The nonzero quantity (4.2) is a connection/scattering phase density (an
eta-type boundary term), not the curvature of a positive hermitian metric.

After complexification, (4.1) is a quotient of inner/outer factors.  Its
Poincare--Lelong current is a **difference** of divisor currents (numerator
minus denominator, plus the Gamma contribution), hence a virtual current.
It is not effective before (3.4) is proved.

### 4.2 The phase density changes sign

At `tau=0`, every term is positive:

\[
 m_\infty(0)=\log\pi-\psi(1/4)>0,
 \qquad
 P_r(1)-1={2r\over1-r}>0,                                    \tag{4.4}
\]

so

\[
 \kappa_P(0)>0.                                                \tag{4.5}
\]

For fixed finite `P`, the prime sum in (4.2) is bounded, whereas

\[
 m_\infty(\tau)
 =\log\pi-\mathrm{Re}\,\psi(1/4+i\tau/2)
 =\log\pi-\log(|\tau|/2)+o(1).                                \tag{4.6}
\]

Hence

\[
 \liminf_{|\tau|\to\infty}\kappa_P(\tau)=-\infty.             \tag{4.7}
\]

Thus neither `kappa_P` nor `-kappa_P` is everywhere nonnegative.  The
natural determinant metric is neither plurisubharmonic nor
plurisuperharmonic in the sense required to deduce (3.4).  Equations
(4.5)--(4.7) are the requested explicit curvature counterexample.

Primitivity imposes the two values at `+/-i/2`; it does not turn the
pointwise density (4.2) into one of fixed sign.  A possible global
inequality after these two constraints is exactly the nonlocal Hodge
statement (3.4), not a local curvature consequence.

## 5. Equality case without spectral input

Assume (3.4), but do not use zeros.  Functional calculus gives

\[
 -B_{\rm nuc}(F,F)
   =\langle F,\Delta_HF\rangle
   =\|\Delta_H^{1/2}F\|^2.                                   \tag{5.1}
\]

Therefore the equality locus is exactly

\[
 \boxed{
 B_{\rm nuc}(F,F)=0
 \Longleftrightarrow
 F\in\ker\Delta_H.}                                           \tag{5.2}
\]

In the contraction model (3.5), this is

\[
 \|\mathbf BF\|^2-\|A\mathbf BF\|^2=0,
 \quad\text{i.e.}\quad
 \mathbf BF\in\ker(I-A^*A).                                  \tag{5.3}
\]

Thus the source-defined strict equality theorem is precisely

\[
 \ker\Delta_H\cap\mathcal P=\{0\},                            \tag{5.4}
\]

or equivalently that the contraction `A` has no isometric vector coming
from a nonzero primitive class.  Neither (5.4) nor even existence of `A`
follows from the Frechet exactness of (1.1).  D.24 proves strictness after
the sign by a spectral density argument; that argument is intentionally not
used here.  Without zeros, (5.4) remains the exact equality gate.

## 6. Why the ordinary Koszul differential cannot manufacture effectivity

One might try to replace the virtual pair `(S,B)` by a two-term Hilbert
complex

\[
 [\mathscr H_B\xrightarrow d\mathscr H_S].                    \tag{6.1}
\]

For its Euler metric to reproduce (3.1) canonically, `d` must intertwine
all A--B--C actions and its graph defect must be (3.3).  Polar decomposition
then produces exactly a factorization `S=A B` with `A` contractive.
Therefore specifying such a differential with positive quotient metric is
equivalent to (3.5).  Taking `d=0` reproduces only a formal difference of
Hilbert spaces; taking `d` from `sigma_zeta` reproduces the Meyer quotient
but supplies no relation between the two norms in (3.1).

The mixed Koszul construction consequently succeeds at the level of
cohomology, Euler character and determinant identity, and fails exactly at
the passage from a virtual hermitian line to an effective positive one.

## 7. Verdict

### Constructed without zeros or a sign assumption

1. the strict Frechet complex (1.1) and mixed derived object (2.1);
2. its Tate--Paugam contraction and Euler character (2.4);
3. the determinant/Green identity (3.1), equivalently (4.3);
4. the exact virtual curvature operator (3.2);
5. the exact Hodge defect `Delta_H` in (3.3);
6. the exact equality locus (5.2).

### Exact failure

1. a determinant functor preserves virtual differences and has no
   positivity order;
2. the natural unitary Green line is flat in norm, while its nonzero RR
   term is a signed phase derivative;
3. the semilocal density `kappa_P` changes sign by (4.5)--(4.7);
4. effectivity is equivalent to the unproved contraction (3.5);
5. strict equality is equivalent to the unproved source injectivity (5.4).

Hence the two-chart mixed/Koszul route does not close row D.  It does,
however, identify the exact curvature defect entirely on the source side:

\[
 \boxed{\Delta_H=\mathbf B^*\mathbf B-\mathbf S^*\mathbf S.}
\]

Proving that this operator is positive and injective on the primitive
subspace is precisely the remaining Hodge/effectivity theorem.
