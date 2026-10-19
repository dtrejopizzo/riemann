# 104_83 — Fourier gate for \(\Xi\): exact cumulants and modular boundary cancellation

**Result.** The positive theta representation carries the deep
observable of `104_75` to an exact formula in the cumulants of a
single probability law. That formula does not give a new inequality:
the logarithm preserves all the zeros of \(\xi\), and the deep event
is precisely a tail of the binomial transform of all the cumulants.

The Fourier audit does produce a falsifier specific to the Riemann
kernel. Writing the kernel as a sum of its theta modes,

\[
 \Phi(u)=\sum_{m\ge1}f_m(u),\qquad
 f_m(u)=\pi m^2e^{5u/2}(2\pi m^2e^{2u}-3)
          e^{-\pi m^2e^{2u}},                                  \tag{1}
\]

it is known from `103_47` that the pointwise tail satisfies
\(0<(\Phi-f_1)/f_1<1/300\). However, modularity forces

\[
 \Phi^{(2j+1)}(0)=0\quad(j\ge0),                                \tag{2}
\]

while \(f_1'(0)>0\). Consequently, the tail, although pointwise
smaller than \(1/300\), cancels **exactly one hundred percent** of the
first odd jet. In Fourier the loss is total:

\[
 C_1(t):=\int_0^\infty f_1(u)\cos(tu)\,du
       =-{f_1'(0)\over t^2}+O(t^{-4}),                           \tag{3}
\]

\[
 C_{\ge2}(t):=\int_0^\infty(\Phi-f_1)(u)\cos(tu)\,du
       ={f_1'(0)\over t^2}+O(t^{-4}),
 \qquad {C_{\ge2}(t)\over C_1(t)}\longrightarrow-1.            \tag{4}
\]

Thus, first-mode dominance, mode truncation, finite-order PF, and
pointwise tail bounds do not control the deep observable. The only
surviving theta possibility must simultaneously use **all** the
modular weights, **all** the cancellations (2), and the logarithm
before extracting coefficients. That remaining inequality is not
proved here, nor is the deep limit, nor RH.

---

## 1. The exact probabilistic coordinate

The theta identity, with an irrelevant positive constant, is

\[
 \xi(s)=c\int_{\mathbb R}\Phi(|u|)e^{(s-1/2)u}\,du.             \tag{5}
\]

Define the tilted probability

\[
 d\nu(u)={\Phi(|u|)e^{u/2}\,du
            \over\int_{\mathbb R}\Phi(|v|)e^{v/2}\,dv},
 \qquad U\sim\nu.                                                \tag{6}
\]

Then, for every \(t\in\mathbb C\),

\[
 M(t):=\mathbb E e^{tU}={\xi(1+t)\over\xi(1)}.                 \tag{7}
\]

Since \(1/(1-z)=1+z/(1-z)\), the Li generating identity gives

\[
 \boxed{
 \sum_{n\ge1}{\lambda_n\over n}z^n
 =\log\mathbb E\exp\!\left({z\over1-z}U\right).}              \tag{8}
\]

If \(\kappa_j\) is the cumulant of order \(j\) of \(U\), the expansion
is absolutely legitimate near zero and produces

\[
 \boxed{
 \lambda_n
 =\sum_{j=1}^n{\binom nj\over(j-1)!}\,\kappa_j.}               \tag{9}
\]

Therefore the deep observable is exactly

\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\left\{
  \sum_{j=1}^n{\binom nj\over(j-1)!}\kappa_j+\log(n+1)
  \le-e^{\sqrt X}\right\}}.                                   \tag{10}
\]

Positivity of \(\nu\) proves \(\kappa_2\ge0\), but does not fix the
higher cumulants. More decisively, \(\log M\) has singularities
exactly at the zeros of \(M\). A Cauchy bound for its coefficients
that crosses the first interior zero already presupposes the absence
of that zero. Thus (8) does not eliminate the meromorphic obstruction
of `104_80`; it expresses it with a single positive law.

## 2. PF/total-positivity audit

The strict log-concavity of the real kernel \(\Phi(|u|)\) was proved
in `103_34`; this provides second-order information. It cannot be
silently lifted to PF\(_\infty\).

Indeed, Schoenberg's characterization of Pólya frequency functions
states that, if a nonzero integrable function is PF\(_\infty\), its
bilateral Laplace transform is, on its strip of convergence, the
reciprocal of an entire Laguerre--Pólya function. In particular that
transform has no zeros where it is finite. Here

\[
 \int_{\mathbb R}\Phi(|u|)e^{itu}\,du=c^{-1}\xi(1/2+it)       \tag{11}
\]

has unconditionally infinitely many real zeros. Hence the translation
kernel associated with the real \(\Phi\) **is not PF\(_\infty\)**.

This does not contradict the second-order PF property. It only shows
that some higher finite-order minor must fail; there is no need to
guess which one or to use a decimal computation. On the other hand,
imposing PF/Jensen at all orders on the central sequence

\[
 c_N={1\over(2N)!}\int_{\mathbb R}u^{2N}\Phi(|u|)\,du           \tag{12}
\]

is precisely the membership of \(\Xi\) in Laguerre--Pólya, equivalent
to RH (`103_31`). Therefore:

```text
Infinite translation PF: false for the real kernel;
Infinite central PF/Jensen: criterion equivalent to RH;
Fixed-order PF: insufficient for (10).
```

## 3. The first jet already destroys modal dominance

The logarithmic derivative of the first mode at zero is

\[
 {f_1'(0)\over f_1(0)}
 ={5\over2}+{4\pi\over2\pi-3}-2\pi
 ={15\pi-4\pi^2-15/2\over2\pi-3}.                     \tag{13}
\]

It is strictly positive with a rational certificate. The function
\(g(x)=15x-4x^2-15/2\) decreases for \(x\ge3\), and \(\pi<22/7\);
therefore

\[
 g(\pi)>g(22/7)={13\over98}>0.                                 \tag{14}
\]

The modular transformation makes \(\Phi(|u|)\) smooth and even. In
particular \(\Phi'(0)=0\). The series of derivatives of (1) converges
absolutely at zero by the factor \(e^{-\pi m^2}\), so that

\[
 \boxed{\sum_{m\ge2}f_m'(0)=-f_1'(0)<0.}                        \tag{15}
\]

The contrast with the pointwise bound is exact:

\[
 0<\sum_{m\ge2}f_m(0)<{f_1(0)\over300},
 \qquad
 \sum_{m\ge2}f_m'(0)=-f_1'(0).                                \tag{16}
\]

Differentiation amplifies the higher modes by powers of
\(m^2\); no Fourier estimate preserves the factor \(1/300\) without
accounting for this cancellation.

## 4. Proof of the complete Fourier cancellation

All derivatives of \(f_1\) are integrable on \([0,\infty)\). Four
integrations by parts give

\[
 C_1(t)=-{f_1'(0)\over t^2}
        +{f_1'''(0)\over t^4}
        +{1\over t^4}\int_0^\infty f_1^{(4)}(u)\cos(tu)\,du.   \tag{17}
\]

This proves (3), and in particular \(C_1(t)<0\) for every
sufficiently large \(t\).

For the full kernel, smooth parity gives (2), and all its derivatives
are integrable. Repeating integration by parts \(2N\) times,

\[
 C(t):=\int_0^\infty\Phi(u)\cos(tu)\,du=O_N(t^{-2N})
 \qquad(N\ge1).                                                 \tag{18}
\]

Since \(C_{\ge2}=C-C_1\), equations (17)--(18), with \(N=3\),
prove (4). In particular, at each sufficiently high critical zero
\(\gamma\) of \(\Xi\),

\[
 C_{\ge2}(\gamma)=-C_1(\gamma),                                \tag{19}
\]

and both sides are nonzero. There are infinitely many such zeros, by
the unconditional theorem of Hardy and by the eventual sign of
\(C_1\). The theta tail is not a small Fourier perturbation: it is the
term that cancels all the algebraic jets of the principal mode.

## 5. The residual identity that preserves all the weights and modularity

The exact translation of `103_47`,

\[
 f_m(u)=m^{-1/2}f_1(u+\log m),                                  \tag{20}
\]

allows the full kernel to be rearranged without removing any mode. For
every \(w\in\mathbb C\), by locally uniform absolute convergence,

\[
\begin{aligned}
 \int_0^\infty\Phi(u)\cosh(wu)\,du
  =\int_0^\infty f_1(v)
   \sum_{m\le e^v}m^{-1/2}
       \cosh\!\bigl(w(v-\log m)\bigr)\,dv.             \tag{21}
\end{aligned}
\]

Indeed, substitute (20) and, in the \(m\)-th term, change variables
\(v=u+\log m\). The domain becomes \(v\ge\log m\); interchanging the
sum and the integral, exactly the integers \(m\le e^v\) survive.
Equivalently, the bracket in (21) is

\[
 {1\over2}\left\{
 e^{wv}\sum_{m\le e^v}m^{-1/2-w}
 +e^{-wv}\sum_{m\le e^v}m^{-1/2+w}\right\}.           \tag{22}
\]

This is the residual possibility that simultaneously preserves the
exact weights of the theta sum, the modular shifts, and the complex
phase. For real \(w\) the integrand is positive. For
\(w=b+it\), \(b\ne0\), the two sums in (22) are complex and have no
sign; their non-vanishing for every \(t\) is exactly the missing zero
localization. Replacing them by their integral term, bounding them by
moduli, or truncating \(m\) destroys the cancellations (2)--(4).

Identity (21) is therefore a legitimately theta-specific entry point.
It is not a proof that its integral is nonzero off the imaginary axis.

## 6. Consequence for Deep-\(\Lambda\)

Equations (8)--(10) show that a density inequality can be formulated
entirely with the positive kernel. Equations (15)--(19) prove it
cannot be obtained through any of these steps:

1. removing the modes \(m\ge2\) by their pointwise size;
2. keeping a finite number of boundary cancellations;
3. using fixed-order PF/TP and then passing to the limit;
4. replacing the logarithm of (8) by the linear transform (11).

The only non-falsified Fourier successor is a **non-local, all-orders**
inequality for the complete modular sum, applied after the logarithm.
It must simultaneously use the exact weights
\(m^{-1/2}\), the shifts \(\log m\) from `103_47`, and the entire
family (2), for example directly via (21)--(22). Separating any of
these three pieces returns to (3)--(4).

This successor is a precise specification, not an already proved
lemma. The present document closes off the dominance/PF Fourier
attack, but does not prove (10), Deep-\(\Lambda\), A1, or RH.

## 7. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 xi_fourier_deep_gate_check.py
```

The checker certifies the sign (14) with `Fraction`, verifies the
cancellation of the first four odd jets by the theta sum, and shows,
only as a quadrature diagnostic, the Fourier cancellation at the first
three critical zeros. The proof of (3)--(4) is the integration by
parts above and does not depend on floating point.
