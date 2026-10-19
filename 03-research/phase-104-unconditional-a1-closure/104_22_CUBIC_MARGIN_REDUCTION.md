# 104_22 — Strictly weaker cubic reduction of A1

**Role.** Retain a factor that the published proof of A0 discards and use
it to replace the strong margin

\[
 2\lambda_n-A_n\ge0
\]

with the strictly weaker margin

\[
 \boxed{D_n^{[3]}:=3\lambda_n-A_n\ge0.}           \tag{1}
\]

This replacement does imply the **original A1**, with the same coefficient
\(1/4\) and the same cutoff, not a variant of the inequality. The
associated cubic cocycle has three positive Euler copies and two positive
Gamma copies. Proving its global sign would close A1 and RH. The sign is
not yet proved in this document.

## 1. The factor retained in A0

The last line of the proof of `thm:a0-tail-direct`, before it is relaxed,
is

\[
 |R_n(T_n)|
 \le {B_n\over4}\int_{T_n}^{\infty}(1+u)^{-2}\,du,
 \qquad 0<B_n\le A_n.                              \tag{2}
\]

The integral in (2) is evaluated exactly. Hence A0 actually proves

\[
 \boxed{
 |R_n(T_n)|\le {B_n\over4(1+T_n)}
              \le {A_n\over4(1+T_n)}.}             \tag{3}
\]

The printed bound \(|R_n(T_n)|\le A_n/4\) is obtained from (3) by
discarding the factor \((1+T_n)^{-1}\). No hypothesis is added and RH is
not used. For the effective triple fixed in `104_01`, \(T_n\ge U_0=1000\);
for the abstract version it suffices to replace any admissible cutoff by
\(\max(T_n,2)\).

## 2. Cubic reduction theorem

Recall the exact identity for the original A1:

\[
 C_n(T_n)=\lambda_n-{1\over4}A_n-R_n(T_n).         \tag{4}
\]

**Theorem 2.1.** Suppose \(A_n>0\), \(T_n\ge2\), (3), and
\(D_n^{[3]}\ge0\). Then \(C_n(T_n)\ge0\), and hence A1 holds at that
index.

**Proof.** From \(3\lambda_n-A_n\ge0\) one obtains
\(\lambda_n\ge A_n/3\). Using (3) in (4),

\[
 \begin{aligned}
 C_n(T_n)
 &\ge {A_n\over3}-{A_n\over4}-|R_n(T_n)|\\
 &\ge {A_n\over12}-{A_n\over4(1+T_n)}\ge0,
 \end{aligned}                                    \tag{5}
\]

because \(T_n\ge2\). \(\square\)

Target (1) is strictly weaker than the one used in `103_59`–`104_21`.
Indeed, \(2\lambda_n-A_n\ge0\) implies
\(3\lambda_n-A_n\ge A_n/2>0\), whereas the algebraic value
\(\lambda_n=A_n/3\) satisfies (1) and violates the quadratic margin.

## 3. The completed family and the cubic cocycle

Set

\[
 G(s)=s\pi^{-s/2}\Gamma(s/2),\qquad
 Y_r(s)={\xi(s)^r\over G(s)},\qquad r\ge2.         \tag{6}
\]

The definitions of the Li coefficients and of the archimedean part give

\[
 \log{Y_r((1-z)^{-1})\over Y_r(1)}
 =\sum_{n\ge1}{D_n^{[r]}\over n}z^n,
 \qquad D_n^{[r]}=r\lambda_n-A_n.                 \tag{7}
\]

Let

\[
 F(s)=(s-1)\zeta(s),\quad
 H_u(s)={F(s-u)\over F(s)},\quad
 K_u(s)=\pi^{u/2}{\Gamma(1+(s-u)/2)\over
                         \Gamma(1+s/2)}.           \tag{8}
\]

Since \(\xi(s)=\tfrac12G(s)F(s)\) and
\(G(s-u)/G(s)=K_u(s)\), one has the exact factorization

\[
 \boxed{
 {Y_r(s-u)\over Y_r(s)}=H_u(s)^rK_u(s)^{r-1}.}    \tag{9}
\]

For \(r=3\), the new front is

\[
 \boxed{\mathcal S_u^{[3]}(s)=H_u(s)^3K_u(s)^2.} \tag{10}
\]

In the half-plane \(\Re s>1+u\), the three Euler copies have the series

\[
 \left({\zeta(s-u)\over\zeta(s)}\right)^3
 =\sum_{m\ge1}{(J_u*J_u*J_u)(m)\over m^s},
 \qquad J_u*J_u*J_u\ge0,                           \tag{11}
\]

and the two copies of \(K_u\) are the convolution of two positive Beta
measures. The only explicit signs are in the polar factor
\((1-u/(s-1))^3\); they must be kept coupled with (11) and Gamma.

The inverse Laplace transform of that factor, in the coordinate used by
(12), has the four exact channels

\[
 \delta_0-3u e^{-\varepsilon y}\,dy
 +3u^2y e^{-\varepsilon y}\,dy
 -{u^3\over2}y^2e^{-\varepsilon y}\,dy.           \tag{11a}
\]

