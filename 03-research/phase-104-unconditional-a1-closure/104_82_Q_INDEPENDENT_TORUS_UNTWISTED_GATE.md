# 104_82 — Independence of prime lengths and the untwisted-point gate

**Result.** Linear independence over \(\mathbf Q\) of \(\{\log p\}\),
injectivity of the norm, and unique factorization diagonalize exactly
the correlations after introducing independent prime phases. They do
not, however, control the untwisted value that appears in the deep
observable of `104_75`.

There are two exact obstructions.

1. The Kronecker flow identifies a Haar average, while the arithmetic
   point is \(\theta_p=0\) for every \(p\). Evaluation at that point is
   not a functional uniformly bounded by the toral norms. In dimension
   \(J\), a polynomial supported on squarefree products has mean zero,
   \(L^2\) norm of order \(2^{J/2}\), and untwisted value of order
   \(2^J\).
2. More decisively, the off-line Euler falsifier of `104_78` can be
   deformed so that **all** its prime lengths are \(\mathbf Q\)-linearly
   independent. The Euler product remains positive, the monoid still has
   unique factorization, and the norm becomes injective. The deformation
   is a holomorphic, non-vanishing factor on \(\Re s>0\), so it does not
   cancel the outer zeros, and the deep density remains \(1/4\).

Hence the following narrow attack is closed:

```text
Q-linear independence of log p / injectivity of the norm
+ orthogonality on the torus or a prime--semiprime involution
=> deep limit for the untwisted point.
```

This does not rule out an inequality that additionally uses the specific
quantitative placement of the ordinary primes, the continuous PNT and
the Gamma factor. It does not prove the deep limit, A1 or RH.

---

## 1. What independence does prove

Fix a finite set of primes \({\cal P}\), a cutoff \(K\), and write

\[
 c_{p,k}^{(n,\varepsilon)}
 ={\log p\over p^{k(1+\varepsilon)}}
 L_{n-1}^{(1)}(k\log p).
\]

The truncated toral lift of the Mangoldt block is

\[
 Q_{n,\varepsilon}^{{\cal P},K}(\theta)
 =\sum_{p\in{\cal P}}\sum_{1\le k\le K}
 c_{p,k}^{(n,\varepsilon)}e^{ik\theta_p}.               \tag{1}
\]

At \(\theta=0\), (1) is exactly the truncation of \(Q_{n,\varepsilon}\).
By unique factorization,

\[
 \sum_{p\in{\cal P}}m_p\log p=0,
 \qquad m_p\in\mathbf Z,
 \quad\Longrightarrow\quad m_p=0\ \ (p\in{\cal P}).   \tag{2}
\]

The continuous flow

\[
 t\longmapsto (t\log p)_{p\in{\cal P}}\pmod {2\pi}
\]

is therefore equidistributed on the torus. In particular,

\[
 \lim_{T\to\infty}{1\over2T}\int_{-T}^{T}
 Q_{n,\varepsilon}^{{\cal P},K}
       ((t\log p)_p)\,dt=0,                              \tag{3}
\]

and Parseval gives the diagonal identity

\[
 \lim_{T\to\infty}{1\over2T}\int_{-T}^{T}
 \left|Q_{n,\varepsilon}^{{\cal P},K}
       ((t\log p)_p)\right|^2dt
 =\sum_{p\in{\cal P}}\sum_{k\le K}|c_{p,k}|^2.         \tag{4}
\]

The same proof holds for any divisor polynomial: distinct characters
correspond to distinct exponent vectors. This is the whole automatic
gain of unique factorization: orthogonality after averaging the twists.

## 2. The untwisted evaluation is not controlled

The obstruction already appears within a single prime tower. For

\[
 S_K(\theta)=\sum_{k=1}^{K}e^{ik\theta},
\]

one has exactly

\[
 \int_{\mathbb T}S_K=0,\qquad
 \|S_K\|_2^2=K,\qquad S_K(0)=K.                         \tag{4a}
\]

So not even orthogonality of the different powers of a prime bounds
their sum at the aligned phase.

Let \(\theta_1,\ldots,\theta_J\) be the phases of \(J\) primes and
consider

\[
 D_J(\theta)=\prod_{j=1}^{J}(1+e^{i\theta_j})-1
 =\sum_{\varnothing\ne S\subseteq\{1,\ldots,J\}}
   e^{i\sum_{j\in S}\theta_j}.                         \tag{5}
\]

