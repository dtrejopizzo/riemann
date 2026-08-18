# 105_04 — Prefix compression and the exact Mangoldt-discrepancy target

## Result

Put

\[
 N=L^2,\qquad
 S_L=\sum_{r=0}^{L-1}|\lambda_{N+r}|,
\]

and define the consecutive prefix sums

\[
 T_{L,j}=\sum_{r=0}^{j}\lambda_{N+r},\qquad
 M_L=\max_{0\le j<L}|T_{L,j}|.
\]

Then

\[
 \boxed{M_L\le S_L\le(2L-1)M_L.}                       \tag{1}
\]

Consequently the block criterion of `105_03` can be tested with only
\(L\) consecutive prefixes, rather than the full cube of \(2^L\) sign
selectors:

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \log(1+M_L)=o(L^2).}                                  \tag{2}
\]

There is also an exact ordinary-prime form.  Define

\[
 \Delta(u)=\gamma-u+
 \sum_{m\le e^u}\frac{\Lambda(m)}m                     \tag{3}
\]

away from the immaterial jump endpoints, and

\[
 H_{N,j}(u)=
 L_{N+j-2}^{(3)}(u)-L_{N-3}^{(3)}(u).                  \tag{4}
\]

Then

\[
 T_{L,j}=
 \sum_{r=0}^{j}A_{N+r}
 +\gamma P_{N,j}(0)
 -\int_0^\infty H_{N,j}(u)\Delta(u)\,du,               \tag{5}
\]

where

\[
 P_{N,j}(u)=
 L_{N+j-1}^{(2)}(u)-L_{N-2}^{(2)}(u).                  \tag{6}
\]

The explicit terms outside the integral are
\(\exp\{o(N)\}\), uniformly for \(0\le j<L=\sqrt N\).  Hence the
remaining literal-prime theorem is exactly

\[
 \boxed{
 \log\!\left(1+\max_{0\le j<L}
 \left|\int_0^\infty H_{N,j}(u)\Delta(u)\,du\right|
 \right)=o(N),\qquad N=L^2.}                           \tag{7}
\]

Equation (7) has not been proved here.  By (2) and (5), proving it is
equivalent to proving RH.  The gain in this document is a lossless
compression of the arithmetic target: the arbitrary selector has
disappeared and only two Laguerre boundary degrees remain in each test.

## 1. Lossless compression to prefixes

For arbitrary real numbers \(x_0,\ldots,x_{L-1}\), put
\(X_j=\sum_{r=0}^jx_r\).  Clearly

\[
 \max_j|X_j|\le\sum_r|x_r|.
\]

Conversely, \(x_0=X_0\) and \(x_r=X_r-X_{r-1}\) for \(r\ge1\), so

\[
 \sum_{r=0}^{L-1}|x_r|
 \le |X_0|+\sum_{r=1}^{L-1}(|X_r|+|X_{r-1}|)
 \le(2L-1)\max_j|X_j|.                                  \tag{8}
\]

Taking \(x_r=\lambda_{N+r}\) proves (1).  Since
\(\log(2L-1)=o(L^2)\), (1) and `105_03`, Theorem (2), prove (2).

## 2. The coupled prime--continuum measure

For \(\varepsilon>0\), retain pole and primes in the single signed
measure

\[
 d\nu_\varepsilon(u)=e^{-\varepsilon u}\,du
 -\sum_{m\ge2}\frac{\Lambda(m)}{m^{1+\varepsilon}}
       \delta_{\log m}(du).                              \tag{9}
\]

Its total mass and tail are

