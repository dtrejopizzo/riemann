# 104_24 — Direct channels and the signed Stein–Mecke gate

**Role.** Expand, with no unnecessary differences, the cubic cocycle of
`104_22` and execute the Stein–Mecke successor of `104_21`. The
four-channel expansion is exact and converges to the direct cubic margin
\(3\lambda_n-A_n\). Stein's identity keeps all the other primes, but its
completed generator is signed before the first arithmetic atom. So the
proof-by-positivity-of-the-generator approach dies; the possible special
nonlocal inequality for Laguerre functions does not.

This document proves neither A1 nor RH.

## 1. Exact four-channel theorem

Let

\[
 d_u:=J_u*J_u*J_u\ge0,
 \qquad s_0=1+\varepsilon,\qquad u=c\varepsilon,\quad 0<c<1. \tag{1}
\]

For the Gamma channel, use two copies of the positive measure

\[
 d\nu_{\varepsilon,u}(v)
 ={\pi^{u/2}\over\Gamma(u/2)}
 v^{(1+\varepsilon-u)/2}(1-v)^{u/2-1}\,dv.        \tag{2}
\]

Define

\[
\begin{aligned}
 T_{k,\delta}:={}&
 \sum_{m\ge1}{d_u(m)\over m^{s_0}}
 \int_0^1\!\int_0^1
 L_k^{(1)}\!\left(\log m-\tfrac12\log(vw)\right)
 d\nu(v)d\nu(w),                                  \tag{3}\\
 T_{k,j}:={}&
 \sum_{m\ge1}{d_u(m)\over m^{s_0}}
 \int_0^1\!\int_0^1\!\int_0^\infty
 L_k^{(1)}\!\left(\log m+y-\tfrac12\log(vw)\right)
 {y^j\over j!}e^{-\varepsilon y}\,dy\,d\nu(v)d\nu(w),
 \quad j=0,1,2.                                    \tag{4}
\end{aligned}
\]

Here and below \(d\nu=d\nu_{\varepsilon,u}\). All the sums and integrals
converge absolutely for \(u<\varepsilon\).

**Theorem 1.1.** If

\[
 \mathcal S_u^{[3]}(s)=H_u(s)^3K_u(s)^2,
 \qquad s_\varepsilon(z)=s_0+{z\over1-z},          \tag{5}
\]

then

\[
 \boxed{
 [z^k]{\mathcal S_u^{[3]}(s_\varepsilon(z))\over(1-z)^2}
 =T_{k,\delta}-3uT_{k,0}+3u^2T_{k,1}-u^3T_{k,2}.} \tag{6}
\]

Hence

\[
 \boxed{
 h_{k,\varepsilon,c}^{[3]}
 ={T_{k,\delta}-3uT_{k,0}+3u^2T_{k,1}-u^3T_{k,2}-(k+1)
   \over u}}                                       \tag{7}
\]

and

\[
 h_{k,\varepsilon,c}^{[3]}\longrightarrow
 -(3\lambda_{k+1}-A_{k+1}).                       \tag{8}
\]

**Proof.** We use

\[
 {e^{-xz/(1-z)}\over(1-z)^2}
 =\sum_{k\ge0}L_k^{(1)}(x)z^k                    \tag{9}
\]

and, for \(j\ge0\),

\[
 {1\over(\varepsilon+z/(1-z))^{j+1}}
 =\int_0^\infty {y^j\over j!}e^{-\varepsilon y}
 e^{-yz/(1-z)}\,dy.                               \tag{10}
\]

The expansion

\[
 \left(1-{u\over s-1}\right)^3
 =1-{3u\over s-1}+{3u^2\over(s-1)^2}
       -{u^3\over(s-1)^3}                         \tag{11}
\]

produces (6). The subtracted term in (7) is \(k+1\), not one, because
\([z^k](1-z)^{-2}=k+1\). Finally (8) is (12) of `104_23` with \(r=3\).
\(\square\)

## 2. Global law and the completed Lévy measure

Normalize the arithmetic part via

\[
 \mathbb P(N=m)
 ={d_u(m)m^{-s_0}\over A_u(s_0)^3},
 \qquad X=\log N.                                  \tag{12}
\]

It is compound-Poisson with measure

\[
 \nu_A^{[3]}
 =3\sum_p\sum_{j\ge1}{R_p^j-r_p^j\over j}
 \delta_{j\log p},
 \quad r_p=p^{-1-\varepsilon},\quad
 R_p=p^{-1-(\varepsilon-u)}.                      \tag{13}
\]

A normalized Gamma copy and a normalized polar copy have, respectively,

\[
\begin{aligned}
 \nu_K(y)\,dy
 &={e^{-(3+\varepsilon-u)y}-e^{-(3+\varepsilon)y}
    \over y(1-e^{-2y})}\,dy,\\
 \nu_P(y)\,dy
 &={e^{-(\varepsilon-u)y}-e^{-\varepsilon y}\over y}\,dy.
                                                               \tag{14}
\end{aligned}
\]

The Lévy exponent of the normalized cubic cocycle has the signed kernel

