# 104_29 — Compensated split at \(\log2\) and the signed-transport gate

**Role.** Execute the proposal of splitting the Laplace variable at the
first arithmetic atom. The split is natural and produces an exact
identity. However, a mass comparison without the Laguerre test function is
invalid and informationally empty; the compensated version that keeps the
test exactly recomposes the margin \(D_n^{[r]}=r\lambda_n-A_n\).

This document proves neither A1 nor RH. It localizes MW-2 in the gap
\((0,\log2)\), quantifies its action on the real vector, and shows what
global signed inequality would still be needed.

## 1. Completed generator before removing the regulator

Fix

\[
 r>1,\qquad s_0=1+\varepsilon,\qquad u=c\varepsilon,
 \qquad 0<c<1.
\]

The first variation of the real cocycle of 104_23–104_24 has the
completed Lévy measure

\[
 \boxed{
 \kappa_{r,\varepsilon}(dx)
 =r e^{-(1+\varepsilon)x}\,d\psi(e^x)
  -r e^{-\varepsilon x}\,dx
  +(r-1){e^{-(3+\varepsilon)x}\over1-e^{-2x}}\,dx.}             \tag{1}
\]

The Gamma part of (1) is \((r-1)/(2x)+O_r(1)\) as \(x\downarrow0\). Hence
(1) has no finite total mass near zero. The correct action on a test
function \(\varphi\) is compensated:

\[
 \mathcal G_{r,\varepsilon}\varphi
 :=\int_0^\infty\bigl(\varphi(x)-\varphi(0)\bigr)
       \kappa_{r,\varepsilon}(dx).                              \tag{2}
\]

For a polynomial, the difference in (2) is \(O(x)\), and

\[
 \int_0^\infty x(1+x^k)|\kappa_{r,\varepsilon}|(dx)<\infty
\]

for every \(k\) and every \(\varepsilon>0\). Thus (2), not an informal
difference of infinite masses, is the legitimate object.

## 2. Exact Laguerre identity and split at the first prime

Set

\[
 \varphi_n(x)=L_{n-1}^{(1)}(x)-n,\qquad \varphi_n(0)=0.          \tag{3}
\]

The normalized linearization of the cocycle gives

\[
 \boxed{
 -D_n^{[r]}
 =-nD_1^{[r]}
  +\lim_{\varepsilon\downarrow0}
       \int_0^\infty\varphi_n(x)\kappa_{r,\varepsilon}(dx),}
 \qquad D_n^{[r]}=r\lambda_n-A_n.                              \tag{4}
\]

Let \(a=\log2\). There are no atoms of \(d\psi(e^x)\) in \(0<x<a\), and
the atom \(m=2\) is assigned to the exterior block. Hence (4) splits
exactly as

\[
 -D_n^{[r]}=-nD_1^{[r]}
 +\lim_{\varepsilon\downarrow0}
 \bigl(J_n^{<}(\varepsilon)+J_n^{\ge}(\varepsilon)\bigr),       \tag{5}
\]

where

\[
 \boxed{
 J_n^{<}(\varepsilon)
 =\int_0^a\varphi_n(x)e^{-\varepsilon x}
 \left[-r+(r-1){e^{-3x}\over1-e^{-2x}}\right]dx}                \tag{6}
\]

and

\[
 \boxed{
 \begin{aligned}
 J_n^{\ge}(\varepsilon)
 ={}&r\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
       \varphi_n(\log m)\\
 &+\int_a^\infty\varphi_n(x)e^{-\varepsilon x}
 \left[-r+(r-1){e^{-3x}\over1-e^{-2x}}\right]dx .
 \end{aligned}}                                                 \tag{7}
\]

Equations (5)–(7) preserve the pole, Gamma, every prime, and the Laguerre
test function. The theorem that would close the margin would be

\[
 \boxed{
 \limsup_{\varepsilon\downarrow0}J_n^{\ge}(\varepsilon)
 \le nD_1^{[r]}-\lim_{\varepsilon\downarrow0}J_n^{<}(\varepsilon)
 \qquad(n\ge150).}                                              \tag{8}
\]

But, by (5), (8) is exactly \(D_n^{[r]}\ge0\). The split organizes the
cancellation; it does not prove it.

## 3. The localized obstruction and its scale on the real test

In the arithmetic gap, the density

