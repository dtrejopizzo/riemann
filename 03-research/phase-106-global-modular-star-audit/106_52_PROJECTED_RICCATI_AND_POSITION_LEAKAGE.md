# 106.52 — Projected Riccati identity and position leakage

## Purpose

Document 106.51 showed that the logarithmic rate variation cannot be
replaced coefficientwise by

\[
 j_2=\delta\Lambda+\Lambda*\Lambda.
\]

This note performs the missing algebra before any sign estimate. The
one-sided Euler connection satisfies a Riccati identity. After compression
against a finite reducing projection, its commutator part has an exact
Hilbert--Schmidt completion. The only negative term left by that completion
is a position-leakage norm.

The calculation is finite-rank and contains no zero-location hypothesis.
It does not identify the Euler connection with the full Doob generator;
that final spatial lift is isolated in Section 5.

## 1. The one-sided connection

Let

\[
 S_a f(x)=f(x+a),\qquad Xf(x)=xf(x),                 \tag{1}
\]

and, first with a finite prime-power cutoff, put

\[
 A=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
       S_{\log n}.                                   \tag{2}
\]

The scale derivation is represented spatially by

\[
 \delta A=-[X,A],                                    \tag{3}
\]

because \([X,S_a]=-aS_a\). Define

\[
 H=A+A^*,\qquad C=A-A^*,\qquad
 B=\delta A+A^2.                                     \tag{4}
\]

Thus \(H\) is symmetric, \(C\) is skew symmetric, and the coefficients of
\(B\) are exactly

\[
 j_2=\delta\Lambda+\Lambda*\Lambda\ge0.              \tag{5}
\]

The cutoff is used only to make every operation bounded. All identities
below therefore pass to any common graph core on which the three displayed
operators converge.

## 2. Exact Riccati square

### Theorem 1 — Symmetric/skew Riccati identity

On the common core,

\[
\boxed{
 H^2=C^*C+2(B+B^*)+2[X,C].}                          \tag{6}
\]

#### Proof

Taking adjoints in (3) gives

\[
 (\delta A)^*=[X,A^*],
\]

and hence

\[
 B+B^*=-[X,C]+A^2+A^{*2}.                            \tag{7}
\]

On the other hand,

\[
 H^2=A^2+A^{*2}+AA^*+A^*A,
\]

whereas

\[
 C^*C=-(A-A^*)^2=AA^*+A^*A-A^2-A^{*2}.             \tag{8}
\]

Substitution of (7)--(8) proves (6). \(\square\)

No positivity of the convolution operator \(B\) is asserted here.
Coefficient positivity in (5) is weaker than operator positivity.

## 3. Compression onto a spectral cluster

The full generator is self-adjoint in \(L^2(\mu_K)\), whereas the shifts in
(2) are unitary in \(L^2(dx)\). Let

\[
 w(x)=\frac{h(x)K(x)}{c_K},\qquad
 (\mathcal Uf)(x)=w(x)^{1/2}f(x).
\]

Then \(\mathcal U:L^2(\mu_K)\to L^2(dx)\) is unitary and commutes with
\(X\). For a spectral projection \(P_\mu\) of the full generator, every
Euler-side formula below uses its conjugate
\(P=\mathcal UP_\mu\mathcal U^{-1}\). This is indispensable: a raw
translation is not unitary in \(L^2(\mu_K)\).

Let \(P\) be a finite-rank orthogonal projection whose range lies in the
common core. In the intended application, \(P\) is the Riesz projection of
a compact subthreshold cluster after the preceding unitary conjugation.
Set

\[
 D=[X,P].                                             \tag{9}
\]

### Lemma 2 — Projected commutator completion

For every skew-adjoint \(C\),

\[
 \operatorname {Tr}P[X,C]
 =2\operatorname {Re}\langle CP,DP\rangle_{\rm HS},  \tag{10}
\]

and consequently

\[
\boxed{
 \|CP\|_{\rm HS}^2+2\operatorname {Tr}P[X,C]
 =\|CP+2DP\|_{\rm HS}^2-4\|DP\|_{\rm HS}^2.}         \tag{11}
\]

#### Proof

Cyclicity is legitimate because \(P\) has finite rank:

\[
 \operatorname {Tr}P[X,C]
 =\operatorname {Tr}([P,X]C).                        \tag{12}
\]

Write the operators in the decomposition
\(\operatorname {Ran}P\oplus\operatorname {Ran}(I-P)\). Only the two
off-diagonal blocks contribute to (12). Using \(C^*=-C\) and \(X^*=X\)
gives

\[
 \operatorname {Tr}P[X,C]
 =2\operatorname {Re}
   \operatorname {Tr}\{(CP)^*DP\},                   \tag{13}
\]

