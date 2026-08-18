# 106.35 — Lemma B: definition and scale gate

## Purpose

Paper 40 proposes the separate estimate

\[
 \mathfrak W_L(g,g)\ge -c_1d_8\|g\|_2^2,
 \qquad g\perp q_L^+,
 \tag{1}
\]

where \(\mathfrak W_L\) is described as the Gamma, pole, scalar-threshold
and zero-extension remainder after extracting and shorting a divisor
covariance.  This note reconstructs that remainder from the exact
prime--Gamma square and tests (1) before attempting an estimate.

There are two conclusions.

1. The divisor covariance introduced in Paper 40 is not connected to the
   original prime jump form by an exact identity.  Its Fourier symbol and
   scale are different.
2. Under the literal interpretation of the components listed in Lemma B,
   (1) is false: on a fixed compact even core its bottom is
   \(-\kappa_N+O(1)=-4\lambda+o(\lambda)\), not \(-O(d_8)\).

Thus Lemma B cannot be proved in its present form.  The valid successor is
a **joint** shorted inequality for the complete prime--Gamma--pole form;
the archimedean--polar part cannot be separated at the \(d_8\) scale.

## 1. Exact finite operator

Use

\[
 I_L=[-L/2,L/2],\qquad N=e^L=\lambda^2,
 \tag{2}
\]

and extend functions by zero to the additive line.  The exact even-sector
identity proved in 106.17 is

\[
 \boxed{
 A_L^+
 =\mathcal D_{p,N}+\mathcal D_\Gamma
  -\kappa_NI+2|h_L\rangle\langle h_L|,}
 \tag{3}
\]

where

\[
 \begin{aligned}
 \mathcal D_{p,N}(g,g)
 &=\sum_{n\le N}\frac{\Lambda(n)}{\sqrt n}
   \|g-\tau_{\log n}g\|_2^2,\\
 \mathcal D_\Gamma(g,g)
 &=\int_0^\infty
   \frac{e^{-u/2}}{1-e^{-2u}}
   \|g-\tau_ug\|_2^2\,du,\\
 h_L(x)&={\bf1}_{I_L}(x)\cosh(x/2),
 \end{aligned}
 \tag{4}
\]

and

\[
 \boxed{
 \kappa_N
 =2\sum_{n\le N}\frac{\Lambda(n)}{\sqrt n}
  +\gamma+\frac\pi2+3\log2+\log\pi
 =4\lambda+o(\lambda).}
 \tag{5}
\]

The zero-extension boundary is already present in every translation norm
in (4); it is not a separate unspecified quadratic form.

## 2. The divisor covariance is not an extraction of the prime jump

Paper 40 defines, for every \(\ell\le N\),

\[
 p_\ell(d)=\frac{\Lambda(d)}{\log\ell}\qquad(d\mid\ell)
 \tag{6}
\]

and the covariance

\[
 \mathcal V_L(g,g)
 =\sum_{\ell\le N}\log\ell
 \left(
  \sum_{d\mid\ell}p_\ell(d)\|\tau_{\log d}g\|_2^2
  -\left\|\sum_{d\mid\ell}p_\ell(d)
                   \tau_{\log d}g\right\|_2^2
 \right).
 \tag{7}
\]

The identity \(\sum_{d\mid\ell}\Lambda(d)=\log\ell\) proves that each
summand is a variance.  It does **not** identify the sum (7) with
\(\mathcal D_{p,N}\), or with a subform of it.

### Proposition 1 — Fourier-symbol mismatch

On an additive Fourier mode, the bulk symbol of (7) is

\[
 v_N(t)=\sum_{\ell\le N}\log\ell
 \left(
 1-\left|
 \sum_{d\mid\ell}\frac{\Lambda(d)}{\log\ell}d^{-it}
 \right|^2
 \right),
\tag{8}
\]
The bracket is nonnegative because the inner sum is the characteristic
function of the probability law \(p_\ell\).  The prime-jump symbol from
(4) is

\[
 p_N(t)=2\sum_{n\le N}\frac{\Lambda(n)}{\sqrt n}
       \bigl(1-\cos(t\log n)\bigr).
 \tag{9}
\]

These symbols are not equal, even up to an \(L\)-dependent scalar.
Indeed,

\[
 \begin{aligned}
 v_N''(0)
 &=2\sum_{\ell\le N}\log\ell\,
   \mathrm{Var}_{p_\ell}(\log d),\\
 p_N''(0)
 &=2\sum_{n\le N}\frac{\Lambda(n)}{\sqrt n}(\log n)^2.
 \end{aligned}
 \tag{10}
\]

The terms \(\ell=2p\), with \(N/4<p\le N/2\) prime, already give

\[
 v_N''(0)\gg N\log N,
 \tag{11}
\]

whereas partial summation and the prime number theorem give

\[
 p_N''(0)\asymp\sqrt N(\log N)^2.
 \tag{12}
\]

#### Proof

For a probability law \(P\) and \(X=\log d\),

\[
 1-|\mathbb E_Pe^{-itX}|^2
 =t^2\mathrm{Var}_P(X)+O(t^3),
\]

which gives (10).  If \(\ell=2p\), the law in (6) is supported at
\(\log2\) and \(\log p\), with masses

\[
 \frac{\log2}{\log(2p)},\qquad
 \frac{\log p}{\log(2p)}.
\]

Hence

\[
 \log(2p)\mathrm{Var}_{p_{2p}}(\log d)
 =\frac{\log2\,\log p}{\log(2p)}
  (\log p-\log2)^2
 \gg(\log N)^2.
\]

There are \(\gg N/\log N\) such primes, proving (11).  Equation (12)
follows by partial summation from \(\psi(x)\sim x\).  The ratio of
(11) and (12) tends to infinity, proving the mismatch.  \(\square\)