\[
 b_r(x)=-r+(r-1){e^{-3x}\over1-e^{-2x}}                       \tag{9}
\]

appears. The second term of (9) strictly decreases from \(+\infty\) to
zero. There is therefore a unique \(x_r>0\) with \(b_r(x_r)=0\). At
\(x_0=\frac12\log2\),

\[
 b_r(x_0)=-r+{r-1\over\sqrt2}<-1<0.                            \tag{10}
\]

This recovers the witness of 104_23 and proves that no argument based on
positivity of the completed measure can work.

Its action on the specific test function has a different reading. On the
fixed interval \([x_r,a]\), the Laguerre asymptotic at fixed argument
gives, uniformly away from zero,

\[
 L_{n-1}^{(1)}(x)=O_r(n^{1/4}),
 \qquad
 \varphi_n(x)=-n+O_r(n^{1/4}).                                 \tag{11}
\]

Consequently, for

\[
 M_r:=\int_{x_r}^{a}(-b_r(x))\,dx>0,
\]

one has

\[
 \int_{x_r}^{a}\varphi_n(x)b_r(x)\,dx
 =nM_r+O_r(n^{1/4}).                                           \tag{12}
\]

The local non-positivity witness only contributes scale \(O_r(n)\),
against \(A_n\asymp n\log n\). It is robust as a positive-measure
stop-gate, but it is not by itself the proportional obstruction. The
difficulty remains in the exterior block (7), where the pole and the
primes cancel to all orders.

## 4. Why the mass balance gives a false diagnosis

The positive prime mass of the generator for \(\varepsilon>0\) equals

\[
 r\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 =-r{\zeta'\over\zeta}(1+\varepsilon)
 \sim {r\over\varepsilon}.                                    \tag{13}
\]

The negative mass of any compact set inside \((0,\log2)\) is
\(O_r(1)\). So the arithmetic part "dominates in mass" automatically,
without this implying any sign for (7). On the path
\(u=c\varepsilon\), the same false victory occurs after normalizing: the
arithmetic Lévy mass tends to \(-r\log(1-c)>0\), while the negative mass on
a compact set of the gap is \(O(\varepsilon)\).

Restoring the Laguerre test function, separating primes and pole is
likewise impossible. Since \(\varphi_n\) has degree \(n-1\),

\[
 \int_0^\infty x^{n-1}e^{-\varepsilon x}\,dx
 ={(n-1)!\over\varepsilon^n}.                                  \tag{14}
\]

The leading moments of the pole and of the prime sum are therefore of
order \(\varepsilon^{-n}\) and cancel in the completed combination. Taking
absolute values, masses, or positive parts before that cancellation
exactly reproduces the loss of 103_53–103_57.

## 5. Falsifier and logical boundary

Every inference using only:

* positivity of the Euler coefficients;
* the support gap \((0,\log2)\);
* positive Gamma and the functional symmetry;

must be submitted to the off-line quartet

\[
 w={1\over2}e^{74\pi i/75},\qquad \rho=(1-w)^{-1}.              \tag{15}
\]

For \(n=150\), its contribution to the exponent-\(r\) margin contains

\[
 4r\bigl(1-\cosh(150\log2)\bigr)<0,                            \tag{16}
\]

and can be amplified by multiplicity. A proof of (8) must use a special
quantitative property of the real weights
\(\Lambda(p^k)=\log p\) and must fail for (15).

## 6. Relation to the earlier gates

* 104_23 already proves the local witness (10).
* The first variation (1) is the Stein–Mecke kernel of 104_24.
* Block (7), with the prime towers not separated, is the surviving global
  multiplicative gate of 104_20.
* Separating its prime part from the polar part repeats the endpoint
  obstruction of 103_53–103_57.

Hence \(\log2\) is the correct geometric cut, but it creates no
coercivity. The live successor remains a nonlocal signed inequality for
(7), or equivalently a direct bound on the hard-edge ray of 104_28.

## Status

* **Proved:** the compensated generator, the exact split (5)–(7), the
  uniqueness of crossing point (9), the local scale (12), and the separate
  divergence (14).
* **Ruled out:** comparing positive and negative masses without the
  Laguerre test function.
* **Not reduced:** the useful inequality (8) is exactly
  \(D_n^{[r]}\ge0\).
* **Live front:** a signed bound for the renormalized prime–pole form on
  \(g_n\), using real multiplicative interaction between towers.
</content>
