# D.207 — Scalar-gap split invariance and the operator-Green pivot

## Verdict

The endpoint-flat \(M=60\) split controls the safe-to-tail capacity, but it
has not closed the full endpoint when the whole complement is replaced by
the single lower bound \(A_{QQ}\ge0.219I\).  Whether that scalar route works
is not a property of the chosen internal split: the strongest certificate
obtainable from the scalar lower bound is invariant under every internal
decomposition of the finite block.

Let \(V=V_{200}\cap\mathcal P_T\), \(Q=V^\perp\cap\mathcal P_T\), and

\[
 A=\begin{pmatrix}B&C^*\\C&A_{QQ}\end{pmatrix},
 \qquad H=C^*C.                                       \tag{0.1}
\]

If the only retained information about the high block is
\(A_{QQ}\ge\delta I\), then the optimal universal sufficient condition is

\[
 \boxed{B-\delta^{-1}H>0.}                            \tag{0.2}
\]

No choice \(V=D\oplus S\), endpoint-flat or otherwise, can strengthen
(0.2) without using additional information about \(A_{QQ}\).  The stable
full-FFT diagnostic gives 43 negative eigenvalues in (0.2), with minimum
about \(-5.326\), at \(\delta=0.219\).  This numerical statement is only a
route audit, not an interval theorem.  The same FFT chart has a high-mode
finite-compression mismatch of order one, caused by endpoint rectangle
aliasing.  Thus (3.1) cannot certify failure of the exact scalar-gap test; a
conforming or directed residual Gram is still required.

The correct next object is the operator-valued Green
\(C^*A_{QQ}^{-1}C\), or a certified multilevel approximation to it obtained
by enlarging the finite core.  No paper file is modified.

## 1. Optimality of the scalar-gap certificate

Completion of the square gives

\[
 A>0\quad\Longleftrightarrow\quad
 A_{QQ}>0\ \hbox{ and }\ B-C^*A_{QQ}^{-1}C>0.         \tag{1.1}
\]

From \(A_{QQ}\ge\delta I\), operator monotonicity of inversion gives
\(A_{QQ}^{-1}\le\delta^{-1}I\).  Hence (0.2) implies (1.1).

Conversely, the operator \(A_{QQ}=\delta I\) is compatible with precisely
the retained scalar information.  For that allowed high block, (1.1) is
exactly (0.2).  Therefore no theorem whose high-block hypothesis consists
only of \(A_{QQ}\ge\delta I\) can guarantee positivity when (0.2) fails.

## 2. Why an internal safe split cannot repair it

Write \(V=D\oplus S\).  Eliminating \(S\) first, as in D.200, is an exact
block congruence.  Eliminating \(Q\) first with the worst allowed Green
\(\delta^{-1}I\) gives (0.2), followed by the Schur complement of its
\(S\)-block.  Associativity of exact Schur complementation shows that both
orders have the same inertia whenever the eliminated blocks are positive.

Thus endpoint-flatness can make the safe capacity
\(\|C_S^*B_{SS}^{-1/2}\|^2\) small, but it cannot compensate for replacing
the Green seen by the remaining \(D\)-directions by \(\delta^{-1}I\).

## 3. Diagnostic at \(T=\tfrac12\log6\)

The converged binary64 residual Gram of D.203, in the finite eigenframe,
gives

\[
 \lambda_{\min}(B-H/0.219)\approx-5.32594,
 \qquad n_-(B-H/0.219)=43.                            \tag{3.1}
\]

Reconstructing the source-defined \(M=60\) safe space with exact Tate
constraints changes the misleading binary64 finite gap: the directed safe
compression has minimum about \(1.21\times10^{-8}\), not \(0.938\).  Its
full-FFT normalized capacity stabilizes near \(0.14717<0.219\).
Nevertheless, after safe elimination the
corrected low Schur diagnostic has minimum about \(-20.46\) and sixty
negative eigenvalues.  These observations suggest that non-flat directions,
rather than the safe-flat tail, are what a scalar Green may mishandle.  They
do not prove that conclusion because the FFT high-mode Gram is not directed.

Equation (3.1) does **not** prove that the true operator is indefinite, nor
even that the exact scalar-gap matrix fails.  It shows that this
nonconforming FFT implementation supplies no usable margin.  The next
calculation must either enclose the exact residual Gram or retain the true
high operator, which is much larger than \(0.219I\) on many coupled
directions.

## 4. Source-defined multilevel replacement

Choose

\[
 V_{200}\subset V_{260}\subset V_{600}\subset\mathcal P_T              \tag{4.1}
\]

from the primitive Legendre filtration.  Relative to
\(V_{200}\oplus(V_{600}\ominus V_{200})\oplus V_{600}^{\perp}\), retain
the actual directed matrix of the middle block and eliminate it exactly.
Only the final \(V_{600}^{\perp}\) is bounded by a scalar gap.  The sharp
endpoint-flat/Plancherel estimates of D.204--D.206 control its residual.

Equivalently, the middle block supplies a rational, finite-rank lower
approximation to the true Green \(A_{QQ}^{-1}\) on the range of \(C\).
The certificate obligations are:

1. build the complete directed primitive compression on \(V_{600}\);
2. prove its positive pivots by nested Schur complements;
3. prove a directed lower bound on the complement of \(V_{600}\);
4. enclose the full residual into that complement;
5. verify the final Schur matrix with outward rounding.

This route preserves the high-mode geometry discarded by (0.2).
