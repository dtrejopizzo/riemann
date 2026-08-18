# D.193 — Three-component A--B Lyapunov polarization gate

## Verdict

The three canonical components of A--B--C do not admit a faithful positive
operator-valued weight invariant under central scaling unless the
correspondence spectrum is supported on the critical line.  The obstruction
is already visible in the exact Lyapunov equation.

On the two ruling directions and the correspondence direction the central
generator is

\[
 A=\mathrm{diag}\,\left(-\tfrac12,\tfrac12,D_\Gamma\right),
 \qquad (D_\Gamma h)(s)=(s-\tfrac12)h(s).                  \tag{0.1}
\]

A Hermitian weight \(W\) is scaling invariant exactly when

\[
 \boxed{A^*W+WA=0.}                                      \tag{0.2}
\]

The ruling diagonal blocks vanish.  Positivity then forces every row and
column meeting a ruling to vanish.  On the correspondence sector, an
invariant kernel can be supported only on

\[
 t=1-\bar s.                                             \tag{0.3}
\]

For distinct reflected points this is an off-diagonal hyperbolic block with
eigenvalues of opposite sign.  A positive kernel can therefore survive only
where \(s=t\), and (0.3) then gives \(\mathrm{Re}\,s=1/2\).

The perfect Witt contact changes determinant masses but not (0.2).  It
cannot turn the hyperbolic Tate pairing into a positive invariant metric.
Thus off-diagonal matrix cancellation supplies a Krein polarization, not
the required Hilbert polarization.  No paper file is modified.

## 1. The three-component source module

The finite-rank nuclear module used by A has the form

\[
 \mathcal N=\mathcal C e_1\oplus\mathcal C e_2
             \oplus\mathcal C e_\Gamma.                    \tag{1.1}
\]

The first two summands are the two rulings.  After the central half-Tate
normalization their scale characters are \(-1/2\) and \(+1/2\).  The third
summand carries the completed Frobenius/correspondence action; under Mellin
transform its generator is multiplication by \(s-1/2\).  Hence the action
is

\[
 U_u=\mathrm{diag}
 \left(e^{-u/2},e^{u/2},e^{uD_\Gamma}\right).              \tag{1.2}
\]

Let \(W=(W_{ij})_{1\le i,j\le3}\) be a Hermitian
operator-valued metric on a common invariant core.  Exact central
conservation is

\[
 U_u^*WU_u=W\qquad(u\in\mathbb R).                         \tag{1.3}
\]

Differentiating (1.3) at zero gives (0.2); conversely (0.2) integrates to
(1.3) on the analytic core.

## 2. Block equations

Writing out (0.2) gives

\[
 \begin{array}{rclcrcl}
 -W_{11}&=&0, && W_{22}&=&0,\\
 (-\tfrac12+\tfrac12)W_{12}&=&0,&&
 W_{13}D_\Gamma-\tfrac12W_{13}&=&0,\\
 W_{23}D_\Gamma+\tfrac12W_{23}&=&0,&&
 D_\Gamma^*W_{33}+W_{33}D_\Gamma&=&0.
 \end{array}                                             \tag{2.1}
\]

Thus \(W_{12}\) is unrestricted by scaling and is precisely the Tate
hyperbolic pairing between the two rulings.  The mixed ruling--correspondence
blocks can be supported only at the polar characters:

\[
 W_{13}:s=1,qquad W_{23}:s=0.                              \tag{2.2}
\]

They do not couple the rulings to a nontrivial correspondence parameter.

If \(W\ge0\), then \(W_{11}=0\) implies \(W_{1j}=0\) for every \(j\).
Indeed positivity and Cauchy--Schwarz give

\[
 |\langle x,W_{1j}y\rangle|^2
 \le\langle x,W_{11}x\rangle\langle y,W_{jj}y\rangle=0.  \tag{2.3}
\]

The same argument with \(W_{22}=0\) kills the second row and column.
Therefore a positive invariant weight is necessarily

\[
 W=0\oplus0\oplus W_{33}.                                 \tag{2.4}
\]

It is not faithful on the full three-component module.  Passing to the
primitive quotient legitimately removes the two ruling directions, but it
leaves the correspondence equation in (2.1), which is row D's real content.

## 3. Kernel form of the correspondence equation

Represent \(W_{33}\) by an operator-valued distribution kernel \(K(s,t)\).
The last equation of (2.1) reads

\[
 (\bar s+t-1)K(s,t)=0.                                    \tag{3.1}
\]

Hence

