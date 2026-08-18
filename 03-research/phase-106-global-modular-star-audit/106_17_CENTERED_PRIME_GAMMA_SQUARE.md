# 106.17 — The centered prime--Gamma square and the exact branch reduction

> **Binding parity correction (106.23).**  The rank-one reduction below is
> exact in the inversion-even sector.  The unsymmetrized moving co-Poisson
> vector of 106.12 is not automatically inversion-even.  In Section 5 it
> must therefore be replaced by its explicit even radical projection
> \(q_L^+\).  On the full space the polar block is rank two:
> \(2|c_L\rangle\langle c_L|-2|s_L\rangle\langle s_L|\).

## Purpose

Document 106.16 reached the correct logarithmic size for the ordinary-prime
Dirichlet polynomial on each translated Fourier block, but its
Montgomery--Vaughan estimate was invariant under an arbitrary translation of
the block center.  This note restores the missing center by retaining the
actual phases of all prime powers and the Gamma factor before taking an
estimate.

The result is an exact positive jump-form decomposition of the full CCM
semilocal Weil form.  It has three consequences.

1. The ordinary-prime--Gamma multiplier has a unique global minimum at the
   fundamental Fourier center \(t=0\).
2. The phase-twist falsifier of 106.16 cannot satisfy the exact identity.
3. In the even sector, the entire signed branch problem becomes a
   rank-one spectral comparison for one explicit positive operator.

The decomposition proves the global centering and the complete square.  It
does not prove the remaining spectral comparison and therefore does not
prove Gate SPG or RH.

## 1. Conventions

Let

\[
 I_L=[-L/2,L/2],\qquad N=e^L=\lambda^2,
 \tag{1}
\]

and extend every \(F\in L^2(I_L)\) by zero to the full additive line.  Use

\[
 \widehat F(t)=\int_{\mathbb R}F(x)e^{-itx}\,dx,
 \qquad
 \|F\|_2^2=\int_{\mathbb R}|\widehat F(t)|^2\,\frac{dt}{2\pi}.
 \tag{2}
\]

Write

\[
 w_n=\frac{\Lambda(n)}{\sqrt n},\qquad a_n=\log n,
 \qquad
 (\tau_aF)(x)=F(x-a).
 \tag{3}
\]

The translation in (3) is translation on the full line after zero
extension.  It is not periodic translation on \(I_L\).

Let

\[
 \theta(t)
 =\operatorname {Im}\log\Gamma\!\left(\frac14+\frac{it}{2}\right)
   -\frac t2\log\pi .
 \tag{4}
\]

The CCM form has the exact diagonal representation

\[
\begin{aligned}
 Q_L(F,F)
 &=
 \int_{\mathbb R}|\widehat F(t)|^2
 \left(
  2\theta'(t)-2\sum_{2\le n\le N}w_n\cos(ta_n)
 \right)\frac{dt}{2\pi}\\
 &\quad
 +2\operatorname {Re}\!\left(
   \widehat F(i/2)\overline{\widehat F(-i/2)}
 \right).
\end{aligned}
\tag{5}
\]

Formula (5) keeps primes, all prime powers, Gamma and the two polar
evaluations in their source normalization.

## 2. The positive jump form

Define the sesquilinear form, initially on \(C_c^\infty(I_L)\), by

\[
\begin{aligned}
 \mathcal D_N(F,G)
 &:=
 \sum_{2\le n\le N}w_n
 \langle F-\tau_{a_n}F,G-\tau_{a_n}G\rangle\\
 &\quad+
 \sum_{k=0}^{\infty}\int_0^\infty
 e^{-2(k+1/4)x}
 \langle F-\tau_xF,G-\tau_xG\rangle\,dx .
\end{aligned}
\tag{6}
\]

Every coefficient and measure in (6) is nonnegative.

### Theorem 1 — Exact centered prime--Gamma square

Put

\[
 \kappa_N
 :=
 2\sum_{2\le n\le N}\frac{\Lambda(n)}{\sqrt n}
 -2\theta'(0).
\tag{7}
\]

Then

\[
\boxed{
\begin{aligned}
 Q_L(F,F)
 &=
 \mathcal D_N(F,F)-\kappa_N\|F\|_2^2\\
 &\quad+
 2\operatorname {Re}\!\left(
 \widehat F(i/2)\overline{\widehat F(-i/2)}
 \right).
\end{aligned}}
\tag{8}
\]

Moreover,

\[
\boxed{
\kappa_N=
2\sum_{n\le N}\frac{\Lambda(n)}{\sqrt n}
+\gamma+\frac{\pi}{2}+3\log2+\log\pi
=4\lambda+o(\lambda).}
\tag{9}
\]

#### Proof

For \(a>0\), Plancherel gives

