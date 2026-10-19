# 104_23 — Near-quartic real margin and the hypergeometric pole

> **Binding correction (`104_56A`).** The identities and Theorem 1.1
> of this document remain correct for the uniform transfer obtained from the
> single raw datum \(T_n\ge1000\). What is withdrawn is its interpretation as
> an intrinsic front. A0 holds for every larger cutoff: if \(4\lambda_n>A_n\),
> a sufficiently large adapted cutoff closes A1.
> Moreover \(4\lambda_n-A_n\ge0\) for every index directly proves RH,
> even though it does not force A1 at a prefixed finite cutoff through A0's
> two-sided bound alone.

**Role.** Extract a weaker uniform choice from the improvement of
`104_22` and from the declared floor \(T_n\ge1000\). With the effective
cutoff fixed by that single floor, the original A1 does not even require
\(3\lambda_n-A_n\ge0\): a real margin with exponent

\[
 r_*={2002\over501}=3.996007984\ldots<4.          \tag{1}
\]

suffices. The Euler and Gamma channels preserve positivity for real
exponents by infinite divisibility. The price is that the pole no longer
has four channels and instead becomes a signed hypergeometric density.
This document proves the reduction and the positivity of the two
arithmetic–Gamma channels; it does not prove the final sign of the coupled
pole, A1, or RH.

## 1. Family deduced from A0 and from the cutoff floor

By `104_22`, for every Phase 104 cutoff,

\[
 |R_n(T_n)|\le {A_n\over4(1+T_n)}.                \tag{2}
\]

Let \(r>1\) and suppose

\[
 D_n^{[r]}:=r\lambda_n-A_n\ge0.                  \tag{3}
\]

Then

\[
 \begin{aligned}
 C_n(T_n)
 &=\lambda_n-{A_n\over4}-R_n(T_n)\\
 &\ge A_n\left({1\over r}-{1\over4}
                  -{1\over4(1+T_n)}\right).       \tag{4}
 \end{aligned}
\]

The right-hand side is non-negative exactly when

\[
 \boxed{r\le r_{\max}(T_n):={4(1+T_n)\over T_n+2}.} \tag{5}
\]

The function \(r_{\max}(T)\) is increasing. The binding effective triple
of `104_01` imposes \(T_n\ge U_0=1000\), so that the fixed value

\[
 \boxed{r_*:=r_{\max}(1000)={4\cdot1001\over1002}
 ={2002\over501}}                                  \tag{6}
\]

serves simultaneously for every \(n\). Thus:

**Theorem 1.1.** For every \(n\ge150\),

\[
 D_n^{[r_*]}\ge0\quad\Longrightarrow\quad C_n(T_n)\ge0. \tag{7}
\]

Independently, by the already-proved compact identity,
\(C_n(T_n)\ge0\Longleftrightarrow\mathrm{A1}_n\). Hence (7) implies
the original A1.

Target (7) is strictly weaker than the cubic one: from
\(3\lambda_n-A_n\ge0\) it follows that
\(r_*\lambda_n-A_n\ge(r_*/3-1)A_n>0\), but not conversely.

## 2. Completed germ for a real exponent

With

\[
 G(s)=s\pi^{-s/2}\Gamma(s/2),\qquad
 Y_r(s)={\xi(s)^r\over G(s)},                     \tag{8}
\]

the power is understood as the analytic germ determined by
\(r\log\xi(s)-\log G(s)\) around \(s=1\). It is not claimed that
\(Y_r\) is an entire function when \(r\notin\mathbb Z\); only its local
logarithm is used, which is single-valued because \(\xi(1)\ne0\). One has
exactly

\[
 \log{Y_r((1-z)^{-1})\over Y_r(1)}
 =\sum_{n\ge1}{r\lambda_n-A_n\over n}z^n.         \tag{9}
\]

In the real half-plane \(s>1+u\), where every factor is positive, the
cocycle is unambiguous and

\[
 \boxed{
 {Y_r(s-u)\over Y_r(s)}=H_u(s)^rK_u(s)^{r-1}.}    \tag{10}
\]