Each character in (5) is the mark of a distinct squarefree product; there
are no collisions, precisely because of unique factorization. However,

\[
 \int_{\mathbb T^J}D_J\,d\theta=0,\qquad
 \|D_J\|_2^2=2^J-1,\qquad
 D_J(0)=2^J-1.                                          \tag{6}
\]

For the real polynomial \(F_J=\Re D_J\),

\[
 \int F_J=0,\qquad
 \|F_J\|_2^2={2^J-1\over2},\qquad
 F_J(0)=2^J-1.                                          \tag{7}
\]

So the norm of the evaluation at the untwisted point grows at least like
\(2^{J/2}\). Taking \(J\asymp\sqrt X\), the pointwise value already
reaches the scale \(e^{\sqrt X}\) of the deep gate even though the Haar
average is zero. There is no uniform constant transferring (3), (4), or
any \(L^2\) estimate obtained from independence, to the point \(0\).

The obstruction also settles the proposal of a prime--semiprime
involution. The character of a prime is \(e_p\), while that of \(qr\) is
\(e_q+e_r\). An involution preserving the phase would require

\[
 e_p=e_q+e_r,                                            \tag{8}
\]

or, in the length coordinate,

\[
 \log p=\log q+\log r.                                  \tag{9}
\]

Equations (8)--(9) are impossible among primes. Hence independence does
not create the cancellation: it precisely prevents an exact pairing
between the two fiber types. At \(\theta=0\), by contrast, all
characters equal \(1\), and the sign depends on the full numerical sum
of the coefficients, about which (2) contains no information.

## 3. Non-lattice falsifier with independent lengths

Start from the monoid of `104_78`. It has \(\pi_d\ge0\) formal primes of
degree \(d\), base length

\[
 a_i=d_i h,\qquad h=\log6,
\]

and zeta function

\[
 Z_0(s)={(1-3\,6^{-s})(1-2\,6^{-s})
          \over(1-6^{-s})(1-6^{1-s})}.                  \tag{10}
\]

Enumerate the formal primes by \(i\ge1\), let \(q_i\) be the \(i\)-th
rational prime, and define

\[
 \delta_i=2^{-2^{i+10}}\sqrt{q_i},\qquad
 \ell_i=a_i+\delta_i.                                  \tag{11}
\]

The sequence \((\ell_i)\) is \(\mathbf Q\)-linearly independent. Indeed,
a finite relation would give

\[
 \left(\sum_i r_id_i\right)\log6
 +\sum_i r_i2^{-2^{i+10}}\sqrt{q_i}=0,
 \qquad r_i\in\mathbf Q.                               \tag{12}
\]

The second term is algebraic. If the first coefficient were not zero,
(12) would make \(\log6\) algebraic, contradicting
Lindemann--Weierstrass. If it were zero, independence over \(\mathbf Q\)
of the square roots of distinct primes forces \(r_i=0\) for every \(i\).

Now build the free abelian monoid on these same generators, but with
norm \(|P_i|=e^{\ell_i}\). It has unique factorization and, by (12), the
norm map is injective. Its Mangoldt weights are

\[
 \widetilde\Lambda(P_i^k)=\ell_i>0.                    \tag{13}
\]

For \(\Re s>1\), its Euler product is

\[
 \widetilde Z(s)=\prod_{i\ge1}(1-e^{-s\ell_i})^{-1}.
                                                               \tag{14}
\]

Convergence is absolute: since \(\ell_i\ge a_i\) and
\(\pi_d\ll6^d/d\), for \(\sigma>1\)

\[
 \sum_i e^{-\sigma\ell_i}
 \le\sum_{d\ge1}\pi_d6^{-\sigma d}<\infty.             \tag{14a}
\]

## 4. The deformation neither moves nor cancels the outer zero

For \(\Re s>1\), (14) factors exactly as

\[
 \widetilde Z(s)=Z_0(s)G(s),
\qquad
 G(s)=\prod_{i\ge1}{1-e^{-sa_i}\over1-e^{-s\ell_i}}.   \tag{15}
\]

The factor \(G\) extends holomorphically and without zeros to the whole
half-plane \(\Re s>0\). To see this, on any compact set of that
half-plane,

