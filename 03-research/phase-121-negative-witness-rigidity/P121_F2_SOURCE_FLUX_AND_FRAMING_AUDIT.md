# P121 -- source flux, boundary threshold and divisor-framing audit

## Status

This note tests four possible derivations of the scalar Krein-flux law in
`P121_PARABOLIC_COMMON_NILPOTENT_LIFT.md`.  All calculations are exact.
They do not prove F2.  They show that the missing datum is a framing law at
the critical divisor, not ordinary determinant single-valuedness, formal
flatness, tensorization, or the two Tate moments.

## 1. The scalar Krein flux is exactly the conormal coefficient

Let

\[
 J=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
 N=\begin{pmatrix}i&1\\1&-i\end{pmatrix},\qquad N^2=0,
\]

and `M_c=I+cN`.  Since `N^*JN=0`, direct expansion gives

\[
 \operatorname {tr}(M_c^*JM_c-J)=-4\operatorname {Im}c. \tag{1.1}
\]

At a critical zero `rho=1/2+i gamma`, put

\[
 c_{F,\rho}=2\pi i\,m_\rho K_F(i\gamma).             \tag{1.2}
\]

The first-contact kernel is complex linear, so `iF` is a first-contact
state whenever `F` is.  Since `c_(iF,rho)=i c_(F,rho)`, conservation of
(1.1) for both `F` and `iF` is equivalent to

\[
 \operatorname {Im}c_{F,\rho}=0,\qquad
 \operatorname {Re}c_{F,\rho}=0.                    \tag{1.3}
\]

Thus the scalar law is a minimal coordinate for F2, but not a weaker
consequence of first contact.  Any proof of it must be orientation-breaking:
the scalar supertrace of the two causal ports cancels their opposite
coefficients for every value of `c`.

## 2. Opposite nilpotents do not obtain flatness for free

It is tempting to attach

\[
 N_+=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
 N_-=\begin{pmatrix}0&0\\1&0\end{pmatrix}           \tag{2.1}
\]

to the two causal jets.  Their mixed commutator is nonzero.  If the two
normal coefficients are `c` and `-c`, the mixed curvature contains

\[
 -c^2[N_+,N_-].                                     \tag{2.2}
\]

Consequently flatness would force `c=0`.

This is not a sourced flatness theorem.  The two frozen scalar
displacements commute.  Every functorial representation of their
commutative dual-number algebra sends them to commuting endomorphisms.
Replacing those endomorphisms by (2.1) is additional noncommutative data;
requiring its curvature (2.2) to vanish is precisely the missing matching.
If instead both connections are obtained by differentiating the same scalar
determinant, their curvature vanishes tautologically and (2.2) never
appears.  Hence the opposite-nilpotent square has the correct detector but
no independent source law.

## 3. Tensorization retains the Tate forcing

For a first-contact state write

\[
 \mathscr A_TF=r_F\in
 \operatorname {span}\{e^{-t/2},e^{t/2}\}.          \tag{3.1}
\]

On the tensor square one has the exact identity

\[
 (\mathscr A_T\otimes I+I\otimes\overline{\mathscr A_T})
 (F\otimes\overline F)
 =r_F\otimes\overline F+F\otimes\overline{r_F}.    \tag{3.2}
\]

The right side does not vanish under the two Tate conditions on `F`; those
conditions pair `F` with the Tate lines and do not annihilate the tensor
vectors in (3.2).  Projecting both factors to the primitive space merely
turns (3.2) into the tensorized compressed zero-mode equation.  It supplies
no new diagonal residue law.  Thus linearizing `|K_F|^2` on the tensor
square preserves, rather than removes, the first-contact forcing.

## 4. Two Tate moments do not cross the half-Sobolev boundary

Let `b` be supported in `[0,delta)` and equal, near zero, to

\[
 b(x)={1\over\sqrt{\log(1/x)}}\quad(x>0),\qquad b(x)=0\quad(x<0). \tag{4.1}
\]

The phase-121 boundary theorem proves `b in H^s` for every `s<1/2`.  The
endpoint is sharp:

### Proposition 4.1

The function `b` is not in `H^(1/2)(R)`.  Moreover there is a compactly
supported function `b_0` satisfying both Tate moments

\[
 \int b_0(t)e^{t/2}dt=\int b_0(t)e^{-t/2}dt=0        \tag{4.2}
\]

which has the same boundary germ (4.1), and hence is still not in
`H^(1/2)`.

#### Proof

The cross-boundary part of the Gagliardo seminorm satisfies

\[
 \begin{aligned}
 [b]_{H^{1/2}}^2
 &\geq
 \int_0^{\delta/2}|b(x)|^2
       \int_{-\delta}^{0}{dy\over|x-y|^2}\,dx\\
 &\gg\int_0^{\delta/2}{dx\over x\log(1/x)}=+\infty.
 \end{aligned}                                      \tag{4.3}
\]

Choose two smooth functions `phi_+`, `phi_-` supported in the interior,
away from zero, whose two-by-two Tate moment matrix is invertible.  There
are unique scalars `a_+`, `a_-` such that

\[
 b_0=b-a_+\phi_+-a_-\phi_-                         \tag{4.4}
\]

satisfies (4.2).  The correction vanishes near zero, so (4.3) is unchanged.
QED.

Therefore the Tate constraints alone cannot improve the radical bootstrap
through the `1/2` threshold.  A proof using boundary regularity must extract
an additional Euler-specific cancellation from the equality equation.

## 5. Ordinary sourced determinants erase the frozen residue

Put `E(z)=xi(1/2+z)`, `H_F=EK_F`, and consider the genuine holomorphic
determinant deformation

\[
 E_\varepsilon=E+\varepsilon H_F
 =E(1+\varepsilon K_F).                             \tag{5.1}
\]

Its logarithmic connection varies by

\[
 \left.\partial_\varepsilon
 {E_\varepsilon'\over E_\varepsilon}\right|_{\varepsilon=0}
 =K_F'.                                             \tag{5.2}
\]

In particular (5.2) has zero residue at every critical zero, for every
`F`.  The frozen-source current instead contains

\[
 {E'\over E}K_F,                                    \tag{5.3}
\]

whose residue at a simple zero `lambda` is `K_F(lambda)`.  In the genuine
variation the two terms in

\[
 {H_F'\over E}-{E'H_F\over E^2}
 ={E'K_F+EK_F'\over E}-{E'K_F\over E}=K_F'          \tag{5.4}
\]

cancel (5.3) exactly.

Equivalently, exponentiating a primitive of (5.3) produces monodromy
`exp(2 pi i K_F(lambda))`.  Declaring it single valued is not inherited
from (5.1); it imposes integral residues on the frozen current.  Since the
radical line contains `aF` for every complex `a`, such integrality for the
whole line would force `K_F(lambda)=0` and is therefore F2 itself.

The distinction is a framing distinction.  The deformation (5.1) preserves
the zero divisor automatically but changes the unit multiplying `E` by
`1+epsilon K_F`.  F2 says that this unit equals one to first order on every
critical fibre.  Ordinary determinant single-valuedness fixes the divisor,
not that fibrewise framing.

## 6. Consequence

The exact remaining source theorem is now:

> a first-contact state canonically preserves the critical framing of the
> completed Euler determinant before the two causal orientations are
> supertraced.

Such a theorem immediately gives the scalar flux law (1.1), hence F2 and
the already proved Cartwright descent.  It may not be replaced by ordinary
determinant deformation, formal flatness, tensorization, the two Tate
moments, or an uncorrected half-Sobolev bootstrap: Sections 2--5 show
exactly why each replacement loses the frozen conormal coefficient.

```text
scalar flux coordinate                            PROVED
opposite-nilpotent flatness from scalar source    NOT AVAILABLE
tensor forcing cancellation                       FALSE
Tate moments imply H^(1/2)                        FALSE
ordinary determinant variation carries F2 residue FALSE
equality-state critical framing law               OPEN (F2)
global square and row (d)                         OPEN
```

No change to paper 42 follows from this audit alone.