The direct normalization

\[
 {Y_r(s_\varepsilon(z)-u)/Y_r(s_\varepsilon(z))-1
  \over u(1-z)^2}
 =\sum_{m\ge0}h_{m,\varepsilon,c}^{[r]}z^m,
 \quad u=c\varepsilon,                            \tag{11}
\]

satisfies

\[
 \boxed{
 h_{n-1,\varepsilon,c}^{[r]}
 \longrightarrow-(r\lambda_n-A_n).}              \tag{12}
\]

By (7), proving that the limit of (11) is non-positive for \(r=r_*\) and
\(n\ge150\) proves the original A1.

## 3. Euler positivity for every real power

Set \(A_u(s)=\zeta(s-u)/\zeta(s)\). In \(\Re s>1+u\),

\[
 \log A_u(s)
 =\sum_p\sum_{k\ge1}{p^{ku}-1\over k p^{ks}},     \tag{13}
\]

and every coefficient is non-negative. For every \(r>0\),

\[
 A_u(s)^r
 =\exp\left(
 r\sum_p\sum_{k\ge1}{p^{ku}-1\over k p^{ks}}
 \right)                                          \tag{14}
\]

has a Dirichlet series with non-negative coefficients: this follows from
exponentiating, prime by prime, series with non-negative coefficients and
constant term one. In probabilistic language, the law of \(\log N\) is
compound-Poisson with Lévy measure

\[
 \boxed{
 \nu_A^{[r]}
 =r\sum_p\sum_{k\ge1}
 {p^{-k(1+\varepsilon-u)}-p^{-k(1+\varepsilon)}\over k}
 \delta_{k\log p}.}                               \tag{15}
\]

\(r\) need not be an integer.

## 4. Gamma positivity for every real power

The normalized Gamma ratio of `104_21` is infinitely divisible. Its Lévy
measure is

\[
 \nu_K(x)\,dx
 ={e^{-(3+\varepsilon-u)x}-e^{-(3+\varepsilon)x}
   \over x(1-e^{-2x})}\,dx\ge0.                  \tag{16}
\]

Hence \(K_u^{r-1}\), normalized at \(s=1+\varepsilon\), is the Laplace
transform of a positive measure for every \(r>1\), with Lévy measure
\((r-1)\nu_K\). In particular this holds for \(r_*\).

Sections 3–4 prove that passing from \(r=3\) to \(r_*\) loses neither
Euler nor Gamma positivity. The only signed channel remains the pole.

## 5. Exact density of the real pole

For \(s-1=\varepsilon+t\),

\[
 \left(1-{u\over s-1}\right)^r
 =\sum_{j\ge0}(-1)^j{r\choose j}{u^j\over(\varepsilon+t)^j}. \tag{17}
\]

Its inverse Laplace transform is

\[
 \delta_0(dy)+e^{-\varepsilon y}
 \sum_{j\ge1}(-1)^j{r\choose j}
 {u^jy^{j-1}\over(j-1)!}\,dy.                    \tag{18}
\]

After \(u=c\varepsilon\) and \(q=\varepsilon y\), the continuous density
sums exactly to

\[
 \boxed{
 -rc\,e^{-q}\,{}_1F_1(1-r;2;cq)\,dq.}            \tag{19}
\]

For \(3<r<4\), channels \(j=1,3\) of (18) are negative and channels
\(j=2\) and \(j\ge4\) are positive. In particular (19) is negative at
\(q=0\); it is not a positive measure and does not allow a
channel-by-channel proof. The series converges for every \(q\), so (19)
is an identity, not an asymptotic expansion.

## 6. Uniform positive-measure stop-gate

The defect does not disappear upon multiplying by the arithmetic and Gamma
channels. Normalize at \(s_0=1+\varepsilon\) the pole–Gamma product

\[
 B_{r,u}(t)=\left({P_u(s_0+t)\over P_u(s_0)}\right)^r
             \left({K_u(s_0+t)\over K_u(s_0)}\right)^{r-1},
 \qquad P_u(s)=1-{u\over s-1}.                    \tag{20}
\]

