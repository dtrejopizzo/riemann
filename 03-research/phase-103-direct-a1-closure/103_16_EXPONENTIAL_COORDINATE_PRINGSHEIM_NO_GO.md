# Exponential coordinate and the Pringsheim obstruction

## Purpose

This note tests a new sufficient condition for Li positivity.  The condition
has an appealing positive-composition form, but is false unconditionally
for \(\xi\).  The obstruction is structural: a power series with
nonnegative coefficients cannot have its nearest logarithmic singularities
only off the positive real axis.

## 1. Exact exponential-coordinate identity

Put
\[
 h(z)=\log\xi\!\left({1\over1-z}\right),\qquad
 x=-\log(1-z),\qquad G(x)=\log\xi(e^x),
\]
so that \(h(z)=G(x(z))\).  Write
\[
 g_k=G^{(k)}(0)=\left.\left(s{d\over ds}\right)^k\log\xi(s)
 \right|_{s=1}.                                                       \tag{1}
\]
The unsigned Stirling numbers of the first kind are defined by
\[
 {(-\log(1-z))^k\over k!}
 =\sum_{n\ge k}\left[{n\atop k}\right]{z^n\over n!}.
\]
Consequently
\[
 \boxed{\quad
 \lambda_n=n[z^n]h(z)
 ={1\over(n-1)!}\sum_{k=1}^n\left[{n\atop k}\right]g_k.\quad}       \tag{2}
\]
Thus the condition
\[
 g_k\ge0\qquad(k\ge1)                                                \tag{3}
\]
would imply every Li inequality, with no zero-side hypothesis.

The theta measure of `103_15` makes the first two signs transparent.  If
\(\kappa_j\) are the cumulants of its tilt at \(a=1\), then
\[
 g_k=\sum_{j=1}^k\left\{{k\atop j}\right\}\kappa_j,
\]
where the braces are Stirling numbers of the second kind.  Hence
\[
 g_1=\kappa_1>0,\qquad g_2=\kappa_1+\kappa_2>0,
 \qquad g_3=\kappa_1+3\kappa_2+\kappa_3.                            \tag{4}
\]
The third cumulant has no fixed sign from positivity of the measure, so
already (4) contains no inductive positive mechanism.

## 2. Elementary Pringsheim lemma

> **Lemma.**  Let \(A(w)=\sum_{n\ge0}a_nw^n\), with \(a_n\ge0\), have a
> finite radius of convergence \(R\).  Then \(w=R\) is a singularity of
> \(A\).

*Proof.*  Suppose instead that \(A\) is analytic in \(|w-R|<\delta\).
For a smaller \(\delta\), Cauchy's estimate gives
\[
 |A^{(k)}(R)|\le Ck!\delta^{-k}.                                    \tag{5}
\]
On the real interval \((0,R)\), positivity permits monotone convergence
of every differentiated series as \(r\uparrow R\).  Thus
\[
 \sum_{m\ge k}a_m{m!\over(m-k)!}R^{m-k}=A^{(k)}(R),
\]
and in particular, for \(k\le n\),
\[
 a_n\le Ck!\delta^{-k}R^{k-n}{(n-k)!\over n!}.                      \tag{6}
\]
Take \(k=\lfloor\theta n\rfloor\), \(0<\theta<1\).  Stirling's
formula in (6) gives
\[
 \limsup_{n\to\infty}a_n^{1/n}
 \le R^{\theta-1}\delta^{-\theta}
       \theta^\theta(1-\theta)^{1-\theta}.                         \tag{7}
\]
For sufficiently small positive \(\theta\), the right side is strictly
less than \(1/R\), because its ratio to \(1/R\) has logarithm
\[
 \theta\log(R/\delta)+\theta\log\theta
 +(1-\theta)\log(1-\theta)<0.
\]
This contradicts the definition of the radius \(R\). \(\square\)

## 3. Application: the sufficient condition is false

The local logarithm \(G\) has finite Taylor radius.  Indeed, \(\xi\) has
nontrivial zeros, and every such zero \(\rho\) produces a logarithmic
singularity of \(G\) at one of the finite points
\[
 x=\Log\rho+2\pi i k.                                                \tag{8}
\]
Let \(R\) be its Taylor radius at zero.  If (3) held, the Lemma applied to
the coefficients \(g_k/k!\) would force a singularity at the positive real
point \(x=R\).  But for every real \(x>0\),
\[
 e^x>1,\qquad \xi(e^x)>0,
\]
because all factors in the defining completed Euler product are positive
there.  Hence a real analytic branch of \(\log\xi(e^x)\) exists in a
neighborhood of every positive \(x\), including \(R\).  This is a
contradiction.

Therefore
\[
 \boxed{\ \text{some }g_k<0.\ }                                    \tag{9}
\]
The tempting shortcut (3) is not merely unproved; it is false.

## 4. Strength audit

Condition (3) is strictly stronger than critical-line reality as a general
principle.  The model
\[
 X(s)=\cosh(s-1/2)
\]
has the functional symmetry \(X(s)=X(1-s)\) and all its zeros on the
critical line, yet the same argument applies to
\(\log X(e^x)\): it has finite non-real logarithmic singularities while
\(X(e^x)>0\) for \(x>0\).  Its exponential-coordinate coefficients cannot
all be nonnegative.

Thus (3) is a valid but overstrong RH-proving condition, not a condition
equivalent to RH.  The failure identifies the relevant structural issue:
the Li-positive combination in (2) must retain cancellations among the
signed \(g_k\).  Any route that tries to prove positivity coefficient by
coefficient after an analytic reparametrisation is ruled out by the
off-axis singularity geometry itself.