\[
 M_\varepsilon
 =\frac1\varepsilon+\frac{\zeta'}{\zeta}(1+\varepsilon),
 \qquad
 \Delta_\varepsilon(u)=\nu_\varepsilon((u,\infty)).    \tag{10}
\]

The Laurent expansion at one gives \(M_\varepsilon\to\gamma\).  On
every compact interval away from a jump,

\[
 \Delta_\varepsilon(u)\longrightarrow
 \gamma-u+\sum_{m\le e^u}\frac{\Lambda(m)}m=\Delta(u). \tag{11}
\]

This is not a separation of two divergent quantities: (10) is formed at
positive \(\varepsilon\), and (11) is its Abel limit.

For a polynomial \(P\), Stieltjes summation by parts at fixed
\(\varepsilon\) gives

\[
 \int_0^\infty P(u)\,d\nu_\varepsilon(u)
 =P(0)M_\varepsilon+
  \int_0^\infty P'(u)\Delta_\varepsilon(u)\,du.          \tag{12}
\]

The effective PNT bound makes the corresponding \(\varepsilon=0\)
integral convergent for every fixed polynomial, so the Abel limit of
(12) is legitimate.

## 3. Telescoping the Laguerre degrees

The elementary addition identity

\[
 \sum_{r=0}^{j}L_{N+r-1}^{(1)}(u)
 =L_{N+j-1}^{(2)}(u)-L_{N-2}^{(2)}(u)                  \tag{13}
\]

turns the prime lift of `105_03` into

\[
 T_{L,j}
 =\lim_{\varepsilon\downarrow0}
 \left\{
 \sum_{r=0}^{j}A_{N+r}+
 \int_0^\infty P_{N,j}(u)\,d\nu_\varepsilon(u)
 \right\}.                                             \tag{14}
\]

Since \((L_k^{(2)})'=-L_{k-1}^{(3)}\), equations
(11)--(14) give (5).  Moreover,

\[
 P_{N,j}(0)=
 \binom{N+j+1}{2}-\binom N2=O(NL),                     \tag{15}
\]

and the known archimedean formula gives

\[
 \sum_{r=0}^{j}A_{N+r}=O(NL\log N).                    \tag{16}
\]

Both (15) and (16) are \(\exp\{o(N)\}\) for \(L=\sqrt N\).
Equations (2), (5), and (15)--(16) prove the equivalence between RH and
(7).

## 4. Two exact stop-gates

### 4.1 Sturm--Liouville coercivity

For \(y=L_k^{(3)}\),

\[
 (u^4e^{-u}y')'+ku^3e^{-u}y=0.                         \tag{17}
\]

Putting the unweighted correlation in the natural Laguerre space forces

\[
 h(u)=e^u u^{-3}\Delta(u),
 \qquad
 \|h\|_{L^2(u^3e^{-u}du)}^2
 =\int_0^\infty e^u u^{-3}\Delta(u)^2\,du.             \tag{18}
\]

An off-line zero \(\rho=\beta+i\gamma_\rho\) contributes a mode of
the form

\[
 \Delta_\rho(u)\asymp
 e^{-(1-\beta)u}\cos(\gamma_\rho u+\phi).              \tag{19}
\]

The tail of (18) then contains
\(e^{(2\beta-1)u}u^{-3}\cos^2(\gamma_\rho u+\phi)\).
It is finite on the critical line and divergent when \(\beta>1/2\).
Thus finiteness of the natural coercive norm is already an RH-selective
input; it cannot be assumed in a proof of (7).

### 4.2 Hardy/outer bounds

Let \(a\in\mathbb D\) and

\[
 b_a(z)=\frac{|a|}{a}\frac{a-z}{1-\overline a z},
 \qquad H_a(z)=z\frac{b_a'(z)}{b_a(z)}.                 \tag{20}
\]

On the unit circle,

\[
 H_a(e^{it})=\frac{1-|a|^2}{|e^{it}-a|^2},
 \qquad \|H_a\|_{L^1}=1,                               \tag{21}
\]

whereas at zero

\[
 H_a(z)=\sum_{n\ge1}
 (\overline a^{,n}-a^{-n})z^n.                         \tag{22}
\]

The coefficients in (22) grow like \(|a|^{-n}\) despite the fixed
boundary norm (21).  On a contour outside \(a\), the missing term is
exactly the interior residue.  Therefore a Hardy, Jensen, outer, or
Carleman norm cannot prove (7) by omitting interior residues: eliminating
those residues is precisely the zero-location statement to be proved.

### 4.3 Exact transform of the remaining correlation

The Laplace transform of (3) is, initially for \(\Re s>0\),

\[
 D(s):=\int_0^\infty e^{-su}\Delta(u)\,du
 =\frac\gamma s-\frac1{s^2}
 -\frac1s\frac{\zeta'}{\zeta}(1+s).                    \tag{23}
\]

Indeed, integrating each step from \(\log m\) to infinity gives
\(s^{-1}\sum_m\Lambda(m)m^{-1-s}\).  The Laguerre generating function
therefore yields the exact identity

\[
 \boxed{
 \sum_{k\ge0}\left\{
 \int_0^\infty L_k^{(3)}(u)\Delta(u)\,du
 \right\}z^k
 =(1-z)^{-4}D\!\left(\frac z{1-z}\right).}              \tag{24}
\]

A zero \(\rho\) maps to the pole \(z=(\rho-1)/\rho\).  Thus the
two-boundary compression in (7) has not lost the spectral obstruction:
it has isolated its coefficients exactly.  Any proof of (7) must exclude
the interior poles by an arithmetic inequality; another analytic
continuation of (24) cannot remove them.

### 4.4 A prime-supported falsifier for generic sawtooth arguments

Even support on the ordinary primes, positive jumps, and a discrepancy
envelope exponentially stronger than Vinogradov--Korobov do not imply
(7) if the literal jump sizes are removed.  This distinguishes precisely
which arithmetic datum remains indispensable.

Use the unconditional Baker--Harman--Pintz prime-gap theorem
\(p_{k+1}-p_k\ll p_k^{0.525}\) (R. C. Baker, G. Harman and J. Pintz,
[*The difference between consecutive primes, II*](https://doi.org/10.1112/plms/83.3.532),
Proc. London Math. Soc. 83 (2001), 532--562).  More generally, write
\(p_{k+1}-p_k\ll p_k^\vartheta\) with any fixed
\(\vartheta<1\), and put \(b=1-\vartheta>0\).  Choose

\[
 0<a<\min\{b,1/2\},\qquad f(u)=\gamma e^{-au}.            \tag{25}
\]

Start with \(D_a(u)=\gamma-u\) on \([0,\log2)\).  At every prime node
\(v_k=\log p_k\), insert the unique jump which resets
\(D_a(v_k+)=f(v_k)\), and let \(D_a\) have slope \(-1\) between nodes.
The first jump is positive, because

\[
 \log2-\gamma(1-2^{-a})
 >\log2(1-a\gamma)>0.                                    \tag{26}
\]

If \(h_k=v_{k+1}-v_k\), every later jump is also positive:

\[
 h_k+f(v_{k+1})-f(v_k)\ge h_k(1-a\gamma)>0.              \tag{27}
\]

Consequently

\[
 dD_a=-du+\sum_p b_p\delta_{\log p},\qquad b_p>0,        \tag{28}
\]

and the prime-gap estimate gives

\[
 D_a(u)-f(u)=O(e^{-bu}),\qquad D_a(u)=O(e^{-au}).         \tag{29}
\]

Nevertheless, if
\(c_k(D_a)=\int_0^\infty D_a(u)L_k^{(3)}(u)\,du\), the
contribution of \(f\) has generating function

\[
 \sum_{k\ge0}c_k(f)z^k
 =\frac{\gamma}{(1-z)^3\{a+(1-a)z\}}.                    \tag{30}
\]

Its dominant coefficient is

\[
 c_k(f)=\frac{\gamma(1-a)^3}{a}
 \left(-\frac{1-a}{a}\right)^k+O(k^2).                  \tag{31}
\]

The error in (29) has a Laplace transform analytic in \(\Re s>-b\),
so its coefficient root rate is at most
\(\max\{1,(1-b)/b\}\), strictly below \((1-a)/a\).  Hence

\[
 c_{N-2}(D_a)-c_{N-3}(D_a)
 =\exp\{(\log((1-a)/a)+o(1))N\}                         \tag{32}
\]

in modulus.  This is the first prefix kernel in (7), and it is
exponential.

The construction is not a counterexample for the actual von Mangoldt
weights: its \(b_p\) are not \(\log p/p\).  Its exact conclusion is that
cell geometry, prime support, positivity, prime gaps, and a strong PNT
envelope cannot prove (7).  The proof must use the literal weights,
equivalently their full divisor relation \(\Lambda*1=\log\), in a
nonlinear signed way.

## Status

The selector complexity has been removed exactly.  The remaining theorem
is the signed correlation (7) for the literal von Mangoldt weights.  A
proof must use information not contained in absolute PNT envelopes,
generic positive jumps, Sturm energy, boundary Hardy norms, or an
algebraic re-expansion of \(-\zeta'/\zeta\).
