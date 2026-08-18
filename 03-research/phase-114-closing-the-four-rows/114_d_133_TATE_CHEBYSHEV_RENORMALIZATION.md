# D.133 — Tate renormalization of the complete Chebyshev contact

## Verdict

Let \(F\in L^2([-T,T])\) satisfy the two primitive Tate conditions

\[
 M_+(F)=\int_{-T}^T e^{t/2}F(t)\,dt=0,
 \qquad
 M_-(F)=\int_{-T}^T e^{-t/2}F(t)\,dt=0.                 \tag{0.1}
\]

Write

\[
 C_F(a)=\int_{-T}^{T-a}F(t+a)\overline{F(t)}\,dt
 \qquad(0\leq a\leq2T).                                \tag{0.2}
\]

The two conditions (0.1) do substantially more than remove two abstract
directions.  They cancel the whole continuous main term of the Chebyshev
contact:

\[
 \boxed{
 2\int_0^{2T}e^{a/2}\operatorname {Re}C_F(a)\,da
 =-2\int_0^{2T}e^{-a/2}\operatorname {Re}C_F(a)\,da.}   \tag{0.3}
\]

Consequently the exact completed primitive form, including every prime
power and the full Gamma place, has the renormalized expression

\[
 \boxed{
 -B_{\rm nuc}^{\rm prim}(F,F)
 =\mathcal H_{5/4}(F)
 -2\int_{[1,e^{2T}]}
      x^{-1/2}\operatorname {Re}C_F(\log x)\,dE_\beta(x),} \tag{0.4}
\]

where