At \(u=0\), the continuous part of the inverse Laplace transform of
\(\partial_uB_{r,u}|_{u=0}\) is

\[
 \boxed{
 f_{r,\varepsilon}(x)
 =-r e^{-\varepsilon x}
 +(r-1){e^{-(3+\varepsilon)x}\over1-e^{-2x}}.}    \tag{21}
\]

At \(x_0=\frac12\log2\), before the first prime atom,

\[
 f_{r,\varepsilon}(x_0)
 =e^{-\varepsilon x_0}\left(-r+{r-1\over\sqrt2}\right)<0
 \qquad(r>1).                                     \tag{22}
\]

The normalized arithmetic factor \(A_u^r\) has positive mass at zero and
all its remaining support in \([\log2,\infty)\). Hence it cannot alter the
density in a neighborhood of \(x_0\). Taking a non-negative test function
supported in that neighborhood, (22) proves that, for each fixed \(r>1\)
and \(\varepsilon>0\), there exists \(u_0(r,\varepsilon)>0\) such that for
\(0<u<u_0(r,\varepsilon)\) the normalized completed cocycle is not the
Laplace transform of a positive measure.

The quantifiers also cover the correlated path, but this does not follow
from a Taylor expansion uniform in \(u\): the polar normalization contains
\((1-c)^{-r}\). It is checked directly. Let \(\varphi\ge0\) be smooth,
nonzero, with support in a compact interval around \(x_0\) contained in
\((0,\log2)\), and let \(\mu_{r,c\varepsilon,\varepsilon}\) be the inverse
Laplace transform of the full normalized cocycle. Since there are no
arithmetic atoms in that support, and the mass at zero of the Euler
channel tends to \((1-c)^r\) and cancels the polar factor
\((1-c)^{-r}\), the diagonal expansion gives

\[
 \langle\varphi,\mu_{r,c\varepsilon,\varepsilon}\rangle
 =c\varepsilon\!\int_0^\infty\!\varphi(x)
 \left[-r+(r-1){e^{-3x}\over1-e^{-2x}}\right]dx+o(\varepsilon). \tag{22a}
\]

The bracket in (22a) equals \(-r+(r-1)/\sqrt2<0\) at \(x_0\), and remains
negative on a sufficiently small support. Hence the left-hand side is
negative for every sufficiently small \(\varepsilon>0\) along
\(u=c\varepsilon\). Here \(o(\varepsilon)\) is understood for fixed
\(c,r\) and fixed compact test function \(\varphi\).

Thus the Bernstein, positive-measure, and stochastic-order routes are
uniformly ruled out, even in the regime \(u\downarrow0\) that extracts
(12). This does not decide the individual Cayley coefficients.

## 7. Diagnostic and exact front

For a real exponent, a Cauchy extraction requires coherently continuing
the branch of \(r\log\xi\) along the whole contour. The current version of
`tools/cubic_cocycle_probe.py` uses pointwise principal logarithms; its
non-integer rows are considered exploratory and **are not used as
evidence** in this document.

The uniform choice obtained using only the declared floor
\(T_n\ge1000\) is

\[
 \boxed{
 r_*\lambda_n-A_n\ge0\qquad(n\ge150),
 \quad r_*={2002\over501}.}                       \tag{23}
\]

Equivalently, one must globally control (11) after combining the
compound-Poisson law (15), the Gamma law (16), and the polar density
(19). The gate is RH-strength, but it is quantitatively weaker than every
margin used earlier in the phase.

## Status

- **Proved:** Theorem 1.1, the local real cocycle, the infinitely
  divisible Euler–Gamma positivity, and the polar formula (19).
- **Progress:** using only \(T_n\ge1000\), the required coefficient drops
  from \(1/3\) to \(1/r_*=501/2002\approx0.25024975\), very close to the
  minimum \(1/4\).
- **Open:** the global sign of (11); neither A1 nor RH is claimed.
</content>
