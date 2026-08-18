# D.98 — Tate boundary nodes, Markov transform and the exact gap

## Status

The positive prime--Gamma operator `L_T` is a continuous graph Laplacian:
its edges are the translations `log n` with conductance
`Lambda(n)/sqrt(n)` and the continuum of Gamma translations with positive
conductance density.  This note tests whether the two Tate moments can be
implemented as genuine boundary nodes so that a positive Schur complement
automatically yields the shifted operator `L_T-m_T I`.

They cannot.  The universal positive boundary attachment has Schur
complement exactly `L_T`; on the kernel of the boundary trace, both the
Dirichlet and Neumann reductions also give `L_T`.  The negative scalar mass
is not created by the two nodes.  Inserting it in the bulk before taking
the complement makes positivity equivalent to the desired gap.

A Doob transform does not supply the mass either.  On a connected
conservative Markov graph a strictly positive eigenfunction has eigenvalue
zero and is constant.  The two Tate exponentials are non-`L^2` boundary
jets, not positive ground states of the prime--Gamma generator; the Gamma
energy has a pole at their exponent.  Passing to a killed process requires
constructing a new positive ground state with eigenvalue `m_T`, which is
again the missing spectral-gap theorem.

Finite models show that two moment constraints alone do not force an
arbitrary prescribed mass.  Thus the boundary-node/ground-state route
does not prove D without an additional geometric inequality.

No RH statement or desired gap is assumed.  The paper is not modified.

## 1. The positive jump Laplacian

On a support window, with zero extension, write

\[
\begin{aligned}
 \mathcal E_T(f,g)={}&
 \sum_{2\le n\le e^{2T}}{\Lambda(n)\over\sqrt n}
 \langle f-S_{\log n}f,g-S_{\log n}g\rangle\\
 &+\int_0^\infty {e^{-r/2}\over1-e^{-2r}}
 \langle f-S_rf,g-S_rg\rangle dr.                         \tag{1.1}
\end{aligned}
\]

It is a closed positive Markov form on the finite window after the usual
domain closure.  Denote its operator by `L_T`.  The completed Weil/Pick
operator is

\[
 A_T=L_T-m_TI+M_T^*CM_T,
 \qquad C=\begin{pmatrix}0&1\\1&0\end{pmatrix},            \tag{1.2}
\]

where

\[
 M_Tf=(\langle e^{-t/2},f\rangle,
       \langle e^{t/2},f\rangle).                          \tag{1.3}
\]

On `ker M_T`, row D is exactly

\[
 \mathcal E_T(f,f)\ge m_T\|f\|^2.                        \tag{1.4}
\]

## 2. Universal positive boundary attachment

Let `H` be any Hilbert space, `L>=0` a graph/Dirichlet operator,
`M:H->C^2` a boundary trace, and `R>0` a boundary conductance.  The most
general elementary positive attachment with boundary value `b` has energy

\[
 \mathcal A(f,b)=\langle f,Lf\rangle
 +\langle Mf-b,R(Mf-b)\rangle.                             \tag{2.1}
\]

Its block operator is

\[
 \mathbf A=
 \begin{pmatrix}
 L+M^*RM&-M^*R\\
 -RM&R
 \end{pmatrix}\ge0.                                      \tag{2.2}
\]

The Schur complement of the boundary block is

\[
 \begin{aligned}
 \mathbf A/R
 &=(L+M^*RM)-M^*R R^{-1}RM\\
 &=L.                                                      \tag{2.3}
 \end{aligned}
\]

Thus eliminating a free boundary value returns the original Laplacian.
Imposing the Dirichlet value `b=0` gives `L+M^*RM`; after restriction to
`ker M` this also equals `L`.  Neither operation produces `L-mI`.

If the shifted bulk is inserted,

\[
 \mathbf A_m=
 \begin{pmatrix}
 L-mI+M^*RM&-M^*R\\
 -RM&R
 \end{pmatrix},                                          \tag{2.4}
\]

then

\[
 \mathbf A_m/R=L-mI.                                     \tag{2.5}
\]

But positivity of (2.4) is equivalent, by the positive Schur-complement
criterion, to `L-mI>=0` on the relevant source.  Hence (2.4) packages the
gap; it does not prove it.

The actual Tate metric `C` in (1.2) is indefinite.  Replacing `R` by `C`
can reproduce the crossed rank-two correction, but the ambient boundary
space then has inertia `(1,1)` and ceases to be a positive Markov/Calderon
system.  This is exactly the Krein construction of D.86 and D.95.

