# 106.178 — Julia super-Hodge colligation and the descent equation

## 1. Purpose

Document 106.177 identifies the complete-return middle amplitude as the
defect operator of a self-adjoint contraction.  This determines a
canonical off-diagonal Hodge operator: the Julia colligation of that
contraction.

The present note constructs this operator, proves its polarization and
scaling properties, and shows that its first-channel compression is
exactly the signed arithmetic return correlation.  Thus the required
mixing of the odd return sector with the even generic sector is no longer
an ansatz.

The final descent question is also computed exactly.  The physical CCM
class enters initially through the first channel, which is not preserved
by the new Hodge star.  A polarized descent is therefore equivalent to a
specific graph/Riccati identity for the CCM restriction range.  No such
identity is assumed below.

## 2. The normalized complete-return contraction

Use the notation of 106.177.  For a finite symmetric return system put

\[
 T_I=C_I^{-1}A_I.                                           \tag{1}
\]

Since \(A_I=A_I^*\), the operator \(T_I\) is self-adjoint.  Moreover,

\[
 \|T_I\|
 \le C_I^{-1}\sum_iw_i\|U_i\|=1.                          \tag{2}
\]

Define its defect amplitude

\[
 D_I=(I-T_I^2)^{1/2}.                                      \tag{3}
\]

The two operators commute.  The variance identity 106.177(13) becomes

\[
 \boxed{
 \|P_I^{\rm mid}\Psi_If\|^2
 =\frac{C_I}{2}\|D_If\|^2.}                               \tag{4}
\]

Thus \(D_I\) is the literal full-return middle amplitude.

## 3. The canonical off-diagonal involution

On \(H\oplus H\) define

\[
 \boxed{
 S_I=
 \begin{pmatrix}
 T_I&D_I\\
 D_I&-T_I
 \end{pmatrix}.}                                           \tag{5}
\]

### Theorem 3.1 — Julia involution

The operator \(S_I\) is self-adjoint and unitary:

\[
 \boxed{S_I^*=S_I,\qquad S_I^2=I.}                         \tag{6}
\]

If a unitary representation \(V_a\) on \(H\) commutes with every return
\(U_i\), then \(S_I\) commutes with \(V_a\oplus V_a\).

#### Proof

Self-adjointness is immediate from (1)--(3).  Since \(T_ID_I=D_IT_I\),

\[
 S_I^2=
 \begin{pmatrix}
 T_I^2+D_I^2&T_ID_I-D_IT_I\\
 D_IT_I-T_ID_I&D_I^2+T_I^2
 \end{pmatrix}=I.                                         \tag{7}
\]

Functional calculus shows that any operator commuting with \(T_I\) also
commutes with \(D_I\), proving the last statement. \(\square\)

## 4. The finite super-Hodge polarization

Take the complex Hilbert inner product to be linear in the first
variable.  Define the Hermitian Krein form

\[
 \mathfrak k_I(v,w)=-C_I\langle S_Iv,w\rangle              \tag{8}
\]

and its underlying real alternating form

\[
 \Omega_I(v,w)=-\mathrm{Im}\,\mathfrak k_I(v,w).
                                                                    \tag{9}
\]

Put

\[
 \boxed{\mathcal J_I=-iS_I.}                               \tag{10}
\]

### Theorem 4.1 — Positive compatible Hodge star

The triple \((\Omega_I,\mathcal J_I,g_I)\), where

\[
 g_I(v,w)=\Omega_I(v,\mathcal J_Iw),                       \tag{11}
\]

satisfies

\[
 \boxed{
 \mathcal J_I^2=-I,
 \quad
 \Omega_I(\mathcal J_Iv,\mathcal J_Iw)=\Omega_I(v,w),
 \quad
 g_I(v,w)=C_I\mathrm{Re}\,\langle v,w\rangle.}       \tag{12}
\]

In particular \(g_I\) is positive definite.  The star commutes with every
common scaling operator \(V_a\oplus V_a\) from Theorem 3.1.

#### Proof

Equation (6) gives \(\mathcal J_I^2=-I\).  It also gives

\[
 \mathfrak k_I(\mathcal J_Iv,\mathcal J_Iw)
 =\mathfrak k_I(v,w),                                      \tag{13}
\]

