# D.151 — Superfactorial control of the two Tate defect directions

## Verdict

The rank-two sector isolated in D.149 is not merely finite-dimensional.  At
the \(170\)-mode endpoint it is quantitatively almost orthogonal to the low
Legendre space.  If

\[
 y=u+q\in\mathcal P_T\cap V_N^\perp,qquad
 u\in L_N,quad q\in L_N^\perp,
\]

then \(u\) belongs to the two-dimensional truncated Tate plane and

\[
 \boxed{\|u\|\le\eta_N\|q\|.}                          \tag{0.1}
\]

At \(T=\frac12\log5\), the directed Bessel bound proves

\[
 \boxed{\eta_{170}<10^{-424}.}                         \tag{0.2}
\]

Thus the rank-two defect cannot be discarded, but its contribution can be
absorbed by any explicit bound below \(10^{424}\) for the completed
operator on the truncated Tate plane.  The remaining substantial endpoint
obligation is the Feshbach residual from the \(168\)-dimensional primitive
block, not the two moment tails.

This estimate is independent of any sign of \(B_{\rm nuc}\).  The paper is
not modified.

## 1. Exact Legendre coefficients of the Tate vectors

Let

\[
 h_\pm(t)=e^{\pm t/2},\qquad
 \phi_n(t)=\sqrt{{2n+1\over2T}}P_n(t/T),qquad
 k={T\over2}.                                          \tag{1.1}
\]

The standard exponential--Legendre integral gives

\[
 g_n:=|\langle h_+,\phi_n\rangle|
 =\sqrt{2T(2n+1)}\,i_n(k),                             \tag{1.2}
\]

where \(i_n\) is the modified spherical Bessel function.  Reflection gives

\[
 \langle h_-,\phi_n\rangle=(-1)^n\langle h_+,\phi_n\rangle.          \tag{1.3}
\]

Let \(M_Q=M|_{L_N^\perp}\).  Its two-by-two Gram matrix is

\[
 M_QM_Q^*=\begin{pmatrix}a_N&b_N\\b_N&a_N\end{pmatrix},qquad
 a_N=\sum_{n\ge N}g_n^2,quad
 b_N=\sum_{n\ge N}(-1)^ng_n^2.                        \tag{1.4}
\]

Consequently

\[
 \|M_Q\|^2\le2a_N.                                    \tag{1.5}
\]

## 2. Graph estimate for the primitive complement

Put \(J_N=M|_{L_N}\).  On
\(U_N=(\ker J_N)^\perp\subset L_N\), the map \(J_N\) is injective and

\[
 \sigma_{\min}(J_N|_{U_N})^2
 =\lambda_{\min}(J_NJ_N^*).                            \tag{2.1}
\]

Because \(MM^*=\mathsf G_T\) and
\(J_NJ_N^*=\mathsf G_T-M_QM_Q^*\),

\[
 \lambda_{\min}(J_NJ_N^*)
 \ge2(\sinh T-T)-2a_N.                                \tag{2.2}
\]

If \(y=u+q\in\mathcal P_T\cap V_N^\perp\), orthogonality to
\(V_N=L_N\cap\ker M\) forces \(u\in U_N\).  Primitivity gives

\[
 J_Nu=-M_Qq.                                           \tag{2.3}
\]

Equations (1.5), (2.1)--(2.3) prove (0.1) with

\[
 \eta_N^2\le{2a_N\over2(\sinh T-T)-2a_N}.             \tag{2.4}
\]

## 3. Directed superfactorial tail

The positive Bessel series implies

\[
 i_n(k)\le {k^n\over(2n+1)!!}
 \exp\left({k^2\over2(2n+3)}\right).                  \tag{3.1}
\]

Indeed the ratio of the \((j+1)\)-st term to the \(j\)-th term in the
series for \(I_{n+1/2}(k)\) is at most
\(k^2/[4(j+1)(n+3/2)]\), and comparison with the exponential series gives
(3.1).

Let the right side of (1.2), with (3.1) substituted, be \(A_n\).  For
\(n\ge N\),

\[
 {A_{n+1}\over A_n}
 \le {k\over2n+3}\sqrt{{2n+3\over2n+1}}=:r_N.         \tag{3.2}
\]

The exponential correction in (3.1) decreases with \(n\), so it contributes
no factor larger than one to (3.2).  Therefore

\[
 a_N\le\sum_{n\ge N}A_n^2\le {A_N^2\over1-r_N^2}.     \tag{3.3}
\]

Every quantity in (3.3) is an elementary expression in \(\log5\), integer
factorials and exponentials.  Arb evaluation at 1000 decimal digits gives

\[
 \log_{10}g_{170}<-425.05,qquad
 \log_{10}a_{170}<-850.10,qquad
 \log_{10}\eta_{170}<-424.52,                         \tag{3.4}
\]

which proves the rounded assertion (0.2).

## 4. Absorbing the defect in the complement gap

Let \(A_T\) be the completed multiplier operator, and suppose the
Legendre-complement estimate is

\[
 \langle A_Tq,q\rangle\ge\delta\|q\|^2
 \quad(q\in L_N^\perp).                               \tag{4.1}
\]

If

\[
 \|A_Tu\|\le C_N\|u\|\quad(u\in U_N),qquad
 \langle A_Tu,u\rangle\ge-M\|u\|^2,                  \tag{4.2}
\]

then (0.1) and Cauchy--Schwarz give

\[
 \langle A_Ty,y\rangle
 \ge(\delta-2C_N\eta_N-M\eta_N^2)\|q\|^2.           \tag{4.3}
\]

Moreover \(\|y\|^2\le(1+\eta_N^2)\|q\|^2\).  Hence a
directed bound \(C_{170}<10^{423}\), enormously weaker than the actual
size, already preserves a positive complement gap.  Formula D.150 supplies
a direct way to enclose \(C_N\).

