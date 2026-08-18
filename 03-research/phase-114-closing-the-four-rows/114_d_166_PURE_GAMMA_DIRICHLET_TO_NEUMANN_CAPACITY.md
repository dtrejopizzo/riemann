# D.166 — Pure-Gamma Dirichlet-to-Neumann capacity of a born strip

## Verdict

The local Gamma estimate of D.164 survives minimization over **arbitrary
old-core extensions**.  It does not collapse to reciprocal-logarithmic
size.

Let (\Omega\subset\mathbb R) have measure at most (2T), let
(E\subset\Omega) have measure at most (2\ell), and put

\[
 \mathcal H_a(f)={1\over2\pi}\int_{\mathbb R}
 h_a(\tau)|\widehat f(\tau)|^2,d\tau,
 \qquad
 h_a(\tau)=\mathrm{Re}\,\psi(a+i\tau/2)-\psi(a),                \tag{0.1}
\]

where (a=5/4).  Define the pure-Gamma shorted form on the born set by

\[
 q_{E,\Omega}^{\Gamma}(g)=
 \inf\{\mathcal H_a(f):\mathrm{supp}\,f\subset\Omega,
                       \mathbf1_Ef=g\}.              \tag{0.2}
\]

For (0<c_0<\pi/2), set

\[
 a_T=\left(1-{2c_0\over\pi}\right)h_a(c_0/T).        \tag{0.3}
\]

Then for every (R>0),

\[
 \boxed{
 q_{E,\Omega}^{\Gamma}(g)\ge
 \left(
  \sqrt{{2\ell R\over\pi a_T}}+{1\over\sqrt{h_a(R)}}
 \right)^{-2}\|g\|_2^2.}                            \tag{0.4}
\]

The same estimate holds after imposing the two Tate moments, because that
only decreases the class of admissible extensions in (0.2).

On the integer cell of D.164, take

\[
 \ell\le\log(1+1/N),\qquad
 T\le{1\over2}\log(N+1),\qquad
 L=\log(1/\ell),\qquad R={1\over\ell L^4}.            \tag{0.5}
\]

Then the coefficient on the right of (0.4) is

\[
 \boxed{(1-o(1))\log N.}                             \tag{0.6}
\]

Thus the operation of shorting the *pure Gamma form* through the whole old
core preserves leading coefficient one.  This resolves the first
capacity objection to D.164.  It does not by itself close the full
arithmetic short: the old prime-contact synthesis must next be estimated
in the Gamma-resolvent metric, rather than by its unweighted norm alone.

## 1. A global support gap

Let (P_{[-R,R]}) be the Fourier band projection.  The time--band
concentration estimate used in D.164 gives, for a function supported on a
set of measure at most (2T),

\[
 {1\over2\pi}\int_{-c_0/T}^{c_0/T}|\widehat f(\tau)|^2d\tau
 \le {2c_0\over\pi}\|f\|_2^2.                       \tag{1.1}
\]

Since (h_a) is even, nonnegative, and increasing on the positive axis,
discarding the low band yields

\[
 \mathcal H_a(f)\ge a_T\|f\|_2^2.                   \tag{1.2}
\]

This is a support uncertainty gap.  It is independent of the location or
number of connected components of (\Omega).

## 2. Restriction estimate after arbitrary extension

Write (f=f_{<R}+f_{>R}) using the Fourier cutoff at (R).  With the
Plancherel normalization of (0.1), Cauchy--Schwarz gives the pointwise
bound

\[
 |f_{<R}(x)|\le\sqrt{R/\pi}\,\|f\|_2.                \tag{2.1}
\]

Consequently

\[
 \|\mathbf1_Ef_{<R}\|_2
 \le\sqrt{{2\ell R\over\pi}}\,\|f\|_2
 \le\sqrt{{2\ell R\over\pi a_T}}\,
       \mathcal H_a(f)^{1/2}.                         \tag{2.2}
\]

Monotonicity of (h_a) gives independently

\[
 \|\mathbf1_Ef_{>R}\|_2
 \le\|f_{>R}\|_2
 \le {\mathcal H_a(f)^{1/2}\over\sqrt{h_a(R)}}.      \tag{2.3}
\]

The triangle inequality in (2.2)--(2.3) proves

\[
 \|\mathbf1_Ef\|_2
 \le\left(
  \sqrt{{2\ell R\over\pi a_T}}+{1\over\sqrt{h_a(R)}}
 \right)\mathcal H_a(f)^{1/2}.                       \tag{2.4}
\]

Taking the infimum over every extension of a fixed (g) proves (0.4).
In particular, (0.4) is already a Dirichlet-to-Neumann/Schur estimate; it
is not merely coercivity for functions supported on (E).

## 3. Integer-cell asymptotics

The Taylor expansion at zero and the digamma asymptotic at infinity are

\[
 h_a(x)=-{\psi''(a)\over8}x^2+O_a(x^4),\qquad
 h_a(x)=\log x+O_a(1).                                \tag{3.1}
\]

Since (-\psi''(a)>0), (0.3) and (T\asymp\log N) imply

\[
 a_T\asymp(\log N)^{-2}.                             \tag{3.2}
\]

For the choice (0.5),

\[
 {2\ell R\over\pi a_T}=O(L^{-2}),                   \tag{3.3}
\]

whereas

\[
 h_a(R)=L-4\log L+O_a(1).                            \tag{3.4}
\]

The first term inside the parentheses in (0.4) is (O(L^{-1})),
and the second is (L^{-1/2}(1+o(1))).  Squaring and inverting proves

\[
 q_{E,\Omega}^{\Gamma}(g)
 \ge L(1-o(1))\|g\|_2^2
 =(1-o(1))\log N\,\|g\|_2^2,                        \tag{3.5}
\]

which is (0.6).

## 4. Correct next comparison

The exact old-contact boundary synthesis of D.164 satisfies

\[
 \|\mathcal B_N\|^2=V_N+H_N
 ={1\over2}(\log N)^2+o((\log N)^2).                 \tag{4.1}
\]

The object entering a Schur complement is not
(\|\mathcal B_N\|) by itself, but

\[
 \boxed{
 \mathcal B_N^*(A_N^{\rm core})^\dagger\mathcal B_N,} \tag{4.2}
\]

where (A_N^{\rm core}) is the already assembled primitive core form.
Replacing (4.2) by
((V_N+H_N)/\inf\sigma(A_N^{\rm core})) destroys the translation and
Gamma structure and is too coarse.  The remaining asymptotic task is the
weighted large-sieve/resolvent estimate

\[
 \mathcal B_N^*(A_N^{\rm core})^\dagger\mathcal B_N
 \le\left({1\over2}+o(1)\right)\log N\,I.            \tag{4.3}
\]

Together with (3.5), (4.3) would leave a positive leading margin
((1/2-o(1))\log N).  Equation (4.3), not the pure-Gamma capacity, is now
the precise unresolved asymptotic estimate.

The ancillary `114_d_166_gamma_dtn_capacity_verify.py` checks the
finite-frequency decomposition algebra and records the quantitative lower
bound from (0.4) along the integer-cell scaling.  Its numerical output is
an audit of the explicit bound; the proof is (1.1)--(3.5).
