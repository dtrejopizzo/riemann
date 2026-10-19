# 104_26 — Quartic attack, missing coercivity, and the squares stop-gate

> **Binding correction (`104_56A`).** The slack \(A_n/1001\) of (1) is
> exactly the cost of `104_23`'s uniform sufficient condition when only the
> floor \(T\ge1000\) is used; it is not necessary for RH nor for an A1
> transfer with an adapted cofinal cutoff. The algebraic squares stop-gate of
> this document remains valid. Only the claim that every quartic route must
> produce that proportional slack is withdrawn: \(D_n^{[4]}\ge0\) already
> directly proves RH, and \(D_n^{[4]}>0\) allows choosing a cutoff that
> closes A1.

**Role.** Exploit the fact that the uniform margin of 104_23,
\(r_*=2002/501\), is only \(2/501\) away from the integer exponent four.
The quartic cocycle admits a local fourth difference and a formal
factorization as the square of a half-power cocycle. This document proves
that neither observation produces a useful sum of squares: the local power
remains algebraic, the real block changes sign, and the genuinely quadratic
part disappears when taking the limit that extracts the coefficients. It
also identifies exactly the slack a quartic attack would have to produce to
recover **the uniform sufficient condition fixed in** `104_23`:

\[
 D_n^{[4]}:=4\lambda_n-A_n\ge {A_n\over1001}.      \tag{1}
\]

This document does not prove (1), A1, or RH.

## 1. Exact fourth difference on a tower

Let \(Q=p^u\), \(\rho=p^{-1-\varepsilon}\), and
\(d_u=J_u^{*4}\). The local generating function is

\[
 \sum_{k\ge0}d_u(p^k)x^k
 =\left({1-x\over1-Qx}\right)^4.
\]

Hence

\[
 \boxed{
 d_u(p^k)=\nabla^4\!\left[{k+3\choose3}Q^k\right].}        \tag{2}
\]

With the operators \(\mathsf P\), \(\mathsf B=I-\rho E_\ell\), and
\(\mathsf C=\mathsf B\mathsf P\) from 104_20, discrete summation gives

\[
 \boxed{
 \sum_{k\ge0}d_u(p^k)\rho^k\mathsf P^4f(x+k\ell)
 =
 \sum_{k\ge0}{k+3\choose3}(Q\rho)^k
 \mathsf C^4f(x+k\ell).}                           \tag{3}
\]

Although \(\mathsf C^4=(\mathsf C^2)^2\), (3) is algebraic composition,
not \(\mathsf C^*\mathsf C\). It defines no norm.

## 2. Two exact local falsifiers

Set \(w_k=d_u(p^k)\rho^k\). A computation of the first three coefficients
of (2) gives

\[
 \boxed{
 w_1^2-w_0w_2
 ={\rho^2r\over2}(Q-1)\bigl((r-1)Q-(r+1)\bigr)}
                                                               \tag{4}
\]

for the general convolution \(J_u^{*r}\). In particular, with
\(r=4\), \(p=2\), \(u=1/2\), \(\varepsilon=1\),
\(\rho=1/4\), \(Q=\sqrt2\),

\[
 w_1^2-w_0w_2={11-8\sqrt2\over8}<0,               \tag{5}
\]

since \(121<128\). The real fourth convolution is neither PF2 nor TP2.

The second falsifier keeps the whole tower, the four polar channels, and
the three Gamma copies. At degree one, over a background \(m\) coprime to
\(p\), the block is a positive prefactor multiplied by

\[
 (1-c)^4
 \bigl(1-\log m-3\bar\eta-\ell\mu_{p,4}\bigr)
 +{4c(1-c)^3\over\varepsilon},                    \tag{6}
\]

where

\[
 M_{p,4}=\left({1-\rho\over1-Q\rho}\right)^4,\qquad
 \mu_{p,4}={4\rho(Q-1)\over(1-\rho)(1-Q\rho)}.     \tag{7}
\]

The sign changes exactly at

\[
 \log m=1-3\bar\eta-\ell\mu_{p,4}
          +{4c\over(1-c)\varepsilon}.             \tag{8}
\]