Consequently the asserted identity

\[
 \langle A_L^+g,g\rangle
 =\mathcal V_L^{\rm sh}(g)+\mathfrak W_L(g,g)
 \tag{13}
\]

does not follow from the divisor-variance identity.  If (13) is adopted as
a definition, then

\[
 \mathfrak W_L(g,g)
 :=\langle A_L^+g,g\rangle-\mathcal V_L^{\rm sh}(g)
 =\mathcal D_{p,N}(g,g)-\mathcal V_L^{\rm sh}(g)
  +\mathcal D_\Gamma(g,g)-\kappa_N\|g\|^2
  +2|\langle h_L,g\rangle|^2
 \tag{14}
\]

contains the negative of an arithmetic divisor covariance.  It is no
longer a Gamma--pole--boundary remainder, and bounding (14) is a coupled
arithmetic theorem rather than Lemma B as stated.

## 3. The literal Gamma--pole--threshold remainder violates Lemma B

The components explicitly listed in Lemma B determine the natural form

\[
 \mathfrak W_L^{\rm nat}(g,g)
 :=\mathcal D_\Gamma(g,g)-\kappa_N\|g\|_2^2
   +2|\langle h_L,g\rangle|^2.
 \tag{15}
\]

### Theorem 2 — Fixed-core obstruction

For every family of normalized even vectors \(q_L^+\), there are
normalized real even functions

\[
 g_L\in C_c^\infty((-1,1)),qquad
 g_L\perp q_L^+,qquad g_L\perp h_L,
 \tag{16}
\]

such that

\[
 \boxed{
 \mathfrak W_L^{\rm nat}(g_L,g_L)
 \le -4\lambda+o(\lambda)+C_E.}
 \tag{17}
\]

In particular, for no fixed \(c_1>0\) can

\[
 \mathfrak W_L^{\rm nat}(g,g)
 \ge-c_1d_8\|g\|_2^2
 \tag{18}
\]

hold on \((q_L^+)^\perp\), because

\[
 d_8\asymp\lambda^{17}e^{-4\pi\lambda^2}\longrightarrow0.
 \tag{19}
\]

#### Proof

Fix any three-dimensional real subspace

\[
 E\subset C_c^\infty((-1,1))^{\rm even}.
\]

For \(L>2\), the restrictions to \(E\) of
\(g\mapsto\langle g,q_L^+\rangle\) and
\(g\mapsto\langle g,h_L\rangle\) are two linear functionals.  Their
common kernel in \(E\) is nonzero.  Choose a unit vector \(g_L\) in that
kernel.  This proves (16).

Put

\[
 K_\Gamma(u)=\frac{e^{-u/2}}{1-e^{-2u}}.
\]

For \(0<u\le1\), translation continuity gives

\[
 \|g-\tau_ug\|_2\le u\|g'\|_2,
 \qquad K_\Gamma(u)\ll u^{-1}.
\]

For \(u\ge1\),

\[
 \|g-\tau_ug\|_2^2\le4\|g\|_2^2,
 \qquad K_\Gamma(u)\ll e^{-u/2}.
\]

Therefore

\[
 \mathcal D_\Gamma(g,g)
 \ll\|g'\|_2^2+\|g\|_2^2.
 \tag{20}
\]

All norms are equivalent on the fixed finite-dimensional space \(E\), so
the right side of (20) is at most one constant \(C_E\) for all the unit
vectors \(g_L\).  The polar term in (15) vanishes by (16).  Equations
(5), (15), and (20) now give (17), which contradicts (18) for large
\(L\).  \(\square\)

The proof already uses zero-extended translations.  Thus the usual
zero-extension boundary contribution is included in (20) and cannot
repair the scale mismatch.

## 4. Correct successor

The failed split must be replaced by one exact coupled statement.  There
are two equivalent valid formulations.

### Operator form

Prove directly that

\[
 \boxed{
 \inf_{\substack{g\perp q_L^+\\g\ {
m even}\\\|g\|=1}}
 \left[
  \mathcal D_{p,N}(g,g)+\mathcal D_\Gamma(g,g)
  +2|\langle h_L,g\rangle|^2-\kappa_N
 \right]
 \ge c_0d_8.}
 \tag{21}
\]

### Exact shorted form

If an arithmetic feature map \(C_L^{\rm ex}\) is desired, it must first
be proved to satisfy an exact decomposition

\[
 \mathcal D_{p,N}(g,g)
 =\|(I-P_L)C_L^{\rm ex}g\|^2
  +\mathcal C_L(g,g)
 \tag{22}
\]

with every weight, boundary term, and compensation term explicit.  The
remaining theorem is then the **joint** inequality

\[
 \boxed{
 \|(I-P_L)C_L^{\rm ex}g\|^2
 +\mathcal C_L(g,g)+\mathcal D_\Gamma(g,g)
 +2|\langle h_L,g\rangle|^2-
 \kappa_N\|g\|^2
 \ge c_0d_8\|g\|^2.}
 \tag{23}
\]

No separate lower bound of size \(-d_8\) for the last four terms is
available: Theorem 2 proves that the scalar threshold must be compensated
by the ordinary-prime energy before any lower estimate is taken.

## 5. Verdict

The proposed Lemma B is not an independent analytic estimate waiting for
a Gamma-kernel proof.

- Under its literal component definition, it is false by Theorem 2.
- Under the tautological definition (14), it contains the negative of the
  unlinked divisor covariance and is not an archimedean--polar lemma.
- The divisor covariance of Paper 40 cannot provide the missing link,
  because Proposition 1 proves that it has the wrong symbol and scale.

The viable target is therefore (21), or an exact compensated version such
as (23).  Prime, Gamma, pole, threshold, and boundary must remain coupled.
