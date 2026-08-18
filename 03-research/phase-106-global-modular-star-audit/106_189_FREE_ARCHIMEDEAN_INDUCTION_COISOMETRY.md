# 106.189 — Free archimedean induction is a coisometry

## 1. Purpose

The nuclear Euler trace domain of 106.188 makes Kronecker restriction
closable but carries the CCM scaling shifts only for the dense discrete
subgroup \(G=\log\mathbb Q_+^\times\).  The most direct way to obtain a
real action is to tensor the coefficient module with a free archimedean
coordinate.

This note performs that construction exactly.  It restores the real
unitary action, but the resulting collapse map is a coisometry and hence
surjective.  Appending a Gamma multiplier afterwards leaves a torsion
object determined only by that multiplier; the Euler coefficients
contribute no cokernel.  Therefore the archimedean coordinate cannot be a
free tensor factor.  It must enter through a nontrivial relative
differential or boundary condition.

## 2. The continuous induced coefficient space

Fix \(c>1/2\) and let

\[
 \mathcal K_c=\ell^2\!\left(
 \bigoplus_p\mathbb Z,\ e^{2c\ell_E(\mathbf n)}\right)       \tag{1}
\]

be \(\mathscr H_1^{(c)}\) from 106.188.  After the unitary coordinate
change

\[
 b_{\mathbf n}=e^{c\ell_E(\mathbf n)}a_{\mathbf n},          \tag{2}
\]

identify \(\mathcal K_c\) with ordinary \(\ell^2\).  Introduce the
archimedean spectral coordinate and set

\[
 \mathcal H_{\rm ind}
 =L^2\!\left(\mathbb R_\xi;\ell^2(\bigoplus_p\mathbb Z)\right).
                                                                    \tag{3}
\]

For each \(\xi\), define

\[
 v_c(\xi)_{\mathbf n}
 =e^{-c\ell_E(\mathbf n)}e^{-i\xi L(\mathbf n)}.             \tag{4}
\]

Lemma 2.1 of 106.188 gives

\[
 \boxed{
 \|v_c(\xi)\|_{\ell^2}^2
 =\sum_{\mathbf n}e^{-2c\ell_E(\mathbf n)}
 =Z_E(2c),}                                                 \tag{5}
\]

independently of \(\xi\).

## 3. The fiberwise collapse operator

Define

\[
 (\mathcal T_cb)(\xi)
 =\langle b(\xi),v_c(\xi)\rangle_{\ell^2}.                   \tag{6}
\]

This is the Fourier-coordinate form of

\[
 a_{\mathbf n}(x)\longmapsto
 \sum_{\mathbf n}
 e^{i\xi L(\mathbf n)}\widehat a_{\mathbf n}(\xi).           \tag{7}
\]

### Theorem 3.1 — Exact coisometry

The operator

\[
 \mathcal T_c:\mathcal H_{\rm ind}\longrightarrow L^2(\mathbb R,d\xi)
                                                                    \tag{8}
\]

is bounded and satisfies

\[
 \boxed{
 \mathcal T_c\mathcal T_c^*
 =Z_E(2c)\,I.}                                              \tag{9}
\]

Consequently \(Z_E(2c)^{-1/2}\mathcal T_c\) is a coisometry and
\(\mathcal T_c\) is surjective.

#### Proof

The adjoint is the pointwise column operator

\[
 (\mathcal T_c^*f)(\xi)=f(\xi)v_c(\xi).                     \tag{10}
\]

Therefore (5) gives

\[
 (\mathcal T_c\mathcal T_c^*f)(\xi)
 =f(\xi)\langle v_c(\xi),v_c(\xi)\rangle
 =Z_E(2c)f(\xi).                                            \tag{11}
\]

This proves every assertion. \(\square\)

The prime support changes the unit vector
\(Z_E(2c)^{-1/2}v_c(\xi)\) inside each fiber, but it does not change the
scalar singular value of the row operator.

## 4. Real scaling is restored

Define

\[
 (\mathcal U_tb)(\xi)=e^{it\xi}b(\xi),\qquad
 (M_tf)(\xi)=e^{it\xi}f(\xi).                               \tag{12}
\]

### Proposition 4.1 — Exact real equivariance

Both actions in (12) are strongly continuous unitary groups and

\[
 \boxed{\mathcal T_c\mathcal U_t=M_t\mathcal T_c
 \qquad(t\in\mathbb R).}                                   \tag{13}
\]

#### Proof

Unitarity and strong continuity are standard for multiplication by
\(e^{it\xi}\).  Equation (13) follows pointwise from (6). \(\square\)

Thus the free archimedean coordinate solves the real-action problem of
106.188, but Theorem 3.1 shows that it simultaneously annihilates the
desired cokernel.

## 5. Appending Gamma after induction

Let \(\gamma(\xi)\) be any measurable scalar multiplier and put

\[
 \mathcal T_{c,\gamma}=M_\gamma\mathcal T_c.                 \tag{14}
\]

### Theorem 5.1 — Euler-blind torsion after scalar Gamma coupling

\[
 \boxed{
 \operatorname {Ran}\mathcal T_{c,\gamma}
 =\operatorname {Ran}M_\gamma,}                             \tag{15}
\]

and

\[
 \mathcal T_{c,\gamma}\mathcal T_{c,\gamma}^*
 =Z_E(2c)M_{|\gamma|^2}.                                    \tag{16}
\]

Hence the reduced and extended range defects of
\(\mathcal T_{c,\gamma}\) are exactly those of the scalar Gamma
multiplier, independently of the prime phases in \(v_c(\xi)\).

#### Proof

Surjectivity of \(\mathcal T_c\) gives (15).  Equation (16) follows from
(9):

\[
 M_\gamma\mathcal T_c\mathcal T_c^*M_{\overline\gamma}
 =Z_E(2c)M_{|\gamma|^2}.                                   \tag{17}
\]

The polar and range assertions are immediate. \(\square\)

A finite-rank polar correction can alter only a finite-dimensional part
of this conclusion.  It cannot turn the free tensor collapse into the
nonreduced CCM spectral cokernel.

## 6. The required non-free coupling

Theorems 3.1 and 5.1 exclude the construction

\[
 \text{Euler coefficient space}
 \ \widehat\otimes\
 \text{free archimedean carrier}
 \ \xrightarrow{\text{row collapse}}\
 \text{real spectral line}.                                \tag{18}
\]

The missing relative differential must violate the fiberwise rank-one
coisometry mechanism.  Concretely, at least one of the following must
occur:

1. Gamma acts as an operator mixing prime indices, not as a scalar
   multiplier after collapse;
2. the pole imposes a boundary relation before the archimedean tensor
   product is completed;
3. the source is a mapping cone in which the Euler row and the
   archimedean row enter with opposite parity and share a nontrivial
   kernel;
4. the coefficient fibers vary with \(\xi\) through a connection whose
   curvature contributes the relative intersection form.

These are different descriptions of a non-free finite/infinite-place
coupling.  A direct sum or scalar product of the already positive local
modules cannot supply it.

## 7. Status

Proved without RH or zero input:

* the exact continuous induction of the nuclear Euler coefficient space;
* restoration of the strongly continuous unitary real action;
* the coisometry identity (9) and disappearance of the cokernel;
* Euler-blindness of every subsequently appended scalar Gamma multiplier.

Still required:

* a non-free Gamma--Euler--polar relative differential whose degree-one
  torsion agrees with CCM and whose Green form is the descended
  alternating form.