## 3. Doob-transform test

For a weighted conservative graph Laplacian

\[
 (Lh)(x)=\sum_yw_{xy}(h(x)-h(y)),\qquad w_{xy}=w_{yx}\ge0,
                                                                    \tag{3.1}
\]

suppose `h>0` and `Lh=lambda h`.  Summing over vertices gives

\[
 0=\sum_x(Lh)(x)=\lambda\sum_xh(x).                       \tag{3.2}
\]

Therefore `lambda=0`; connectedness then makes `h` constant.  A positive
Doob ground-state transform of a conservative graph cannot create a
positive spectral shift `m`.

On the translation interior, a formal exponential satisfies

\[
 (2I-S_a-S_{-a})e^{\sigma t}
 =(2-2\cosh(\sigma a))e^{\sigma t},                       \tag{3.3}
\]

whose eigenvalue is nonpositive, not `m_T>0`.  At the Tate values
`sigma=plus-or-minus 1/2`, the Gamma analytic energy also hits the first
oscillator pole.  With the finite-window cutoff, boundary layers destroy
even the formal eigenvector identity.  Hence `e^(plus-or-minus t/2)` are
boundary/residue vectors, not Doob ground states.

A killed Markov process can have a positive ground-state eigenvalue, but
then a ground state `h_T` satisfying

\[
 L_Th_T=m_Th_T                                             \tag{3.4}
\]

must first be constructed.  Equation (3.4), with the exact value `m_T`
and compatibility with the two Tate traces, is the sharp gap in another
form.

## 4. First finite boundary model

With two interior vertices joined by one edge, two independent positive
moment vectors span the whole dual space.  Their common kernel is zero.
Any claimed two-moment inequality is therefore vacuous in the first
one-edge model; it cannot determine a mass.

The minimal nonvacuous example has three path vertices and two edges.  Put

\[
 L=\begin{pmatrix}
 1&-1&0\\-1&2&-1\\0&-1&1
 \end{pmatrix},
 \quad h_+=(1/2,1,2),
 \quad h_-=(2,1,1/2).                                     \tag{4.1}
\]

The common moment kernel is generated by

\[
 v=(1,-5/2,1),qquad
 \langle h_+,v\rangle=\langle h_-,v\rangle=0.             \tag{4.2}
\]

Its Rayleigh quotient is

\[
 {\langle v,Lv\rangle\over\langle v,v\rangle}
 ={49/2\over33/4}={98\over33}<3.                          \tag{4.3}
\]

Thus the same two exponential moments do not force the mass `m=3`, even
in the smallest nontrivial positive graph.  More generally, scaling or
changing the interior conductances changes the quotient while leaving the
two boundary functionals fixed.  Any exact value of `m_T` must come from a
specific global inequality for the arithmetic conductances, not from the
mere existence of two moments.

## 5. Boundary triplet/Weyl function

The boundary triplet of `(L_T,M_T)` has Weyl matrix

\[
 \mathcal W_T(\lambda)=M_T(L_T-\lambda)^{-1}M_T^*.         \tag{5.1}
\]

It is a matrix Herglotz function off the spectrum because `L_T` is
self-adjoint.  Asking that the primitive compression have no spectrum
below `m_T` is equivalent to requiring that the relevant Schur/Weyl
continuation have no pole before `m_T`, together with the finite-rank
boundary determinant condition.  This is the Birman--Schwinger reduction
already isolated in D.49--D.69; the boundary triplet does not locate those
poles by itself.

In particular, a DtN operator built from (5.1) reproduces `QW` only after
the shift `m_T` and the crossed Tate metric have been supplied.  Its
positivity then restates (1.4).

## 6. Outcome and next admissible pivot

Positive boundary nodes, Schur complementation, Doob transforms and
boundary triplets all preserve the source typing, but none creates the
exact completed mass.  The obstruction is now the sharp Poincare estimate
(1.4), not the construction of its boundary notation.

A further viable source-side route must exploit a special arithmetic
identity among **all** conductances, not a generic Markov theorem.  The
next audit is a Picone/ground-state-representation inequality using a
positive supersolution assembled from the Euler--Gamma heat kernels.  It
must be constructed without `Xi` zeros and must prove

\[
 (L_T-m_TI)\big|_{\ker M_T}\ge0.                           \tag{6.1}
\]

If its supersolution is defined by solving (3.4), by the lowest eigenvector
of the compressed operator, or from the completed zero divisor, the
argument is circular.

