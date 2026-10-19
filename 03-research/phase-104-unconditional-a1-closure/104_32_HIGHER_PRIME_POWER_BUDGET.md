# 104_32 — Explicit budget for higher prime powers

**Role.** Rigorously separate the powers \(p^k, k\ge2\), from the singular
prime channel at the Li point. The result is unconditional: the
higher-power part is an ordinarily convergent correction of size
\(O(n)\), with an explicit constant. The only channel needing joint
regularization remains formed by the primes \(p\) and the pole at
\(s=1\).

The document does not prove the coercive bound of `104_26`, A1, or RH. In
particular, the threshold obtained by absorbing the correction via absolute
value into \(A_n/1001\) is deliberately enormous.

## 1. Exact generator and Möbius separation

Let \(N=n-1\ge0\) and define

\[
 R_N:=P_N^{(\ge2)}(1)
 :=\sum_p\sum_{k\ge2}{\log p\over p^k}
       L_N^{(1)}(k\log p).                              \tag{1}
\]

For each \(N\), the series converges absolutely. Indeed,
\(L_N^{(1)}\) is a fixed polynomial and
\(\sum_p\sum_{k\ge2}(\log p)^{N+1}k^Np^{-k}<\infty\).

Set

\[
 \mathcal L(s):=-{\zeta'\over\zeta}(s),\qquad
 H_{\ge2}(s):=\sum_p\sum_{k\ge2}\log p\,p^{-ks}.
\]

Möbius inversion of
\(\mathcal L(s)=\sum_{k\ge1}Q(ks)\),
\(Q(s)=\sum_p\log p\,p^{-s}\), gives, for \(\Re s>1/2\),

\[
 \boxed{H_{\ge2}(s)
 =-\sum_{j\ge2}\mu(j)\mathcal L(js).}               \tag{2}
\]

The series on the right converges locally normally in that half-plane.
The Laguerre generating function then gives, for \(|z|<1\),

\[
 \boxed{
 \sum_{N\ge0}R_Nz^N
 ={1\over(1-z)^2}
 H_{\ge2}\!\left({1\over1-z}\right).}              \tag{3}
\]

There is no sum over zeros nor any hypothesis about their location in
(1)–(3).

## 2. The pole \(j=2\) and its sign

Since \(\mu(2)=-1\), the first term of (2) is
\(+\mathcal L(2s)\). Near \(s=1/2\),

\[
 \mathcal L(2s)={1\over2s-1}+O(1).                \tag{4}
\]

Under \(s=(1-z)^{-1}\), the exact contribution of the polar term of (4) to
(3) is

\[
 {1\over(1-z)^2}{1\over2/(1-z)-1}
 ={1\over1-z^2}
 ={1\over2}\left({1\over1-z}+{1\over1+z}\right). \tag{5}
\]

Hence:

* the main singularity located at \(z=-1\) contributes
  \(\frac12(-1)^N\), positive for even \(N\) and negative for odd \(N\);
* the coefficient of the complete polar model (5) is exactly
  \[
    [z^N](1-z^2)^{-1}={\bf1}_{2\mid N}.             \tag{6}
  \]

The term \(1/[2(1-z)]\) in (5) is not a real singularity of the complete
generator at \(z=1\): there \(s\to\infty\) and \(H_{\ge2}(s)\) is flat.
It cancels with the regular part when recomposing (3). Consequently,
(5)–(6) determine the leading term **of the \(j=2\) pole**, not a
dominant asymptotic for the complete coefficient \(R_N\).

In the prime–Laguerre convention of `103_14`, equation (4), the
contribution to \(\lambda_n^{\rm prime}\) carries the opposite sign. So
the local square singularity contributes \(-\frac12(-1)^N\) to that
channel.

## 3. Uniform bound for the square block

Write

\[
 S_{2,N}:=\sum_p{\log p\over p^2}L_N^{(1)}(2\log p),
 \qquad
 M_{2,N}:=\int_1^\infty x^{-2}L_N^{(1)}(2\log x)\,dx. \tag{7}
\]

The same generating function used in (5) proves exactly

\[
 M_{2,N}={\bf1}_{2\mid N}.                         \tag{8}
\]

We use two classical, elementary inequalities:

\[
 \theta(x):=\sum_{p\le x}\log p\le2(\log2)x\quad(x\ge1),       \tag{9}
\]
\[
 |L_N^{(1)}(u)|\le(N+1)e^{u/2}\quad(u\ge0).                    \tag{10}
\]

For (10), it suffices to combine Fejér's inequality
\(|L_j(u)|\le e^{u/2}\) with
\(L_N^{(1)}=\sum_{j=0}^NL_j\).

Set \(f_N(x)=x^{-2}L_N^{(1)}(2\log x)\) and
\(E_2(x)=\theta(x)-x+2\). Since \(E_2(2^-)=0\), Stieltjes integration on
\([2^-,\infty)\) gives

\[
 S_{2,N}-M_{2,N}
 =-\int_1^2f_N(x)\,dx-\int_{2^-}^\infty E_2(x)\,df_N(x).        \tag{11}
\]

From (9), for \(x\ge2\),

\[
 |E_2(x)|\le2(\log2)x.                            \tag{12}
\]

With \(u=2\log x\), the identity

\[
 {d\over du}\bigl(e^{-u}L_N^{(1)}(u)\bigr)
 =-e^{-u}L_N^{(2)}(u)                              \tag{13}
\]

and (10) produce

\[
 \left|\int_1^2f_N(x)\,dx\right|\le(\log2)(N+1). \tag{14}
\]

By Laguerre orthogonality,

\[
 \int_0^\infty e^{-u}u^2[L_N^{(2)}(u)]^2\,du
 =(N+1)(N+2).                                      \tag{15}
\]

Applying Cauchy–Schwarz to (11)–(13), with \(u_0=2\log2\), gives

\[
\begin{aligned}
 \left|\int_{2^-}^\infty E_2\,df_N\right|
 &\le2\log2\int_{u_0}^\infty
       e^{-u/2}|L_N^{(2)}(u)|\,du\\
 &\le \sqrt{2\log2\,(N+1)(N+2)}.                \tag{16}
\end{aligned}
\]

Thus,

\[
 \boxed{
 |S_{2,N}-{\bf1}_{2\mid N}|
 \le(\log2)(N+1)
 +\sqrt{2\log2\,(N+1)(N+2)}.}                   \tag{17}
\]

## 4. Bound for the \(k\ge3\) block

By (10),

\[
 \left|\sum_p\sum_{k\ge3}{\log p\over p^k}
 L_N^{(1)}(k\log p)\right|
 \le(N+1)C_{\ge3},                                \tag{18}
\]

where

\[
 C_{\ge3}:=\sum_p{\log p\over p^{3/2}(1-p^{-1/2})}
 \le\sum_{m\ge2}{\log m\over m^{3/2}(1-m^{-1/2})}<11.        \tag{19}
\]

The last constant uses no numerical computation: the terms \(m=2,3\) are
less than \(3/2\) and \(1\), respectively; for \(m\ge4\),
\((1-m^{-1/2})^{-1}\le2\), and monotonicity of
\(g(x)=\log x\,x^{-3/2}\) gives

\[
 2\sum_{m\ge4}g(m)
 \le2\left(g(4)+\int_4^\infty g(x)\,dx\right)
 <2\left({1\over4}+4\right)={17\over2}.           \tag{20}
\]

## 5. Explicit theorem and the quartic budget

From (17)–(20), with \(n=N+1\), one obtains:

**Theorem 5.1 (higher powers).** For every \(n\ge1\),

\[
 \boxed{
 |P_{n-1}^{(\ge2)}(1)|
 \le1+(11+\log2)n+\sqrt{2\log2\,n(n+1)}
 <14n+1.}                                           \tag{21}
\]

The regularization of `103_14` can now be separated unambiguously. If
\(B_n^{(p+\mathrm{pole})}\) denotes the joint limit of the \(k=1\)
channel and the pole,

\[
 B_n^{(p+\mathrm{pole})}
 :=\lim_{a\downarrow1}\left\{
 n[z^n]\log(s_a(z)-1)
 -a\sum_p{\log p\over p^a}L_{n-1}^{(1)}(a\log p)
 \right\},
 \quad s_a(z)={a\over1-z}.                         \tag{22}
\]

Indeed, for \(a>1\), the regularized Euler identity is

\[
\begin{aligned}
n[z^n]\log\!\bigl((s_a(z)-1)\zeta(s_a(z))\bigr)
={}&n[z^n]\log(s_a(z)-1)\\
&-a\sum_p\sum_{k\ge1}{\log p\over p^{ka}}
 L_{n-1}^{(1)}(ka\log p).                         \tag{23}
\end{aligned}
\]

The left-hand side converges to \(\lambda_n^{\rm prime}\), since
\((s-1)\zeta(s)\) is analytic and nonzero at \(s=1\). In the
\(k\ge2\) block, dominated convergence allows taking \(a\downarrow1\)
term by term and produces \(-P_{n-1}^{(\ge2)}(1)\). Consequently, the
exact identity is

\[
 \boxed{\lambda_n^{\rm prime}
 =B_n^{(p+\mathrm{pole})}-P_{n-1}^{(\ge2)}(1).}    \tag{24}
\]

Hence the quartic front of `104_26` becomes, exactly,

\[
 \boxed{
 D_n^{[4]}=3A_n+4B_n^{(p+\mathrm{pole})}
             -4P_{n-1}^{(\ge2)}(1),}               \tag{25}
\]

and its coercive obligation is equivalent to the **primes-and-pole-only**
inequality

\[
 \boxed{
 3A_n+4B_n^{(p+\mathrm{pole})}
 \ge {A_n\over1001}+4P_{n-1}^{(\ge2)}(1).}         \tag{26}
\]

The right-hand side of (26) is an exact, absolutely convergent budget; it
is not a new regularized unknown.

To quantify when it can be discarded even by absolute value, we use the
floor proved in `103_02`,

\[
 A_n\ge {n\over2}(\log n-2.899)\qquad(n\ge19).     \tag{27}
\]

Rational computations give:

\[
 |P_{n-1}^{(\ge2)}(1)|\le {A_n\over1001}
 \quad\text{if}\quad n\ge\lceil e^{28032}\rceil, \tag{28}
\]

\[
 4|P_{n-1}^{(\ge2)}(1)|\le {A_n\over1001}
 \quad\text{if}\quad n\ge\lceil e^{112116}\rceil.            \tag{29}
\]

The factor of four in (29), not (28), is the one relevant for `104_26`.
These thresholds do not cover the front \(n\ge150\); their purpose is to
demonstrate, without any asymptotic hypothesis, that the higher powers are
\(o(A_n)\), to remove exactly all of their regularization, and to localize
the single proportional channel still open in primes-and-pole.

## Status

- **Proved unconditionally:** (2), (3), the polar term (5)–(6), the
  uniform bound (21), the exact separation (24)–(26), and thresholds
  (28)–(29).
- **Not proved:** the sign of the complete coefficient \(R_N\), a bound
  absorbing (21) into \(A_n/1001\) starting at \(n=150\), or the
  primes-and-pole inequality (26).
- **Resulting front:** nonlocal coercivity of the joint primes-and-pole
  channel, with the higher-power correction already explicit and
  unregularized.
</content>