For sufficiently small \(\varepsilon\), \(m=1\) is on the positive side
and there are infinitely many prime backgrounds on the negative side.
Hence block-by-block positivity does not exist for the real arithmetic
either.

## 3. The square vanishes in the direct limit

Let

\[
 B_u(s)=H_u(s)^2K_u(s)^{3/2},\qquad
 \mathcal S_u^{[4]}(s)=H_u(s)^4K_u(s)^3=B_u(s)^2. \tag{9}
\]

Then

\[
 {1-\mathcal S_u^{[4]}\over u}
 ={1-B_u\over u}(1+B_u),                          \tag{10}
\]

while, since \(B_u\to1\),

\[
 {(1-B_u)^2\over u}\longrightarrow0.              \tag{11}
\]

The limit of (10), which extracts \(4\lambda_n-A_n\), is linear. The
genuinely quadratic part is lost before reaching the coefficient. Writing
(9) is not a sum-of-squares certificate.

The positive-generator alternative fails by the same exact witness of
104_23. Before the first atom \(\log2\), the first variation of the
completed inverse is

\[
 f_{4,\varepsilon}(x)
 =-4e^{-\varepsilon x}
 +3{e^{-(3+\varepsilon)x}\over1-e^{-2x}},
\]

and at \(x_0=\frac12\log2\),

\[
 f_{4,\varepsilon}(x_0)
 =e^{-\varepsilon x_0}\left(-4+{3\over\sqrt2}\right)<0.   \tag{12}
\]

## 4. Off-line falsifier within the target range

Let

\[
 w={1\over2}e^{74\pi i/75},\qquad
 \rho={1\over1-w}.                                  \tag{13}
\]

Then \(1/2<\Re\rho<1\) and \(\Im\rho\ne0\). For the associated symmetric
quartet, with \(a=\log2\) and \(\theta=74\pi/75\), the contribution to
\(4\lambda_n\) is

\[
 16\bigl(1-\cosh(na)\cos(n\theta)\bigr).           \tag{14}
\]

At \(n=150\), \(\cos(n\theta)=\cos(148\pi)=1\), so (14) is strictly
negative. Repeating the quartet with multiplicity defeats any fixed
archimedean term. Hence a sum of squares using only symmetry, the
functional equation, and the fourth exponent would also be falsified by an
off-line divisor.

The witness already appears at \(n=2\): for
\(w=\frac12e^{5\pi i/6}\),

\[
 \lambda_2^{\rm quartet}
 =4-4\cosh(2\log2)\cos(5\pi/3)=-{1\over4}.        \tag{15}
\]

## 5. Exact relation to the near-quartic margin

Let

\[
 r_*={2002\over501},\qquad \delta=4-r_*={2\over501}.
\]

Then

\[
 \boxed{
 D_n^{[r_*]}
 =D_n^{[4]}-\delta\lambda_n
 ={1001D_n^{[4]}-A_n\over1002}.}                  \tag{16}
\]

Hence

\[
 \boxed{
 D_n^{[r_*]}\ge0
 \quad\Longleftrightarrow\quad
 D_n^{[4]}\ge {A_n\over1001}.}                    \tag{17}
\]

Mere semidefiniteness \(D_n^{[4]}\ge0\) is not enough. In cocycle
coordinates,

\[
 \mathcal S_u^{[r_*]}
 =\mathcal S_u^{[4]}
 \left({\xi(s-u)\over\xi(s)}\right)^{-2/501}.      \tag{18}
\]

The fractional corrector in (18) subtracts exactly the slack of (17) and
reintroduces the zero/branch gate.

## Status

- **Proved:** the fourth difference (2), the local factorization (3),
  witnesses (5), (8), (12), (14), and the coercive equivalence (17).
- **Ruled out:** the fourth power as a local sum of squares, PF/TP,
  generator positivity, and mere quartic semidefiniteness.
- **Open:** a special global inequality producing the quantitative
  coercivity \(D_n^{[4]}\ge A_n/1001\), or directly the real margin of
  104_23.
</content>
