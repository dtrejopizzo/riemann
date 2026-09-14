# P121 -- dyadic radical bootstrap for the compressed Gamma--Euler operator

## Status

This note proves a new regularity theorem for every finite-window
Gamma--Euler eigenvector.  In particular, a hypothetical first-loss radical,
extended by zero, belongs to

\[
        H^s(\mathbb R)\qquad\text{for every }0\leq s<\frac12.       \tag{0.1}
\]

The proof is purely operator-theoretic and uses no sign of the Weil form.
The force-bearing point is the exact boundary commutator of
`log <D>`: it is a pair of exponentially weighted Carleman operators, hence
is bounded below the half-Sobolev transmission threshold.

Equation (0.1) crosses the quarter-Sobolev threshold of
`P121_FRACTIONAL_REGULARITY_GATE.md`, so it puts the radical in the maximal
co-Poisson graph domain.  A fresh audit at the end of this note corrects an
overstatement in that file: graph-domain membership alone is **not** yet the
annular gap-transport theorem (441) of v94 and therefore does not, by itself,
exclude first loss.  The global square is not promoted to proved here.

## 1. The compressed equation on the full line

Fix `T>0`, put `I=(-T,T)` and let

\[
 \chi=\mathbf 1_I,\qquad u=E_TF=\chi u.
\]

Use the Fourier convention

\[
 \widehat u(\tau)=\int_{\mathbb R}u(t)e^{-it\tau}\,dt
\]

and define

\[
 L=\log\langle D\rangle,
 \qquad \ell(\tau)=\frac12\log(1+\tau^2).                       \tag{1.1}
\]

The exact Gamma symbol is

\[
 g_\Gamma(\tau)
 =\operatorname {Re}\psi\left(\frac14+\frac{i\tau}{2}\right)
   -\psi\left(\frac14\right).
\]

The digamma asymptotic at infinity and continuity on the real axis give

\[
                  b_\Gamma:=g_\Gamma-\ell\in L^\infty(\mathbb R). \tag{1.2}
\]

If `F` is in the operator domain of the finite-window Friedrichs operator,
the eigenvalue equation, extended by zero, has the form

\[
 \chi g_\Gamma(D)u
 -m_0u-
 \sum_{2\le n<e^{2T}}w_n\chi
       (\tau_{\log n}+\tau_{-\log n})u
 =f,                                                        \tag{1.3}
\]

where the sum is finite.  For a first-loss vector,

\[
 f=\chi(\alpha e^{-t/2}+\beta e^{t/2}).                     \tag{1.4}
\]

Because `u=chi u`, (1.2)--(1.3) become, on the whole line,

\[
        (L+R_T)u=f,                                          \tag{1.5}
\]

with

\[
\begin{split}
 R_T={}&[\chi,L]\chi+\chi b_\Gamma(D)\chi-m_0I\\
 &-\sum_{2\le n<e^{2T}}w_n\chi
       (\tau_{\log n}+\tau_{-\log n})\chi .                 \tag{1.6}
\end{split}
\]

The point of (1.5) is that its unbounded part is now the translation
invariant multiplier `L`; every boundary and arithmetic term has been
placed in `R_T` without discarding the exterior Gamma leakage.

## 2. The half-Sobolev boundary lemma

### Lemma 2.1 -- characteristic multipliers

For every bounded interval `J` and every `|s|<1/2`, multiplication by
`1_J` is bounded on `H^s(R)`.

#### Proof

For `0<s<1/2`, use the Gagliardo norm.  The only new contribution after
multiplication by `1_J` comes from pairs separated by an endpoint and is
bounded by the one-dimensional fractional Hardy inequality

\[
 \int_J {|v(x)|^2\over \operatorname {dist}(x,\partial J)^{2s}}\,dx
 \le C_{s,J}\|v\|_{H^s(\mathbb R)}^2.
\]

The `L2` term is immediate.  Duality gives `-1/2<s<0`, and `s=0` is
trivial.  QED.

### Lemma 2.2 -- the logarithmic transmission commutator

For `|s|<1/2`, the operator

\[
                 [\chi,L]\chi                              \tag{2.1}
\]

extends boundedly on `H^s(R)`.

#### Proof

Away from the diagonal, the distribution kernel of `L` is

\[
       k(x)=-\frac12\,{e^{-|x|}\over |x|}.                   \tag{2.2}
\]

