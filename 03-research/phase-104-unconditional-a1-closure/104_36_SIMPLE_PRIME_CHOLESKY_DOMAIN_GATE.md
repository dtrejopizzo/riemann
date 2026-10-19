# 104_36 — Simple-prime–pole Cholesky and the residue-domain gate

**Status.** The simple-prime–pole channel of `104_32` and `104_35`
admits an exact Cholesky/large-sieve factorization before reaching the Li
point. The factorization jointly preserves every prime: its norm is the
squared modulus of the complete prime–pole difference, not a sum of
per-prime absolute values.

Continuing that norm to the Li point, however, does not exist. Each
critical zero produces a pole approaching the Hardy boundary as the
regulator tends to \(a\downarrow1\), and the squared norm grows at least
like \((a-1)^{-1}\). A zero with \(\Re\rho>a/2\) places the pole inside
the Laplace half-plane and makes even membership in
\(L^2(0,\infty)\) impossible. For two consecutive prefixes, membership in
\(L^2\) already implies there are no such zeros. In the limit
\(a\downarrow1\) that condition contains RH.

Hence the natural Cholesky approach does not produce the coercivity of
(26) in `104_32`: it loses precisely the signed cancellation that keeps
the scalar moment finite. The document proves neither that inequality,
nor A1, nor RH.

## 1. Pre-registration and non-duplication

The target is

\[
 3A_n+4B_n^{(p+\mathrm{pole})}
 \ge {A_n\over1001}+4P_{n-1}^{(\ge2)}(1),            \tag{1}
\]

equivalent to (26) of `104_32`. A single idea is tested: writing
\(B_{n,a}^{(p+\mathrm{pole})}\) as the inner product of a
prime–continuum discrepancy vector with the hard-edge prefix, and using a
quadratic norm that keeps all the cross terms.

`104_11` factorizes the `max` kernel of M1 and proves that its Hessian
cancels when the linear functional is recomposed. `104_31` studies the
birth–death flow in the degree. `104_33` carries the flag symbol to the
critical line and separates boundary from residues. `104_35` obtains the
exact \(\theta-x\) formula and rules out the simple Selberg Riccati as an
autonomous source of sign.

What is new here is different: the global Cholesky vector of the simple
channel is built, its norm is computed via Plancherel, and its domain is
determined exactly via the residues of \(Q(s)=\sum_p\log p\,p^{-s}\).

The falsifier is the rational quartet

\[
 w={i\over2},\qquad \rho={1\over1-w}={4+2i\over5}.       \tag{2}
\]

At index \(n=152\), its Cholesky mode grows like
\(e^{3x/10}\) and does not belong to \(L^2\). So the factorization fails,
rather than falsely certifying anything, against an off-line divisor.

## 2. Hard-edge semigroup and discrepancy vector

Let

\[
 \mathcal H=L^2(0,\infty),\qquad
 (S_tf)(x)=f(x-t){\bf1}_{x\ge t},\qquad
 T_t=e^{-t/2}S_t.                                      \tag{3}
\]

Semigroup \(T_t\) is contractive. For

\[
 g_n(x)=e^{-x/2}L_{n-1}^{(1)}(x)                       \tag{4}
\]

Laguerre orthogonality and the identity
\(L_{n-1}^{(1)}=\sum_{j=0}^{n-1}L_j\) give

\[
 \|g_n\|_2^2=n.                                        \tag{5}
\]

The translation correlation of `104_28` becomes

\[
 \boxed{\langle T_tg_n,g_n\rangle
       =e^{-t}L_{n-1}^{(1)}(t).}                       \tag{6}
\]

Set

\[
 d\theta(y)=\sum_p\log p\,\delta_p(dy),
 \qquad d\sigma(y)=dy-d\theta(y).                     \tag{7}
\]

For \(a>2\), the Bochner integral

\[
 \boxed{
 V_{n,a}:=a\int_1^\infty T_{a\log y}g_n\,d\sigma(y)}   \tag{8}
\]

converges absolutely in \(\mathcal H\), because

\[
 \|T_{a\log y}g_n\|_2=\sqrt n\,y^{-a/2}
\]

and both \(\int_1^\infty y^{-a/2}dy\) and
\(\sum_p\log p\,p^{-a/2}\) converge. From (6),

\[
\begin{aligned}
 \langle V_{n,a},g_n\rangle
 &={a}\int_1^\infty y^{-a}L_{n-1}^{(1)}(a\log y)
       \{dy-d\theta(y)\}\\
 &=B_{n,a}^{(p+\mathrm{pole})}.
\end{aligned}                                             \tag{9}
\]

The second equality is exactly (4)–(6) of `104_35`, including the
continuous pole and its sign. By Cauchy–Schwarz,

\[
 B_{n,a}^{(p+\mathrm{pole})}
 \ge-\sqrt n\,\|V_{n,a}\|_2.                         \tag{10}
\]

This is the coercive-type lower bound (1) would need if the norm remained
uniformly finite as the regulator is removed.

## 3. Exact large-sieve identity

Adopt

\[
 Q(s)=\sum_p{\log p\over p^s},\qquad
 M(s)={1\over s-1}-Q(s)                               \tag{11}
\]