\[
 \mathrm{supp}\,K\subseteq\{(s,t):t=1-\bar s\}.      \tag{3.2}
\]

This is exactly the functional-equation/Tate reflection.  It exists
unconditionally and yields a nondegenerate indefinite pairing.

Suppose \(s\ne1-\bar s\) and restrict to the two-dimensional fiber spanned
by the reflected pair.  Since (3.2) permits only cross terms, the Hermitian
matrix is

\[
 \begin{pmatrix}0&c\\\bar c&0\end{pmatrix},              \tag{3.3}
\]

whose eigenvalues are \(\pm|c|\).  It is positive semidefinite only when
\(c=0\).  Equivalently, the general fact used in (2.3) says that a positive
kernel with zero diagonal cannot have a nonzero off-diagonal value.

A nonzero positive invariant kernel can therefore be supported only on the
intersection of the reflection graph with the diagonal:

\[
 s=t=1-\bar s
 \quad\Longleftrightarrow\quad\mathrm{Re}\,s=\tfrac12. \tag{3.4}
\]

This conclusion is derived from the source scaling law and positivity; no
zero is used to define \(W\).

## 4. The role of the perfect B contact

For \(n>1\), row B constructs

\[
 K_n^W\simeq[\mathbb Z\xrightarrow{\Phi_n(1)}\mathbb Z]    \tag{4.1}
\]

from the Witt characteristic, and its torsion determinant has mass

\[
 -\log|\det_{\rm tor}K_n^W|=\Lambda(n).                    \tag{4.2}
\]

Tensoring (1.1) with (4.1), or using its determinant line as a coefficient,
does not change the scale exponents in (0.1).  The Lyapunov equation on each
finite perfect summand is still (0.2).  Since (4.1) becomes acyclic after
tensoring with \(\mathbb C\), it supplies no new positive complex Hilbert
fiber on which the missing diagonal of \(W\) could live.

Thus the contact is essential for the arithmetic trace, but it cannot
repair the positivity obstruction of Sections 2--3.

## 5. Determinant/trace compatibility

Assume nevertheless that a positive, faithful \(W\) satisfying (1.3)
existed on the primitive correspondence quotient and that Hilbert traces
agreed with row C.  The integrated action would obey

\[
 \mathscr Q_-(a^\vee)=\mathscr Q_-(a)^{*W}.                \tag{5.1}
\]

For primitive \(a\), D.191 would give

\[
 B_{\rm nuc}(a,a)
 =-\mathrm{Tr}_W\bigl(
 \mathscr Q_-(a)\mathscr Q_-(a)^{*W}\bigr)\le0.           \tag{5.2}
\]

Therefore the desired positive solution of (0.2), with trace compatibility,
is exactly a row-D polarization.  The block analysis shows that the ruling
and contact decorations do not make it automatic.

## 6. What off-diagonal cancellation does provide

Dropping positivity, one may take

\[
 W_{\rm Tate}=
 \begin{pmatrix}0&1&0\\1&0&0\\0&0&W_\Gamma^{\rm refl}\end{pmatrix}, \tag{6.1}
\]

where \(W_\Gamma^{\rm refl}\) is supported on (3.2).  This solves the
Lyapunov equation and encodes the functional equation.  Every noncentral
reflected pair contributes one positive and one negative direction.  Hence
(6.1) is the natural Krein/symplectic metric already present in A--B--C,
not the Hodge metric required in D.

The distinction is sharp:

\[
 \text{off-diagonal reflection}\Rightarrow\text{functional equation},
 \qquad
 \text{positive diagonal reflection}\Rightarrow\text{critical line}. \tag{6.2}
\]

## 7. Next source test

The failure of a static three-component weight does not exclude positivity
arising from a larger source dilation.  The next admissible candidate is the
Witt/Fock module in which

\[
 V_n\phi_r=\phi_{nr}                                     \tag{7.1}
\]

is an actual isometry before Poisson descent.  One must test whether the
defect indices of these isometries, the central torsor, and the perfect
contact reproduce \(\Lambda(n)\), the Gamma term and the complete
\(B_{\rm nuc}\) form without converting (6.1) into a spectral positive
part.  This is carried out in D.194.

## 8. Finite certificate

The companion script `114_d_193_three_component_lyapunov_verify.py` checks:

1. the exact Lyapunov support rule
   \(\bar\alpha_i+\alpha_j=0\);
2. the ruling and reflected-pair invariant blocks;
3. their opposite eigenvalues;
4. positivity only for central exponents \(\mathrm{Re}\,\alpha=0\).
