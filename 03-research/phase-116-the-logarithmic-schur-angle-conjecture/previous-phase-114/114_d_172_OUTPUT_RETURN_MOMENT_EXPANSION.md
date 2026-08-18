# D.172 — Output return-moment expansion

## Verdict

The phase-defect Carleson capacity of D.171 is exactly a positive return
series through the old comparison.  Put

\[
 K_N=A_NA_N^*,\qquad D_{\rm out}=I-K_N,\qquad
 c_k(N)=y_N^*K_N^ky_N.                               \tag{0.1}
\]

Then, with the standard range convention,

\[
 \boxed{
 y_N^*D_{\rm out}^\dagger y_N
 =\sum_{k=0}^{\infty}c_k(N).}                        \tag{0.2}
\]

All terms are positive operators on the born-boundary space.  Thus the
new cell is positive exactly when the total energy of all successive
round trips is within the normalized boundary budget.

The spectral layer estimate requested after D.171 follows from decay of
the same moments.  In particular, if

\[
 c_k(N)\le {C_N\over(k+1)(1+\log(k+1))^2}I,          \tag{0.3}
\]

then

\[
 \mu_N^y((0,\delta])
 \ll {C_N\delta\over(1+|\log\delta|)^2}.             \tag{0.4}
\]

Conversely, the output capacity itself is the sum in (0.2), so a proof can
work directly with the return moments without losing a dyadic logarithm.

For the exact A--B--C features,

\[
 \boxed{
 c_k(N)=
 y_N^*\bigl(Y_0R_0^\dagger Y_0^*\bigr)^ky_N,}        \tag{0.5}
\]

where (R_0=X_0^*X_0) contains Gamma and every (J_{p^j,-}), while
(Y_0) contains the Tate/resolvent and every (J_{p^j,+}).  Formula
(0.5), unlike the discarded ambient powers of D.155, inserts the exact
reference inverse between every return.

The Witt multiplication law types the arithmetic part of every return,
but absolute Dirichlet convolution estimates do not prove (0.3): at the
central weight they reproduce a divergent Euler series.  The two Tate
moments must be used at every return to replace the coherent zeta factor by
the centered polynomial (E_N=W_N-M_N).  This is the precise substantive
task left by (0.5).

## 1. Positive Neumann identity

Assume first (0\le K_N<I).  The spectral theorem gives

\[
 (I-K_N)^{-1}=\sum_{k=0}^{\infty}K_N^k              \tag{1.1}
\]

in the strong topology.  Sandwiching (1.1) by (y_N) proves (0.2).
For a merely contractive old cell, let (E_K) be the spectral measure of
(K_N).  Monotone convergence gives

\[
\begin{aligned}
 \sum_{k=0}^{\infty}c_k(N)
 &=\int_{[0,1)}\sum_{k=0}^{\infty}\lambda^k
       \,d(y_N^*E_K(\lambda)y_N)\\
 &=\int_{[0,1)}{1\over1-\lambda}
       \,d(y_N^*E_K(\lambda)y_N).                  \tag{1.2}
\end{aligned}
\]

This equals (y_N^*D_{\rm out}^\dagger y_N) precisely when (y_N)
has no component in (ker D_{\rm out}) and the integral is finite.
Otherwise both sides are infinite in the extended positive cone.  Hence
(0.2) includes, rather than suppresses, the range condition.

There is also an explicit observability factor.  Define

\[
 \mathcal O_Ny=\bigl(y,K_N^{1/2}y,K_Ny,
                     K_N^{3/2}y,\ldots\bigr).        \tag{1.3}
\]

Then

\[
 \|\mathcal O_Ny_Ne\|^2
 =\sum_{k\ge0}\langle e,c_k(N)e\rangle
 =\|D_{\rm out}^{\dagger/2}y_Ne\|^2.                \tag{1.4}
\]

Thus constructing the Douglas factor of D.169 is equivalent to proving
that this observability map is contractive.

## 2. Moments imply spectral-layer bounds

Let

\[
 F_N(\delta)=\mu_N^y((0,\delta])
 =y_N^*E_{D_{\rm out}}((0,\delta])y_N.               \tag{2.1}
\]

On this spectral layer (K_N=I-D_{\rm out}\ge1-\delta).  Therefore

