# D.251 — The unitary transfer-defect theorem and the final comparison map

## Verdict

Once a conservative source network is realized as a unitary colligation,
positivity of its transfer-defect kernel is an algebraic identity.  Cascades
and orthogonal sums preserve the identity.  D.247--D.249 construct the local
conservative components that could supply this mechanism.  They do **not**
yet construct the particular balanced Redheffer wiring whose transfer
symbol is the full row-D score.

The remaining row-D theorem is not another estimate: it is the comparison
that identifies the D.190 supported Schur residual with a compression of
this transfer-defect kernel.

## 1. Unitary colligation identity

Let

\[
 \mathcal U=
 \begin{pmatrix}A&B\\C&D\end{pmatrix}:
 \mathcal X\oplus\mathcal E\longrightarrow
 \mathcal X\oplus\mathcal E
\]

be unitary, and define

\[
 S(z)=D+zC(I-zA)^{-1}B,\qquad |z|<1.               \tag{1.1}
\]

Then

\[
 \boxed{
 {I-S(w)^*S(z)\over1-\bar wz}
 =
 B^*(I-\bar wA^*)^{-1}(I-zA)^{-1}B.
 }                                                   \tag{1.2}
\]

In particular the kernel on the left is positive and

\[
 I-S(z)^*S(z)
 =(1-|z|^2)
 B^*(I-\bar zA^*)^{-1}(I-zA)^{-1}B\ge0.            \tag{1.3}
\]

### Proof

Unitarity gives

\[
 A^*A+C^*C=I,\quad B^*B+D^*D=I,\quad A^*B+C^*D=0.
\]

Insert (1.1) into \(I-S(w)^*S(z)\), use these relations, and collect the
resolvents.  The numerator factors as

\[
 (1-\bar wz)B^*(I-\bar wA^*)^{-1}
 (I-zA)^{-1}B,
\]

which proves (1.2).

## 2. Compression and Douglas

Compress the positive kernel (1.2) to orthogonal input subspaces
\(P_O\mathcal E\oplus P_E\mathcal E\).  Its block matrix

\[
 \begin{pmatrix}
 K_{OO}&K_{OE}\\K_{EO}&K_{EE}
 \end{pmatrix}\ge0
\]

automatically satisfies

\[
 \mathrm{Ran}\,K_{OE}\subseteq
 \mathrm{Ran}\,K_{OO}^{1/2},\qquad
 K_{EE}-K_{EO}K_{OO}^\dagger K_{OE}\ge0.           \tag{2.1}
\]

Equivalently there is a contraction \(\Theta\) with

\[
 K_{OE}=K_{OO}^{1/2}\Theta K_{EE}^{1/2}.            \tag{2.2}
\]

The supported-range condition comes from the same positive block and is
not separately assumed.

## 3. Stability of conservative components

Orthogonal sums of unitary colligations are unitary.  Cascades are
Redheffer products of their unitary system matrices and remain unitary
after the internal port is eliminated.  The following conservative
components have been constructed:

* the prime Julia systems of D.248;
* the archimedean Blaschke systems of D.249;
* the degree/contact partial isometry of D.247, after its canonical unitary
  dilation.

Their orthogonal sum is a unitary colligation and consequently has a
positive transfer-defect kernel with sharp constant one.  This statement
only gives the orthogonal sum of the local kernels.  It does not identify
the feedback ports that combine degree, contact, prime score and Gamma
score into the balanced D.137 form.  Constructing that specific Redheffer
wiring, while keeping the renormalized Gamma free-delay differences paired,
is part of the open comparison theorem.

## 4. The exact comparison still required

Let \(K_S^{\rm tr}\) denote the transfer-defect kernel of the **proposed
balanced wired network, once that wiring has been constructed**, and let

\[
 \mathscr R_E^{\rm D190}
 =B_E-X_{OE}^*A_O^\dagger X_{OE}.                  \tag{4.1}
\]

D.245--D.246 prove equality of the uncompressed first-order local symbols.
D.190 proves that \(X_{OE}\) is the exact support commutator.  Two things
are not yet proved: construction of the balanced wiring with full score
symbol, and the state-elimination identity

\[
 \boxed{
 \mathscr R_E^{\rm D190}
 =
 P_E\Pi_TK_S^{\rm tr}\Pi_TP_E,
 }                                                   \tag{4.2}
\]

with the old state and the two Tate ports eliminated in the same order.

If (4.2) holds, (1.2)--(2.2) prove D.190(0.3), including the range
condition.  If it fails, the exact remaining residual is

\[
 \mathscr R_E^{\rm D190}
 -P_E\Pi_TK_S^{\rm tr}\Pi_TP_E.                    \tag{4.3}
\]

No norm estimate should precede computation of (4.3).

## 5. Domain protocol

Prove the comparison first for a finite prime set, a finite paired Gamma
truncation, \(A_O+\varepsilon I\), and compactly supported smooth primitive
vectors.  Then take, in order:

1. the Gamma monotone form limit;
2. \(\varepsilon\downarrow0\);
3. closure of the compact form core;
4. the directed support-window limit.

Monotone convergence of the positive transfer kernels then supplies the
supported-range statement.  Reversing the order risks applying the
pseudoinverse outside its proved domain.

## 6. Classification

* Unitary transfer-defect formula (1.2): **PROVED**.
* Sharp Douglas consequence (2.1)--(2.2): **PROVED**.
* Stability under finite sums/cascades: **PROVED STANDARD ALGEBRA**.
* Conservative local components and their orthogonal sum:
  **CONSTRUCTED IN D.247--D.249**.
* Balanced Redheffer wiring realizing the full row-D score: **OPEN**.
* Uncompressed first-order score comparison: **PROVED IN D.245--D.246**.
* State-elimination identity (4.2): **OPEN**.
* Row D: **OPEN**.
