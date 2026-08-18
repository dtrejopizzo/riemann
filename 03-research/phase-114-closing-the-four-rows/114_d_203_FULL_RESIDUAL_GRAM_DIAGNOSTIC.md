# D.203 — Full residual-Gram diagnostic at the first endpoint

## Purpose and status

The diagonal trace estimate of D.201 loses all correlations.  This note
records the first computation of the complete \(198\times198\) residual
Gram matrix for the primitive \(V_{200}\) frame at
\(T=\frac12\log 6\).  It is a binary64 FFT sizing experiment, not a
directed infinite-dimensional certificate.

The implementation is

\[
\texttt{114\_d\_203\_t6\_full\_fft\_residual\_gram.py}.
\]

Its main \(2^{17}\)-point artifact is

\[
\texttt{/tmp/t6\_full\_fft\_residual\_gram.npz}.
\]

## 1. Residual Gram identity

Let \(X:\mathbb R^{198}\to V_{200}\cap\ker J\) be the orthonormal
primitive eigenframe, \(A=-B_{\rm nuc}\) the zero-extension chart
operator, and \(P\) the orthogonal projection to the finite chart.  Put

\[
 B_{\rm fin}=X^*PAPX.
\]

Then

\[
 \begin{aligned}
 H
 &=(AX)^*(AX)-B_{\rm fin}^*B_{\rm fin}\\
 &=X^*AP^\perp AX\ge0.                                \tag{1.1}
 \end{aligned}
\]

Thus \(H\) contains every cross term of the finite-to-complement
coupling.  If \(\Lambda=\mathrm{diag}(\lambda_i)\) is the positive
finite block, the generalized coupling on a safe index set \(S\) is

\[
 M_S=\Lambda_S^{-1/2}H_{SS}\Lambda_S^{-1/2},\qquad
 \kappa_S=\lambda_{\max}(M_S).                        \tag{1.2}
\]

The diagonal-only sum of D.201 is \(\mathrm{tr}\,M_S\); it can be
much larger than the operator norm and cannot identify the directions
which must be promoted.

On a uniform grid the measured basis Gram is not exactly the identity.
The code therefore uses the algebraically equivalent formula

\[
 H_{\rm grid}=A_{\rm grid}^*A_{\rm grid}
 -B_{\rm grid}^*G_{\rm grid}^{-1}B_{\rm grid}.        \tag{1.3}
\]

The symmetric binary64 matrix is projected to its positive spectral part
only to remove roundoff-size negative eigenvalues.  At \(2^{17}\) points
the negative trace before projection was \(3.7\,10^{-12}\).

## 2. Numerical result

With the first two finite eigenvectors kept in the original delicate
block, the initial \(2^{17}\)-point computation gives

\[
 \kappa_S=0.4016866781.                               \tag{2.1}
\]

The first generalized eigenvalues are

\[
\begin{array}{rrrrrrrr}
0.401687,&0.352441,&0.312968,&0.306216,&
0.297705,&0.294499,&0.292596,&0.291415.
\end{array}
\]

For the scalar complement margin \(\delta=0.219\), forty generalized
eigenvalues lie above \(\delta\), while

\[
 \sigma_{40}^2=0.2167541172<0.219.                    \tag{2.2}
\]

Therefore the complete coupling does not support the earlier
eight-direction promotion suggested by a \(30\)-row band.  At this
resolution it suggests a delicate block of about \(2+40\) directions.

## 3. Resolution audit

The corresponding leading values are

\[
\begin{array}{c|c|c}
\text{FFT grid}&\kappa_S&
 \#\{\sigma_j^2>0.219\}\\ \hline
2^{16}&0.3873607&38\\
2^{17}&0.4016867&40\\
2^{18}&0.5155949&42\\
2^{20}&0.4364321&42
\end{array}
\]

The \(2^{20}\) run uses \(dx=3.0518\,10^{-5}\), comparable with the
\(N^{-2}\) endpoint scale.  Its next generalized eigenvalue after the
forty-two promoted directions is

\[
 \sigma_{42}^2=0.2162240<0.219.                       \tag{3.1}
\]

The leading value is not yet monotone.  The reason is visible in the measured
uniform-grid Gram: high Legendre modes have an endpoint layer on scale
\(O(N^{-2})\), and a uniform FFT grid samples that layer poorly.  In
the \(2^{20}\) run its eigenvalue range has improved to
\([0.99956,1.21542]\), but the finite projected operator is still not
close enough to the directed finite matrix in operator norm.
Consequently neither the number forty-two nor the value \(0.4364\) is a
proof-quality bound.  The stabilization of the promotion count between
\(2^{18}\) and \(2^{20}\) nevertheless makes a \(44\)-dimensional
delicate block (the original two plus forty-two generalized directions)
the appropriate next directed sizing target.

## 4. Consequence for the rigorous route

The diagnostic makes one structural decision reliable: a narrow
high-row band is not enough to estimate the full safe-to-complement
operator.  The directed proof must do one of the following:

1. compute the generalized residual Gram in successive exact Legendre
   row bands and add a directed analytic tail bound; or
2. bound the weighted Green operator
   \(A_{QQ}^{-1/2}A_{QS}A_{SS}^{-1/2}\) directly, rather than replacing
   \(A_{QQ}\) by the scalar \(\delta I\).

After its large singular directions are promoted into \(D\), the correct
three-block condition remains

\[
 K_D-(\delta-\kappa_S)^{-1}C_DC_D^*>0,               \tag{4.1}
\]

with \(K_D,C_D,\kappa_S\) as defined in D.200.  No sign conclusion is
drawn from the FFT diagnostic alone.

## Conclusion

The full Gram computation improves the route by retaining all
correlations and by exposing the approximate promotion rank.  It also
shows why the band-only value was overoptimistic.  The comparison with
\(B_{\rm nuc}\) is unaffected; what remains is a directed
infinite-dimensional estimate for the complete residual coupling.