Indeed `ell'(tau)=tau/(1+tau^2)`; inverse Fourier transformation and one
integration in the distributional variable give (2.2).  A possible
diagonal delta term disappears from the commutator.

If `v=chi v`, then `[chi,L]v` vanishes inside `I`.  On the right exterior,
write `x=T+X`, `y=T-Y`, with `X>0` and `0<Y<2T`.  Up to the harmless factor
`1/2`, the output is

\[
 e^{-X}\int_0^{2T}{e^{-Y}v(T-Y)\over X+Y}\,dY.               \tag{2.3}
\]

The unweighted operator

\[
       (Cv)(X)=\int_0^\infty {v(Y)\over X+Y}\,dY              \tag{2.4}
\]

is a reflected, restricted Hilbert transform: if `Rv` is the reflection of
the zero extension of `v` onto the negative half-line, then

\[
          Cv=\pi\,\mathbf1_{(0,\infty)}H(Rv).                 \tag{2.5}
\]

The Hilbert transform is bounded on every `H^s`; the two half-line
cutoffs in (2.5) are bounded for `|s|<1/2` by Lemma 2.1.  Multiplication by
the exponential weights and the finite-interval cutoff is bounded in the
same range.  Hence (2.3) is bounded on `H^s`.  The left exterior is the
reflection of the same operator.  Their direct sum is (2.1).  QED.

### Corollary 2.3 -- all finite perturbations preserve the scale

For every fixed `T` and every `|s|<1/2`, the operator `R_T` of (1.6) is
bounded on `H^s(R)`.

#### Proof

Lemma 2.2 treats the only unbounded-looking term.  The multiplier
`b_Gamma(D)` is bounded on every `H^s` by (1.2).  Translations are
isometries on `H^s`, multiplication by `chi` is bounded by Lemma 2.1, and
the active arithmetic sum is finite.  QED.

## 3. A radical slope lemma

Let `Pi_0` be Fourier restriction to `|tau|<2`, and for `j>=1` let `Pi_j`
be restriction to

\[
       2^j\le |\tau|<2^{j+1}.
\]

These are mutually orthogonal projections.  Define the dyadic number
operator

\[
             Nu=\sum_{j\ge1}j\Pi_ju.                         \tag{3.1}
\]

Since

\[
 \sup_{\tau\in\mathbb R}
 \left|\ell(\tau)-(\log2)\sum_{j\ge1}j\mathbf1_{
       \{2^j\le|\tau|<2^{j+1}\}}(\tau)\right|<\infty,
                                                                  \tag{3.2}
\]

we have

\[
                   L=(\log2)N+B,                              \tag{3.3}
\]

where `B` is bounded on every `H^s`.

### Lemma 3.1 -- dyadic radical bootstrap

Let `0<s<1/2`.  Suppose `R` is bounded both on `L2(R)` and on `H^s(R)`,
`u in Dom N`, and

\[
                 ((\log2)N+R)u=f                              \tag{3.4}
\]

with `f in H^s`.  Then `u in H^s`.

#### Proof

Choose an integer `J` so large that

\[
 J\log2>2\max\{\|R\|_{L^2\to L^2},
                    \|R\|_{H^s\to H^s}\}.                   \tag{3.5}
\]

Put `P=sum_{j<J}Pi_j` and `Q=I-P`.  The high-frequency part of (3.4) is

\[
 ((\log2)N_Q+QRQ)Qu=Qf-QRPu.                                 \tag{3.6}
\]

The right side belongs to `H^s`: `Pu` has bounded Fourier support and is
therefore in every `H^s`, while `R` preserves `H^s`.  On the high block,

\[
 \|((\log2)N_Q)^{-1}QRQ\|_{H^s\to H^s}<\frac12.              \tag{3.7}
\]

Thus the operator on the left of (3.6) is invertible on `QH^s` by a
Neumann series.  The same argument in `L2` shows that it has a unique `L2`
solution.  The original `Qu` and the `H^s` solution therefore coincide.
Consequently `Qu in H^s`; the low part `Pu` already lies there.  QED.

The lemma is not an elliptic estimate of the invalid form
`1/log <D> : L2 -> H^s`.  It uses the homogeneous/eigenvector equation:
the high block has no independent rough forcing, while the perturbation
preserves the target scale.  This is why the factor `J` in (3.7) can absorb
the perturbation.

