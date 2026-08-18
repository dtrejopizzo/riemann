# 106.73 — Large-prime filter atoms and midpoint derivative sampling

## Purpose and verdict

Document 106.71 gives the exact cofinal filter-bank law but uses only a
global superexponential upper bound for the omitted Euler bank.  The
finite-head diagnostics suggest a more specific signal-processing picture:
when the mode span grows, a new prime channel may raise a newly exposed
direction.  This note determines what a literal large-prime channel actually
measures.

For the elementary mean-periodic mode

\[
 \chi_z(x)=\frac{\cos(zx)}{\cosh(x/2)}
\]

and a prime \(p\), the overlap \(K(x)K(x-\log p)\) is concentrated at

\[
 x=\frac12\log p
 \quad\text{with width}\quad p^{-1/2}.
\]

Consequently the atom is, to leading order, a rank-one derivative sampler.
Uniformly on every fixed compact \(z\)-block,

\[
 \boxed{
 \frac{\log p}{\sqrt p}\,
 \mathcal J_{\log p}(z,w)
 =\beta_p\,\overline{A_p(z)}A_p(w)+E_p(z,w),}
 \tag{1}
\]

where

\[
\begin{aligned}
 A_p(z)
 &=2z\sin\!\left(\frac{z\log p}{2}\right)
   +\tanh\!\left(\frac{\log p}{4}\right)
    \cos\!\left(\frac{z\log p}{2}\right),\\
 \beta_p
 &=C_\Xi^2\pi^3(\log p)p^2e^{-2\pi p}
   (1+p^{-1/2})^{-2},                              \tag{2}
\end{aligned}
\]

and the error is smaller by one power of \(p\), without any division by
\(A_p(z)\).  The latter qualification is essential because the derivative
sample can vanish.

This proves the literal moving-filter interpretation.  It also gives its
quantitative limitation: large-prime channel strengths decay like
\((\log p)p^2e^{-2\pi p}\).  A Vandermonde determinant of their phase samples
can prove finite-dimensional injectivity, but by itself it cannot give a
uniform lower frame bound.  Such a bound would additionally require a
quantitative comparison with the conditioning of the mode Gram matrix and
with the shrinking complete-form deficit.  No sign of the full compensated
form is asserted here.

## 1. Semantic audit

The following earlier results are adjacent but do not contain (1).

* Documents 106.32 and 106.38 give the exact theta dilation and the
  divisor/fractional/central decomposition of every prime-power jump.
* Document 106.67 proves the coarse bound
  \(\mathcal J_u(q)\ll_M e^{-ce^u}\|q\|^2\) on a fixed mode space.
* Document 106.71 packages the finite heads as a cofinal analysis bank and
  records that its conditioning constant may grow with the mode dimension.
* Phases 47 and 50 investigate prime phases and show that multiplicative
  independence yields qualitative transversality, not a uniform Riesz lower
  bound.

The full research tree was searched for midpoint localization, large-prime
Laplace asymptotics, derivative sampling, and rank-one prime atoms.  The
large-prime expansion below, including its constant and the exact sample
\(A_p\), is not present there.  It is an asymptotic refinement of the already
proved all-atoms flag, not a new positivity mechanism.

## 2. The literal atom kernel

Use the normalization of 106.31:

\[
 \widehat K(z)=\Xi(z),
\]

and, for \(s\ge0\),

\[
 K(s)=C_\Xi\sum_{m\ge1}
 \left(2\pi^2m^4e^{9s/2}-3\pi m^2e^{5s/2}\right)
 e^{-\pi m^2e^{2s}}.                              \tag{3}
\]

The function \(K\) is even.  For complex \(z,w\), define the Hermitian
polarization of the displacement atom by

\[
 \mathcal J_u(z,w)
 :=\int_{\mathbb R}K(x)K(x-u)
 \overline{\Delta_u\chi_z(x)}\,
 \Delta_u\chi_w(x)\,dx,                           \tag{4}
\]

where

\[
 \Delta_u\chi_z(x)=\chi_z(x)-\chi_z(x-u).          \tag{5}
\]

The diagonal is the literal positive jump
\(\mathcal J_u(\chi_z)=\mathcal J_u(z,z)\).

Put

\[
 u=\log p,\qquad t=\frac u2,\qquad x=t+y.          \tag{6}
\]

Evenness gives the exact midpoint form

\[
\boxed{
\begin{aligned}
 \mathcal J_{\log p}(z,w)
 =\int_{\mathbb R}K(t+y)K(t-y)
 \overline{d_{p,z}(y)}d_{p,w}(y)\,dy,\\
 d_{p,z}(y)=\chi_z(t+y)-\chi_z(t-y).
\end{aligned}}                                     \tag{7}
\]