which is (10). Expanding the square in (11) and invoking (10) proves the
second identity. \(\square\)

Combining Theorem 1 and Lemma 2 gives the principal formula of this note.

### Theorem 3 — Projected Riccati identity

\[
\boxed{
\begin{aligned}
 \operatorname {Tr}(PH^2)
 ={}&\|CP+2[X,P]P\|_{\rm HS}^2\\
 &+2\operatorname {Tr}\{P(B+B^*)\}
 -4\|[X,P]P\|_{\rm HS}^2.
\end{aligned}}                                       \tag{14}
\]

#### Proof

Since \(H\) is symmetric,
\(\operatorname {Tr}(PH^2)=\|HP\|_{\rm HS}^2\). Take the trace of (6)
against \(P\), use
\(\operatorname {Tr}(PC^*C)=\|CP\|_{\rm HS}^2\), and apply (11).
\(\square\)

## 4. Geometry of the leakage

The negative term in (14) has several equivalent exact forms:

\[
\begin{aligned}
 \|[X,P]P\|_{\rm HS}^2
 &=\operatorname {Tr}\{PX(I-P)XP\}\\
 &=\operatorname {Tr}\{PX^2P-(PXP)^2\}.              \tag{15}
\end{aligned}
\]

If \(P\) has kernel

\[
 \Pi(x,y)=\sum_{k=1}^m q_k(x)\overline{q_k(y)},       \tag{16}
\]

with respect to \(dx\), then

\[
\boxed{
 2\|[X,P]P\|_{\rm HS}^2
 =\|[X,P]\|_{\rm HS}^2
 =\iint (x-y)^2|\Pi(x,y)|^2\,dx\,dy.}                \tag{17}
\]

Thus the obstruction left by the logarithmic derivation is not an
unidentified arithmetic error. It is exactly the off-diagonal position
spread of the reducing cluster.

## 5. What the physical three-point formula must now prove

Formula (14) is an Euler-side algebraic identity. Formula 106.51(16) is
the physical three-point identity for the complete Doob generator. A
valid lift has to combine them before taking signs.

Define \(\mathfrak G_{\Gamma,0}(P)\) to be the complete Gamma and polar
part of the three-point curvature, including all prime--Gamma mixed
triangles and the threshold subtraction. Define
\(\mathfrak J_2(P)\) to be the spatial theta lift of
\(2\operatorname {Re}\operatorname {Tr}(PB)\). The exact remaining
statement is

\[
\boxed{
 \mathfrak J_2(P)+\mathfrak G_{\Gamma,0}(P)
 \ge 4\|[X,P]P\|_{\rm HS}^2,}                        \tag{18}
\]

after the nonnegative square in (14) and the commuting-move squares in
106.51 are identified only once. Every term in (18) is projection
specific. This is essential: the unrestricted \(j_2\) Hankel lift is
indefinite by 106.40, while \(P\) here is idempotent, reducing for the full
generator, and annihilates the radical threshold space.

If (18) holds, (14) and the exact three-point formula yield

\[
 \mathfrak T(P)
 =\operatorname {Tr}\{P_\mu(L^2-\tfrac12L)\}\ge0.    \tag{19}
\]

But every nonzero cluster in a compact interval
\(J\Subset(0,1/2)\) has \(\mathfrak T(P)<0\) by 106.48. Therefore (18)
would exclude every subthreshold bound state.

Equation (18), not coefficient positivity by itself, is the next theorem
to establish. Its left side must still be derived from the full physical
kernel; no such inequality is assumed in this note.

### Subsequent cutoff correction

Document 106.55 proves that the two prime terms suggested on the left of
(18) do not have separate \(N\to\infty\) limits. The primitive \(j_2\)
operator and its intermediate-position defect diverge and cancel only in
the common finite-cutoff physical product. Accordingly, (18) is a
finite-cutoff bookkeeping target, not a cutoff-free inequality between two
independently defined forms. The valid limiting object is solely the full
three-point trace 106.55(16).

## 6. Verification and non-duplication audit

The algebraic identities (6), (10), (11), (14), and (17) were checked on
random complex finite matrices for dimensions \(3\) through \(11\); the
largest discrepancy was below \(2\times10^{-14}\).

Phases 100--101 already use the general principle that a trace kills an
ordinary commutator, and E101.063 in particular proves that compression of
the logarithmic Euler commutator creates a non-negligible projection shell.
Neither fact is claimed as new. The calculation here is the adaptation of
that shell to the finite Riesz projection of the full Phase-106 generator:
the Riccati square identifies its exact Hilbert--Schmidt value as the
position leakage (15)--(17). Thus the old Gamma--Euler shell is not removed;
it is converted into the weaker projection-specific inequality (18).
