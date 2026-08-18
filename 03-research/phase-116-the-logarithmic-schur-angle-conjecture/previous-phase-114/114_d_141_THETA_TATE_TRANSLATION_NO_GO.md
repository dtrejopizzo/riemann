# D.141 — No Frobenius-equivariant transport from the theta boundary plane to the Tate plane

## Verdict

The two-dimensional defect of the positive theta quotient in D.140 cannot
be identified naturally with the two A--B--C Tate moments.  The obstruction
is representation-theoretic and already appears for one nontrivial
translation.

The Tate plane is invariant under every logarithmic translation:

\[
 M_\pm(S_aF)=e^{\pm a/2}M_\pm(F).                     \tag{0.1}
\]

Thus, at \(a=k\log p\), it carries exactly the two Frobenius characters
\(p^{\pm k/2}\).

The theta defect plane is represented by

\[
 \mathcal B_\Theta=\operatorname{span}\{k,Dk\},
 \qquad \widehat k=\Xi/2.                             \tag{0.2}
\]

It is not invariant under \(S_a\) for any \(a\ne0\).  Indeed, invariance
would make \(k\) satisfy a nontrivial second-order constant-coefficient
difference equation.  Fourier transformation would then give

\[
 P(e^{ia\tau})\Xi(\tau)=0\quad\text{a.e.}             \tag{0.3}
\]

for a nonzero polynomial \(P\).  Since \(\Xi\ne0\) almost everywhere and
\(e^{ia\tau}\) runs around the unit circle, (0.3) is impossible.

Therefore

\[
 \boxed{\mathcal B_\Theta\not\simeq\mathcal B_{\rm Tate}
 \quad\text{as a }\mathbb N^\times\text{-module}.}    \tag{0.4}
\]

An abstract isomorphism between two two-dimensional vector spaces can
always be chosen, but it cannot intertwine even \(\Gamma_2\), much less all
\(\Gamma_{p^k}\) and the Gamma/Poisson assembly.  The theta quotient route
cannot construct the support-compatible contraction of D.137.

No zero location is used.  The paper is not modified.

## 1. Translation covariance of the Tate moments

Use

\[
 (S_aF)(x)=F(x-a).                                    \tag{1.1}
\]

For

\[
 M_s(F)=\int_{\mathbb R}e^{sx}F(x)\,dx,\qquad
 s=\pm\tfrac12,                                      \tag{1.2}
\]

a change of variables gives

\[
 M_s(S_aF)=e^{sa}M_s(F).                              \tag{1.3}
\]

Consequently the primitive test space

\[
 \mathcal P=\ker M_{-1/2}\cap\ker M_{1/2}             \tag{1.4}
\]

is translation invariant.  On the quotient dual plane, \(S_a\) is the
diagonal matrix

\[
 \begin{pmatrix}e^{-a/2}&0\\0&e^{a/2}\end{pmatrix}.   \tag{1.5}
\]

For \(a=k\log p\), (1.5) is precisely
\(\operatorname{diag}(p^{-k/2},p^{k/2})\).  This is the metric
normalization already shared by rows A, B and C.

## 2. The theta defect plane

Let

\[
 k(x)=\varTheta_{00}(ie^{2x}),\qquad D=-i\partial_x.  \tag{2.1}
\]

D.139 proved

\[
 k\in\mathcal S(\mathbb R),\quad k>0,\quad
 \widehat k(\tau)={1\over2}\Xi(\tau),                 \tag{2.2}
\]

and D.140 proved that the quotient-pair defect is represented by the two
functionals with Riesz vectors \(k,Dk\).  Thus

\[
 \mathcal B_\Theta=\operatorname{span}\{k,Dk\}
 \subset L^2(\mathbb R).                              \tag{2.3}
\]

The two vectors are linearly independent.  Otherwise \(Dk=ck\), so \(k\)
would be an exponential; no nonzero exponential belongs to the Schwartz
class on the whole line.

## 3. No nontrivial translation preserves the theta plane