## 4. Regularity of every finite-window zero mode

### Theorem 4.1 -- sub-half-Sobolev radical regularity

Let `F` be in the operator domain of the finite-window Gamma--Euler
Friedrichs operator and suppose

\[
 A_TF=\alpha e^{-t/2}+\beta e^{t/2}\quad\text{on }I_T.        \tag{4.1}
\]

Then its zero extension satisfies

\[
            \boxed{E_TF\in H^s(\mathbb R)
                    \quad(0\le s<1/2).}                       \tag{4.2}
\]

#### Proof

The zero extension of the right side of (4.1) belongs to `H^s` for every
`s<1/2` by Lemma 2.1.  Equations (1.5), (3.3) and Corollary 2.3 put the
problem in the form of Lemma 3.1.  Apply that lemma separately for each
fixed `s<1/2`.  QED.

### Corollary 4.2 -- first-loss consequence

Every hypothetical first-loss vector of v94 belongs to `H^s(R)` for every
`s<1/2`.  In particular, choosing

\[
                     \frac14<s<\frac12,                       \tag{4.3}
\]

the convexity bound for zeta gives

\[
 \zeta(1/2+i\tau)\widehat {E_TF}(\tau)\in L^2(\mathbb R).    \tag{4.4}
\]

Thus a first-loss vector belongs to the maximal physical co-Poisson graph
domain.

## 5. Audit of the last arrow

The implication

\[
 \text{first-loss vector in the maximal co-Poisson domain}
 \quad\Longrightarrow\quad F=0                              \tag{5.1}
\]

is not proved in v94.  What v94 proves is:

* graph-domain membership makes the global co-Poisson observation exist;
* the observation already has the natural gap `(0,e^{-T})`;
* exclusion follows if the zero-mode equation amplifies that gap across the
  annulus to `(0,e^T)`, equation (358), or equivalently if the local
  observation vanishes on the annulus, equation (441).

The maximal domain supplies existence, not this extra vanishing.  Hence the
sentence in `P121_FRACTIONAL_REGULARITY_GATE.md` asserting that v94 already
places every nonzero first-loss vector outside that domain is too strong.
The same overstatement appears as item 4 in
`P121_REVERSE_ENGINEERING_AND_ASC_NO_GO.md`.

What is now genuinely closed is the former regularity/domain obstruction:

\[
 \boxed{
 \text{a compressed first-loss radical cannot escape through roughness;
 it is automatically a nuclear graph vector.}}                \tag{5.2}
\]

The remaining obstruction is narrower and of a different type:

\[
 \boxed{
 P_TA_TF=0, F\in\operatorname{Dom}S_T^{\max}
 \quad\Longrightarrow\quad
 \mathfrak S_TF=0\text{ on }(e^{-T},e^T).}                     \tag{5.3}
\]

This is the equality-state annular transport statement.  It may now be
attacked on the closed nuclear graph itself; boundary roughness and lack of
definition of the observation are no longer admissible escape mechanisms.

## 6. Circularity and comparison audit

1. No positivity of `A_T`, except the already proved semidefiniteness at a
   hypothetical first contact, is used to prove (4.2).
2. No square root, Douglas contraction, zero set of zeta, or row-(d) norm is
   defined.
3. The theorem applies to any finite shift perturbation of the compressed
   Gamma operator.  Accordingly it cannot by itself distinguish zeta from a
   Davenport--Heilbronn analogue; the arithmetic discrimination must enter
   in the annular transport step (5.3).
4. The half threshold is structural: the characteristic cutoff and the
   Carleman transmission cease to be bounded on the uncorrected Sobolev
   scale at `s=1/2`.

## 7. Corpus audit

The corpus contains dyadic contact batching, dyadic Bessel estimates,
number operators for the archimedean determinant, and the phase-116 warning
that powers of logarithmic form regularity do not imply one derivative.  It
does not contain the decomposition (1.5), the Carleman commutator lemma
(2.2)--(2.5), the high-block radical lemma 3.1, or conclusion (4.2).

The nearest prior statement is the open boundary bootstrap (341) in v94.
The present theorem does not prove that full translation jet; it proves the
maximal regularity compatible with an uncorrected zero-extension boundary
and removes the graph-domain part of that gate.