\[
 \boxed{\nu_3=\nu_A^{[3]}+2\nu_K-3\nu_P.}         \tag{15}
\]

## 3. Stein–Mecke identity without losing the other primes

Define \(\mu_3\) by its Laplace transform

\[
 \mathcal L\mu_3(t)
 ={\mathcal S_u^{[3]}(s_0+t)\over
   \mathcal S_u^{[3]}(s_0)}.                       \tag{15a}
\]

To justify the following identity, (13) and also
\(\nu_K\) are truncated to \(y\ge\delta\), the truncated transform is
differentiated, and the limit is taken first in the arithmetic height and
then \(\delta\downarrow0\). The step is dominated because, for each fixed
degree \(k\),

\[
 \int_0^\infty y(1+y^k)|\nu_3|(dy)<\infty.        \tag{15b}
\]

The singularity \(\nu_K(y)\asymp u/(2y)\) at zero has infinite activity,
but the factor \(y\) in (15b) makes it integrable. Thus, for polynomial
test functions,

\[
 \boxed{
 \int x\varphi(x)\,d\mu_3(x)
 =\int_0^\infty y\int\varphi(x+y)\,d\mu_3(x)\,\nu_3(dy).} \tag{16}
\]

This identity keeps inside \(\mu_3\) every prime distinct from the
selected jump. For

\[
 a_k=\int L_k^{(1)}(x)\,d\mu_3(x),                \tag{17}
\]

the Laguerre recurrence produces

\[
\boxed{
 (2k+2)a_k-(k+1)a_{k+1}-(k+1)a_{k-1}
 =\int y\int L_k^{(1)}(x+y)\,d\mu_3(x)\,\nu_3(dy).} \tag{18}
\]

Take \(a_{-1}=0\). Equation (18) is an exact global recurrence, but it has
no fixed sign because \(\nu_3\) is not positive.

## 4. Exact witness before the first prime

The loss of sign occurs in the real arithmetic, not in an abstract
falsifier. Take

\[
 \varepsilon=2,\qquad u=1,\qquad c={1\over2},\qquad
 y_0={1\over2}\log2.                              \tag{19}
\]

Since \(0<y_0<\log2\), measure \(\nu_A^{[3]}\) has no support in a
neighborhood of \(y_0\). Evaluating the continuous part of (15),

\[
 \boxed{
 (2\nu_K-3\nu_P)(y_0)
 ={\frac52-2\sqrt2\over y_0}<0.}                  \tag{20}
\]

The inequality is exact: \(2\sqrt2>5/2\) because
\(8>25/4\). By continuity, \(\nu_3\) is strictly negative on an open
interval contained in \((0,\log2)\).

For \(\varepsilon>0\) fixed, taking \(u\downarrow0\) first,

\[
 {\nu_3\over u}\longrightarrow
 \kappa_\varepsilon(dy),                          \tag{21}
\]

where

\[
\boxed{
 \kappa_\varepsilon(dy)
 =3e^{-(1+\varepsilon)y}\,d\psi(e^y)
 -3e^{-\varepsilon y}\,dy
 +{2e^{-(3+\varepsilon)y}\over1-e^{-2y}}\,dy.}   \tag{22}
\]

On the diagonal path \(u=c\varepsilon\), \(\varepsilon\downarrow0\), the
same convergence is local/vague toward \(\kappa_0\). The continuous
density of that local kernel at \(y_0\) equals

\[
 {2e^{-3y_0}\over1-e^{-2y_0}}-3=\sqrt2-3<0.       \tag{23}
\]

Hence the positivity defect persists exactly in the regime that extracts
\(3\lambda_n-A_n\). The notation \(\kappa_0\) does not designate a measure
of finite total variation on the whole half-line: every global
recomposition with Laguerre functions is understood as the paired Abel
limit \(\varepsilon\downarrow0\), not as an ordinary integral against
\(\kappa_0\).

## 5. Scope of the stop-gate

Measure (22) transparently has the form

\[
 \text{primes}-\text{pole}+\text{Gamma}.
\]

Integrating \(\kappa_\varepsilon\) against the Laguerre response of (18)
and then taking the Abel limit recomposes
\(3\lambda_n-A_n\); integrating the first term by parts against
\(d\psi(e^y)\) returns to \(\psi(e^y)-e^y\), that is, to the weighted
correlation of A1. Stein–Mecke's identity does not by itself add a new
arithmetic input.

Only this mechanism is closed:

> positivity of the completed Lévy measure + jump order
> \(\Longrightarrow h_k\le0\).

Witness (20) falsifies its premise. It does not refute the special
inequality \(h_{k,\varepsilon,c}^{[3]}\le0\): a nonlocal cancellation
specific to the Laguerre functions and to the real masses
\(\Lambda(p^j)\) could still prove it.

## Status

- **Proved:** the four direct channels, the global Stein–Mecke identity,
  the Laguerre recurrence, and the exact sign witness.
- **Ruled out:** closing the cubic margin via positivity/order of the
  completed generator.
- **Open within this mechanism:** a nonlocal signed inequality for
  (18), or the weaker real margin of `104_23`.
</content>