in \(\Re s>1\). The Fourier transform of (4), extended by zero to the
line, is

\[
 \widehat g_n(t)
 =1-\left({-1/2+it\over1/2+it}\right)^n.              \tag{12}
\]

For \(a>2\), every integration in (8) is absolute and

\[
 \boxed{
 \widehat V_{n,a}(t)
 =a\widehat g_n(t)M\!\left(a(1/2+it)\right).}          \tag{13}
\]

Plancherel gives the sought collective Cholesky:

\[
 \boxed{
 \|V_{n,a}\|_2^2
 ={a^2\over2\pi}\int_{-\infty}^{\infty}
 |\widehat g_n(t)|^2
 \left|M\!\left(a(1/2+it)\right)\right|^2dt.}        \tag{14}
\]

The sum over primes and the pole are formed inside \(M\) before taking
the modulus. Expanding (14) brings in every interaction between two
primes and between primes and the continuum. Neither term-by-term
positivity nor the triangle inequality has been used in the Euler sum.

The problem with (14) is not algebraic, but its domain: the condition
\(a>2\) places the entire integration line within the half-plane of the
Euler product. Reaching \(a=1\) moves that line onto the critical line.

## 4. Exact form in \(\theta-x\)

Although (8) is not a Bochner integral for \(a\le2\), it defines a
pointwise locally square-integrable function: for each \(x\) only
\(y\le X=e^{x/a}\) enter. Let

\[
 D_\theta(X)=X-1-\theta(X).                             \tag{15}
\]

Since

\[
 (T_{a\log y}g_n)(x)
 =e^{-x/2}L_{n-1}^{(1)}(x-a\log y){\bf1}_{y\le X},      \tag{16}
\]

