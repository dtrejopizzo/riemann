# D.179 — Actual-cross phase divisibility

## Verdict

After the harmonic part is telescoped as in D.175, the scalar Hadamard
counter-scaling of D.171 no longer applies to an arbitrary boundary load.
The remaining vector is the actual gap cross

\[
 q=X_0^*X_E-Y_0^*Y_E.                                \tag{0.1}
\]

In every commuting Hadamard fibre, (q) contains the same factor which
vanishes in the old output defect.  For

\[
 r(\theta)=1-\cos\theta,\qquad
 l(\theta)=1+\cos\theta,                              \tag{0.2}
\]

the normalized defect and the unnormalized gap are

\[
 d(\theta)={r-l\over r}={-2\cos\theta\over1-\cos\theta},
 \qquad g(\theta)=r-l=-2\cos\theta.                  \tag{0.3}
\]

Thus an actual cross of the form (q=g h) satisfies

\[
 { |q|^2\over d}=r\,g\,|h|^2,                       \tag{0.4}
\]

which tends to zero, rather than infinity, when the balanced phase is
approached from the contractive side.  The divergence in D.171 came from
choosing (y=\epsilon^{1/4}) independently of (g).

For the complete A--B--C form the scalar gap is the exact symbol of
D.163,

\[
 g_T(\tau)=h_{5/4}(\tau)-\beta-{1\over\tau^2+1/4}
 -\sum_p\log p\,[P_{p,K_p(T)}(\tau)-1],              \tag{0.5}
\]

so the same fibrewise statement retains Gamma and every (p^j).

What remains is entirely a compression problem.  In physical old/born
coordinates,

\[
 q=P_0M_{g_T}P_E,\qquad
 D_0=R_0^{-1/2}P_0M_{g_T}P_0R_0^{-1/2}.              \tag{0.6}

The projections do not commute with (M_{g_T}).  Therefore the required
factorization is a Toeplitz--Hankel divisibility theorem for the off-diagonal
block in (0.6).  It is automatic in the commuting fibres and false for a
general self-adjoint block matrix with only a positive old corner.

## 1. Exact scalar cancellation

Choose the D.171 phase by

\[
 \cos\theta_\epsilon=-{\epsilon\over2-\epsilon}.     \tag{1.1}
\]

Then

\[
 d(\theta_\epsilon)=\epsilon,\qquad
 r(\theta_\epsilon)={2\over2-\epsilon},\qquad
 g(\theta_\epsilon)={2\epsilon\over2-\epsilon}.     \tag{1.2}
\]

For a fixed overlap amplitude (h),

\[
 {|g(\theta_\epsilon)h|^2\over d(\theta_\epsilon)}
 ={4\epsilon\over(2-\epsilon)^2}|h|^2\longrightarrow0. \tag{1.3}
\]

This is the precise linear vanishing which D.175 exposes.  It does not
prove the compressed statement, but it removes arbitrary scalar
phase-defect countermodels from the reduced (q)-problem.

## 2. Complete symbol and Tate projection

Equation (0.5) is obtained term by term from

\[
 J_{p^j,-}^*J_{p^j,-}-J_{p^j,+}^*J_{p^j,+}
 =-(S_{j\log p}+S_{-j\log p}),                       \tag{2.1}
\]

with coefficient ((\log p)p^{-j/2}), and from the full digamma/Gamma,
(\beta) and (Q_{1/2}) channels.  The two Tate evaluations are removed by
the same projection on both sides of (0.6).  Hence the off-diagonal block
is the compression of the **same** completed symbol as the old defect;
there is no independently attached (E_N) load after D.175.

The centered discrepancy remains because the old/born projections turn
the multiplier into a Hankel block.  Tate centering changes its coherent
continuous part but does not make the Hankel block zero, as proved in
D.177.

## 3. Exact remaining factorization

Let

\[
 G_{00}=P_0M_{g_T}P_0,\qquad G_{0E}=P_0M_{g_T}P_E.    \tag{3.1}

The reduced Douglas assertion is

\[
 \boxed{
 R_0^{-1/2}G_{0E}S_E^{-1/2}
 =\bigl(R_0^{-1/2}G_{00}R_0^{-1/2}\bigr)^{1/2}A_N}   \tag{3.2}

with a quantitatively bounded (A_N).  If (M_{g_T}\ge0) on the whole
space, (3.2) follows from positivity of its (2\times2) compression.
But global positivity of the completed multiplier is unavailable and is
stronger than the old-corner induction hypothesis.

The structure which may still prove (3.2) is that (G_{00}) and
(G_{0E}) are Toeplitz and Hankel blocks of the same explicit convolution
kernel.  The next step is therefore to control the Hankel block using the
inverse-closed decay of the positive reference (R_0), not to estimate an
arbitrary (y) against an arbitrary small defect.

The accompanying verifier contrasts the actual cross with the arbitrary
D.171 load and checks a noncommuting block example showing why the
compression theorem remains substantive.