which proves symplectic invariance after taking imaginary parts.  Finally,

\[
 \begin{aligned}
 \mathfrak k_I(v,\mathcal J_Iw)
 &=-C_I\langle S_Iv,-iS_Iw\rangle\\
 &=-iC_I\langle v,w\rangle.
 \end{aligned}                                             \tag{14}
\]

Taking minus the imaginary part proves (12). \(\square\)

This is a genuine positive Hodge structure assembled only from the real
return unitaries and their positive weights.

## 5. Exact compression to the arithmetic correlation

Let \(\iota_0:H\to H\oplus H\) be \(\iota_0f=(f,0)\).  Then

\[
 \boxed{
 \mathfrak k_I(\iota_0f,\iota_0g)
 =-\langle A_If,g\rangle.}                                 \tag{15}
\]

#### Proof

The first component of \(S_I(f,0)\) is \(T_If\).  Hence (8) gives

\[
 -C_I\langle T_If,g\rangle=-\langle A_If,g\rangle.
\]
\(\square\)

For the ordinary-prime return system (20) of 106.177, the right side of
(15) is precisely

\[
 -\sum_{p,k\ne0}(\log p)p^{-|k|/2}
   \langle U_p^kf,g\rangle,                                \tag{16}
\]

the signed finite-place correlation in the completed explicit formula.
Thus the arithmetic sign is a compression of an unconditional polarized
object.  It is not inserted into the positive metric (12).

## 6. Why compression is not yet descent

The first channel is not Hodge-stable:

\[
 \mathcal J_I\iota_0f
 =-i(T_If,D_If).                                             \tag{17}
\]

The second component vanishes only on the unitary part
\(\ker(I-T_I^2)\).  Therefore (15) alone does not transport the positive
metric (12) to the CCM quotient.

Let \(K\) be a closed operator on a common invariant core and consider
the graph map

\[
 \iota_Kf=(f,Kf).                                           \tag{18}
\]

### Theorem 6.1 — Exact Hodge graph equation

The graph of \(K\) is invariant under \(\mathcal J_I\) if and only if

\[
 \boxed{
 D_I-T_IK=K(T_I+D_IK).}                                    \tag{19}
\]

If \(K\) strongly commutes with \(T_I\), the two extremal solutions are

\[
 \boxed{
 K_+=(I-T_I)D_I^\dagger,
 \qquad
 K_-=-(I+T_I)D_I^\dagger,}                                \tag{20}
\]

on the corresponding defect domains.  Their graphs are the \(+1\) and
\(-1\) eigenspaces of \(S_I\), respectively.

#### Proof

Applying \(S_I\) to \((f,Kf)\) gives

\[
 (T_If+D_IKf,\ D_If-T_IKf).                                \tag{21}
\]

It lies in the graph of \(K\) exactly when the second component equals
\(K\) applied to the first, which is (19).  For commuting \(K\), the
scalar functional calculus reduces (19) at \(t\in[-1,1]\) to

\[
 d-tk=k(t+dk),\qquad d=\sqrt{1-t^2}.                        \tag{22}
\]

Its two invariant graph solutions are \(k=(1-t)/d\) and
\(k=-(1+t)/d\), interpreted with the Moore--Penrose inverse at the
endpoints.  Substitution in (21) gives eigenvalues \(+1\) and \(-1\).
\(\square\)

## 7. The remaining chain identity

Let \(d_{\rm CCM}\) be the cyclic restriction differential and let
\(\mathrm{Loc}_I\) be the full-return localization through the
prime, Gamma, and polar pages.  The Julia construction descends to a
positive Hodge structure on CCM degree one if one can construct a second
component \(K_I\mathrm{Loc}_I\) satisfying both

\[
 \boxed{
 \begin{aligned}
 D_I-T_IK_I&=K_I(T_I+D_IK_I),\\
 \mathrm{Loc}_I(\overline{\mathrm{Ran}\,d_{\rm CCM}})
 &\subseteq
 \ker\bigl[(f,K_If)\bigr]
 \quad\text{in the relative graded quotient}.
 \end{aligned}}                                            \tag{23}
\]

The first line is the exact Hodge invariance equation.  The second is the
chain descent equation.  In addition, the pullback of \(\Omega_I\) must
equal the CCM residue alternating form.  These are algebraic equalities;
no norm estimate is hidden in their statement.