\[
 \|F-\tau_aF\|_2^2
 =
 2\int_{\mathbb R}(1-\cos(at))
 |\widehat F(t)|^2\frac{dt}{2\pi}.
\tag{10}
\]

Let \(b_k=k+1/4\).  The digamma expansion gives

\[
\begin{aligned}
 2\bigl(\theta'(t)-\theta'(0)\bigr)
 &=
 \sum_{k=0}^{\infty}
 \frac{(t/2)^2}
 {b_k\bigl(b_k^2+(t/2)^2\bigr)}\\
 &=
 \sum_{k=0}^{\infty}
 2\int_0^\infty e^{-2b_kx}(1-\cos(tx))\,dx .
\end{aligned}
\tag{11}
\]

Applying (10) to both lines of (6), its Fourier multiplier is

\[
 2\sum_{n\le N}w_n(1-\cos(ta_n))
 +2\bigl(\theta'(t)-\theta'(0)\bigr).
\tag{12}
\]

Subtracting \(\kappa_N\) leaves

\[
 2\theta'(t)-2\sum_{n\le N}w_n\cos(ta_n),
\tag{13}
\]

which is the first line of (5).  This proves (8).

The special value

\[
 \psi(1/4)=-\gamma-\frac{\pi}{2}-3\log2
\tag{14}
\]

