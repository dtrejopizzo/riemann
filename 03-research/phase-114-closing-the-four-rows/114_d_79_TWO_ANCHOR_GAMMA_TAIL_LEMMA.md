# D.79 supplement — two-anchor Loewner domination for Gamma energies

## Status

This note proves an exact full-space lower bound for the Gamma tail.  It
does not use a Galerkin projection, a moment constraint, or the sign of the
Weil form.  Its purpose is to retain both the low- and high-frequency mass
of a block of Gamma energies while using only its two endpoint anchors.

For `b>0`, let

\[
 E_b(F)=\int_{\mathbb R}
 {2\xi^2\over b(b^2+\xi^2)}|\widehat F(\xi)|^2\,d\xi .       \tag{1}
\]

The Fourier convention only changes the common Plancherel constant and is
irrelevant for the operator order below.

## Two-anchor lemma

Let `0<B<=b<=C` and put

\[
 \alpha_{B,C}(b)
 ={B^3(C^2-b^2)\over b^3(C^2-B^2)},\qquad
 \beta_{B,C}(b)
 ={C^3(b^2-B^2)\over b^3(C^2-B^2)}.                       \tag{2}
\]

Both coefficients are nonnegative, and

\[
 \boxed{E_b\ \geq\ \alpha_{B,C}(b)E_B+
                    \beta_{B,C}(b)E_C.}                  \tag{3}
\]

At `b=B` and `b=C`, (3) is equality with coefficients `(1,0)` and
`(0,1)`, respectively.

### Proof

Put `x=xi^2`.  The coefficients in (2) are the unique coefficients which
match the multiplier at `x=0` after division by `2x`, and match its leading
term as `x` tends to infinity:

\[
 {1\over b^3}={\alpha\over B^3}+{\beta\over C^3},
 \qquad
 {1\over b}={\alpha\over B}+{\beta\over C}.              \tag{4}
\]

Direct reduction to a common denominator gives

\[
\begin{aligned}
 {1\over b(b^2+x)}
 &-{\alpha\over B(B^2+x)}
  -{\beta\over C(C^2+x)}\\
 &=
 {x(b^2-B^2)(C^2-b^2)
  \over b^3(B^2+x)(b^2+x)(C^2+x)}\geq0.                 \tag{5}
\end{aligned}
\]

Multiplication by `2x>=0` proves the pointwise Fourier-multiplier
inequality, and Plancherel proves (3) on the complete Hilbert space.

## Block consequence

For any finite set `J` with `B<=b<=C` for all `b in J`, summing (3) gives

\[
 \sum_{b\in J}E_b\geq
 \left(\sum_{b\in J}\alpha_{B,C}(b)\right)E_B+
 \left(\sum_{b\in J}\beta_{B,C}(b)\right)E_C.           \tag{6}
\]

No `P--Q` cross term is lost when (6) is inserted before a Feshbach
decomposition.  In contrast with the one-anchor bound

\[
 E_b\geq(B/b)^3E_B,
\]

(3) is sharp at both `x=0` and `x=infinity`.  The only discarded mass is
the explicitly positive rational function (5), which is second order in
the separation from either endpoint.

The symbolic identity and positivity conditions are checked by
`114_d_79_two_anchor_loewner_verify.py`.

