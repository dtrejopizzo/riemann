# 104_86 — Positive Bose kernel and Mellin sine self-reflection

**Result.** The continuation of \(\zeta\) in the critical strip admits a
single-sign Mellin representation. Set

\[
 q(x)={1\over x}-{1\over e^x-1}>0.                     \tag{1}
\]

For \(0<\Re s<1\),

\[
 \boxed{
 \int_0^\infty x^{s-1}q(x)\,dx=-\Gamma(s)\zeta(s).}    \tag{2}
\]

The functional equation is equivalent to the exact self-reflection

\[
 \boxed{
 q(x)={1\over\pi}\int_0^\infty
 q(t)\sin\left({xt\over2\pi}\right)\,dt,}              \tag{3}
\]

with the integral understood in the Dirichlet improper sense.

However, (1)--(3) do not force the zeros to \(\Re s=1/2\). The kernel is not
completely monotone nor PF\(_\infty\), and there exists a positive,
decreasing kernel with the same asymptotics and the same sine
reflection, whose transform has quartets strictly off the line. Hence
single sign, monotonicity, log-concavity, functional symmetry, and
self-reciprocity do not prove Deep-\(\Lambda\) or RH.

---

## 1. Single-sign representation

The classical Mellin formula,

\[
 \Gamma(s)\zeta(s)=\int_0^\infty {x^{s-1}\over e^x-1}\,dx
 \qquad(\Re s>1),                                      \tag{4}
\]

is renormalized by subtracting \(1/x\). The integral in (2) converges on
\(0<\Re s<1\): near zero,

\[
 q(x)={1\over2}-{x\over12}+{x^3\over720}
       -{x^5\over30240}+\cdots,                         \tag{5}
\]

and at infinity \(q(x)=x^{-1}+O(e^{-x})\). Continuation from (4), or an
integration by parts with a cutoff, proves (2). The sign is consistent with
\(\zeta(\sigma)<0\) for \(0<\sigma<1\).

There is also an exact probability law. With \(x=e^u\), define

\[
 Q(u)=1-{e^u\over e^{e^u}-1}=e^u q(e^u),               \tag{6}
\]

and

\[
 p(u)=Q'(u)
 ={x\{(x-1)e^x+1\}\over(e^x-1)^2}>0.                  \tag{7}
\]

We have \(Q(-\infty)=0\), \(Q(+\infty)=1\), so that
\(\int_\mathbb R p=1\). Integrating by parts in (2) gives

\[
 \boxed{
 (s-1)\Gamma(s)\zeta(s)
 =\int_\mathbb R p(u)e^{(s-1)u}\,du.}                  \tag{8}
\]

Thus the zeros of \(\zeta\) in the strip are complex zeros of the moment
generating function of an explicit probability law. The positivity of a
law does not exclude such zeros.

## 2. Derivation of the sine reflection

The functional equation applied to (2) gives

\[
 M(s)=R(s)M(1-s),\qquad M(s)=-\Gamma(s)\zeta(s),         \tag{9}
\]

with

\[
 R(s)=2^s\pi^{s-1}\Gamma(s)\sin{\pi s\over2}
 ={(2\pi)^s\over2\cos(\pi s/2)\Gamma(1-s)},
 \qquad R(s)R(1-s)=1.                                  \tag{10}
\]

The function

\[
 r(x)={1\over\pi}\sin{x\over2\pi}                    \tag{11}
\]

has Mellin transform \(R(s)\), by continuation from its
fundamental strip. Moreover,

\[
 \mathcal M[x^{-1}q(1/x)](s)=M(1-s).                    \tag{12}
\]

The multiplicative convolution of (10)--(12), followed by the change
\(t=1/y\), proves (3). The kernel \(r\) changes sign; the functional
equation is a signed symmetry, not a positive operator.

## 3. Positivity stop-gates

Expansion (5) gives

\[
 q'''(0^+)={1\over120}>0,                               \tag{13}
\]

contradicting \((-1)^3q'''\ge0\), necessary for complete
monotonicity. Even the weaker log-convexity condition of a positive
Laplace transform fails:

\[
 \lim_{x\downarrow0}\{q(x)q''(x)-q'(x)^2\}
 =-{1\over144}<0.                                      \tag{14}
\]

In the logarithmic coordinate,

\[
 K_a(u)=e^{au}q(e^u),\qquad0<a<1,                       \tag{15}
\]

is indeed strictly log-concave; this only provides PF\(_2\). Its
bilateral transform is

\[
 \int_\mathbb R K_a(u)e^{zu}\,du
 =-\Gamma(a+z)\zeta(a+z).                              \tag{16}
\]

For \(a=1/2\), (16) has infinitely many zeros on the imaginary axis by
Hardy's theorem. A Pólya frequency function PF\(_\infty\) would have a
zero-free transform in its fundamental strip. Hence the real kernel
is not PF\(_\infty\); some upper minor must fail.

## 4. Falsifier with the same symmetry

Fix \(0<\eta<1/2\) and \(a>0\). Let

\[
 \nu=\delta_{-a}+\delta_a
      +\eta(\delta_{-2a}+\delta_{2a}),                  \tag{17}
\]

and choose \(c>0\) so that

\[
 d\mu(v)=c e^{-v/2}\,d\nu(v)                           \tag{18}
\]

has the required normalization. Define

\[
 \widetilde q(x)=\int q(xe^{-v})\,d\mu(v)>0.           \tag{19}
\]

It is decreasing, has \(\widetilde q(0^+)=1/2\) after normalizing and
\(x\widetilde q(x)\to1\). Its Mellin transform is

\[
 \widetilde M(s)=M(s)X(s),                             \tag{20}
\]

where

\[
 X(s)=2c\left\{
 \cosh(a(s-\tfrac12))
 +\eta\cosh(2a(s-\tfrac12))\right\},
 \qquad X(1-s)=X(s).                                   \tag{21}
\]

By (9) and (21), \(\widetilde M\) satisfies the same functional equation and
\(\widetilde q\) the same self-reflection (3). Nevertheless, writing
\(y=a(s-1/2)\), its additional zeros satisfy

\[
 2\eta\cosh^2y+\cosh y-\eta=0.                         \tag{22}
\]

The root

\[
 x_-={-1-\sqrt{1+8\eta^2}\over4\eta}<-1               \tag{23}
\]

produces

\[
 y=\pm\mathrm{arcosh}(-x_-)+(2k+1)\pi i.        \tag{24}
\]

If \(a>2\mathrm{arcosh}(-x_-)\), those zeros satisfy
\(0<\Re s<1\) and \(\Re s\ne1/2\).

## 5. Decision

```text
proved:
  positive Mellin representation (2) and probabilistic one (8);
  exact sine self-reflection (3);
  q is not CM, Stieltjes, nor PF-infinity;
  a positive kernel with the same asymptotics and the same reflection
  admits off-line quartets.

ruled out:
  single sign + monotonicity/log-concavity + sine FE => RH.

not proved:
  an additional property specific to the arithmetic q implying
  Deep-Lambda, A1, or RH.
```