After \(u=c\varepsilon\), \(r=\varepsilon y\), the continuous part is

\[
 c\left(-3+3cr-{c^2r^2\over2}\right)e^{-r}\,dr. \tag{11b}
\]

It is negative near zero and for large \(r\), for every \(c>0\). Hence
the cubic margin is not obtained by declaring the four channels separately
positive: the advantage of (1) must be exploited in the full
Euler–Gamma–pole sum.

## 4. Coefficients and the exact gate

Fix

\[
 s_\varepsilon(z)=1+\varepsilon+{z\over1-z},
 \qquad u=c\varepsilon,\quad0<c<1,                \tag{12}
\]

and define the normalization that targets the margin **directly**, without
introducing an unnecessary first difference,

\[
 {\mathcal S_{c\varepsilon}^{[3]}(s_\varepsilon(z))-1
  \over c\varepsilon(1-z)^2}
 =\sum_{m\ge0}h_{m,\varepsilon,c}^{[3]}z^m.       \tag{13}
\]

Removing the regulator,

\[
 {\mathcal S_u^{[3]}(s)-1\over u}
 \longrightarrow-{(Y_3)'(s)\over Y_3(s)}.
\]

Differentiating (7) and using \((1-z)^{-2}=s^2\) gives

\[
 \boxed{
 h_{n-1,\varepsilon,c}^{[3]}
 \longrightarrow-D_n^{[3]}=-(3\lambda_n-A_n),
 \qquad n\ge1.}                                   \tag{14}
\]

Indeed,

\[
 s^2{(Y_3)'(s)\over Y_3(s)}
 ={d\over dz}\log Y_3((1-z)^{-1})
 =\sum_{n\ge1}D_n^{[3]}z^{n-1}.                   \tag{15}
\]

Hence it suffices to prove \(h_{n-1,\varepsilon,c}^{[3]}\le0\) upon
removing the regulator, for every \(n\ge150\). This condition converges
exactly to the direct cubic gate \(D_n^{[3]}\ge0\); it does not require
the stronger condition \(\Delta D_n^{[3]}\ge0\). Theorem 2.1 and the
already-proved chain A1 \(\Rightarrow\Omega_7\Rightarrow\) RH would then
complete the goal.

The earlier normalization of `104_19`, with only \((1-z)^{-1}\), remains
valid, but it converges to \(-\Delta D_n^{[3]}\). It is kept only as an
optional tool should a difference identity favor it; it is not the main
target.

## 5. Third-order local identity

The tower factorization of `104_20` generalizes with no loss to every
**integer** \(r\ge1\). If \(Q=p^u\) and

\[
 a_k^{[r]}={k+r-1\choose r-1}Q^k,
 \]

with \(a_k^{[r]}=0\) for \(k<0\), then

\[
 (J_u^{*r})(p^k)=\nabla^r a_k^{[r]}.              \tag{16}
\]

Indeed, the generating functions of both sides are

\[
 \left({1-x\over1-Qx}\right)^r.                  \tag{17}
\]

Discrete summation turns (16) into \((I-\rho E_\ell)^r\), and keeping the
pole \((1-u/(s-1))^r\) gives the local algebraic power
\(\mathsf C_{p,\varepsilon,c}^r\). For \(r=3\) this is an algebraic cube,
not a positive operator. This identity organizes the cubic cocycle but does
not decide the global sign of (13).

For \(r\notin\mathbb N\), the notation \(J_u^{*r}\) and an ordinary
order-\(r\) difference are not used. The local coefficient is instead
defined by \([x^k]((1-x)/(1-Qx))^r\), and the correct treatment is the
fractional binomial series of `104_23`.

## 6. Diagnostic and live front

`tools/cubic_cocycle_probe.py` evaluates (13) by Cauchy extraction at two
radii. In `float64`, for \(\varepsilon=0.1\), \(c=1/2\), one finds

\[
 h_{n-1,\varepsilon,c}^{[3]}<0\qquad(1\le n\le1201).
\]

In the target range \(150\le n\le1201\), the largest observed coefficient
is approximately \(-390.1000885\), at \(n=150\). This is evidence, not a
certificate: both radii share the evaluation of \(\zeta\), Lanczos, FFT,
and floating-point errors.

The live front is therefore:

\[
 \boxed{
 \text{prove globally that }h_{n-1,\varepsilon,c}^{[3]}\le0
 \text{ as }\varepsilon\text{ is removed,}
 \quad\text{or prove directly that }D_n^{[3]}\ge0.} \tag{18}
\]

The global Stein–Mecke identity of `104_21` remains available, now with
the arithmetic Lévy measure multiplied by three and two Gamma copies. A
proof must keep the cubic pole coupled; absolute value or a per-tower sign
returns to the earlier stop-gates.

## Status

- **Proved unconditionally:** (3), Theorem 2.1, and identities
  (7)–(17).
- **Real improvement of the front:** the original A1 no longer requires
  the quadratic margin; the strictly weaker cubic margin suffices.
- **Open:** the global sign (18). This document does not yet prove A1
  or RH.
</content>
