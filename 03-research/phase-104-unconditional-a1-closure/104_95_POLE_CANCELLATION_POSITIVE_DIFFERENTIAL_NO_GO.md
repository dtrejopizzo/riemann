# 104_95 — Pole cancellation and rigidity of positive differential polynomials

## Result

Let

\[
 \ell(s)=-{\zeta'(s)\over\zeta(s)},\qquad
 \delta=-{d\over ds},\qquad
 \ell_j=\delta^j\ell
 =\sum_{m\ge2}{\Lambda(m)(\log m)^j\over m^s}
 \quad(\Re s>1).
 \tag{1}
\]

The attempt examined consists in building a differential polynomial

\[
 F(s)=P(\ell_0(s),\ldots,\ell_r(s))
     =a_1+\sum_{m\ge2}{a_m\over m^s},
 \qquad P\in\mathbb R[X_0,\ldots,X_r],
 \tag{2}
\]

that cancels the real pole of \(\ell\), preserves \(a_m\ge0\) and keeps
poles at the zeros of \(\zeta\). Landau would then convert a right-hand
zero into a real singularity. This natural class is ruled out by a
stronger rigidity, prior to any information about the zeros.

> **Theorem 1 (squarefree rigidity).** Suppose that the Dirichlet
> coefficients of (2) satisfy
> \(a_m\ge0\) for all \(m\ge2\). If \(F\) is holomorphic at \(s=1\), then
> \(P\) is constant. In particular, no non-constant differential
> polynomial with constant coefficients can simultaneously
>
> 1. cancel the pole at \(s=1\);
> 2. preserve non-negative Dirichlet coefficients;
> 3. retain a singularity at a zero of \(\zeta\).

This includes all polynomials in
\(\ell,-\ell',\ell'',\ldots\), because these are precisely the
polynomials in the \(\ell_j\) after fixed sign changes.

The theorem does not prove RH. It proves that the desired Landau closure
does not exist in this algebraic class. It does not cover non-polynomial
transformations, shifts of the argument, or operators that do not
have fixed Dirichlet coefficients.

---

## 1. The conflict is already complete at quadratic order

Put \(t=s-1\). The expansion

\[
 \ell(s)={1\over t}-\gamma+O(t)
 \tag{3}
\]

gives

\[
 \ell'=-{1\over t^2}+O(1),\qquad
 \ell^2={1\over t^2}-{2\gamma\over t}+O(1).
 \tag{4}
\]

Hence

\[
 -\ell'+\ell^2={\zeta''\over\zeta}
 =\sum_{m\ge1}{\Lambda(m)\log m+(\Lambda*\Lambda)(m)\over m^s}
 \tag{5}
\]

has non-negative coefficients, but retains the double pole
\(2t^{-2}\). The opposite sign

\[
 \ell'+\ell^2
 \tag{6}
\]

cancels the double pole, but leaves \(-2\gamma t^{-1}\), and its
coefficient at a prime \(p\) is \(-\log^2p<0\).

More generally, consider

\[
 F=A\ell'+B\ell^2+C\ell+D.
 \tag{7}
\]

The holomorphy conditions at \(s=1\) are, successively,

\[
 -A+B=0,\qquad -2\gamma B+C=0.
 \tag{8}
\]

So, except for the constant \(D\), the only candidate is

\[
 \boxed{F=A\{\ell'+\ell^2+2\gamma\ell\}+D.}
 \tag{9}
\]

Its coefficient at a prime is

\[
 a_p=A\log p\,(2\gamma-\log p).
 \tag{10}
\]

The elementary inequalities \(\frac12<\gamma<1\), \(\log2<1\) and
\(\log11>2\) show that the bracket is positive for \(p=2\) and
negative for \(p=11\). If \(A>0\), (10) is negative at \(11\); if
\(A<0\), it is negative at \(2\); and if \(A=0\), only a
constant remains.

Candidate (9) would indeed have preserved the zeros: if \(\rho\) has
multiplicity \(m\), then

\[
 \ell(s)=-{m\over s-\rho}+O(1),
 \qquad
 F(s)={A\,m(m+1)\over(s-\rho)^2}
       +O\!\left({1\over s-\rho}\right).
 \tag{11}
\]

So the failure is not that the cancellation erases the zeros: it is
exactly the loss of positivity in the prime coefficients.

---

## 2. Squarefree fiber of a homogeneous degree

Write

\[
 P=P_0+P_1+\cdots+P_d,
 \tag{12}
\]

where \(P_k\) is homogeneous of degree \(k\). For a degree-\(k\) monomial
the Dirichlet coefficient is a convolution of \(k\) copies of weights
supported on prime powers.

If \(n=p_1\cdots p_k\) is a product of \(k\) distinct primes, only
\(P_k\) can contribute to \(a_n\): fewer than \(k\) factors do not cover
the \(k\) primes and more than \(k\) factors would repeat one of them.

Define the symmetrization map

\[
 \mathscr S_k(X_{j_1}\cdots X_{j_k})(x_1,\ldots,x_k)
 :=\sum_{\pi\in S_k}\prod_{i=1}^k x_i^{j_{\pi(i)}+1}.
 \tag{13}
\]

Then, exactly,

\[
 \boxed{
 a_{p_1\cdots p_k}
 =(\mathscr S_kP_k)(\log p_1,\ldots,\log p_k).}
 \tag{14}
\]

The map \(\mathscr S_k\) is injective. Indeed, if the multiset
\(\{j_1,\ldots,j_k\}\) has multiplicities \(\alpha_j\), (13) is
\(\prod_j\alpha_j!\) times the monomial symmetric polynomial associated
to the partition \((j_1+1,\ldots,j_k+1)\). Distinct partitions give a
linearly independent basis.

---

## 3. Proof of Theorem 1

Series (2) converges absolutely for \(\Re s>1\). If \(F\) is
holomorphic at \(1\), then

\[
 \lim_{\sigma\downarrow1}\{F(\sigma)-a_1\}<\infty.
 \tag{15}
\]

Since \(a_m\ge0\), monotone convergence applied to the Dirichlet series
implies

\[
 \sum_{m\ge2}{a_m\over m}<\infty.
 \tag{16}
\]

Now suppose some \(P_k\ne0\), \(k\ge1\), and put
\(Q=\mathscr S_kP_k\). By the injectivity above, \(Q\ne0\). The
Cartesian product of any infinite set is Zariski-dense; in
particular one can fix distinct primes
\(q_1,\ldots,q_{k-1}\) such that

\[
 q(x):=Q(\log q_1,\ldots,\log q_{k-1},x)
 \tag{17}
\]

is a non-zero polynomial. For every prime \(p\) distinct from the
previous ones, (14) and the sign hypothesis give

\[
 q(\log p)=a_{q_1\cdots q_{k-1}p}\ge0.
 \tag{18}
\]

A non-zero real polynomial that is non-negative on an unbounded sequence
has positive leading coefficient (or is a positive constant). Therefore
there exist \(p_0\) and \(c_0>0\) such that
\(q(\log p)\ge c_0\) for every prime \(p\ge p_0\). If
\(C=q_1\cdots q_{k-1}\), it follows that

\[
 \sum_m{a_m\over m}
 \ge {c_0\over C}\sum_{\substack{p\ge p_0\\p\nmid C}}{1\over p}
 =\infty,
 \tag{19}
\]

by the divergence of the sum of reciprocals of primes. This
contradicts (16). Hence \(P_k=0\) for all \(k\ge1\), and \(P=P_0\) is
constant. \(\square\)

Note that (15)--(19) contain Landau's mechanism in its most
elementary form: a non-negative Dirichlet series cannot hide at
\(s=1\) the divergent mass of a fiber of primes. There was no need to
assume or deny RH.

---

## 4. Relation to the previous gates

- `104_13` dealt with the particular identity
  \(-\ell'+\ell^2=\zeta''/\zeta\), its Laguerre recurrence and its scale
  barrier. Theorem 1 is the genuine extension: it classifies **every**
  constant-coefficient differential polynomial before projecting it to
  Laguerre.
- `103_16` ruled out coefficient-by-coefficient positivity after the
  exponential coordinate of \(\log\xi\) via Pringsheim. Here the
  variable remains \(s\), the coefficients are the arithmetic Dirichlet
  coefficients, and the rigidity comes from the squarefree fibers.

## 5. Decision

```text
proved:
  the only quadratic combination that cancels the whole pole at s=1;
  its sign change already between the coefficients p=2 and p=11;
  rigidity for every P(ell,delta ell,...,delta^r ell) with constant coefficients;
  impossibility of simultaneously preserving a cancelled pole,
  non-negative coefficients, and poles at zeros within that class.

not covered:
  non-polynomial functions of ell_j;
  shifts or dilations of the argument;
  non-local operators over all prime towers.

not proved:
  Deep-Lambda, A1, or RH.
```

## Mechanical verification

`tools/pole_cancellation_squarefree_rigidity_check.py` checks with
integer arithmetic the quadratic-order pole equations and the diagonal
injectivity of (13) for arbitrary finite degrees and orders. The script
uses no zero values nor floating point.
