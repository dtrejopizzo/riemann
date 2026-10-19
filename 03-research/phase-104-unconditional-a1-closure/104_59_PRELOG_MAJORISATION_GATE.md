# 104_59 — Pre-log majorization and Schur-convexity gate

**Role.** Audit the last classical family proposed for the law
\(X=\log N\) before extracting the Laguerre coefficient: majorization of
mass vectors, convex order of laws, and Schur-convexity of the test.

**Verdict.** The probabilistic layer was already built in 104_21 and
104_43. Classical majorization does not read the A1 observable:

1. majorization of the **masses** forgets which mass is attached to each
   \(\log m\), while the Laguerre moment depends on that attachment;
2. majorization of the **support points** only orders convex or
   concave functions, but
   \(\varphi_n=L_{n-1}^{(1)}-n\) has curvature of both signs for every
   \(n\ge4\);
3. in the real arithmetic disintegration, the divisor selector lies
   above the uniform selector at \(N=2\) and below it at \(N=30\), already
   for the linear test.

Hence the classical family contributes no inequality for A1. What is not
ruled out is a **signed, position-dependent, \(\Lambda\)-specific** global
comparison; but by keeping that data its transform is exactly the
functional \(R\) of 104_43, and its Laguerre projection returns to the
open margin. This document proves neither A1 nor RH.

## 1. What "majorizing a law" means

There are two canonical readings, and they should not be mixed.

### 1.1 Majorization of the probability vector

For an atomic law

\[
 \mu=\sum_jp_j\delta_{x_j},                                      \tag{1}
\]

one can majorize the unlabeled vector \(p=(p_j)\). Every Schur-convex
function of \(p\) is symmetric: a permutation of the masses leaves its
value invariant.

The observable that appears before the regulated limit is, instead,

\[
 \mathcal L_n(\mu)=\sum_jp_j\varphi_n(x_j),
 \qquad \varphi_n(x)=L_{n-1}^{(1)}(x)-n.                       \tag{2}
\]

The association \(p_j\leftrightarrow x_j\) is an essential part of (2). So
(2) is not a Schur function of the mass vector.

The minimal counterexample is exact. On the supports
\((0,\ell)\), \(\ell=\log2>0\), take

\[
 p=(3/4,1/4),\qquad q=(1/4,3/4).                               \tag{3}
\]

The vectors are permutations, so \(p\succ q\) and \(q\succ p\). For
\(n=2\),

\[
 \varphi_2(x)=L_1^{(1)}(x)-2=-x,
\]

and yet

\[
 \mathcal L_2(p)=-{\ell\over4},\qquad
 \mathcal L_2(q)=-{3\ell\over4}.                              \tag{4}
\]

So mass majorization alone has already discarded precisely the
information that needs to be projected.

### 1.2 Majorization of points, or convex order of measures

The second reading keeps the positions. For two vectors with the
same sum, \(x\succ y\), Karamata gives

\[
 \sum_j\phi(x_j)\ge\sum_j\phi(y_j)                              \tag{5}
\]

when \(\phi\) is convex; it reverses (5) when \(\phi\) is concave. In the
language of laws, \(\mu\succeq_{\rm cx}\nu\) controls exactly the convex
tests. The weak-majorization variants add monotonicity to the requirement.

For the actual test,

\[
 \varphi_n''(x)=L_{n-3}^{(3)}(x)\qquad(n\ge3).                  \tag{6}
\]