\[
 \left|{\partial\over\partial x}
       \log(1-e^{-sx})\right|
 =\left|{s\over e^{sx}-1}\right|
 \le C_K e^{-\sigma_Kx}.                               \tag{16}
\]

By Bertrand's postulate, \(q_i<2^i\), and from (11) it follows that
\(\sum_i\delta_i<\infty\). Integrating (16) between \(a_i\) and
\(\ell_i\) shows that

\[
 \sum_i\{\log(1-e^{-sa_i})-\log(1-e^{-s\ell_i})\}    \tag{17}
\]

converges uniformly on compact subsets of \(\Re s>0\). Its exponential is
precisely \(G\), so it is holomorphic and never vanishes there.

The meromorphic continuation defined by (15) therefore preserves all
zeros and poles of \(Z_0\) in \(\Re s>0\). In particular it preserves the
zero

\[
 \beta_+={\log3\over\log6}>{1\over2}.                  \tag{18}
\]

With the map of `104_80`, that zero produces

\[
 z_{+,\varepsilon}
 ={\beta_+-1-\varepsilon\over\beta_+-\varepsilon},
 \qquad
 |z_{+,\varepsilon}|^{-1}\longrightarrow
 R={\log3\over\log2}>1.                               \tag{19}
\]

The summand \(-\partial_z\log G(s_\varepsilon(z))\) is holomorphic in the
unit disk. Fix \(r\) between \(|z_{+,0}|\) and the modulus of the next
singularity of \(Z_0\), with \(r<1\). For small \(\varepsilon\) it is
uniformly holomorphic on \(|z|\le r\), and Cauchy's formula bounds its
coefficients by \(O(r^{-n})\), where \(r^{-1}<R\). It cannot cancel the
leading term of (19).

More formally, if \(\Xi^0_\varepsilon\) is the regulated completion of
`104_78`, define

\[
 \widetilde\Xi_\varepsilon(s)
 =\Xi^0_\varepsilon(s)G(s+\varepsilon).                 \tag{19a}
\]

This is exactly the change that results from replacing
\(Z_0(s+\varepsilon)\) by
\(\widetilde Z(s+\varepsilon)=Z_0(s+\varepsilon)G(s+\varepsilon)\) in
the Euler channel, keeping the other edges fixed. We define
\(\widetilde\lambda_{n,\varepsilon}\) by the same Li derivative of
`104_78`, equation (17), applied to (19a).

Consequently, on the diagonal \(\varepsilon_X=e^{-X/100}\), the Li
coefficients of the deformed model satisfy

\[
 \widetilde\lambda_{n,\varepsilon_X}
 =-z_{+,\varepsilon_X}^{-n}+O(R_1^n),
 \qquad 1<R_1<R,\quad 1\le n\le X.                    \tag{20}
\]

For even degrees, (20) is \(-(1+o(1))R^n\). The same harmonic
computation of `104_78`, §4, gives

\[
 \boxed{
 {1\over H_X}\sum_{n\le X}{1\over n}
 \mathbf1_{\{\widetilde\lambda_{n,\varepsilon_X}
          +\log(n+1)\le-e^{\sqrt X}\}}
 \longrightarrow {1\over4}.}                           \tag{21}
\]

So the off-line result of `104_81` survives after removing the lattice
norm collisions and imposing full \(\mathbf Q\)-linear independence.

The summable deformation does not remove the vertical poles inherited
from \(Z_0\) on \(\Re s=1\). Hence this model does not satisfy the
continuous PNT and does not preserve the standard Riemann Gamma
completion either. It is an exact falsifier of **independence as a
sufficient input**, not of a future theorem that simultaneously uses
those additional structures.

## 5. Exact scope

```text
proved:
  Q-linear independence => toral equidistribution and Parseval;
  the untwisted evaluation is not uniformly controllable by those
  averages;
  there is no exact phase-preserving prime--semiprime involution;
  there exists a positive Euler product, with unique factorization and
  injective norm, with Q-independent prime lengths and deep density 1/4.

ruled out:
  independence / injectivity / unique factorization
  + toral averaging or exact fiber pairing
  => deep limit.

not ruled out:
  an inequality that jointly uses the continuous PNT, Gamma, and the
  exact quantitative placement of the ordinary primes.

not proved:
  the deep limit for ordinary Lambda, A1 or RH.
```