Thus both the kernel and the difference are centered at the same physical
point \(t=(\log p)/2\).

## 3. Theta localization at the midpoint

### Lemma 1 — Uniform first-theta-atom expansion

For \(s\to+\infty\),

\[
\boxed{
 K(s)=2C_\Xi\pi^2e^{9s/2}e^{-\pi e^{2s}}
 \left\{1-\frac{3}{2\pi}e^{-2s}
 +O\!\left(e^{-3\pi e^{2s}}\right)\right\}.}      \tag{8}
\]

For each fixed derivative, the analogous estimate holds after replacing
\(3\pi\) by any fixed smaller positive exponent constant.

#### Proof

Separate the \(m=1\) term in (3).  It equals the displayed main term and
its explicit \(e^{-2s}\) correction.  Relative to it, the \(m\)-th term for
\(m\ge2\) is bounded by a fixed polynomial in \(m\) and \(e^s\), multiplied
by

\[
 \exp\{-\pi(m^2-1)e^{2s}\}.
\]

The first exponent is \(3\pi e^{2s}\), at \(m=2\), and the rest is bounded
by a convergent geometric majorant after decreasing the exponential
constant.  Differentiation changes only the polynomial prefactor.  \(\square\)

For \(|y|\le p^{-2/5}\), Lemma 1 gives

\[
\boxed{
 K(t+y)K(t-y)
 =4C_\Xi^2\pi^4p^{9/2}
 e^{-2\pi p\cosh(2y)}\{1+O(p^{-1})\}.}             \tag{9}
\]

The error is uniform in that interval.  Outside it, the product is smaller
than its midpoint scale by \(e^{-c p^{1/5}}\), up to a fixed polynomial in
\(p\).  Indeed, for \(|y|\le t\),

\[
 e^{2(t+y)}+e^{2(t-y)}=2p\cosh(2y),                \tag{10}
\]

and for \(|y|>t\), evenness makes the exponent still larger.  This proves
the precise aperture statement

\[
 \boxed{|y|\asymp p^{-1/2}.}                       \tag{11}
\]

### Lemma 2 — The midpoint Gaussian moment

As \(p\to\infty\),

\[
\boxed{
 \int_{\mathbb R}y^2e^{-2\pi p\cosh(2y)}\,dy
 =\frac{e^{-2\pi p}}{16\pi p^{3/2}}
 \{1+O(p^{-1})\}.}                                \tag{12}
\]

#### Proof

Use

\[
 \cosh(2y)=1+2y^2+O(y^4)
\]

on \(|y|\le p^{-2/5}\), and set
\(v=(4\pi p)^{1/2}y\).  Dominated convergence with one further Taylor term
gives relative error \(O(p^{-1})\).  The Gaussian moment is

\[
 \int_{\mathbb R}y^2e^{-4\pi py^2}\,dy
 =\frac1{16\pi p^{3/2}}.
\]

The complement is \(e^{-cp^{1/5}}\) times the main scale by (10).  \(\square\)

## 4. The derivative sample

Let \(\mathcal B\) be a compact subset of

\[
 \{z\in\mathbb C:|\mathrm{Im}\,z|<1/2\},
\]

and put

\[
 b=\max_{z\in\mathcal B}|\mathrm{Im}\,z|<\frac12. \tag{13}
\]

For fixed derivative order \(j\), uniformly on \(\mathcal B\),

\[
 |\chi_z^{(j)}(s)|
 \le C_{\mathcal B,j}e^{-(1/2-b)s},\qquad s\ge1.  \tag{14}
\]

At \(s=t=(\log p)/2\), direct differentiation gives

\[
\boxed{
 2\chi_z'(t)
 =-\mathrm{sech}(t/2)A_p(z),}               \tag{15}
\]

with \(A_p\) as in (2).  Taylor expansion about the midpoint therefore
gives, uniformly for \(|y|\le p^{-2/5}\),

\[
\boxed{
 d_{p,z}(y)
 =-\mathrm{sech}(t/2)A_p(z)y
 +O_{\mathcal B}\!\left(
 p^{-1/4+b/2}|y|^3\right).}                        \tag{16}
\]

Equation (15) shows that the phase vector is not an ad hoc trigonometric
choice:

\[
 A_p(z)=-2\cosh(t/2)\chi_z'(t).                    \tag{17}
\]

The prime channel samples the derivative of the physical quotient mode at
the midpoint of its two translated theta packets.

## 5. The asymptotic rank-one theorem

### Theorem 3 — A large prime is a midpoint derivative channel

For every compact \(\mathcal B\) as above, uniformly for
\(z,w\in\mathcal B\),

\[
\boxed{
 \mathcal J_{\log p}(z,w)
 =\alpha_p\overline{A_p(z)}A_p(w)+R_p(z,w),}        \tag{18}
\]