Assume for contradiction that \(S_a\mathcal B_\Theta\subset
\mathcal B_\Theta\) for some \(a\ne0\).  Since \(S_a\) is invertible and
\(\mathcal B_\Theta\) is finite-dimensional, equality holds.  Let \(A_a\)
be the resulting \(2\times2\) matrix.

Cayley--Hamilton gives

\[
 A_a^2-(\operatorname{tr}A_a)A_a
       +(\det A_a)I=0.                                \tag{3.1}
\]

Applying (3.1) to \(k\) yields

\[
 S_{2a}k-(\operatorname{tr}A_a)S_ak
       +(\det A_a)k=0.                                \tag{3.2}
\]

With the Fourier convention of D.139,

\[
 \widehat{S_ak}(\tau)=e^{-ia\tau}\widehat k(\tau).    \tag{3.3}
\]

Hence (3.2) becomes

\[
 \left(e^{-2ia\tau}
 -(\operatorname{tr}A_a)e^{-ia\tau}
 +\det A_a\right)\Xi(\tau)=0
 \quad\text{for a.e. }\tau.                           \tag{3.4}
\]

The real zeros of the nonzero entire function \(\Xi\) form a discrete set,
so they have measure zero.  Therefore the quadratic polynomial

\[
 P(z)=z^2-(\operatorname{tr}A_a)z+\det A_a            \tag{3.5}
\]

vanishes at \(z=e^{-ia\tau}\) for almost every real \(\tau\).  Those values
fill the unit circle, forcing \(P\equiv0\).  This contradicts the leading
coefficient \(1\).  Thus

\[
 S_a\mathcal B_\Theta\not\subset\mathcal B_\Theta
 \qquad(a\ne0).                                      \tag{3.6}
\]

The argument needs only one translation; no incommensurability of
\(\log2\) and \(\log3\) is required.

## 4. Dual-plane formulation

The theta boundary functionals are

\[
 b_0(u)=\langle u,k\rangle,\qquad
 b_1(u)=\langle u,Dk\rangle.                          \tag{4.1}
\]

Their transforms under source translation are represented by
\(S_{-a}k,S_{-a}Dk\).  If a two-dimensional quotient carrying these
functionals were translation covariant, the span of those representing
vectors would have to be invariant.  Section 3 excludes this.

By contrast, the Tate functionals (1.2) are distributional eigenvectors of
the translation dual.  Their plane is a genuine two-character quotient.
This remains true after restricting to compactly supported smooth tests.

Thus the failure is not caused by choosing vectors instead of functionals;
it is intrinsic to their semigroup representations.

## 5. Gamma does not repair the mismatch

The theta vector already contains the archimedean Gamma factor through its
Mellin transform and the integer dilation sum through the Jacobi series.
What it does not retain is a two-dimensional subquotient on which each
individual \(p^k\) acts by its two central characters.

Adding the Gamma screw to both sides cannot change (3.6): the contradiction
uses the action of a single finite correspondence \(\Gamma_{p^k}\).
Similarly, passing from \(k\) to the pair \(k,Dk\) already includes the
first logarithmic jet; any finite number of derivatives would give a
finite-dimensional translate-invariant span and the same
Cayley--Hamilton contradiction of higher degree.

## 6. Consequence for the active construction

D.140 reduced the theta quotient to a finite boundary mismatch.  D.141
shows that this mismatch cannot be repaired by a natural symplectic
identification compatible with row B:

\[
 \text{theta quotient boundary}
 \;\not\longrightarrow\;
 \text{Tate primitive boundary}
 \quad\text{equivariantly}.                           \tag{6.1}
\]

Therefore the contraction

\[
 C_TX_T=Y_T                                           \tag{6.2}
\]

must be constructed directly from the periodic--Witt--Poisson feature
system \(X_T,Y_T\), where the \(p^k\) labels remain separate.  The Jacobi
theta sum is useful as a scalar spectral package, but it has already
collapsed the individual Frobenius module structure needed for (6.2).

This removes the theta transport from the live route without changing the
completed comparison of D.137.