a Stieltjes integration, using
\((L_{n-1}^{(1)})'=-L_{n-2}^{(2)}\), gives for \(n\ge2\)

\[
 \boxed{
 V_{n,a}(x)=ae^{-x/2}\left[
 nD_\theta(X)-a\int_1^X{D_\theta(y)\over y}
 L_{n-2}^{(2)}(x-a\log y)\,dy\right].}              \tag{17}
\]

For \(n=1\), the integral term vanishes:

\[
 \boxed{V_{1,a}(x)=ae^{-x/2}D_\theta(e^{x/a}),}        \tag{18}
\]

and hence

\[
 \boxed{\|V_{1,a}\|_2^2
 =a^3\int_1^\infty D_\theta(X)^2X^{-a-1}\,dX}         \tag{19}
\]

if either side is finite. The Cholesky norm already contains, at its
first state, the full quadratic energy of the PNT error. It is not a
weaker estimator of the linear moment.

## 5. Laplace transform and the residues of the zeros

For \(\Re z>1/a-1/2\), the Laplace transform of (17) can be computed in
the half-plane of absolute convergence. Defining

\[
 G_n(z)=\int_0^\infty e^{-zx}g_n(x)\,dx
 =1-\left({z-1/2\over z+1/2}\right)^n,                \tag{20}
\]

one obtains

\[
 \boxed{
 \mathcal L V_{n,a}(z)
 =aG_n(z)M\!\left(a(z+1/2)\right).}                  \tag{21}
\]

The relevant meromorphic continuation needs no separation of prime
powers. If

\[
 \mathcal L_\zeta(s)=-{\zeta'\over\zeta}(s),
\]

Möbius inversion gives

\[
 Q(s)=\sum_{k\ge1}\mu(k)\mathcal L_\zeta(ks).         \tag{22}
\]

In \(\Re s>1/2\), the terms \(k\ge2\) are regular and the series converges
normally on compact sets, except at the boundary \(s=1/2\). Hence, if
\(\rho\) is a nontrivial zero of multiplicity \(m_\rho\), then \(M\) has
residue \(+m_\rho\) at \(s=\rho\).

Equation (21) then has a pole at

\[
 z_{\rho,a}={\rho\over a}-{1\over2}                   \tag{23}
\]

with exact residue

\[
 \boxed{
 \mathop{\mathrm{Res}}_{z=z_{\rho,a}}
 \mathcal LV_{n,a}(z)
 =m_\rho\left[1-\left(1-{a\over\rho}\right)^n\right].} \tag{24}
\]

This gives a domain gate, not merely a bad bound. If
\(V_{n,a}\in L^2(0,\infty)\), its Laplace transform is holomorphic on
\(\Re z>0\). Consequently, for each zero with
\(\Re\rho>a/2\), necessarily

\[
 \left(1-{a\over\rho}\right)^n=1.                   \tag{25}
\]

Condition (25) cannot hold for two consecutive indices. If it held for
\(n\) and \(n+1\), their quotient would give \(1-a/\rho=1\), impossible.
This proves:

> **Domain theorem.** If \(V_{n,a}\) and \(V_{n+1,a}\) belong to
> \(L^2(0,\infty)\), then \(\zeta\) has no zeros in
> \(\Re s>a/2\). In particular, having the Hilbert factorization for
> every prefix \(n\ge150\) and for \(a\downarrow1\) already excludes every
> zero with \(\Re\rho>1/2\), that is, already contains RH by the
> functional symmetry.

No explicit formula was assumed to prove this theorem: uniqueness of the
Laplace transform of an \(L^2\) function and residue (24) suffice.

## 6. Critical zeros make the norm diverge even under RH

The problem persists even if every zero is critical. Fix a zero
\(\rho=1/2+i\gamma\) and an index \(n\) for which

\[
 1-\left(1-{1\over\rho}\right)^n\ne0.                \tag{26}
\]

Such a zero exists for every \(n\): there are infinitely many critical
zeros, while (26) can fail only when \(1-1/\rho\) belongs to the finite
set of \(n\)-th roots of unity.

For \(a>1\), pole (23) lies at distance

\[
 \delta_a={a-1\over2a}                                      \tag{27}
\]

to the left of the imaginary axis. Isolating that pole in a disc with no
other zeros, (21) has on the boundary the form

\[
 aG_n(it)M(a(1/2+it))
 ={R_{n,a}\over\delta_a+i(t-\gamma/a)}+H_{n,a}(t),     \tag{28}
\]

where \(R_{n,a}\) tends to the nonzero value of (26) multiplied by
\(m_\rho\), and \(H_{n,a}\) remains uniformly bounded on a fixed interval
after subtracting the principal part. Integrating the square over that
interval,

\[
 \int {dt\over\delta_a^2+(t-\gamma/a)^2}
 \asymp{1\over\delta_a},                                  \tag{29}
\]

one obtains, as \(a\downarrow1\),

\[
 \boxed{\|V_{n,a}\|_2^2\ge {c_{n,\rho}\over a-1}}
 \qquad(c_{n,\rho}>0),                                     \tag{30}
\]

if the continuation belongs to \(L^2\). At \(a=1\) the pole falls exactly
on the boundary, and the multiplier is not square-integrable.

Divergence (30) is unconditional because the existence of infinitely many
zeros on the critical line is Hardy's theorem. The scalar quantity
\(B_{n,a}^{(p+\mathrm{pole})}=\langle V_{n,a},g_n\rangle\) does have a
finite limit: the projection against the fixed test \(g_n\), which decays
exponentially, integrates each boundary mode. The Cholesky norm removes
that damping test and squares the boundary pole.

## 7. Quantitative off-line falsifier

For quartet (2),

\[
 \Re\rho-{1\over2}={3\over10}.                       \tag{31}
\]

At \(a=1\) and \(n=152\),

\[
 G_{152}(\rho-1/2)
 =1-w^{152}=1-2^{-152}>0.                              \tag{32}
\]

By (23)–(24), the Cholesky vector would have a nonzero mode proportional
to

\[
 e^{(3/10+2i/5)x},                                      \tag{33}
\]

which does not belong to \(L^2(0,\infty)\). To fix the normalization,
this quartet's contribution to the Li coefficient is

\[
 Q_n^{\mathrm{off}}
 :=4-2\Re(w^n+w^{-n})
 =4-4\cosh(n\log2)\cos(n\pi/2).                      \tag{34}
\]

Since \(152\equiv0\pmod4\),

\[
 \boxed{Q_{152}^{\mathrm{off}}
 =4-4\cosh(152\log2)<0.}                               \tag{35}
\]

So the mechanism is not blind to the falsifier: its domain breaks before
producing a false inequality. `tools/simple_prime_cholesky_gate.py`
verifies (31)–(32) and the rational Laguerre transforms with `Fraction`.

## 8. Consequence for the proportional front

From (10), a sufficient condition for (1) would have been

\[
 \sqrt n\,\liminf_{a\downarrow1}\|V_{n,a}\|_2
 \le {\left(3-1/1001\right)A_n
          -4P_{n-1}^{(\ge2)}(1)\over4}.                \tag{36}
\]

The right-hand side is finite. The left-hand side diverges by (30).
Hence (36), and every proof applying Cauchy–Schwarz to this vector with no
additional subtraction, is ruled out.

Subtracting the modes (24) before taking the norm makes the construction
finite, but requires identifying every critical residue and deciding what
to do with the off-line interior residues. Returning those contributions
to the projection onto \(g_n\) exactly recovers the Li terms the
inequality aims to control. That renormalization is not a new bound.

## Decision

```text
proved unconditionally:
  the prime--pole discrepancy vector (8) for a>2;
  the scalar identity (9) and the collective Cholesky/large-sieve (14);
  the exact theta-x formula (17)--(19);
  the Laplace transform (21) and each zero's residue (24);
  two consecutive L2 prefixes => region Re rho <= a/2;
  norm divergence >= c/(a-1) from a critical zero;
  exponential breakdown for the rational off-line quartet.

ruled out:
  Cauchy--Schwarz on the global vector as a closure of (1);
  continuing the safe norm from a=2+ down to a=1 without paying residues;
  calling "large sieve" the subtraction of those residues without
  reinserting Li.

remains open:
  a one-sided bound for the signed projection
  <V_{n,a},g_n> surviving the limit without controlling the full norm;
  (1), A1, and RH.
```
</content>