and \(2\theta'(0)=\psi(1/4)-\log\pi\) prove the exact expression in
(9).  Finally, partial summation and the prime number theorem give

\[
 \sum_{n\le N}\frac{\Lambda(n)}{\sqrt n}
 =2\sqrt N+o(\sqrt N)=2\lambda+o(\lambda).
\tag{15}
\]

This proves the asymptotic statement. \(\square\)

### Corollary 2 — The fundamental Fourier center is unique

Let

\[
 m_N(t)=2\theta'(t)
 -2\sum_{n\le N}\frac{\Lambda(n)}{\sqrt n}\cos(t\log n).
\tag{16}
\]

Then

\[
\boxed{
 m_N(t)-m_N(0)
 =
 2\sum_{n\le N}\frac{\Lambda(n)}{\sqrt n}
   \bigl(1-\cos(t\log n)\bigr)
 +2\bigl(\theta'(t)-\theta'(0)\bigr)\ge0.}
\tag{17}
\]

The inequality is strict for \(t\ne0\).

#### Proof

Every term on the right of (17) is nonnegative.  The Gamma series (11) is
strictly positive when \(t\ne0\). \(\square\)

Thus the actual von Mangoldt phases and Gamma factor select \(t=0\)
exactly.  A coefficient twist \(w_n\mapsto w_nn^{i\tau}\) moves the prime
well but does not move the Gamma minimum, so it no longer preserves (17).
This is the precise information absent from the mean-square estimate of
106.16.

## 3. Pure-gauge form of the multiplier

Define

\[
 \phi_N(t)
 =
 \theta(t)
 -\sum_{n\le N}
 \frac{\Lambda(n)}{\sqrt n\log n}\sin(t\log n),
 \qquad
 U_N=e^{i\phi_N},
 \tag{18}
\]

and let \(\mathsf X=-i\,d/dt\).  On the standard smooth core,

\[
\boxed{
 2\bigl(U_N^*\mathsf XU_N-\mathsf X\bigr)=M_{m_N}.}
\tag{19}
\]

Indeed \(U_N^*\mathsf XU_N-\mathsf X\) is multiplication by
\(\phi_N'\), and \(2\phi_N'=m_N\).  Equation (19) is an identity, not a
positivity theorem: the gauge has nontrivial boundary and polar coupling
on the finite interval.

## 4. Exact even-sector reduction

If \(F\) is even, then

\[
 \widehat F(i/2)=\widehat F(-i/2)
 =\langle h_L,F\rangle,
 \qquad
 h_L(x)=\mathbf1_{I_L}(x)\cosh(x/2).
\tag{20}
\]

Therefore (8) polarizes to

\[
\boxed{
 Q_L^+(F,G)
 =
 \mathcal D_N(F,G)-\kappa_N\langle F,G\rangle
 +2\overline{\langle h_L,F\rangle}\langle h_L,G\rangle.}
\tag{21}
\]

Let \(\mathcal L_N^+\) be the positive operator associated with the closed
form

\[
 \ell_N^+(F,G)
 =
 \mathcal D_N(F,G)
 +2\overline{\langle h_L,F\rangle}\langle h_L,G\rangle .
\tag{22}
\]

Then, as closed forms,

\[
\boxed{A_L^+=\mathcal L_N^+-\kappa_NI,\qquad \mathcal L_N^+\ge0.}
\tag{23}
\]

This is the exact signed prime--Gamma--pole decomposition.  All negative
spectral information of the even Weil operator is now equivalent to the
position of the positive spectrum of \(\mathcal L_N^+\) relative to the
explicit threshold \(\kappa_N\).

## 5. Gate SPG in the positive coordinate

Let \(q_L^+\) be the normalized inversion-even radical projection of the
moving co-Poisson vector, as constructed in 106.23, and let \(d_4,d_8\) be
the first two constrained prolate leakage levels.  Since the scalar term in
(23) vanishes in cross terms with \(g\perp q_L^+\), the even Gate SPG is
exactly the following pair of estimates:

\[
\boxed{
\sup_{\substack{g\perp q_L^+\\g\ {\rm even}\\\|g\|=1}}
\left|
\mathcal D_N(q_L^+,g)
+2\overline{\langle h_L,q_L^+\rangle}\langle h_L,g\rangle
\right|
=o(\lambda^{-\sigma}d_8),
\quad \sigma<\frac12,}
\tag{24}
\]

and

\[
\boxed{
\inf_{\substack{g\perp q_L^+\\g\ {\rm even}\\\|g\|=1}}
\left(
\mathcal D_N(g,g)+2|\langle h_L,g\rangle|^2
\right)
\ge\kappa_N+c\,d_8.}
\tag{25}
\]

The original sufficient estimate \(r_L^{\mathrm{mov}}=O(d_4)\) would give

\[
 \ell_N^+(q_L^+,q_L^+)=\kappa_N+O(d_4).
\tag{26}
\]

It is not minimal.  By 106.23 it is enough to have
\(|r_L^{\mathrm{mov}}|=O(\lambda^{p_R}d_4)\) for any fixed \(p_R<8\),
with the corresponding polynomial loss in (26).

Thus (24)--(26), taken together, say that \(q_L^+\) is a first-level
quasimode of the explicit positive operator \(\mathcal L_N^+\), to form-dual accuracy
\(o(\lambda^{-\sigma}d_8)\), and that its next level lies at least
\(c\,d_8\) above the threshold.

### Rank-one resolvent form

For qualitative nonnegativity there is a still narrower conditional
criterion.  Assume

\[
 \lambda_1(\mathcal D_N)<\kappa_N<\lambda_2(\mathcal D_N).
\]

This one-negative-level inertia hypothesis is itself unproved and
force-bearing.  Rank-one inertia then gives

\[
 Q_L^+\ge0
 \quad\Longleftrightarrow\quad
 1+2\langle h_L,(\mathcal D_N-\kappa_N)^{-1}h_L\rangle\le0.
\tag{27}
\]

At finite Galerkin level the scalar in (27) is exactly the determinant
ratio

\[
 \frac{\det(\mathcal L_N^+-z)}
 {\det(\mathcal D_N-z)}
 =
 1+2\langle h_L,(\mathcal D_N-z)^{-1}h_L\rangle.
\tag{28}
\]

The closed Gamma jump form has compact resolvent on the finite interval.
Under the displayed strict inertia hypothesis,
\(\mathcal D_N-\kappa_NI\) is boundedly invertible, so the
infinite-dimensional version of (27) follows directly from the rank-one
inertia theorem; no limiting determinant is required.  This formulation
makes the final sign explicit: constructing the positive square is not
enough; one must place the scalar threshold \(\kappa_N\) on the correct
side of the rank-one Herglotz function.  Criterion (27) concerns only
\(Q_L^+\ge0\); it does not imply the quantitative \(d_8\) gap and
form-dual residual required in (24)--(25).

## 6. Domain and boundary warning

The Gamma measure in (6) behaves like \(dx/(2x)\) near zero.  Define the CCM
logarithmic Gamma-form domain as the completion of \(C_c^\infty(I_L)\)
under the norm

\[
 \|F\|_2^2+
 \int_{\mathbb R}\log(2+|t|)|\widehat F(t)|^2\,dt.
\]

Then \(\mathcal D_N\) extends by closure to that domain.  It is not a
bounded form on all of \(L^2(I_L)\).

Zero extension is essential.  When \(a\) is comparable with \(L\),
\(\|F-\tau_aF\|_2^2\) contains the boundary loss.  Replacing \(\tau_a\) by
periodic translation removes that loss and produces a false identity.

## 7. Verdict

The missing Fourier center is now selected exactly, and the complete
ordinary-prime--Gamma block is a positive jump square.  After adding the
even polar channel, the signed branch problem is no longer an unspecified
global cancellation: it is the explicit rank-one spectral comparison
(24)--(25) for \(\mathcal L_N^+\).

Those two quantitative inequalities are not consequences of
\(\mathcal L_N^+\ge0\).  They remain the force-bearing part of Gate SPG.
No assertion in this note proves them or RH.
