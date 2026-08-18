# 106.16 — Local logarithmic prime--Gamma scale and the center-loss gate

## Purpose

The absolute norm of the finite prime block in the semilocal Weil operator
is \(O(\lambda)\). Combined with Gamma coercivity, this gives only an
\(O(Le^{C\lambda})\) upper bound for the negative index. The branch gate in
106.15 needs an effective logarithmic prime scale.

This note proves that the desired \(O(\log\lambda)\) scale is indeed
available on each Fourier block of the natural target width. It also proves
why this fact does not globalize: the estimate is uniform in the block
center and hence cannot exclude even one negative well.

Put

\[
 N=\lambda^2=e^L,
 \qquad
 D_N(t)=\sum_{n\le N}\frac{\Lambda(n)}{\sqrt n}\,n^{-it}.
 \tag{1}
\]

Up to the sign fixed by the explicit formula, \(2\operatorname {Re}D_N\)
is the Fourier multiplier of the finite prime-power translation block.

## 1. Uniform translated mean square

### Theorem 1 — Local prime RMS bound

Uniformly for \(U\in\mathbb R\) and \(T\ge1\),

\[
 \boxed{
 \int_{U-T}^{U+T}|D_N(t)|^2\,dt
 \le C\bigl(TL^2+NL\bigr).}
 \tag{2}
\]

Consequently, at the target width

\[
 T=N/L,
 \tag{3}
\]

one has

\[
 \boxed{
 \left(\frac1{2T}\int_{U-T}^{U+T}|D_N(t)|^2dt\right)^{1/2}
 \le C L.}
 \tag{4}
\]

#### Proof

The translated Montgomery--Vaughan form of the generalized Hilbert
inequality gives, for \(a_n=\Lambda(n)n^{-1/2-iU}\),

\[
 \int_{-T}^{T}\left|\sum_{n\le N}a_nn^{-it}\right|^2dt
 \le C\left(
 T\sum_{n\le N}|a_n|^2+
 \sum_{n\le N}n|a_n|^2\right).
 \tag{5}
\]

The phase \(n^{-iU}\) changes neither sum. Partial summation and the
elementary Chebyshev bounds give

\[
 \sum_{n\le N}\frac{\Lambda(n)^2}{n}=O(L^2),
 \qquad
 \sum_{n\le N}\Lambda(n)^2=O(NL).
 \tag{6}
\]

Substitution proves (2). With (3), both terms on the right of (2) are
\(O(NL)\), and division by \(2N/L\) proves (4). \(\square\)

The second term in (5) is \(O(NL)\), not the absolute square
\(O(N^2)\). This is the exact cancellation that lowers the local prime
scale from \(\lambda\) to \(L=2\log\lambda\).

## 2. Local negative-mode budget

Let \(I_L\) be the additive interval of length \(L\), and let
\((v_j)_{j=1}^d\) be orthonormal in \(L^2(I_L)\), extended by zero. With
the Fourier convention used in Phase 106, Bessel's inequality gives

\[
 \rho(t):=\sum_{j=1}^d|\widehat v_j(t)|^2\le L.
 \tag{7}
\]

Let \(B\) be a Fourier block of length comparable to \(N/L\). Equations
(2), (7), Cauchy--Schwarz and \(|B|\asymp N/L\) give

\[
\begin{aligned}
 \sum_{j=1}^d\int_B
 (2\operatorname {Re}D_N(t))_+
 |\widehat v_j(t)|^2\frac{dt}{2\pi}
 &\le\frac L\pi\int_B|D_N(t)|dt\\
 &\le C L N.
\end{aligned}
 \tag{8}
\]

On blocks with \(|t|\asymp N/L\), the Riemann--Siegel/Gamma multiplier is
bounded below by \(cL\). Therefore, if every \(v_j\) has at least \(\eta\)
of its Fourier mass in \(B\) and has negative prime--Gamma form when
restricted to that block, (8) implies

\[
 \boxed{d\le C N/\eta=C\lambda^2/\eta.}
 \tag{9}
\]

Thus the \(O(\lambda^2)\) Slepian dimension is the correct local budget.
This is a real improvement over the absolute \(O(\lambda)\) operator norm.

## 3. Why the estimate does not select the global branch

The estimate (2) is invariant under translation of the Fourier center.
The absolute prime norm confines a possible negative space only to

\[
 |t|\le H_\lambda:=e^{C\lambda}.
 \tag{10}
\]

There are \(\asymp H_\lambda L/N\) target-width blocks in this interval.
Summing the local allowance (9) therefore recovers, up to polynomial
factors,

\[
 \dim\mathcal N_L=O(Le^{C\lambda}),
 \tag{11}
\]

which is the bound already obtained from Gamma coercivity. The increasing
Gamma threshold improves the allowance in a far block only by a logarithmic
factor and does not remove the exponential number of possible centers.

More decisively, (2) is compatible with a single negative well. Hence it
cannot prove

\[
 \beta_L=inf_{g\perp q_L,\ \|g\|=1}QW_L(g,g)>0,
 \tag{12}
\]

which is required by the branch gate.

### Proposition 2 — Center-information falsifier

Replace the coefficients in (1) by

\[
 a_n^{(\tau)}=\frac{\Lambda(n)}{\sqrt n}n^{i\tau}.
 \tag{13}
\]

Then

\[
 D_N^{(\tau)}(t)=D_N(t-\tau),
 \tag{14}
\]

so every estimate (2)--(4) is unchanged, while the coherent prime peak is
moved from zero to \(t=\tau\). At its center,

\[
 D_N^{(\tau)}(\tau)
 =\sum_{n\le N}\frac{\Lambda(n)}{\sqrt n}
 \asymp2\lambda.
 \tag{15}
\]

It remains of order \(\lambda\) on a window of width \(c/L\). For
\(\log(2+|\tau|)<c'\lambda\), this peak exceeds the Gamma multiplier on
that window. A time-limited wave packet on \(I_L\) resolves precisely this
width. Thus translated mean-square data alone cannot distinguish the
ordinary-prime phase from a coefficient system with a negative well at an
arbitrary center.

#### Proof

Equations (14)--(15) are immediate. If
\(|t-\tau|\le c/L\), then
\(|(t-\tau)\log n|\le c\) for every \(n\le N\); choosing \(c\) small
keeps the real part of every summand positive. The Gamma multiplier is
\(O(\log(2+|\tau|))\), proving the comparison. The uncertainty width of an
interval of length \(L\) is \(1/L\), so a standard first prolate packet
has a fixed positive fraction of its Fourier mass in this well. \(\square\)

The twisted system is a methodological falsifier, not the ordinary-prime
system. It proves that the magnitude information in Theorem 1 cannot by
itself select the branch. The untwisted phases and the polar term must enter
through an additional signed identity.

## 4. Verdict

The logarithmic effective scale requested by 106.14 is now proved on every
individual target-width Fourier block. What remains open is not the local
size but the global location and sign:

\[
 \boxed{
 \text{exclude every negative Fourier well using the actual phases of }
 \Lambda(n),\ \Gamma,\text{ and the polar block jointly}.}
 \tag{16}
\]

This is exactly Gate SPG of 106.15. The local large-sieve theorem does not
prove that gate or RH, but it identifies the lost variable: the block
center.