\[
 F_N(\delta)\le(1-\delta)^{-k}c_k(N).                \tag{2.2}
\]

For (0<\delta\le1/2), take (k=\lfloor1/\delta\rfloor).  Since
((1-\delta)^{-k}\le e^2), (0.3) gives (0.4), with an explicit universal
factor (e^2).  This proves the claimed layer implication.

The exact Stieltjes identity is

\[
 y_N^*D_{\rm out}^\dagger y_N
 =F_N(1)+\int_0^1{F_N(t)\over t^2}\,dt,              \tag{2.3}
\]

provided the right side is finite.  It explains why a bare
(F_N(t)=O(t)) loses a logarithm, while (0.4) is integrable.

## 3. Correct A--B--C return formula

D.170 gives

\[
 A_N=Y_0R_0^{\dagger/2},\qquad
 y_N=(Y_E-Y_0R_0^\dagger X_0^*X_E)S_E^{\dagger/2}.   \tag{3.1}
\]

Substitution into (0.1) yields (0.5).  Expanded without abbreviations,

\[
\begin{aligned}
 c_k(N)={}&S_E^{\dagger/2}
 (Y_E-Y_0H)^*\\
 &\quad\cdot
 \bigl(Y_0R_0^\dagger Y_0^*\bigr)^k
 (Y_E-Y_0H)S_E^{\dagger/2}.                          \tag{3.2}
\end{aligned}
\]

Every occurrence of (R_0^\dagger) is the complete old reference
shorting.  Hence (3.2) retains:

* the full Gamma screw at each return;
* the two Tate jets through the common primitive projection;
* every prime power through (J_{p^j,\pm}); and
* the exact collision (nm=N) through the integer-cell Gram.

Replacing (R_0^\dagger) by a scalar gap or deleting the Paley--Wiener
projection changes (3.2) and is not permitted.

## 4. Witt typing and the absolute-value obstruction

On the algebraic Dirichlet labels, one round-trip composition obeys

\[
 \Gamma_m\circ\Gamma_n=\Gamma_{mn},\qquad
 {1\over\sqrt m}{1\over\sqrt n}={1\over\sqrt{mn}}.   \tag{4.1}
\]

Thus a (k)-fold arithmetic word collapses to its product label, and its
coefficient is a Dirichlet convolution.  The exact identity

\[
 {\Lambda(n)\over\sqrt n}
 =\sum_{dm=n}{\mu(d)\over\sqrt d}
             {\log m\over\sqrt m}                   \tag{4.2}
\]

is the finite-label form of
(\(\Lambda=\mu*\log\)).  It suggests a Möbius output channel for the return
series.

However, taking absolute values before the reference inverse produces

\[
 \sum_n{|\mu(n)|\over\sqrt n}=\infty,\qquad
 \sum_n{\Lambda(n)\over\sqrt n}=\infty,              \tag{4.3}
\]

and even square summation gives logarithmically growing critical norms.
Therefore (4.2) alone is not a Douglas factorization through
(D_{\rm out}^{1/2}).  It becomes useful only if the continuous
(log)-channel is identified with the output defect and the two Tate
characters remove its coherent main term at every iterate.

The exact centered return target is consequently

\[
 \boxed{
 c_k(N)\le {C_N\over(k+1)(1+\log(k+1))^2}I,
 \qquad \sum_{k\ge0}c_k(N)\le I,}                   \tag{4.4}
\]

proved from (3.2), not from an unweighted convolution majorant.

## 5. Finite endpoint consequence

If a directed computation splits the output space so that

\[
 K_N\le qI\quad\text{on the safe output complement},\qquad q<1,     \tag{5.1}
\]

then its uncomputed return tail is bounded exactly by

\[
 \sum_{k\ge m}y_N^*K_N^ky_N
 \le {q^m\over1-q}\,y_N^*y_N.                       \tag{5.2}
\]

This is the correctly compressed replacement for the ambient four-moment
route of D.155.  The five endpoint-flat dangerous directions are handled
by a directed finite solve; (5.2) handles the safe complement with its
actual output contraction, rather than a scalar lower gap for the spatial
operator.

The ancillary `114_d_172_output_return_moments_verify.py` checks
(0.2), (1.4), (2.2)--(2.3), the exact Möbius convolution (4.2), and the
geometric tail (5.2) on noncommuting finite matrices.