\[
 \begin{aligned}
 \mathcal H_{5/4}(F)
 &=\frac1{2\pi}\int_{\mathbb R}
 \left(\operatorname {Re}\psi(5/4+i\tau/2)-\psi(5/4)\right)
 |\widehat F(\tau)|^2\,d\tau\geq0,                     \tag{0.5}\\
 dE_\beta(x)&=d\psi_C(x)-dx+{\beta\over2}\delta_1,
 \qquad
 \beta=\log\pi-\psi(5/4)>0,                            \tag{0.6}\\
 \psi_C(x)&=\sum_{n\leq x}\Lambda(n).
 \end{aligned}

Here \(d\psi_C=\sum_{p^k}\log p\,\delta_{p^k}\), so (0.4) retains, rather
than approximates, all powers \(p^k\).  Formula (0.4) also shows precisely
what remains: a logarithmic-energy bound for the *centred Chebyshev
discrepancy*.  It removes the exponentially large but spurious PNT main
term from the capacity problem.  It does not by itself prove the sign of
the discrepancy term.

## 1. Exact cancellation forced by the two jets

Extend \(F\) by zero outside \([-T,T]\).  Since both factors in

\[
 M_+(F)\overline{M_-(F)}
 =\iint_{\mathbb R^2}e^{(s-t)/2}F(s)\overline{F(t)}\,ds\,dt             \tag{1.1}
\]

vanish, splitting the plane into \(s>t\) and \(s<t\), then putting
\(a=|s-t|\), gives

\[
 0=\int_0^{2T}
 \left(e^{a/2}C_F(a)+e^{-a/2}\overline{C_F(a)}\right)da. \tag{1.2}
\]

Taking real parts proves (0.3).  Notice that both jets are essential: the
product in (1.1) uses \(M_+\) and \(M_-\), not two copies of one moment.

The continuous approximation to the prime-power contact is

\[
 \begin{aligned}
 \mathcal P_0(F)
 &=2\int_1^{e^{2T}}x^{-1/2}\operatorname {Re}C_F(\log x)\,dx\\
 &=2\int_0^{2T}e^{a/2}\operatorname {Re}C_F(a)\,da.       \tag{1.3}
 \end{aligned}

Thus (0.3) turns an apparently exponentially weighted contact into the
bounded-side expression

\[
 \mathcal P_0(F)
 =-2\int_0^{2T}e^{-a/2}\operatorname {Re}C_F(a)\,da.      \tag{1.4}

In particular

\[
 |\mathcal P_0(F)|\leq4\|F\|_2^2,                        \tag{1.5}

\]

because \(|C_F(a)|\leq\|F\|_2^2\).  The \(e^T\)-scale obtained by taking
absolute values before using the jets is therefore artificial.

## 2. The digamma shift from \(1/4\) to \(5/4\)

With the Fourier convention

\[
 \widehat F(\tau)=\int_{\mathbb R}F(t)e^{-i\tau t}\,dt,                 \tag{2.1}

\]

Parseval gives

\[
 2\int_0^\infty e^{-a/2}\operatorname {Re}C_F(a)\,da
 ={1\over2\pi}\int_{\mathbb R}{|\widehat F(\tau)|^2\over
                                    \tau^2+1/4}\,d\tau. \tag{2.2}

The unrenormalized Gamma multiplier in the established A--B--C pullback is

\[
 g_{1/4}(\tau)=\operatorname {Re}\psi(1/4+i\tau/2)-\log\pi.            \tag{2.3}

\]

The recurrence \(\psi(z+1)=\psi(z)+1/z\) and

\[
 \operatorname {Re}{1\over1/4+i\tau/2}={1\over\tau^2+1/4}             \tag{2.4}

\]

show that subtracting the continuous contact (1.3), after the Tate
identity (1.4), changes the multiplier exactly to

\[
 g_{1/4}(\tau)+{1\over\tau^2+1/4}
 =\operatorname {Re}\psi(5/4+i\tau/2)-\log\pi.          \tag{2.5}

Put \(\beta=\log\pi-\psi(5/4)\).  Then (2.5) equals

\[
 h_{5/4}(\tau)-\beta,
 \qquad
 h_{5/4}(\tau)=\operatorname {Re}\psi(5/4+i\tau/2)-\psi(5/4).         \tag{2.6}

\]

For \(x>0\), the absolutely convergent digamma difference gives

\[
 \operatorname {Re}\psi(x+iy)-\psi(x)
 =\sum_{m=0}^\infty
 {y^2\over(m+x)((m+x)^2+y^2)}\geq0.                    \tag{2.7}

Hence \(\mathcal H_{5/4}\) in (0.5) is a genuine positive form.  Also
\(\beta>0\) (numerically \(\beta=1.3721834192256655\ldots\)).

## 3. Exact Stieltjes decomposition, including all \(p^k\)

The arithmetic contact is

\[
 \mathcal P(F)
 =2\sum_{p^k\leq e^{2T}}{\log p\over p^{k/2}}
       \operatorname {Re}C_F(k\log p)
 =2\int_{[1,e^{2T}]}x^{-1/2}\operatorname {Re}C_F(\log x)\,d\psi_C(x).
                                                                    \tag{3.1}

\]

Write \(dR=d\psi_C-dx\).  The established pullback is

\[
 -B_{\rm nuc}^{\rm prim}(F,F)
 =\mathcal G_{1/4}(F)-\mathcal P(F).                    \tag{3.2}

Adding and subtracting \(\mathcal P_0\), and using (2.5)--(2.6), yields

\[
 -B_{\rm nuc}^{\rm prim}(F,F)
 =\mathcal H_{5/4}(F)-\beta\|F\|_2^2
 -2\int x^{-1/2}\operatorname {Re}C_F(\log x)\,dR(x).  \tag{3.3}

Since \(C_F(0)=\|F\|_2^2\), adjoining \((\beta/2)\delta_1\) to \(dR\)
absorbs the scalar term and proves (0.4).

No prime number theorem estimate has been used.  Formula (0.4) is an
identity of quadratic forms on the two-jet primitive source.

## 4. Balanced opening of a prime-power threshold

The same renormalization gives a better typed threshold update.  Let
\(a=\log N\), \(w_N=\Lambda(N)/\sqrt N\), and suppose
\(a/2<T<a\), as is the case throughout the short cell after the birth of
the contact at \(T=a/2\).  Put

\[
 A=[-T,T-a],\qquad A+a=[a-T,T],                           \tag{4.1}

\]

and define

\[
 J_\pm F(t)={F(t+a)\pm F(t)\over\sqrt2},\qquad t\in A.  \tag{4.2}

\]

Then

\[
 2\operatorname {Re}C_F(a)=\|J_+F\|_{L^2(A)}^2-
                             \|J_-F\|_{L^2(A)}^2.       \tag{4.3}

\]

Therefore the exact update is

\[
 q_N(F)=q_{N-1}(F)+w_N\|J_-F\|^2-w_N\|J_+F\|^2.         \tag{4.4}

\]

This is the infinite-dimensional positive/negative spectral split of the
new translated contact.  If \(q_{N-1}\geq0\), define the positive reference

\[
 r_N(F)=q_{N-1}(F)+w_N\|J_-F\|^2.                        \tag{4.5}

\]

Then propagation through the cell is equivalent, with the standard kernel
range convention, to

\[
 \boxed{
 \|\sqrt{w_N}\,J_+\,r_N^{-1/2}\|\leq1.}                \tag{4.6}

\]

Unlike a norm estimate on \(S_a+S_{-a}\), (4.6) retains the favourable
antisymmetric channel \(J_-\).  Unlike Gamma-only absorption, its reference
contains the entire accumulated old contact.  At birth \(|A|=2T-a=0\), so
both channels vanish exactly.

## 5. The sharpened remaining theorem

Combining (0.4) and (4.6), row D is reduced without loss to either of the
following equivalent source-defined statements:

1. **Centred-discrepancy form**

   \[
   2\int x^{-1/2}\operatorname {Re}C_F(\log x)\,dE_\beta(x)
   \leq\mathcal H_{5/4}(F)                              \tag{5.1}
   \]

   for every compactly supported two-jet primitive \(F\).

2. **Balanced threshold capacity**

   \[
   \|\sqrt{w_N}J_+r_N^{-1/2}\|\leq1                    \tag{5.2}
   \]

   for every prime-power cell, uniformly in the directed regularization.

The gain over D.121--D.132 is concrete: the PNT main term has disappeared
exactly, the Gamma reference is manifestly positive, and the entering
contact is split into its two true annular channels.  What is not yet
proved is the uniform estimate (5.1), or equivalently (5.2).  Proving it is
the next sign step; assuming it would be assuming row D.
