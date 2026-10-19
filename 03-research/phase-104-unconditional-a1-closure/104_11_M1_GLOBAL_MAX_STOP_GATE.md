# 104_11 — Global M1: `max` energy, Hessian cancellation, and stop-gate

**Status:** the global factorization of the `max` kernel is now exactly closed. The
continuous compensator of `104_10` is the energy of the same kernel applied to

\[
 d\sigma=d\psi-dx.
\]

Adding it to the first term of M1, the quadratic component
\(d\psi\times d\psi\) cancels identically. No Gram form capable of supplying coercivity
survives: what remains is the original linear functional
\(-\int E\tau'\). Hence **M1 as a global operator mechanism is ruled out**. This
does not refute the sought inequality for the real von Mangoldt weights; it proves that
proving it requires a new arithmetic input that comes neither from the `max` kernel nor from
its compensator.

Section 7 records the exact successor M5: a signed Möbius–divisor
convolution in the Laguerre degree. Neither A1 nor RH is proved.

## 1. Finite formulation

Fix \(X>1\), not a prime power, and a real function
\(w\in C^1([1,X])\). Set

\[
 d\mu=\sum_{q_j<X}\ell_j\delta_{q_j},
 \qquad d\nu=\mathbf 1_{[1,X]}(x)\,dx,
 \qquad d\sigma=d\mu-d\nu,
\tag{1}
\]

where \(q_j\) are the prime powers and \(\ell_j=\Lambda(q_j)\). Its cumulative function
is

\[
 E(x)=\sigma([1,x])=\psi(x)-x+1
 \qquad(1\le x\le X).
\tag{2}
\]

Define the global energy and the first M1 term by

\[
 Q_X(w;\sigma)
 ={1\over2}\iint_{[1,X]^2}
 w(\max\{x,y\})\,d\sigma(x)d\sigma(y),
\tag{3}
\]

\[
 S_X(w;\mu)
 =\int_{[1,X]}(x-1)w(x)\,d\mu(x)
 -{1\over2}\iint_{[1,X]^2}
 w(\max\{x,y\})\,d\mu(x)d\mu(y).
\tag{4}
\]

For the von Mangoldt measure, (4) is exactly

\[
 S_X=\sum_{q_j<X}\ell_jd_jw(q_j),
 \qquad
 d_j=q_j-1-\Psi_{j-1}-{\ell_j\over2},
\tag{5}
\]

because grouping the double sum by its maximum index gives identity (8) of
`104_10`.

## 2. Global energy theorem

**Theorem 1 (the compensator is the `max` energy).** With the above conventions,

\[
 \boxed{
 Q_X(w;\sigma)
 ={1\over2}E(X)^2w(X)
 -{1\over2}\int_1^X E(x)^2w'(x)\,dx.}
\tag{6}
\]

In particular, if \(w=\tau'\), the second term of (6) is exactly the
compensator of (6) in `104_10`, boundary term included.

**Proof.** The image of the product measure \(\sigma\otimes\sigma\) under
\((x,y)\mapsto\max\{x,y\}\) has cumulative function

\[
 (\sigma\otimes\sigma)
 \{(x,y):\max(x,y)\le t\}=E(t)^2.
\]

This equality automatically incorporates the atomic diagonals. Hence

\[
 2Q_X=\int_{[1,X]}w(t)\,d(E(t)^2).
\]

Stieltjes integration by parts, using \(E(1)=0\), proves (6).
\(\square\)

There is also a continuous signed factorization:

\[
 \boxed{
 Q_X={w(X)\over2}E(X)^2
 +{1\over2}\int_1^X[-w'(t)]E(t)^2\,dt.}
\tag{7}
\]

Thus, when \(w(X)\ge0\) and \(-w'\ge0\), (7) is indeed a positive mixture of
squares of prefixes. For the real Laguerre weight, these hypotheses do not hold
uniformly.

## 3. Exact cancellation of the quadratic part

**Theorem 2 (global collapse of M1).** For every finite measure \(\mu\) on
\([1,X]\), not only for the von Mangoldt one,

\[
 \boxed{
 S_X(w;\mu)+Q_X(w;\mu-\nu)
 =-\int_1^X E(x)w(x)\,dx.}
\tag{8}
\]

Consequently, taking \(w=\tau'\), (8) is exactly

\[
 C_{n,\varepsilon}(X)=-\int_1^XE(x)\tau'(x)\,dx.
\tag{9}
\]

**Proof.** Expand (3) into its three components:

\[
 \begin{aligned}
 Q_X={}&{1\over2}\iint w(\max)\,d\mu d\mu
 -\int_{[1,X]}\left(\int_1^Xw(\max\{q,y\})\,dy\right)d\mu(q)\\
 &+{1\over2}\iint_{[1,X]^2}w(\max\{x,y\})\,dxdy.
 \end{aligned}
\tag{10}
\]

The two elementary integrals appearing here are

\[
 \int_1^Xw(\max\{q,y\})\,dy
 =(q-1)w(q)+\int_q^Xw(y)\,dy,
\tag{11}
\]

\[
 {1\over2}\iint_{[1,X]^2}w(\max\{x,y\})\,dxdy
 =\int_1^X(y-1)w(y)\,dy.
\tag{12}
\]

Adding (4), the term \(\frac12\iint w(\max)d\mu d\mu\) of (10)
exactly cancels the negative-sign term of (4). The terms \((q-1)w(q)\) also cancel.
By Fubini,

\[
 \int_{[1,X]}\int_q^Xw(y)\,dy\,d\mu(q)
 =\int_1^X\mu([1,y])w(y)\,dy.
\]

The remaining sum is

\[
 -\int_1^X\{\mu([1,y])-(y-1)\}w(y)\,dy
 =-\int_1^XE(y)w(y)\,dy,
\]

which proves (8). \(\square\)

The operational conclusion is stronger than merely observing that integrating by
parts returns to the starting point: **the only arithmetic quadratic component cancels
before any estimate is made**.

## 4. Zero Hessian: no quadratic coercivity survives

Let \(\eta\) be any finite signed measure and consider
\(\mu_t=\mu+t\eta\). In (4), the coefficient of \(t^2\) is

\[
 -{1\over2}\iint w(\max)\,d\eta d\eta;
\tag{13}
\]

in (3), the coefficient of \(t^2\) is its opposite

\[
 +{1\over2}\iint w(\max)\,d\eta d\eta.
\tag{14}
\]

Hence

\[
 {d^2\over dt^2}
 \{S_X(w;\mu_t)+Q_X(w;\mu_t-\nu)\}=0.
\tag{15}
\]

The boundary term of this cancellation can be seen without appealing to (8). If

\[
 F(x)=\eta([1,x]),
\]

Theorem 1, applied to \(\eta\), gives exactly

\[
 \boxed{
 \iint_{[1,X]^2}w(\max\{x,y\})\,d\eta(x)d\eta(y)
 =w(X)F(X)^2-\int_1^X F(x)^2w'(x)\,dx.}
\tag{15a}
\]

The second variation of \(S_X\) is the negative of the left-hand side of
(15a). The second variation of the compensator written as in (6) is

\[
 -\int_1^XF(x)^2w'(x)\,dx+w(X)F(X)^2,
\]

its exact opposite. In particular, omitting the boundary term
\(w(X)F(X)^2\) would produce a spurious residual Hessian. Moreover, (8) gives
the complete affine identity

\[
 \boxed{
 S_X(w;\mu+t\eta)+Q_X(w;\mu+t\eta-\nu)
 =S_X(w;\mu)+Q_X(w;\mu-\nu)
   -t\int_1^XF(x)w(x)\,dx.}
\tag{15b}
\]

There are no hidden second-order or higher terms due to the truncation.

This is the minimal stop-gate for a global Gram factorization:

* factorizing the compensator only factorizes (14);
* the first term contains exactly (13);
* keeping both coupled, as the plan requires, leaves neither a positive nor a negative
  quadratic form;
* any subsequent coercivity must come from an additional arithmetic property of the
  fixed measure \(d\psi\), not from the `max` kernel.

It is not claimed that every possible nonlinear argument is impossible. What is ruled out
is the specific source of positivity proposed by M1.

### 4.1 The modulus alternative loses scale in a quantified way

After (15b), taking moduli no longer estimates a collective energy: it estimates the
original linear functional. With \(w=\tau'\) and after removing the regulator, the
pointwise VK bound produces exactly the load \(\mathcal B_n\) of `103_56`, equation (20).
There it was proved that

\[
 \mathcal B_n\ge
 \exp\!\left({2\over3}n\log n+{1\over3}n\log\log n-O(n)\right),
\tag{15c}
\]

while the first-difference budget is
\(\frac12\Delta A_n=O(\log n)\). Hence, once the Hessian is canceled,
the "absolute value + VK" exit is not merely inconclusive: it loses a
superpolynomial amount against the budget. The only possibility M1 left alive was a
special signed estimate of the real measure; (8) shows that this estimate is again the
first-difference functional and not a consequence of the `max` kernel.

## 5. Exact inertia of the discrete kernel

At ordered points \(x_1<\cdots<x_M\), set \(w_j=w(x_j)\) and

\[
 K_{ij}=w_{\max(i,j)},\qquad
 \delta_j=w_j-w_{j+1}\ (j<M),\qquad \delta_M=w_M.
\tag{16}
\]

If \(v_j=(1,\ldots,1,0,\ldots,0)^T\) has its first \(j\) entries equal
to one, then

\[
 \boxed{K=\sum_{j=1}^M\delta_jv_jv_j^T.}
\tag{17}
\]

The matrix with columns \(v_j\) is triangular and invertible. By Sylvester's law of
inertia, the inertia of \(K\) is exactly the count of positive, negative, and zero signs
among

\[
 w_1-w_2,\ldots,w_{M-1}-w_M,w_M.
\tag{18}
\]

So the decomposition of `104_10` was not missing a hidden global PSD: (17)
is the maximal factorization of the kernel.

For the regulated weight

\[
 \tau(x)=x^{-a}L_n(\log x),\qquad a=1+\varepsilon,\qquad w=\tau',
\]

one has

\[
 \tau''(x)=x^{-a-2}
 \{L_n''(u)-(2a+1)L_n'(u)+a(a+1)L_n(u)\},
 \qquad u=\log x.
\tag{19}
\]

At \(x=1\), the factor in braces equals

\[
 {n(n-1)\over2}+(2a+1)n+a(a+1)>0.
\tag{20}
\]

As \(u\to\infty\), its leading term is

\[
 a(a+1){(-1)^n\over n!}u^n.
\tag{21}
\]

For every odd \(n\), \(\tau''\) changes sign. Hence the mixture of squares
(7) is indefinite, and the continuous kernel admits fine discretizations with both
inertias, for infinitely many indices in the target range. This does not assert, without
further checking, that a discretization fixed only on prime powers samples both sign
intervals. That assertion is not needed: the cancellation (15a) is also exact at those
nodes. Even before canceling the Hessians, there is no uniform PSD for the continuous
kernel.

## 6. Falsifiers under the exact axioms

### 6.1 Positive-measure relaxation

If the fixed arithmetic is relaxed and a mass \(W>0\) is moved from \(b\) to
\(a<b\), conserving total mass, (8) gives

\[
 \delta C=W\{\tau(a)-\tau(b)\}.
\tag{22}
\]

The Laguerre polynomials make (22) take both signs. Hence no argument that uses only
ordered support, positive masses, and the `max` kernel can produce the M1 bound. This
falsifier satisfies exactly the finite algebraic level of `104_10`.

### 6.2 Spectral relaxation

If a step abandons the real weights \(\Lambda(p^k)=\log p\) and keeps only
conjugation and the functional equation, the quartet

\[
 8-8\cosh(n\alpha)\cos(n\theta),
\tag{23}
\]

applies, and it has both signs. (23) is not used to refute an arithmetic theorem:
it is used only against relaxations that have already stopped using level 4 of
`104_10`.

## 7. Successor M5: signed Möbius–divisor convolution

The stop-gate above leaves an exact structure not yet exploited by M1:

\[
 \Lambda=\mu*\log.
\]

Let \(a=1+\varepsilon>1\), and define

\[
 \mathfrak M_j(a)
 =\sum_{d\ge1}{\mu(d)\over d^a}L_j(\log d),
\qquad
 \mathfrak B_k(a)
 =\sum_{m\ge1}{\log m\over m^a}L_k^{(-1)}(\log m).
\tag{24}
\]

All the series are absolutely convergent. The addition formula

\[
 L_n(x+y)=\sum_{j=0}^nL_j(x)L_{n-j}^{(-1)}(y)
\tag{25}
\]

and \(\Lambda=\mu*\log\) give the exact theorem

\[
 \boxed{
 \sum_{r\ge2}{\Lambda(r)\over r^a}L_n(\log r)
 =\sum_{j=0}^n\mathfrak M_j(a)\mathfrak B_{n-j}(a).}
\tag{26}
\]

No absolute value or Cauchy–Schwarz has been applied in the degree.

With

\[
 t={z\over1-z},
\]

the generating functions satisfy

\[
 \sum_{j\ge0}\mathfrak M_j(a)z^j
 ={1\over1-z}{1\over\zeta(a+t)},
 \qquad
 \sum_{k\ge0}\mathfrak B_k(a)z^k=-\zeta'(a+t).
\tag{27}
\]

Their product is exactly the generating function of the left-hand side of (26).

The continuous term that must remain paired is

\[
 J_{n,\varepsilon}
 =\int_1^\infty x^{-1-\varepsilon}L_n(\log x)\,dx
 ={(\varepsilon-1)^n\over\varepsilon^{n+1}}.
\tag{28}
\]

Hence

\[
 \boxed{
 C_{n,\varepsilon}
 =\sum_{j=0}^n\mathfrak M_j(1+\varepsilon)
                     \mathfrak B_{n-j}(1+\varepsilon)
  -J_{n,\varepsilon}.}
\tag{29}
\]

The two terms of (29) diverge separately as
\(\varepsilon\downarrow0\); (29) is a paired identity, not a license
to estimate them separately.

There is a normalization that automatically preserves this collision. Define

\[
 F_\varepsilon(z)
 =(\varepsilon+t)\zeta(1+\varepsilon+t).
\tag{30}
\]

Then, using the germ \(R\) from `103_66`,

\[
 \boxed{
 \sum_{n\ge0}C_{n,\varepsilon}z^n
 =-(1-z)F_\varepsilon(z)^{-1}F_\varepsilon'(z).}
\tag{31}
\]

If \(F_\varepsilon=\sum f_kz^k\) and
\(F_\varepsilon^{-1}=\sum g_jz^j\), (31) is an explicit signed convolution
between the degrees of the normalized Euler unit and those of its Möbius inverse. The
Riccati identity of E70.12 is the derivative of (31); by itself it supplies no
archimedean sign.

The new theorem M5 would have to supply is a **direct estimate of the full
convolution (29) or (31)** by

\[
 {1\over2}\Delta A_n,
\tag{32}
\]

uniform before taking \(\varepsilon\downarrow0\). Separating the norms of
\(\mathfrak M\) and \(\mathfrak B\) recreates exactly the exponential loss of
`103_70`–`103_71` and is forbidden.

## 8. Decision

```text
proved:
  the continuous compensator is the global energy of the max kernel;
  the M1 identity is S_X + Q_X with all boundary terms;
  the mu x mu part cancels exactly;
  the total Hessian with respect to the measure is zero;
  the inertia of the max kernel is given exactly by its first differences;
  the Laguerre kernel is indefinite for every odd index;
  the signed Möbius–divisor factorization (26)--(31).

ruled out:
  M1 as a global source of coercivity or a Gram matrix;
  any PSD obtained by factorizing only one of the two terms;
  estimating the two factors of the degree convolution separately.

not proved:
  a special inequality for the real von Mangoldt weights;
  (32), A1, or RH.

recommended successor:
  M5, exclusively in the coupled form (29) or (31).
```

M3 may still exist as a non-local reorganization of lobes, but the stationary map does not
introduce an arithmetic input. After the exact cancellation of
M1, M5 is the successor with a concrete additional structure not yet consumed: the Möbius
inversion within the degree convolution.

## Mechanical verification

`tools/m1_global_hessian_check.py` verifies, using `Fraction` with no floating point,
the finite identities (6), (8), and (15a). It includes two perturbations: one of zero
total mass and another with \(F(X)\ne0\), so that an incorrect sign or the omission
of the boundary term \(w(X)F(X)^2\) makes the check fail.
</content>