where

\[
\boxed{
\begin{aligned}
 \alpha_p
 &=\frac{C_\Xi^2\pi^3}{4}p^3
   \mathrm{sech}^2\!\left(\frac{\log p}{4}\right)
   e^{-2\pi p}\\
 &=C_\Xi^2\pi^3p^{5/2}e^{-2\pi p}
   (1+p^{-1/2})^{-2},                              \tag{19}\\
 |R_p(z,w)|
 &\le C_{\mathcal B}\alpha_p p^{b-1}.             \tag{20}
\end{aligned}}
\]

After multiplying by the literal von Mangoldt weight, (1) holds with

\[
 |E_p(z,w)|\le C_{\mathcal B}\beta_pp^{b-1}.       \tag{21}
\]

#### Proof

Insert (9) and (16) in (7).  The leading product is

\[
 \mathrm{sech}^2(t/2)
 \overline{A_p(z)}A_p(w)y^2.
\]

Combining it with (12) gives

\[
 4C_\Xi^2\pi^4p^{9/2}
 \mathrm{sech}^2(t/2)
 \frac{e^{-2\pi p}}{16\pi p^{3/2}},
\]

which is exactly (19).

The error in the product of the two differences in (16) is bounded by

\[
 C_{\mathcal B}p^{-1/2+b}(|y|^4+|y|^6).
\]

Its Gaussian integral is \(O(\alpha_pp^{b-1})\).  The \(O(p^{-1})\)
relative error in (9), the \(O(p^{-1})\) correction in the Laplace moment,
and the theta-tail contribution obey the same bound.  The region
\(|y|>p^{-2/5}\) is smaller by \(e^{-cp^{1/5}}\), so it is absorbed as
well.  This proves (18)--(20).  Multiplication by
\((\log p)/\sqrt p\) proves (1) and (21).  \(\square\)

The theorem is additive rather than relative.  It remains valid when
\(A_p(z)=0\), whereas a statement of the form
\(\mathcal J=\alpha_p|A_p|^2(1+o(1))\) would be false at such phases.

### Corollary 4 — Prime powers

For \(n=p^k\to\infty\), replace \(p\) by \(n\) in \(A_p\) and
\(\alpha_p\),
but retain \(\Lambda(n)=\log p\).  Thus the weighted strength is

\[
 \beta_{p^k}
 =C_\Xi^2\pi^3(\log p)(p^k)^2e^{-2\pi p^k}
 (1+p^{-k/2})^{-2}.                               \tag{22}
\]

In particular, higher prime powers are much smaller than the first-power
channel of the same prime.

## 6. Finite blocks and the Vandermonde question

Fix distinct elementary modes \(z_1,\ldots,z_d\in\mathcal B\), and define

\[
 v_p=(\overline{A_p(z_1)},\ldots,
      \overline{A_p(z_d)})^{\mathsf T}.             \tag{23}
\]

Let \(P_p\) be the \(d\times d\) matrix of the weighted literal prime atom.
Theorem 3 gives

\[
\boxed{
 P_p=\beta_pv_pv_p^*+\mathcal E_p,
 \qquad
 \|\mathcal E_p\|\le C_{\mathcal B,d}\beta_pp^{b-1}.}
                                                               \tag{24}
\]

Also

\[
 \|v_p\|^2\le C_{\mathcal B,d}p^b,                \tag{25}
\]

and hence

\[
\boxed{
 \|P_p\|\le C_{\mathcal B,d}
 (\log p)p^{2+b}e^{-2\pi p}.}                     \tag{26}
\]

Summing over primes, or more strongly over all integers, gives the sharp
qualitative tail scale

\[
\boxed{
 \left\|\sum_{p\ge P}P_p\right\|
 \le C_{\mathcal B,d}(\log P)P^{2+b}e^{-2\pi P}.} \tag{27}
\]

This refines the unspecified \(e^{-cP}\) constant in 106.67 on a fixed
elementary block.

For exactly \(d\) leading rank-one channels \(p_1,\ldots,p_d\), let

\[
 V=(A_{p_i}(z_j))_{1\le i,j\le d},
 \qquad W=\mathrm{diag}(\beta_{p_1},\ldots,\beta_{p_d}).
                                                               \tag{28}
\]

Their leading Gram matrix is \(V^*WV\), so

\[
\boxed{
 \det(V^*WV)
 =\left(\prod_{i=1}^d\beta_{p_i}\right)|\det V|^2.}             \tag{29}
\]

The determinant \(\det V\) is a trigonometric-exponential sampling
determinant.  It is generically nonzero, and nonvanishing proves that this
particular finite sample is injective.  However, Hadamard's inequality and
(25) give

