# Completed Weil autocorrelation for the direct strong margin

## Exact factorization

For $n\geq1$, put

\[
 f_n(x)=\mathbf 1_{[0,\infty)}(x)L_{n-1}^{(1)}(x),
 \qquad
 F_n(s)=\int_{\mathbb R}f_n(x)e^{-sx}\,dx.
 \tag{1}
\]

The elementary Laplace transform of the Laguerre polynomial gives

\[
 F_n(s)=1-\left(1-{1\over s}\right)^n
       =1-\left({s-1\over s}\right)^n,
 \qquad \Re s>0.
 \tag{2}
\]

Use the Weil involution and additive convolution

\[
 f^\#(x)=e^x\overline{f(-x)},
 \qquad h_n=f_n*f_n^\# .
 \tag{3}
\]

Then

\[
 \mathcal L(f^\#)(s)=\overline{F(1-\bar s)},
 \qquad
 \mathcal Lh_n(s)=F_n(s)F_n(1-s),
 \tag{4}
\]

and, writing $w=(s-1)/s$,

\[
 \boxed{
 \mathcal Lh_n(s)=(1-w^n)(1-w^{-n})
                  =2-w^n-w^{-n}.}
 \tag{5}
\]

The convolution itself is the explicit real function

\[
 h_n(x)=e^x\int_{\max(0,x)}^\infty e^{-y}
 L_{n-1}^{(1)}(y)L_{n-1}^{(1)}(y-x)\,dy,
 \tag{6}
\]

and satisfies $h_n(x)=e^xh_n(-x)$.  Equivalently, with

\[
 g_n(x)=e^{-x/2}f_n(x),\qquad k_n(x)=e^{-x/2}h_n(x),
\]

one has the ordinary autocorrelation

\[
 k_n=g_n*\widetilde g_n,
 \qquad \widetilde g_n(x)=g_n(-x).
 \tag{7}
\]

Let

\[
 \mathcal W(h)=\sum_\rho \mathcal Lh(\rho)
\]

denote the zero side of the Weil explicit formula, with multiplicities.
For (5) the sum is absolutely convergent: each summand is
$O_n(|\rho|^{-2})$.  The functional equation permutes the zeros by
$\rho\mapsto1-\rho$, hence it permutes $w\mapsto w^{-1}$.  Therefore

\[
\begin{aligned}
 \mathcal W(h_n)
 &=\sum_\rho\{2-w_\rho^n-w_\rho^{-n}\}\\
 &=2\sum_\rho^*\{1-w_\rho^n\}
 =2\lambda_n.
\end{aligned}
\tag{8}
\]

Thus the direct strong margin has the unconditional completed identity

\[
 \boxed{D_n=\mathcal W(f_n*f_n^\#)-A_n.}
 \tag{9}
\]

This coupling is made at the completed Weil level, before any Euler or
Laguerre pullback.  It is not the phase-averaged square of the von
Mangoldt series.

## Sign audit

On the critical line, $1-s=\bar s$, so (4) becomes

\[
 \mathcal Lh_n(1/2+it)=|F_n(1/2+it)|^2\geq0.
 \tag{10}
\]

Away from the line, (5) is a reciprocal product, not a modulus square.
For a noncritical quartet with
$w=e^{-a+i\theta}$, $a>0$, its total contribution to (8) is

\[
 8-8\cosh(na)\cos(n\theta),
 \tag{11}
\]

which has both signs.  Consequently positivity of the Weil functional on
the autocorrelations (7) is precisely the missing zero-location input; the
word ``autocorrelation'' does not make (8) positive unconditionally.
Moreover $A_n>0$ for $n\geq8$, so the correction in (9) is
$-A_n<0$, not an elementary positive remainder.

## Divisor inversion does not preserve the square

The natural primitive exponents are

\[
 q_n={1\over n}\sum_{d\mid n}\mu(n/d)D_d,
 \qquad D_n=\sum_{d\mid n}d q_d,
 \tag{12}
\]

equivalently

\[
 \exp\!\left(\sum_{n\geq1}{D_n\over n}z^n\right)
 =\prod_{m\geq1}(1-z^m)^{-q_m}.
 \tag{13}
\]

The zero-side test produced by (12) has, on the critical line
$w=e^{i\theta}$, the spectral value

\[
 \Psi_n(\theta)
 ={1\over n}\sum_{d\mid n}\mu(n/d)|1-e^{id\theta}|^2.
 \tag{14}
\]

Already

\[
 \Psi_2(\theta)
 ={1\over2}\bigl(|1-e^{2i\theta}|^2-|1-e^{i\theta}|^2\bigr)
 \tag{15}
\]

has both signs:

\[
 \Psi_2(\pi/3)=1,
 \qquad \Psi_2(\pi)=-2.
 \tag{16}
\]

Hence the Möbius-inverted test is not an autocorrelation, nor a positive
sum of autocorrelations.  Equations (9)--(11) give the exact square supplied
by this construction; they do not prove $D_n\geq0$ or RH.