The canonical candidates (20) show that the star itself is no longer
missing.  What remains is **arithmetic branch descent**: the CCM
restriction cone must select one of the two invariant Julia graphs in a
way compatible with Gamma and the polar plane.  Selecting a graph merely
by declaring a sign would not prove (23).

### 7.1 The Fourier odd graph solves the Riccati equation

There is an unconditional solution before the nonreduced quotient is
taken.  Double the coefficient space once more and put

\[
 \widehat T_I=
 \begin{pmatrix}T_I&0\\0&-T_I\end{pmatrix}.                \tag{23a}
\]

Let \(F=F^*=F^{-1}\) be the normalized additive Fourier involution.  On
the symmetric return channel, Fourier exchanges \(U_i\) and \(U_i^*\),
so \(FT_I=T_IF\).  Define

\[
 \mathcal F_{\rm odd}
 =\begin{pmatrix}0&F\\F&0\end{pmatrix}.                    \tag{23b}
\]

Then

\[
 \boxed{
 \mathcal F_{\rm odd}^2=I,
 \qquad
 \mathcal F_{\rm odd}\widehat T_I
 =-\widehat T_I\mathcal F_{\rm odd}.}                      \tag{23c}
\]

Since the defect
\(\widehat D_I=(I-\widehat T_I^2)^{1/2}\) commutes with
\(\mathcal F_{\rm odd}\), equation (23c) gives

\[
 \begin{aligned}
 \widehat D_I-\widehat T_I\mathcal F_{\rm odd}
 &=\mathcal F_{\rm odd}
   (\widehat T_I+\widehat D_I\mathcal F_{\rm odd}).
 \end{aligned}                                             \tag{23d}
\]

Thus the Fourier odd graph is an exact solution of the Hodge graph
equation (19), for every finite cutoff and with all return phases kept.
Poisson summation makes the doubled CCM restriction range invariant under
this graph operation.

This closes the **algebraic** graph equation, but not the last line of
(23) in the nonreduced category.  It is precisely the Fourier-doubled
relative complex of 106.155--106.156 in the Julia coordinate.  Its Hilbert
quotient uses the closure of the restriction range and therefore loses
the distributional CCM degree one.  Consequently (23d) must not be
reported as the global polarization theorem: the remaining issue is the
torsion-sensitive metric descent, not the Riccati identity.

## 8. Cofinal normalization

For primes \(p\le X\), the complete-return mass satisfies

\[
 C_X=4\sqrt X+o(\sqrt X).                                  \tag{24}
\]

The first-return part of the Mellin multiplier of \(T_X\) at frequency
\(t\) is

\[
 \mathrm{Re}
 \frac{e^{it\log X}}{1+2it}+o(1),                          \tag{25}
\]

locally uniformly for fixed \(t\), by partial summation and the prime
number theorem; higher returns contribute \(o(C_X)\).  Thus the symmetric
contraction does not have a pointwise cofinal limit without retaining the
two orientations.  On the one-sided orientation, removal of the moving
phase \(e^{it\log X}\) gives the universal limit

\[
 \frac1{1+2it}.                                             \tag{26}
\]

This is the Cauchy/exponential coefficient already present in 106.154.
It proves that the leading cofinal Julia star is universal.  The arithmetic
information needed for (23) is in the jointly renormalized finite part,
not in the leading normalized contraction.

## 9. Status

Proved without RH or zero input:

* the canonical Julia involution attached to all real prime returns;
* a positive compatible Hodge star commuting with common scaling;
* exact compression to the signed von Mangoldt correlation;
* the exact graph/Riccati equation for Hodge-stable descent;
* the two canonical invariant graph branches;
* the Fourier odd solution of the graph equation and its exact relation
  to the earlier Fourier--Poisson complex;
* the PNT cofinal normalization and its universal Cauchy limit.

Still required:

* prove the torsion-sensitive chain descent and residue-pairing identities
  in (23) after Gamma and the polar plane are included;
* prove that the selected graph survives the cofinal finite part on the
  full CCM nuclear cokernel.

The positive off-diagonal star has been constructed.  The unresolved
statement is now its arithmetic descent, not its operator-theoretic
existence.