\[
 |\det V|^2\le C_{\mathcal B,d}\prod_{i=1}^dp_i^b.              \tag{30}
\]

Therefore even an optimally nonzero phase determinant does not cancel the
factor

\[
 \exp\!\left(-2\pi\sum_{i=1}^dp_i\right)          \tag{31}
\]

coming from the physical theta overlaps.  Vandermonde nonvanishing is an
injectivity statement, not a uniform frame estimate.

There is an equally direct rank count.  For \(r<d\), choose a coefficient
vector \(a\ne0\) orthogonal to
\(v_{p_1},\ldots,v_{p_r}\).  Then (24) gives

\[
 a^*\left(\sum_{i=1}^rP_{p_i}\right)a
 \le C_{\mathcal B,d}\|a\|^2
 \sum_{i=1}^r\beta_{p_i}p_i^{b-1}.                \tag{32}
\]

Thus the small non-rank-one remainder, rather than the leading samples,
is all that these \(r\) channels see in that direction.

## 7. Comparison with mode conditioning

Let

\[
 N_d=(\langle\chi_{z_i},\chi_{z_j}\rangle_{L^2(\mu_K)})_{i,j}
                                                               \tag{33}
\]

be the physical norm Gram matrix.  It is positive definite for each fixed
block.  Normalization changes (27) into

\[
\boxed{
 \left\|N_d^{-1/2}
 \left(\sum_{p\ge P}P_p\right)N_d^{-1/2}\right\|
 \le
 \frac{C_{\mathcal B,d}}{\lambda_{\min}(N_d)}
 (\log P)P^{2+b}e^{-2\pi P}.}                     \tag{34}
\]

Consequently a normalized negative deficit of size \(\eta_d\) cannot be
repaired solely by the prime tail beyond \(P\) if

\[
 \frac{C_{\mathcal B,d}}{\lambda_{\min}(N_d)}
 (\log P)P^{2+b}e^{-2\pi P}<\eta_d.               \tag{35}
\]

Formula (35) is the quantitative balance which the moving-filter proposal
must meet.  It has two unknown moving quantities:

1. the normalized complete-form deficit \(\eta_d\);
2. the conditioning scale \(\lambda_{\min}(N_d)\).

Neither multiplicative independence nor the prime number theorem compares
those quantities to the superexponential factor in (35).

There is also a resolution condition.  If the largest frequency in a
moving block is \(Z\), tracking the first and third derivatives in (16)
shows that the dimensionless aperture parameter in the additive remainder
is

\[
 \frac{(1+Z)^2}{p}.                                \tag{36}
\]

More explicitly, the proof gives on
\(\{|z|,|w|\le Z,\ |\mathrm{Im}\,z|,
|\mathrm{Im}\,w|\le b\}\)
\[
 |R_p(z,w)|
 \le C_b\alpha_pp^b
 \left\{\frac{(1+Z)^4}{p}
       +\frac{(1+Z)^6}{p^2}\right\}.               \tag{36a}
\]
Compared with the natural upper scale
\(\alpha_pp^b(1+Z)^2\), this yields (36).

Thus the rank-one derivative-sampling regime for a growing block requires

\[
 p\gg Z^2.                                         \tag{37}
\]

At that scale the raw channel strength is already at most
\(e^{-cZ^2}\), apart from polynomial factors.  A cofinal frame theorem could
still hold if the exposed deficits vanish on the same or a smaller scale,
or if the norm Gram conditioning supplies the matching normalization.  But
that comparison is an additional theorem; it does not follow from the
Vandermonde determinant.

This explains the finite computations without extrapolating them.  The
small primes \(2,3,5,7\) are pre-asymptotic, sizeable channels.  The fact
that \(7\) repairs a direction exposed by more modes is compatible with
(1), but it does not imply that successively large primes carry a uniform
amount of energy.  In the asymptotic bank they are increasingly narrow and
increasingly weak derivative sensors.

## 8. Status

The following statements are proved here.

* The exact midpoint of the \(p\)-channel is \((\log p)/2\), and its aperture
  is \(p^{-1/2}\).
* On every fixed elementary mode block, its leading feature is the
  rank-one derivative sample \(A_p\), with the explicit constant (19).
* The literal von Mangoldt-weighted strength is
  \((\log p)p^2e^{-2\pi p}\), with a uniform additive error.
* The fixed-block prime tail satisfies the refined bound (27).
* A Vandermonde lower bound must additionally overcome the physical weights
  and the mode Gram conditioning; nonvanishing alone cannot do so.

The missing sign is unchanged: one must compare the complete normalized
prime--Gamma bank with the polar threshold.  Equations (34)--(37) specify
the exact quantitative data that a cofinal sampling proof would have to
add.
