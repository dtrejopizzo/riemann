# 104_102 — Analytic/rational rigidity of the Landau transform

## Result

Set

\[
 \ell_j(s)=\left(-{d\over ds}\right)^j
             \left(-{\zeta'(s)\over\zeta(s)}\right)
 =\sum_{m\ge2}{\Lambda(m)(\log m)^j\over m^s},
 \qquad \Re s>1.
 \tag{1}
\]

This document extends `104_95` from polynomials to analytic and rational
transformations. The exact result is as follows.

> **Theorem A (analytic rigidity).** Let
> \(\Phi\) be a holomorphic germ at
> \(0\in\mathbb C^{r+1}\), and for \(\Re s\) large define
> \[
>  F(s)=\Phi(\ell_0(s),\ldots,\ell_r(s))
>      =\sum_{n\ge1}{a_n\over n^s}.
>  \tag{2}
> \]
> The series on the right is the ordinary expansion induced by the Taylor
> series of \(\Phi\). Suppose \(a_n\ge0\) for every \(n\ge2\). If that series
> represents \(F\) for every \(\Re s>1\) and the same branch extends
> holomorphically to \(s=1\), then \(\Phi\) is constant.

It is not required that the Taylor series of \(\Phi\) have positive
coefficients. The positivity required is only that of the already-assembled
Dirichlet coefficients.

> **Theorem B (singular quotients open no exception).** Let
> \(R=P/Q\in\mathbb C(X_0,\ldots,X_r)\), written in reduced form. If
> \(R(\ell_0(s),\ldots,\ell_r(s))\) has an **ordinary** Dirichlet series
> in some right half-plane, then
> \[
>  Q(0)\ne0.
>  \tag{3}
> \]
> Hence \(R\) is already a holomorphic germ at the origin and falls under
> Theorem A once its series reaches \(\Re s>1\), has non-negative
> coefficients, and cancels the pole at \(s=1\).

A necessary caveat is needed. "Holomorphic locally at \(s=1\)" without
requiring the positive series to reach \(1\) from the right is too weak. If
\(\sigma_c\) is the abscissa of convergence of (2), then:

> **Corollary C (real-anchor dichotomy).** If the branch of \(F\) admits
> holomorphic continuation to \(s=1\), \(a_n\ge0\), and \(\Phi\) is not
> constant, then necessarily
> \[
>  \boxed{\sigma_c>1.}
>  \tag{4}
> \]
> By Landau's theorem, \(s=\sigma_c\) is a real singularity of
> \(F\). It lies to the right of every nontrivial zero of \(\zeta\), and
> therefore it masks any singularity that the transform retains at those
> zeros.

This closes the natural analytic/rational extension of `104_95`: either
the positive transform reaches \(s=1\) and is constant, or it is
non-constant and manufactures a real anchor \(\sigma_c>1\) beforehand. No
Landau transformation appears that cancels the pole, preserves
non-negative coefficients, and forces the absence of zeros in
\(1/2<\Re s<1\).

The result does not cover nonlocal operators, argument shifts, or
transformations that are not functions of a finite jet
\((\ell_0,\ldots,\ell_r)\). It does not prove Deep-\(\Lambda\), A1, or RH.

---

## 1. The infinite Taylor series still has squarefree fibers

Write the convergent Taylor series

\[
 \Phi(X)=\sum_{k\ge0}\Phi_k(X),
 \tag{5}
\]

where \(\Phi_k\) is homogeneous of degree \(k\). Since each \(\ell_j\)
has vanishing constant term, the coefficient of a fixed integer receives
contributions from only finitely many degrees; (5) formally defines a
Dirichlet series. For \(\Re s\) sufficiently large, the definition is
moreover absolutely convergent, because the \(\ell_j(s)\) lie within the
polydisc of convergence of \(\Phi\).

Let \(n=p_1\cdots p_k\) be a product of \(k\) distinct primes. Exactly
as in `104_95`, no degree other than \(k\) can contribute: fewer than
\(k\) factors do not cover all the primes, and more than \(k\) factors
repeat one of them. Therefore

\[
 \boxed{
 a_{p_1\cdots p_k}
   =(\mathscr S_k\Phi_k)(\log p_1,\ldots,\log p_k),}
 \tag{6}
\]

where, on monomials,

\[
 \mathscr S_k(X_{j_1}\cdots X_{j_k})(x_1,\ldots,x_k)
 =\sum_{\pi\in S_k}\prod_{i=1}^kx_i^{j_{\pi(i)}+1}.
 \tag{7}
\]

The map \(\mathscr S_k\) is injective: its images are nonzero multiples
of the monomial symmetric polynomials associated with the partitions
\((j_1+1,\ldots,j_k+1)\).

## 2. Proof of Theorem A

Holomorphy of the same branch at \(s=1\), together with the
representation by (2) for \(\sigma>1\), gives

\[
 \lim_{\sigma\downarrow1}\{F(\sigma)-a_1\}<\infty.
 \tag{8}
\]

Since \(a_n\ge0\), monotone convergence implies

\[
 \sum_{n\ge2}{a_n\over n}<\infty.
 \tag{9}
\]

Suppose \(\Phi_k\ne0\) for some \(k\ge1\), and set
\(Q_k=\mathscr S_k\Phi_k\). By injectivity, \(Q_k\ne0\). The family
\(\{\log p:p\text{ prime}\}\) is infinite and therefore its Cartesian
product is Zariski-dense. One can fix distinct primes
\(q_1,\ldots,q_{k-1}\) so that

\[
 q(x)=Q_k(\log q_1,\ldots,\log q_{k-1},x)
 \tag{10}
\]

is a nonzero polynomial. For every prime \(p\) distinct from the fixed
ones,

\[
 q(\log p)=a_{q_1\cdots q_{k-1}p}\ge0.
 \tag{11}
\]

Although a priori \(q\) may have complex coefficients, (11) forces its
imaginary part to be the zero polynomial. Its real leading coefficient is
positive, or else \(q\) is a positive constant. There then exist
\(p_0\) and \(c_0>0\) such that \(q(\log p)\ge c_0\) for every prime
\(p\ge p_0\). With \(C=q_1\cdots q_{k-1}\),

\[
 \sum_{n\ge2}{a_n\over n}
 \ge {c_0\over C}
      \sum_{\substack{p\ge p_0\\p\nmid C}}{1\over p}
 =\infty,
 \tag{12}
\]

contradicting (9). Hence \(\Phi_k=0\) for every \(k\ge1\), and \(\Phi\)
is constant. \(\square\)

This proof shows why moving from a polynomial to an infinite power
series creates no degrees capable of canceling one another: the
squarefree support of \(k\) primes projects exactly onto degree \(k\).

## 3. Proof of Theorem B

Use the formal Dirichlet algebra

\[
 \mathscr D=\mathbb C[[x_p:p\text{ prime}]],
 \qquad x_p\longleftrightarrow p^{-s}.
 \tag{13}
\]

In it

\[
 \mathcal L_j(\mathbf x)
 =\sum_p(\log p)^{j+1}\sum_{\nu\ge1}\nu^j x_p^\nu
 \tag{14}
\]

represents \(\ell_j\). Uniqueness of Dirichlet series, applied to the
identity \(Q(\ell)F=P(\ell)\), gives the formal identity

\[
 Q(\mathcal L)\,\mathcal F=P(\mathcal L)
 \quad\hbox{in }\mathscr D.
 \tag{15}
\]

Choose \(r+1\) distinct primes \(p_0,\ldots,p_r\) and set all remaining
variables to zero. One obtains an identity in
\(\mathbb C[[x_{p_0},\ldots,x_{p_r}]]\). The Jacobian at the origin of
\(X_j=\mathcal L_j\) is

\[
 J_{j,i}=(\log p_i)^{j+1},
 \qquad
 \det J=\left(\prod_{i=0}^r\log p_i\right)
        \prod_{0\le i<k\le r}(\log p_k-\log p_i)\ne0.
 \tag{16}
\]

The formal inverse function theorem then turns (15) into

\[
 Q(X)G(X)=P(X),
 \qquad G\in\mathbb C[[X_0,\ldots,X_r]].
 \tag{17}
\]

That is, \(P/Q\) is regular as a formal germ at the origin. Faithful
flatness of
\(\mathbb C[[X]]\) over the local ring
\(\mathbb C[X]_{(X)}\) gives

\[
 Q\mathbb C[[X]]\cap\mathbb C[X]_{(X)}
 =Q\mathbb C[X]_{(X)}.
 \tag{18}
\]

By (17), \(Q\) divides \(P\) in the local ring. Since \(P,Q\) were
taken coprime, \(Q\) must be a local unit, which is equivalent to
\(Q(0)\ne0\). This proves the theorem. \(\square\)

For example, the seemingly innocent quotient \(\ell_1/\ell_0\) is not
an ordinary Dirichlet series. On the real axis, if
\(a=\log2\), \(b=\log3\),

\[
 {\ell_1(s)\over\ell_0(s)}
 =a+{b(b-a)\over a}\left({2\over3}\right)^s
   +o\!\left((2/3)^s\right).
 \tag{19}
\]

The frequency \(\log(3/2)\) is not \(\log n\) for any integer
\(n\). It is the one-dimensional manifestation of the formal obstruction
of (16)–(18).

## 4. The abscissa caveat and an exact counterexample

Let \(\sigma_c\) be the abscissa of convergence of the positive series (2).
If \(\sigma_c\le1\) and the branch extends holomorphically to \(1\),
then

\[
 \sum_{n\ge2}{a_n\over n}<\infty.
 \tag{20}
\]

Indeed, if the sum diverges, \(F(\sigma)\uparrow\infty\) as \(\sigma\)
decreases to \(1\), incompatible with holomorphy; if it converges, (20)
is literal. Theorem A again gives that \(\Phi\) is constant. This
proves (4). For a non-constant, non-negative Dirichlet series, Landau
further states that its finite abscissa \(\sigma_c\) is a real
singularity.

The need to control the abscissa can be seen without any zero at all. For
\(c>0\), define

\[
 F_c(s)={1\over c-\ell_0(s)}.
 \tag{21}
\]

In the half-plane where \(\ell_0(\sigma)<c\),

\[
 F_c(s)=\sum_{k\ge0}{\ell_0(s)^k\over c^{k+1}},
 \tag{22}
\]

and all its Dirichlet coefficients are non-negative. However,
\(\ell_0(\sigma)\) strictly decreases from \(+\infty\) to \(0\) as
\(\sigma\) goes from \(1^+\) to \(+\infty\). There is a unique
\(\sigma_c>1\) with \(\ell_0(\sigma_c)=c\), and (21) has a real
pole there. At the same time,

\[
 \ell_0(s)={1\over s-1}-\gamma+O(s-1)
 \quad\Longrightarrow\quad
 F_c(s)=-(s-1)+O((s-1)^2),
 \tag{23}
\]

so that \(F_c\) is holomorphic — and vanishes — at \(s=1\).

The example shows that the mere phrase "positive coefficients and local
holomorphy at \(1\)" is not enough. The exact price is the real pole
\(\sigma_c>1\). Moreover, near a zero \(\rho\) of multiplicity
\(m\), \(\ell_0(s)=-m/(s-\rho)+O(1)\), and hence
\(F_c(s)=(s-\rho)/m+O((s-\rho)^2)\): this example erases, rather than
retains, the singularity of the zero.

## 5. Decision

```text
proved:
  rigidity for every analytic germ of a finite jet of ell;
  exact isolation of each Taylor degree by squarefree fibers;
  every rational transformation with an ordinary Dirichlet series is
  automatically regular at the origin;
  dichotomy: constant if the positive series reaches 1, or an artificial
  real anchor sigma_c>1 if the transform is non-constant;
  exact counterexample showing why merely local holomorphy is not enough.

not proved:
  a global, nonlocal inequality for the real Lambda weights;
  the subpolynomial energy of 104_93--104_94;
  Deep-Lambda, A1, or RH.
```

## Mechanical verification

`tools/analytic_rational_landau_rigidity_check.py` verifies with rational
arithmetic the Vandermonde determinants of the coordinate change, the
positive recurrence of the geometric expansion (22), and the formal
identity \((c-L)F=1\) on finite truncations. Existence and uniqueness of
the real pole are proved analytically via the strict monotonicity of
\(\ell_0(\sigma)\); they are not delegated to the program. The program uses
neither zeros of \(\zeta\) nor floating point.
</content>
