# 107.186 -- The Gamma boundary channel is a regularized Green trace

## 1. Archimedean operator

Let \(N\) be the number operator on \(\ell^2(\mathbb Z_{\ge0})\):

\[
 Ne_n=ne_n.
\]

For \(a\notin\{0,-1,-2,\ldots\}\), the resolvent has diagonal entries
\((n+a)^{-1}\).  Its ordinary trace diverges logarithmically, but its
Hadamard finite part exists:

\[
 \operatorname{Tr}_{\rm reg}(N+a)^{-1}
 :=\lim_{M\to\infty}left(
 \sum_{n=0}^{M}{1\over n+a}-\log M
 \right)
 =-\psi(a).
 \tag{1.1}
\]

This is the resolvent analogue of the periodic-orbit Green kernels in
`107_185`.

## 2. Gamma channel

Set \(a=s/2\).  Equation (1.1) gives

\[
 \mathscr G_\Gamma(s)
 ={1\over2}\operatorname{Tr}_{\rm reg}(N+s/2)^{-1}
 +{1\over2}\log\pi
 =-{1\over2}\psi(s/2)+{1\over2}\log\pi.
 \tag{2.1}
\]

Adding the degree-zero and degree-two pole terms gives

\[
 \mathscr G_\infty(s)
 =-{1\over s}-{1\over s-1}+\mathscr G_\Gamma(s).
 \tag{2.2}
\]

Together with the prime-orbit Green traces,

\[
 \sum_p\ell_pG_{p,s}(\ell_p^-)+\mathscr G_\infty(s)
 =-{\xi'(s)\over\xi(s)}.
 \tag{2.3}
\]

Thus every summand of the completed scalar channel now has an operator
Green realization: twisted first-order orbit operators at finite places
and a regularized number-operator resolvent at infinity.

## 3. Nature of the regularization

The subtraction \(\log M\) in (1.1) is fixed by the asymptotic spectral
density of \(N\); changing it by a constant would change the
\(\frac12\log\pi\) normalization and fail (2.3).  The white-light
divergence of the semilocal trace formula is the global counterpart of
this logarithmic divergence.

The poles at nonpositive integral \(a\) are genuine failures of
invertibility of \(N+a\).  They combine with the finite and rational pole
terms exactly as in the completed zeta function.

## 4. Result and remaining geometry

The finite and archimedean scalar Green operators are constructed.  What
is still absent is a single sheaf/cohomology object on the absolute
arithmetic space whose restrictions are these operators and whose
determinant line carries an intersection pairing.

In particular, (2.3) is not yet an Arakelov Green current: the number
operator acts on a spectral Hilbert space, not on functions of a proved
proper arithmetic surface.  The next comparison must identify this
regularized resolvent with the archimedean Green datum of the sought
primitive class.

## 5. Falsifier

The verifier computes the finite parts in (1.1) by direct independent
spectral sums up to \(M=10^6\), for real and complex \(a\), and compares
them with \(-\psi(a)\).  Errors must decrease at every fixed cutoff and
the final fixed tolerance is \(3\times10^{-6}\).  It then checks (2.3)
against the completed logarithmic derivative.  Any normalization error
returns `VERDICT: NO`.
