# Completed Mellin-law factorization

## Exact identity

Put

\[
 H(s)=\pi^{-s/2}\Gamma(s/2)\{(s-1)\zeta(s)\}^2,
 \qquad s=1+t={1\over1-z},
 \tag{1}
\]

so that \(H(1)=1\).  Let \(a=\log 2\), and introduce four independent
random variables:

\[
 \begin{array}{ll}
 X\sim {\rm Exp}(1),&V\sim {\rm Unif}[0,a],\\[2mm]
 {\displaystyle
  \mathbb P(U\in du)={1\over a}e^{-u}
  \mathbf1_{\{\lfloor e^u\rfloor\ {\rm odd}\}}\,du,}
 &G\sim {\rm Gamma}(1/2,1),\quad
 W=-{1\over2}\log(G/\pi).
 \end{array}
 \tag{2}
\]

The density defining \(U\) has mass one because

\[
 \int_0^\infty e^{-u}
 \mathbf1_{\{\lfloor e^u\rfloor\ {\rm odd}\}}\,du
 =\sum_{k\geq1}\left({1\over2k-1}-{1\over2k}\right)=a.
 \tag{3}
\]

Writing \(L_Y(t)=\mathbb E e^{-tY}\), direct integration gives

\[
 L_U(t)={\eta(1+t)\over a(1+t)},\qquad
 L_V(t)={1-e^{-at}\over at},\qquad
 L_X(t)={1\over1+t},
 \tag{4}
\]

and

\[
 L_W(t)=\pi^{-t/2}{\Gamma((1+t)/2)\over\Gamma(1/2)}.
 \tag{5}
\]

Since

\[
 {L_U(t)\over L_V(t)L_X(t)}
 ={t\eta(1+t)\over1-2^{-t}}
 =t\zeta(1+t),
 \tag{6}
\]

we obtain the completed factorization

\[
 \boxed{
 {H(1+t)\over H(1)}
 =L_W(t)\left\{{L_U(t)\over L_V(t)L_X(t)}\right\}^{\!2}.}
 \tag{7}
\]

In particular, if \(U_1,U_2,V_1,V_2,X_1,X_2,X_3\) are independent copies
and

\[
 A=W+U_1+U_2,\qquad
 B=V_1+V_2+X_1+X_2+X_3,
 \tag{8}
\]

then

\[
 \boxed{
 K(t):=(1+t){H(1+t)\over H(1)}={L_A(t)\over L_B(t)}.}
 \tag{9}
\]

This identity pairs the pole, the alternating Euler factor, and the Gamma
factor before any limit is taken.

## Direct strong-margin coefficients

The completed first-difference generator is

\[
 G(z)=1+s\,{d\over ds}\log H(s).
 \tag{10}
\]

Since multiplication by \(s=(1-z)^{-1}\) accumulates first differences,

\[
 \sum_{n\geq1}D_nz^{n-1}
 =sG(z)=s+{d\over dz}\log H(s).
 \tag{11}
\]

Consequently the cumulative target, which does not require the first
differences to keep one sign, is exactly

\[
 \boxed{
 D_n=n[z^n]\log K\!\left({z\over1-z}\right).}
 \tag{12}
\]

Equations (9)--(12) are an Abel-exact cumulant formulation of A1 involving
only the four explicit laws in (2).

## Deconvolution check

The elementary positive-law deconvolutions of (9) do not exist.  Indeed,

\[
 (\log K)'(0)
 =1+{3\gamma\over2}-{1\over2}\log(4\pi)=D_1>0,
 \tag{13}
\]

whereas a Laplace transform of a nonnegative variable is nonincreasing.
Moreover

\[
 (\log K)''(0)
 =-1+{\pi^2\over8}-4\gamma_1-2\gamma^2<0.
 \tag{14}
\]

The coarse rational enclosures already used by the finite verifiers,

\[
 \gamma>0.577,\qquad -0.073<\gamma_1,\qquad \pi^2<9.870,
 \tag{15}
\]

put the right side of (14) below \(-0.140\).  Thus \(K\) is not an mgf,
since logarithms of mgfs are convex.  The reciprocal \(K^{-1}\) is not the
mgf of a nonnegative variable because its derivative at zero is negative.
A representation \(K^{-1}=L_Y\), \(Y\geq0\), would instead imply the
independent convolution \(B\overset d=A+Y\); this is impossible because
\(B\geq0\), while \(A\) has support unbounded below.

The still smaller reciprocal factor
\(\{t\zeta(1+t)\}^{-1}\) also fails positivity directly: its unique inverse
Laplace density is
\(\sum_{n\leq e^u}\mu(n)/n\), and the exact first obstruction is

\[
 \sum_{n\leq13}{\mu(n)\over n}=-{2323\over30030}<0.
 \tag{16}
\]

Thus (7) is a genuine completed probabilistic factorization, but not a
hidden positive deconvolution.