If \(n\ge4\), the Laguerre polynomial on the right has \(n-3\) simple
positive zeros. Its sign alternates between them. Consequently, for
**every** \(n\ge4\), and hence for every \(n\ge150\), \(\varphi_n\) is
neither globally convex nor globally concave. Moreover
\(\varphi_n'=-L_{n-2}^{(2)}\) changes sign, so it also fails to belong
to the increasing-convex or decreasing-convex classes of the weak orders.

This is not an asymptotic objection. The first case, \(n=4\), already gives
two closed-form witnesses:

\[
 \varphi_4(x)=-6x+2x^2-{x^3\over6},\qquad
 \varphi_4''(x)=4-x.                                          \tag{7}
\]

For any \(a\ge h\ge0\), the vector
\((a-h,a+h)\) majorizes \((a,a)\), and the Karamata defect is

\[
 \boxed{
 \varphi_4(a-h)+\varphi_4(a+h)-2\varphi_4(a)
 =h^2(4-a).}                                                   \tag{8}
\]

With \((a,h)=(1,1)\), (8) equals \(3>0\); with \((a,h)=(5,1)\), it equals
\(-1<0\). The same majorization relation demands opposite orientations.

The sign change also occurs on logarithms of integers. If
\(\ell=\log2\), then

\[
 (\log1,\log4)\succ(\log2,\log2)
\]

and (8) equals

\[
 \ell^2(4-\ell)>0.                                             \tag{9}
\]

On the other hand,

\[
 (\log64,\log256)\succ(\log128,\log128)
\]

and the same defect equals

\[
 \ell^2(4-7\ell)<0.                                           \tag{10}
\]

The signs of (9)--(10) use no decimals: \(2<e\) gives
\(\ell<1\), while \(e<3\) and \(3^4=81<128=2^7\) give
\(4<7\ell\).

Hence there is no universal Schur orientation for the family of tests
that contains A1. Splitting the axis into intervals of constant curvature
does not resolve the problem: it introduces boundary terms with
alternating signs and turns into the signed lobe comparison of 103_64.

## 2. The pre-log law was already available

The proposal does not duplicate the **matrix** Schur complement of 104_34;
that document uses a Schur complement on two adjacent rays. Nor does it
duplicate the analytic pre-log Schur function of 103_24 §6. It does
coincide with two earlier probabilistic constructions:

1. 104_21 §1--§2 normalizes the Euler product and proves that
   \(X=\log N\) is compound-Poisson. For \(u_2>u_1\) it builds the
   exact coupling

   \[
    X(u_2)=X(u_1)+Z_{u_1,u_2},\qquad Z_{u_1,u_2}\ge0.          \tag{11}
   \]

   This already gives stochastic order and its convex refinements. The
   document itself records that the oscillatory Laguerre functions do not
   belong to those classes.

2. 104_43 and 104_44 work before separating out the integer's product. The
   identity \(\Lambda*1=\log\) gives

   \[
    N^\star=DN',\qquad
    \mathbb P(D=d\mid N^\star=N)
      ={\Lambda(d)\over\log N}{\bf1}_{d\mid N}.                \tag{12}
   \]

   The polar comparator selects a point of
   \([0,\log N]\) uniformly. This is precisely the natural slot where an
   arithmetic pre-log majorization should be attempted.

Moreover, 103_64 §6 already audits the convex order after the
decomposition into cells: the cost is separable, its Monge difference is
zero, and the arithmetic primitive changes sign, with real certificates
\(G(2976)>10\) and \(G(4000)<-3700\). 104_14 imports that stop-gate into the
Phase 104 map.

## 3. The real arithmetic comparator has no orientation

The lack of convexity of the test already prevents using Karamata. There
is a further, earlier obstruction: not even the real divisor selector has
a uniform orientation relative to the continuous selector.

Conditioned on \(N\), let

\[
 Y=\log D,\qquad U_N\sim{\rm Unif}[0,\log N].                   \tag{13}
\]

For the linear test \(f(y)=y\), 104_43 obtains

\[
 2L\{\mathbb E(Y\mid N)-\mathbb E U_N\}
 =\sum_p a_p(a_p+1)(\log p)^2-L^2,
 \quad N=\prod_pp^{a_p},\quad L=\log N.                       \tag{14}
\]

At \(N=2\), (14) is \((\log2)^2>0\). At \(N=30\), setting
\(a=\log2,b=\log3,c=\log5\), it is

\[
 a^2+b^2+c^2-2ab-2ac-2bc
 =(a+b-c)^2-4ab<0.                                             \tag{15}
\]

The last inequality is exact: \(0<a+b-c=\log(6/5)<a\), hence
\((a+b-c)^2<a^2<4ab\). Thus both uniform orientations already fail
for a function that is simultaneously increasing, convex and concave.

This witness uses the real weights
\(\Lambda(2),\Lambda(3),\Lambda(5)\); it does not replace arithmetic with
an abstract law.

## 4. The minimal candidate and its no-go

The strongest classical use that can be made without adding new structure
is:

> **Candidate PM.** Build a majorization order between the arithmetic
> pre-log law and a reference law, and apply Karamata or
> Schur-convexity to order their moments \(\mathcal L_n\).

Candidate PM fails in two independent ways:

* if the mass vector is majorized, (3)--(4) prove the observable does not
  descend to the quotient by permutations;
* if the random variable is majorized, (6)--(10) prove the observable does
  not lie in the order's dual cone, for any index in the target range.

The version conditioned on the real factorizations fails further by
(14)--(15). Hence there is no useful theorem from the classical family
deriving A1 after establishing a single majorization relation.

## 5. What is not ruled out

These witnesses do not exclude an identity that simultaneously:

1. keeps the label \(m\mapsto\log m\);
2. distinguishes every curvature interval of \(\varphi_n\);
3. compensates the signs across different factorizations \(N=dk\);
4. keeps the pole, Gamma and all the weights \(\Lambda(p^j)\) bound together.

But that is no longer Schur-convexity nor Karamata. Averaging the
comparison (12) globally, 104_43 §5 shows that its Laplace transform is
exactly

\[
 R(t)=-{\zeta'\over\zeta}(1+t)-{1\over t},                    \tag{16}
\]

and that the Laguerre projection produces
\(\Delta A_n-\Delta\lambda_n\). So a special signed inequality for
(16) remains a legitimate front, but it is not a consequence of
majorization: it is the open arithmetic content.

The off-line falsifier remains binding for any successor. The positive
properties of the Euler law and the earlier majorization relations do not
by themselves see the quadruple
\(4-4\cosh(n\alpha)\cos(n\theta)\); an inference that also accepted it
could not close A1.

## 6. Exact verification

Run

    cd 03-research/phase-104-unconditional-a1-closure
    python3 tools/prelog_majorisation_gate_check.py

The verifier uses Fraction for:

* the defects \(+3\) and \(-1\) of (8);
* the formal factorizations (9)--(10);
* the permutation obstruction (4);
* outward intervals via the artanh series to certify the real
  signs of (14)--(15).

It evaluates neither \(\zeta\), nor Li coefficients, nor A1, nor RH.

## Status

* **Duplication located:** the pre-log law and its couplings are already
  in 104_21, 104_43 and 104_44.
* **Ruled out:** classical majorization followed by Schur-convexity,
  Karamata, stochastic or convex order of the Laguerre test.
* **Not ruled out:** a labeled, \(\Lambda\)-specific signed global
  comparison; by (16), it remains the same A1-strength arithmetic gate.
* **Closure:** neither A1 nor RH is proved.
