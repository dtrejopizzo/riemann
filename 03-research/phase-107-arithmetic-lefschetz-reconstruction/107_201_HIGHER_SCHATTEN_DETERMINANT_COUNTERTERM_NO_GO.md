# 107.201 -- Higher Schatten determinants introduce prime-zeta counterterms

## 1. Schatten threshold

For the balanced global operator of 107_200, the two singular values in
the \(p\)-block are \(p^{-\sigma/2}\).  Hence

\[
 D_s\in\mathcal S_m
 \quad\Longleftrightarrow\quad
 \sum_p p^{-m\sigma/2}<\infty
 \quad\Longleftrightarrow\quad
 \sigma>{2\over m}.
 \tag{1.1}
\]

Thus \(m=5\) is the first integer order defined on the critical line
\(\sigma=1/2\); \(m=4\) is at the divergent endpoint.

## 2. Exact block formula

For \(A\in\mathcal S_m\),

\[
 \det{}_m(1-A)=
 \prod_\lambda(1-\lambda)
 \exp\left(\sum_{k=1}^{m-1}{\lambda^k\over k}\right).
\]

Pairing \(\lambda=\pm a\), with \(a^2=q=p^{-s}\), cancels odd
powers but not even powers:

\[
 \det{}_m(1-D_{p,s})
 =(1-q)\exp\left(
 \sum_{j=1}^{\lfloor(m-1)/2\rfloor}{q^j\over j}
 \right).
 \tag{2.1}
\]

Only \(m=2\) has no surviving counterterm.

## 3. Global consequence

In the common Euler domain, writing
\(P(z)=\sum_p p^{-z}\) for the prime-zeta function gives

\[
 \det{}_m(1-D_s)
 ={1\over\zeta(s)}
 \exp\left(
 \sum_{j=1}^{\lfloor(m-1)/2\rfloor}{P(js)\over j}
 \right).
 \tag{3.1}
\]

For the critical-line order \(m=5\),

\[
 \det{}_5(1-D_s)
 ={1\over\zeta(s)}
 \exp\left(P(s)+\frac12P(2s)\right).
 \tag{3.2}
\]

Neither prime-zeta series converges separately on the critical line.
Their analytically continued combination cancels the leading logarithmic
branch at \(s=1/2\), but, as proved in 107_202, retains fractional
branches elsewhere in the critical strip.

## 4. No-go theorem

**Theorem.**  No uncorrected higher regularized determinant
\(\det_m(1-D_s)\), \(m\ge3\), is equal to \(\zeta(s)^{-1}\).
Changing Schatten order does not by itself analytically continue the
row-(c) determinant.

**Proof.**  Formula (2.1) contains the nonconstant factor
\(\exp(q)\) already for \(m=3\).  Multiplication over primes yields
(3.1), whose exponential counterterm is nontrivial. \(\square\)

Recovering \(\zeta^{-1}\) requires a specified renormalization that
subtracts the prime-zeta counterterms.  Such subtraction cannot be
called canonical merely because it restores the desired answer; it must
arise from Gamma/pole blocks, a relative determinant, or a geometric
local counterterm.

## 5. Exact scope

This does not exclude a completed graded operator whose archimedean and
degree-zero/two sectors cancel (3.1).  It proves that the prime Dirac
family alone cannot be continued by simply replacing \(\det_2\) with
\(\det_5\).

## 6. Falsifier

The verifier checks the block identity for \(m=2,3,5,6\) on the fixed
prime/spectral atlas, verifies that only \(m=2\) is counterterm-free,
and compares finite global products with (3.1).  It also checks the
Schatten threshold at \(\sigma=1/2\) on real prime data.
